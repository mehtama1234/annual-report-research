#!/usr/bin/env python3
"""Verify Eaton FY2025 GAAP denominators used by the research dossier."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "industrial-goods/industrial-electrical-equipment/eaton-corporation"
EXPECTED = {
    "RevenueFromContractWithCustomerExcludingAssessedTax": 27_448_000_000,
    "NetIncomeLoss": 4_087_000_000,
    "NetCashProvidedByUsedInOperatingActivities": 4_472_000_000,
    "PaymentsToAcquirePropertyPlantAndEquipment": 919_000_000,
    "PaymentsToAcquireBusinessesNetOfCashAcquired": 1_490_000_000,
    "PaymentsForRepurchaseOfCommonStock": 1_862_000_000,
    "DividendsCommonStockCash": 1_628_000_000,
    "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents": 622_000_000,
    "LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities": 9_894_000_000,
    "ReceivablesNetCurrent": 5_387_000_000,
    "InventoryNet": 4_721_000_000,
    "StockIssuedDuringPeriodValueShareBasedCompensation": 106_000_000,
    "Goodwill": 15_769_000_000,
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
    print("eaton ok", actual)
    print("eaton-filing-denominators-ok")


if __name__ == "__main__":
    main()
