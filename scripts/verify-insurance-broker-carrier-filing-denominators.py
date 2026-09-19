#!/usr/bin/env python3
"""Verify FY2025 filing facts for the broker-versus-carrier insurance lane."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "marsh-mclennan-companies-inc": {
        "base": "financial/insurance-brokers/marsh-mclennan-companies-inc",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 5_292_000_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 291_000_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 652_000_000,
            "PaymentsForRepurchaseOfCommonStock": 2_012_000_000,
            "PaymentsOfDividendsCommonStock": 1_699_000_000,
            "AllocatedShareBasedCompensationExpense": 394_000_000,
            "LongTermDebt": 19_587_000_000,
        },
    },
    "chubb-limited": {
        "base": "financial/property-casualty-insurance/chubb-limited",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 12_816_000_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 289_000_000,
            "PaymentsForRepurchaseOfCommonStock": 3_694_000_000,
            "PaymentsOfDividendsCommonStock": 1_505_000_000,
            "LongTermDebt": 15_728_000_000,
            "RestrictedCashAndCashEquivalents": 198_000_000,
        },
    },
}


def fy2025_value(facts: dict, tag: str) -> int:
    obj = facts["facts"]["us-gaap"][tag]
    candidates = []
    for unit_rows in obj["units"].values():
        for row in unit_rows:
            if row.get("fy") == 2025 and row.get("fp") == "FY" and row.get("form") == "10-K":
                candidates.append(row["val"])
    if not candidates:
        raise AssertionError(f"missing FY2025 fact: {tag}")
    return candidates[-1]


def main() -> None:
    for name, case in CASES.items():
        base = ROOT / "raw/sec" / case["base"]
        filing = base / "2025-10k.html"
        facts_path = ROOT / "raw/sec/companyfacts" / case["base"] / "companyfacts.json"
        if not filing.exists() or filing.stat().st_size < 100_000:
            raise AssertionError(f"missing annual filing: {filing}")
        facts = json.loads(facts_path.read_text())
        actual = {tag: fy2025_value(facts, tag) for tag in case["values"]}
        if actual != case["values"]:
            raise AssertionError(f"{name}: expected {case['values']}, got {actual}")
        print(name, "ok", actual)
    print("insurance-broker-carrier-filing-denominators-ok")


if __name__ == "__main__":
    main()
