#!/usr/bin/env python3
"""Verify FY2025 filing facts used in the restaurant comparison."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "cava-group-inc": {
        "facts": {
            "NetCashProvidedByUsedInOperatingActivities": 184_840_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 158_699_000,
            "ShareBasedCompensation": 15_234_000,
        }
    },
    "restaurant-brands-international-inc": {
        "facts": {
            "NetCashProvidedByUsedInOperatingActivities": 1_714_000_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 265_000_000,
            "PaymentsToAcquireBusinessesNetOfCashAcquired": 152_000_000,
            "PaymentsOfDividends": 1_108_000_000,
        }
    },
    "wingstop-inc": {
        "facts": {
            "NetCashProvidedByUsedInOperatingActivities": 153_065_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 47_441_000,
            "PaymentsForRepurchaseOfCommonStock": 221_859_000,
            "PaymentsOfDividends": 32_382_000,
        }
    },
    "yum-brands-inc": {
        "facts": {
            "NetCashProvidedByUsedInOperatingActivities": 2_010_000_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 371_000_000,
            "PaymentsForRepurchaseOfCommonStock": 552_000_000,
            "ShareBasedCompensation": 70_000_000,
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
        filing = ROOT / "raw/sec/services/restaurants" / name / "2025-10k.html"
        facts_path = ROOT / "raw/sec/companyfacts/services/restaurants" / name / "companyfacts.json"
        if not filing.exists() or filing.stat().st_size < 100_000:
            raise AssertionError(f"missing annual filing: {filing}")
        facts = json.loads(facts_path.read_text())
        actual = {tag: fy2025_value(facts, tag) for tag in case["facts"]}
        if actual != case["facts"]:
            raise AssertionError(f"{name}: expected {case['facts']}, got {actual}")
        print(name, "ok", actual)
    text_checks = {
        "restaurant-brands-international-inc": [
            r"over\s*95\s*%\s*of system-wide restaurants were franchised",
        ],
        "wingstop-inc": [
            r"approximately\s*98\s*%\s*franchised",
            r"2,999\s*franchised",
            r"5\.5\s*%\s*,?\s*of gross sales",
            r"average unit volume.*?\$\s*2\.0\s*million",
            r"initial investment.*?\$\s*580,000",
        ],
        "yum-brands-inc": [
            r"97\s*%\s*of our restaurants were owned and operated by franchisees",
            r"refranchised\s*23",
        ],
    }
    for name, patterns in text_checks.items():
        filing = ROOT / "raw/sec/services/restaurants" / name / "2025-10k.html"
        raw = filing.read_text(encoding="utf-8", errors="ignore").replace("&#160;", " ")
        normalized = re.sub(r"<[^>]+>", " ", raw)
        normalized = re.sub(r"\s+", " ", normalized)
        for pattern in patterns:
            if not re.search(pattern, normalized, re.IGNORECASE):
                raise AssertionError(f"{name}: missing filing text control: {pattern}")
        print(name, "text-controls-ok")
    print("restaurant-franchise-filing-denominators-ok")


if __name__ == "__main__":
    main()
