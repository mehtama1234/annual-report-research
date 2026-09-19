#!/usr/bin/env python3
"""Verify FY2025 filing facts for Ares' fee-paying-AUM model."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "financial/asset-management/ares-management-corporation"
EXPECTED = {
    "RevenueFromContractWithCustomerExcludingAssessedTax": 5_601_482_000,
    "NetIncomeLoss": 527_362_000,
    "NetCashProvidedByUsedInOperatingActivities": 3_266_959_000,
    "AllocatedShareBasedCompensationExpense": 740_549_000,
    "GoodwillAcquiredDuringPeriod": 2_285_242_000,
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
        raise AssertionError(f"Ares: expected {EXPECTED}, got {actual}")
    print("ares-management-corporation ok", actual)
    print("ares-filing-denominators-ok")


if __name__ == "__main__":
    main()
