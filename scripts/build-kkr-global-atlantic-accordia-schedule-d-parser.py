#!/usr/bin/env python3
"""Parse Accordia Q4 2025 Schedule D rows from the Global Atlantic statutory filing."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
ANALYSIS = ROOT / "analysis/company-first-principles"
PDF = ROOT / "raw/primary-sources/capital-flow/kkr/global-atlantic/statutory/2025/Accordia_4Q_2025_Quarterly_Statements.pdf"

OUT = DATA / "capital-flow-kkr-global-atlantic-accordia-schedule-d-parser-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-kkr-global-atlantic-accordia-schedule-d-parser-diagnostic-pass-1.csv"
MEMO = ANALYSIS / "capital-flow-kkr-global-atlantic-accordia-schedule-d-parser-pass-1.md"

FIELDNAMES = [
    "parser_row_id",
    "schedule_part",
    "page",
    "cusip",
    "issuer_or_description",
    "asset_type_guess",
    "naic_designation_detected",
    "transaction_date_1",
    "transaction_date_2",
    "counterparty_or_vendor_guess",
    "money_token_count",
    "money_tokens_first_12",
    "raw_text",
    "current_status",
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
    ("Schedule D Part 1 Section 1 issuer-credit obligations owned", 218, 240),
    ("Schedule D Part 1 Section 2 asset-backed securities owned", 242, 247),
    ("Schedule D Part 2 Section 2 common stocks owned", 248, 248),
    ("Schedule D Part 3 acquired during year", 249, 258),
    ("Schedule D Part 4 sold/redeemed/disposed during year", 259, 268),
    ("Schedule D Part 5 acquired and fully disposed during year", 269, 270),
]

START_RE = re.compile(r"^(?P<cusip>[A-Z0-9]{6}-[A-Z0-9]{2}-[A-Z0-9])\s+\.{2,}\s*(?P<body>.*)$")
SUBTOTAL_RE = re.compile(r"^\d{3,7}\.")
DATE_RE = re.compile(r"\d{2}/\d{2}/\d{4}")
NAIC_RE = re.compile(r"\b([1-6]\.[A-Z])\b|\b([1-6]\.)\b")
MONEY_RE = re.compile(r"\(?\d{1,3}(?:,\d{3})+(?:\.\d+)?\)?")


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\u0092", "'").replace("", "'")).strip()


def page_lines(reader: PdfReader, page: int) -> list[str]:
    return [clean(line) for line in (reader.pages[page - 1].extract_text() or "").splitlines() if clean(line)]


def is_noise(line: str) -> bool:
    if not line:
        return True
    upper = line.upper()
    if upper.startswith("ANNUAL STATEMENT") or upper.startswith("SCHEDULE D"):
        return True
    if upper.startswith("SHOWING ALL") or upper in {"CUSIP", "IDENTIFICATION", "DESCRIPTION"}:
        return True
    if SUBTOTAL_RE.match(line):
        return True
    return False


def split_issuer_and_body(body: str) -> tuple[str, str]:
    parts = re.split(r"\s+\.{2,}\s+", body, maxsplit=1)
    issuer = clean(parts[0])
    rest = clean(parts[1]) if len(parts) > 1 else ""
    return issuer, rest


def first_naic(text: str) -> str:
    match = NAIC_RE.search(text)
    if not match:
        return ""
    return match.group(1) or match.group(2) or ""


def classify(schedule: str, issuer: str) -> str:
    lower = issuer.lower()
    if "asset-backed" in schedule.lower() or " - abs" in lower or "rmbs" in lower or "cmbs" in lower:
        return "asset_backed_security"
    if "common stocks" in schedule.lower():
        return "common_stock"
    if "treasury" in lower:
        return "us_treasury"
    if "bank" in lower or "bancorp" in lower:
        return "bank_or_financial_credit"
    if "capital" in lower or "finance" in lower or "funding" in lower:
        return "finance_company_or_funding_vehicle"
    if "electric" in lower or "energy" in lower or "gas" in lower or "utility" in lower:
        return "utility_or_energy_credit"
    return "issuer_credit_or_corporate_bond"


def counterparty_guess(rest: str, dates: list[str]) -> str:
    if not dates:
        return ""
    after = rest.split(dates[0], 1)[-1]
    after = re.sub(r"\.{2,}", " ", after)
    after = MONEY_RE.split(after, maxsplit=1)[0]
    return clean(after)[:140]


def parse_schedule(reader: PdfReader, schedule: str, start_page: int, end_page: int) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for page in range(start_page, end_page + 1):
        current_cusip = ""
        current_parts: list[str] = []

        def flush() -> None:
            nonlocal current_cusip, current_parts
            if not current_cusip:
                return
            raw = clean(" ".join(current_parts))
            issuer, rest = split_issuer_and_body(raw)
            dates = DATE_RE.findall(rest)
            money = MONEY_RE.findall(rest)
            rows.append(
                {
                    "schedule_part": schedule,
                    "page": str(page),
                    "cusip": current_cusip,
                    "issuer_or_description": issuer[:180],
                    "asset_type_guess": classify(schedule, issuer),
                    "naic_designation_detected": first_naic(rest),
                    "transaction_date_1": dates[0] if dates else "",
                    "transaction_date_2": dates[1] if len(dates) > 1 else "",
                    "counterparty_or_vendor_guess": counterparty_guess(rest, dates),
                    "money_token_count": str(len(money)),
                    "money_tokens_first_12": "; ".join(money[:12]),
                    "raw_text": raw[:1200],
                    "current_status": "raw-schedule-d-row-parsed",
                    "boundary": "raw Schedule D parser row; numeric tokens are preserved but not yet assigned to final statutory columns or reconciled to totals",
                    "next_action": "assign numeric tokens to statutory columns and reconcile by schedule part",
                }
            )
            current_cusip = ""
            current_parts = []

        for line in page_lines(reader, page):
            match = START_RE.match(line)
            if match:
                flush()
                current_cusip = match.group("cusip")
                current_parts = [match.group("body")]
            elif current_cusip and not is_noise(line):
                current_parts.append(line)
        flush()
    return rows


def build_rows() -> list[dict[str, str]]:
    reader = PdfReader(str(PDF))
    rows: list[dict[str, str]] = []
    for schedule, start_page, end_page in PAGE_SPECS:
        rows.extend(parse_schedule(reader, schedule, start_page, end_page))
    for idx, row in enumerate(rows, start=1):
        row["parser_row_id"] = f"CFKKRGACEDP-{idx:04d}"
    return rows


def diagnostic_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    by_schedule = Counter(r["schedule_part"] for r in rows)
    by_asset = Counter(r["asset_type_guess"] for r in rows)
    with_money = sum(1 for r in rows if int(r["money_token_count"]) > 0)
    with_dates = sum(1 for r in rows if r["transaction_date_1"])
    metrics: list[tuple[str, str | int, str]] = [
        ("parsed_schedule_d_rows", len(rows), "count"),
        ("owned_issuer_credit_rows", by_schedule["Schedule D Part 1 Section 1 issuer-credit obligations owned"], "count"),
        ("owned_abs_rows", by_schedule["Schedule D Part 1 Section 2 asset-backed securities owned"], "count"),
        ("owned_common_stock_rows", by_schedule["Schedule D Part 2 Section 2 common stocks owned"], "count"),
        ("acquired_rows", by_schedule["Schedule D Part 3 acquired during year"], "count"),
        ("disposed_rows", by_schedule["Schedule D Part 4 sold/redeemed/disposed during year"], "count"),
        ("same_year_acquired_disposed_rows", by_schedule["Schedule D Part 5 acquired and fully disposed during year"], "count"),
        ("rows_with_money_tokens", with_money, "count"),
        ("rows_with_dates", with_dates, "count"),
        ("asset_backed_security_rows", by_asset["asset_backed_security"], "count"),
        ("bank_or_financial_credit_rows", by_asset["bank_or_financial_credit"], "count"),
        ("finance_company_or_funding_vehicle_rows", by_asset["finance_company_or_funding_vehicle"], "count"),
        ("utility_or_energy_credit_rows", by_asset["utility_or_energy_credit"], "count"),
        ("full_named_cash_proof_upgrades", 0, "count"),
        ("next_parser", "accordia-schedule-d-column-reconciliation", "parser"),
    ]
    out = []
    for idx, (metric, value, units) in enumerate(metrics, start=1):
        out.append(
            {
                "diagnostic_id": f"CFKKRGACEDPD-{idx:03d}",
                "metric": metric,
                "value": str(value),
                "units": units,
                "proof_use": "controls Accordia Schedule D raw parser coverage",
                "boundary": "Diagnostics summarize raw parsed rows only; they do not prove final column assignment, cash receipt, borrower use, or return.",
                "next_action": "perform column reconciliation by Schedule D part and reconcile to statutory summary totals.",
            }
        )
    return out


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_memo(rows: list[dict[str, str]], diagnostics: list[dict[str, str]]) -> None:
    by_metric = {r["metric"]: r["value"] for r in diagnostics}
    sample = rows[:12]
    sample_table = "\n".join(
        "| {parser_row_id} | {schedule_part} | {page} | {cusip} | {issuer_or_description} | {asset_type_guess} |".format(**r)
        for r in sample
    )
    MEMO.write_text(
        f"""# Capital Flow KKR Global Atlantic Accordia Schedule D Parser Pass 1

