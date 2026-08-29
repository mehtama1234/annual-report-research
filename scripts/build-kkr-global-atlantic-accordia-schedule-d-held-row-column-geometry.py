#!/usr/bin/env python3
"""Diagnose held rows and high-dollar variance drivers for Accordia Schedule D."""

from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
ANALYSIS = ROOT / "analysis/company-first-principles"

RAW = DATA / "capital-flow-kkr-global-atlantic-accordia-schedule-d-parser-pass-1.csv"
RECONCILIATION = DATA / "capital-flow-kkr-global-atlantic-accordia-schedule-d-column-reconciliation-pass-1.csv"
OUT = DATA / "capital-flow-kkr-global-atlantic-accordia-schedule-d-held-row-column-geometry-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-kkr-global-atlantic-accordia-schedule-d-held-row-column-geometry-diagnostic-pass-1.csv"
MEMO = ANALYSIS / "capital-flow-kkr-global-atlantic-accordia-schedule-d-held-row-column-geometry-pass-1.md"

TARGET_BOND_BASE = Decimal("7318322163")
CANDIDATE_BOOK_SUM = Decimal("6409765632")
VARIANCE_VS_TARGET = CANDIDATE_BOOK_SUM - TARGET_BOND_BASE
HIGH_DOLLAR_LIMIT = 25

FIELDNAMES = [
    "geometry_row_id",
    "row_type",
    "reconciliation_row_id",
    "parser_row_id",
    "page",
    "cusip",
    "issuer_or_description",
    "asset_type_guess",
    "money_token_count",
    "first_four_candidate_book_value",
    "extra_group_count",
    "extra_group_book_candidates",
    "max_extra_group_book_candidate",
    "geometry_class",
    "variance_relevance",
    "proof_effect",
    "boundary",
    "next_action",
]

DIAGNOSTIC_FIELDS = [
    "diagnostic_id",
    "metric",
    "value",
    "units",
    "proof_use",
    "boundary",
    "next_action",
]


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def decimal_from_token(token: str) -> Decimal:
    token = (token or "").strip()
    if not token:
        return Decimal(0)
    negative = token.startswith("(") and token.endswith(")")
    value = Decimal(token.strip("()").replace(",", ""))
    return -value if negative else value


def int_text(value: Decimal) -> str:
    return str(int(value))


def money_tokens(row: dict[str, str]) -> list[str]:
    return [token.strip() for token in row["money_tokens_first_12"].split(";") if token.strip()]


def complete_extra_groups(tokens: list[str]) -> list[list[str]]:
    groups: list[list[str]] = []
    for idx in range(4, len(tokens), 4):
        group = tokens[idx : idx + 4]
        if len(group) == 4:
            groups.append(group)
    return groups


def extra_book_values(tokens: list[str]) -> list[Decimal]:
    return [decimal_from_token(group[3]) for group in complete_extra_groups(tokens)]


def classify_held(row: dict[str, str], raw_row: dict[str, str]) -> str:
    token_count = int(row["money_token_count"])
    if token_count < 4:
        return "short-token-fragment-probable-income-or-continuation"
    extra_books = extra_book_values(money_tokens(raw_row))
    if any(value >= Decimal("100000000") for value in extra_books):
        return "long-token-row-with-page-or-section-total-signature"
    if any(value >= Decimal("10000000") for value in extra_books):
        return "long-token-row-with-possible-embedded-security"
    return "long-token-row-with-small-extra-column-noise"


