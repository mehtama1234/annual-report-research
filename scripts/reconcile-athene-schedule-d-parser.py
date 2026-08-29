#!/usr/bin/env python3
"""Build reconciliation diagnostics for Athene Schedule D parser output."""

from __future__ import annotations

import csv
from collections import Counter
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FULL_D = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-full-range-parser-pass-1.csv"
COMPACT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-compact-extraction-pass-1.csv"
OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-reconciliation-diagnostic-pass-1.csv"
PAGE_OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-page-diagnostic-pass-1.csv"

FIELDNAMES = [
    "diagnostic_id",
    "diagnostic_type",
    "schedule_scope",
    "parser_metric",
    "parser_value",
    "statutory_reference_metric",
    "statutory_reference_value",
    "difference_value",
    "coverage_ratio",
    "current_status",
    "proof_use",
    "boundary",
    "next_action",
]

PAGE_FIELDNAMES = [
    "page_diagnostic_id",
    "schedule",
    "page",
    "located_page_range",
    "parser_row_count",
    "rows_with_naic_designation",
    "rows_with_actual_cost",
    "rows_with_fair_value",
    "rows_with_book_adjusted_carrying_value",
    "rows_with_maturity_date",
    "missing_book_value_rows",
    "book_value_coverage_ratio",
    "actual_cost_sum_usd",
    "fair_value_sum_usd",
    "book_adjusted_carrying_value_sum_usd",
    "largest_book_value_row_id",
    "largest_book_value_usd",
    "current_status",
    "proof_use",
    "boundary",
    "next_action",
]


def money(value: str) -> Decimal:
    if not value:
        return Decimal(0)
    negative = value.startswith("(") and value.endswith(")")
    cleaned = value.strip("()").replace(",", "")
    try:
        parsed = Decimal(cleaned)
    except Exception:
        return Decimal(0)
    return -parsed if negative else parsed


def fmt(value: Decimal) -> str:
    return f"{value:.6f}"


def compact_refs() -> dict[str, Decimal]:
    refs: dict[str, Decimal] = {}
    with COMPACT.open(newline="") as f:
        for row in csv.DictReader(f):
            if row["units"] == "B USD":
                refs[row["metric_name"]] = Decimal(row["metric_value"]) * Decimal("1000000000")
    return refs


def add_row(
    rows: list[dict[str, str]],
    diagnostic_type: str,
    schedule_scope: str,
    parser_metric: str,
    parser_value: str,
    statutory_reference_metric: str,
    statutory_reference_value: str,
    difference_value: str,
    coverage_ratio: str,
    current_status: str,
    proof_use: str,
    boundary: str,
    next_action: str,
) -> None:
    rows.append(
        {
            "diagnostic_id": f"CFAASDRD-{len(rows) + 1:03d}",
            "diagnostic_type": diagnostic_type,
            "schedule_scope": schedule_scope,
            "parser_metric": parser_metric,
            "parser_value": parser_value,
            "statutory_reference_metric": statutory_reference_metric,
            "statutory_reference_value": statutory_reference_value,
            "difference_value": difference_value,
            "coverage_ratio": coverage_ratio,
            "current_status": current_status,
            "proof_use": proof_use,
            "boundary": boundary,
            "next_action": next_action,
        }
    )


def page_status(row_count: int, book_coverage: Decimal) -> tuple[str, str]:
    if row_count == 0:
        return "no-parser-rows", "inspect page for subtotal, blank terminal page, or missed row boundary"
    if book_coverage < Decimal("0.80"):
        return "high-priority-column-correction", "inspect raw PDF text and correct book-value column assignment"
    if book_coverage < Decimal("0.95"):
        return "medium-priority-column-correction", "sample rows with missing book value and wrapped numeric columns"
    return "page-parser-coverage-visible", "use in reconciliation after section-level totals are corrected"


def write_page_diagnostics(rows: list[dict[str, str]]) -> None:
    by_page: dict[tuple[str, int], list[dict[str, str]]] = {}
    for row in rows:
        by_page.setdefault((row["schedule"], int(row["page"])), []).append(row)

    ranges = {
        "Schedule D Part 1 Section 1": (5836, 5911),
        "Schedule D Part 1 Section 2": (5912, 6027),
    }
    output: list[dict[str, str]] = []
    for schedule, (start_page, end_page) in ranges.items():
        for page in range(start_page, end_page + 1):
            page_rows = by_page.get((schedule, page), [])
            row_count = len(page_rows)
            with_book = [row for row in page_rows if row["book_adjusted_carrying_value"]]
            book_coverage = Decimal(len(with_book)) / Decimal(row_count) if row_count else Decimal(0)
            largest = max(with_book, key=lambda row: abs(money(row["book_adjusted_carrying_value"])), default=None)
            status, next_action = page_status(row_count, book_coverage)
            output.append(
                {
                    "page_diagnostic_id": f"CFAASDPD-{len(output) + 1:03d}",
                    "schedule": schedule,
                    "page": str(page),
                    "located_page_range": f"{start_page}-{end_page}",
                    "parser_row_count": str(row_count),
                    "rows_with_naic_designation": str(sum(1 for row in page_rows if row["naic_designation"])),
                    "rows_with_actual_cost": str(sum(1 for row in page_rows if row["actual_cost"])),
                    "rows_with_fair_value": str(sum(1 for row in page_rows if row["fair_value"])),
                    "rows_with_book_adjusted_carrying_value": str(len(with_book)),
                    "rows_with_maturity_date": str(sum(1 for row in page_rows if row["maturity_date"])),
                    "missing_book_value_rows": str(row_count - len(with_book)),
                    "book_value_coverage_ratio": f"{book_coverage:.6f}",
                    "actual_cost_sum_usd": fmt(sum(money(row["actual_cost"]) for row in page_rows)),
                    "fair_value_sum_usd": fmt(sum(money(row["fair_value"]) for row in page_rows)),
                    "book_adjusted_carrying_value_sum_usd": fmt(sum(money(row["book_adjusted_carrying_value"]) for row in page_rows)),
                    "largest_book_value_row_id": largest["normalized_row_id"] if largest else "",
                    "largest_book_value_usd": fmt(money(largest["book_adjusted_carrying_value"])) if largest else "",
                    "current_status": status,
                    "proof_use": "page-level parser correction targeting",
                    "boundary": "page coverage is a parser diagnostic and does not prove reconciled statutory totals",
                    "next_action": next_action,
                }
            )

    with PAGE_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=PAGE_FIELDNAMES)
        writer.writeheader()
        writer.writerows(output)

    print(f"wrote {len(output)} rows to {PAGE_OUT.relative_to(ROOT)}")


