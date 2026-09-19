#!/usr/bin/env python3
"""Verify Caterpillar FY2025 GAAP denominators used by the research dossier."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "industrial-goods/construction-farm-machinery/caterpillar-inc"
EXPECTED = {
    "Revenues": 67_589_000_000,
    "NetIncomeLossAvailableToCommonStockholdersBasic": 8_884_000_000,
    "NetCashProvidedByUsedInOperatingActivities": 11_739_000_000,
    "PaymentsToAcquirePropertyPlantAndEquipment": 2_821_000_000,
    "PaymentsToAcquireBusinessesNetOfCashAcquired": 47_000_000,
    "PaymentsForRepurchaseOfCommonStock": 5_190_000_000,
    "DividendsCommonStockCash": 2_788_000_000,
    "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents": 9_986_000_000,
    "LongTermDebtNoncurrent": 30_696_000_000,
    "InventoryNet": 18_135_000_000,
    "AllocatedShareBasedCompensationExpense": 242_000_000,
    "Goodwill": 5_321_000_000,
    "ProductWarrantyAccrual": 1_626_000_000,
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
    print("caterpillar ok", actual)
    print("caterpillar-filing-denominators-ok")


if __name__ == "__main__":
    main()
