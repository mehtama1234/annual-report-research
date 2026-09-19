#!/usr/bin/env python3
"""Verify ConocoPhillips FY2025 GAAP facts and disclosed capital program."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "basic-materials/major-integrated-oil-gas/conocophillips"
EXPECTED = {
    "Revenues": 58_944_000_000,
    "NetIncomeLoss": 7_988_000_000,
    "NetCashProvidedByUsedInOperatingActivities": 19_796_000_000,
    "PaymentsForRepurchaseOfCommonStock": 5_018_000_000,
    "PaymentsOfDividendsCommonStock": 3_995_000_000,
    "CashAndCashEquivalentsAtCarryingValue": 6_497_000_000,
    "LongTermDebtAndCapitalLeaseObligations": 22_424_000_000,
    "DebtCurrent": 1_020_000_000,
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
    text = filing.read_text(errors="ignore")
    if "Capital Program" not in text or "12,553" not in text:
        raise AssertionError("missing FY2025 capital-program disclosure")
    facts = json.loads(facts_path.read_text())
    actual = {tag: fy2025_value(facts, tag) for tag in EXPECTED}
    if actual != EXPECTED:
        raise AssertionError(f"expected {EXPECTED}, got {actual}")
    print("conocophillips ok", actual, "capital_program=12553000000")
    print("conocophillips-filing-denominators-ok")

if __name__ == "__main__":
    main()
