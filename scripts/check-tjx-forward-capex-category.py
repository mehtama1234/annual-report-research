#!/usr/bin/env python3
"""Check the TJX FY2027 forward-capex category arithmetic."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "analysis/company-first-principles/data/combined-investment-research-pilot-02-tjx-forward-capex-category-boundary-2026-09-15.csv"


def main() -> int:
    with SOURCE.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    expected = {"Store renovations": 1000, "Offices and distribution centers including IT systems": 992, "New stores": 222, "Named-category sum": 2214}
    if len(rows) != 4:
        raise SystemExit(f"FAIL: expected four TJX forward-capex rows, found {len(rows)}")
    by_category = {row["category"]: row for row in rows}
    if set(by_category) != set(expected):
        raise SystemExit(f"FAIL: TJX forward-capex categories changed: {sorted(by_category)}")
    for category, amount in expected.items():
        if by_category[category]["amount_musd"] != str(amount):
            raise SystemExit(f"FAIL: TJX forward-capex amount changed: {category}")
    named_sum = sum(expected[category] for category in ("Store renovations", "Offices and distribution centers including IT systems", "New stores"))
    if named_sum != expected["Named-category sum"]:
        raise SystemExit("FAIL: TJX forward-capex category arithmetic failed")
    print("TJX FY2027 forward-capex category check passed: $2,214M named-category sum")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
