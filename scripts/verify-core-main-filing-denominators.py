#!/usr/bin/env python3
"""Verify Core & Main FY2025 facts using the filing's CY2025 frame."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "industrial-goods/building-materials-wholesale/core-main-inc"
EXPECTED = {
    "RevenueFromContractWithCustomerExcludingAssessedTax": 7_647_000_000,
    "NetCashProvidedByUsedInOperatingActivities": 650_000_000,
    "PaymentsToAcquireProductiveAssets": 46_000_000,
    "PaymentsToAcquireBusinessesNetOfCashAcquired": 61_000_000,
    "NetIncomeLossAvailableToCommonStockholdersBasic": 441_000_000,
    "NetIncomeLossAttributableToNoncontrollingInterest": 21_000_000,
    "CashAndCashEquivalentsAtCarryingValue": 220_000_000,
    "LongTermDebtNoncurrent": 2_124_000_000,
    "LongTermDebtCurrent": 24_000_000,
    "AccountsReceivableNetCurrent": 981_000_000,
    "InventoryNet": 986_000_000,
    "ShareBasedCompensation": 17_000_000,
    "Goodwill": 1_920_000_000,
}

def frame_value(facts, tag, frame):
    rows = []
    for units in facts["facts"]["us-gaap"][tag]["units"].values():
        rows.extend(r for r in units if r.get("frame") == frame)
    if not rows:
        raise AssertionError(f"missing {frame} fact: {tag}")
    return rows[-1]["val"]

def main():
    filing = ROOT / "raw/sec" / BASE / "2025-10k.html"
    facts_path = ROOT / "raw/sec/companyfacts" / BASE / "companyfacts.json"
    if not filing.exists() or filing.stat().st_size < 100_000:
        raise AssertionError(f"missing annual filing: {filing}")
    facts = json.loads(facts_path.read_text())
    actual = {}
    for tag, expected in EXPECTED.items():
        frame = "CY2025" if tag in {
            "RevenueFromContractWithCustomerExcludingAssessedTax",
            "NetCashProvidedByUsedInOperatingActivities",
            "PaymentsToAcquireProductiveAssets",
            "PaymentsToAcquireBusinessesNetOfCashAcquired",
            "NetIncomeLossAvailableToCommonStockholdersBasic",
            "NetIncomeLossAttributableToNoncontrollingInterest",
            "ShareBasedCompensation",
        } else "CY2025Q4I"
        actual[tag] = frame_value(facts, tag, frame)
    if actual != EXPECTED:
        raise AssertionError(f"expected {EXPECTED}, got {actual}")
    if actual["NetIncomeLossAvailableToCommonStockholdersBasic"] + actual["NetIncomeLossAttributableToNoncontrollingInterest"] != 462_000_000:
        raise AssertionError("common and NCI earnings do not reconcile to reported net income")
    print("core-main ok", actual, "consolidated_net_income=462000000")
    print("core-main-filing-denominators-ok")

if __name__ == "__main__":
    main()
