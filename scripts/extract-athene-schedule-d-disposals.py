#!/usr/bin/env python3
"""Extract Athene Schedule D disposal/proceeds rows from Part 4 and Part 5."""

from __future__ import annotations

import csv
import importlib.util
import re
from collections import Counter
from decimal import Decimal
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
PARSER_SCRIPT = ROOT / "scripts/extract-athene-statutory-detail-samples.py"
COMPACT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-compact-extraction-pass-1.csv"
DETAIL_OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-disposal-proceeds-parser-pass-1.csv"
DIAGNOSTIC_OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-disposal-proceeds-diagnostic-pass-1.csv"

PARTS = [
    ("Schedule D Part 4", 6074, 6283),
    ("Schedule D Part 5", 6284, 6336),
]

DISPOSAL_DATE_RE = re.compile(r"\.{2,}\s*(?P<date>\d{2}/\d{2}/\d{4})\s*\.")
SMALL_PAREN_RE = re.compile(r"\((\d{1,3})\)")

DETAIL_FIELDNAMES = [
    "disposal_row_id",
    "schedule_part",
    "page",
    "cusip",
    "issuer_or_description",
    "disposal_date",
    "purchaser_or_disposition_type",
    "consideration",
    "par_or_shares",
    "actual_cost",
    "prior_or_disposal_book_value",
    "book_adjusted_carrying_value_at_disposal",
    "realized_gain_loss",
    "total_gain_loss",
    "interest_or_dividends_received",
    "numeric_values",
    "economic_disposition_class",
    "row_cash_likeness",
    "safe_realized_gain_loss",
    "gain_loss_interpretation_status",
    "current_status",
    "boundary",
]

DIAGNOSTIC_FIELDNAMES = [
    "diagnostic_id",
    "scope",
    "parser_rows",
    "parser_consideration_sum_usd",
    "statutory_reference_metric",
    "statutory_reference_value_usd",
    "difference_value_usd",
    "coverage_ratio",
    "top_page_by_consideration",
    "top_page_consideration_usd",
    "current_status",
    "proof_use",
    "boundary",
    "next_action",
]


