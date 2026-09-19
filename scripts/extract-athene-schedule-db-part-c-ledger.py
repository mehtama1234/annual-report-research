#!/usr/bin/env python3
"""Extract a conservative row ledger for Athene Schedule DB Part C components."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw/primary-sources/capital-flow/apollo/athene/statutory/2025/athene-annuity-and-life-company-2025-statutory-statement.pdf"
OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-db-part-c-ledger-pass-1.csv"

FIELDNAMES = [
    "ledger_id",
    "source_page",
    "derivative_identifier",
    "derivative_description",
    "derivative_instrument_type",
    "cash_instrument_cusip",
    "cash_instrument_description",
    "derivative_notional_candidates",
    "derivative_book_value_candidates",
    "derivative_fair_value_candidates",
    "cash_instrument_book_value_candidates",
    "cash_instrument_fair_value_candidates",
    "row_mapping_status",
    "what_is_proven",
    "boundary",
    "next_proof",
]


def numeric_candidates(value: str) -> list[str]:
    return re.findall(r"\(?-?[\d,]+(?:\.\d+)?\)?", value)


def clean_text(words: list[tuple]) -> str:
    return " ".join(
        word[4]
        for word in words
        if word[4].strip(".")
    ).strip()


def column_words(words: list[tuple], low: float, high: float) -> list[tuple]:
    return [word for word in words if low <= word[0] < high]


def main() -> None:
    rows: list[dict[str, str]] = []
    document = fitz.open(PDF)
    for page_number in range(465, 490):
        words = document[page_number - 1].get_text("words")
        identifiers = [
            (word[1], word[4].strip())
            for word in words
            if word[0] < 105
            and word[1] > 135
            and re.match(r"^\d{4,6}[A-Z0-9@#*\-]+$", word[4].strip())
        ]
        for row_number, (y, identifier) in enumerate(identifiers, start=1):
            row_words = [word for word in words if y - 8.5 <= word[1] <= y + 1.5]
            derivative_description = clean_text(column_words(row_words, 100, 195))
            derivative_type = clean_text(column_words(row_words, 500, 590))
            cash_cusip = clean_text(column_words(row_words, 690, 730)).replace(" ", "")
            cash_description = clean_text(column_words(row_words, 730, 820))
            if not cash_cusip:
                continue
            if identifier == "9999999999" or "XXX" in cash_cusip:
                continue

            fields = {
                "derivative_notional_candidates": numeric_candidates(
                    " ".join(word[4] for word in column_words(row_words, 260, 315))
                ),
                "derivative_book_value_candidates": numeric_candidates(
                    " ".join(word[4] for word in column_words(row_words, 315, 365))
                ),
                "derivative_fair_value_candidates": numeric_candidates(
                    " ".join(word[4] for word in column_words(row_words, 365, 415))
                ),
                "cash_instrument_book_value_candidates": numeric_candidates(
                    " ".join(word[4] for word in column_words(row_words, 890, 940))
                ),
                "cash_instrument_fair_value_candidates": numeric_candidates(
                    " ".join(word[4] for word in column_words(row_words, 945, 1000))
                ),
            }
            component_fields = [
                fields["derivative_book_value_candidates"],
                fields["derivative_fair_value_candidates"],
                fields["cash_instrument_book_value_candidates"],
                fields["cash_instrument_fair_value_candidates"],
            ]
            ambiguous = any(len(values) > 1 for values in fields.values())
            missing = any(not values for values in component_fields)
            status = (
                "source-row-visible-column-ambiguous"
                if ambiguous
                else "source-row-visible-column-sparse"
                if missing
                else "source-row-visible-component-columns-resolved"
            )
            rows.append(
                {
                    "ledger_id": f"CFAASDBPC-{len(rows) + 1:04d}",
                    "source_page": str(page_number),
                    "derivative_identifier": identifier,
                    "derivative_description": derivative_description,
                    "derivative_instrument_type": derivative_type,
                    "cash_instrument_cusip": cash_cusip,
                    "cash_instrument_description": cash_description,
                    **{key: "|".join(values) for key, values in fields.items()},
                    "row_mapping_status": status,
                    "what_is_proven": "Schedule DB Part C names a derivative/synthetic-asset row and its cash-instrument CUSIP/description in the statutory source.",
                    "boundary": "Source-row identity and candidate columns are not settlement, counterparty remittance, hedge cost, liability allocation, borrower receipt, or Apollo owner cash.",
                    "next_proof": "Verify row coordinates and numeric columns, then match Schedule DB verification, custody/counterparty, cash settlement, hedged liability block, and related income.",
                }
            )

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
