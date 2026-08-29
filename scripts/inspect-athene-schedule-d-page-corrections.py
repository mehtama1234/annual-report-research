#!/usr/bin/env python3
"""Inspect high-priority Athene Schedule D pages for parser correction clues."""

from __future__ import annotations

import csv
import re
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw/primary-sources/capital-flow/apollo/athene/statutory/2025/athene-annuity-and-life-company-2025-statutory-statement.pdf"
FULL_D = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-full-range-parser-pass-1.csv"
PAGE_DIAGNOSTIC = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-page-diagnostic-pass-1.csv"
OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-high-priority-page-inspection-pass-1.csv"

MONEY_RE = re.compile(r"\(?\d{1,3}(?:,\d{3})+(?:\.\d+)?\)?")

FIELDNAMES = [
    "inspection_id",
    "page",
    "source_parser_row_id",
    "cusip",
    "issuer_or_description",
    "page_priority_status",
    "parser_actual_cost",
    "parser_fair_value",
    "parser_book_adjusted_carrying_value",
    "parser_interest_income",
    "parser_interest_received_during_year",
    "raw_line_excerpt",
    "raw_numeric_tokens",
    "blank_marker_count_before_first_number",
    "diagnosis",
    "current_status",
    "next_action",
]


def page_lines(reader: PdfReader, page_no: int) -> list[str]:
    text = reader.pages[page_no - 1].extract_text() or ""
    return [line.strip() for line in text.splitlines() if line.strip()]


def line_for_cusip(lines: list[str], cusip: str) -> str:
    for idx, line in enumerate(lines):
        if cusip in line:
            parts = [line]
            for next_line in lines[idx + 1 : idx + 3]:
                if MONEY_RE.search(next_line) or next_line.startswith("E11."):
                    break
                parts.append(next_line)
            return " ".join(parts)
    return ""


def high_priority_pages() -> list[str]:
    with PAGE_DIAGNOSTIC.open(newline="") as f:
        rows = list(csv.DictReader(f))
    return [
        row["page"]
        for row in rows
        if row["current_status"] == "high-priority-column-correction"
    ]


def diagnosis(raw_line: str, parser_book: str) -> str:
    if parser_book:
        return "parser has book value on a high-priority page; use as control row"
    if ".........................." in raw_line:
        return "raw row contains repeated blank-column dot markers; positional numeric parser likely shifted fields left"
    if not raw_line:
        return "source row not found in raw pypdf line scan; inspect page text extraction manually"
    return "missing book value requires row-level column inspection"


def main() -> None:
    pages = set(high_priority_pages())
    with FULL_D.open(newline="") as f:
        full_rows = [
            row
            for row in csv.DictReader(f)
            if row["page"] in pages
        ]

    by_page: dict[str, list[dict[str, str]]] = {}
    for row in full_rows:
        by_page.setdefault(row["page"], []).append(row)

    reader = PdfReader(str(PDF))
    output: list[dict[str, str]] = []
    for page in sorted(pages, key=int):
        page_rows = by_page.get(page, [])
        missing_book = [row for row in page_rows if not row["book_adjusted_carrying_value"]]
        control = [row for row in page_rows if row["book_adjusted_carrying_value"]]
        sample_rows = (missing_book[:4] + control[:1])[:5]
        lines = page_lines(reader, int(page))
        for row in sample_rows:
            raw_line = line_for_cusip(lines, row["cusip"])
            tokens = MONEY_RE.findall(raw_line)
            before_first = raw_line.split(tokens[0], 1)[0] if tokens else raw_line
            output.append(
                {
                    "inspection_id": f"CFAASDHP-{len(output) + 1:03d}",
                    "page": page,
                    "source_parser_row_id": row["source_parser_row_id"],
                    "cusip": row["cusip"],
                    "issuer_or_description": row["issuer_or_description"],
                    "page_priority_status": "high-priority-column-correction",
                    "parser_actual_cost": row["actual_cost"],
                    "parser_fair_value": row["fair_value"],
                    "parser_book_adjusted_carrying_value": row["book_adjusted_carrying_value"],
                    "parser_interest_income": row["interest_income"],
                    "parser_interest_received_during_year": row["interest_received_during_year"],
                    "raw_line_excerpt": raw_line[:700],
                    "raw_numeric_tokens": "; ".join(tokens[:12]),
                    "blank_marker_count_before_first_number": str(before_first.count("..........................")),
                    "diagnosis": diagnosis(raw_line, row["book_adjusted_carrying_value"]),
                    "current_status": "raw-row-inspection-visible",
                    "next_action": "add ABS parser logic that preserves blank numeric columns instead of compacting numeric tokens",
                }
            )

    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(output)

    print(f"wrote {len(output)} rows to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