def row_base(
    idx: int,
    row_type: str,
    row: dict[str, str],
    raw_row: dict[str, str],
    geometry_class: str,
    variance_relevance: str,
    proof_effect: str,
) -> dict[str, str]:
    tokens = money_tokens(raw_row)
    extras = extra_book_values(tokens)
    extra_text = "; ".join(int_text(value) for value in extras)
    max_extra = max(extras) if extras else Decimal(0)
    return {
        "geometry_row_id": f"CFKKRGACEDHG-{idx:03d}",
        "row_type": row_type,
        "reconciliation_row_id": row["reconciliation_row_id"],
        "parser_row_id": row["parser_row_id"],
        "page": row["page"],
        "cusip": row["cusip"],
        "issuer_or_description": row["issuer_or_description"],
        "asset_type_guess": row["asset_type_guess"],
        "money_token_count": row["money_token_count"],
        "first_four_candidate_book_value": row["candidate_book_adjusted_carrying_value"].replace(",", ""),
        "extra_group_count": str(len(extras)),
        "extra_group_book_candidates": extra_text,
        "max_extra_group_book_candidate": int_text(max_extra),
        "geometry_class": geometry_class,
        "variance_relevance": variance_relevance,
        "proof_effect": proof_effect,
        "boundary": "Geometry diagnostic only; extra token groups are not promoted to statutory columns or cash proof.",
        "next_action": "inspect source-page column geometry and rerun reconciliation before treating book, income, proceeds, or return fields as final.",
    }


