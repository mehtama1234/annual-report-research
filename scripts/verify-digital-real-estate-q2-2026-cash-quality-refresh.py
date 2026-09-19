#!/usr/bin/env python3
"""Verify the digital real-estate Q2 cash-quality comparison."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "company-first-principles"
REPORT = ANALYSIS / "combined-investment-research-digital-real-estate-q2-2026-cash-quality-refresh-2026-09-17.md"
TABLE = ANALYSIS / "data/combined-investment-research-digital-real-estate-q2-2026-cash-quality-refresh-2026-09-17.csv"


def main() -> int:
    for path in (REPORT, TABLE):
        if not path.is_file():
            raise SystemExit(f"FAIL: missing digital real-estate refresh: {path.relative_to(ROOT)}")
    text = REPORT.read_text(encoding="utf-8")
    for marker in (
        "OCF `$1.784B`",
        "OCF `$1.595B`",
        "`$1.477B` development",
        "These are forensic controls",
        "No owner-cash promotion is made",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: digital real-estate marker missing: {marker}")
    with TABLE.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 15 or {row["company"] for row in rows} != {"Equinix", "Digital Realty"}:
        raise SystemExit("FAIL: digital real-estate table must contain 15 rows across two companies")
    print("digital-real-estate-q2-2026-cash-quality-refresh-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
