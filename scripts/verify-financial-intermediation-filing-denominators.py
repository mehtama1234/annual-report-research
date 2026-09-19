#!/usr/bin/env python3
"""Verify FY2025 cash-flow denominators used in financial dossiers."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

CASES = {
    "aon-plc": {
        "path": "financial/insurance-brokers/aon-plc",
        "facts": {
            "NetCashProvidedByUsedInOperatingActivities": 3_481_000_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 394_000_000,
            "ProceedsFromDivestitureOfBusinessesNetOfCashDivested": 2_349_000_000,
            "ShareBasedCompensation": 432_000_000,
        },
    },
    "apollo-global-management-inc": {
        "path": "financial/asset-management/apollo-global-management-inc",
        "facts": {
            "NetCashProvidedByUsedInOperatingActivities": 7_246_000_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": -99_000_000,
            "PaymentsForRepurchaseOfCommonStock": 773_000_000,
            "ShareBasedCompensation": 789_000_000,
        },
    },
    "blackrock-inc": {
        "path": "financial/asset-management/blackrock-inc",
        "facts": {
            "NetCashProvidedByUsedInOperatingActivities": 3_927_000_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 3_496_000_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 375_000_000,
            "ShareBasedCompensation": 1_307_000_000,
        },
    },
    "cme-group-inc": {
        "path": "financial/investment-brokerage-national/cme-group-inc",
        "facts": {
            "NetCashProvidedByUsedInOperatingActivities": 4_277_100_000,
            "InvestmentIncomeNonoperating": 5_736_500_000,
            "PaymentsOfDividends": 3_933_000_000,
            "ShareBasedCompensation": 94_800_000,
        },
    },
    "t-rowe-price-group-inc": {
        "path": "financial/asset-management/t-rowe-price-group-inc",
        "facts": {
            "NetCashProvidedByUsedInOperatingActivities": 1_753_400_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 274_200_000,
            "PaymentsForRepurchaseOfCommonStock": 620_900_000,
            "PaymentsOfDividends": 1_143_000_000,
            "ShareBasedCompensation": 216_900_000,
        },
    },
}


def fy2025_value(facts: dict, tag: str) -> int:
    rows = facts["facts"]["us-gaap"][tag]["units"]
    candidates = []
    for unit_rows in rows.values():
        for row in unit_rows:
            if row.get("fy") == 2025 and row.get("fp") == "FY" and row.get("form") == "10-K":
                candidates.append(row["val"])
    if not candidates:
        raise AssertionError(f"missing FY2025 10-K fact: {tag}")
    return candidates[-1]


def main() -> None:
    for name, case in CASES.items():
        base = ROOT / "raw/sec" / case["path"]
        filing = base / "2025-10k.html"
        facts_path = ROOT / "raw/sec/companyfacts" / case["path"] / "companyfacts.json"
        if not filing.exists() or filing.stat().st_size < 100_000:
            raise AssertionError(f"missing or suspicious annual filing: {filing}")
        facts = json.loads(facts_path.read_text())
        actual = {tag: fy2025_value(facts, tag) for tag in case["facts"]}
        if actual != case["facts"]:
            raise AssertionError(f"{name}: expected {case['facts']}, got {actual}")
        print(name, "ok", actual)
    print("financial-intermediation-filing-denominators-ok")


if __name__ == "__main__":
    main()
