#!/usr/bin/env python3
"""Classify sparse Schedule D value fields before any ABS imputation."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-full-range-parser-pass-1.csv"
OUTPUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-sparse-row-classification-pass-1.csv"
REPORT = ROOT / "analysis/company-first-principles/capital-flow-apollo-athene-statutory-sparse-row-classification-pass-1.md"

VALUE_FIELDS = (
    "actual_cost",
    "par_value",
    "fair_value",
    "book_adjusted_carrying_value",
)


def classify(row: dict[str, str]) -> tuple[str, str]:
    text = row["issuer_or_description"].lower()
    missing = sum(not row[field].strip() for field in VALUE_FIELDS)
    if missing == 0:
        return "complete-value-row", "no-sparse-value-review"
    if "nim" in text or "net interest margin" in text:
        return "source-visible-sparse-nim", "preserve-blanks-no-imputation"
    if "government national mortgage" in text or "mortgage" in text or "securit" in text:
        return "source-visible-or-legacy-abs-sparse", "row-level-source-review"
    return "non-nim-sparse-row", "high-priority-column-review"


def main() -> None:
    with INPUT.open(newline="") as handle:
        rows = list(csv.DictReader(handle))

    classified: list[dict[str, str]] = []
    by_page: defaultdict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        missing = sum(not row[field].strip() for field in VALUE_FIELDS)
        subtype, status = classify(row)
        by_page[row["page"]][subtype] += 1
        if missing:
            classified.append(
                {
                    "source_parser_row_id": row["normalized_row_id"],
                    "schedule": row["schedule"],
                    "page": row["page"],
                    "cusip": row["cusip"],
                    "issuer_or_description": row["issuer_or_description"],
                    "missing_value_field_count": str(missing),
                    "missing_value_fields": ";".join(field for field in VALUE_FIELDS if not row[field].strip()),
                    "sparse_subtype": subtype,
                    "review_status": status,
                    "boundary": "source-visible blanks must not be imputed; classification is a repair worklist, not final accounting evidence",
                }
            )

    fieldnames = list(classified[0]) if classified else [
        "source_parser_row_id", "schedule", "page", "cusip", "issuer_or_description",
        "missing_value_field_count", "missing_value_fields", "sparse_subtype",
        "review_status", "boundary",
    ]
    with OUTPUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(classified)

    counts = Counter(row["sparse_subtype"] for row in classified)
    page_counts = Counter(row["page"] for row in classified)
    high_pages = sorted(page_counts.items(), key=lambda item: (-item[1], int(item[0])))[:15]
    report = [
        "# Athene Schedule D Sparse-Row Classification Pass 1",
        "",
        "This worklist classifies rows with at least one blank among actual cost,",
        "par value, fair value, and book/adjusted carrying value. It does not fill",
        "or reinterpret blanks.",
        "",
        f"- Full parser rows: `{len(rows):,}`",
        f"- Sparse rows: `{len(classified):,}`",
        f"- Complete-value rows: `{len(rows) - len(classified):,}`",
        "",
        "## Classification counts",
        "",
        "| Classification | Rows | Treatment |",
        "|---|---:|---|",
        f"| `source-visible-sparse-nim` | {counts['source-visible-sparse-nim']:,} | Preserve blanks; no imputation. |",
        f"| `source-visible-or-legacy-abs-sparse` | {counts['source-visible-or-legacy-abs-sparse']:,} | Inspect source row and subtype. |",
        f"| `non-nim-sparse-row` | {counts['non-nim-sparse-row']:,} | Highest-priority column review. |",
        "",
        "## Largest sparse pages",
        "",
        "| Page | Sparse rows |",
        "|---:|---:|",
    ]
    report.extend(f"| {page} | {count:,} |" for page, count in high_pages)
    report.extend(
        [
            "",
            "## Boundary",
            "",
            "A source-visible blank is not zero, a parser error, or borrower cash.",
            "The output is a repair and review worklist only. Any corrected row",
            "must be checked against the source page and aggregate reconciliation",
            "before it can enter income, proceeds, liability-cost, or return work.",
            "",
            "Decision: `sparse-row-classification-created; no-imputation-gate-active`",
        ]
    )
    REPORT.write_text("\n".join(report) + "\n")
    print(f"wrote {len(classified)} sparse rows to {OUTPUT.relative_to(ROOT)}")
    print(f"wrote report to {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
