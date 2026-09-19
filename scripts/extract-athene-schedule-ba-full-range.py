#!/usr/bin/env python3
"""Extract Athene Schedule BA Parts 1-3 and reconcile visible control rows.

This is deliberately a raw/detail pass.  Schedule BA has different layouts
between owned assets, additions, and disposals, so the parser preserves the
source row text and only promotes the visible control subtotal.  It does not
impute blank columns or treat acquisition/disposal rows as year-end holdings.
"""

from __future__ import annotations

import csv
import importlib.util
import re
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw/primary-sources/capital-flow/apollo/athene/statutory/2025/athene-annuity-and-life-company-2025-statutory-statement.pdf"
OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-full-range-parser-pass-1.csv"
CONTROL_OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-ba-control-reconciliation-pass-1.csv"

BA_SPECS = [
    ("Schedule BA Part 1", 5813, 5825, "year-end-owned-assets"),
    ("Schedule BA Part 2", 5826, 5829, "current-year-acquisitions-additions"),
    ("Schedule BA Part 3", 5830, 5835, "current-year-disposals-transfers-repayments"),
]

START_RE = re.compile(r"^(?P<id>(?:[A-Z0-9*@#]{6}-[A-Z0-9*@#]{2}-[A-Z0-9*@#]|[A-Z0-9]{6,9}[.*]))\s+\.{2,}\s*(?P<body>.*)")
# Most controls use ``1239999.``, while the final BA total is printed as
# ``7099999 - Totals`` on the source page.
SUBTOTAL_RE = re.compile(r"^(?P<code>\d{6,7})(?:\.|\s+-\s+)\s*(?P<body>.*)$")
MONEY_RE = re.compile(r"(?<![\w.])\(?\d{1,3}(?:,\d{3})+(?:\.\d+)?\)?(?![\w.])")
# pypdf sometimes places a numeric field directly after a dot-marker run
# (``......85,081,101``).  The field is still complete; do not drop its
# leading digits merely because the preceding character is a period.
BA_MONEY_RE = re.compile(r"(?<!\d)\(?\d{1,3}(?:,\d{3})+(?:\.\d+)?\)?")
NAIC_RE = re.compile(r"\b(?P<naic>[1-6]\.[A-Z])\b|\b(?P<naic_plain>[1-6]\.)(?!\d)")


def load_detail_helpers():
    path = Path(__file__).with_name("extract-athene-statutory-detail-samples.py")
    spec = importlib.util.spec_from_file_location("athene_detail_helpers", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


HELPERS = load_detail_helpers()


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("", "'")).strip()


def page_lines(reader: PdfReader, page_no: int) -> list[str]:
    text = reader.pages[page_no - 1].extract_text() or ""
    return [line.strip() for line in text.splitlines() if line.strip()]


def extract_control_rows(lines: list[str]) -> list[tuple[str, str]]:
    controls: list[tuple[str, str]] = []
    for line in lines:
        match = SUBTOTAL_RE.match(line.strip())
        if match:
            controls.append((match.group("code"), clean(match.group("body"))))
    return controls


def extract_ba_rows(lines: list[str]) -> list[tuple[str, str]]:
    """Extract CUSIP-bearing rows while stopping at BA subtotal boundaries."""
    rows: list[tuple[str, str]] = []
    current_id = ""
    current_parts: list[str] = []

    def flush() -> None:
        nonlocal current_id, current_parts
        if current_id and current_parts:
            raw = clean(" ".join(current_parts))
            if raw:
                rows.append((current_id, raw))
        current_id = ""
        current_parts = []

    for line in lines:
        stripped = line.strip()
        if SUBTOTAL_RE.match(stripped):
            flush()
            continue
        match = START_RE.match(stripped)
        if match:
            flush()
            current_id = clean(match.group("id").replace(" ", ""))
            body = match.group("body")
            current_parts = [body] if body else []
        elif current_id:
            current_parts.append(stripped)

    flush()
    return rows


def classify(schedule: str, raw: str) -> str:
    lowered = raw.lower()
    if "fund" in lowered or "lp" in lowered or "llc" in lowered:
        return "fund-partnership-or-private-asset"
    if "mortgage" in lowered or "trust" in lowered:
        return "structured-credit-or-real-estate"
    if "schedule d" in lowered or "bond" in lowered or "note" in lowered:
        return "transferred-or-debt-style-asset"
    if "Schedule BA Part 2" in schedule:
        return "addition-or-acquisition"
    if "Schedule BA Part 3" in schedule:
        return "disposal-transfer-or-repayment"
    return "other-invested-asset"


def main() -> None:
    reader = PdfReader(str(PDF))
    rows: list[dict[str, str]] = []
    controls: list[dict[str, str]] = []
    sequence = 1
    control_sequence = 1

    for schedule, start_page, end_page, population in BA_SPECS:
        for page_no in range(start_page, end_page + 1):
            lines = page_lines(reader, page_no)
            for code, body in extract_control_rows(lines):
                controls.append(
                    {
                        "control_row_id": f"CFAASBAC-{control_sequence:04d}",
                        "schedule": schedule,
                        "page": str(page_no),
                        "control_code": code,
                        "raw_control_text": body[:1200],
                        "numeric_tokens": "; ".join(MONEY_RE.findall(body)),
                        "current_status": "source-visible-control-row",
                        "boundary": "visible statutory Schedule BA subtotal/control row; column meaning requires schedule header and verification-page mapping",
                    }
                )
                control_sequence += 1

            for identifier, raw in extract_ba_rows(lines):
                rows.append(
                    {
                        "parser_row_id": f"CFAASBAFR-{sequence:05d}",
                        "schedule": schedule,
                        "population": population,
                        "page": str(page_no),
                        "cusip_or_identifier": identifier,
                        "name_and_raw_terms": raw[:1400],
                        "naic_designation_detected": (HELPERS.first_naic(raw) or ""),
                        "asset_type_guess": classify(schedule, raw),
                        "first_numeric_values": "; ".join(BA_MONEY_RE.findall(raw)[:16]),
                        "current_status": "full-range-schedule-ba-parser-row-visible",
                        "proof_use": "repeatable named Schedule BA detail row",
                        "boundary": "raw row population; Part 1/2/3 layouts differ, blanks are preserved, and row-level numeric columns are not promoted to cash or return proof",
                    }
                )
                sequence += 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    with CONTROL_OUT.open("w", newline="") as handle:
        fieldnames = list(controls[0]) if controls else ["control_row_id"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(controls)

    part1_totals = [row for row in controls if row["schedule"] == "Schedule BA Part 1" and row["control_code"] == "7099999"]
    print(f"wrote {len(rows)} detail rows to {OUT.relative_to(ROOT)}")
    print(f"wrote {len(controls)} control rows to {CONTROL_OUT.relative_to(ROOT)}")
    if part1_totals:
        print("part1-total-control-rows:")
        for row in part1_totals:
            print(f"  page={row['page']} code={row['control_code']} numeric_tokens={row['numeric_tokens']}")


if __name__ == "__main__":
    main()
