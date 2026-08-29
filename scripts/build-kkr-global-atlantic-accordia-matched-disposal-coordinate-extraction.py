#!/usr/bin/env python3
"""Coordinate-extract Accordia matched Schedule D Part 4 disposal rows."""

from __future__ import annotations

import csv
import re
from collections import Counter
from decimal import Decimal
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
ANALYSIS = ROOT / "analysis/company-first-principles"
PDF = ROOT / "raw/primary-sources/capital-flow/kkr/global-atlantic/statutory/2025/Accordia_4Q_2025_Quarterly_Statements.pdf"

EVENTS = DATA / "capital-flow-kkr-global-atlantic-accordia-owned-bond-income-proceeds-cusip-match-event-pass-1.csv"
MATCHES = DATA / "capital-flow-kkr-global-atlantic-accordia-owned-bond-income-proceeds-cusip-match-pass-1.csv"
PARSER = DATA / "capital-flow-kkr-global-atlantic-accordia-schedule-d-parser-pass-1.csv"

OUT = DATA / "capital-flow-kkr-global-atlantic-accordia-matched-disposal-coordinate-extraction-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-kkr-global-atlantic-accordia-matched-disposal-coordinate-extraction-diagnostic-pass-1.csv"
MEMO = ANALYSIS / "capital-flow-kkr-global-atlantic-accordia-matched-disposal-coordinate-extraction-pass-1.md"

