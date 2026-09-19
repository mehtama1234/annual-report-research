#!/usr/bin/env python3
"""Verify the PBF completed-redemption source/use boundary."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "company-first-principles"
REPORT = ANALYSIS / "capital-flow-pbf-redemption-settlement-bridge-pass-1.md"
TABLE = ANALYSIS / "data" / "capital-flow-pbf-redemption-settlement-bridge-pass-1.csv"


def main() -> int:
    for path in (REPORT, TABLE):
        if not path.is_file():
            raise SystemExit(f"FAIL: missing PBF redemption artifact: {path.relative_to(ROOT)}")
    text = REPORT.read_text(encoding="utf-8")
    for marker in (
        "completed-redemption-source-use-visible",
        "500.0M USD",
        "492.1M USD",
        "801.6M USD",
        "settlement-ledger-hold",
        "not full settlement-ledger proof",
        "Consolidated financing cash flow",
        "`$1.100B` of revolver borrowings",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: PBF bridge marker missing: {marker}")
    with TABLE.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 11:
        raise SystemExit(f"FAIL: expected 11 PBF bridge rows, found {len(rows)}")
    if rows[1]["value_or_metric"] != "492.1M USD net proceeds":
        raise SystemExit("FAIL: PBF net proceeds value does not match the filing")
    if rows[2]["value_or_metric"] != "801.6M USD redeemed at par plus accrued interest":
        raise SystemExit("FAIL: PBF redemption value does not match the filing")
    print("pbf-redemption-settlement-bridge-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
