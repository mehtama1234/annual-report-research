#!/usr/bin/env python3
"""Parse Athene Schedule BA Part 1 with PDF x-coordinate columns.

The text-layer parser is useful for row discovery but collapses blank columns.
This pass uses the PDF word coordinates for the fixed Schedule BA Part 1
columns, preserving blanks and retaining rows without a CUSIP identifier.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

import pymupdf


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw/primary-sources/capital-flow/apollo/athene/statutory/2025/athene-annuity-and-life-company-2025-statutory-statement.pdf"
OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-part1-coordinate-parser-pass-1.csv"
DIAGNOSTIC = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-part1-coordinate-reconciliation-pass-1.csv"

START_PAGE = 5813
END_PAGE = 5825
CONTROL_BOOK_VALUE = 17_461_797_562
CONTROL_VALUES = {
    "actual_cost": 15_285_961_900,
    "fair_value": 17_724_920_754,
    "book_adjusted_carrying_value": CONTROL_BOOK_VALUE,
    "investment_income": 237_086_005,
    "commitment_for_additional_investment": 4_368_051_289,
}

CUSIP_RE = re.compile(r"^(?:[A-Z0-9*@#]{6}-[A-Z0-9*@#]{2}-[A-Z0-9*@#]|[A-Z0-9]{6,9}[.*])$")
CONTROL_RE = re.compile(r"^\d{6,7}\.")
DOT_RE = re.compile(r"^\.+$")
MONEY_RE = re.compile(r"\(?\d{1,3}(?:,\d{3})+(?:\.\d+)?\)?")
# Coordinate-bounded numeric cells also contain small uncomma-separated
# values (for example `933`, `13`, `1`, or `6`).
FIELD_NUMBER_RE = re.compile(r"\(?\d[\d,]*(?:\.\d+)?\)?")

# Left and right x-coordinates of the Schedule BA Part 1 numeric columns.
FIELD_RANGES = {
    "actual_cost": (575.0, 616.0),
    "fair_value": (616.0, 657.0),
    "book_adjusted_carrying_value": (657.0, 698.0),
    "unrealized_valuation_change": (698.0, 739.0),
    "current_year_depreciation_or_amortization": (739.0, 775.0),
    "current_year_other_than_temporary_impairment": (775.0, 811.0),
    "capitalized_deferred_interest_and_other": (811.0, 847.0),
    "total_foreign_exchange_change": (847.0, 883.0),
    "investment_income": (883.0, 919.0),
    "commitment_for_additional_investment": (919.0, 955.0),
    "percentage_of_ownership": (955.0, 983.0),
}


def money_in(words: list[tuple], y: float, xlo: float, xhi: float) -> str:
    # Dot markers are often fused with the numeric token in the PDF text
    # layer, and the fused word can begin in the preceding column. Assign
    # each numeric token by its interpolated center so a neighboring blank or
    # populated statutory column cannot bleed into this field.
    values: list[tuple[float, str]] = []
    for word in words:
        x0, wy, x1, _y1, text = float(word[0]), float(word[1]), float(word[2]), float(word[3]), str(word[4])
        if abs(wy - y) >= 1.35 or x1 <= x0:
            continue
        matches = list(FIELD_NUMBER_RE.finditer(text))
        for match in matches:
            center_fraction = (match.start() + match.end()) / (2 * len(text))
            center_x = x0 + (x1 - x0) * center_fraction
            if (xlo - 1.5) <= center_x < xhi:
                values.append((center_x, match.group()))
    return values[-1][1] if values else ""


def numeric(value: str) -> int | None:
    if not value:
        return None
    return int(value.replace(",", "").replace("(", "-").replace(")", ""))


def row_anchors(words: list[tuple]) -> list[tuple[float, str]]:
    candidates: list[tuple[float, str]] = []
    for word in words:
        x, y, _x1, _y1, text = float(word[0]), float(word[1]), float(word[2]), float(word[3]), str(word[4])
        if not (x < 90 and 165 < y < 760):
            continue
        if CONTROL_RE.match(text):
            continue
        if CUSIP_RE.match(text):
            candidates.append((y, text))
        elif DOT_RE.match(text):
            candidates.append((y, ""))

    anchors: list[tuple[float, str]] = []
    for y, identifier in sorted(candidates):
        if anchors and abs(y - anchors[-1][0]) < 1.2:
            if identifier and not anchors[-1][1]:
                anchors[-1] = (anchors[-1][0], identifier)
            continue
        anchors.append((y, identifier))
    return anchors


def name_near(words: list[tuple], y: float) -> str:
    selected = []
    for word in words:
        x, wy, text = float(word[0]), float(word[1]), str(word[4])
        if not (90 <= x < 210 and y - 7.5 <= wy <= y + 1.2):
            continue
        if DOT_RE.match(text) or re.fullmatch(r"[0-9./%*-]+", text):
            continue
        selected.append((wy, x, text))
    return " ".join(item[2] for item in sorted(selected, key=lambda item: (item[0], item[1])))[:300]


def main() -> None:
    document = pymupdf.open(PDF)
    output_rows: list[dict[str, str]] = []
    sequence = 1
    for page_no in range(START_PAGE, END_PAGE + 1):
        words = document[page_no - 1].get_text("words")
        for y, identifier in row_anchors(words):
            values = {field: money_in(words, y, *bounds) for field, bounds in FIELD_RANGES.items()}
            # A few page decorations contain dot-only first-column words. Keep
            # only rows with either an identifier, a name, or a numeric field.
            label = name_near(words, y)
            if not (identifier or label or any(values.values())):
                continue
            output_rows.append(
                {
                    "parser_row_id": f"CFAASBACP-{sequence:04d}",
                    "schedule": "Schedule BA Part 1",
                    "page": str(page_no),
                    "source_y": f"{y:.1f}",
                    "cusip_or_identifier": identifier,
                    "name_or_description_near_row": label,
                    **values,
                    "current_status": "coordinate-column-parser-row-visible",
                    "boundary": "Schedule BA Part 1 coordinate extraction; source blanks preserved; row-level accounting still requires control and population reconciliation",
                }
            )
            sequence += 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    fields = list(output_rows[0])
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output_rows)

    book_values = [numeric(row["book_adjusted_carrying_value"]) for row in output_rows]
    book_values = [value for value in book_values if value is not None]
    book_sum = sum(book_values)
    diagnostic_rows = [
        {
            "diagnostic_id": "CFAASBACP-RECON-001",
            "metric": "coordinate-parser-row-count",
            "parser_value": str(len(output_rows)),
            "control_value": "not-applicable",
            "difference": "",
            "status": "source-population-visible",
            "boundary": "Includes CUSIP-bearing and blank-CUSIP rows identified by the first-column table geometry.",
        },
        {
            "diagnostic_id": "CFAASBACP-RECON-002",
            "metric": "book-adjusted-carrying-value-row-sum",
            "parser_value": str(book_sum),
            "control_value": str(CONTROL_BOOK_VALUE),
            "difference": str(book_sum - CONTROL_BOOK_VALUE),
            "status": "coordinate-control-near-tie" if abs(book_sum - CONTROL_BOOK_VALUE) <= 2_000 else "coordinate-control-review",
            "boundary": "Promotable as a control reconciliation only; not holding-level cash or return proof.",
        },
        {
            "diagnostic_id": "CFAASBACP-RECON-003",
            "metric": "rows-with-book-value",
            "parser_value": str(len(book_values)),
            "control_value": str(len(output_rows)),
            "difference": str(len(output_rows) - len(book_values)),
            "status": "sparse-row-review-open" if len(book_values) < len(output_rows) else "complete-visible",
            "boundary": "Rows with blank book value remain blank; no imputation from neighboring columns.",
        },
    ]
    for index, field in enumerate(("actual_cost", "fair_value", "book_adjusted_carrying_value", "investment_income", "commitment_for_additional_investment"), start=4):
        parsed = sum(numeric(row[field]) or 0 for row in output_rows)
        control = CONTROL_VALUES[field]
        diagnostic_rows.append(
            {
                "diagnostic_id": f"CFAASBACP-RECON-{index:03d}",
                "metric": field,
                "parser_value": str(parsed),
                "control_value": str(control),
                "difference": str(parsed - control),
                "status": "control-near-tie" if abs(parsed - control) <= 5 else "column-or-sparse-review-open",
                "boundary": "Part 1 page-5825 subtotal comparison; income and commitment differences are not promoted to cash receipt or owner cash.",
            }
        )
    with DIAGNOSTIC.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(diagnostic_rows[0]))
        writer.writeheader()
        writer.writerows(diagnostic_rows)

    print(f"wrote {len(output_rows)} coordinate rows to {OUT.relative_to(ROOT)}")
    print(f"book_rows={len(book_values)} book_sum={book_sum} control={CONTROL_BOOK_VALUE} difference={book_sum - CONTROL_BOOK_VALUE}")
    print(f"wrote {len(diagnostic_rows)} diagnostics to {DIAGNOSTIC.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
