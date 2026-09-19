#!/usr/bin/env python3
"""Crosswalk controlled BA Sale rows to same-CUSIP Schedule D disposal rows."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BA_SALES = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-sale-review-queue-pass-1.csv"
SCHEDULE_D = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-disposal-proceeds-parser-pass-1.csv"
OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-sale-schedule-d-crosswalk-pass-1.csv"
NOTE = ROOT / "analysis/company-first-principles/capital-flow-apollo-athene-statutory-schedule-ba-sale-schedule-d-crosswalk-pass-1.md"


def integer(value: str) -> int:
    return int((value or "0").replace(",", "").replace("(", "-").replace(")", ""))


def money(value: int) -> str:
    return f"$({abs(value):,})" if value < 0 else f"${value:,}"


def main() -> None:
    d_by_cusip: defaultdict[str, list[dict[str, str]]] = defaultdict(list)
    with SCHEDULE_D.open() as handle:
        for row in csv.DictReader(handle):
            if row["cusip"]:
                d_by_cusip[row["cusip"]].append(row)
    output = []
    with BA_SALES.open() as handle:
        for index, ba in enumerate(csv.DictReader(handle), start=1):
            matches = d_by_cusip.get(ba["cusip_or_identifier"], [])
            for match_index, d in enumerate(matches, start=1):
                output.append({
                    "crosswalk_id": f"CFAASBASD-XW-{index:03d}-{match_index:02d}",
                    "ba_sale_page": ba["page"],
                    "ba_cusip": ba["cusip_or_identifier"],
                    "ba_name": ba["name"],
                    "ba_book_value": ba["book_value"],
                    "ba_consideration": ba["consideration"],
                    "ba_gain_loss": ba["gain_loss"],
                    "ba_acquisition_date": ba.get("acquisition_date", ""),
                    "ba_disposal_date": ba.get("disposal_date", ""),
                    "schedule_d_part": d["schedule_part"],
                    "schedule_d_page": d["page"],
                    "schedule_d_disposal_date": d["disposal_date"],
                    "schedule_d_disposition_type": d["purchaser_or_disposition_type"],
                    "schedule_d_consideration": d["consideration"],
                    "schedule_d_book_value": d["book_adjusted_carrying_value_at_disposal"],
                    "schedule_d_total_gain_loss": d["total_gain_loss"],
                    "schedule_d_cash_likeness": d["row_cash_likeness"],
                    "schedule_d_current_status": d["current_status"],
                    "match_status": "same-cusip-schedule-d-disposal-row-visible",
                    "boundary": "Identifier crosswalk only; Schedule D parser values remain parser-derived and do not prove that the BA event and Schedule D event are the same lot, settlement, borrower repayment, or owner cash.",
                })
    fields = list(output[0]) if output else ["crosswalk_id"]
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output)
    matched_ba = len({row["ba_cusip"] for row in output})
    total_ba = sum(1 for _ in csv.DictReader(BA_SALES.open()))
    d_consideration = sum(integer(row["schedule_d_consideration"]) for row in output)
    lines = [
        "# Apollo/Athene BA Sale to Schedule D disposal crosswalk pass 1",
        "",
        f"The queue contains `{total_ba}` coordinate-controlled BA rows whose disposal-nature column is `Sale`. `{matched_ba}` distinct BA identifiers have one or more same-CUSIP Schedule D disposal-parser rows; the crosswalk contains `{len(output)}` identifier matches.",
        "",
        f"The matched Schedule D parser rows sum to `{money(d_consideration)}` of schedule-positioned consideration. This is not a consolidated cash total: duplicate identifiers, parser-derived columns, differing dates, transfers, and lot boundaries remain unresolved.",
        "",
        "| BA page | CUSIP | BA dates | BA consideration | Schedule D part/page | D date | D disposition | D consideration | D cash-likeness |",
        "|---:|---|---|---:|---|---|---|---:|---|",
    ]
    for row in output:
        lines.append(f"| {row['ba_sale_page']} | `{row['ba_cusip']}` | {row['ba_acquisition_date']} → {row['ba_disposal_date']} | {row['ba_consideration']} | {row['schedule_d_part']}/{row['schedule_d_page']} | {row['schedule_d_disposal_date']} | {row['schedule_d_disposition_type'][:70]} | {row['schedule_d_consideration']} | {row['schedule_d_cash_likeness']} |")
    lines.extend([
        "",
        "## Interpretation boundary",
        "",
        "A same-CUSIP match is a useful route-finding clue because the BA population includes debt-style assets transferred from Schedule D. It does not establish same-lot identity, chronological direction, cash settlement, borrower repayment, legal-entity cash receipt, liability release, tax/fee treatment, or Apollo distribution. The Schedule D disposal parser itself remains subject to its documented positional-column boundaries.",
        "",
        "The underlying queues are [BA Sale queue](capital-flow-apollo-athene-statutory-schedule-ba-sale-review-queue-pass-1.md) and the [Schedule D disposal parser data](data/capital-flow-apollo-athene-statutory-schedule-d-disposal-proceeds-parser-pass-1.csv).",
    ])
    NOTE.write_text("\n".join(lines) + "\n")
    print(f"wrote {len(output)} Schedule D crosswalk rows to {OUT.relative_to(ROOT)}")
    print(f"matched-ba-identifiers={matched_ba} total-ba-sale-rows={total_ba} schedule-d-consideration={d_consideration}")
    print(f"wrote note to {NOTE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
