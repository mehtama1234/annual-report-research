#!/usr/bin/env python3
"""Verify FY2025 filing facts across the industrial-contractor cohort."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "comfort-systems-usa-inc": {
        "base": "industrial-goods/general-contractors/comfort-systems-usa-inc",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 1_186_356_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 154_903_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 279_610_000,
            "PaymentsForRepurchaseOfCommonStock": 215_999_000,
        },
    },
    "emcor-group-inc": {
        "base": "industrial-goods/general-contractors/emcor-group-inc",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 1_302_063_000,
            "PaymentsToAcquireProductiveAssets": 112_750_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 1_022_105_000,
            "PaymentsForRepurchaseOfCommonStock": 586_258_000,
        },
    },
    "sterling-infrastructure-inc": {
        "base": "industrial-goods/heavy-construction/sterling-infrastructure-inc",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 439_988_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 77_312_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 482_333_000,
            "ShareBasedCompensation": 24_181_000,
        },
    },
    "quanta-services-inc": {
        "base": "industrial-goods/general-contractors/quanta-services-inc",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 2_229_970_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 609_154_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 3_052_116_000,
            "ShareBasedCompensation": 181_947_000,
        },
    },
    "mastec-inc": {
        "base": "industrial-goods/engineering-construction/mastec-inc",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 545_714_000,
            "PaymentsToAcquireProductiveAssets": 259_985_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 71_044_000,
            "ShareBasedCompensation": 34_002_000,
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
    print("industrial-contractor-filing-denominators-ok")


if __name__ == "__main__":
    main()
