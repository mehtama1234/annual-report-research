#!/usr/bin/env python3
"""Verify the deep-dossier scenario register and its source-memo links."""

from __future__ import annotations

import csv
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "analysis" / "valuation" / "deep-dossier-scenario-inputs-2026-09-13.csv"
EXPECTED_HEADER = [
    "company",
    "reference_period",
    "starting_cash_measure_usd_m",
    "historical_2023_residual_usd_m",
    "historical_2024_residual_usd_m",
    "historical_2025_residual_usd_m",
    "bear_normalized_owner_cash_usd_m",
    "base_normalized_owner_cash_usd_m",
    "bull_normalized_owner_cash_usd_m",
    "bear_equity_cash_multiple",
    "base_equity_cash_multiple",
    "bull_equity_cash_multiple",
    "current_equity_value_usd_m",
    "bear_implied_equity_value_usd_m",
    "base_implied_equity_value_usd_m",
    "bull_implied_equity_value_usd_m",
    "source_memo",
    "normalization_basis",
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def number(row: dict[str, str], field: str) -> float:
    try:
        value = float(row[field])
    except (KeyError, ValueError) as exc:
        fail(f"{row.get('company', '<unknown>')} has invalid {field}: {exc}")
    if not math.isfinite(value):
        fail(f"{row['company']} has non-finite {field}")
    return value


def main() -> int:
    if not REGISTER.exists():
        fail(f"missing {REGISTER.relative_to(ROOT)}")

    with REGISTER.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != EXPECTED_HEADER:
            fail(f"header mismatch: {reader.fieldnames}")
        rows = list(reader)

    if not rows:
        fail("register has no data rows")
    companies: set[str] = set()
    for row_number, row in enumerate(rows, start=2):
        company = row["company"].strip()
        if not company:
            fail(f"row {row_number} has no company")
        if company in companies:
            fail(f"duplicate company {company}")
        companies.add(company)

        source = ROOT / "analysis" / "valuation" / row["source_memo"]
        if not source.exists():
            fail(f"{company} source memo missing: {row['source_memo']}")
        if not row["normalization_basis"].strip():
            fail(f"{company} has no normalization basis")

        bear_cash = number(row, "bear_normalized_owner_cash_usd_m")
        base_cash = number(row, "base_normalized_owner_cash_usd_m")
        bull_cash = number(row, "bull_normalized_owner_cash_usd_m")
        bear_multiple = number(row, "bear_equity_cash_multiple")
        base_multiple = number(row, "base_equity_cash_multiple")
        bull_multiple = number(row, "bull_equity_cash_multiple")
        current_value = number(row, "current_equity_value_usd_m")

        if not (0 <= bear_cash <= base_cash <= bull_cash):
            fail(f"{company} cash cases are not ordered nonnegative bear <= base <= bull")
        if not (0 < bear_multiple <= base_multiple <= bull_multiple):
            fail(f"{company} multiples are not ordered positive bear <= base <= bull")
        if current_value <= 0:
            fail(f"{company} current equity value is not positive")

        for cash_field, multiple_field, implied_field in (
            ("bear_normalized_owner_cash_usd_m", "bear_equity_cash_multiple", "bear_implied_equity_value_usd_m"),
            ("base_normalized_owner_cash_usd_m", "base_equity_cash_multiple", "base_implied_equity_value_usd_m"),
            ("bull_normalized_owner_cash_usd_m", "bull_equity_cash_multiple", "bull_implied_equity_value_usd_m"),
        ):
            expected = number(row, cash_field) * number(row, multiple_field)
            actual = number(row, implied_field)
            if not math.isclose(actual, expected, rel_tol=0, abs_tol=1.1):
                fail(f"{company} {implied_field}={actual} does not equal cash × multiple={expected}")

    print(f"Deep-dossier scenario register verification passed: {len(rows)} rows, 18 fields, source links and implied values checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
