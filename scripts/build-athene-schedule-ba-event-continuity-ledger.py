#!/usr/bin/env python3
"""Join Schedule BA Part 3 events to Part 1 holdings and Part 2 additions."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PART1 = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-part1-coordinate-parser-pass-1.csv"
PART2 = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-part2-coordinate-parser-pass-1.csv"
PART3 = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-part3-coordinate-parser-pass-1.csv"
OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-event-continuity-ledger-pass-1.csv"
SUMMARY = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-event-continuity-summary-pass-1.csv"


def integer(value: str) -> int:
    if not value:
        return 0
    return int(value.replace(",", "").replace("(", "-").replace(")", ""))


def index(path: Path) -> dict[str, list[dict[str, str]]]:
    result: dict[str, list[dict[str, str]]] = defaultdict(list)
    with path.open() as handle:
        for row in csv.DictReader(handle):
            if row["cusip_or_identifier"]:
                result[row["cusip_or_identifier"]].append(row)
    return result


def main() -> None:
    part1 = index(PART1)
    part2 = index(PART2)
    with PART3.open() as handle:
        part3 = list(csv.DictReader(handle))

    rows = []
    status_counts: Counter[str] = Counter()
    for sequence, event in enumerate(part3, start=1):
        identifier = event["cusip_or_identifier"]
        p1 = part1.get(identifier, []) if identifier else []
        p2 = part2.get(identifier, []) if identifier else []
        if not identifier:
            status = "blank-cusip-event-no-continuity-key"
        elif p1 and p2:
            status = "same-cusip-part1-and-part2-and-part3-visible"
        elif p1:
            status = "same-cusip-part1-and-part3-visible"
        elif p2:
            status = "same-cusip-part2-and-part3-visible"
        else:
            status = "part3-cusip-no-part1-or-part2-match"
        status_counts[status] += 1
        part1_book_value_sum = sum(integer(row["book_adjusted_carrying_value"]) for row in p1)
        part3_book_value = integer(event["book_adjusted_carrying_value_on_disposal"])
        part1_book_delta = part3_book_value - part1_book_value_sum if p1 else 0
        if not p1:
            amount_screen = "no-part1-amount-screen"
        elif abs(part1_book_delta) <= 1:
            amount_screen = "part3-book-vs-part1-book-exact-within-1"
        elif abs(part1_book_delta) <= 1_000_000:
            amount_screen = "part3-book-vs-part1-book-near-within-1m"
        else:
            amount_screen = "part3-book-vs-part1-book-large-or-multi-lot-delta"
        rows.append(
            {
                "continuity_id": f"CFAASBACONT-{sequence:04d}",
                "part3_parser_row_id": event["parser_row_id"],
                "part3_page": event["page"],
                "cusip_or_identifier": identifier,
                "part3_name": event["name_or_description_near_row"],
                "book_value_on_disposal": event["book_adjusted_carrying_value_on_disposal"],
                "disposal_consideration": event["disposal_consideration"],
                "total_gain_loss_on_disposal": event["total_gain_loss_on_disposal"],
                "part3_investment_income": event["investment_income"],
                "part1_match_count": str(len(p1)),
                "part1_pages": ";".join(sorted({row["page"] for row in p1})),
                "part1_book_value_sum": str(part1_book_value_sum),
                "part3_book_minus_part1_book": str(part1_book_delta),
                "part3_vs_part1_amount_screen": amount_screen,
                "part2_match_count": str(len(p2)),
                "part2_pages": ";".join(sorted({row["page"] for row in p2})),
                "part2_acquisition_cost_sum": str(sum(integer(row["actual_cost_at_time_of_acquisition"]) for row in p2)),
                "part2_additional_investment_sum": str(sum(integer(row["additional_investment_made_after_acquisition"]) for row in p2)),
                "continuity_status": status,
                "boundary": "Statutory same-identifier continuity only; consideration is not bank settlement, borrower repayment, liability release, or Apollo owner cash.",
            }
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    total_consideration = sum(integer(row["disposal_consideration"]) for row in part3)
    total_book_on_disposal = sum(integer(row["book_adjusted_carrying_value_on_disposal"]) for row in part3)
    summary_rows = [
        {"metric": "part3-coordinate-event-rows", "value": str(len(part3)), "status": "source-visible", "boundary": "Coordinate rows across corrected Part 3 pages 5830-5835; Schedule D starts at page 5836."},
        {"metric": "total-disposal-consideration-visible", "value": str(total_consideration), "status": "statutory-consideration-visible", "boundary": "Not proven bank receipt or owner cash."},
        {"metric": "total-book-value-on-disposal-visible", "value": str(total_book_on_disposal), "status": "statutory-disposal-book-value-visible", "boundary": "Not a realized cash or return measure by itself."},
    ]
    for status, count in sorted(status_counts.items()):
        summary_rows.append({"metric": f"continuity-status:{status}", "value": str(count), "status": "classified", "boundary": "Identifier matching only; no lot-level or settlement inference."})
    amount_counts = Counter(row["part3_vs_part1_amount_screen"] for row in rows)
    for status, count in sorted(amount_counts.items()):
        summary_rows.append({"metric": f"amount-screen:{status}", "value": str(count), "status": "screened", "boundary": "Same-identifier book-value comparison only; does not prove same lot, disposal settlement, borrower repayment, or owner cash."})
    with SUMMARY.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summary_rows[0]))
        writer.writeheader()
        writer.writerows(summary_rows)

    print(f"wrote {len(rows)} continuity rows to {OUT.relative_to(ROOT)}")
    print(f"total_consideration={total_consideration} total_book_value_on_disposal={total_book_on_disposal}")
    print("status_counts=" + "; ".join(f"{key}:{value}" for key, value in sorted(status_counts.items())))
    print(f"wrote {len(summary_rows)} summary rows to {SUMMARY.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
