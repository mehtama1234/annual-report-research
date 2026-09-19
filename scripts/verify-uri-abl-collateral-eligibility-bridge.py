#!/usr/bin/env python3
"""Verify the URI ABL collateral-eligibility and availability boundary."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "company-first-principles"
REPORT = ANALYSIS / "capital-flow-uri-abl-collateral-eligibility-bridge-2026-09-17.md"
TABLE = ANALYSIS / "data" / "capital-flow-uri-abl-collateral-eligibility-bridge-2026-09-17.csv"


def main() -> int:
    for path in (REPORT, TABLE):
        if not path.is_file():
            raise SystemExit(f"FAIL: missing URI collateral artifact: {path.relative_to(ROOT)}")
    text = REPORT.read_text(encoding="utf-8")
    for marker in (
        "Eligible Rental Equipment",
        "Combined Availability",
        "$2.802B",
        "populated collateral and lifecycle return unproven",
        "should not infer those values from total fleet",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: URI collateral boundary marker missing: {marker}")
    with TABLE.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) < 18:
        raise SystemExit(f"FAIL: expected at least 18 URI collateral fields, found {len(rows)}")
    observed = {row["observed_value"] for row in rows}
    if "$2.802B" not in observed or "$1.666B" not in observed:
        raise SystemExit("FAIL: URI Q2 capacity/debt observations missing")
    print("uri-abl-collateral-eligibility-bridge-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
