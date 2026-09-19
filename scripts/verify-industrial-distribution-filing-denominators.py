#!/usr/bin/env python3
"""Verify FY2025 filing facts across the industrial-distribution cohort."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "ferguson-enterprises-inc": {
        "base": "industrial-goods/plumbing-hvac-distribution/ferguson-enterprises-inc",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 1_908_000_000,
            "PaymentsToAcquireProductiveAssets": 305_000_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 301_000_000,
            "PaymentsForRepurchaseOfCommonStock": 948_000_000,
            "PaymentsOfDividends": 489_000_000,
        },
    },
    "fastenal-company": {
        "base": "industrial-goods/industrial-supply/fastenal-company",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 1_295_900_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 245_300_000,
            "PaymentsOfDividends": 1_004_200_000,
            "ShareBasedCompensation": 8_400_000,
        },
    },
    "ww-grainger-inc": {
        "base": "industrial-goods/industrial-equipment-components/ww-grainger-inc",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 2_015_000_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 684_000_000,
            "PaymentsForRepurchaseOfCommonStock": 1_045_000_000,
            "ShareBasedCompensation": 64_000_000,
        },
    },
    "wesco-international-inc": {
        "base": "industrial-goods/industrial-equipment-components/wesco-international-inc",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 125_000_000,
            "PaymentsToAcquireProductiveAssets": 99_800_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 36_100_000,
            "ShareBasedCompensation": 40_500_000,
            "PaymentsForRepurchaseOfCommonStock": 75_000_000,
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
    print("industrial-distribution-filing-denominators-ok")


if __name__ == "__main__":
    main()
