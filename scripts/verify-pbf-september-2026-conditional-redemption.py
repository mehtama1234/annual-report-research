#!/usr/bin/env python3
"""Verify PBF's current conditional-redemption liquidity boundary."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "company-first-principles"
REPORT = ANALYSIS / "capital-flow-pbf-september-2026-conditional-redemption-liquidity-boundary-2026-09-17.md"
TABLE = ANALYSIS / "data" / "capital-flow-pbf-september-2026-conditional-redemption-liquidity-boundary-2026-09-17.csv"


def main() -> int:
    for path in (REPORT, TABLE):
        if not path.is_file():
            raise SystemExit(f"FAIL: missing PBF September boundary: {path.relative_to(ROOT)}")
    text = REPORT.read_text(encoding="utf-8")
    for marker in (
        "September 14, 2026 Form 8-K",
        "$500M",
        "103.938%",
        "$519.690M",
        "pbf-2032-exchangeable-financing-issued; 2030-redemption-settlement-open",
        "issuer level",
        "diluted common-owner return",
        "$533.6M",
        "$96.80",
        "7,812,475",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: PBF September boundary marker missing: {marker}")
    with TABLE.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 7:
        raise SystemExit(f"FAIL: expected 7 PBF September rows, found {len(rows)}")
    if rows[2]["observed_value"] != "103.938% plus accrued and unpaid interest":
        raise SystemExit("FAIL: PBF redemption premium mismatch")
    print("pbf-september-2026-conditional-redemption-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
