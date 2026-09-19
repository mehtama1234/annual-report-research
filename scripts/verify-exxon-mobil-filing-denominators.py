#!/usr/bin/env python3
"""Verify ExxonMobil FY2025 GAAP denominators."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "basic-materials/major-integrated-oil-gas/exxon-mobil-corporation"
EXPECTED = {
    "Revenues": 332_238_000_000,
    "NetIncomeLoss": 28_844_000_000,
    "NetCashProvidedByUsedInOperatingActivities": 51_970_000_000,
    "PaymentsToAcquirePropertyPlantAndEquipment": 28_358_000_000,
    "PaymentsForRepurchaseOfCommonStock": 20_273_000_000,
    "PaymentsOfDividendsCommonStock": 17_231_000_000,
    "CashAndCashEquivalentsAtCarryingValue": 10_681_000_000,
    "LongTermDebtAndCapitalLeaseObligations": 34_241_000_000,
    "DebtCurrent": 9_296_000_000,
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
    print("exxon-mobil ok", actual)
    print("exxon-mobil-filing-denominators-ok")

if __name__ == "__main__":
    main()
