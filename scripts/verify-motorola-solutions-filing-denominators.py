#!/usr/bin/env python3
"""Verify Motorola Solutions FY2025 GAAP denominators."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "technology/diversified-communication-services/motorola-solutions-inc"
EXPECTED = {
    "RevenueFromContractWithCustomerExcludingAssessedTax": 11_682_000_000,
    "NetIncomeLoss": 2_154_000_000,
    "NetCashProvidedByUsedInOperatingActivities": 2_837_000_000,
    "PaymentsToAcquireProductiveAssets": 265_000_000,
    "PaymentsForRepurchaseOfCommonStock": 1_154_000_000,
    "PaymentsOfDividendsCommonStock": 728_000_000,
    "CashAndCashEquivalentsAtCarryingValue": 1_165_000_000,
    "ShareBasedCompensation": 293_000_000,
    "Goodwill": 6_800_000_000,
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
    print("motorola-solutions ok", actual)
    print("motorola-solutions-filing-denominators-ok")

if __name__ == "__main__":
    main()
