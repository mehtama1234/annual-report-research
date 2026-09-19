#!/usr/bin/env python3
"""Verify Cummins FY2025 GAAP denominators used by the research dossier."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "industrial-goods/farm-construction-machinery/cummins-inc"
EXPECTED = {
    "Revenues": 33_670_000_000,
    "NetIncomeLossAvailableToCommonStockholdersBasic": 2_843_000_000,
    "NetIncomeLossAttributableToNoncontrollingInterest": 114_000_000,
    "NetCashProvidedByUsedInOperatingActivities": 3_621_000_000,
    "PaymentsToAcquirePropertyPlantAndEquipment": 1_235_000_000,
    "PaymentsToAcquireBusinessesNetOfCashAcquired": 12_000_000,
    "DividendsCommonStockCash": 1_055_000_000,
    "CashCashEquivalentsAndShortTermInvestments": 3_609_000_000,
    "LongTermDebtAndCapitalLeaseObligations": 6_792_000_000,
    "AccountsReceivableNet": 5_818_000_000,
    "InventoryNet": 5_822_000_000,
    "AllocatedShareBasedCompensationExpense": 93_000_000,
    "Goodwill": 2_224_000_000,
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
    print("cummins ok", actual)
    print("cummins-filing-denominators-ok")


if __name__ == "__main__":
    main()
