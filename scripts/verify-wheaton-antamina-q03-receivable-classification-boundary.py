#!/usr/bin/env python3
"""Verify the Q-03 public receivable-classification boundary."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "company-first-principles"
REPORT = ANALYSIS / "capital-flow-wheaton-antamina-q03-receivable-classification-boundary-2026-09-17.md"
TABLE = ANALYSIS / "data" / "capital-flow-wheaton-antamina-q03-receivable-classification-boundary-2026-09-17.csv"


def main() -> int:
    for path in (REPORT, TABLE):
        if not path.is_file():
            raise SystemExit(f"FAIL: missing Q-03 receivable artifact: {path.relative_to(ROOT)}")
    text = REPORT.read_text(encoding="utf-8")
    for marker in (
        "does not identify an Antamina, BHP, or metal-credit receivable",
        "does not prove that no BHP-related amount existed",
        "searched-negative",
        "No Antamina\nreceipt, owner cash, or return ranking is promoted.",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: Q-03 receivable boundary marker missing: {marker}")
    with TABLE.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 4:
        raise SystemExit(f"FAIL: expected 4 Q-03 receivable rows, found {len(rows)}")
    if rows[0]["june_30_2026"] != "$26.056M" or rows[0]["december_31_2025"] != "$46.723M":
        raise SystemExit("FAIL: total receivable values do not match the filing")
    print("wheaton-antamina-q03-receivable-classification-boundary-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
