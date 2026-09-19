#!/usr/bin/env python3
"""Verify the expansion-lane QoE and financial-shenanigans overlay."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "company-first-principles"
MEMO = ANALYSIS / "combined-investment-research-expansion-lane-qoe-overlay-2026-09-16.md"
TABLE = ANALYSIS / "data" / "combined-investment-research-expansion-lane-qoe-overlay-2026-09-16.csv"


def main() -> int:
    for path in (MEMO, TABLE):
        if not path.is_file():
            raise SystemExit(f"FAIL: missing expansion-lane QoE artifact: {path.relative_to(ROOT)}")

    text = MEMO.read_text(encoding="utf-8")
    for marker in (
        "not a fraud score",
        "Power-grid customer cash",
        "Insurance statutory named-asset income",
        "Asset-backed collateral and borrowing base",
        "An unusual ratio alone is never a manipulation conclusion",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: expansion-lane QoE marker missing: {marker}")

    with TABLE.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 12:
        raise SystemExit(f"FAIL: expected 12 expansion-lane QoE rows, found {len(rows)}")
    expected_lanes = {
        "power_grid_customer_cash",
        "insurance_statutory_named_asset",
        "asset_backed_collateral_and_borrowing_base",
    }
    if {row["lane"] for row in rows} != expected_lanes:
        raise SystemExit("FAIL: QoE overlay must cover exactly the three expansion lanes")
    if not all(row["evidence_status"] in {"observed", "partial", "searched-negative", "not-assembled", "missing"} for row in rows):
        raise SystemExit("FAIL: invalid evidence status in expansion-lane QoE register")
    if not all(row["next_required_source"].strip() and row["do_not_infer"].strip() for row in rows):
        raise SystemExit("FAIL: every QoE row must name a next source and non-inference boundary")

    print("Expansion-lane QoE overlay verification passed: 12 diagnostics across three lanes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
