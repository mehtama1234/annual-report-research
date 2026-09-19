#!/usr/bin/env python3
"""Build a review queue for the strongest same-identifier BA lot screens."""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTINUITY = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-event-continuity-ledger-pass-1.csv"
RAW = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-full-range-parser-pass-1.csv"
OUT_CSV = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-lot-review-queue-pass-1.csv"
OUT_MD = ROOT / "analysis/company-first-principles/capital-flow-apollo-athene-statutory-schedule-ba-lot-review-queue-pass-1.md"


def integer(value: str) -> int:
    return int((value or "0").replace(",", "").replace("(", "-").replace(")", ""))


def money(value: str) -> str:
    return f"${integer(value):,}"


def source_signal(terms: str) -> tuple[str, str, str]:
    nature = "blank-or-not-visible-in-compact-row"
    for candidate in ("Partial Sale", "Final Distribution", "Tax Free Exchange", "Redemption", "Distribution", "Sale", "Transfer"):
        if candidate in terms:
            nature = candidate
            break
    dates = re.findall(r"\d{2}/\d{2}/\d{4}", terms)
    acquired = dates[0] if len(dates) >= 1 else ""
    disposed = dates[1] if len(dates) >= 2 else ""
    return nature, acquired, disposed


def main() -> None:
    with CONTINUITY.open() as handle:
        source_rows = list(csv.DictReader(handle))
    selected = [
        row for row in source_rows
        if row["part3_vs_part1_amount_screen"] in {
            "part3-book-vs-part1-book-exact-within-1",
            "part3-book-vs-part1-book-near-within-1m",
        }
    ]
    selected.sort(key=lambda row: (0 if row["part3_vs_part1_amount_screen"].endswith("within-1") else 1, abs(integer(row["part3_book_minus_part1_book"]))))

    raw_by_key = {}
    with RAW.open() as handle:
        for row in csv.DictReader(handle):
            raw_by_key[(row["schedule"], row["page"], row["cusip_or_identifier"])] = row["name_and_raw_terms"]

    fields = [
        "review_id", "screen_tier", "cusip_or_identifier", "part3_page", "part1_pages", "part2_pages",
        "part3_name", "part1_book_value_sum", "part3_book_value", "part3_book_minus_part1_book",
        "disposal_consideration", "total_gain_loss_on_disposal", "part2_acquisition_cost_sum",
        "part2_additional_investment_sum", "part1_source_terms", "part2_source_terms", "part3_source_terms",
        "part3_nature_signal", "part3_acquired_date_signal", "part3_disposal_date_signal",
        "part2_cost_to_part3_book_ratio", "part2_population_screen",
        "continuity_status", "review_boundary",
    ]
    rows = []
    for index, source in enumerate(selected, start=1):
        exact = source["part3_vs_part1_amount_screen"].endswith("within-1")
        part2_cost = integer(source["part2_acquisition_cost_sum"])
        part3_book = integer(source["book_value_on_disposal"])
        ratio = part2_cost / part3_book if part3_book else 0
        if not part2_cost:
            population_screen = "no-Part2-cost"
        elif ratio >= 1.75:
            population_screen = "Part2-cost-materially-exceeds-Part3-book-review-multi-row-or-multi-lot"
        elif ratio >= 1.25:
            population_screen = "Part2-cost-exceeds-Part3-book-review"
        else:
            population_screen = "Part2-cost-not-materially-above-Part3-book"
        rows.append({
            "review_id": f"CFAASBALRQ-{index:03d}",
            "screen_tier": "exact-within-$1" if exact else "near-within-$1M",
            "cusip_or_identifier": source["cusip_or_identifier"],
            "part3_page": source["part3_page"],
            "part1_pages": source["part1_pages"],
            "part2_pages": source["part2_pages"],
            "part3_name": source["part3_name"],
            "part1_book_value_sum": money(source["part1_book_value_sum"]),
            "part3_book_value": money(source["book_value_on_disposal"]),
            "part3_book_minus_part1_book": money(source["part3_book_minus_part1_book"]),
            "disposal_consideration": money(source["disposal_consideration"]),
            "total_gain_loss_on_disposal": money(source["total_gain_loss_on_disposal"]),
            "part2_acquisition_cost_sum": money(source["part2_acquisition_cost_sum"]),
            "part2_additional_investment_sum": money(source["part2_additional_investment_sum"]),
            "part1_source_terms": raw_by_key.get(("Schedule BA Part 1", source["part1_pages"].split(";")[0] if source["part1_pages"] else "", source["cusip_or_identifier"]), ""),
            "part2_source_terms": raw_by_key.get(("Schedule BA Part 2", source["part2_pages"].split(";")[0] if source["part2_pages"] else "", source["cusip_or_identifier"]), ""),
            "part3_source_terms": raw_by_key.get(("Schedule BA Part 3", source["part3_page"], source["cusip_or_identifier"]), ""),
            "part3_nature_signal": source_signal(raw_by_key.get(("Schedule BA Part 3", source["part3_page"], source["cusip_or_identifier"]), ""))[0],
            "part3_acquired_date_signal": source_signal(raw_by_key.get(("Schedule BA Part 3", source["part3_page"], source["cusip_or_identifier"]), ""))[1],
            "part3_disposal_date_signal": source_signal(raw_by_key.get(("Schedule BA Part 3", source["part3_page"], source["cusip_or_identifier"]), ""))[2],
            "part2_cost_to_part3_book_ratio": f"{ratio:.3f}" if ratio else "",
            "part2_population_screen": population_screen,
            "continuity_status": source["continuity_status"],
            "review_boundary": "Prioritized same-identifier book-value screen only; verify page row, dates, disposal nature, lot terms, and settlement before treating as an economic-lot or cash-flow bridge.",
        })

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Apollo/Athene Schedule BA same-identifier lot review queue pass 1",
        "",
        "This queue prioritizes only the strongest quantitative continuity screens from the corrected Schedule BA Part 3 ledger. It is a review queue, not a promoted asset-lot or cash-flow conclusion.",
        "",
        f"The queue contains `{sum(row['screen_tier'] == 'exact-within-$1' for row in rows)}` exact-within-$1 screens and `{sum(row['screen_tier'] == 'near-within-$1M' for row in rows)}` near-within-$1M screens.",
        "Six queue rows have Part 2 acquisition cost approximately twice the Part 3 disposal book value. That pattern is a multi-row or multi-lot warning, not evidence that one identifier maps to one economic lot.",
        "",
        "| tier | identifier | pages P1/P2/P3 | Part 1 book | Part 3 book | delta | consideration | gain/loss | Part 3 source-row signal |",
        "|---|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        pages = f"{row['part1_pages'] or '—'}/{row['part2_pages'] or '—'}/{row['part3_page']}"
        signal = f"{row['part3_nature_signal']}; {row['part3_acquired_date_signal']} -> {row['part3_disposal_date_signal']}"
        lines.append(f"| {row['screen_tier']} | `{row['cusip_or_identifier']}` | {pages} | {row['part1_book_value_sum']} | {row['part3_book_value']} | {row['part3_book_minus_part1_book']} | {row['disposal_consideration']} | {row['total_gain_loss_on_disposal']} | {signal} |")
    lines.extend([
        "",
        "## Required review before promotion",
        "",
        "1. Read the exact source row on the Part 1, Part 2, and Part 3 pages and confirm identifier, issuer/description, acquisition/disposal dates, and disposal nature.",
        "2. Determine whether the Part 3 row is a full disposal, partial sale, redemption, transfer, distribution, or tax-free exchange; a same-CUSIP book tie does not resolve that distinction.",
        "3. Locate settlement-account, counterparty, borrower, liability-release, tax/fee, and legal-entity cash evidence. Schedule BA consideration alone does not prove any of those joins.",
        "4. Keep any Apollo distribution or common-owner cash claim separate until the Athene legal-entity-to-parent receipt is independently evidenced.",
        "",
        "The underlying ledger is [capital-flow-apollo-athene-statutory-schedule-ba-event-continuity-ledger-pass-1.csv](data/capital-flow-apollo-athene-statutory-schedule-ba-event-continuity-ledger-pass-1.csv).",
    ])
    OUT_MD.write_text("\n".join(lines) + "\n")
    print(f"wrote {len(rows)} lot-review rows to {OUT_CSV.relative_to(ROOT)}")
    print(f"wrote review note to {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
