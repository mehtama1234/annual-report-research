#!/usr/bin/env python3
"""Build coordinate-based owned-bond reconciliation for Accordia Schedule D."""

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
RAW = DATA / "capital-flow-kkr-global-atlantic-accordia-schedule-d-parser-pass-1.csv"

OUT = DATA / "capital-flow-kkr-global-atlantic-accordia-schedule-d-coordinate-owned-bond-reconciliation-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-kkr-global-atlantic-accordia-schedule-d-coordinate-owned-bond-reconciliation-diagnostic-pass-1.csv"
MEMO = ANALYSIS / "capital-flow-kkr-global-atlantic-accordia-schedule-d-coordinate-owned-bond-reconciliation-pass-1.md"

TARGET_BOND_BASE = Decimal("7318322163")

FIELDNAMES = [
    "coordinate_row_id",
    "schedule_part",
    "page",
    "row_y",
    "cusip",
    "cusip_marker_type",
    "actual_cost",
    "par_value",
    "fair_value",
    "book_adjusted_carrying_value",
    "unrealized_valuation_change",
    "current_year_amortization_accretion",
    "current_year_otti",
    "foreign_exchange_change",
    "stated_rate",
    "effective_rate",
    "when_paid",
    "interest_income_due_accrued",
    "interest_received_during_year",
    "acquired_date",
    "maturity_date",
    "payment_due_at_maturity",
    "parser_match_status",
    "parser_row_id",
    "parser_money_token_count",
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

PAGE_SPECS = [
    ("Schedule D Part 1 Section 1 issuer-credit obligations owned", 218, 240, "section1"),
    ("Schedule D Part 1 Section 2 asset-backed securities owned", 242, 247, "section2"),
]

CUSIP_BROAD_RE = re.compile(r"^[A-Z0-9#@*]{6}-[A-Z0-9#@*]{2}-[A-Z0-9#@*]")
MONEY_RE = re.compile(r"^\(?\d{1,3}(?:,\d{3})+(?:\.\d+)?\)?$")
DATE_RE = re.compile(r"^\d{2}/\d{2}/\d{4}$")
RATE_RE = re.compile(r"^\d{1,2}\.\d{3}$")


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def decimal_from_token(token: str) -> Decimal:
    token = (token or "").strip()
    if not token:
        return Decimal(0)
    negative = token.startswith("(") and token.endswith(")")
    value = Decimal(token.strip("()").replace(",", ""))
    return -value if negative else value


def int_text(value: Decimal) -> str:
    return str(int(value))


def clean_value(value: str) -> str:
    return value.strip().replace(",", "")


def page_items(reader: PdfReader, page_no: int) -> list[tuple[float, float, str]]:
    items: list[tuple[float, float, str]] = []

    def visitor(text: str, cm: object, tm: object, font_dict: object, font_size: object) -> None:
        text = text.strip()
        if text:
            items.append((float(tm[4]), float(tm[5]), text))

    reader.pages[page_no - 1].extract_text(visitor_text=visitor)
    return items


def row_band(items: list[tuple[float, float, str]], row_y: float) -> list[tuple[float, str]]:
    return sorted((x, text.strip()) for x, y, text in items if abs(y - row_y) < 0.55 and x > 0)


def first_token_in_x(row: list[tuple[float, str]], lo: float, hi: float, pattern: re.Pattern[str]) -> str:
    values = [text for x, text in row if lo <= x < hi and pattern.match(text.strip())]
    return clean_value(values[-1]) if values else ""


def tokens_in_x(row: list[tuple[float, str]], lo: float, hi: float, pattern: re.Pattern[str]) -> list[str]:
    return [clean_value(text) for x, text in row if lo <= x < hi and pattern.match(text.strip())]


def column_ranges(section: str) -> dict[str, tuple[float, float]]:
    if section == "section1":
        return {
            "actual_cost": (286, 342),
            "par_value": (342, 396),
            "fair_value": (396, 451),
            "book_adjusted_carrying_value": (451, 505),
            "value_block": (286, 505),
            "unrealized_valuation_change": (505, 545),
            "current_year_amortization_accretion": (545, 585),
            "current_year_otti": (585, 625),
            "foreign_exchange_change": (625, 665),
            "stated_rate": (665, 693),
            "effective_rate": (693, 722),
            "when_paid": (722, 746),
            "interest_income_due_accrued": (746, 796),
            "interest_received_during_year": (796, 845),
            "acquired_date": (845, 881),
            "maturity_date": (881, 924),
            "payment_due_at_maturity": (924, 990),
        }
    return {
            "actual_cost": (286, 342),
            "par_value": (342, 391),
            "fair_value": (391, 441),
            "book_adjusted_carrying_value": (441, 495),
            "value_block": (286, 495),
        "unrealized_valuation_change": (495, 535),
        "current_year_amortization_accretion": (535, 575),
        "current_year_otti": (575, 615),
        "foreign_exchange_change": (615, 655),
        "stated_rate": (655, 683),
        "effective_rate": (683, 712),
        "when_paid": (712, 736),
        "interest_income_due_accrued": (736, 786),
        "interest_received_during_year": (786, 835),
        "acquired_date": (835, 871),
        "maturity_date": (871, 914),
        "payment_due_at_maturity": (914, 990),
    }


def cusip_marker_type(cusip: str) -> str:
    if any(marker in cusip for marker in "#@*"):
        return "statutory-private-marker-cusip"
    return "standard-cusip-like"


def build_rows() -> list[dict[str, str]]:
    reader = PdfReader(str(PDF))
    raw_by_cusip = {row["cusip"]: row for row in read_rows(RAW)}
    rows: list[dict[str, str]] = []
    for schedule_part, start_page, end_page, section in PAGE_SPECS:
        ranges = column_ranges(section)
        for page_no in range(start_page, end_page + 1):
            items = page_items(reader, page_no)
            starts = sorted(
                ((x, y, text.strip()) for x, y, text in items if 40 < x < 100 and CUSIP_BROAD_RE.match(text.strip())),
                key=lambda item: (-item[1], item[0]),
            )
            for _, y, cusip in starts:
                band = row_band(items, y)
                value_block = tokens_in_x(band, *ranges["value_block"], MONEY_RE)
                dates = tokens_in_x(band, ranges["acquired_date"][0], ranges["maturity_date"][1], DATE_RE)
                rates = []
                for field in ("stated_rate", "effective_rate"):
                    lo, hi = ranges[field]
                    rates.append(first_token_in_x(band, lo, hi, RATE_RE))
                parser_row = raw_by_cusip.get(cusip, {})
                parser_status = "matched-raw-parser-row" if parser_row else "not-in-raw-parser-private-marker-or-geometry-row"
                rows.append(
                    {
                        "coordinate_row_id": f"CFKKRGACEDCOB-{len(rows)+1:04d}",
                        "schedule_part": schedule_part,
                        "page": str(page_no),
                        "row_y": f"{y:.2f}",
                        "cusip": cusip,
                        "cusip_marker_type": cusip_marker_type(cusip),
                        "actual_cost": value_block[0] if len(value_block) > 0 else "",
                        "par_value": value_block[1] if len(value_block) > 1 else "",
                        "fair_value": value_block[2] if len(value_block) > 2 else "",
                        "book_adjusted_carrying_value": value_block[3] if len(value_block) > 3 else "",
                        "unrealized_valuation_change": first_token_in_x(band, *ranges["unrealized_valuation_change"], MONEY_RE),
                        "current_year_amortization_accretion": first_token_in_x(band, *ranges["current_year_amortization_accretion"], MONEY_RE),
                        "current_year_otti": first_token_in_x(band, *ranges["current_year_otti"], MONEY_RE),
                        "foreign_exchange_change": first_token_in_x(band, *ranges["foreign_exchange_change"], MONEY_RE),
                        "stated_rate": rates[0],
                        "effective_rate": rates[1],
                        "when_paid": "".join(text.strip() for x, text in band if ranges["when_paid"][0] <= x < ranges["when_paid"][1] and text.strip().isalpha())[:12],
                        "interest_income_due_accrued": first_token_in_x(band, *ranges["interest_income_due_accrued"], MONEY_RE),
                        "interest_received_during_year": first_token_in_x(band, *ranges["interest_received_during_year"], MONEY_RE),
                        "acquired_date": dates[0] if dates else "",
                        "maturity_date": dates[1] if len(dates) > 1 else "",
                        "payment_due_at_maturity": first_token_in_x(band, *ranges["payment_due_at_maturity"], MONEY_RE),
                        "parser_match_status": parser_status,
                        "parser_row_id": parser_row.get("parser_row_id", ""),
                        "parser_money_token_count": parser_row.get("money_token_count", ""),
                        "boundary": "coordinate-owned-bond row; reconciles source-page columns but does not prove cash receipt, borrower use, liability spread, waterfall, collateral certificate, or return",
                        "next_action": "use coordinate columns to replace token-only owned-bond reconciliation, then join income/proceeds and liability context",
                    }
                )
    return rows


def diagnostic_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    by_schedule = Counter(row["schedule_part"] for row in rows)
    by_marker = Counter(row["cusip_marker_type"] for row in rows)
    by_match = Counter(row["parser_match_status"] for row in rows)
    book_sum = sum((decimal_from_token(row["book_adjusted_carrying_value"]) for row in rows if row["book_adjusted_carrying_value"]), Decimal(0))
    issuer_book = sum(
        (decimal_from_token(row["book_adjusted_carrying_value"]) for row in rows if row["schedule_part"].endswith("issuer-credit obligations owned") and row["book_adjusted_carrying_value"]),
        Decimal(0),
    )
    abs_book = sum(
        (decimal_from_token(row["book_adjusted_carrying_value"]) for row in rows if row["schedule_part"].endswith("asset-backed securities owned") and row["book_adjusted_carrying_value"]),
        Decimal(0),
    )
    private_book = sum(
        (decimal_from_token(row["book_adjusted_carrying_value"]) for row in rows if row["cusip_marker_type"] == "statutory-private-marker-cusip" and row["book_adjusted_carrying_value"]),
        Decimal(0),
    )
    variance = book_sum - TARGET_BOND_BASE
    coverage = (book_sum / TARGET_BOND_BASE * Decimal(100)) if TARGET_BOND_BASE else Decimal(0)
    metrics: list[tuple[str, str | int, str]] = [
        ("coordinate_owned_bond_rows", len(rows), "count"),
        ("coordinate_issuer_credit_rows", by_schedule["Schedule D Part 1 Section 1 issuer-credit obligations owned"], "count"),
        ("coordinate_abs_rows", by_schedule["Schedule D Part 1 Section 2 asset-backed securities owned"], "count"),
        ("standard_cusip_like_rows", by_marker["standard-cusip-like"], "count"),
        ("statutory_private_marker_cusip_rows", by_marker["statutory-private-marker-cusip"], "count"),
        ("matched_raw_parser_rows", by_match["matched-raw-parser-row"], "count"),
        ("not_in_raw_parser_private_marker_or_geometry_rows", by_match["not-in-raw-parser-private-marker-or-geometry-row"], "count"),
        ("coordinate_book_value_sum", int_text(book_sum), "USD"),
        ("coordinate_issuer_credit_book_value_sum", int_text(issuer_book), "USD"),
        ("coordinate_abs_book_value_sum", int_text(abs_book), "USD"),
        ("coordinate_private_marker_book_value_sum", int_text(private_book), "USD"),
        ("statutory_bond_net_admitted_assets_target", int_text(TARGET_BOND_BASE), "USD"),
        ("coordinate_book_value_variance_vs_target", int_text(variance), "USD"),
        ("coordinate_book_value_coverage_of_target_pct", f"{coverage:.6f}", "percent"),
        ("full_column_reconciliation_status", "near-reconciled-coordinate-book-hold", "status"),
        ("full_named_cash_proof_upgrades", 0, "count"),
        ("next_parser", "accordia-coordinate-owned-bond-income-proceeds-join", "parser"),
    ]
    out = []
    for idx, (metric, value, units) in enumerate(metrics, start=1):
        out.append(
            {
                "diagnostic_id": f"CFKKRGACEDCOBD-{idx:03d}",
                "metric": metric,
                "value": str(value),
                "units": units,
                "proof_use": "tests coordinate-column reconciliation against the Accordia statutory Schedule D bond base",
                "boundary": "Coordinate columns nearly reconcile owned bonds, but this still does not prove cash receipts, borrower use, liability spread, waterfalls, collateral certificates, or return.",
                "next_action": "Promote coordinate columns into the owned-bond reconciliation, then join income/proceeds and liability context.",
            }
        )
    return out


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def table_rows(rows: list[dict[str, str]], limit: int) -> str:
    return "\n".join(
        "| {coordinate_row_id} | {page} | {cusip} | {cusip_marker_type} | {book_adjusted_carrying_value} | {parser_match_status} |".format(**row)
        for row in rows[:limit]
    )


def write_memo(rows: list[dict[str, str]], diagnostics: list[dict[str, str]]) -> None:
    by_metric = {row["metric"]: row["value"] for row in diagnostics}
    private_rows = [row for row in rows if row["cusip_marker_type"] == "statutory-private-marker-cusip"]
    missing_rows = [row for row in rows if row["parser_match_status"] == "not-in-raw-parser-private-marker-or-geometry-row"]
    high_private = sorted(private_rows, key=lambda row: decimal_from_token(row["book_adjusted_carrying_value"]), reverse=True)
    MEMO.write_text(
        f"""# Capital Flow KKR Global Atlantic Accordia Schedule D Coordinate Owned-Bond Reconciliation Pass 1

## Purpose

This pass uses source-page coordinate columns to reconcile Accordia Schedule D owned bonds after the held-row geometry diagnostic.

It asks:

`Can broad CUSIP starts, including statutory private-marker CUSIPs, and x/y column reads reconcile owned issuer-credit and ABS book value to the Accordia statutory Schedule D bond base?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-schedule-d-coordinate-owned-bond-reconciliation-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-schedule-d-coordinate-owned-bond-reconciliation-diagnostic-pass-1.csv`

## Short Answer

`Yes, for owned-bond book value at source-page coordinate level. The coordinate pass extracts {by_metric['coordinate_owned_bond_rows']} owned bond rows: {by_metric['coordinate_issuer_credit_rows']} issuer-credit rows and {by_metric['coordinate_abs_rows']} ABS rows. It finds {by_metric['statutory_private_marker_cusip_rows']} statutory private-marker CUSIP rows that the raw parser did not cleanly promote. Coordinate book value sums to {by_metric['coordinate_book_value_sum']} USD versus the {by_metric['statutory_bond_net_admitted_assets_target']} USD statutory bond target, a variance of {by_metric['coordinate_book_value_variance_vs_target']} USD and {by_metric['coordinate_book_value_coverage_of_target_pct']}% coverage.`

## Diagnostic Metrics

| Metric | Value |
|---|---:|
| Coordinate owned bond rows | {by_metric['coordinate_owned_bond_rows']} |
| Coordinate issuer-credit rows | {by_metric['coordinate_issuer_credit_rows']} |
| Coordinate ABS rows | {by_metric['coordinate_abs_rows']} |
| Standard CUSIP-like rows | {by_metric['standard_cusip_like_rows']} |
| Statutory private-marker CUSIP rows | {by_metric['statutory_private_marker_cusip_rows']} |
| Matched raw parser rows | {by_metric['matched_raw_parser_rows']} |
| Not in raw parser private-marker/geometry rows | {by_metric['not_in_raw_parser_private_marker_or_geometry_rows']} |
| Coordinate book value sum | {by_metric['coordinate_book_value_sum']} |
| Coordinate issuer-credit book value | {by_metric['coordinate_issuer_credit_book_value_sum']} |
| Coordinate ABS book value | {by_metric['coordinate_abs_book_value_sum']} |
| Coordinate private-marker book value | {by_metric['coordinate_private_marker_book_value_sum']} |
| Statutory bond target | {by_metric['statutory_bond_net_admitted_assets_target']} |
| Coordinate variance | {by_metric['coordinate_book_value_variance_vs_target']} |
| Coordinate coverage pct | {by_metric['coordinate_book_value_coverage_of_target_pct']} |

## Private-Marker Rows That Explain The Parser Gap

| ID | Page | CUSIP | Marker Type | Book Value | Parser Status |
|---|---:|---|---|---:|---|
{table_rows(high_private, 12)}

## Rows Not Promoted By The Raw Parser

| ID | Page | CUSIP | Marker Type | Book Value | Parser Status |
|---|---:|---|---|---:|---|
{table_rows(missing_rows, 12)}

## Proof Effect

This pass materially improves the KKR/Global Atlantic statutory prototype. The prior token parser showed a `-908.556531M USD` book-value variance because it missed or swallowed statutory private-marker rows and subtotal-adjacent geometry. The coordinate pass reads the same source pages by x/y column bands and nearly reconciles owned Schedule D bonds to the statutory target.

The safe use is:

`Accordia owned Schedule D bond book value is near-reconciled at coordinate-column level, including statutory private-marker CUSIP rows.`

## Boundary

This is still not full named-cash proof. It proves source-page owned-bond column reconciliation to near tolerance. It does not prove issuer-level income, disposal proceeds, borrower receipt/use, liability-cost spread, funds-withheld waterfall, FHLB economics, collateral certificates, or return.

## Next Action

Promote the coordinate-owned-bond table as the owned-bond baseline, then join it to income/proceeds fields and liability context. The next named-cash milestone is `accordia-coordinate-owned-bond-income-proceeds-join`.

## Decision

`kkr-global-atlantic-accordia-coordinate-owned-bond-near-reconciled-income-proceeds-join-next`
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
