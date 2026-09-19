#!/usr/bin/env python3
"""Verify FY2025 filing facts for S&P Global's information-infrastructure model."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "financial/investment-brokerage-national/sp-global-inc"
EXPECTED = {
    "RevenueFromContractWithCustomerExcludingAssessedTax": 15_336_000_000,
    "NetIncomeLoss": 4_471_000_000,
    "NetCashProvidedByUsedInOperatingActivities": 5_651_000_000,
    "PaymentsToAcquireBusinessesNetOfCashAcquired": 2_023_000_000,
    "PaymentsForRepurchaseOfCommonStock": 5_001_000_000,
    "PaymentsOfDividendsCommonStock": 1_170_000_000,
    "PaymentsOfDividendsMinorityInterest": 321_000_000,
    "ShareBasedCompensation": 236_000_000,
    "CashAndCashEquivalentsAtCarryingValue": 1_745_000_000,
    "LongTermDebt": 13_088_000_000,
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
        raise AssertionError(f"S&P Global: expected {EXPECTED}, got {actual}")
    print("sp-global-inc ok", actual)
    print("sp-global-filing-denominators-ok")


if __name__ == "__main__":
    main()
