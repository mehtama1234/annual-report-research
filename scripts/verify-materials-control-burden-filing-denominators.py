#!/usr/bin/env python3
"""Verify FY2025 filing facts for specialty-service versus steel-cycle materials."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "ecolab-inc": {
        "base": "basic-materials/specialty-chemicals/ecolab-inc",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 2_952_600_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 1_048_300_000,
            "PaymentsToAcquireBusinessesAndInterestInAffiliates": 1_621_300_000,
            "PaymentsForRepurchaseOfCommonStock": 783_800_000,
            "PaymentsOfDividendsCommonStock": 753_600_000,
            "AllocatedShareBasedCompensationExpense": 136_600_000,
            "LongTermDebtAndCapitalLeaseObligations": 7_365_900_000,
        },
    },
    "nucor-corporation": {
        "base": "basic-materials/steel-iron/nucor-corporation",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 3_234_000_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 3_422_000_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 2_000_000,
            "PaymentsForRepurchaseOfCommonStock": 700_000_000,
            "PaymentsOfDividendsCommonStock": 512_000_000,
            "ShareBasedCompensation": 133_000_000,
            "LongTermDebtAndCapitalLeaseObligations": 6_909_000_000,
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
    print("materials-control-burden-filing-denominators-ok")


if __name__ == "__main__":
    main()
