#!/usr/bin/env python3
"""Prioritize explicitly labeled Schedule BA Part 3 sale events."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PART3 = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-part3-coordinate-parser-pass-1.csv"
RAW = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-full-range-parser-pass-1.csv"
CONTINUITY = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-event-continuity-ledger-pass-1.csv"
OUT_CSV = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-sale-review-queue-pass-1.csv"
OUT_MD = ROOT / "analysis/company-first-principles/capital-flow-apollo-athene-statutory-schedule-ba-sale-review-queue-pass-1.md"


def integer(value: str) -> int:
    return int((value or "0").replace(",", "").replace("(", "-").replace(")", ""))


def money(value: str) -> str:
    number = integer(value)
    return f"$({abs(number):,})" if number < 0 else f"${number:,}"


def main() -> None:
    continuity_by_key = {}
    with CONTINUITY.open() as handle:
        for row in csv.DictReader(handle):
            continuity_by_key[(row["part3_page"], row["cusip_or_identifier"])] = row
    selected = []
    with PART3.open() as handle:
        for row in csv.DictReader(handle):
            nature = row.get("disposal_nature_source_column", "")
            if nature != "Sale":
                continue
            continuity = continuity_by_key.get((row["page"], row["cusip_or_identifier"]), {})
            selected.append({
                "page": row["page"],
                "cusip_or_identifier": row["cusip_or_identifier"],
                "name": row["name_or_description_near_row"],
                "book_value": row["book_adjusted_carrying_value_on_disposal"],
                "consideration": row["disposal_consideration"],
                "gain_loss": row["total_gain_loss_on_disposal"],
                "investment_income": row["investment_income"],
                "acquisition_date": row.get("acquisition_date_source_column", ""),
                "disposal_date": row.get("disposal_date_source_column", ""),
                "part1_pages": continuity.get("part1_pages", ""),
                "part2_pages": continuity.get("part2_pages", ""),
                "continuity_status": continuity.get("continuity_status", ""),
                "source_terms": nature,
                "boundary": "Explicit Sale label and coordinate-extracted Schedule BA consideration; not settlement-account, borrower-repayment, legal-entity cash, or Apollo owner-cash proof.",
            })
    selected.sort(key=lambda row: integer(row["consideration"]), reverse=True)
    fields = list(selected[0]) if selected else ["page"]
    with OUT_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(selected)
    lines = [
        "# Apollo/Athene Schedule BA explicitly labeled Sale review queue pass 1",
        "",
        f"The corrected Part 3 coordinate ledger contains `{len(selected)}` rows whose PDF-coordinate disposal-nature column equals `Sale`, excluding rows classified as `Partial Sale`. They are sorted by coordinate-extracted disposal consideration.",
        "",
        "| page | identifier | name | acquisition → disposal | Part 1 pages | Part 2 pages | book on disposal | consideration | gain/loss | continuity |",
        "|---:|---|---|---|---|---|---:|---:|---:|---|",
    ]
    for row in selected:
        lines.append(f"| {row['page']} | `{row['cusip_or_identifier'] or 'blank'}` | {row['name'][:80].replace('|', '/')} | {row['acquisition_date']} → {row['disposal_date']} | {row['part1_pages'] or '—'} | {row['part2_pages'] or '—'} | {money(row['book_value'])} | {money(row['consideration'])} | {money(row['gain_loss'])} | {row['continuity_status'] or 'no identifier continuity'} |")
    lines.extend([
        "",
        "## Use and stop rule",
        "",
        "Use this queue to select primary-document follow-up targets. The `Sale` label identifies a statutory disposition type, not a bank receipt. Before promoting any row, locate counterparty/settlement evidence, determine whether it is a full or partial lot disposition, identify any liability release or tax/fee deduction, and reconcile the legal-entity cash flow. Do not infer Apollo cash from Athene consideration.",
        "",
        "The underlying controlled Part 3 ledger is [capital-flow-apollo-athene-statutory-schedule-ba-part3-coordinate-parser-pass-1.csv](data/capital-flow-apollo-athene-statutory-schedule-ba-part3-coordinate-parser-pass-1.csv).",
    ])
    OUT_MD.write_text("\n".join(lines) + "\n")
    print(f"wrote {len(selected)} explicit-sale rows to {OUT_CSV.relative_to(ROOT)}")
    print(f"total-sale-consideration={sum(integer(row['consideration']) for row in selected)}")
    print(f"wrote review note to {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
