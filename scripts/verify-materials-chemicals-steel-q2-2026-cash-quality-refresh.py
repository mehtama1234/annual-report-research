#!/usr/bin/env python3
"""Verify the materials/chemicals/steel Q2 refresh."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "company-first-principles"
REPORT = ANALYSIS / "combined-investment-research-materials-chemicals-steel-q2-2026-cash-quality-refresh-2026-09-17.md"
TABLE = ANALYSIS / "data/combined-investment-research-materials-chemicals-steel-q2-2026-cash-quality-refresh-2026-09-17.csv"


def main() -> int:
    for path in (REPORT, TABLE):
        if not path.is_file():
            raise SystemExit(f"FAIL: missing materials refresh: {path.relative_to(ROOT)}")
    text = REPORT.read_text(encoding="utf-8")
    for marker in (
        "Operating cash `$1.1754B`",
        "Operating cash `$2.286B`",
        "West Virginia sheet mill",
        "These are reconciliation controls",
        "no normalized\nowner-cash ranking is promoted",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: materials refresh marker missing: {marker}")
    with TABLE.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 14 or {row["company"] for row in rows} != {"Ecolab", "Nucor"}:
        raise SystemExit("FAIL: materials table must contain 14 rows across Ecolab and Nucor")
    print("materials-chemicals-steel-q2-2026-cash-quality-refresh-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
