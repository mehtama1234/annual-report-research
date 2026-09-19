#!/usr/bin/env python3
"""Parse Athene Schedule BA Part 3 and match disposal rows to Part 1 CUSIPs."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import pymupdf


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw/primary-sources/capital-flow/apollo/athene/statutory/2025/athene-annuity-and-life-company-2025-statutory-statement.pdf"
PART1 = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-part1-coordinate-parser-pass-1.csv"
OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-part3-coordinate-parser-pass-1.csv"
MATCH_OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-part3-part1-cusip-match-pass-1.csv"

CUSIP_RE = re.compile(r"^(?:[A-Z0-9*@#]{6}-[A-Z0-9*@#]{2}-[A-Z0-9*@#]|[A-Z0-9]{6,9}[.*])$")
CONTROL_RE = re.compile(r"^\d{6,7}\.")
DOT_RE = re.compile(r"^\.+$")
FIELD_NUMBER_RE = re.compile(r"\(?\d[\d,]*(?:\.\d+)?\)?")

FIELD_RANGES = {
    "book_adjusted_carrying_value_prior_year": (503, 545),
    "unrealized_valuation_change": (545, 580),
    "current_year_depreciation_or_amortization": (580, 615),
    "current_year_other_than_temporary_impairment": (615, 650),
    "capitalized_deferred_interest_and_other": (650, 685),
    "total_change_in_book_adjusted_carrying_value": (685, 720),
    "total_foreign_exchange_change": (720, 755),
    "book_adjusted_carrying_value_on_disposal": (755, 798),
    "disposal_consideration": (798, 840),
    "foreign_exchange_gain_loss_on_disposal": (840, 875),
    "realized_gain_loss_on_disposal": (875, 910),
    "total_gain_loss_on_disposal": (910, 945),
    "investment_income": (945, 983),
}


def value(words: list[tuple], y: float, xlo: float, xhi: float) -> str:
    # Dot markers are emitted as part of the same PDF word as an adjacent
    # numeric cell.  Assign each numeric token by its interpolated center,
    # rather than by the word's left edge, so a token cannot bleed into the
    # preceding statutory column.
    values: list[tuple[float, str]] = []
    for word in words:
        x0, wy, x1, _y1, text = float(word[0]), float(word[1]), float(word[2]), float(word[3]), str(word[4])
        if abs(wy - y) >= 1.35:
            continue
        matches = list(FIELD_NUMBER_RE.finditer(text))
        if not matches or x1 <= x0:
            continue
        for match in matches:
            center_fraction = (match.start() + match.end()) / (2 * len(text))
            center_x = x0 + (x1 - x0) * center_fraction
            if (xlo - 1.5) <= center_x < xhi:
                values.append((center_x, match.group()))
    return values[-1][1] if values else ""


def integer(value_text: str) -> int:
    if not value_text:
        return 0
    return int(value_text.replace(",", "").replace("(", "-").replace(")", ""))


def anchors(words: list[tuple]) -> list[tuple[float, str]]:
    control_ys = [float(w[1]) for w in words if float(w[0]) < 100 and CONTROL_RE.match(str(w[4]))]
    candidates = []
    for word in words:
        x, y, text = float(word[0]), float(word[1]), str(word[4])
        if not (x < 95 and 165 < y < 760) or any(abs(y - cy) < 2.0 for cy in control_ys):
            continue
        if CUSIP_RE.match(text) or DOT_RE.match(text):
            candidates.append((y, text if CUSIP_RE.match(text) else ""))
    result = []
    for y, identifier in sorted(candidates):
        if result and abs(y - result[-1][0]) < 1.2:
            if identifier and not result[-1][1]:
                result[-1] = (result[-1][0], identifier)
            continue
        result.append((y, identifier))
    return result


def nearby_name(words: list[tuple], y: float) -> str:
    selected = []
    for word in words:
        x, wy, text = float(word[0]), float(word[1]), str(word[4])
        if not (100 <= x < 335 and y - 7.5 <= wy <= y + 1.2):
            continue
        if DOT_RE.match(text) or re.fullmatch(r"[0-9./%*-]+", text):
            continue
        selected.append((wy, x, text))
    return " ".join(item[2] for item in sorted(selected, key=lambda item: (item[0], item[1])))[:320]


def disposal_nature(words: list[tuple], y: float) -> str:
    """Read the current row's purchaser/nature column without adjacent-row bleed."""
    selected = []
    for word in words:
        x, wy, text = float(word[0]), float(word[1]), str(word[4])
        if not (330 <= x < 425 and y - 1.35 <= wy <= y + 1.35):
            continue
        if DOT_RE.match(text):
            continue
        selected.append((x, text))
    return " ".join(text for _x, text in sorted(selected))[:160]


