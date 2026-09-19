#!/usr/bin/env python3
"""Verify Nucor FY2025 GAAP denominators."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "basic-materials/steel-iron/nucor-corporation"
EXPECTED = {
    "RevenueFromContractWithCustomerExcludingAssessedTax": 32_494_000_000,
    "NetIncomeLoss": 1_744_000_000,
    "NetCashProvidedByUsedInOperatingActivities": 3_234_000_000,
    "PaymentsToAcquirePropertyPlantAndEquipment": 3_422_000_000,
    "PaymentsToAcquireBusinessesNetOfCashAcquired": 2_000_000,
    "PaymentsForRepurchaseOfCommonStock": 700_000_000,
    "PaymentsOfDividendsCommonStock": 512_000_000,
    "CashAndCashEquivalentsAtCarryingValue": 2_260_000_000,
    "LongTermDebtAndCapitalLeaseObligations": 6_909_000_000,
    "AccountsReceivableNetCurrent": 3_105_000_000,
    "InventoryNet": 5_462_000_000,
    "ShareBasedCompensation": 133_000_000,
    "Goodwill": 4_297_000_000,
}

def fy2025_value(facts, tag):
    rows = []
    for units in facts["facts"]["us-gaap"][tag]["units"].values():
        rows.extend(r for r in units if r.get("fy") == 2025 and r.get("fp") == "FY" and r.get("form") == "10-K" and r.get("end", "2025-12-31") == "2025-12-31")
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
    print("nucor ok", actual)
    print("nucor-filing-denominators-ok")

if __name__ == "__main__":
    main()
