#!/usr/bin/env python3
"""Build column review for short-stream Athene same-CUSIP cash-like rows."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
RAW_INSPECTION = DATA / "capital-flow-apollo-athene-statutory-safe-cashlike-same-cusip-raw-text-inspection-pass-1.csv"
OUT = DATA / "capital-flow-apollo-athene-statutory-safe-cashlike-column-review-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-apollo-athene-statutory-safe-cashlike-column-review-diagnostic-pass-1.csv"

FIELDNAMES = [
    "column_review_id",
    "cusip",
    "source_row_id",
    "source_schedule",
    "source_page",
    "issuer_or_description",
    "raw_money_token_count",
    "raw_date_token_count",
    "raw_money_tokens",
    "interpreted_par_or_shares_usd",
    "interpreted_actual_cost_usd",
    "interpreted_consideration_usd",
    "interpreted_book_value_at_disposal_usd",
    "interpreted_safe_gain_loss_usd",
    "interpreted_interest_or_dividends_received_usd",
    "column_review_status",
    "promotion_decision",
    "evidence_basis",
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


def money_tokens(row: dict[str, str]) -> list[str]:
    return [token.strip() for token in row["parser_numeric_values"].split(";") if token.strip()]


def interpreted_row(seq: int, row: dict[str, str]) -> dict[str, str]:
    tokens = money_tokens(row)
    if row["source_schedule"] == "Schedule D Part 5":
        evidence_basis = (
            "Part 5 header order is par/shares, actual cost, consideration, "
            "book value at disposal, then later gain/loss and interest/dividends. "
            "The raw row carries four repeated 1,806,570 tokens and a final 43,047 token."
        )
        par, cost, consideration, book = tokens[:4]
        gain_loss = ""
        interest = tokens[4] if len(tokens) > 4 else ""
    elif row["source_schedule"] == "Schedule D Part 4":
        evidence_basis = (
            "Part 4 header order is consideration, par value, actual cost, prior-year book, "
            "book value at disposal, then gain/loss and interest/dividends. "
            "The raw row carries repeated 268,000,000 tokens and a final 3,986,842 token."
        )
        par = tokens[1] if len(tokens) > 1 else ""
        cost = tokens[2] if len(tokens) > 2 else ""
        consideration = tokens[0] if tokens else ""
        book = tokens[3] if len(tokens) > 3 else ""
        gain_loss = ""
        interest = tokens[4] if len(tokens) > 4 else ""
    else:
        evidence_basis = "Unhandled schedule layout."
        par = cost = consideration = book = gain_loss = interest = ""

    return {
        "column_review_id": f"CFAASCCR-{seq:03d}",
        "cusip": row["cusip"],
        "source_row_id": row["source_row_id"],
        "source_schedule": row["source_schedule"],
        "source_page": row["source_page"],
        "issuer_or_description": row["raw_row_text"].split(" ................................", 1)[0],
        "raw_money_token_count": row["raw_row_money_token_count"],
        "raw_date_token_count": row["raw_row_date_token_count"],
        "raw_money_tokens": "; ".join(tokens),
        "interpreted_par_or_shares_usd": par.replace(",", ""),
        "interpreted_actual_cost_usd": cost.replace(",", ""),
        "interpreted_consideration_usd": consideration.replace(",", ""),
        "interpreted_book_value_at_disposal_usd": book.replace(",", ""),
        "interpreted_safe_gain_loss_usd": gain_loss,
        "interpreted_interest_or_dividends_received_usd": interest.replace(",", ""),
        "column_review_status": "short-stream-row-column-review-complete",
        "promotion_decision": "consideration-and-interest-promotable-gain-loss-blank-hold",
        "evidence_basis": evidence_basis,
        "boundary": "column review supports these sparse row fields, but does not prove borrower receipt, source/use, liability spread, or asset return",
        "next_action": "map issuer/borrower context and reconcile lot continuity before any final named cash-return claim",
    }


def diagnostic_row(seq: int, metric: str, value: str, units: str) -> dict[str, str]:
    return {
        "diagnostic_id": f"CFAASCCRD-{seq:03d}",
        "metric": metric,
        "value": value,
        "units": units,
        "proof_use": "controls page-specific column review for short-stream same-CUSIP rows",
        "boundary": "diagnostic is row-column interpretation only; it is not borrower receipt, liability spread, or return proof",
        "next_action": "use promoted consideration/interest fields in the next borrower and lot-continuity workbench",
    }


def main() -> None:
    held_rows = [
        row
        for row in read_rows(RAW_INSPECTION)
        if row["inspection_status"] == "raw-row-found-short-numeric-stream-column-hold"
    ]
    output = [interpreted_row(idx, row) for idx, row in enumerate(held_rows, start=1)]
    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(output)

    diagnostics = [
        ("column_review_rows", str(len(output)), "count"),
        ("consideration_promotable_rows", str(sum(1 for row in output if row["interpreted_consideration_usd"])), "count"),
        ("interest_promotable_rows", str(sum(1 for row in output if row["interpreted_interest_or_dividends_received_usd"])), "count"),
        ("gain_loss_blank_hold_rows", str(sum(1 for row in output if not row["interpreted_safe_gain_loss_usd"])), "count"),
        ("pages_reviewed", str(len({row["source_page"] for row in output})), "count"),
        ("cusips_reviewed", str(len({row["cusip"] for row in output})), "count"),
        ("interpreted_consideration_total", str(sum(int(row["interpreted_consideration_usd"]) for row in output)), "USD"),
        ("interpreted_interest_or_dividends_total", str(sum(int(row["interpreted_interest_or_dividends_received_usd"]) for row in output)), "USD"),
    ]
    with DIAGNOSTIC_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DIAGNOSTIC_FIELDS)
        writer.writeheader()
        for idx, (metric, value, units) in enumerate(diagnostics, start=1):
            writer.writerow(diagnostic_row(idx, metric, value, units))

    print(f"wrote {len(output)} rows to {OUT.relative_to(ROOT)}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
