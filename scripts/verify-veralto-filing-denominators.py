#!/usr/bin/env python3
"""Verify Veralto FY2025 GAAP denominators."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "industrial-goods/pollution-treatment-controls/veralto-corporation"
EXPECTED = {
    "RevenueFromContractWithCustomerExcludingAssessedTax": 5_503_000_000,
    "NetIncomeLoss": 940_000_000,
    "NetCashProvidedByUsedInOperatingActivities": 1_077_000_000,
    "PaymentsToAcquirePropertyPlantAndEquipment": 63_000_000,
    "PaymentsOfDividends": 109_000_000,
    "CashAndCashEquivalentsAtCarryingValue": 2_031_000_000,
    "LongTermDebt": 2_673_000_000,
    "LongTermDebtCurrent": 700_000_000,
    "AccountsReceivableNetCurrent": 897_000_000,
    "InventoryNet": 307_000_000,
    "ShareBasedCompensation": 74_000_000,
    "Goodwill": 2_838_000_000,
}

def fy2025_value(facts, tag):
    rows = []
    for units in facts["facts"]["us-gaap"][tag]["units"].values():
        rows.extend(r for r in units if r.get("fy") == 2025 and r.get("fp") == "FY" and r.get("form") == "10-K")
    if not rows:
        raise AssertionError(f"missing FY2025 fact: {tag}")
    return rows[-1]["val"]

def main():
    filing = ROOT / "raw/sec" / BASE / "2025-10k.html"
    facts_path = ROOT / "raw/sec/companyfacts" / BASE / "companyfacts.json"
    if not filing.exists() or filing.stat().st_size < 100_000:
        raise AssertionError(f"missing annual filing: {filing}")
    facts = json.loads(facts_path.read_text())
    actual = {tag: fy2025_value(facts, tag) for tag in EXPECTED}
    if actual != EXPECTED:
        raise AssertionError(f"expected {EXPECTED}, got {actual}")
    print("veralto ok", actual)
    print("veralto-filing-denominators-ok")

if __name__ == "__main__":
    main()
