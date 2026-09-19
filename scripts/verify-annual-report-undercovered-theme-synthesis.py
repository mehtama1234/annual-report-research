#!/usr/bin/env python3
"""Verify the eight-family undercovered-industry theme atlas."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "company-first-principles"
SYNTHESIS = ANALYSIS / "annual-report-undercovered-industry-theme-synthesis-pass-1.md"
TABLE = ANALYSIS / "data" / "annual-report-undercovered-industry-theme-synthesis-pass-1.csv"

REQUIRED_FIELDS = (
    "theme_id",
    "priority",
    "theme_family",
    "plain_question",
    "social_or_cultural_insight",
    "industrial_or_operating_insight",
    "financial_or_investment_insight",
    "representative_company_sets",
    "proof_boundary",
    "writing_status",
)


def main() -> int:
    for path in (SYNTHESIS, TABLE):
        if not path.is_file():
            raise SystemExit(f"FAIL: missing undercovered-theme artifact: {path.relative_to(ROOT)}")

    text = SYNTHESIS.read_text(encoding="utf-8")
    for marker in (
        "The economy is not only trying to grow.",
        "## Theme 1: Services And Cultural Consumption",
        "## Theme 8: Ordinary Finance, Banks, Cards, Brokers, And Insurance Distribution",
        "## How These Themes Change The Final Article",
        "Keep named-cash proof as the hard boundary",
        "The cash-proof lane remains important",
    ):
        if marker not in text:
            raise SystemExit(f"FAIL: undercovered-theme synthesis marker missing: {marker}")

    with TABLE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != list(REQUIRED_FIELDS):
            raise SystemExit("FAIL: undercovered-theme CSV header mismatch")
        rows = list(reader)

    if len(rows) != 8:
        raise SystemExit(f"FAIL: expected 8 undercovered theme rows, found {len(rows)}")
    if {row["theme_id"] for row in rows} != {f"ARUITS-{index:03d}" for index in range(1, 9)}:
        raise SystemExit("FAIL: undercovered-theme rows must be ARUITS-001 through ARUITS-008")
    if {row["writing_status"] for row in rows} != {"ready-for-integration"}:
        raise SystemExit("FAIL: every undercovered theme must be ready-for-integration")
    for row in rows:
        for field in REQUIRED_FIELDS:
            if not row[field].strip():
                raise SystemExit(f"FAIL: empty {field}: {row['theme_id']}")

    print("Annual-report undercovered-theme synthesis verification passed: 8 theme families, 10 fields, article and proof boundaries checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
