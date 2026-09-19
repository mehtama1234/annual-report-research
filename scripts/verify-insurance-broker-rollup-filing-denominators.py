#!/usr/bin/env python3
"""Verify FY2025 filing facts for Gallagher's acquisition-heavy broker model."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "financial/insurance-brokers/arthur-j-gallagher-co"
EXPECTED = {
    "RevenueFromContractWithCustomerExcludingAssessedTax": 13_942_000_000,
    "NetCashProvidedByUsedInOperatingActivities": 1_930_000_000,
    "PaymentsOfDividendsCommonStock": 667_000_000,
    "ShareBasedCompensation": 49_000_000,
    "LongTermDebt": 12_873_000_000,
    "GoodwillAcquiredDuringPeriod": 9_904_000_000,
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
        raise AssertionError(f"Gallagher: expected {EXPECTED}, got {actual}")
    print("arthur-j-gallagher-co ok", actual)
    print("insurance-broker-rollup-filing-denominators-ok")


if __name__ == "__main__":
    main()
