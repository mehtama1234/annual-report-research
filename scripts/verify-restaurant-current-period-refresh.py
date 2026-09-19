#!/usr/bin/env python3
"""Verify the current-period restaurant refresh for McDonald's and Chipotle."""

import json
import re
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "mcdonalds-corporation": {
        "facts_file": "companyfacts-cik0000063908.json",
        "facts": {
            "NetCashProvidedByUsedInOperatingActivities": 5_222_000_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 1_516_000_000,
            "PaymentsForRepurchaseOfCommonStock": 1_251_000_000,
            "DividendsCash": 2_640_000_000,
            "NumberOfRestaurants": 46_028,
        },
    },
    "chipotle-mexican-grill": {
        "facts_file": "companyfacts-cik0001058090.json",
        "facts": {
            "NetCashProvidedByUsedInOperatingActivities": 1_332_003_000,
            "PaymentsToAcquirePropertyPlantAndEquipment": 397_601_000,
            "PaymentsForRepurchaseOfCommonStock": 1_354_905_000,
            "NumberOfRestaurants": 4_186,
        },
    },
}


def q2_2026_value(facts: dict, tag: str) -> int:
    rows = []
    for unit_rows in facts["facts"]["us-gaap"][tag]["units"].values():
        for row in unit_rows:
            if row.get("fy") == 2026 and row.get("fp") == "Q2" and row.get("form") == "10-Q":
                rows.append(row)
    if not rows:
        raise AssertionError(f"missing Q2 2026 fact: {tag}")
    h1_rows = [row for row in rows if row.get("start") == "2026-01-01"]
    return (h1_rows or rows)[-1]["val"]


def main() -> None:
    for name, case in CASES.items():
        filing_name = "2026-q2-10q.html" if name == "mcdonalds-corporation" else "2026-q2-10q.pdf"
        filing = ROOT / "raw/sec/services/restaurants" / name / filing_name
        facts_path = ROOT / "raw/sec/services/restaurants" / name / case["facts_file"]
        if not filing.exists() or filing.stat().st_size < 100_000:
            raise AssertionError(f"missing current filing: {filing}")
        facts = json.loads(facts_path.read_text())
        actual = {tag: q2_2026_value(facts, tag) for tag in case["facts"]}
        if actual != case["facts"]:
            raise AssertionError(f"{name}: expected {case['facts']}, got {actual}")
        print(name, "ok", actual)
    mcd_text = (ROOT / "raw/sec/services/restaurants/mcdonalds-corporation/2026-q2-10q.html").read_text(
        encoding="utf-8", errors="ignore"
    )
    mcd_text = re.sub(r"<[^>]+>", " ", mcd_text)
    mcd_text = re.sub(r"\s+", " ", mcd_text)
    if not re.search(r"Total Franchised\s+44,016.*?42,059", mcd_text) or not re.search(
        r"Company-owned and operated\s+2,012", mcd_text
    ):
        raise AssertionError("mcdonalds-corporation: missing ownership table controls")
    if not re.search(r"franchised sales are not recorded as revenues", mcd_text, re.IGNORECASE):
        raise AssertionError("mcdonalds-corporation: missing franchise-revenue perimeter control")
    chipotle_pdf = ROOT / "raw/sec/services/restaurants/chipotle-mexican-grill/2026-q2-10q.pdf"
    chipotle_text = "\n".join((page.extract_text() or "") for page in PdfReader(chipotle_pdf).pages)
    if "we owned 4,186 restaurants" not in chipotle_text or "15 international partner-operated restaurants" not in chipotle_text:
        raise AssertionError("chipotle-mexican-grill: missing ownership text controls")
    print("ownership-text-controls-ok")
    print("restaurant-current-period-refresh-ok")


if __name__ == "__main__":
    main()
