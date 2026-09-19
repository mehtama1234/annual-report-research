#!/usr/bin/env python3
"""Verify the asset-backed collateral expansion lane and its certificate boundary."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "company-first-principles"
CHASE_MD = ANALYSIS / "capital-flow-uri-borrowing-base-collateral-availability-proof-chase-pass-1.md"
CHASE_CSV = ANALYSIS / "data" / "capital-flow-uri-borrowing-base-collateral-availability-proof-chase-pass-1.csv"
RETURN_MD = ANALYSIS / "capital-flow-uri-collateral-fleet-return-bridge-pass-1.md"
DEFINITIONS_MD = ANALYSIS / "capital-flow-uri-abl-borrowing-base-definitions-pass-1.md"
EXPANSION_MD = ANALYSIS / "combined-investment-research-next-cycle-candidate-expansion-2026-09-16.md"


def require_file(path: Path) -> None:
    if not path.is_file():
        raise SystemExit(f"FAIL: missing asset-backed lane artifact: {path.relative_to(ROOT)}")


def main() -> int:
    for path in (CHASE_MD, CHASE_CSV, RETURN_MD, DEFINITIONS_MD, EXPANSION_MD):
        require_file(path)

    chase_text = CHASE_MD.read_text(encoding="utf-8")
    for marker in (
        "No full upgrade yet",
        "populated borrowing-base certificate",
        "Combined Borrowing Base",
        "Upgrade Test",
        "uri-borrowing-base-collateral-availability-proof-chase-hold",
    ):
        if marker not in chase_text:
            raise SystemExit(f"FAIL: URI collateral boundary marker missing: {marker}")

    with CHASE_CSV.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    expected_ids = {f"CFURIBBCA-{index:03d}" for index in range(1, 14)}
    if {row["chase_id"] for row in rows} != expected_ids:
        raise SystemExit("FAIL: URI collateral chase must contain exactly thirteen declared proof gates")
    if not any(row["current_status"] == "certificate-hold" for row in rows):
        raise SystemExit("FAIL: URI chase lost the populated-certificate hold boundary")
    if not any(row["proof_gate"] == "ar_securitization_collateral_pool" for row in rows):
        raise SystemExit("FAIL: URI chase lost the AR collateral-pool control")

    return_text = RETURN_MD.read_text(encoding="utf-8")
    definitions_text = DEFINITIONS_MD.read_text(encoding="utf-8")
    for marker in ("collateral-return-proof-hold", "source-to-purchase allocation", "lifecycle ROIC"):
        if marker not in return_text:
            raise SystemExit(f"FAIL: URI return boundary marker missing: {marker}")
    for marker in ("85% net orderly liquidation value", "recurring Borrowing Base Certificates", "reserve adjustments"):
        if marker not in definitions_text:
            raise SystemExit(f"FAIL: URI ABL formula marker missing: {marker}")

    expansion_text = EXPANSION_MD.read_text(encoding="utf-8")
    if "Asset-backed collateral and borrowing base" not in expansion_text:
        raise SystemExit("FAIL: next-cycle expansion lost the asset-backed lane")
    if "United Rentals" not in expansion_text or "eligible collateral" not in expansion_text:
        raise SystemExit("FAIL: next-cycle expansion lost the URI collateral route")

    print("Asset-backed expansion lane verification passed: URI collateral and borrowing-base boundaries checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
