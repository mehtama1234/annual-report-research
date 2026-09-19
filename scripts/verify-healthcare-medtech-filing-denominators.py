#!/usr/bin/env python3
"""Verify FY2025 filing facts used in the healthcare medtech comparison."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "healthcare/medical-instruments-supplies"
CASES = {
    "baxter-international-inc": {
        "facts": {
            "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations": 951_000_000,
            "NetCashProvidedByUsedInOperatingActivities": 845_000_000,
            "PaymentsToAcquireProductiveAssets": 513_000_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 9_000_000,
        }
    },
    "henry-schein-inc": {
        "facts": {
            "NetCashProvidedByUsedInOperatingActivities": 712_000_000,
            "PaymentsToAcquireProductiveAssets": 139_000_000,
            "PaymentsToAcquireBusinessesAndInterestInAffiliates": 199_000_000,
            "PaymentsForRepurchaseOfCommonStock": 850_000_000,
        }
    },
    "intuitive-surgical-inc": {
        "facts": {
            "NetCashProvidedByUsedInOperatingActivities": 3_030_500_000,
            "PaymentsToAcquireProductiveAssets": 539_800_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 13_900_000,
            "ShareBasedCompensation": 788_200_000,
        }
    },
    "stryker-corporation": {
        "facts": {
            "NetCashProvidedByUsedInOperatingActivities": 5_044_000_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 761_000_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 4_960_000_000,
            "ShareBasedCompensation": 243_000_000,
        }
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
        filing = ROOT / "raw/sec" / BASE / name / "2025-10k.html"
        facts_path = ROOT / "raw/sec/companyfacts" / BASE / name / "companyfacts.json"
        if not filing.exists() or filing.stat().st_size < 100_000:
            raise AssertionError(f"missing annual filing: {filing}")
        actual = {
            tag: fy2025_value(json.loads(facts_path.read_text()), tag)
            for tag in case["facts"]
        }
        if actual != case["facts"]:
            raise AssertionError(f"{name}: expected {case['facts']}, got {actual}")
        print(name, "ok", actual)
    print("healthcare-medtech-filing-denominators-ok")


if __name__ == "__main__":
    main()
