#!/usr/bin/env python3
"""Extract first-pass Schedule BA/D detail samples from Athene statutory PDF."""

from __future__ import annotations

import csv
import re
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw/primary-sources/capital-flow/apollo/athene/statutory/2025/athene-annuity-and-life-company-2025-statutory-statement.pdf"
OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-parser-prototype-pass-1.csv"
NORM_OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-normalized-sample-pass-1.csv"
FULL_D_OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-full-range-parser-pass-1.csv"

PAGE_SPECS = [
    ("Schedule BA Part 1", 5813, 18),
    ("Schedule BA Part 2", 5826, 14),
    ("Schedule D Part 1 Section 1", 5836, 25),
    ("Schedule D Part 1 Section 2", 5912, 25),
]

FULL_SCHEDULE_D_SPECS = [
    ("Schedule D Part 1 Section 1", 5836, 5911),
    ("Schedule D Part 1 Section 2", 5912, 6027),
]

START_RE = re.compile(r"^(?P<id>(?:[A-Z0-9*@#]{6}-[A-Z0-9*@#]{2}-[A-Z0-9*@#]|[A-Z0-9]{6,9}[.*]))\s+\.{2,}\s*(?P<body>.*)")
SUBTOTAL_RE = re.compile(r"^\d{6,7}\.")
NAIC_RE = re.compile(r"\b(?P<naic>[1-6]\.[A-Z])\b|\b(?P<naic_plain>[1-6]\.)\b")
MONEY_RE = re.compile(r"(?<![\w.])\(?\d{1,3}(?:,\d{3})+(?:\.\d+)?\)?(?![\w.])")
DETAIL_MONEY_RE = re.compile(r"\(?\d{1,3}(?:,\d{3})+(?:\.\d+)?\)?")
DETAIL_NUMBER_RE = re.compile(r"^\(?\d[\d,]*(?:\.\d+)?\)?$")
DATE_RE = re.compile(r"\d{2}/\d{2}/\d{4}")
ABS_RATE_RE = re.compile(r"\s+\.{2,}\s*\(?\d+\.\d{3}\)?\s+\.{2,}\s*\(?\d+\.\d{3}\)?\s+[A-Z]{3}\b")


def page_lines(reader: PdfReader, page_no: int) -> list[str]:
    text = reader.pages[page_no - 1].extract_text() or ""
    return [line.strip() for line in text.splitlines() if line.strip()]


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("", "'")).strip()


def extract_rows(lines: list[str], limit: int | None = None) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    current_id = ""
    current_parts: list[str] = []

    def flush() -> None:
        nonlocal current_id, current_parts
        if current_id and current_parts:
            raw = clean(" ".join(current_parts))
            if raw and not SUBTOTAL_RE.match(current_id):
                rows.append((current_id, raw))
        current_id = ""
        current_parts = []

    for line in lines:
        if limit is not None and len(rows) >= limit:
            break
        match = START_RE.match(line)
        if match:
            flush()
            current_id = clean(match.group("id").replace(" ", ""))
            body = match.group("body")
            current_parts = [body] if body else []
            continue
        if current_id:
            current_parts.append(line)

    flush()
    return rows[:limit] if limit is not None else rows


def classify(schedule: str, raw: str) -> str:
    lowered = raw.lower()
    if "government national mortgage" in lowered or "gnr " in lowered:
        return "agency_mbs_or_abs"
    if "treasury" in lowered:
        return "us_treasury"
    if "mortgage trust" in lowered or "capital i trust" in lowered:
        return "structured_credit_or_cmbs"
    if "credit fund" in lowered:
        return "credit_fund_or_private_credit_vehicle"
    if "ap " in lowered or "athene" in lowered:
        return "affiliated_or_apollo_related"
    if "Schedule BA" in schedule:
        return "schedule_ba_other_invested_asset"
    return "issuer_credit_or_bond"


def first_naic(raw: str) -> str:
    match = NAIC_RE.search(raw)
    if not match:
        return ""
    return match.group("naic") or match.group("naic_plain") or ""


def first_money_values(raw: str, count: int = 8) -> str:
    return "; ".join(MONEY_RE.findall(raw)[:count])