## Purpose

This pass parses Accordia Q4 `2025` Schedule D pages `220-270` into raw CUSIP-level rows.

It asks:

`Can we move from Accordia legal-entity totals and Schedule D samples into a full named security row set for owned, acquired, disposed, and same-year acquisition/disposal securities?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-schedule-d-parser-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-schedule-d-parser-diagnostic-pass-1.csv`

## Short Answer

`Yes, at raw parser level. The pass creates {by_metric['parsed_schedule_d_rows']} CUSIP-level Schedule D rows: {by_metric['owned_issuer_credit_rows']} owned issuer-credit rows, {by_metric['owned_abs_rows']} owned ABS rows, {by_metric['owned_common_stock_rows']} common-stock rows, {by_metric['acquired_rows']} acquired rows, {by_metric['disposed_rows']} disposed/redeemed rows, and {by_metric['same_year_acquired_disposed_rows']} same-year acquired/disposed rows. This materially upgrades KKR/Global Atlantic from named samples to a full raw named-security universe, but still needs column reconciliation before cash/proceeds/return claims.`

## Parser Coverage

| Metric | Value |
|---|---:|
| Parsed Schedule D rows | {by_metric['parsed_schedule_d_rows']} |
| Owned issuer-credit rows | {by_metric['owned_issuer_credit_rows']} |
| Owned ABS rows | {by_metric['owned_abs_rows']} |
| Common-stock rows | {by_metric['owned_common_stock_rows']} |
| Acquired rows | {by_metric['acquired_rows']} |
| Disposed/redeemed rows | {by_metric['disposed_rows']} |
| Same-year acquired/disposed rows | {by_metric['same_year_acquired_disposed_rows']} |
| Rows with numeric tokens | {by_metric['rows_with_money_tokens']} |
| Rows with transaction dates | {by_metric['rows_with_dates']} |
| Full named cash proof upgrades | {by_metric['full_named_cash_proof_upgrades']} |

## First Rows

| ID | Schedule | Page | CUSIP | Issuer / Description | Type |
|---|---|---:|---|---|---|
{sample_table}

## Proof Effect

This pass moves the KKR/Global Atlantic / Accordia case from compact legal-entity bridge to a raw named-security universe. It now shows the filing can be parsed into exact CUSIPs and issuer names across owned bonds/ABS, acquisitions, disposals/redemptions, and same-year round-trip securities.

## Boundary

This is still not final named cash proof.

The parser preserves raw numeric tokens but does not yet assign every number to final statutory columns such as actual cost, par, fair value, book value, consideration, realized gain/loss, interest income, or interest received. It also does not prove borrower receipt/use, liability-cost spread, funds-withheld waterfall, FHLB economics, collateral certificates, or return.

## Next Action

Run `accordia-schedule-d-column-reconciliation` by schedule part, then reconcile owned rows to the `7.318322163B USD` Schedule D bond base and disposal rows to cash-flow/income/proceeds fields.

## Decision

`kkr-global-atlantic-accordia-schedule-d-parser-raw-named-security-universe-visible-column-reconciliation-next`
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
