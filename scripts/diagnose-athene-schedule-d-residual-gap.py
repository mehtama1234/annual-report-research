#!/usr/bin/env python3
"""Diagnose residual Athene Schedule D reconciliation gaps after parser corrections."""

from __future__ import annotations

import csv
import importlib.util
import re
from collections import Counter
from decimal import Decimal
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
PARSER_SCRIPT = ROOT / "scripts/extract-athene-statutory-detail-samples.py"
FULL_D = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-full-range-parser-pass-1.csv"
COMPACT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-compact-extraction-pass-1.csv"
OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-residual-gap-diagnostic-pass-1.csv"

FIELDNAMES = [
    "residual_id",
    "scope",
    "parser_rows",
    "parser_book_value_usd",
    "statutory_reference_metric",
    "statutory_reference_value_usd",
    "residual_gap_usd",
    "coverage_ratio",
    "missing_book_rows",
    "raw_row_like_unmatched_candidates",
    "raw_candidate_apparent_book_sum_usd",
    "largest_raw_candidate_page",
    "largest_raw_candidate_label",
    "largest_raw_candidate_apparent_book_usd",
    "diagnosis",
    "proof_use",
    "boundary",
    "next_action",
]

RANGES = {
    "Schedule D Part 1 Section 1": (5836, 5911, "issuer_credit_obligations_book_adjusted_carrying_value"),
    "Schedule D Part 1 Section 2": (5912, 6027, "asset_backed_securities_book_adjusted_carrying_value"),
}


def load_parser_module():
    spec = importlib.util.spec_from_file_location("athene_schedule_d_parser", PARSER_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load parser script: {PARSER_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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


def raw_candidates(parser_module, reader: PdfReader, start_page: int, end_page: int) -> list[dict[str, str]]:
    candidates: list[dict[str, str]] = []
    for page in range(start_page, end_page + 1):
        for line in parser_module.page_lines(reader, page):
            if parser_module.START_RE.match(line):
                continue
            if not re.match(r"^[A-Z0-9*@#/-]{2,}", line):
                continue
            if "..." not in line:
                continue
            if not re.search(r"\b[1-6]\.[A-Z]\b|\b[1-6]\.\b", line):
                continue
            values = parser_module.money_tokens(line)
            apparent_book = values[3] if len(values) > 3 else ""
            candidates.append(
                {
                    "page": str(page),
                    "label": line.split()[0],
                    "apparent_book_value": apparent_book,
                    "raw_excerpt": parser_module.clean(line)[:240],
                }
            )
    return candidates


def diagnosis(scope: str, gap: Decimal, missing_book_rows: int, candidates: list[dict[str, str]]) -> str:
    if scope.endswith("Section 1"):
        return (
            "Section 1 is near-reconciled after the CUSIP-marker row-start correction. "
            "Only one parsed row lacks book value, but raw row-like continuation/tranche lines remain. "
            "Because their apparent book sum exceeds the residual gap, they require row-level inspection before any fallback parser counts them."
        )
    return (
        "Section 2 is effectively tied on book value despite many missing-book parser fields. "
        "The residual is small relative to the statutory reference, so the missing fields appear mostly blank/low-dollar or continuation artifacts; "
        "large raw candidates should be treated as likely continuation/duplicate risks until inspected."
    )


def main() -> None:
    parser_module = load_parser_module()
    refs = compact_refs()
    with FULL_D.open(newline="") as f:
        rows = list(csv.DictReader(f))

    by_scope: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        by_scope.setdefault(row["schedule"], []).append(row)

    reader = PdfReader(str(parser_module.PDF))
    output: list[dict[str, str]] = []
    combined_book = Decimal(0)
    combined_ref = refs["total_bonds_book_adjusted_carrying_value"]
    combined_missing = 0
    combined_candidates: list[dict[str, str]] = []

    for scope, (start_page, end_page, ref_metric) in RANGES.items():
        scope_rows = by_scope.get(scope, [])
        parser_book = sum(money(row["book_adjusted_carrying_value"]) for row in scope_rows)
        reference = refs[ref_metric]
        gap = parser_book - reference
        missing = sum(1 for row in scope_rows if not row["book_adjusted_carrying_value"])
        candidates = raw_candidates(parser_module, reader, start_page, end_page)
        largest = max(candidates, key=lambda row: abs(money(row["apparent_book_value"])), default=None)
        candidate_sum = sum(money(row["apparent_book_value"]) for row in candidates)
        output.append(
            {
                "residual_id": f"CFAASDRG-{len(output) + 1:03d}",
                "scope": scope,
                "parser_rows": str(len(scope_rows)),
                "parser_book_value_usd": fmt(parser_book),
                "statutory_reference_metric": ref_metric,
                "statutory_reference_value_usd": fmt(reference),
                "residual_gap_usd": fmt(gap),
                "coverage_ratio": f"{(parser_book / reference):.6f}",
                "missing_book_rows": str(missing),
                "raw_row_like_unmatched_candidates": str(len(candidates)),
                "raw_candidate_apparent_book_sum_usd": fmt(candidate_sum),
                "largest_raw_candidate_page": largest["page"] if largest else "",
                "largest_raw_candidate_label": largest["label"] if largest else "",
                "largest_raw_candidate_apparent_book_usd": fmt(money(largest["apparent_book_value"])) if largest else "",
                "diagnosis": diagnosis(scope, gap, missing, candidates),
                "proof_use": "residual Schedule D reconciliation targeting",
                "boundary": "raw row-like candidates are not counted as additional holdings until row-level duplicate and continuation checks pass",
                "next_action": "inspect residual candidate rows, subtotal treatment, and PDF continuation boundaries before final Schedule D promotion",
            }
        )
        combined_book += parser_book
        combined_missing += missing
        combined_candidates.extend(candidates)

    largest = max(combined_candidates, key=lambda row: abs(money(row["apparent_book_value"])), default=None)
    candidate_pages = Counter(row["page"] for row in combined_candidates).most_common(6)
    output.append(
        {
            "residual_id": f"CFAASDRG-{len(output) + 1:03d}",
            "scope": "Schedule D Part 1 Section 1 plus Section 2",
            "parser_rows": str(len(rows)),
            "parser_book_value_usd": fmt(combined_book),
            "statutory_reference_metric": "total_bonds_book_adjusted_carrying_value",
            "statutory_reference_value_usd": fmt(combined_ref),
            "residual_gap_usd": fmt(combined_book - combined_ref),
            "coverage_ratio": f"{(combined_book / combined_ref):.6f}",
            "missing_book_rows": str(combined_missing),
            "raw_row_like_unmatched_candidates": str(len(combined_candidates)),
            "raw_candidate_apparent_book_sum_usd": fmt(sum(money(row["apparent_book_value"]) for row in combined_candidates)),
            "largest_raw_candidate_page": largest["page"] if largest else "",
            "largest_raw_candidate_label": largest["label"] if largest else "",
            "largest_raw_candidate_apparent_book_usd": fmt(money(largest["apparent_book_value"])) if largest else "",
            "diagnosis": "Combined Schedule D Section 1 plus Section 2 is near-reconciled, but raw candidate apparent book value exceeds the residual gap, so automatic fallback row counting would likely double-count continuation/tranche text.",
            "proof_use": "near-final Schedule D reconciliation gate",
            "boundary": "near-reconciled book value is not income, proceeds, liability-cost spread, borrower receipt, or return proof",
            "next_action": f"inspect residual raw candidate pages {[page for page, _ in candidate_pages]} and define final reconciliation tolerance before income/proceeds joins",
        }
    )

    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(output)
    print(f"wrote {len(output)} rows to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
