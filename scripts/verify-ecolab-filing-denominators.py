#!/usr/bin/env python3
"""Verify Ecolab FY2025 GAAP facts and investing-cash disclosure."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "basic-materials/specialty-chemicals/ecolab-inc"
EXPECTED = {
    "RevenueFromContractWithCustomerExcludingAssessedTax": 16_081_200_000,
    "NetIncomeLoss": 2_075_600_000,
    "NetCashProvidedByUsedInOperatingActivities": 2_952_600_000,
    "PaymentsToAcquirePropertyPlantAndEquipment": 1_048_300_000,
    "PaymentsForRepurchaseOfCommonStock": 783_800_000,
    "PaymentsOfDividendsCommonStock": 753_600_000,
    "CashAndCashEquivalentsAtCarryingValue": 646_200_000,
    "LongTermDebtAndCapitalLeaseObligations": 7_365_900_000,
    "DebtCurrent": 870_400_000,
    "AccountsReceivableNetCurrent": 3_249_400_000,
    "InventoryNet": 1_490_400_000,
    "ShareBasedCompensation": 136_600_000,
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
    if "1,621.3" not in text or "Acquisitions and investments in affiliates" not in text:
        raise AssertionError("missing FY2025 acquisition/investment disclosure")
    facts = json.loads(facts_path.read_text())
    actual = {tag: fy2025_value(facts, tag) for tag in EXPECTED}
    if actual != EXPECTED:
        raise AssertionError(f"expected {EXPECTED}, got {actual}")
    print("ecolab ok", actual, "acquisitions_and_affiliates_net=1621300000")
    print("ecolab-filing-denominators-ok")

if __name__ == "__main__":
    main()
