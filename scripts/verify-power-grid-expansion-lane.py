#!/usr/bin/env python3
"""Verify the first next-cycle power-grid cash lane and its hard boundary."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "company-first-principles"
CHASE_MD = ANALYSIS / "capital-flow-fpl-billing-determinant-category-receipt-proof-chase-pass-1.md"
CHASE_CSV = ANALYSIS / "data" / "capital-flow-fpl-billing-determinant-category-receipt-proof-chase-pass-1.csv"
EXPANSION_MD = ANALYSIS / "combined-investment-research-next-cycle-candidate-expansion-2026-09-16.md"
EXPANSION_CSV = ANALYSIS / "data" / "combined-investment-research-next-cycle-candidate-expansion-2026-09-16.csv"
POWER_GRID_MD = ANALYSIS / "capital-flow-power-grid-pilot-answer-synthesis-pass-2.md"
FPL_REFRESH_MD = ANALYSIS / "capital-flow-fpl-distribution-inspection-official-psc-source-refresh-2026-09-16.md"

REQUIRED_LOCAL_SOURCES = (
    ROOT / "raw/primary-sources/capital-flow/power-grid-pilot/nextera/fpl-rate-case/fpl-2025-sppcrc-actual-estimated-projection.pdf",
    ROOT / "raw/primary-sources/capital-flow/power-grid-pilot/nextera/fpl-rate-case/final-trueup-2025/fpl-2025-sppcrc-final-trueup-epperson-01940-2026.pdf",
    ROOT / "raw/primary-sources/capital-flow/power-grid-pilot/nextera/fpl-rate-case/factor-order-2026/fpl-2026-sppcrc-factor-order-psc-2025-0439.pdf",
    ROOT / "raw/primary-sources/capital-flow/power-grid-pilot/nextera/fpl-rate-case/current-sppcrc-2026/fpl-2026-sppcrc-epperson-factor-workpapers-02560-2026.pdf",
    ROOT / "raw/primary-sources/capital-flow/power-grid-pilot/nextera/fpl-rate-case/amended-factor-2026/fpl-2026-sppcrc-amended-form-4p-5p-03227-2026.pdf",
)


def require_file(path: Path) -> None:
    if not path.is_file():
        raise SystemExit(f"FAIL: missing power-grid lane artifact: {path.relative_to(ROOT)}")


def main() -> int:
    for path in (CHASE_MD, CHASE_CSV, EXPANSION_MD, EXPANSION_CSV, POWER_GRID_MD, FPL_REFRESH_MD, *REQUIRED_LOCAL_SOURCES):
        require_file(path)

    chase_text = CHASE_MD.read_text(encoding="utf-8")
    for marker in (
        "No full upgrade yet",
        "Distribution Inspection",
        "billing determinants",
        "Category customer receipts",
        "fpl-billing-determinant-category-receipt-proof-chase-hold",
    ):
        if marker not in chase_text:
            raise SystemExit(f"FAIL: FPL chase boundary marker missing: {marker}")

    with CHASE_CSV.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    expected_ids = {f"CFFPLBDCR-{index:03d}" for index in range(1, 10)}
    if {row["chase_id"] for row in rows} != expected_ids:
        raise SystemExit("FAIL: FPL chase must contain exactly nine declared proof gates")
    if not any(row["current_status"] == "category-receipt-hold" for row in rows):
        raise SystemExit("FAIL: FPL chase lost the category-receipt hold boundary")
    if not any(row["proof_gate"] == "billing_determinants_search_result" for row in rows):
        raise SystemExit("FAIL: FPL chase lost the billing-determinants search result")

    expansion_text = EXPANSION_MD.read_text(encoding="utf-8")
    for marker in (
        "First lane already underway",
        "hold-with-strong-route-visible",
        "FPL Distribution Inspection category recovery",
        "AEP large-load customer obligations",
    ):
        if marker not in expansion_text:
            raise SystemExit(f"FAIL: next-cycle expansion marker missing: {marker}")
    if "Duke" not in expansion_text or "secured-ESA/project recovery" not in expansion_text:
        raise SystemExit("FAIL: next-cycle expansion lost the Duke secured-ESA/project recovery route")

    refresh_text = FPL_REFRESH_MD.read_text(encoding="utf-8")
    for marker in ("02711-2025.pdf", "13931-2025/13931-2025.pdf", "02559-2026/02559-2026.pdf", "180,000", "$92.1M", "evidence-insufficient", "category-specific cash", "2025 final-true-up petition", "searched-negative for those specific public packet"):
        if marker not in refresh_text:
            raise SystemExit(f"FAIL: FPL official PSC refresh marker missing: {marker}")

    with EXPANSION_CSV.open(newline="", encoding="utf-8") as handle:
        expansion_rows = list(csv.DictReader(handle))
    if [row["priority"] for row in expansion_rows] != ["1", "2", "3"]:
        raise SystemExit("FAIL: next-cycle candidate priorities must be 1, 2, 3")
    if expansion_rows[0]["lane"] != "power_grid_customer_cash":
        raise SystemExit("FAIL: power-grid customer cash must remain the first lane")

    power_grid_text = POWER_GRID_MD.read_text(encoding="utf-8")
    if "full project-return proof" not in power_grid_text or "Claims Not To Make Yet" not in power_grid_text:
        raise SystemExit("FAIL: power-grid answer synthesis lost its proof boundary")

    print("Power-grid expansion lane verification passed: FPL receipt boundary and next-cycle sequencing checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