def build_geometry_rows(reconciliation_rows: list[dict[str, str]], raw_rows: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    held = [r for r in reconciliation_rows if r["reconciliation_status"] != "candidate-first-four-column-map"]
    for row in held:
        raw_row = raw_rows[row["parser_row_id"]]
        geometry_class = classify_held(row, raw_row)
        rows.append(
            row_base(
                len(rows) + 1,
                "held-reconciliation-row",
                row,
                raw_row,
                geometry_class,
                "direct blocker: current reconciliation explicitly holds this row",
                "explains why the column map cannot yet become final statutory-column proof",
            )
        )

    candidate_rows = [r for r in reconciliation_rows if r["reconciliation_status"] == "candidate-first-four-column-map"]
    candidate_rows.sort(key=lambda r: decimal_from_token(r["candidate_book_adjusted_carrying_value"]), reverse=True)
    for row in candidate_rows[:HIGH_DOLLAR_LIMIT]:
        raw_row = raw_rows[row["parser_row_id"]]
        rows.append(
            row_base(
                len(rows) + 1,
                "high-dollar-candidate-row",
                row,
                raw_row,
                "candidate-mapped-high-dollar-row",
                "sensitivity row: already mapped, but a column error would move the reconciliation materially",
                "prioritizes high-dollar spot checks after held-row geometry is resolved",
            )
        )
    return rows


def diagnostic_rows(geometry_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    held = [r for r in geometry_rows if r["row_type"] == "held-reconciliation-row"]
    high = [r for r in geometry_rows if r["row_type"] == "high-dollar-candidate-row"]
    short = [r for r in held if r["geometry_class"].startswith("short-token")]
    long_rows = [r for r in held if r["geometry_class"].startswith("long-token")]
    subtotal = [r for r in held if r["geometry_class"] == "long-token-row-with-page-or-section-total-signature"]
    embedded = [r for r in held if r["geometry_class"] == "long-token-row-with-possible-embedded-security"]
    held_book = sum((decimal_from_token(r["first_four_candidate_book_value"]) for r in held), Decimal(0))
    high_book = sum((decimal_from_token(r["first_four_candidate_book_value"]) for r in high), Decimal(0))
    extra_books: list[Decimal] = []
    for row in held:
        extra_books.extend(decimal_from_token(token) for token in row["extra_group_book_candidates"].split("; ") if token)
    extra_sum = sum(extra_books, Decimal(0))
    large_extra = [value for value in extra_books if value >= Decimal("50000000")]
    max_extra = max(extra_books) if extra_books else Decimal(0)
    coverage = (CANDIDATE_BOOK_SUM / TARGET_BOND_BASE * Decimal(100)) if TARGET_BOND_BASE else Decimal(0)
    metrics: list[tuple[str, str | int, str]] = [
        ("geometry_rows", len(geometry_rows), "count"),
        ("held_reconciliation_rows", len(held), "count"),
        ("short_token_held_rows", len(short), "count"),
        ("long_token_held_rows", len(long_rows), "count"),
        ("subtotal_signature_held_rows", len(subtotal), "count"),
        ("possible_embedded_security_held_rows", len(embedded), "count"),
        ("held_first_four_candidate_book_value_sum", int_text(held_book), "USD"),
        ("held_extra_group_book_candidate_count", len(extra_books), "count"),
        ("held_extra_group_book_candidate_sum_not_proof", int_text(extra_sum), "USD"),
        ("held_extra_group_book_candidates_over_50m", len(large_extra), "count"),
        ("largest_extra_group_book_candidate_not_proof", int_text(max_extra), "USD"),
        ("high_dollar_candidate_rows_selected", len(high), "count"),
        ("high_dollar_candidate_first_four_book_value_sum", int_text(high_book), "USD"),
        ("candidate_book_value_sum_before_geometry", int_text(CANDIDATE_BOOK_SUM), "USD"),
        ("statutory_bond_net_admitted_assets_target", int_text(TARGET_BOND_BASE), "USD"),
        ("candidate_book_value_variance_vs_target_before_geometry", int_text(VARIANCE_VS_TARGET), "USD"),
        ("candidate_book_value_coverage_before_geometry_pct", f"{coverage:.6f}", "percent"),
        ("full_column_reconciliation_status", "hold", "status"),
        ("full_named_cash_proof_upgrades", 0, "count"),
        ("next_parser", "accordia-schedule-d-page-column-extraction-or-manual-geometry", "parser"),
    ]
    out = []
    for idx, (metric, value, units) in enumerate(metrics, start=1):
        out.append(
            {
                "diagnostic_id": f"CFKKRGACEDHGD-{idx:03d}",
                "metric": metric,
                "value": str(value),
                "units": units,
                "proof_use": "diagnoses why Accordia Schedule D column reconciliation remains on hold",
                "boundary": "The diagnostic identifies held-row geometry and sensitivity rows only; it does not promote extra groups to final statutory columns or prove cash returns.",
                "next_action": "Use source-page column geometry or table extraction for held rows, then rerun full reconciliation against the statutory bond target.",
            }
        )
    return out


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def markdown_table(rows: list[dict[str, str]], limit: int) -> str:
    return "\n".join(
        "| {geometry_row_id} | {row_type} | {page} | {cusip} | {issuer_or_description} | {first_four_candidate_book_value} | {max_extra_group_book_candidate} | {geometry_class} |".format(**row)
        for row in rows[:limit]
    )


def write_memo(geometry_rows: list[dict[str, str]], diagnostics: list[dict[str, str]]) -> None:
    by_metric = {row["metric"]: row["value"] for row in diagnostics}
    held_rows = [row for row in geometry_rows if row["row_type"] == "held-reconciliation-row"]
    high_rows = [row for row in geometry_rows if row["row_type"] == "high-dollar-candidate-row"]
    MEMO.write_text(
        f"""# Capital Flow KKR Global Atlantic Accordia Schedule D Held-Row Column Geometry Pass 1

## Purpose

This pass diagnoses the exact held-row geometry problem after the first Accordia Schedule D column reconciliation.

It asks:

`Which rows block the Accordia Schedule D owned-bond reconciliation, which token patterns are likely short fragments, embedded rows, or page/section total signatures, and which high-dollar candidate rows need spot checks before book-value proof can be promoted?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-schedule-d-held-row-column-geometry-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-schedule-d-held-row-column-geometry-diagnostic-pass-1.csv`

## Short Answer

`The column problem is now localized. There are {by_metric['held_reconciliation_rows']} held reconciliation rows: {by_metric['short_token_held_rows']} short-token fragments and {by_metric['long_token_held_rows']} long-token rows. The long rows include {by_metric['subtotal_signature_held_rows']} rows with page/section-total signatures and {by_metric['possible_embedded_security_held_rows']} rows with possible embedded-security patterns. The held rows carry {by_metric['held_first_four_candidate_book_value_sum']} USD of first-four candidate book value, but their extra token groups include {by_metric['held_extra_group_book_candidate_sum_not_proof']} USD of non-promoted candidate book-like values, including {by_metric['held_extra_group_book_candidates_over_50m']} values above 50M USD. That is why blindly adding later token groups would be unsafe.`

## Diagnostic Metrics

| Metric | Value |
|---|---:|
| Geometry rows | {by_metric['geometry_rows']} |
| Held reconciliation rows | {by_metric['held_reconciliation_rows']} |
| Short-token held rows | {by_metric['short_token_held_rows']} |
| Long-token held rows | {by_metric['long_token_held_rows']} |
| Subtotal-signature held rows | {by_metric['subtotal_signature_held_rows']} |
| Possible embedded-security held rows | {by_metric['possible_embedded_security_held_rows']} |
| Held first-four candidate book value | {by_metric['held_first_four_candidate_book_value_sum']} |
| Extra group book-like sum, not proof | {by_metric['held_extra_group_book_candidate_sum_not_proof']} |
| Extra group book-like values over 50M | {by_metric['held_extra_group_book_candidates_over_50m']} |
| Largest extra group book-like value, not proof | {by_metric['largest_extra_group_book_candidate_not_proof']} |
| High-dollar candidate rows selected | {by_metric['high_dollar_candidate_rows_selected']} |
| High-dollar selected first-four book value | {by_metric['high_dollar_candidate_first_four_book_value_sum']} |
| Candidate book value before geometry | {by_metric['candidate_book_value_sum_before_geometry']} |
| Statutory bond target | {by_metric['statutory_bond_net_admitted_assets_target']} |
| Variance before geometry | {by_metric['candidate_book_value_variance_vs_target_before_geometry']} |
| Coverage before geometry pct | {by_metric['candidate_book_value_coverage_before_geometry_pct']} |

## Held Row Examples

| ID | Type | Page | CUSIP | Issuer | First-Four Book | Max Extra Book-Like Value | Geometry Class |
|---|---|---:|---|---|---:|---:|---|
{markdown_table(held_rows, 12)}

## High-Dollar Candidate Spot Checks

| ID | Type | Page | CUSIP | Issuer | First-Four Book | Max Extra Book-Like Value | Geometry Class |
|---|---|---:|---|---|---:|---:|---|
{markdown_table(high_rows, 10)}

## Proof Effect

This pass improves the proof stack by identifying the real parser boundary. The short-token held rows look like fragments or continuation/income-only rows. The long-token held rows are the real issue: some later token groups may represent embedded securities, but others clearly look like page or section totals. Because the later groups mix those patterns, they cannot be promoted by formula.

The safe use is:

`Accordia Schedule D has a named-security universe and a quantified column-reconciliation frontier, but final book-value proof needs source-page column geometry for held rows and high-dollar spot checks.`

## Boundary

Do not use this pass as final statutory column proof. Do not add the extra token groups to book value. Do not claim issuer-level income, proceeds, gain/loss, liability spread, waterfall, collateral support, or return from this diagnostic.

## Next Action

Run a source-page column extraction or manual geometry pass for the held rows, starting with page/section-total signatures on pages `219`, `240`, and `246`, then rerun the full reconciliation against the `7.318322163B USD` statutory bond base.

## Decision

`kkr-global-atlantic-accordia-held-row-column-geometry-localized-next-page-column-extraction`
""",
        encoding="utf-8",
    )


def main() -> None:
    reconciliation_rows = read_rows(RECONCILIATION)
    raw_rows = {row["parser_row_id"]: row for row in read_rows(RAW)}
    geometry_rows = build_geometry_rows(reconciliation_rows, raw_rows)
    diagnostics = diagnostic_rows(geometry_rows)
    write_csv(OUT, FIELDNAMES, geometry_rows)
    write_csv(DIAGNOSTIC_OUT, DIAGNOSTIC_FIELDS, diagnostics)
    write_memo(geometry_rows, diagnostics)
    print(f"wrote {len(geometry_rows)} rows to {OUT.relative_to(ROOT)}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT.relative_to(ROOT)}")
    print(f"wrote memo to {MEMO.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
