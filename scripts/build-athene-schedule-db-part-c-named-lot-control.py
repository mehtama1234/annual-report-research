#!/usr/bin/env python3
"""Build a conservative named-instrument Part C to Schedule D control ledger.

This is an exposure/identity control, not a settlement or owner-cash bridge.
Part C component values are aggregated only when the source row exposes one
unambiguous numeric candidate. Ambiguous alternatives remain visible and are
excluded from the numeric aggregate rather than being guessed.
"""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
PART_C = DATA / "capital-flow-apollo-athene-statutory-schedule-db-part-c-ledger-pass-1.csv"
SCHEDULE_D = DATA / "capital-flow-apollo-athene-statutory-schedule-d-full-range-parser-pass-1.csv"
CROSSWALK = DATA / "capital-flow-apollo-athene-statutory-schedule-db-part-c-schedule-d-crosswalk-pass-1.csv"
OUT = DATA / "capital-flow-apollo-athene-statutory-schedule-db-part-c-named-lot-control-pass-1.csv"
MEMO = ROOT / "analysis/company-first-principles/capital-flow-apollo-athene-statutory-schedule-db-part-c-named-lot-control-pass-1.md"

FIELDNAMES = [
    "control_id",
    "cash_instrument_cusip",
    "cash_instrument_description",
    "named_family",
    "part_c_row_count",
    "part_c_ledger_ids",
    "part_c_pages",
    "part_c_row_mapping_statuses",
    "part_c_book_candidate_rows_used",
    "part_c_book_candidate_rows_excluded_ambiguous",
    "part_c_book_candidate_sum_used",
    "part_c_fair_candidate_rows_used",
    "part_c_fair_candidate_rows_excluded_ambiguous",
    "part_c_fair_candidate_sum_used",
    "part_c_book_candidates_raw",
    "part_c_fair_candidates_raw",
    "schedule_d_row_count",
    "schedule_d_row_ids",
    "schedule_d_pages",
    "schedule_d_actual_cost_sum",
    "schedule_d_fair_value_sum",
    "schedule_d_book_value_sum",
    "schedule_d_interest_income_sum",
    "schedule_d_interest_received_sum",
    "part_c_book_vs_schedule_d_book_difference",
    "part_c_fair_vs_schedule_d_fair_difference",
    "numeric_control_status",
    "what_is_proven",
    "boundary",
    "next_proof",
]

FAMILY_PATTERNS = (
    ("MF1", re.compile(r"\bMF1\b", re.I)),
    ("AMAPS", re.compile(r"\bAMAPS\b", re.I)),
    ("ATLAS", re.compile(r"\bATLAS\b", re.I)),
    ("VARDE", re.compile(r"\bVARDE\b", re.I)),
    ("ARES", re.compile(r"\bARES\b", re.I)),
)


def number_candidates(raw: str) -> list[int]:
    values: list[int] = []
    for token in raw.split("|"):
        token = token.strip().replace(",", "")
        if token and re.fullmatch(r"-?\d+", token):
            values.append(int(token))
    return values


def amount(rows: list[dict[str, str]], field: str) -> int | None:
    values = [number_candidates(row[field]) for row in rows]
    values = [items[0] for items in values if len(items) == 1]
    return sum(values) if values else None


def fmt(value: int | None) -> str:
    return "" if value is None else f"{value:,}"


def sum_schedule(rows: list[dict[str, str]], field: str) -> int | None:
    values = [number_candidates(row[field]) for row in rows]
    values = [items[0] for items in values if len(items) == 1]
    return sum(values) if values else None


def family(description: str) -> str:
    for name, pattern in FAMILY_PATTERNS:
        if pattern.search(description):
            return name
    return "OTHER"


