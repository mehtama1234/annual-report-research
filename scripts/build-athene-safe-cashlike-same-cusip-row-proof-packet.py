#!/usr/bin/env python3
"""Build row-level packets for top safe cash-like same-CUSIP Athene proceeds."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
SAFE_SUMMARY = DATA / "capital-flow-apollo-athene-statutory-safe-cashlike-proceeds-summary-pass-1.csv"
HOLDINGS = DATA / "capital-flow-apollo-athene-statutory-schedule-d-full-range-parser-pass-1.csv"
DISPOSALS = DATA / "capital-flow-apollo-athene-statutory-schedule-d-disposal-proceeds-parser-pass-1.csv"
SUMMARY_OUT = DATA / "capital-flow-apollo-athene-statutory-safe-cashlike-same-cusip-row-proof-packet-pass-1.csv"
DETAIL_OUT = DATA / "capital-flow-apollo-athene-statutory-safe-cashlike-same-cusip-row-proof-packet-detail-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-apollo-athene-statutory-safe-cashlike-same-cusip-row-proof-packet-diagnostic-pass-1.csv"

TOP_N = 10

SUMMARY_FIELDS = [
    "proof_packet_id",
    "safe_summary_rank",
    "cusip",
    "issuer_or_description_sample",
    "dominant_economic_disposition_class",
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
    "safe_realized_gain_loss_usd",
    "disposal_interest_or_dividends_received_usd",
    "consideration_to_year_end_book_ratio",
    "cash_like_to_total_disposal_consideration_ratio",
    "candidate_verdict",
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
    "interest_income_or_safe_gain_loss_usd",
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


def fmt(value: Decimal) -> str:
    return f"{value:.6f}"


def ratio(numerator: Decimal, denominator: Decimal) -> str:
    return f"{(numerator / denominator):.6f}" if denominator else ""


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def top_label(values: list[str]) -> str:
    counts = Counter(value for value in values if value)
    return counts.most_common(1)[0][0] if counts else ""


def select_candidates() -> list[dict[str, str]]:
    candidates = [
        row
        for row in read_rows(SAFE_SUMMARY)
        if row["row_type"] == "top-cashlike-cusip"
        and row["match_status"] == "holding-and-disposal-same-cusip-visible"
        and row["cash_likeness"] == "cash-like-candidate"
    ]
    return candidates[:TOP_N]


def candidate_verdict(cash_like: Decimal, total: Decimal, noncash: Decimal) -> str:
    if cash_like and not noncash:
        return "same-cusip-cashlike-row-packet-clean-cashlike-candidate"
    if cash_like and total:
        return "same-cusip-mixed-cashlike-and-noncash-row-packet-hold"
    return "same-cusip-row-packet-no-cashlike-proceeds-hold"


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
    total_consideration = sum(money(row["consideration"]) for row in disposals)
    cash_like = sum(money(row["consideration"]) for row in disposals if row["row_cash_likeness"] == "cash-like-candidate")
    noncash = total_consideration - cash_like
    disposal_book = sum(money(row["book_adjusted_carrying_value_at_disposal"]) for row in disposals)
    gain_loss = sum(money(row["safe_realized_gain_loss"]) for row in disposals)
    disposal_interest = sum(money(row["interest_or_dividends_received"]) for row in disposals)
    return {
        "proof_packet_id": f"CFAASCSCRP-{seq:03d}",
        "safe_summary_rank": candidate["rank"],
        "cusip": candidate["cusip"],
        "issuer_or_description_sample": candidate["issuer_or_description_sample"],
        "dominant_economic_disposition_class": top_label([row["economic_disposition_class"] for row in disposals]),
        "top_purchaser_or_disposition_type": top_label([row["purchaser_or_disposition_type"] for row in disposals]),
        "year_end_holding_rows": str(len(holdings)),
        "disposal_rows": str(len(disposals)),
        "year_end_book_value_usd": fmt(book),
        "year_end_fair_value_usd": fmt(fair),
        "year_end_interest_income_usd": fmt(income),
        "year_end_interest_received_usd": fmt(received),
        "disposal_consideration_usd": fmt(total_consideration),
        "cash_like_disposal_consideration_usd": fmt(cash_like),
        "noncash_or_transfer_hold_consideration_usd": fmt(noncash),
        "disposal_book_value_at_disposal_usd": fmt(disposal_book),
        "safe_realized_gain_loss_usd": fmt(gain_loss),
        "disposal_interest_or_dividends_received_usd": fmt(disposal_interest),
        "consideration_to_year_end_book_ratio": ratio(total_consideration, book),
        "cash_like_to_total_disposal_consideration_ratio": ratio(cash_like, total_consideration),
        "candidate_verdict": candidate_verdict(cash_like, total_consideration, noncash),
        "row_level_evidence": "same CUSIP appears in Athene year-end Schedule D holdings and corrected disposal/proceeds rows selected from the safe cash-like summary",
        "proof_boundary": "same-CUSIP cash-like proceeds support row-level proof targeting; they do not prove lot continuity, borrower receipt, liability-cost spread, or final asset return",
        "next_action": "inspect selected PDF rows and match issuer/borrower context, liability-cost evidence, and return model support before any stronger claim",
    }


def holding_detail(seq: int, packet_id: str, row: dict[str, str]) -> dict[str, str]:
    return {
        "detail_row_id": f"CFAASCSCRPD-{seq:04d}",
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
        "interest_income_or_safe_gain_loss_usd": fmt(money(row["interest_income"])),
        "interest_received_or_dividends_usd": fmt(money(row["interest_received_during_year"])),
        "naic_designation": row["naic_designation"],
        "asset_type_guess": row["asset_type_guess"],
        "raw_numeric_values": "",
        "boundary": row["boundary"],
    }


def disposal_detail(seq: int, packet_id: str, row: dict[str, str]) -> dict[str, str]:
    return {
        "detail_row_id": f"CFAASCSCRPD-{seq:04d}",
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
        "row_economic_disposition_class": row["economic_disposition_class"],
        "row_cash_likeness": row["row_cash_likeness"],
        "book_value_or_disposal_book_usd": fmt(money(row["book_adjusted_carrying_value_at_disposal"])),
        "fair_value_or_consideration_usd": fmt(money(row["consideration"])),
        "actual_cost_usd": fmt(money(row["actual_cost"])),
        "par_or_shares": row["par_or_shares"],
        "interest_income_or_safe_gain_loss_usd": fmt(money(row["safe_realized_gain_loss"])),
        "interest_received_or_dividends_usd": fmt(money(row["interest_or_dividends_received"])),
        "naic_designation": "",
        "asset_type_guess": "",
        "raw_numeric_values": row["numeric_values"],
        "boundary": row["boundary"],
    }


def diagnostic_row(seq: int, metric: str, value: Decimal, units: str) -> dict[str, str]:
    return {
        "diagnostic_id": f"CFAASCSCRPDG-{seq:03d}",
        "metric": metric,
        "value": fmt(value) if units in {"USD", "ratio"} else str(int(value)),
        "units": units,
        "proof_use": "controls the safe cash-like same-CUSIP row proof packet",
        "boundary": "diagnostic supports targeted row inspection, not borrower receipt, liability spread, or final return proof",
        "next_action": "inspect PDF rows and resolve borrower/use/return support for the selected same-CUSIP candidates",
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
        row = summary_row(seq, candidate, holdings_by_cusip[cusip], disposals_by_cusip[cusip])
        summary.append(row)
        for holding in holdings_by_cusip[cusip]:
            details.append(holding_detail(detail_seq, row["proof_packet_id"], holding))
            detail_seq += 1
        for disposal in disposals_by_cusip[cusip]:
            details.append(disposal_detail(detail_seq, row["proof_packet_id"], disposal))
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
    total_noncash = sum(money(row["noncash_or_transfer_hold_consideration_usd"]) for row in summary)
    total_book = sum(money(row["year_end_book_value_usd"]) for row in summary)
    total_safe_gain_loss = sum(money(row["safe_realized_gain_loss_usd"]) for row in summary)
    total_interest = sum(money(row["disposal_interest_or_dividends_received_usd"]) for row in summary)
    diagnostics = [
        ("summary_rows", Decimal(len(summary)), "count"),
        ("detail_rows", Decimal(len(details)), "count"),
        ("selected_holding_rows", Decimal(sum(int(row["year_end_holding_rows"]) for row in summary)), "count"),
        ("selected_disposal_rows", Decimal(sum(int(row["disposal_rows"]) for row in summary)), "count"),
        ("selected_disposal_consideration", total_consideration, "USD"),
        ("selected_cash_like_disposal_consideration", total_cash_like, "USD"),
        ("selected_noncash_or_transfer_hold_consideration", total_noncash, "USD"),
        ("selected_cash_like_share", total_cash_like / total_consideration if total_consideration else Decimal(0), "ratio"),
        ("selected_year_end_book_value", total_book, "USD"),
        ("selected_consideration_to_year_end_book_ratio", total_consideration / total_book if total_book else Decimal(0), "ratio"),
        ("selected_safe_realized_gain_loss", total_safe_gain_loss, "USD"),
        ("selected_disposal_interest_or_dividends_received", total_interest, "USD"),
    ]
    class_counts = Counter(row["dominant_economic_disposition_class"] for row in summary)
    for cls, count in class_counts.most_common():
        diagnostics.append((f"dominant_economic_class_count__{cls}", Decimal(count), "count"))

    with DIAGNOSTIC_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DIAGNOSTIC_FIELDS)
        writer.writeheader()
        for seq, (metric, value, units) in enumerate(diagnostics, start=1):
            writer.writerow(diagnostic_row(seq, metric, value, units))

    print(f"wrote {len(summary)} rows to {SUMMARY_OUT.relative_to(ROOT)}")
    print(f"wrote {len(details)} rows to {DETAIL_OUT.relative_to(ROOT)}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT.relative_to(ROOT)}")
    print("; ".join(row["cusip"] for row in summary))


if __name__ == "__main__":
    main()
