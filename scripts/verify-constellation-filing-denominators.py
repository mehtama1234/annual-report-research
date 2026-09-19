#!/usr/bin/env python3
"""Verify Constellation Energy FY2025 GAAP denominators."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "utilities/diversified-utilities/constellation-energy-corporation"
EXPECTED = {
    "Revenues": 25_533_000_000,
    "NetIncomeLoss": 2_319_000_000,
    "NetCashProvidedByUsedInOperatingActivities": 4_237_000_000,
    "PaymentsToAcquirePropertyPlantAndEquipment": 2_949_000_000,
    "PaymentsToAcquireBusinessesNetOfCashAcquired": 14_000_000,
    "PaymentsForRepurchaseOfCommonStock": 400_000_000,
    "DividendsCommonStock": 486_000_000,
    "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents": 3_748_000_000,
    "DebtAndCapitalLeaseObligations": 7_250_000_000,
    "AccountsReceivableNetCurrent": 4_266_000_000,
    "InventoryNet": 1_736_000_000,
    "AllocatedShareBasedCompensationExpense": 385_000_000,
    "Goodwill": 420_000_000,
    "SpentNuclearFuelObligationNoncurrent": 1_426_000_000,
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
    print("constellation ok", actual)
    print("constellation-filing-denominators-ok")


if __name__ == "__main__":
    main()
