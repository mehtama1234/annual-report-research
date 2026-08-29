#!/usr/bin/env python3
"""Build first column reconciliation diagnostic for Accordia Schedule D owned rows."""

from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
ANALYSIS = ROOT / "analysis/company-first-principles"

RAW = DATA / "capital-flow-kkr-global-atlantic-accordia-schedule-d-parser-pass-1.csv"
OUT = DATA / "capital-flow-kkr-global-atlantic-accordia-schedule-d-column-reconciliation-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-kkr-global-atlantic-accordia-schedule-d-column-reconciliation-diagnostic-pass-1.csv"
MEMO = ANALYSIS / "capital-flow-kkr-global-atlantic-accordia-schedule-d-column-reconciliation-pass-1.md"

TARGET_BOND_BASE = Decimal("7318322163")
OWNED_SCHEDULES = {
    "Schedule D Part 1 Section 1 issuer-credit obligations owned",
    "Schedule D Part 1 Section 2 asset-backed securities owned",
}

FIELDNAMES = [
    "reconciliation_row_id",
    "parser_row_id",
    "schedule_part",
    "page",
    "cusip",
    "issuer_or_description",
    "naic_designation_detected",
    "asset_type_guess",
    "candidate_actual_cost",
    "candidate_par_value",
    "candidate_fair_value",
    "candidate_book_adjusted_carrying_value",
    "money_token_count",
    "reconciliation_status",
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


def tokens(row: dict[str, str]) -> list[str]:
    return [token.strip() for token in row["money_tokens_first_12"].split(";") if token.strip()]


def money(token: str) -> Decimal:
    token = token.strip()
    if not token:
        return Decimal(0)
    negative = token.startswith("(") and token.endswith(")")
    value = Decimal(token.strip("()").replace(",", ""))
    return -value if negative else value


def fmt(value: Decimal) -> str:
    return str(int(value))


def status_for(row: dict[str, str], toks: list[str]) -> str:
    count = int(row["money_token_count"])
    if len(toks) < 4:
        return "short-token-column-hold"
    if count > 12:
        return "long-token-merged-row-review-hold"
    return "candidate-first-four-column-map"


def build_rows() -> list[dict[str, str]]:
    out = []
    for row in read_rows(RAW):
        if row["schedule_part"] not in OWNED_SCHEDULES:
            continue
        toks = tokens(row)
        status = status_for(row, toks)
        out.append(
            {
                "reconciliation_row_id": f"CFKKRGACEDCR-{len(out)+1:04d}",
                "parser_row_id": row["parser_row_id"],
                "schedule_part": row["schedule_part"],
                "page": row["page"],
                "cusip": row["cusip"],
                "issuer_or_description": row["issuer_or_description"],
                "naic_designation_detected": row["naic_designation_detected"],
                "asset_type_guess": row["asset_type_guess"],
                "candidate_actual_cost": toks[0] if len(toks) > 0 else "",
                "candidate_par_value": toks[1] if len(toks) > 1 else "",
                "candidate_fair_value": toks[2] if len(toks) > 2 else "",
                "candidate_book_adjusted_carrying_value": toks[3] if len(toks) > 3 else "",
                "money_token_count": row["money_token_count"],
                "reconciliation_status": status,
                "boundary": "candidate column assignment only; unresolved variance remains versus statutory bond base",
                "next_action": "inspect held long-token and short-token rows; use page-column geometry or tabula-style extraction for final reconciliation",
            }
        )
    return out


def diagnostic_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    candidate_rows = [r for r in rows if r["reconciliation_status"] == "candidate-first-four-column-map"]
    hold_rows = [r for r in rows if r["reconciliation_status"] != "candidate-first-four-column-map"]
    book_sum = sum((money(r["candidate_book_adjusted_carrying_value"]) for r in rows if r["candidate_book_adjusted_carrying_value"]), Decimal(0))
    cost_sum = sum((money(r["candidate_actual_cost"]) for r in rows if r["candidate_actual_cost"]), Decimal(0))
    fair_sum = sum((money(r["candidate_fair_value"]) for r in rows if r["candidate_fair_value"]), Decimal(0))
    variance = book_sum - TARGET_BOND_BASE
    coverage = (book_sum / TARGET_BOND_BASE * Decimal(100)) if TARGET_BOND_BASE else Decimal(0)
    issuer_rows = [r for r in rows if r["schedule_part"].endswith("issuer-credit obligations owned")]
    abs_rows = [r for r in rows if r["schedule_part"].endswith("asset-backed securities owned")]
    metrics: list[tuple[str, str | int, str]] = [
        ("owned_reconciliation_rows", len(rows), "count"),
        ("candidate_first_four_column_map_rows", len(candidate_rows), "count"),
        ("column_hold_rows", len(hold_rows), "count"),
        ("owned_issuer_credit_reconciliation_rows", len(issuer_rows), "count"),
        ("owned_abs_reconciliation_rows", len(abs_rows), "count"),
        ("candidate_actual_cost_sum", fmt(cost_sum), "USD"),
        ("candidate_fair_value_sum", fmt(fair_sum), "USD"),
        ("candidate_book_adjusted_carrying_value_sum", fmt(book_sum), "USD"),
        ("statutory_bond_net_admitted_assets_target", fmt(TARGET_BOND_BASE), "USD"),
        ("candidate_book_value_variance_vs_target", fmt(variance), "USD"),
        ("candidate_book_value_coverage_of_target_pct", f"{coverage:.6f}", "percent"),
        ("full_column_reconciliation_status", "hold", "status"),
        ("full_named_cash_proof_upgrades", 0, "count"),
        ("next_parser", "accordia-schedule-d-held-row-column-geometry", "parser"),
    ]
    out = []
    for idx, (metric, value, units) in enumerate(metrics, start=1):
        out.append(
            {
                "diagnostic_id": f"CFKKRGACEDCRD-{idx:03d}",
                "metric": metric,
                "value": str(value),
                "units": units,
                "proof_use": "controls first Accordia Schedule D column reconciliation status",
                "boundary": "Diagnostics quantify candidate column assignment and unresolved variance only; they do not prove final cash receipts or returns.",
                "next_action": "resolve held rows and final column geometry before promoting book, consideration, gain/loss, income, or return claims.",
            }
        )
    return out


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_memo(rows: list[dict[str, str]], diagnostics: list[dict[str, str]]) -> None:
    by_metric = {r["metric"]: r["value"] for r in diagnostics}
    examples = [r for r in rows if r["reconciliation_status"] == "candidate-first-four-column-map"][:10]
    table = "\n".join(
        "| {reconciliation_row_id} | {cusip} | {issuer_or_description} | {candidate_book_adjusted_carrying_value} | {reconciliation_status} |".format(**r)
        for r in examples
    )
    MEMO.write_text(
        f"""# Capital Flow KKR Global Atlantic Accordia Schedule D Column Reconciliation Pass 1

## Purpose

This pass tests whether the raw Accordia Schedule D owned-bond rows can be promoted from numeric-token evidence to statutory-column evidence.

It asks:

`Can we safely assign actual cost, par, fair value, and book/adjusted carrying value for the owned Schedule D bond/ABS universe, and does the candidate book value reconcile to the Accordia statutory bond base?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-schedule-d-column-reconciliation-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-schedule-d-column-reconciliation-diagnostic-pass-1.csv`

## Short Answer

`Partial hold. The first-four-token candidate map covers {by_metric['candidate_first_four_column_map_rows']} owned Schedule D rows and marks {by_metric['column_hold_rows']} rows for column review. Candidate book/adjusted carrying value sums to {by_metric['candidate_book_adjusted_carrying_value_sum']} USD versus the {by_metric['statutory_bond_net_admitted_assets_target']} USD statutory bond target, a variance of {by_metric['candidate_book_value_variance_vs_target']} USD and {by_metric['candidate_book_value_coverage_of_target_pct']}% coverage. This is not clean enough for final book-value proof, but it is a quantified reconciliation frontier.`

## Reconciliation Metrics

| Metric | Value |
|---|---:|
| Owned reconciliation rows | {by_metric['owned_reconciliation_rows']} |
| Candidate mapped rows | {by_metric['candidate_first_four_column_map_rows']} |
| Held rows | {by_metric['column_hold_rows']} |
| Candidate actual cost sum | {by_metric['candidate_actual_cost_sum']} |
| Candidate fair value sum | {by_metric['candidate_fair_value_sum']} |
| Candidate book value sum | {by_metric['candidate_book_adjusted_carrying_value_sum']} |
| Statutory bond target | {by_metric['statutory_bond_net_admitted_assets_target']} |
| Candidate book variance | {by_metric['candidate_book_value_variance_vs_target']} |
| Candidate book coverage pct | {by_metric['candidate_book_value_coverage_of_target_pct']} |

## Candidate Examples

| ID | CUSIP | Issuer | Candidate Book Value | Status |
|---|---|---|---:|---|
{table}

## Proof Effect

This pass does not finish the cash proof, but it narrows the exact blocker. The named-security universe exists. The first-four-token column map works for many normal rows, but final promotion requires resolving short-token and long-token rows and likely page-column geometry for dense statutory rows.

## Boundary

Do not use this pass as final book-value, proceeds, income, gain/loss, or return proof. The current evidence is a candidate reconciliation map with an unresolved variance against the statutory bond target.

## Next Action

Build `accordia-schedule-d-held-row-column-geometry` for the held rows and high-dollar variance drivers, then rerun reconciliation against the `7.318322163B USD` statutory bond base.

## Decision

`kkr-global-atlantic-accordia-schedule-d-column-reconciliation-candidate-map-visible-held-row-geometry-next`
""",
        encoding="utf-8",
    )


def main() -> None:
    rows = build_rows()
    diagnostics = diagnostic_rows(rows)
    write_csv(OUT, FIELDNAMES, rows)
    write_csv(DIAGNOSTIC_OUT, DIAGNOSTIC_FIELDS, diagnostics)
    write_memo(rows, diagnostics)
    print(f"wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT.relative_to(ROOT)}")
    print(f"wrote memo to {MEMO.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