def main() -> None:
    with PART_C.open(newline="", encoding="utf-8") as handle:
        part_c = list(csv.DictReader(handle))
    with SCHEDULE_D.open(newline="", encoding="utf-8") as handle:
        schedule_d = list(csv.DictReader(handle))
    with CROSSWALK.open(newline="", encoding="utf-8") as handle:
        crosswalk = list(csv.DictReader(handle))

    schedule_by_cusip: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in schedule_d:
        schedule_by_cusip[row["cusip"].strip().upper()].append(row)

    part_by_cusip: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in part_c:
        cusip = row["cash_instrument_cusip"].strip().upper()
        if cusip and any(pattern.search(row["cash_instrument_description"]) for _, pattern in FAMILY_PATTERNS):
            part_by_cusip[cusip].append(row)

    # Keep the crosswalk as the identity inclusion control. This prevents a
    # malformed/private identifier from silently entering the named ledger.
    crosswalk_cusips = {row["cash_instrument_cusip"].strip().upper() for row in crosswalk}
    output: list[dict[str, str]] = []
    for cusip in sorted(part_by_cusip):
        if cusip not in crosswalk_cusips:
            continue
        p_rows = part_by_cusip[cusip]
        d_rows = schedule_by_cusip.get(cusip, [])
        descriptions = sorted({row["cash_instrument_description"].strip() for row in p_rows})
        description = " | ".join(descriptions)
        book_raw = [row["cash_instrument_book_value_candidates"] for row in p_rows if row["cash_instrument_book_value_candidates"]]
        fair_raw = [row["cash_instrument_fair_value_candidates"] for row in p_rows if row["cash_instrument_fair_value_candidates"]]
        book_used = [row for row in p_rows if len(number_candidates(row["cash_instrument_book_value_candidates"])) == 1]
        fair_used = [row for row in p_rows if len(number_candidates(row["cash_instrument_fair_value_candidates"])) == 1]
        book_excluded = [row for row in p_rows if len(number_candidates(row["cash_instrument_book_value_candidates"])) > 1]
        fair_excluded = [row for row in p_rows if len(number_candidates(row["cash_instrument_fair_value_candidates"])) > 1]
        p_book = amount(p_rows, "cash_instrument_book_value_candidates")
        p_fair = amount(p_rows, "cash_instrument_fair_value_candidates")
        d_book = sum_schedule(d_rows, "book_adjusted_carrying_value")
        d_fair = sum_schedule(d_rows, "fair_value")
        book_diff = p_book - d_book if p_book is not None and d_book is not None else None
        fair_diff = p_fair - d_fair if p_fair is not None and d_fair is not None else None
        if not d_rows:
            status = "identity-crosswalk-missing-schedule-d-row"
        elif book_excluded or fair_excluded:
            status = "matched-identity-with-ambiguous-part-c-candidate"
        elif p_book is None and p_fair is None:
            status = "matched-identity-without-component-numeric-candidate"
        else:
            status = "matched-identity-component-exposure-control"
        output.append(
            {
                "control_id": f"CFAASDBNLC-{len(output) + 1:04d}",
                "cash_instrument_cusip": cusip,
                "cash_instrument_description": description,
                "named_family": family(description),
                "part_c_row_count": str(len(p_rows)),
                "part_c_ledger_ids": " | ".join(row["ledger_id"] for row in p_rows),
                "part_c_pages": " | ".join(sorted({row["source_page"] for row in p_rows})),
                "part_c_row_mapping_statuses": " | ".join(sorted({row["row_mapping_status"] for row in p_rows})),
                "part_c_book_candidate_rows_used": str(len(book_used)),
                "part_c_book_candidate_rows_excluded_ambiguous": str(len(book_excluded)),
                "part_c_book_candidate_sum_used": fmt(p_book),
                "part_c_fair_candidate_rows_used": str(len(fair_used)),
                "part_c_fair_candidate_rows_excluded_ambiguous": str(len(fair_excluded)),
                "part_c_fair_candidate_sum_used": fmt(p_fair),
                "part_c_book_candidates_raw": " | ".join(book_raw),
                "part_c_fair_candidates_raw": " | ".join(fair_raw),
                "schedule_d_row_count": str(len(d_rows)),
                "schedule_d_row_ids": " | ".join(row["normalized_row_id"] for row in d_rows),
                "schedule_d_pages": " | ".join(sorted({row["page"] for row in d_rows})),
                "schedule_d_actual_cost_sum": fmt(sum_schedule(d_rows, "actual_cost")),
                "schedule_d_fair_value_sum": fmt(d_fair),
                "schedule_d_book_value_sum": fmt(d_book),
                "schedule_d_interest_income_sum": fmt(sum_schedule(d_rows, "interest_income")),
                "schedule_d_interest_received_sum": fmt(sum_schedule(d_rows, "interest_received_during_year")),
                "part_c_book_vs_schedule_d_book_difference": fmt(book_diff),
                "part_c_fair_vs_schedule_d_fair_difference": fmt(fair_diff),
                "numeric_control_status": status,
                "what_is_proven": "A named Part C cash-instrument component is identity-matched to one or more Schedule D rows; unambiguous component candidates and statutory book/fair/income/received fields are shown side by side.",
                "boundary": "The Part C component is not assumed to equal the full Schedule D holding. Differences may reflect replication structure, parent/component presentation, column sparsity, or lot perimeter. No field proves derivative settlement, custody remittance, policyholder-liability allocation, borrower repayment, or Apollo common-owner cash.",
                "next_proof": "Obtain page-level source-column confirmation and a custody, counterparty, settlement/remittance, hedged-liability, and asset-income allocation record for the selected lot.",
            }
        )

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output)

    counts: dict[str, int] = defaultdict(int)
    families: dict[str, int] = defaultdict(int)
    for row in output:
        counts[row["numeric_control_status"]] += 1
        families[row["named_family"]] += 1
    lines = [
        "# Apollo/Athene Schedule DB Part C named-lot control — pass 1",
        "",
        "This control ledger narrows the exact-CUSIP crosswalk to named MF1, AMAPS, Atlas, Varde, and Ares instruments. It is an exposure and identity control, not a settlement, liability-allocation, repayment, or Apollo-owner-cash bridge.",
        "",
        f"- Included `{len(output)}` named CUSIP controls from the Part C ↔ Schedule D crosswalk.",
        f"- Families: " + ", ".join(f"{key} `{value}`" for key, value in sorted(families.items())) + ".",
        f"- Statuses: " + ", ".join(f"`{key}` `{value}`" for key, value in sorted(counts.items())) + ".",
        "- Part C values are summed only when a row exposes one unambiguous numeric candidate. Pipe-separated alternatives remain in the raw columns and are excluded from the numeric aggregate.",
        "- A difference between a Part C component and a Schedule D holding is not treated as an error or a cash-flow match; it is a perimeter/control signal because Part C presents replication components while Schedule D presents statutory holdings.",
        "",
        "## What this advances",
        "",
        "The ledger gives the next reviewer a reproducible page/CUSIP queue: named derivative component, Schedule D row, statutory book/fair value, interest income, and interest received. It identifies where a custody or transaction-level document could connect a derivative component to a legal-entity cash or liability bridge.",
        "",
        "## What remains unproven",
        "",
        "- derivative cash settlement and counterparty remittance;",
        "- whether Schedule D interest received was collected into Athene cash for the matched lot;",
        "- policyholder-liability or product-level hedge-cost allocation;",
        "- borrower/project repayment or asset-level return; and",
        "- cash available to Apollo common owners.",
        "",
        "The machine-readable ledger is [here](data/capital-flow-apollo-athene-statutory-schedule-db-part-c-named-lot-control-pass-1.csv).",
    ]
    MEMO.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {len(output)} named controls; statuses={dict(sorted(counts.items()))}")


if __name__ == "__main__":
    main()
