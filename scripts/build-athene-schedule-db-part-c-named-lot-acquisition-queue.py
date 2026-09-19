#!/usr/bin/env python3
"""Prioritize the smallest decisive source request for named Part C lots."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
INPUT = DATA / "capital-flow-apollo-athene-statutory-schedule-db-part-c-named-lot-control-pass-1.csv"
OUTPUT = DATA / "capital-flow-apollo-athene-statutory-schedule-db-part-c-named-lot-acquisition-queue-pass-1.csv"
MEMO = ROOT / "analysis/company-first-principles/capital-flow-apollo-athene-statutory-schedule-db-part-c-named-lot-acquisition-queue-pass-1.md"

FIELDS = [
    "queue_id",
    "priority_tier",
    "priority_rank",
    "cash_instrument_cusip",
    "named_family",
    "cash_instrument_description",
    "part_c_ledger_ids",
    "part_c_pages",
    "schedule_d_row_ids",
    "schedule_d_pages",
    "schedule_d_book_value_sum",
    "schedule_d_fair_value_sum",
    "schedule_d_interest_received_sum",
    "part_c_book_candidate_sum_used",
    "part_c_fair_candidate_sum_used",
    "numeric_control_status",
    "priority_reason",
    "minimum_decisive_source_object",
    "why_that_object_matters",
    "current_boundary",
]


def money(value: str) -> int:
    return int((value or "0").replace(",", ""))


def main() -> None:
    with INPUT.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    def sort_key(row: dict[str, str]) -> tuple[int, int, int]:
        # High statutory book value comes first; received interest and source
        # ambiguity break ties and ensure ambiguous rows remain visible.
        return (
            money(row["schedule_d_book_value_sum"]),
            money(row["schedule_d_interest_received_sum"]),
            1 if "ambiguous" in row["numeric_control_status"] else 0,
        )

    rows.sort(key=sort_key, reverse=True)
    output: list[dict[str, str]] = []
    for index, row in enumerate(rows, start=1):
        book = money(row["schedule_d_book_value_sum"])
        received = money(row["schedule_d_interest_received_sum"])
        ambiguous = "ambiguous" in row["numeric_control_status"]
        if ambiguous or not row["schedule_d_row_ids"]:
            tier = "A"
            reason = "source-column ambiguity or missing row-level control must be resolved before numeric use"
            source = "page-level Athene statutory Schedule DB/Schedule D custody or accounting support showing the exact columns and lot"
            matters = "It determines whether the apparent named component is a reliable lot-level amount before requesting settlement or remittance evidence."
        elif book >= 100_000_000 or received >= 10_000_000:
            tier = "A"
            reason = "large statutory holding or received-interest control with a direct named Part C identity"
            source = "Athene custody statement, trustee/paying-agent remittance, or transaction settlement record for the exact CUSIP and period"
            matters = "It could connect the statutory holding and income fields to an actual legal-entity receipt, counterparty, or settlement event."
        elif book >= 25_000_000 or received >= 1_000_000:
            tier = "B"
            reason = "material named statutory holding or received-interest control"
            source = "lot-level custody, trustee, remittance, or settlement record for the exact CUSIP and period"
            matters = "It would test whether the named exposure has an observable cash or claim event without assuming one from Schedule D."
        else:
            tier = "C"
            reason = "lower-dollar named identity retained for completeness and later aggregation"
            source = "lot-level custody or income-allocation record if the route becomes material"
            matters = "It preserves a reproducible path for aggregation without allowing small rows to be promoted by inference."
        output.append(
            {
                "queue_id": f"CFAASDBNLQ-{index:04d}",
                "priority_tier": tier,
                "priority_rank": str(index),
                "cash_instrument_cusip": row["cash_instrument_cusip"],
                "named_family": row["named_family"],
                "cash_instrument_description": row["cash_instrument_description"],
                "part_c_ledger_ids": row["part_c_ledger_ids"],
                "part_c_pages": row["part_c_pages"],
                "schedule_d_row_ids": row["schedule_d_row_ids"],
                "schedule_d_pages": row["schedule_d_pages"],
                "schedule_d_book_value_sum": row["schedule_d_book_value_sum"],
                "schedule_d_fair_value_sum": row["schedule_d_fair_value_sum"],
                "schedule_d_interest_received_sum": row["schedule_d_interest_received_sum"],
                "part_c_book_candidate_sum_used": row["part_c_book_candidate_sum_used"],
                "part_c_fair_candidate_sum_used": row["part_c_fair_candidate_sum_used"],
                "numeric_control_status": row["numeric_control_status"],
                "priority_reason": reason,
                "minimum_decisive_source_object": source,
                "why_that_object_matters": matters,
                "current_boundary": "Schedule DB identity, Schedule D carrying value, fair value, and interest fields do not by themselves prove settlement, remittance, liability allocation, borrower repayment, or Apollo owner cash.",
            }
        )

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output)

    tier_counts = {tier: sum(row["priority_tier"] == tier for row in output) for tier in ("A", "B", "C")}
    lines = [
        "# Apollo/Athene named-lot acquisition queue — pass 1",
        "",
        "This queue converts the named Part C ↔ Schedule D control into a targeted evidence request order. It is a source-acquisition worklist, not evidence that the requested records exist or that cash was received.",
        "",
        f"- `{len(output)}` named CUSIP routes retained; tiers: A `{tier_counts['A']}`, B `{tier_counts['B']}`, C `{tier_counts['C']}`.",
        "- Ranking prioritizes Schedule D statutory book value, then received interest, while placing source-column ambiguity in Tier A for resolution.",
        "- The minimum decisive object is deliberately specific: page-level column support, custody, trustee/paying-agent remittance, transaction settlement, or lot-level income allocation.",
        "",
        "## Promotion rule",
        "",
        "Do not promote a queue row to Athene cash, liability-adjusted return, borrower repayment, or Apollo common-owner cash unless the requested object joins the exact legal entity, period, CUSIP/lot, counterparty or payer, amount, and cash/claim disposition.",
        "",
        "The machine-readable queue is [here](data/capital-flow-apollo-athene-statutory-schedule-db-part-c-named-lot-acquisition-queue-pass-1.csv).",
    ]
    MEMO.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {len(output)} acquisition-queue rows; tiers={tier_counts}")


if __name__ == "__main__":
    main()