def main() -> None:
    refs = compact_refs()
    with FULL_D.open(newline="") as f:
        rows = list(csv.DictReader(f))

    by_schedule: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        by_schedule.setdefault(row["schedule"], []).append(row)

    diagnostics: list[dict[str, str]] = []
    section_refs = {
        "Schedule D Part 1 Section 1": "issuer_credit_obligations_book_adjusted_carrying_value",
        "Schedule D Part 1 Section 2": "asset_backed_securities_book_adjusted_carrying_value",
    }

    for schedule, ref_name in section_refs.items():
        schedule_rows = by_schedule.get(schedule, [])
        parser_book = sum(money(row["book_adjusted_carrying_value"]) for row in schedule_rows)
        reference = refs[ref_name]
        difference = parser_book - reference
        ratio = parser_book / reference if reference else Decimal(0)
        add_row(
            diagnostics,
            "book-value-reconciliation",
            schedule,
            "parser_book_adjusted_carrying_value_sum_usd",
            fmt(parser_book),
            ref_name,
            fmt(reference),
            fmt(difference),
            f"{ratio:.6f}",
            "not-reconciled",
            "quantifies parser gap against statutory Schedule D bucket",
            "positional parser book-value fields do not yet reconcile to statutory verification totals",
            "improve row boundary and numeric-column assignment then rerun reconciliation",
        )

    combined = by_schedule.get("Schedule D Part 1 Section 1", []) + by_schedule.get("Schedule D Part 1 Section 2", [])
    combined_book = sum(money(row["book_adjusted_carrying_value"]) for row in combined)
    total_ref = refs["total_bonds_book_adjusted_carrying_value"]
    add_row(
        diagnostics,
        "book-value-reconciliation",
        "Schedule D Part 1 Section 1 plus Section 2",
        "combined_parser_book_adjusted_carrying_value_sum_usd",
        fmt(combined_book),
        "total_bonds_book_adjusted_carrying_value",
        fmt(total_ref),
        fmt(combined_book - total_ref),
        f"{(combined_book / total_ref):.6f}",
        "not-reconciled",
        "tests whether parsed issuer-credit plus ABS rows approach the total Schedule D bond base",
        "Schedule D also contains other sections and parser positional fields remain unreconciled",
        "add remaining Schedule D sections or reconcile Section 1 and Section 2 before total comparison use",
    )

    schedule_counts = Counter(row["schedule"] for row in rows)
    for schedule in section_refs:
        add_row(
            diagnostics,
            "row-count",
            schedule,
            "parser_row_count",
            str(schedule_counts[schedule]),
            "located_page_range",
            "range-located",
            "",
            "",
            "row-population-visible",
            "confirms full located range generated row population",
            "row count alone does not prove complete statutory population",
            "compare page-level row counts against PDF table breaks and subtotal pages",
        )

    for field in ["naic_designation", "actual_cost", "fair_value", "book_adjusted_carrying_value", "maturity_date"]:
        present = sum(1 for row in rows if row[field])
        ratio = Decimal(present) / Decimal(len(rows))
        add_row(
            diagnostics,
            "field-coverage",
            "Schedule D Part 1 Section 1 plus Section 2",
            f"rows_with_{field}",
            str(present),
            "parser_rows",
            str(len(rows)),
            str(present - len(rows)),
            f"{ratio:.6f}",
            "coverage-measured",
            "shows which fields are populated enough for the next reconciliation pass",
            "coverage does not prove field accuracy because dense PDF columns may be positionally shifted",
            "sample inspect missing and high-gap rows before final accounting use",
        )

    pages = [int(row["page"]) for row in rows]
    add_row(
        diagnostics,
        "page-coverage",
        "Schedule D Part 1 Section 1 plus Section 2",
        "parser_page_min_to_max",
        f"{min(pages)}-{max(pages)}",
        "located_page_range",
        "5836-6027",
        "page 6027 produced no parsed rows",
        "",
        "page-coverage-measured",
        "confirms parser executed the located range and shows where parsed rows actually appeared",
        "empty terminal pages or subtotal pages may be valid but need manual confirmation",
        "inspect page 6027 and subtotal boundaries",
    )

    add_row(
        diagnostics,
        "decision",
        "Schedule D Part 1 Section 1 plus Section 2",
        "reconciliation_status",
        "full-range-parser-visible-not-reconciled",
        "promotion_gate",
        "reconciled-to-statutory-verification-totals",
        "gate not passed",
        "",
        "reconciliation-hold",
        "prevents overclaiming named holdings as final statutory accounting proof",
        "bulk extraction is useful but below cash-return or spread-proof grade",
        "build row-boundary and numeric-column correction pass",
    )

    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(diagnostics)

    print(f"wrote {len(diagnostics)} rows to {OUT.relative_to(ROOT)}")
    write_page_diagnostics(rows)


if __name__ == "__main__":
    main()