def money_tokens(raw: str) -> list[str]:
    return [token.strip() for token in DETAIL_MONEY_RE.findall(raw)]


def date_tokens(raw: str) -> list[str]:
    return DATE_RE.findall(raw)


def issuer_description(raw: str) -> str:
    text = re.split(r"\s+\.{3,}\s+", raw, maxsplit=1)[0]
    return clean(text)[:220]


def clean_numeric_slot(value: str) -> str:
    cleaned = clean(value)
    return cleaned if DETAIL_NUMBER_RE.match(cleaned) else ""


def abs_numeric_columns(raw: str) -> dict[str, str] | None:
    pre_rate = ABS_RATE_RE.split(raw, maxsplit=1)[0]
    parts = [part.strip() for part in re.split(r"\.{2,}", pre_rate)]
    naic_idx = -1
    for idx, part in enumerate(parts):
        if NAIC_RE.search(part):
            naic_idx = idx
            break
    if naic_idx < 0:
        return None

    slots = [clean_numeric_slot(part) for part in parts[naic_idx + 2 : naic_idx + 10]]
    slots.extend([""] * (8 - len(slots)))
    return {
        "actual_cost": slots[0],
        "par_value": slots[1],
        "fair_value": slots[2],
        "book_adjusted_carrying_value": slots[3],
        "unrealized_valuation_change": slots[4],
    }


def normalized_schedule_d_row(
    row: dict[str, str],
    seq: int,
    row_id_prefix: str = "CFAASDNS",
    row_id_width: int = 3,
    status: str = "normalized-schedule-d-sample-visible",
    boundary: str = "first normalized Schedule D sample; numeric columns are positional parser output and require statement-column reconciliation before asset-level cash-return use",
) -> dict[str, str]:
    raw = row["name_and_raw_terms"]
    values = money_tokens(raw)
    dates = date_tokens(raw)
    is_abs = row["schedule"].endswith("Section 2")

    # Schedule D columns are dense in extracted text. This sample intentionally
    # uses a conservative positional parse and keeps the row boundary explicit.
    corrected_abs = abs_numeric_columns(raw) if is_abs else None
    actual_cost = corrected_abs["actual_cost"] if corrected_abs else (values[0] if len(values) > 0 else "")
    par_value = corrected_abs["par_value"] if corrected_abs else ("" if is_abs else (values[1] if len(values) > 1 else ""))
    fair_value = corrected_abs["fair_value"] if corrected_abs else (values[1] if is_abs and len(values) > 1 else (values[2] if len(values) > 2 else ""))
    book_value = corrected_abs["book_adjusted_carrying_value"] if corrected_abs else (values[2] if is_abs and len(values) > 2 else (values[3] if len(values) > 3 else ""))
    unrealized = corrected_abs["unrealized_valuation_change"] if corrected_abs else (values[3] if is_abs and len(values) > 3 else (values[4] if len(values) > 4 else ""))
    interest_income = values[-2] if len(values) >= 2 else ""
    interest_received = values[-1] if values else ""

    acquired_date = dates[-2] if len(dates) >= 2 else (dates[0] if dates else "")
    maturity_date = dates[-1] if dates else ""

    return {
        "normalized_row_id": f"{row_id_prefix}-{seq:0{row_id_width}d}",
        "source_parser_row_id": row["parser_row_id"],
        "schedule": row["schedule"],
        "page": row["page"],
        "cusip": row["cusip_or_identifier"],
        "issuer_or_description": issuer_description(raw),
        "naic_designation": row["naic_designation_detected"],
        "asset_type_guess": row["asset_type_guess"],
        "actual_cost": actual_cost,
        "par_value": par_value,
        "fair_value": fair_value,
        "book_adjusted_carrying_value": book_value,
        "unrealized_valuation_change": unrealized,
        "interest_income": interest_income,
        "interest_received_during_year": interest_received,
        "acquired_date": acquired_date,
        "maturity_date": maturity_date,
        "current_status": status,
        "boundary": boundary,
    }


