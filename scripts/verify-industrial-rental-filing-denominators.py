#!/usr/bin/env python3
"""Verify FY2025 filing facts for the industrial rental contradiction case."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "industrial-goods/rental-leasing-services/united-rentals-inc"
VALUES = {
    "NetCashProvidedByUsedInOperatingActivities": 5_190_000_000,
    "PaymentsToAcquireBusinessesNetOfCashAcquired": 357_000_000,
    "PaymentsForRepurchaseOfCommonStock": 1_969_000_000,
    "PaymentsOfDividends": 464_000_000,
    "ShareBasedCompensation": 134_000_000,
    "ProceedsFromSaleOfPropertyPlantAndEquipment": 56_000_000,
    "LongTermDebt": 14_302_000_000,
    "CashAndCashEquivalentsAtCarryingValue": 459_000_000,
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
    base = ROOT / "raw/sec" / BASE
    filing = base / "2025-10k.html"
    facts_path = ROOT / "raw/sec/companyfacts" / BASE / "companyfacts.json"
    if not filing.exists() or filing.stat().st_size < 100_000:
        raise AssertionError(f"missing annual filing: {filing}")
    facts = json.loads(facts_path.read_text())
    actual = {tag: fy2025_value(facts, tag) for tag in VALUES}
    if actual != VALUES:
        raise AssertionError(f"expected {VALUES}, got {actual}")
    print("united-rentals-inc ok", actual)
    print("industrial-rental-filing-denominators-ok")


if __name__ == "__main__":
    main()