def load_parser_module():
    spec = importlib.util.spec_from_file_location("athene_schedule_d_parser", PARSER_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load parser script: {PARSER_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def money(value: str) -> Decimal:
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


def compact_ref(metric_name: str) -> Decimal:
    with COMPACT.open(newline="") as f:
        for row in csv.DictReader(f):
            if row["metric_name"] == metric_name:
                multiplier = Decimal("1000000000") if row["units"] == "B USD" else Decimal("1000000")
                return Decimal(row["metric_value"]) * multiplier
    raise KeyError(metric_name)


def disposal_date(raw: str, parser_module) -> str:
    match = DISPOSAL_DATE_RE.search(raw)
    if match:
        return match.group("date")
    dates = parser_module.date_tokens(raw)
    return dates[-1] if dates else ""


def purchaser(raw: str, parser_module) -> str:
    disposed = disposal_date(raw, parser_module)
    if not disposed:
        return ""
    after_date = raw.split(disposed, 1)[-1]
    before_numbers = parser_module.MONEY_RE.split(after_date, maxsplit=1)[0]
    cleaned = parser_module.clean(before_numbers.replace(".", " "))
    cleaned = re.sub(r"\s+\(?\d[\d,()]*$", "", cleaned)
    return cleaned[:120]


def economic_disposition_class(label: str) -> str:
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


def small_parenthetical_gain_loss(raw: str) -> str:
    values = [int(value) for value in SMALL_PAREN_RE.findall(raw)]
    if not values:
        return ""
    return f"({min(values)})"


def safe_gain_loss(raw: str, consideration: str, realized_gain_loss: str) -> tuple[str, str]:
    small = small_parenthetical_gain_loss(raw)
    if small:
        return small, "small-parenthetical-gain-loss-visible"
    if realized_gain_loss and money(realized_gain_loss) == money(consideration):
        return "", "parser-gain-loss-equals-consideration-column-shift-hold"
    if realized_gain_loss:
        return "", "legacy-positional-gain-loss-not-promoted"
    return "", "gain-loss-not-visible"


def detail_row(parser_module, seq: int, schedule_part: str, page: int, cusip: str, raw: str) -> dict[str, str]:
    values = parser_module.money_tokens(raw)
    dates = parser_module.date_tokens(raw)
    if schedule_part == "Schedule D Part 4":
        consideration = values[0] if len(values) > 0 else ""
        par_or_shares = values[1] if len(values) > 1 else ""
        actual_cost = values[2] if len(values) > 2 else ""
        prior_book = values[3] if len(values) > 3 else ""
        book_at_disposal = values[-4] if len(values) >= 7 else ""
    else:
        par_or_shares = values[0] if len(values) > 0 else ""
        actual_cost = values[1] if len(values) > 1 else ""
        consideration = values[2] if len(values) > 2 else ""
        prior_book = values[3] if len(values) > 3 else ""
        book_at_disposal = values[3] if len(values) > 3 else ""

    realized_gain_loss = values[-3] if len(values) >= 4 else ""
    total_gain_loss = values[-2] if len(values) >= 3 else ""
    interest = values[-1] if values else ""
    purchaser_or_type = purchaser(raw, parser_module)
    disposition_class = economic_disposition_class(purchaser_or_type)
    safe_gain, gain_status = safe_gain_loss(raw, consideration, realized_gain_loss)

    return {
        "disposal_row_id": f"CFAASDDP-{seq:05d}",
        "schedule_part": schedule_part,
        "page": str(page),
        "cusip": cusip,
        "issuer_or_description": parser_module.issuer_description(raw),
        "disposal_date": disposal_date(raw, parser_module),
        "purchaser_or_disposition_type": purchaser_or_type,
        "consideration": consideration,
        "par_or_shares": par_or_shares,
        "actual_cost": actual_cost,
        "prior_or_disposal_book_value": prior_book,
        "book_adjusted_carrying_value_at_disposal": book_at_disposal,
        "realized_gain_loss": realized_gain_loss,
        "total_gain_loss": total_gain_loss,
        "interest_or_dividends_received": interest,
        "numeric_values": "; ".join(values[:16]),
        "economic_disposition_class": disposition_class,
        "row_cash_likeness": "cash-like-candidate" if is_cash_like(disposition_class) else "noncash-or-transfer-hold",
        "safe_realized_gain_loss": safe_gain,
        "gain_loss_interpretation_status": gain_status,
        "current_status": "disposal-proceeds-parser-row-visible",
        "boundary": "Schedule D disposal parser with safer disposition classification; consideration is schedule-positioned, while gain/loss is promoted only when independently visible and otherwise remains a hold",
    }


def add_diagnostic(
    output: list[dict[str, str]],
    scope: str,
    rows: list[dict[str, str]],
    reference: Decimal,
    ref_metric: str,
) -> None:
    consideration_sum = sum(money(row["consideration"]) for row in rows)
    by_page: Counter[str] = Counter()
    for row in rows:
        by_page[row["page"]] += money(row["consideration"])
    top_page, top_value = by_page.most_common(1)[0] if by_page else ("", Decimal(0))
    ratio = consideration_sum / reference if reference else Decimal(0)
    status = "near-reconciled-hold" if Decimal("0.98") <= ratio <= Decimal("1.02") else "not-reconciled"
    output.append(
        {
            "diagnostic_id": f"CFAASDDPD-{len(output) + 1:03d}",
            "scope": scope,
            "parser_rows": str(len(rows)),
            "parser_consideration_sum_usd": fmt(consideration_sum),
            "statutory_reference_metric": ref_metric,
            "statutory_reference_value_usd": fmt(reference),
            "difference_value_usd": fmt(consideration_sum - reference),
            "coverage_ratio": f"{ratio:.6f}",
            "top_page_by_consideration": str(top_page),
            "top_page_consideration_usd": fmt(top_value),
            "current_status": status,
            "proof_use": "named disposal/proceeds worklist and reconciliation targeting",
            "boundary": "parser consideration totals are not final realized-return proof until subtotal, Part 4/Part 5, and gain/loss fields reconcile",
            "next_action": "inspect subtotal treatment, Part 5 column shifts, and largest consideration pages before matching proceeds to holdings",
        }
    )


def main() -> None:
    parser_module = load_parser_module()
    reader = PdfReader(str(parser_module.PDF))
    rows: list[dict[str, str]] = []
    seq = 1
    for schedule_part, start_page, end_page in PARTS:
        for page in range(start_page, end_page + 1):
            for cusip, raw in parser_module.extract_rows(parser_module.page_lines(reader, page)):
                rows.append(detail_row(parser_module, seq, schedule_part, page, cusip, raw))
                seq += 1

    with DETAIL_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DETAIL_FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    ref = compact_ref("consideration_for_bonds_and_stocks_disposed")
    part4 = [row for row in rows if row["schedule_part"] == "Schedule D Part 4"]
    part5 = [row for row in rows if row["schedule_part"] == "Schedule D Part 5"]
    diagnostics: list[dict[str, str]] = []
    add_diagnostic(diagnostics, "Schedule D Part 4", part4, ref, "consideration_for_bonds_and_stocks_disposed")
    add_diagnostic(diagnostics, "Schedule D Part 5", part5, ref, "consideration_for_bonds_and_stocks_disposed")
    add_diagnostic(diagnostics, "Schedule D Part 4 plus Part 5", rows, ref, "consideration_for_bonds_and_stocks_disposed")
    with DIAGNOSTIC_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DIAGNOSTIC_FIELDNAMES)
        writer.writeheader()
        writer.writerows(diagnostics)

    print(f"wrote {len(rows)} rows to {DETAIL_OUT.relative_to(ROOT)}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
