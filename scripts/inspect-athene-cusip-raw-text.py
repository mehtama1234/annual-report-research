#!/usr/bin/env python3
"""Extract raw PDF text rows for selected Athene CUSIP proof packets."""

from __future__ import annotations

import csv
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PARSER_SCRIPT = ROOT / "scripts/extract-athene-statutory-detail-samples.py"
DATA = ROOT / "analysis/company-first-principles/data"
DETAIL = DATA / "capital-flow-apollo-athene-statutory-cusip-row-proof-packet-detail-pass-1.csv"
OUT = DATA / "capital-flow-apollo-athene-statutory-cusip-raw-text-inspection-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-apollo-athene-statutory-cusip-raw-text-inspection-diagnostic-pass-1.csv"

SELECTED_CUSIPS = {"00264#-AB-3", "28655*-AA-7", "02300A-AA-8"}

FIELDNAMES = [
    "raw_text_row_id",
    "proof_packet_id",
    "cusip",
    "source_row_type",
    "source_row_id",
    "source_schedule",
    "source_page",
    "raw_row_found",
    "raw_row_text",
    "raw_row_money_token_count",
    "raw_row_date_token_count",
    "parser_numeric_values",
    "parser_consideration_or_fair_value_usd",
    "parser_book_or_disposal_book_usd",
    "parser_gain_or_income_usd",
    "parser_interest_received_usd",
    "inspection_status",
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


def load_parser_module():
    spec = importlib.util.spec_from_file_location("athene_schedule_d_parser", PARSER_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load parser script: {PARSER_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def page_rows(parser_module, reader, page: int) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for cusip, raw in parser_module.extract_rows(parser_module.page_lines(reader, page)):
        rows.append((cusip, raw))
    return rows


def normalized_amount(value: str) -> str:
    value = (value or "").strip()
    if "." in value:
        value = value.split(".", 1)[0]
    return f"{int(value):,}" if value.isdigit() else value


def raw_for_detail(page_rows_for_page: list[tuple[str, str]], detail: dict[str, str]) -> str:
    candidates = [raw for cusip, raw in page_rows_for_page if cusip == detail["cusip"]]
    if not candidates:
        return ""
    if len(candidates) == 1:
        return candidates[0]

    amount = normalized_amount(detail["fair_value_or_consideration_usd"])
    date = detail["date_1"]
    label = detail["counterparty_or_disposition"].split()[0] if detail["counterparty_or_disposition"] else ""
    scored: list[tuple[int, str]] = []
    for raw in candidates:
        score = 0
        if amount and amount in raw:
            score += 3
        if date and date in raw:
            score += 2
        if label and label in raw:
            score += 1
        scored.append((score, raw))
    scored.sort(key=lambda item: item[0], reverse=True)
    return scored[0][1]


def status(source_type: str, raw: str, money_count: int) -> str:
    if not raw:
        return "raw-row-not-found-hold"
    if source_type == "disposal_or_proceeds" and money_count <= 5:
        return "raw-row-found-short-numeric-stream-parser-column-hold"
    return "raw-row-found-inspection-ready"


def main() -> None:
    parser_module = load_parser_module()
    reader = parser_module.PdfReader(str(parser_module.PDF))
    candidates = [row for row in read_rows(DETAIL) if row["cusip"] in SELECTED_CUSIPS]

    page_cache: dict[int, list[tuple[str, str]]] = {}
    output: list[dict[str, str]] = []
    for idx, row in enumerate(candidates, start=1):
        page = int(row["source_page"])
        if page not in page_cache:
            page_cache[page] = page_rows(parser_module, reader, page)
        raw = raw_for_detail(page_cache[page], row)
        money_tokens = parser_module.money_tokens(raw)
        date_tokens = parser_module.date_tokens(raw)
        output.append(
            {
                "raw_text_row_id": f"CFAASCRTI-{idx:03d}",
                "proof_packet_id": row["proof_packet_id"],
                "cusip": row["cusip"],
                "source_row_type": row["source_row_type"],
                "source_row_id": row["source_row_id"],
                "source_schedule": row["source_schedule"],
                "source_page": row["source_page"],
                "raw_row_found": "yes" if raw else "no",
                "raw_row_text": raw[:1200],
                "raw_row_money_token_count": str(len(money_tokens)),
                "raw_row_date_token_count": str(len(date_tokens)),
                "parser_numeric_values": row["raw_numeric_values"],
                "parser_consideration_or_fair_value_usd": row["fair_value_or_consideration_usd"],
                "parser_book_or_disposal_book_usd": row["book_value_or_disposal_book_usd"],
                "parser_gain_or_income_usd": row["interest_income_or_realized_gain_loss_usd"],
                "parser_interest_received_usd": row["interest_received_or_dividends_usd"],
                "inspection_status": status(row["source_row_type"], raw, len(money_tokens)),
                "boundary": "raw PDF text extraction supports row inspection but does not by itself prove column semantics, borrower cash, liability spread, or asset return",
                "next_action": "inspect statutory row columns visually or with page-specific column parsing before promoting consideration, gain/loss, and interest fields",
            }
        )

    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(output)

    found = sum(1 for row in output if row["raw_row_found"] == "yes")
    short = sum(1 for row in output if row["inspection_status"] == "raw-row-found-short-numeric-stream-parser-column-hold")
    diagnostics = [
        ("raw_text_inspection_rows", len(output), "count"),
        ("raw_rows_found", found, "count"),
        ("raw_rows_missing", len(output) - found, "count"),
        ("short_numeric_stream_holds", short, "count"),
        ("selected_cusips", len(SELECTED_CUSIPS), "count"),
        ("selected_pages", len({row["source_page"] for row in output}), "count"),
    ]
    with DIAGNOSTIC_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DIAGNOSTIC_FIELDS)
        writer.writeheader()
        for idx, (metric, value, units) in enumerate(diagnostics, start=1):
            writer.writerow(
                {
                    "diagnostic_id": f"CFAASCRTID-{idx:03d}",
                    "metric": metric,
                    "value": str(value),
                    "units": units,
                    "proof_use": "raw PDF text inspection for selected CUSIP row proof packets",
                    "boundary": "raw text confirms row availability but not final statutory column semantics or return proof",
                    "next_action": "perform page-specific column inspection for rows with short or suspicious numeric streams",
                }
            )

    print(f"wrote {len(output)} rows to {OUT}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT}")
    print({"found": found, "short_numeric_stream_holds": short})


if __name__ == "__main__":
    main()
