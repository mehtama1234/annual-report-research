#!/usr/bin/env python3
"""Verify FY2025 filing facts for KKR's multi-engine alternatives model."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "financial/asset-management/kkr-co-inc"
EXPECTED = {
    "Revenues": 19_464_307_000,
    "NetIncomeLoss": 2_370_463_000,
    "NetCashProvidedByUsedInOperatingActivities": 477_760_000,
    "PaymentsToAcquireBusinessesNetOfCashAcquired": 146_273_000,
    "PaymentsForRepurchaseOfCommonStock": 3_362_000,
    "PaymentsOfDividendsCommonStock": 649_942_000,
    "ShareBasedCompensation": 722_109_000,
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
        raise AssertionError(f"KKR: expected {EXPECTED}, got {actual}")
    print("kkr-co-inc ok", actual)
    print("kkr-filing-denominators-ok")


if __name__ == "__main__":
    main()
