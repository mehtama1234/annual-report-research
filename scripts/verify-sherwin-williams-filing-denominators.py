#!/usr/bin/env python3
"""Verify FY2025 filing facts for Sherwin-Williams' coatings/control-point model."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "basic-materials/specialty-chemicals/the-sherwin-williams-company"
EXPECTED = {
    "RevenueFromContractWithCustomerExcludingAssessedTax": 23_574_300_000,
    "NetIncomeLoss": 2_568_500_000,
    "NetCashProvidedByUsedInOperatingActivities": 3_451_600_000,
    "PaymentsToAcquireBusinessesNetOfCashAcquired": 1_211_300_000,
    "DividendsCash": 789_800_000,
    "PaymentsForRepurchaseOfEquity": 1_656_400_000,
    "ShareBasedCompensation": 123_500_000,
    "CashAndCashEquivalentsAtCarryingValue": 207_200_000,
    "LongTermDebt": 9_670_800_000,
}


def fy2025_value(facts: dict, tag: str) -> int:
    rows = []
    for unit_rows in facts["facts"]["us-gaap"][tag]["units"].values():
        rows.extend(
            row for row in unit_rows
            if row.get("fy") == 2025 and row.get("fp") == "FY" and row.get("form") == "10-K"
        )
    if not rows:
        raise AssertionError(f"missing FY2025 fact: {tag}")
    return rows[-1]["val"]


def main() -> None:
    base = ROOT / "raw/sec" / BASE
    filing = base / "2025-10k.html"
    facts_path = ROOT / "raw/sec/companyfacts" / BASE / "companyfacts.json"
    if not filing.exists() or filing.stat().st_size < 100_000:
        raise AssertionError(f"missing annual filing: {filing}")
    facts = json.loads(facts_path.read_text())
    actual = {tag: fy2025_value(facts, tag) for tag in EXPECTED}
    if actual != EXPECTED:
        raise AssertionError(f"Sherwin-Williams: expected {EXPECTED}, got {actual}")
    print("the-sherwin-williams-company ok", actual)
    print("sherwin-williams-filing-denominators-ok")


if __name__ == "__main__":
    main()