def date_column(words: list[tuple], y: float, xlo: float, xhi: float) -> str:
    selected = []
    for word in words:
        x, wy, text = float(word[0]), float(word[1]), str(word[4])
        if xlo <= x < xhi and y - 1.35 <= wy <= y + 1.35:
            selected.append((x, text))
    text = " ".join(text for _x, text in sorted(selected))
    match = re.search(r"\d{2}/\d{2}/\d{4}", text)
    return match.group(0) if match else ""


def main() -> None:
    document = pymupdf.open(PDF)
    rows = []
    sequence = 1
    # The source continues Part 3 through pages 5834-5835; Schedule D starts
    # on page 5836.  The earlier 5830-5833 boundary dropped two full pages.
    for page_no in range(5830, 5836):
        words = document[page_no - 1].get_text("words")
        for y, identifier in anchors(words):
            values = {field: value(words, y, *bounds) for field, bounds in FIELD_RANGES.items()}
            name = nearby_name(words, y)
            if not (identifier or name or any(values.values())):
                continue
            rows.append(
                {
                    "parser_row_id": f"CFAASBACP3-{sequence:04d}",
                    "schedule": "Schedule BA Part 3",
                    "population": "current-year-disposals-transfers-repayments",
                    "page": str(page_no),
                    "source_y": f"{y:.1f}",
                    "cusip_or_identifier": identifier,
                    "name_or_description_near_row": name,
                    "disposal_nature_source_column": disposal_nature(words, y),
                    "acquisition_date_source_column": date_column(words, y, 435, 475),
                    "disposal_date_source_column": date_column(words, y, 475, 505),
                    **values,
                    "current_status": "coordinate-column-parser-row-visible",
                    "boundary": "Schedule BA Part 3 disposal/transfer/repayment row; consideration is not independently proven bank receipt",
                }
            )
            sequence += 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    part1 = {}
    with PART1.open() as handle:
        for row in csv.DictReader(handle):
            identifier = row["cusip_or_identifier"]
            if identifier:
                part1.setdefault(identifier, []).append(row)

    matches = []
    for row in rows:
        identifier = row["cusip_or_identifier"]
        candidates = part1.get(identifier, []) if identifier else []
        matches.append(
            {
                "match_id": f"CFAASBAMATCH-{len(matches)+1:04d}",
                "part3_parser_row_id": row["parser_row_id"],
                "part3_page": row["page"],
                "cusip_or_identifier": identifier,
                "part3_name": row["name_or_description_near_row"],
                "disposal_consideration": row["disposal_consideration"],
                "part3_investment_income": row["investment_income"],
                "part1_match_count": str(len(candidates)),
                "part1_pages": ";".join(sorted({candidate["page"] for candidate in candidates})),
                "part1_book_value": ";".join(candidate["book_adjusted_carrying_value"] for candidate in candidates),
                "match_status": "same-cusip-part1-and-part3-visible" if candidates else ("part3-blank-cusip" if not identifier else "part3-cusip-no-part1-match"),
                "boundary": "Same-CUSIP statutory continuity clue; does not prove cash settlement, borrower receipt, or Apollo distribution.",
            }
        )
    with MATCH_OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(matches[0]))
        writer.writeheader()
        writer.writerows(matches)

    matched = sum(row["match_status"] == "same-cusip-part1-and-part3-visible" for row in matches)
    consideration = sum(integer(row["disposal_consideration"]) for row in rows)
    print(f"wrote {len(rows)} Part 3 coordinate rows to {OUT.relative_to(ROOT)}")
    print(f"same-cusip-part1-matches={matched} total-disposal-consideration-visible={consideration}")
    print(f"wrote {len(matches)} match rows to {MATCH_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
