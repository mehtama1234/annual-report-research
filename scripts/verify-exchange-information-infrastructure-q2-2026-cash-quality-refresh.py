#!/usr/bin/env python3
"""Verify the exchange/information infrastructure Q2 refresh."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "company-first-principles"
REPORT = ANALYSIS / "combined-investment-research-exchange-information-infrastructure-q2-2026-cash-quality-refresh-2026-09-17.md"
TABLE = ANALYSIS / "data/combined-investment-research-exchange-information-infrastructure-q2-2026-cash-quality-refresh-2026-09-17.csv"


def main() -> int:
    for path in (REPORT, TABLE):
        if not path.is_file():
            raise SystemExit(f"FAIL: missing exchange/information refresh: {path.relative_to(ROOT)}")
    text = REPORT.read_text(encoding="utf-8")
    for marker in (
        "Federal Reserve cash account `$138.5B`",
        "operating cash `$2.476B`",
        "disposition proceeds `$361M`",
        "not automatically corporate cash",
        "No collateral\nbalance, adjusted free cash flow",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: exchange/information marker missing: {marker}")
    with TABLE.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 14 or {row["company"] for row in rows} != {"CME Group", "S&P Global"}:
        raise SystemExit("FAIL: exchange/information table must contain 14 rows across two models")
    print("exchange-information-infrastructure-q2-2026-cash-quality-refresh-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
