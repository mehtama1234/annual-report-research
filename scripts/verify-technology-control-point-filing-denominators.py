#!/usr/bin/env python3
"""Verify annual filing facts for the technology control-point cohort."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "f5-inc": {
        "filing": "raw/sec/technology/networking-communications/f5-inc/2025-10k.html",
        "facts": "raw/sec/companyfacts/technology/networking-communications/f5-inc/companyfacts.json",
        "fy": 2025,
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 949_666_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 43_260_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 171_059_000,
            "ShareBasedCompensation": 231_491_000,
        },
    },
    "kla-corporation": {
        "filing": "raw/sec/technology/semiconductors/kla-corporation/2026-10k.html",
        "facts": "raw/sec/companyfacts/technology/semiconductors/kla-corporation/companyfacts.json",
        "fy": 2026,
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 4_143_079_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 375_945_000,
            "PaymentsForRepurchaseOfCommonStock": 2_289_769_000,
            "ShareBasedCompensation": 310_171_000,
        },
    },
}


def annual_value(facts: dict, tag: str, fy: int) -> int:
    obj = facts["facts"]["us-gaap"][tag]
    candidates = []
    for unit_rows in obj["units"].values():
        for row in unit_rows:
            if row.get("fy") == fy and row.get("fp") == "FY" and row.get("form") == "10-K":
                candidates.append(row["val"])
    if not candidates:
        raise AssertionError(f"missing FY{fy} fact: {tag}")
    return candidates[-1]


def main() -> None:
    for name, case in CASES.items():
        filing = ROOT / case["filing"]
        if not filing.exists() or filing.stat().st_size < 100_000:
            raise AssertionError(f"missing annual filing: {filing}")
        facts = json.loads((ROOT / case["facts"]).read_text())
        actual = {tag: annual_value(facts, tag, case["fy"]) for tag in case["values"]}
        if actual != case["values"]:
            raise AssertionError(f"{name}: expected {case['values']}, got {actual}")
        print(name, "ok", actual)
    print("technology-control-point-filing-denominators-ok")


if __name__ == "__main__":
    main()