def write_normalized_rows(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "normalized_row_id",
                "source_parser_row_id",
                "schedule",
                "page",
                "cusip",
                "issuer_or_description",
                "naic_designation",
                "asset_type_guess",
                "actual_cost",
                "par_value",
                "fair_value",
                "book_adjusted_carrying_value",
                "unrealized_valuation_change",
                "interest_income",
                "interest_received_during_year",
                "acquired_date",
                "maturity_date",
                "current_status",
                "boundary",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def write_normalized_schedule_d(rows: list[dict[str, str]]) -> None:
    norm_rows = [
        normalized_schedule_d_row(
            row,
            seq,
            row_id_prefix="CFAASDNS",
            row_id_width=3,
            status="normalized-schedule-d-sample-visible",
            boundary="first normalized Schedule D sample; numeric columns are positional parser output and require statement-column reconciliation before asset-level cash-return use",
        )
        for seq, row in enumerate((r for r in rows if r["schedule"].startswith("Schedule D")), start=1)
    ]
    write_normalized_rows(NORM_OUT, norm_rows)
    print(f"wrote {len(norm_rows)} rows to {NORM_OUT.relative_to(ROOT)}")


def schedule_d_full_range_rows(reader: PdfReader) -> list[dict[str, str]]:
    raw_rows: list[dict[str, str]] = []
    seq = 1
    for schedule, start_page, end_page in FULL_SCHEDULE_D_SPECS:
        for page_no in range(start_page, end_page + 1):
            for identifier, raw in extract_rows(page_lines(reader, page_no)):
                raw_rows.append(
                    {
                        "parser_row_id": f"CFAASDFR-{seq:04d}",
                        "schedule": schedule,
                        "page": str(page_no),
                        "cusip_or_identifier": identifier,
                        "name_and_raw_terms": raw[:900],
                        "naic_designation_detected": first_naic(raw),
                        "asset_type_guess": classify(schedule, raw),
                    }
                )
                seq += 1

    return [
        normalized_schedule_d_row(
            row,
            seq,
            row_id_prefix="CFAASDFR",
            row_id_width=4,
            status="full-range-schedule-d-parser-row-visible",
            boundary="full Schedule D range parser output; row boundaries and positional numeric fields require reconciliation to statutory verification totals before asset-level cash-return use",
        )
        for seq, row in enumerate(raw_rows, start=1)
    ]


def write_full_range_schedule_d(reader: PdfReader) -> None:
    rows = schedule_d_full_range_rows(reader)
    write_normalized_rows(FULL_D_OUT, rows)
    print(f"wrote {len(rows)} rows to {FULL_D_OUT.relative_to(ROOT)}")


def main() -> None:
    reader = PdfReader(str(PDF))
    out_rows: list[dict[str, str]] = []
    seq = 1
    for schedule, page_no, limit in PAGE_SPECS:
        rows = extract_rows(page_lines(reader, page_no), limit)
        for identifier, raw in rows:
            out_rows.append(
                {
                    "parser_row_id": f"CFAASPP-{seq:03d}",
                    "schedule": schedule,
                    "page": str(page_no),
                    "cusip_or_identifier": identifier,
                    "name_and_raw_terms": raw[:700],
                    "naic_designation_detected": first_naic(raw),
                    "asset_type_guess": classify(schedule, raw),
                    "first_numeric_values": first_money_values(raw),
                    "current_status": "parser-prototype-row-visible",
                    "proof_use": "repeatable named statutory holding extraction row",
                    "boundary": "prototype row; column-level statutory values still need schedule-specific normalization and reconciliation",
                }
            )
            seq += 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "parser_row_id",
                "schedule",
                "page",
                "cusip_or_identifier",
                "name_and_raw_terms",
                "naic_designation_detected",
                "asset_type_guess",
                "first_numeric_values",
                "current_status",
                "proof_use",
                "boundary",
            ],
        )
        writer.writeheader()
        writer.writerows(out_rows)
    print(f"wrote {len(out_rows)} rows to {OUT.relative_to(ROOT)}")
    write_normalized_schedule_d(out_rows)
    write_full_range_schedule_d(reader)


if __name__ == "__main__":
    main()
