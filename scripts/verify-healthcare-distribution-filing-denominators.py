#!/usr/bin/env python3
"""Verify FY2025 filing facts for the pharmaceutical-distribution cohort."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "mckesson-corporation": {
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 6_085_000_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 537_000_000,
            "PaymentsToAcquireProductiveAssets": 859_000_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 24_000_000,
            "PaymentsForRepurchaseOfCommonStock": 3_146_000_000,
        }
    },
    "cencora-inc": {
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 3_875_120_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 667_981_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 4_095_630_000,
            "ShareBasedCompensation": 147_963_000,
        }
    },
    "cardinal-health-inc": {
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 2_397_000_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 547_000_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 5_250_000_000,
            "ShareBasedCompensation": 244_000_000,
            "PaymentsForRepurchaseOfCommonStock": 765_000_000,
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
        base = ROOT / "raw/sec/healthcare/pharmaceutical-distribution" / name
        filing = base / "2025-10k.html"
        facts_path = ROOT / "raw/sec/companyfacts/healthcare/pharmaceutical-distribution" / name / "companyfacts.json"
        if not filing.exists() or filing.stat().st_size < 100_000:
            raise AssertionError(f"missing annual filing: {filing}")
        facts = json.loads(facts_path.read_text())
        actual = {tag: fy2025_value(facts, tag) for tag in case["values"]}
        if actual != case["values"]:
            raise AssertionError(f"{name}: expected {case['values']}, got {actual}")
        print(name, "ok", actual)
    print("healthcare-distribution-filing-denominators-ok")


if __name__ == "__main__":
    main()
