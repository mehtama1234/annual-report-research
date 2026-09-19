#!/usr/bin/env python3
"""Prioritize named Schedule BA Part 1 rows by coordinate-extracted income."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PART1 = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-part1-coordinate-parser-pass-1.csv"
PART3 = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-part3-coordinate-parser-pass-1.csv"
OUT_CSV = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-part1-income-review-queue-pass-1.csv"
OUT_MD = ROOT / "analysis/company-first-principles/capital-flow-apollo-athene-statutory-schedule-ba-part1-income-review-queue-pass-1.md"
CONTROL = 237_086_005


def integer(value: str) -> int:
    return int((value or "0").replace(",", "").replace("(", "-").replace(")", ""))


def money(value: int) -> str:
    return f"$({abs(value):,})" if value < 0 else f"${value:,}"


def main() -> None:
    with PART1.open() as handle:
        source = list(csv.DictReader(handle))
    part3_by_id = {}
    with PART3.open() as handle:
        for row in csv.DictReader(handle):
            identifier = row["cusip_or_identifier"]
            if not identifier:
                continue
            part3_by_id.setdefault(identifier, []).append(row)
    for row in source:
        row["income_int"] = integer(row["investment_income"])
        row["book_int"] = integer(row["book_adjusted_carrying_value"])
    positives = sorted((row for row in source if row["income_int"] > 0), key=lambda row: row["income_int"], reverse=True)
    selected = positives[:30]
    fields = ["rank", "page", "cusip_or_identifier", "name_or_description_near_row", "book_value", "investment_income", "income_to_book_screen", "part3_event_count", "part3_consideration_sum", "part3_book_value_sum", "part3_nature_signals", "current_year_other_than_temporary_impairment", "boundary"]
    output = []
    for rank, row in enumerate(selected, start=1):
        ratio = row["income_int"] / row["book_int"] if row["book_int"] else 0
        events = part3_by_id.get(row["cusip_or_identifier"], []) if row["cusip_or_identifier"] else []
        part3_consideration = sum(integer(event["disposal_consideration"]) for event in events)
        part3_book = sum(integer(event["book_adjusted_carrying_value_on_disposal"]) for event in events)
        nature_signals = ";".join(sorted({event.get("disposal_nature_source_column", "") for event in events if event.get("disposal_nature_source_column", "")}))
        output.append({
            "rank": str(rank),
            "page": row["page"],
            "cusip_or_identifier": row["cusip_or_identifier"],
            "name_or_description_near_row": row["name_or_description_near_row"],
            "book_value": money(row["book_int"]),
            "investment_income": money(row["income_int"]),
            "income_to_book_screen": f"{ratio:.2%}" if ratio else "",
            "part3_event_count": str(len(events)),
            "part3_consideration_sum": money(part3_consideration) if events else "",
            "part3_book_value_sum": money(part3_book) if events else "",
            "part3_nature_signals": nature_signals,
            "current_year_other_than_temporary_impairment": row["current_year_other_than_temporary_impairment"],
            "boundary": "Coordinate-extracted Schedule BA Part 1 income field; not collected cash, borrower repayment, liability-adjusted spread, or Apollo owner cash.",
        })
    with OUT_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output)
    top_sum = sum(row["income_int"] for row in selected)
    all_sum = sum(row["income_int"] for row in source)
    lines = [
        "# Apollo/Athene Schedule BA Part 1 income review queue pass 1",
        "",
        f"The coordinate parser reconciles Part 1 investment income to `{money(all_sum)}` against the page-5825 control `{money(CONTROL)}`. The top 30 positive rows contribute `{money(top_sum)}` (`{top_sum / all_sum:.2%}` of the parsed positive total).",
        "",
        "| rank | page | identifier | name | book value | income | income/book | Part 3 events | Part 3 consideration | Part 3 nature |",
        "|---:|---:|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in output:
        lines.append(f"| {row['rank']} | {row['page']} | `{row['cusip_or_identifier'] or 'blank'}` | {row['name_or_description_near_row'][:90].replace('|', '/')} | {row['book_value']} | {row['investment_income']} | {row['income_to_book_screen']} | {row['part3_event_count']} | {row['part3_consideration_sum'] or '—'} | {row['part3_nature_signals'] or '—'} |")
    lines.extend([
        "",
        "## Interpretation boundary",
        "",
        "This queue identifies where the Part 1 statutory income field is concentrated and whether an identifier has a visible Part 3 event. It does not resolve the page-18 Other invested assets category mismatch, does not prove income was collected in cash, and does not identify the ultimate borrower or liability-cost spread. The four source-sparse book cells remain blank and no values are imputed.",
        "",
        "The underlying controlled population is [capital-flow-apollo-athene-statutory-schedule-ba-part1-coordinate-parser-pass-1.csv](data/capital-flow-apollo-athene-statutory-schedule-ba-part1-coordinate-parser-pass-1.csv).",
    ])
    OUT_MD.write_text("\n".join(lines) + "\n")
    print(f"wrote {len(output)} income-review rows to {OUT_CSV.relative_to(ROOT)}")
    print(f"part1-income={all_sum} control={CONTROL} top30={top_sum}")
    print(f"wrote note to {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
