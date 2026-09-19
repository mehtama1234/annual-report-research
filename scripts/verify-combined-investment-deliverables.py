#!/usr/bin/env python3
"""Verify the mature-system deliverables named by the combined research goal."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "analysis" / "company-first-principles" / "data" / "combined-investment-research-deliverable-audit.csv"
EXPECTED = [
    "deliverable_id", "deliverable", "status", "authoritative_artifact",
    "boundary_or_gap", "verification",
]
ALLOWED = {"usable", "qualified", "partial", "checked"}
REQUIRED_CHECKS = (
    "scripts/verify-combined-investment-pilots.py",
    "scripts/verify-combined-investment-deliverables.py",
    "scripts/verify-reader-routes.py",
    "scripts/check-internal-links.py",
    "scripts/check-reader-browser.mjs",
    "scripts/check-apollo-q2-fund-distribution-route.py",
    "scripts/check-tjx-forward-capex-category.py",
    "scripts/verify-power-grid-expansion-lane.py",
    "scripts/verify-insurance-statutory-expansion-lane.py",
    "scripts/verify-asset-backed-expansion-lane.py",
    "scripts/verify-expansion-lane-qoe-overlay.py",
    "scripts/verify-combined-investment-completion-audit.py",
    "scripts/verify-integrated-oil-gas-q2-2026-cash-quality-refresh.py",
    "scripts/verify-q2-2026-cross-sector-cash-quality-control-panel.py",
    "scripts/verify-q2-2026-valuation-liquidity-stress-matrix.py",
    "scripts/verify-wheaton-antamina-q03-metal-credit-receipt-boundary.py",
    "scripts/verify-q10-current-six-lane-macro-overlay.py",
    "scripts/verify-q2-2026-qoe-financial-shenanigans-panel.py",
    "scripts/verify-annual-report-undercovered-theme-synthesis.py",
    "scripts/verify-wheaton-antamina-q03-receivable-classification-boundary.py",
    "scripts/verify-uri-abl-collateral-eligibility-bridge.py",
    "scripts/verify-pbf-redemption-settlement-bridge.py",
    "scripts/verify-ares-frontline-primary-source-refresh.py",
    "scripts/verify-pbf-september-2026-conditional-redemption.py",
    "scripts/verify-insurance-brokers-carrier-q2-2026-cash-quality-refresh.py",
    "scripts/verify-exchange-information-infrastructure-q2-2026-cash-quality-refresh.py",
    "scripts/verify-materials-chemicals-steel-q2-2026-cash-quality-refresh.py",
    "scripts/verify-digital-real-estate-q2-2026-cash-quality-refresh.py",
    "scripts/verify-healthcare-distribution-current-period-synthesis.py",
    "scripts/verify-combined-investment-promotion-gate-execution-ledger.py",
    "scripts/verify-retail-tjx-q2-2026-settlement-capex-boundary.py",
    "scripts/verify-uri-q2-2026-availability-lifecycle-boundary.py",
    "scripts/verify-retail-target-q2-2026-cash-quality-boundary.py",
    "scripts/verify-retail-walmart-q2-fy27-capex-refund-boundary.py",
)


def resolve(raw: str) -> Path:
    path = Path(raw)
    return path if path.is_absolute() else ROOT / path


def main() -> int:
    if not AUDIT.is_file():
        raise SystemExit(f"FAIL: missing {AUDIT.relative_to(ROOT)}")
    with AUDIT.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != EXPECTED:
            raise SystemExit(f"FAIL: deliverable audit header mismatch: {reader.fieldnames}")
        rows = list(reader)
    if len(rows) != 98:
        raise SystemExit(f"FAIL: expected 98 deliverables, found {len(rows)}")
    by_id = {row["deliverable_id"]: row for row in rows}
    expected_browser_record = "analysis/company-first-principles/combined-investment-research-reader-browser-review-2026-09-17.md"
    if by_id.get("D-16", {}).get("authoritative_artifact") != expected_browser_record:
        raise SystemExit("FAIL: D-16 must point to the dated reader browser-review record")
    expected_candidate_record = "analysis/company-first-principles/combined-investment-research-next-cycle-candidate-expansion-2026-09-16.md"
    if by_id.get("D-18", {}).get("authoritative_artifact") != expected_candidate_record:
        raise SystemExit("FAIL: D-18 must point to the next-cycle candidate-expansion memo")
    expected_insurance_record = "analysis/company-first-principles/capital-flow-insurance-statutory-named-asset-income-next-dig-pass-1.md"
    if by_id.get("D-19", {}).get("authoritative_artifact") != expected_insurance_record:
        raise SystemExit("FAIL: D-19 must point to the insurance statutory named-asset memo")
    expected_asset_backed_record = "analysis/company-first-principles/capital-flow-uri-borrowing-base-collateral-availability-proof-chase-pass-1.md"
    if by_id.get("D-20", {}).get("authoritative_artifact") != expected_asset_backed_record:
        raise SystemExit("FAIL: D-20 must point to the asset-backed collateral proof chase")
    expected_qoe_record = "analysis/company-first-principles/combined-investment-research-expansion-lane-qoe-overlay-2026-09-16.md"
    if by_id.get("D-21", {}).get("authoritative_artifact") != expected_qoe_record:
        raise SystemExit("FAIL: D-21 must point to the expansion-lane QoE overlay")
    expected_fpl_record = "analysis/company-first-principles/capital-flow-fpl-distribution-inspection-official-psc-source-refresh-2026-09-16.md"
    if by_id.get("D-22", {}).get("authoritative_artifact") != expected_fpl_record:
        raise SystemExit("FAIL: D-22 must point to the official FPL PSC source refresh")
    expected_mf1_record = "analysis/company-first-principles/capital-flow-apollo-athene-mf1-public-sec-document-refresh-2026-09-16.md"
    if by_id.get("D-23", {}).get("authoritative_artifact") != expected_mf1_record:
        raise SystemExit("FAIL: D-23 must point to the MF1 public SEC document refresh")
    ids = set()
    for row_number, row in enumerate(rows, start=2):
        if row["deliverable_id"] in ids:
            raise SystemExit(f"FAIL: duplicate deliverable id at row {row_number}")
        ids.add(row["deliverable_id"])
        if row["status"] not in ALLOWED:
            raise SystemExit(f"FAIL: invalid status at row {row_number}: {row['status']}")
        for field in ("deliverable", "authoritative_artifact", "boundary_or_gap", "verification"):
            if not row[field].strip():
                raise SystemExit(f"FAIL: empty {field} at row {row_number}")
        artifact = resolve(row["authoritative_artifact"])
        if not artifact.exists():
            raise SystemExit(f"FAIL: missing artifact at row {row_number}: {row['authoritative_artifact']}")
    for relative in REQUIRED_CHECKS:
        checker = ROOT / relative
        if not checker.is_file():
            raise SystemExit(f"FAIL: missing reusable verification control: {relative}")
    print(f"Combined investment deliverable audit passed: {len(rows)} deliverables, boundaries recorded")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
