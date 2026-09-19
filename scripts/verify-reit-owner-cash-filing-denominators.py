#!/usr/bin/env python3
"""Verify FY2025 filing facts for the real-estate owner-cash cohort."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "equinix-inc": {
        "base": "real-estate/reit-specialty-real-estate/equinix-inc",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 3_911_000_000,
            "PaymentsToAcquireProductiveAssets": 4_311_000_000,
            "PaymentsToAcquireRealEstate": 994_000_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 251_000_000,
            "PaymentsOfDividends": 1_856_000_000,
            "ShareBasedCompensation": 498_000_000,
            "NetIncomeLoss": 1_350_000_000,
        },
    },
    "digital-realty-trust-inc": {
        "base": "real-estate/reit-specialty-real-estate/digital-realty-trust-inc",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 2_412_136_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 309_000_000,
            "PaymentsOfDividends": 1_728_466_000,
            "DevelopmentInProcess": 4_976_785_000,
        },
    },
    "host-hotels-resorts-inc": {
        "base": "real-estate/reit-hotel-motel/host-hotels-resorts-inc",
        "values": {
            "NetCashProvidedByUsedInOperatingActivities": 1_510_000_000,
            "PaymentsForCapitalImprovements": 282_000_000,
            "PaymentsToAcquireOtherProductiveAssets": 362_000_000,
            "PaymentsOfDividendsCommonStock": 623_000_000,
            "PaymentsForRepurchaseOfCommonStock": 205_000_000,
        },
    },
}


def fy2025_value(facts: dict, tag: str) -> int:
    for namespace in facts["facts"].values():
        obj = namespace.get(tag)
        if not obj:
            continue
        candidates = []
        for unit_rows in obj["units"].values():
            for row in unit_rows:
                if row.get("fy") == 2025 and row.get("fp") == "FY" and row.get("form") == "10-K":
                    candidates.append(row["val"])
        if candidates:
            return candidates[-1]
    raise AssertionError(f"missing FY2025 fact: {tag}")


def main() -> None:
    for name, case in CASES.items():
        base = ROOT / "raw/sec" / case["base"]
        filing = base / "2025-10k.html"
        facts = json.loads((ROOT / "raw/sec/companyfacts" / case["base"] / "companyfacts.json").read_text())
        if not filing.exists() or filing.stat().st_size < 100_000:
            raise AssertionError(f"missing annual filing: {filing}")
        actual = {tag: fy2025_value(facts, tag) for tag in case["values"]}
        if actual != case["values"]:
            raise AssertionError(f"{name}: expected {case['values']}, got {actual}")
        print(name, "ok", actual)
    print("reit-owner-cash-filing-denominators-ok")


if __name__ == "__main__":
    main()
