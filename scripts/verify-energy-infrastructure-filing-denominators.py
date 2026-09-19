#!/usr/bin/env python3
"""Verify FY2025 filing facts used in the energy/physical-capacity cohort."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "nextera-energy-inc": {
        "filing": "raw/sec/energy/utilities/nextera-energy-inc/2025-10k.html",
        "facts": "raw/sec/companyfacts/energy/utilities/nextera-energy-inc/companyfacts.json",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 12_485_000_000,
            "PaymentsOfDividends": 4_680_000_000,
            "ProceedsFromIssuanceOfLongTermDebt": 23_394_000_000,
        },
    },
    "oneok-inc": {
        "filing": "raw/sec/energy/utilities/oneok-inc/2025-10k.html",
        "facts": "raw/sec/companyfacts/energy/utilities/oneok-inc/companyfacts.json",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 5_599_000_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 3_152_000_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 25_000_000,
            "PaymentsOfDividends": 2_583_000_000,
        },
    },
    "generac-holdings-inc": {
        "filing": "raw/sec/industrial-goods/electrical-equipment-supplies/generac-holdings-inc/2025-10k.html",
        "facts": "raw/sec/companyfacts/industrial-goods/electrical-equipment-supplies/generac-holdings-inc/companyfacts.json",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 437_978_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 169_850_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 762_000,
            "PaymentsForRepurchaseOfCommonStock": 147_917_000,
        },
    },
    "vertiv-holdings-co": {
        "filing": "raw/sec/industrial-goods/industrial-electrical-equipment/vertiv-holdings-co/2025-10k.html",
        "facts": "raw/sec/companyfacts/industrial-goods/electrical-equipment-supplies/vertiv-holdings-co/companyfacts.json",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 2_113_800_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 220_000_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 1_184_800_000,
            "PaymentsOfDividends": 66_600_000,
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
        filing = ROOT / case["filing"]
        if not filing.exists() or filing.stat().st_size < 100_000:
            raise AssertionError(f"missing annual filing: {filing}")
        facts = json.loads((ROOT / case["facts"]).read_text())
        actual = {tag: fy2025_value(facts, tag) for tag in case["values"]}
        if actual != case["values"]:
            raise AssertionError(f"{name}: expected {case['values']}, got {actual}")
        print(name, "ok", actual)
    print("energy-infrastructure-filing-denominators-ok")


if __name__ == "__main__":
    main()
