#!/usr/bin/env python3
"""Verify the annual-report cross-sector integration matrix and source joins."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "company-first-principles"
MATRIX_MD = ANALYSIS / "annual-report-cross-sector-integration-matrix-pass-1.md"
MATRIX_CSV = ANALYSIS / "data" / "annual-report-cross-sector-integration-matrix-pass-1.csv"

REQUIRED_FIELDS = (
    "theme_id",
    "theme",
    "force_or_pressure",
    "control_point",
    "payer_or_funder",
    "burden_carrier",
    "operating_denominator",
    "qoe_financial_shenanigans_control",
    "owner_cash_valuation_object",
    "macro_liquidity_route",
    "current_grade",
    "decisive_breaker",
    "source_artifact",
)


def main() -> int:
    for path in (MATRIX_MD, MATRIX_CSV):
        if not path.is_file():
            raise SystemExit(f"FAIL: missing integration artifact: {path.relative_to(ROOT)}")

    text = MATRIX_MD.read_text(encoding="utf-8")
    for marker in (
        "force -> control point -> payer/funder",
        "QoE / financial-shenanigans control",
        "The matrix does not rank sectors",
        "Do not pool denominators",
        "Do not promote a theme because the macro route is plausible",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: integration boundary marker missing: {marker}")

    with MATRIX_CSV.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != list(REQUIRED_FIELDS):
            raise SystemExit("FAIL: integration CSV header does not match the required schema")
        rows = list(reader)

    expected_ids = {f"ARCSIM-{index:03d}" for index in range(1, 13)}
    if {row["theme_id"] for row in rows} != expected_ids:
        raise SystemExit("FAIL: integration matrix must contain exactly ARCSIM-001 through ARCSIM-012")

    for row in rows:
        for field in REQUIRED_FIELDS:
            if not row[field].strip():
                raise SystemExit(f"FAIL: empty {field}: {row['theme_id']}")
        source = ANALYSIS / row["source_artifact"]
        if not source.is_file():
            raise SystemExit(f"FAIL: missing source artifact for {row['theme_id']}: {row['source_artifact']}")
        if "ranking" in row["current_grade"].lower():
            raise SystemExit(f"FAIL: integration row must not claim a ranking: {row['theme_id']}")

    print("Annual-report cross-sector integration verification passed: 12 themes, 13 fields, source artifacts and non-ranking boundaries checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