FIELDNAMES = [
    "disposal_coordinate_row_id",
    "match_row_id",
    "event_row_id",
    "cusip",
    "issuer_or_description",
    "page",
    "row_y",
    "disposal_date",
    "purchaser_or_disposition_type",
    "consideration",
    "par_or_shares",
    "actual_cost",
    "prior_year_book_adjusted_carrying_value",
    "unrealized_valuation_change",
    "current_year_amortization_accretion",
    "current_year_otti",
    "foreign_exchange_change",
    "total_change_in_book_adjusted_carrying_value",
    "book_adjusted_carrying_value_at_disposal",
    "foreign_exchange_gain_loss_on_disposal",
    "realized_gain_loss_on_disposal",
    "total_gain_loss_on_disposal",
    "interest_or_dividends_received",
    "maturity_date",
    "source_token_count",
    "raw_parser_money_token_count",
    "parser_row_id",
    "coordinate_capture_status",
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

DATE_RE = re.compile(r"^\d{2}/\d{2}/\d{4}$")
MONEY_RE = re.compile(r"^\(?\d{1,3}(?:,\d{3})*(?:\.\d+)?\)?$")


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def money(value: str) -> Decimal:
    value = (value or "").strip()
    if not value:
        return Decimal(0)
    negative = value.startswith("(") and value.endswith(")")
    parsed = Decimal(value.strip("()").replace(",", ""))
    return -parsed if negative else parsed


def fmt(value: Decimal) -> str:
    return str(int(value)) if value == value.to_integral() else f"{value:.6f}"


def clean(value: str) -> str:
    return value.strip().replace(",", "")


def page_items(reader: PdfReader, page_no: int) -> list[tuple[float, float, str]]:
    items: list[tuple[float, float, str]] = []

    def visitor(text: str, cm: object, tm: object, font_dict: object, font_size: object) -> None:
        text = text.strip()
        if text:
            items.append((float(tm[4]), float(tm[5]), text))

    reader.pages[page_no - 1].extract_text(visitor_text=visitor)
    return items


def row_band(items: list[tuple[float, float, str]], y: float, tolerance: float = 0.7) -> list[tuple[float, str]]:
    return sorted((x, text.strip()) for x, yy, text in items if abs(yy - y) < tolerance and x > 0)


def first_money(row: list[tuple[float, str]], lo: float, hi: float) -> str:
    values = [clean(text) for x, text in row if lo <= x < hi and MONEY_RE.match(text)]
    return values[-1] if values else ""


def first_date(row: list[tuple[float, str]], lo: float, hi: float) -> str:
    values = [text for x, text in row if lo <= x < hi and DATE_RE.match(text)]
    return values[-1] if values else ""


def clean_counterparty(value: str) -> str:
    value = re.sub(r"^\W+", "", value or "").strip()
    value = re.sub(r"\s+\d[\d,()]*$", "", value).strip()
    return value


def purchaser(items: list[tuple[float, float, str]], y: float, fallback: str) -> str:
    values = [
        text.strip()
        for x, yy, text in sorted(items, key=lambda item: (-item[1], item[0]))
        if 254 <= x < 365 and y - 9 <= yy <= y + 1 and text.strip(". ")
    ]
    coordinate_value = " ".join(values).strip()
    if coordinate_value and any(char.isalpha() for char in coordinate_value) and not any(char.isdigit() for char in coordinate_value):
        return clean_counterparty(coordinate_value)
    return clean_counterparty(fallback)


def find_row_y(items: list[tuple[float, float, str]], cusip: str) -> float:
    ys = [y for x, y, text in items if 45 <= x < 70 and text == cusip]
    if not ys:
        raise ValueError(f"Could not find CUSIP {cusip}")
    return ys[0]


def column_values(row: list[tuple[float, str]]) -> dict[str, str]:
    return {
        "disposal_date": first_date(row, 220, 255),
        "consideration": first_money(row, 365, 407),
        "par_or_shares": first_money(row, 407, 454),
        "actual_cost": first_money(row, 454, 499),
        "prior_year_book_adjusted_carrying_value": first_money(row, 499, 544),
        "unrealized_valuation_change": first_money(row, 544, 584),
        "current_year_amortization_accretion": first_money(row, 584, 624),
        "current_year_otti": first_money(row, 624, 664),
        "foreign_exchange_change": first_money(row, 664, 707),
        "total_change_in_book_adjusted_carrying_value": first_money(row, 707, 744),
        "book_adjusted_carrying_value_at_disposal": first_money(row, 744, 787),
        "foreign_exchange_gain_loss_on_disposal": first_money(row, 787, 824),
        "realized_gain_loss_on_disposal": first_money(row, 824, 866),
        "total_gain_loss_on_disposal": first_money(row, 866, 904),
        "interest_or_dividends_received": first_money(row, 904, 948),
        "maturity_date": first_date(row, 948, 990),
    }


def build_rows() -> list[dict[str, str]]:
    events = [row for row in read_rows(EVENTS) if "sold-redeemed-disposed" in row["event_type"]]
    matches_by_id = {row["match_row_id"]: row for row in read_rows(MATCHES)}
    parser_by_id = {row["parser_row_id"]: row for row in read_rows(PARSER)}
    reader = PdfReader(str(PDF))
    items_by_page: dict[int, list[tuple[float, float, str]]] = {}
    out: list[dict[str, str]] = []

    for event in events:
        page_no = int(event["page"])
        items = items_by_page.setdefault(page_no, page_items(reader, page_no))
        y = find_row_y(items, event["cusip"])
        band = row_band(items, y)
        values = column_values(band)
        match = matches_by_id[event["match_row_id"]]
        parser_row = parser_by_id.get(event["parser_row_id"], {})
        captured = sum(1 for key, value in values.items() if value and key != "disposal_date" and key != "maturity_date")
        status = "coordinate-disposal-columns-visible" if captured >= 7 else "coordinate-disposal-columns-partial"
        out.append(
            {
                "disposal_coordinate_row_id": f"CFKKRGACDCE-{len(out)+1:03d}",
                "match_row_id": event["match_row_id"],
                "event_row_id": event["event_row_id"],
                "cusip": event["cusip"],
                "issuer_or_description": event["issuer_or_description"],
                "page": event["page"],
                "row_y": f"{y:.3f}",
                "disposal_date": values["disposal_date"],
                "purchaser_or_disposition_type": purchaser(items, y, parser_row.get("counterparty_or_vendor_guess", "")),
                "consideration": values["consideration"],
                "par_or_shares": values["par_or_shares"],
                "actual_cost": values["actual_cost"],
                "prior_year_book_adjusted_carrying_value": values["prior_year_book_adjusted_carrying_value"],
                "unrealized_valuation_change": values["unrealized_valuation_change"],
                "current_year_amortization_accretion": values["current_year_amortization_accretion"],
                "current_year_otti": values["current_year_otti"],
                "foreign_exchange_change": values["foreign_exchange_change"],
                "total_change_in_book_adjusted_carrying_value": values["total_change_in_book_adjusted_carrying_value"],
                "book_adjusted_carrying_value_at_disposal": values["book_adjusted_carrying_value_at_disposal"],
                "foreign_exchange_gain_loss_on_disposal": values["foreign_exchange_gain_loss_on_disposal"],
                "realized_gain_loss_on_disposal": values["realized_gain_loss_on_disposal"],
                "total_gain_loss_on_disposal": values["total_gain_loss_on_disposal"],
                "interest_or_dividends_received": values["interest_or_dividends_received"],
                "maturity_date": values["maturity_date"],
                "source_token_count": str(captured),
                "raw_parser_money_token_count": event["money_token_count"],
                "parser_row_id": event["parser_row_id"],
                "coordinate_capture_status": status,
                "proof_use": "coordinate-extracted same-CUSIP disposal row for named proceeds/gain-loss testing",
                "boundary": "coordinate columns identify statutory disposal amounts but do not prove settlement cash, lot-level continuity, borrower use, liability spread, waterfall, collateral certificate, or return",
                "next_action": "join disposal columns back to owned interest rows and issuer/wrapper evidence; request settlement or custodian support before final cash proof",
            }
        )
    return out


def diagnostic_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    status_counts = Counter(row["coordinate_capture_status"] for row in rows)
    consideration = sum(money(row["consideration"]) for row in rows)
    book_at_disposal = sum(money(row["book_adjusted_carrying_value_at_disposal"]) for row in rows)
    realized_gain_loss = sum(money(row["realized_gain_loss_on_disposal"]) for row in rows)
    total_gain_loss = sum(money(row["total_gain_loss_on_disposal"]) for row in rows)
    interest = sum(money(row["interest_or_dividends_received"]) for row in rows)
    raw_parser_token_count = sum(int(row["raw_parser_money_token_count"] or 0) for row in rows)
    coordinate_token_count = sum(int(row["source_token_count"] or 0) for row in rows)
    rows_with_consideration = sum(1 for row in rows if row["consideration"])
    metrics = [
        ("coordinate_disposal_rows", str(len(rows)), "count"),
        ("coordinate_columns_visible_rows", str(status_counts["coordinate-disposal-columns-visible"]), "count"),
        ("rows_with_consideration", str(rows_with_consideration), "count"),
        ("raw_parser_money_token_count", str(raw_parser_token_count), "count"),
        ("coordinate_source_token_count", str(coordinate_token_count), "count"),
        ("consideration_sum", fmt(consideration), "USD"),
        ("book_adjusted_carrying_value_at_disposal_sum", fmt(book_at_disposal), "USD"),
        ("realized_gain_loss_on_disposal_sum", fmt(realized_gain_loss), "USD"),
        ("total_gain_loss_on_disposal_sum", fmt(total_gain_loss), "USD"),
        ("interest_or_dividends_received_sum", fmt(interest), "USD"),
        ("largest_consideration", fmt(max((money(row["consideration"]) for row in rows), default=Decimal(0))), "USD"),
        ("plain_number_token_recovery_rows", str(sum(1 for row in rows if int(row["source_token_count"] or 0) > int(row["raw_parser_money_token_count"] or 0))), "count"),
        ("full_named_cash_proof_upgrades", "0", "count"),
        ("next_parser", "accordia-matched-disposal-owned-interest-proof-packet", "parser"),
    ]
    out: list[dict[str, str]] = []
    for idx, (metric, value, units) in enumerate(metrics, start=1):
        out.append(
            {
                "diagnostic_id": f"CFKKRGACDCEX-{idx:03d}",
                "metric": metric,
                "value": value,
                "units": units,
                "proof_use": "controls matched Accordia disposal coordinate extraction status",
                "boundary": "Disposal coordinate columns are statutory row evidence, not settlement receipts, borrower use, liability spread, waterfall, collateral certificate, IRR, NPV, ROIC, or platform profit.",
                "next_action": "Build proof packets for Intel, Commonwealth Edison, and Orange that join owned interest, disposal columns, issuer/wrapper context, and remaining controlled-document gaps.",
            }
        )
    return out


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def table(rows: list[dict[str, str]]) -> str:
    return "\n".join(
        "| {disposal_coordinate_row_id} | {cusip} | {issuer_or_description} | {consideration} | {book_adjusted_carrying_value_at_disposal} | {realized_gain_loss_on_disposal} | {interest_or_dividends_received} |".format(**row)
        for row in rows
    )


def write_memo(rows: list[dict[str, str]], diagnostics: list[dict[str, str]]) -> None:
    diag = {row["metric"]: row["value"] for row in diagnostics}
    MEMO.write_text(
        f"""# Capital Flow KKR Global Atlantic Accordia Matched Disposal Coordinate Extraction Pass 1

## Purpose

This pass coordinate-extracts the three Accordia Schedule D Part 4 disposal rows that matched top owned-bond interest-received CUSIPs.

It asks:

`Can the KKR/Global Atlantic Accordia proof stack move from raw same-CUSIP disposal tokens to coordinate-column disposal amounts for named CUSIPs without claiming final settlement cash or return?`

The structured table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-matched-disposal-coordinate-extraction-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-matched-disposal-coordinate-extraction-diagnostic-pass-1.csv`

## Short Answer

`The three same-CUSIP disposal candidates now have coordinate-column statutory disposal amounts. Consideration sums to {diag['consideration_sum']} USD, book/adjusted carrying value at disposal sums to {diag['book_adjusted_carrying_value_at_disposal_sum']} USD, realized gain/loss on disposal sums to {diag['realized_gain_loss_on_disposal_sum']} USD, and disposal-row interest/dividends received sums to {diag['interest_or_dividends_received_sum']} USD. This is proceeds-column evidence, not settlement cash, waterfall, liability-spread, or final return proof.`

## Extracted Disposal Rows

| ID | CUSIP | Issuer | Consideration | Book at Disposal | Realized Gain/Loss | Interest/Dividends |
|---|---|---|---:|---:|---:|---:|
{table(rows)}

## Diagnostics

| Metric | Value | Units |
|---|---:|---|
| Coordinate disposal rows | {diag['coordinate_disposal_rows']} | count |
| Rows with consideration | {diag['rows_with_consideration']} | count |
| Raw parser money-token count | {diag['raw_parser_money_token_count']} | count |
| Coordinate source-token count | {diag['coordinate_source_token_count']} | count |
| Consideration sum | {diag['consideration_sum']} | USD |
| Book at disposal sum | {diag['book_adjusted_carrying_value_at_disposal_sum']} | USD |
| Realized gain/loss sum | {diag['realized_gain_loss_on_disposal_sum']} | USD |
| Interest/dividends received sum | {diag['interest_or_dividends_received_sum']} | USD |
| Plain-number token recovery rows | {diag['plain_number_token_recovery_rows']} | count |
| Full named cash proof upgrades | {diag['full_named_cash_proof_upgrades']} | count |

## Proof Effect

This pass upgrades the three disposal candidates from raw-token holds to coordinate-column statutory disposal rows. It also recovers plain-number row values that the raw parser undercounted, most visibly on the Commonwealth Edison row.

The safe use is:

`Accordia has coordinate-column disposal evidence for Intel, Commonwealth Edison, and Orange same-CUSIP rows. These rows show statutory consideration, book value at disposal, realized gain/loss, and interest/dividend fields, but they do not prove settlement cash, lot-level continuity, borrower use, liability-cost spread, waterfall, collateral certificates, or return.`

## Boundary

This is not full named-cash proof. Statutory disposal consideration is a stronger proceeds-column signal than raw tokens, but it is not a custodian receipt, bank statement, trustee remittance, liability waterfall, collateral certificate, IRR, NPV, ROIC, or KKR platform profit bridge.

## Next Action

Build `accordia-matched-disposal-owned-interest-proof-packet`: join these disposal rows back to the owned interest rows, legal-entity income bridge, issuer/wrapper context, and controlled-document gaps.

## Decision

`kkr-global-atlantic-accordia-matched-disposal-coordinate-columns-visible-proof-packet-next`
""",
        encoding="utf-8",
    )


def main() -> None:
    rows = build_rows()
    diagnostics = diagnostic_rows(rows)
    write_csv(OUT, FIELDNAMES, rows)
    write_csv(DIAGNOSTIC_OUT, DIAGNOSTIC_FIELDS, diagnostics)
    write_memo(rows, diagnostics)
    print(f"wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT.relative_to(ROOT)}")
    print(f"wrote memo to {MEMO.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
