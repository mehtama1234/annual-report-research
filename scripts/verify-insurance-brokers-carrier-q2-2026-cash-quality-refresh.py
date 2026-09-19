#!/usr/bin/env python3
"""Verify the current insurance broker/carrier QoE refresh."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "company-first-principles"
REPORT = ANALYSIS / "combined-investment-research-insurance-brokers-carrier-q2-2026-cash-quality-refresh-2026-09-17.md"
TABLE = ANALYSIS / "data/combined-investment-research-insurance-brokers-carrier-q2-2026-cash-quality-refresh-2026-09-17.csv"


def main() -> int:
    for path in (REPORT, TABLE):
        if not path.is_file():
            raise SystemExit(f"FAIL: missing insurance Q2 refresh: {path.relative_to(ROOT)}")
    text = REPORT.read_text(encoding="utf-8")
    for marker in (
        "fiduciary cash `$12.203B`",
        "operating cash `$967M`",
        "adjusted operating cash `$3.48B`",
        "These are reconciliation controls",
        "No cross-model ranking is",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: insurance Q2 marker missing: {marker}")
    with TABLE.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 19 or {row["company"] for row in rows} != {"Marsh", "Arthur J. Gallagher", "Chubb"}:
        raise SystemExit("FAIL: insurance Q2 table must contain 19 rows across three models")
    print("insurance-brokers-carrier-q2-2026-cash-quality-refresh-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
