#!/usr/bin/env python3
"""Verify FY2025 filing facts for CME and S&P Global."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "cme-group-inc": {
        "values": {
            "Revenues": 6_520_600_000,
            "NetCashProvidedByUsedInOperatingActivities": 4_277_100_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 83_500_000,
            "PaymentsOfDividends": 3_933_000_000,
            "UnsecuredLongTermDebt": 3_422_300_000,
            "AllocatedShareBasedCompensationExpense": 95_600_000,
        }
    },
    "sp-global-inc": {
        "values": {
            "RevenueFromContractWithCustomerExcludingAssessedTax": 15_336_000_000,
            "NetCashProvidedByUsedInOperatingActivities": 5_651_000_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 2_023_000_000,
            "PaymentsForRepurchaseOfCommonStock": 5_001_000_000,
            "PaymentsOfDividendsCommonStock": 1_170_000_000,
            "ShareBasedCompensation": 236_000_000,
            "LongTermDebt": 13_088_000_000,
        }
    },
}


def fy2025_value(facts: dict, tag: str) -> int:
    rows = []
    for unit_rows in facts["facts"]["us-gaap"][tag]["units"].values():
        rows.extend(row for row in unit_rows if row.get("fy") == 2025 and row.get("fp") == "FY" and row.get("form") == "10-K")
    if not rows:
        raise AssertionError(f"missing FY2025 fact: {tag}")
    return rows[-1]["val"]


def main() -> None:
    for name, case in CASES.items():
        base = ROOT / "raw/sec/financial/investment-brokerage-national" / name
        filing = base / "2025-10k.html"
        facts_path = ROOT / "raw/sec/companyfacts/financial/investment-brokerage-national" / name / "companyfacts.json"
        if not filing.exists() or filing.stat().st_size < 100_000:
            raise AssertionError(f"missing annual filing: {filing}")
        facts = json.loads(facts_path.read_text())
        actual = {tag: fy2025_value(facts, tag) for tag in case["values"]}
        if actual != case["values"]:
            raise AssertionError(f"{name}: expected {case['values']}, got {actual}")
        print(name, "ok", actual)
    print("exchange-information-filing-denominators-ok")


if __name__ == "__main__":
    main()

