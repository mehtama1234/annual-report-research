#!/usr/bin/env python3
"""Verify FY2025 filing facts across the LNG and midstream cohort."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "cheniere-energy-inc": {
        "base": "energy/oil-gas-pipelines/cheniere-energy-inc",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 5_539_000_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 3_078_000_000,
            "PaymentsForRepurchaseOfCommonStock": 2_724_000_000,
            "PaymentsOfDividends": 451_000_000,
            "ShareBasedCompensation": 161_000_000,
        },
    },
    "energy-transfer-lp": {
        "base": "energy/oil-gas-pipelines/energy-transfer-lp",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 10_149_000_000,
            "PaymentsToAcquireProductiveAssets": 6_303_000_000,
            "PaymentsOfDividendsMinorityInterest": 1_734_000_000,
            "ShareBasedCompensation": 148_000_000,
            "LongTermDebt": 68_333_000_000,
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
    print("energy-midstream-filing-denominators-ok")


if __name__ == "__main__":
    main()
