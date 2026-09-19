#!/usr/bin/env python3
"""Verify FY2025 filing facts for Blackstone's alternative-manager model."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "financial/asset-management/blackstone-inc"
EXPECTED = {
    "NetIncomeLoss": 3_019_214_000,
    "NetCashProvidedByUsedInOperatingActivities": 4_663_161_000,
    "PaymentsToAcquirePropertyPlantAndEquipment": 115_703_000,
    "PaymentsToAcquireBusinessesNetOfCashAcquired": 0,
    "PaymentsOfDividendsCommonStock": 6_013_385_000,
    "PaymentsOfDividendsMinorityInterest": 1_035_141_000,
    "ShareBasedCompensation": 1_445_352_000,
    "CashAndCashEquivalentsAtCarryingValue": 2_631_241_000,
    "LongTermDebt": 12_576_587_000,
}


def fy2025_value(facts: dict, tag: str) -> int:
    rows = []
    for unit_rows in facts["facts"]["us-gaap"][tag]["units"].values():
        rows.extend(
            row for row in unit_rows
            if row.get("fy") == 2025 and row.get("fp") == "FY" and row.get("form") == "10-K"
        )
    if not rows:
        raise AssertionError(f"missing FY2025 fact: {tag}")
    return rows[-1]["val"]


def main() -> None:
    base = ROOT / "raw/sec" / BASE
    filing = base / "2025-10k.html"
    facts_path = ROOT / "raw/sec/companyfacts" / BASE / "companyfacts.json"
    if not filing.exists() or filing.stat().st_size < 100_000:
        raise AssertionError(f"missing annual filing: {filing}")
    facts = json.loads(facts_path.read_text())
    actual = {tag: fy2025_value(facts, tag) for tag in EXPECTED}
    if actual != EXPECTED:
        raise AssertionError(f"Blackstone: expected {EXPECTED}, got {actual}")
    print("blackstone-inc ok", actual)
    print("blackstone-filing-denominators-ok")


if __name__ == "__main__":
    main()
