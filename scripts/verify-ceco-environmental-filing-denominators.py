#!/usr/bin/env python3
"""Verify CECO Environmental FY2025 GAAP denominators."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "industrials/pollution-treatment-controls/ceco-environmental-corp"
EXPECTED = {
    "RevenueFromContractWithCustomerExcludingAssessedTax": 774_381_000,
    "NetIncomeLoss": 50_051_000,
    "NetCashProvidedByUsedInOperatingActivities": 5_861_000,
    "PaymentsToAcquirePropertyPlantAndEquipment": 11_343_000,
    "CashAndCashEquivalentsAtCarryingValue": 33_144_000,
    "LongTermDebt": 212_438_000,
    "LongTermDebtCurrent": 1_879_000,
    "AccountsReceivableNetCurrent": 172_909_000,
    "InventoryNet": 53_996_000,
    "ShareBasedCompensation": 13_105_000,
    "Goodwill": 288_163_000,
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
    print("ceco-environmental ok", actual)
    print("ceco-environmental-filing-denominators-ok")

if __name__ == "__main__":
    main()
