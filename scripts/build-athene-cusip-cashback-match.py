#!/usr/bin/env python3
"""Build CUSIP-level Athene Schedule D holdings-to-proceeds match table."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
HOLDINGS = DATA / "capital-flow-apollo-athene-statutory-schedule-d-full-range-parser-pass-1.csv"
DISPOSALS = DATA / "capital-flow-apollo-athene-statutory-schedule-d-disposal-proceeds-parser-pass-1.csv"
COMPACT = DATA / "capital-flow-apollo-athene-statutory-compact-extraction-pass-1.csv"
OUT = DATA / "capital-flow-apollo-athene-statutory-cusip-cashback-match-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-apollo-athene-statutory-cusip-cashback-match-diagnostic-pass-1.csv"

OUT_FIELDS = [
    "match_row_id",
    "cusip",
    "identifier_quality",
    "match_status",
    "year_end_holding_rows",
    "disposal_rows",
    "holding_schedule_sections",
    "disposal_schedule_parts",
    "issuer_or_description_sample",
    "year_end_book_value_usd",
    "year_end_fair_value_usd",
    "year_end_interest_income_usd",
    "year_end_interest_received_usd",
    "disposal_consideration_usd",
    "disposal_book_value_at_disposal_usd",
    "disposal_realized_gain_loss_usd",
    "disposal_interest_or_dividends_received_usd",
    "first_disposal_date",
    "last_disposal_date",
    "top_purchaser_or_disposition_type",
    "cash_back_signal",
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


def safe_disposal_gain_loss(row: dict[str, str]) -> Decimal:
    if "safe_realized_gain_loss" in row:
        return money(row["safe_realized_gain_loss"])
    return money(row["realized_gain_loss"])


def fmt(value: Decimal) -> str:
    return f"{value:.6f}"


def compact_ref(metric_name: str) -> Decimal:
    with COMPACT.open(newline="") as f:
        for row in csv.DictReader(f):
            if row["metric_name"] == metric_name:
                multiplier = Decimal("1000000000") if row["units"] == "B USD" else Decimal("1000000")
                return Decimal(row["metric_value"]) * multiplier
    raise KeyError(metric_name)


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def uniq(values: list[str]) -> str:
    seen: list[str] = []
    for value in values:
        if value and value not in seen:
            seen.append(value)
    return "; ".join(seen[:8])


def first_last(dates: list[str]) -> tuple[str, str]:
    valid = sorted(date for date in dates if date)
    if not valid:
        return "", ""
    return valid[0], valid[-1]


def match_status(holding_count: int, disposal_count: int) -> str:
    if holding_count and disposal_count:
        return "holding-and-disposal-same-cusip-visible"
    if disposal_count:
        return "disposal-only-cusip-visible"
    return "year-end-holding-only-cusip-visible"


def identifier_quality(cusip: str) -> str:
    if cusip in {"000000-00-0", "000000000"}:
        return "placeholder-identifier-hold"
    if any(marker in cusip for marker in ("@", "#", "*")):
        return "statutory-private-or-marker-cusip"
    return "standard-cusip-like"


def cash_signal(holding_count: int, disposal_count: int, consideration: Decimal, interest: Decimal) -> str:
    signals: list[str] = []
    if consideration:
        signals.append("disposal-consideration")
    if interest:
        signals.append("interest-or-dividend-cash")
    if holding_count and disposal_count:
        signals.append("same-cusip-year-end-and-disposal-bridge")
    return "; ".join(signals) if signals else "holding-without-current-proceeds-signal"


def proof_use(status: str) -> str:
    if status == "holding-and-disposal-same-cusip-visible":
        return "same-CUSIP cash-back candidate for row-level reconciliation and return testing"
    if status == "disposal-only-cusip-visible":
        return "named disposal/proceeds candidate; no year-end holding row expected or found in current parser"
    return "year-end holding candidate for future income, maturity, or later-period proceeds matching"


def boundary(status: str) -> str:
    if status == "holding-and-disposal-same-cusip-visible":
        return "same CUSIP appears in both year-end holdings and disposal/proceeds output, but lot-level continuity, subtotal treatment, income allocation, liability cost, borrower receipt, and return are not proven"
    if status == "disposal-only-cusip-visible":
        return "disposed asset may not remain in year-end Schedule D holdings; absence from year-end holdings is not a parser failure by itself"
    return "year-end holding row has no current disposal/proceeds match; it may still have income, maturity, credit-quality, or later-period cash evidence"


def next_action(status: str) -> str:
    if status == "holding-and-disposal-same-cusip-visible":
        return "inspect lot-level dates and numeric columns, then reconcile consideration, book value, gain/loss, and interest fields"
    if status == "disposal-only-cusip-visible":
        return "classify disposition type and test whether the CUSIP was fully sold, matured, paid down, or appears under a corrected identifier"
    return "join to page 18 income categories, later disposal rows, credit-quality migration, and liability-cost spread support"


def main() -> None:
    holdings = read_rows(HOLDINGS)
    disposals = read_rows(DISPOSALS)

    holdings_by_cusip: dict[str, list[dict[str, str]]] = defaultdict(list)
    disposals_by_cusip: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in holdings:
        holdings_by_cusip[row["cusip"]].append(row)
    for row in disposals:
        disposals_by_cusip[row["cusip"]].append(row)

    output: list[dict[str, str]] = []
    for seq, cusip in enumerate(sorted(set(holdings_by_cusip) | set(disposals_by_cusip)), start=1):
        hrows = holdings_by_cusip.get(cusip, [])
        drows = disposals_by_cusip.get(cusip, [])
        status = match_status(len(hrows), len(drows))
        consideration = sum(money(row["consideration"]) for row in drows)
        disposal_book = sum(money(row["book_adjusted_carrying_value_at_disposal"]) for row in drows)
        gain_loss = sum(safe_disposal_gain_loss(row) for row in drows)
        disposal_interest = sum(money(row["interest_or_dividends_received"]) for row in drows)
        holding_interest = sum(money(row["interest_income"]) for row in hrows)
        holding_received = sum(money(row["interest_received_during_year"]) for row in hrows)
        first_date, last_date = first_last([row["disposal_date"] for row in drows])
        purchaser_counts = Counter(row["purchaser_or_disposition_type"] for row in drows if row["purchaser_or_disposition_type"])
        top_purchaser = purchaser_counts.most_common(1)[0][0] if purchaser_counts else ""
        descriptions = [row["issuer_or_description"] for row in hrows] + [row["issuer_or_description"] for row in drows]
        output.append(
            {
                "match_row_id": f"CFAASCBCM-{seq:05d}",
                "cusip": cusip,
                "identifier_quality": identifier_quality(cusip),
                "match_status": status,
                "year_end_holding_rows": str(len(hrows)),
                "disposal_rows": str(len(drows)),
                "holding_schedule_sections": uniq([row["schedule"] for row in hrows]),
                "disposal_schedule_parts": uniq([row["schedule_part"] for row in drows]),
                "issuer_or_description_sample": descriptions[0][:220] if descriptions else "",
                "year_end_book_value_usd": fmt(sum(money(row["book_adjusted_carrying_value"]) for row in hrows)),
                "year_end_fair_value_usd": fmt(sum(money(row["fair_value"]) for row in hrows)),
                "year_end_interest_income_usd": fmt(holding_interest),
                "year_end_interest_received_usd": fmt(holding_received),
                "disposal_consideration_usd": fmt(consideration),
                "disposal_book_value_at_disposal_usd": fmt(disposal_book),
                "disposal_realized_gain_loss_usd": fmt(gain_loss),
                "disposal_interest_or_dividends_received_usd": fmt(disposal_interest),
                "first_disposal_date": first_date,
                "last_disposal_date": last_date,
                "top_purchaser_or_disposition_type": top_purchaser,
                "cash_back_signal": cash_signal(len(hrows), len(drows), consideration, disposal_interest + holding_received),
                "proof_use": proof_use(status),
                "boundary": boundary(status),
                "next_action": next_action(status),
            }
        )

    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=OUT_FIELDS)
        writer.writeheader()
        writer.writerows(output)

    status_counts = Counter(row["match_status"] for row in output)
    matched = [row for row in output if row["match_status"] == "holding-and-disposal-same-cusip-visible"]
    disposal_only = [row for row in output if row["match_status"] == "disposal-only-cusip-visible"]
    holding_only = [row for row in output if row["match_status"] == "year-end-holding-only-cusip-visible"]
    headline_rows = [row for row in output if row["identifier_quality"] != "placeholder-identifier-hold"]
    headline_matched = [row for row in headline_rows if row["match_status"] == "holding-and-disposal-same-cusip-visible"]
    ref = compact_ref("consideration_for_bonds_and_stocks_disposed")
    total_consideration = sum(money(row["disposal_consideration_usd"]) for row in output)
    matched_consideration = sum(money(row["disposal_consideration_usd"]) for row in matched)
    headline_consideration = sum(money(row["disposal_consideration_usd"]) for row in headline_rows)
    headline_matched_consideration = sum(money(row["disposal_consideration_usd"]) for row in headline_matched)

    diagnostics = [
        ("unique_cusips_total", Decimal(len(output)), "count"),
        ("headline_unique_cusips_ex_placeholder", Decimal(len(headline_rows)), "count"),
        ("same_cusip_holding_and_disposal_count", Decimal(len(matched)), "count"),
        ("headline_same_cusip_holding_and_disposal_count", Decimal(len(headline_matched)), "count"),
        ("disposal_only_cusip_count", Decimal(len(disposal_only)), "count"),
        ("year_end_holding_only_cusip_count", Decimal(len(holding_only)), "count"),
        ("total_disposal_consideration", total_consideration, "USD"),
        ("headline_disposal_consideration_ex_placeholder", headline_consideration, "USD"),
        ("statutory_disposal_consideration_reference", ref, "USD"),
        ("total_disposal_consideration_coverage", total_consideration / ref if ref else Decimal(0), "ratio"),
        ("headline_disposal_consideration_coverage_ex_placeholder", headline_consideration / ref if ref else Decimal(0), "ratio"),
        ("same_cusip_matched_consideration", matched_consideration, "USD"),
        ("same_cusip_matched_consideration_share", matched_consideration / total_consideration if total_consideration else Decimal(0), "ratio"),
        ("headline_same_cusip_matched_consideration_ex_placeholder", headline_matched_consideration, "USD"),
        ("headline_same_cusip_matched_consideration_share_ex_placeholder", headline_matched_consideration / headline_consideration if headline_consideration else Decimal(0), "ratio"),
        ("holding_rows_input", Decimal(len(holdings)), "count"),
        ("disposal_rows_input", Decimal(len(disposals)), "count"),
    ]

    with DIAGNOSTIC_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DIAGNOSTIC_FIELDS)
        writer.writeheader()
        for idx, (metric, value, units) in enumerate(diagnostics, start=1):
            writer.writerow(
                {
                    "diagnostic_id": f"CFAASCBCMD-{idx:03d}",
                    "metric": metric,
                    "value": fmt(value) if units in {"USD", "ratio"} else str(int(value)),
                    "units": units,
                    "proof_use": "CUSIP-level holdings-to-proceeds matching diagnostics",
                    "boundary": "diagnostic supports workbench quality control, not final lot-level cash return or liability spread proof",
                    "next_action": "inspect same-CUSIP matched rows, disposal-only rows, and highest-dollar consideration rows before claim promotion",
                }
            )

    print(f"wrote {len(output)} rows to {OUT}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT}")
    print(dict(status_counts))


if __name__ == "__main__":
    main()
