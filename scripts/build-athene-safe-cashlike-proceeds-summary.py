#!/usr/bin/env python3
"""Summarize Athene Schedule D disposal proceeds by cash-likeness and CUSIP."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
DISPOSALS = DATA / "capital-flow-apollo-athene-statutory-schedule-d-disposal-proceeds-parser-pass-1.csv"
MATCH = DATA / "capital-flow-apollo-athene-statutory-cusip-cashback-match-pass-1.csv"
OUT = DATA / "capital-flow-apollo-athene-statutory-safe-cashlike-proceeds-summary-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-apollo-athene-statutory-safe-cashlike-proceeds-summary-diagnostic-pass-1.csv"

OUT_FIELDS = [
    "summary_row_id",
    "row_type",
    "rank",
    "cash_likeness",
    "economic_disposition_class",
    "cusip",
    "identifier_quality",
    "match_status",
    "issuer_or_description_sample",
    "rows",
    "consideration_usd",
    "share_of_total_consideration",
    "safe_realized_gain_loss_usd",
    "interest_or_dividends_received_usd",
    "first_disposal_date",
    "last_disposal_date",
    "top_purchaser_or_disposition_type",
    "proof_use",
    "boundary",
    "next_action",
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


def pct(numerator: Decimal, denominator: Decimal) -> str:
    if not denominator:
        return "0.000000"
    return f"{(numerator / denominator):.6f}"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def first_last(dates: list[str]) -> tuple[str, str]:
    valid = sorted(date for date in dates if date)
    if not valid:
        return "", ""
    return valid[0], valid[-1]


def top_label(values: list[str]) -> str:
    counts = Counter(value for value in values if value)
    return counts.most_common(1)[0][0] if counts else ""


def identifier_quality(cusip: str) -> str:
    if cusip in {"000000-00-0", "000000000"}:
        return "placeholder-identifier-hold"
    if any(marker in cusip for marker in ("@", "#", "*")):
        return "statutory-private-or-marker-cusip"
    return "standard-cusip-like"


def match_lookup() -> dict[str, str]:
    rows = read_rows(MATCH)
    return {row["cusip"]: row["match_status"] for row in rows}


def add_summary_row(
    rows_out: list[dict[str, str]],
    seq: int,
    row_type: str,
    rank: int,
    rows: list[dict[str, str]],
    total_consideration: Decimal,
    cash_likeness: str = "",
    economic_class: str = "",
    cusip: str = "",
    match_status: str = "",
) -> None:
    consideration = sum(money(row["consideration"]) for row in rows)
    safe_gain_loss = sum(money(row["safe_realized_gain_loss"]) for row in rows)
    interest = sum(money(row["interest_or_dividends_received"]) for row in rows)
    first_date, last_date = first_last([row["disposal_date"] for row in rows])
    issuer_sample = rows[0]["issuer_or_description"][:220] if rows and row_type == "top-cashlike-cusip" else ""
    class_label = economic_class or top_label([row["economic_disposition_class"] for row in rows])
    cash_label = cash_likeness or top_label([row["row_cash_likeness"] for row in rows])

    if row_type == "cash-likeness-total":
        proof_use = "all-row split between cash-like disposal candidates and noncash or transfer holds"
        boundary = "cash-likeness is parser classification; it does not prove borrower receipt, liability spread, or final asset return"
        next_action = "use the cash-like candidate subset for named CUSIP proceeds ranking and row-level proof packets"
    elif row_type == "economic-class-total":
        proof_use = "economic disposition class total for deciding which proceeds can be pursued as cash-like evidence"
        boundary = "class labels are disposition evidence, not proof of lot-level continuity, gain/loss, borrower receipt, or return"
        next_action = "inspect high-dollar rows in this class and reconcile consideration, book value, income, and disposition language"
    else:
        proof_use = "named high-dollar cash-like proceeds candidate for row-level proof"
        boundary = "CUSIP-level consideration is visible, but lot continuity, borrower receipt, liability cost, and return model are not proven"
        next_action = "inspect source PDF row, reconcile lot economics, then connect to issuer/borrower and liability-cost evidence"

    rows_out.append(
        {
            "summary_row_id": f"CFAASCPS-{seq:04d}",
            "row_type": row_type,
            "rank": str(rank),
            "cash_likeness": cash_label,
            "economic_disposition_class": class_label,
            "cusip": cusip,
            "identifier_quality": identifier_quality(cusip) if cusip else "",
            "match_status": match_status,
            "issuer_or_description_sample": issuer_sample,
            "rows": str(len(rows)),
            "consideration_usd": fmt(consideration),
            "share_of_total_consideration": pct(consideration, total_consideration),
            "safe_realized_gain_loss_usd": fmt(safe_gain_loss),
            "interest_or_dividends_received_usd": fmt(interest),
            "first_disposal_date": first_date,
            "last_disposal_date": last_date,
            "top_purchaser_or_disposition_type": top_label([row["purchaser_or_disposition_type"] for row in rows]),
            "proof_use": proof_use,
            "boundary": boundary,
            "next_action": next_action,
        }
    )


def diagnostic_row(seq: int, metric: str, value: Decimal, units: str) -> dict[str, str]:
    return {
        "diagnostic_id": f"CFAASCPD-{seq:03d}",
        "metric": metric,
        "value": fmt(value),
        "units": units,
        "proof_use": "controls the full-universe safe cash-like proceeds summary",
        "boundary": "diagnostic total is parser-derived and remains below final accounting, borrower-cash, liability-spread, or return proof",
        "next_action": "use diagnostics to select the next row-level proof packet and reconciliation target",
    }


def main() -> None:
    disposals = read_rows(DISPOSALS)
    matches = match_lookup()
    total_consideration = sum(money(row["consideration"]) for row in disposals)
    rows_out: list[dict[str, str]] = []
    seq = 1

    by_cash: dict[str, list[dict[str, str]]] = defaultdict(list)
    by_class: dict[str, list[dict[str, str]]] = defaultdict(list)
    by_cusip: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in disposals:
        by_cash[row["row_cash_likeness"]].append(row)
        by_class[row["economic_disposition_class"]].append(row)
        by_cusip[row["cusip"]].append(row)

    for rank, (cash_label, rows) in enumerate(
        sorted(by_cash.items(), key=lambda item: sum(money(row["consideration"]) for row in item[1]), reverse=True),
        start=1,
    ):
        add_summary_row(rows_out, seq, "cash-likeness-total", rank, rows, total_consideration, cash_likeness=cash_label)
        seq += 1

    for rank, (class_label, rows) in enumerate(
        sorted(by_class.items(), key=lambda item: sum(money(row["consideration"]) for row in item[1]), reverse=True),
        start=1,
    ):
        add_summary_row(
            rows_out,
            seq,
            "economic-class-total",
            rank,
            rows,
            total_consideration,
            economic_class=class_label,
        )
        seq += 1

    cash_like_rows = [row for row in disposals if row["row_cash_likeness"] == "cash-like-candidate"]
    cash_like_by_cusip: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in cash_like_rows:
        if identifier_quality(row["cusip"]) == "placeholder-identifier-hold":
            continue
        cash_like_by_cusip[row["cusip"]].append(row)

    top_cusips = sorted(
        cash_like_by_cusip.items(),
        key=lambda item: sum(money(row["consideration"]) for row in item[1]),
        reverse=True,
    )[:50]
    top_cusip_consideration = sum(sum(money(row["consideration"]) for row in rows) for _, rows in top_cusips)
    for rank, (cusip, rows) in enumerate(top_cusips, start=1):
        add_summary_row(
            rows_out,
            seq,
            "top-cashlike-cusip",
            rank,
            rows,
            total_consideration,
            cusip=cusip,
            match_status=matches.get(cusip, ""),
        )
        seq += 1

    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=OUT_FIELDS)
        writer.writeheader()
        writer.writerows(rows_out)

    cash_like_consideration = sum(money(row["consideration"]) for row in cash_like_rows)
    noncash_rows = [row for row in disposals if row["row_cash_likeness"] != "cash-like-candidate"]
    noncash_consideration = sum(money(row["consideration"]) for row in noncash_rows)
    same_cusip_cashlike_consideration = sum(
        sum(money(row["consideration"]) for row in rows)
        for cusip, rows in cash_like_by_cusip.items()
        if matches.get(cusip) == "holding-and-disposal-same-cusip-visible"
    )

    diagnostics: list[dict[str, str]] = []
    metrics = [
        ("disposal_rows", Decimal(len(disposals)), "count"),
        ("summary_rows", Decimal(len(rows_out)), "count"),
        ("total_consideration", total_consideration, "USD"),
        ("cash_like_candidate_rows", Decimal(len(cash_like_rows)), "count"),
        ("cash_like_candidate_consideration", cash_like_consideration, "USD"),
        ("cash_like_candidate_consideration_share", Decimal(pct(cash_like_consideration, total_consideration)), "ratio"),
        ("noncash_or_transfer_hold_rows", Decimal(len(noncash_rows)), "count"),
        ("noncash_or_transfer_hold_consideration", noncash_consideration, "USD"),
        ("noncash_or_transfer_hold_consideration_share", Decimal(pct(noncash_consideration, total_consideration)), "ratio"),
        ("top_cashlike_cusip_rows", Decimal(len(top_cusips)), "count"),
        ("top_cashlike_cusip_consideration", top_cusip_consideration, "USD"),
        ("top_cashlike_cusip_consideration_share", Decimal(pct(top_cusip_consideration, total_consideration)), "ratio"),
        ("same_cusip_cashlike_consideration_ex_placeholder", same_cusip_cashlike_consideration, "USD"),
        ("safe_realized_gain_loss_sum", sum(money(row["safe_realized_gain_loss"]) for row in disposals), "USD"),
    ]
    for seq, (metric, value, units) in enumerate(metrics, start=1):
        diagnostics.append(diagnostic_row(seq, metric, value, units))

    with DIAGNOSTIC_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DIAGNOSTIC_FIELDS)
        writer.writeheader()
        writer.writerows(diagnostics)

    print(f"wrote {len(rows_out)} rows to {OUT.relative_to(ROOT)}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
