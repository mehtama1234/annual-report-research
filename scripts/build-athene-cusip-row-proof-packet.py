#!/usr/bin/env python3
"""Build row-level proof packets for top Athene CUSIP cash-back candidates."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
INSPECTION = DATA / "capital-flow-apollo-athene-statutory-cusip-cashback-high-dollar-inspection-pass-1.csv"
HOLDINGS = DATA / "capital-flow-apollo-athene-statutory-schedule-d-full-range-parser-pass-1.csv"
DISPOSALS = DATA / "capital-flow-apollo-athene-statutory-schedule-d-disposal-proceeds-parser-pass-1.csv"
SUMMARY_OUT = DATA / "capital-flow-apollo-athene-statutory-cusip-row-proof-packet-pass-1.csv"
DETAIL_OUT = DATA / "capital-flow-apollo-athene-statutory-cusip-row-proof-packet-detail-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-apollo-athene-statutory-cusip-row-proof-packet-diagnostic-pass-1.csv"

TOP_N = 5

SUMMARY_FIELDS = [
    "proof_packet_id",
    "rank_source",
    "cusip",
    "issuer_or_description_sample",
    "economic_disposition_class",
    "top_purchaser_or_disposition_type",
    "year_end_holding_rows",
    "disposal_rows",
    "year_end_book_value_usd",
    "year_end_fair_value_usd",
    "year_end_interest_income_usd",
    "year_end_interest_received_usd",
    "disposal_consideration_usd",
    "cash_like_disposal_consideration_usd",
    "noncash_or_transfer_hold_consideration_usd",
    "disposal_book_value_at_disposal_usd",
    "disposal_realized_gain_loss_usd",
    "disposal_interest_or_dividends_received_usd",
    "consideration_to_year_end_book_ratio",
    "realized_gain_loss_to_consideration_ratio",
    "cashback_candidate_verdict",
    "row_level_evidence",
    "proof_boundary",
    "next_action",
]

DETAIL_FIELDS = [
    "detail_row_id",
    "proof_packet_id",
    "cusip",
    "source_row_type",
    "source_row_id",
    "source_schedule",
    "source_page",
    "issuer_or_description",
    "date_1",
    "date_2",
    "counterparty_or_disposition",
    "row_economic_disposition_class",
    "row_cash_likeness",
    "book_value_or_disposal_book_usd",
    "fair_value_or_consideration_usd",
    "actual_cost_usd",
    "par_or_shares",
    "interest_income_or_realized_gain_loss_usd",
    "interest_received_or_dividends_usd",
    "naic_designation",
    "asset_type_guess",
    "raw_numeric_values",
    "boundary",
]

DIAGNOSTIC_FIELDS = [
    "diagnostic_id",
    "metric",
    "value",
    "units",
    "proof_use",
    "boundary",
    "next_action",
]


def money(value: str) -> Decimal:
    value = (value or "").strip()
    if not value:
        return Decimal(0)
    negative = value.startswith("(") and value.endswith(")")
    cleaned = value.strip("()").replace(",", "")
    try:
        parsed = Decimal(cleaned)
    except Exception:
        return Decimal(0)
    return -parsed if negative else parsed


def safe_disposal_gain_loss(row: dict[str, str]) -> Decimal:
    if "safe_realized_gain_loss" in row:
        return money(row["safe_realized_gain_loss"])
    return money(row["realized_gain_loss"])


def fmt(value: Decimal) -> str:
    return f"{value:.6f}"


def ratio(numerator: Decimal, denominator: Decimal) -> str:
    return f"{(numerator / denominator):.6f}" if denominator else ""


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def disposition_class(label: str) -> str:
    lowered = (label or "").lower()
    if "tax free exchange" in lowered:
        return "tax-free-exchange-hold"
    if "security withdraw" in lowered or "withdraw" in lowered:
        return "security-withdrawal-hold"
    if "paydown" in lowered:
        return "principal-paydown-cash-candidate"
    if "maturity" in lowered:
        return "maturity-proceeds-cash-candidate"
    if "redemption" in lowered or "call" in lowered:
        return "redemption-or-call-cash-candidate"
    if "direct" in lowered or "private" in lowered:
        return "direct-or-private-transfer-hold"
    if not lowered:
        return "unclassified-hold"
    return "market-sale-or-counterparty-cash-candidate"


def is_cash_like(cls: str) -> bool:
    return cls in {
        "principal-paydown-cash-candidate",
        "maturity-proceeds-cash-candidate",
        "redemption-or-call-cash-candidate",
        "market-sale-or-counterparty-cash-candidate",
    }


def select_candidates() -> list[dict[str, str]]:
    rows = [
        row
        for row in read_rows(INSPECTION)
        if row["candidate_tier"] == "tier-1-same-cusip-cash-candidate"
    ]
    return rows[:TOP_N]


def verdict(disposition_class: str, gain_ratio: str) -> str:
    if disposition_class == "principal-paydown-cash-candidate":
        return "row-level-paydown-cash-candidate-reconciliation-hold"
    if disposition_class == "market-sale-or-counterparty-cash-candidate":
        return "row-level-market-sale-cash-candidate-reconciliation-hold"
    if disposition_class == "maturity-proceeds-cash-candidate":
        return "row-level-maturity-cash-candidate-reconciliation-hold"
    if disposition_class == "redemption-or-call-cash-candidate":
        return "row-level-redemption-cash-candidate-reconciliation-hold"
    return "row-level-cashback-classification-hold"


def summary_row(
    seq: int,
    candidate: dict[str, str],
    holdings: list[dict[str, str]],
    disposals: list[dict[str, str]],
) -> dict[str, str]:
    book = sum(money(row["book_adjusted_carrying_value"]) for row in holdings)
    fair = sum(money(row["fair_value"]) for row in holdings)
    income = sum(money(row["interest_income"]) for row in holdings)
    received = sum(money(row["interest_received_during_year"]) for row in holdings)
    consideration = sum(money(row["consideration"]) for row in disposals)
    cash_like = sum(
        money(row["consideration"])
        for row in disposals
        if is_cash_like(disposition_class(row["purchaser_or_disposition_type"]))
    )
    noncash_or_transfer = consideration - cash_like
    disposal_book = sum(money(row["book_adjusted_carrying_value_at_disposal"]) for row in disposals)
    gain_loss = sum(safe_disposal_gain_loss(row) for row in disposals)
    disposal_interest = sum(money(row["interest_or_dividends_received"]) for row in disposals)
    gl_ratio = ratio(gain_loss, consideration)
    return {
        "proof_packet_id": f"CFAASCBCRP-{seq:03d}",
        "rank_source": candidate["rank"],
        "cusip": candidate["cusip"],
        "issuer_or_description_sample": candidate["issuer_or_description_sample"],
        "economic_disposition_class": candidate["economic_disposition_class"],
        "top_purchaser_or_disposition_type": candidate["top_purchaser_or_disposition_type"],
        "year_end_holding_rows": str(len(holdings)),
        "disposal_rows": str(len(disposals)),
        "year_end_book_value_usd": fmt(book),
        "year_end_fair_value_usd": fmt(fair),
        "year_end_interest_income_usd": fmt(income),
        "year_end_interest_received_usd": fmt(received),
        "disposal_consideration_usd": fmt(consideration),
        "cash_like_disposal_consideration_usd": fmt(cash_like),
        "noncash_or_transfer_hold_consideration_usd": fmt(noncash_or_transfer),
        "disposal_book_value_at_disposal_usd": fmt(disposal_book),
        "disposal_realized_gain_loss_usd": fmt(gain_loss),
        "disposal_interest_or_dividends_received_usd": fmt(disposal_interest),
        "consideration_to_year_end_book_ratio": ratio(consideration, book),
        "realized_gain_loss_to_consideration_ratio": gl_ratio,
        "cashback_candidate_verdict": verdict(candidate["economic_disposition_class"], gl_ratio),
        "row_level_evidence": "same CUSIP has underlying year-end holding row(s) and disposal/proceeds row(s) in Athene Schedule D parser outputs",
        "proof_boundary": "row-level packet supports candidate inspection only; it does not prove lot-level continuity, borrower receipt, liability-cost spread, or final asset return",
        "next_action": "inspect statutory PDF row image/text for selected holding and disposal pages, then reconcile consideration, book value, gain/loss, interest, and disposition economics",
    }


def holding_detail(seq: int, packet_id: str, row: dict[str, str]) -> dict[str, str]:
    return {
        "detail_row_id": f"CFAASCBCRPD-{seq:04d}",
        "proof_packet_id": packet_id,
        "cusip": row["cusip"],
        "source_row_type": "year_end_holding",
        "source_row_id": row["normalized_row_id"],
        "source_schedule": row["schedule"],
        "source_page": row["page"],
        "issuer_or_description": row["issuer_or_description"],
        "date_1": row["acquired_date"],
        "date_2": row["maturity_date"],
        "counterparty_or_disposition": "",
        "row_economic_disposition_class": "",
        "row_cash_likeness": "",
        "book_value_or_disposal_book_usd": fmt(money(row["book_adjusted_carrying_value"])),
        "fair_value_or_consideration_usd": fmt(money(row["fair_value"])),
        "actual_cost_usd": fmt(money(row["actual_cost"])),
        "par_or_shares": row["par_value"],
        "interest_income_or_realized_gain_loss_usd": fmt(money(row["interest_income"])),
        "interest_received_or_dividends_usd": fmt(money(row["interest_received_during_year"])),
        "naic_designation": row["naic_designation"],
        "asset_type_guess": row["asset_type_guess"],
        "raw_numeric_values": "",
        "boundary": row["boundary"],
    }


def disposal_detail(seq: int, packet_id: str, row: dict[str, str]) -> dict[str, str]:
    cls = disposition_class(row["purchaser_or_disposition_type"])
    return {
        "detail_row_id": f"CFAASCBCRPD-{seq:04d}",
        "proof_packet_id": packet_id,
        "cusip": row["cusip"],
        "source_row_type": "disposal_or_proceeds",
        "source_row_id": row["disposal_row_id"],
        "source_schedule": row["schedule_part"],
        "source_page": row["page"],
        "issuer_or_description": row["issuer_or_description"],
        "date_1": row["disposal_date"],
        "date_2": "",
        "counterparty_or_disposition": row["purchaser_or_disposition_type"],
        "row_economic_disposition_class": cls,
        "row_cash_likeness": "cash-like-candidate" if is_cash_like(cls) else "noncash-or-transfer-hold",
        "book_value_or_disposal_book_usd": fmt(money(row["book_adjusted_carrying_value_at_disposal"])),
        "fair_value_or_consideration_usd": fmt(money(row["consideration"])),
        "actual_cost_usd": fmt(money(row["actual_cost"])),
        "par_or_shares": row["par_or_shares"],
        "interest_income_or_realized_gain_loss_usd": fmt(safe_disposal_gain_loss(row)),
        "interest_received_or_dividends_usd": fmt(money(row["interest_or_dividends_received"])),
        "naic_designation": "",
        "asset_type_guess": "",
        "raw_numeric_values": row["numeric_values"],
        "boundary": row["boundary"],
    }


def main() -> None:
    candidates = select_candidates()
    selected = {row["cusip"] for row in candidates}
    holdings_by_cusip: dict[str, list[dict[str, str]]] = defaultdict(list)
    disposals_by_cusip: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in read_rows(HOLDINGS):
        if row["cusip"] in selected:
            holdings_by_cusip[row["cusip"]].append(row)
    for row in read_rows(DISPOSALS):
        if row["cusip"] in selected:
            disposals_by_cusip[row["cusip"]].append(row)

    summary: list[dict[str, str]] = []
    details: list[dict[str, str]] = []
    detail_seq = 1
    for seq, candidate in enumerate(candidates, start=1):
        cusip = candidate["cusip"]
        hrows = holdings_by_cusip[cusip]
        drows = disposals_by_cusip[cusip]
        srow = summary_row(seq, candidate, hrows, drows)
        summary.append(srow)
        for row in hrows:
            details.append(holding_detail(detail_seq, srow["proof_packet_id"], row))
            detail_seq += 1
        for row in drows:
            details.append(disposal_detail(detail_seq, srow["proof_packet_id"], row))
            detail_seq += 1

    with SUMMARY_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=SUMMARY_FIELDS)
        writer.writeheader()
        writer.writerows(summary)

    with DETAIL_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DETAIL_FIELDS)
        writer.writeheader()
        writer.writerows(details)

    total_consideration = sum(money(row["disposal_consideration_usd"]) for row in summary)
    total_cash_like = sum(money(row["cash_like_disposal_consideration_usd"]) for row in summary)
    total_book = sum(money(row["year_end_book_value_usd"]) for row in summary)
    total_gain_loss = sum(money(row["disposal_realized_gain_loss_usd"]) for row in summary)
    class_counts = Counter(row["economic_disposition_class"] for row in summary)
    diagnostics: list[tuple[str, Decimal | str, str]] = [
        ("proof_packet_summary_rows", Decimal(len(summary)), "count"),
        ("proof_packet_detail_rows", Decimal(len(details)), "count"),
        ("selected_holding_rows", Decimal(sum(int(row["year_end_holding_rows"]) for row in summary)), "count"),
        ("selected_disposal_rows", Decimal(sum(int(row["disposal_rows"]) for row in summary)), "count"),
        ("selected_disposal_consideration", total_consideration, "USD"),
        ("selected_cash_like_disposal_consideration", total_cash_like, "USD"),
        ("selected_cash_like_share_of_disposal_consideration", total_cash_like / total_consideration if total_consideration else Decimal(0), "ratio"),
        ("selected_year_end_book_value", total_book, "USD"),
        ("selected_realized_gain_loss", total_gain_loss, "USD"),
        ("selected_consideration_to_year_end_book_ratio", total_consideration / total_book if total_book else Decimal(0), "ratio"),
    ]
    for cls, count in class_counts.most_common():
        diagnostics.append((f"economic_class_count__{cls}", Decimal(count), "count"))

    with DIAGNOSTIC_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DIAGNOSTIC_FIELDS)
        writer.writeheader()
        for idx, (metric, value, units) in enumerate(diagnostics, start=1):
            writer.writerow(
                {
                    "diagnostic_id": f"CFAASCBCRPDG-{idx:03d}",
                    "metric": metric,
                    "value": fmt(value) if isinstance(value, Decimal) and units in {"USD", "ratio"} else str(int(value)),
                    "units": units,
                    "proof_use": "row-level proof packet diagnostics for top tier-1 same-CUSIP cash-back candidates",
                    "boundary": "diagnostic supports targeted row inspection, not final statutory accounting or asset-return proof",
                    "next_action": "inspect PDF rows for the five selected CUSIPs and reconcile lot-level fields before claim promotion",
                }
            )

    print(f"wrote {len(summary)} rows to {SUMMARY_OUT}")
    print(f"wrote {len(details)} rows to {DETAIL_OUT}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT}")
    print({row['cusip']: (row['year_end_holding_rows'], row['disposal_rows']) for row in summary})


if __name__ == "__main__":
    main()
