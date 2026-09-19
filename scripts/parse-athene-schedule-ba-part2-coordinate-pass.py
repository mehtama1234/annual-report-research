#!/usr/bin/env python3
"""Parse Athene Schedule BA Part 2 acquisitions/additions by coordinates."""

from __future__ import annotations

import csv
import re
from pathlib import Path

import pymupdf


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw/primary-sources/capital-flow/apollo/athene/statutory/2025/athene-annuity-and-life-company-2025-statutory-statement.pdf"
OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-part2-coordinate-parser-pass-1.csv"
DIAGNOSTIC = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-part2-coordinate-reconciliation-pass-1.csv"

CONTROL_VALUES = {
    "actual_cost_at_time_of_acquisition": 6_030_604_898,
    "additional_investment_made_after_acquisition": 3_822_866_876,
}

CUSIP_RE = re.compile(r"^(?:[A-Z0-9*@#]{6}-[A-Z0-9*@#]{2}-[A-Z0-9*@#]|[A-Z0-9]{6,9}[.*])$")
CONTROL_RE = re.compile(r"^\d{6,7}\.")
DOT_RE = re.compile(r"^\.+$")
FIELD_NUMBER_RE = re.compile(r"\(?\d[\d,]*(?:\.\d+)?\)?")


def field_value(words: list[tuple], y: float, xlo: float, xhi: float) -> str:
    text = " ".join(str(w[4]) for w in words if abs(float(w[1]) - y) < 1.35 and (xlo - 1.5) <= float(w[0]) < xhi)
    values = FIELD_NUMBER_RE.findall(text)
    return values[-1] if values else ""


def numeric(value: str) -> int | None:
    if not value:
        return None
    return int(value.replace(",", "").replace("(", "-").replace(")", ""))


def anchors(words: list[tuple]) -> list[tuple[float, str]]:
    control_ys = [float(w[1]) for w in words if float(w[0]) < 100 and CONTROL_RE.match(str(w[4]))]
    candidates: list[tuple[float, str]] = []
    for word in words:
        x, y, text = float(word[0]), float(word[1]), str(word[4])
        if not (x < 95 and 115 < y < 760):
            continue
        if any(abs(y - control_y) < 2.0 for control_y in control_ys):
            continue
        if CUSIP_RE.match(text) or DOT_RE.match(text):
            candidates.append((y, text if CUSIP_RE.match(text) else ""))
    output: list[tuple[float, str]] = []
    for y, identifier in sorted(candidates):
        if output and abs(y - output[-1][0]) < 1.2:
            if identifier and not output[-1][1]:
                output[-1] = (output[-1][0], identifier)
            continue
        output.append((y, identifier))
    return output


def nearby_name(words: list[tuple], y: float) -> str:
    selected = []
    for word in words:
        x, wy, text = float(word[0]), float(word[1]), str(word[4])
        if not (100 <= x < 325 and y - 7.5 <= wy <= y + 1.2):
            continue
        if DOT_RE.match(text) or re.fullmatch(r"[0-9./%*-]+", text):
            continue
        selected.append((wy, x, text))
    return " ".join(item[2] for item in sorted(selected, key=lambda item: (item[0], item[1])))[:320]


def main() -> None:
    document = pymupdf.open(PDF)
    rows: list[dict[str, str]] = []
    sequence = 1
    for page_no in range(5826, 5830):
        words = document[page_no - 1].get_text("words")
        for y, identifier in anchors(words):
            values = {
                "actual_cost_at_time_of_acquisition": field_value(words, y, 740, 802),
                "additional_investment_made_after_acquisition": field_value(words, y, 802, 865),
                "amount_of_encumbrances": field_value(words, y, 865, 927),
                "percentage_of_ownership": field_value(words, y, 927, 983),
            }
            label = nearby_name(words, y)
            if not (identifier or label or any(values.values())):
                continue
            rows.append(
                {
                    "parser_row_id": f"CFAASBACP2-{sequence:04d}",
                    "schedule": "Schedule BA Part 2",
                    "population": "current-year-acquisitions-additions",
                    "page": str(page_no),
                    "source_y": f"{y:.1f}",
                    "cusip_or_identifier": identifier,
                    "name_or_description_near_row": label,
                    **values,
                    "current_status": "coordinate-column-parser-row-visible",
                    "boundary": "Schedule BA Part 2 acquisition/addition row; not a year-end holding or cash receipt without event matching",
                }
            )
            sequence += 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    diagnostics = [
        {
            "diagnostic_id": "CFAASBACP2-RECON-001",
            "metric": "coordinate-parser-row-count",
            "parser_value": str(len(rows)),
            "control_value": "not-applicable",
            "difference": "",
            "status": "source-population-visible",
            "boundary": "Includes CUSIP-bearing and blank-CUSIP Part 2 rows identified by first-column geometry.",
        }
    ]
    for index, field in enumerate(CONTROL_VALUES, start=2):
        parsed = sum(numeric(row[field]) or 0 for row in rows)
        control = CONTROL_VALUES[field]
        diagnostics.append(
            {
                "diagnostic_id": f"CFAASBACP2-RECON-{index:03d}",
                "metric": field,
                "parser_value": str(parsed),
                "control_value": str(control),
                "difference": str(parsed - control),
                "status": "control-near-tie" if abs(parsed - control) <= 5 else "part2-population-or-column-review-open",
                "boundary": "Page-5829 Part 2 subtotal comparison; additions are not treated as year-end assets or owner cash.",
            }
        )
    with DIAGNOSTIC.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(diagnostics[0]))
        writer.writeheader()
        writer.writerows(diagnostics)

    print(f"wrote {len(rows)} coordinate rows to {OUT.relative_to(ROOT)}")
    for row in diagnostics[1:]:
        print(f"{row['metric']}={row['parser_value']} control={row['control_value']} difference={row['difference']}")
    print(f"wrote {len(diagnostics)} diagnostics to {DIAGNOSTIC.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
