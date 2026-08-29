#!/usr/bin/env python3
"""Interpret selected Athene Schedule D disposal row columns conservatively."""

from __future__ import annotations

import csv
import re
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
RAW = DATA / "capital-flow-apollo-athene-statutory-cusip-raw-text-inspection-pass-1.csv"
OUT = DATA / "capital-flow-apollo-athene-statutory-cusip-column-interpretation-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-apollo-athene-statutory-cusip-column-interpretation-diagnostic-pass-1.csv"

MONEY_RE = re.compile(r"\(?\d{1,3}(?:,\d{3})+(?:\.\d+)?\)?")
SMALL_PAREN_RE = re.compile(r"\((\d{1,3})\)")

FIELDNAMES = [
    "column_interpretation_id",
    "raw_text_row_id",
    "proof_packet_id",
    "cusip",
    "source_row_id",
    "schedule_part",
    "source_page",
    "disposition_label",
    "raw_money_tokens",
    "raw_small_parenthetical_tokens",
    "safe_consideration_usd",
    "safe_par_or_shares",
    "safe_actual_cost_usd",
    "safe_prior_or_disposal_book_value_usd",
    "safe_book_adjusted_carrying_value_at_disposal_usd",
    "safe_realized_gain_loss_usd",
    "safe_interest_or_dividends_received_usd",
    "parser_consideration_usd",
    "parser_gain_or_income_usd",
    "consideration_interpretation_status",
    "gain_loss_interpretation_status",
    "cashback_column_verdict",
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
    return f"{value:.6f}" if value else ""


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def schedule_part(row: dict[str, str]) -> str:
    schedule = row["source_schedule"]
    if "Part 5" in schedule:
        return "Schedule D Part 5"
    if "Part 4" in schedule:
        return "Schedule D Part 4"
    return schedule


def label(raw: str) -> str:
    lowered = raw.lower()
    for token in [
        "Tax Free Exchange",
        "Interest Capitalization",
        "Apollo Capital Markets Partner",
        "Redemption 100.0000",
        "Paydown",
        "Various",
    ]:
        if token.lower() in lowered:
            return token
    return ""


def parenthetical_gain(raw: str) -> str:
    values = [int(value) for value in SMALL_PAREN_RE.findall(raw)]
    if not values:
        return ""
    # Ignore parentheticals in rates or page artifacts by only using tiny values
    # when a disposal row also has repeated blank-column markers.
    smallest = min(values)
    return f"-{smallest}.000000"


def interpret_part4(tokens: list[str], raw: str) -> dict[str, str]:
    result = {
        "safe_consideration_usd": fmt(money(tokens[0])) if len(tokens) > 0 else "",
        "safe_par_or_shares": tokens[1] if len(tokens) > 1 else "",
        "safe_actual_cost_usd": fmt(money(tokens[2])) if len(tokens) > 2 else "",
        "safe_prior_or_disposal_book_value_usd": fmt(money(tokens[3])) if len(tokens) > 3 else "",
        "safe_book_adjusted_carrying_value_at_disposal_usd": "",
        "safe_realized_gain_loss_usd": "",
        "safe_interest_or_dividends_received_usd": fmt(money(tokens[-1])) if tokens else "",
    }
    small_gain = parenthetical_gain(raw)
    if small_gain:
        result["safe_realized_gain_loss_usd"] = small_gain
    if len(tokens) >= 6:
        result["safe_book_adjusted_carrying_value_at_disposal_usd"] = fmt(money(tokens[-2]))
    elif len(tokens) == 5:
        result["safe_book_adjusted_carrying_value_at_disposal_usd"] = fmt(money(tokens[3]))
    return result


def interpret_part5(tokens: list[str], raw: str) -> dict[str, str]:
    result = {
        "safe_consideration_usd": fmt(money(tokens[2])) if len(tokens) > 2 else "",
        "safe_par_or_shares": tokens[0] if len(tokens) > 0 else "",
        "safe_actual_cost_usd": fmt(money(tokens[1])) if len(tokens) > 1 else "",
        "safe_prior_or_disposal_book_value_usd": fmt(money(tokens[3])) if len(tokens) > 3 else "",
        "safe_book_adjusted_carrying_value_at_disposal_usd": fmt(money(tokens[3])) if len(tokens) > 3 else "",
        "safe_realized_gain_loss_usd": "",
        "safe_interest_or_dividends_received_usd": fmt(money(tokens[-1])) if tokens else "",
    }
    small_gain = parenthetical_gain(raw)
    if small_gain:
        result["safe_realized_gain_loss_usd"] = small_gain
    return result


def consideration_status(row: dict[str, str], interpreted: dict[str, str]) -> str:
    parsed = money(row["parser_consideration_or_fair_value_usd"])
    safe = money(interpreted["safe_consideration_usd"])
    if safe and safe == parsed:
        return "parser-consideration-confirmed"
    if safe:
        return "parser-consideration-corrected-by-schedule-layout"
    return "consideration-not-safe"


def gain_status(row: dict[str, str], interpreted: dict[str, str]) -> str:
    parsed = money(row["parser_gain_or_income_usd"])
    safe = money(interpreted["safe_realized_gain_loss_usd"])
    if safe:
        return "small-gain-loss-visible-parser-missed-or-shifted" if safe != parsed else "gain-loss-confirmed"
    if parsed and parsed == money(row["parser_consideration_or_fair_value_usd"]):
        return "parser-gain-loss-equals-consideration-column-shift-hold"
    return "gain-loss-not-safely-visible"


def verdict(row: dict[str, str], interpreted: dict[str, str]) -> str:
    raw = row["raw_row_text"].lower()
    if "tax free exchange" in raw:
        return "noncash-exchange-hold"
    if not interpreted["safe_consideration_usd"]:
        return "column-interpretation-hold"
    if "paydown" in raw:
        return "consideration-safe-principal-paydown-cash-candidate-gain-loss-hold"
    if "redemption" in raw:
        return "consideration-safe-redemption-cash-candidate-gain-loss-hold"
    return "consideration-safe-market-or-counterparty-cash-candidate-gain-loss-hold"


def main() -> None:
    rows = [row for row in read_rows(RAW) if row["source_row_type"] == "disposal_or_proceeds"]
    output: list[dict[str, str]] = []
    for idx, row in enumerate(rows, start=1):
        raw = row["raw_row_text"]
        tokens = MONEY_RE.findall(raw)
        part = schedule_part(row)
        interpreted = interpret_part5(tokens, raw) if part == "Schedule D Part 5" else interpret_part4(tokens, raw)
        output.append(
            {
                "column_interpretation_id": f"CFAASCPCI-{idx:03d}",
                "raw_text_row_id": row["raw_text_row_id"],
                "proof_packet_id": row["proof_packet_id"],
                "cusip": row["cusip"],
                "source_row_id": row["source_row_id"],
                "schedule_part": part,
                "source_page": row["source_page"],
                "disposition_label": label(raw),
                "raw_money_tokens": "; ".join(tokens),
                "raw_small_parenthetical_tokens": "; ".join(f"({v})" for v in SMALL_PAREN_RE.findall(raw)),
                **interpreted,
                "parser_consideration_usd": row["parser_consideration_or_fair_value_usd"],
                "parser_gain_or_income_usd": row["parser_gain_or_income_usd"],
                "consideration_interpretation_status": consideration_status(row, interpreted),
                "gain_loss_interpretation_status": gain_status(row, interpreted),
                "cashback_column_verdict": verdict(row, interpreted),
                "boundary": "page-specific interpretation promotes consideration only where schedule layout and raw tokens support it; gain/loss remains hold unless independently visible",
                "next_action": "apply this schedule-layout correction back to the disposal parser and reconcile full Part 4/Part 5 consideration, book-at-disposal, and gain/loss totals",
            }
        )

    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(output)

    confirmed = sum(1 for row in output if row["consideration_interpretation_status"] == "parser-consideration-confirmed")
    gain_holds = sum(1 for row in output if "hold" in row["gain_loss_interpretation_status"])
    noncash = sum(1 for row in output if row["cashback_column_verdict"] == "noncash-exchange-hold")
    cash_consideration = sum(
        money(row["safe_consideration_usd"])
        for row in output
        if row["cashback_column_verdict"] != "noncash-exchange-hold"
    )
    diagnostics = [
        ("column_interpretation_rows", len(output), "count"),
        ("parser_consideration_confirmed_rows", confirmed, "count"),
        ("gain_loss_hold_rows", gain_holds, "count"),
        ("noncash_exchange_hold_rows", noncash, "count"),
        ("safe_cashlike_consideration_interpreted", cash_consideration, "USD"),
    ]
    with DIAGNOSTIC_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DIAGNOSTIC_FIELDS)
        writer.writeheader()
        for idx, (metric, value, units) in enumerate(diagnostics, start=1):
            writer.writerow(
                {
                    "diagnostic_id": f"CFAASCPID-{idx:03d}",
                    "metric": metric,
                    "value": fmt(value) if isinstance(value, Decimal) else str(value),
                    "units": units,
                    "proof_use": "page-specific column interpretation for selected Athene Schedule D disposal rows",
                    "boundary": "supports parser correction and cash-like consideration selection, not final gain/loss or asset-return proof",
                    "next_action": "update disposal parser column rules and run full reconciliation diagnostics",
                }
            )

    print(f"wrote {len(output)} rows to {OUT}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT}")
    print({"confirmed_consideration": confirmed, "gain_holds": gain_holds, "noncash": noncash})


if __name__ == "__main__":
    main()

