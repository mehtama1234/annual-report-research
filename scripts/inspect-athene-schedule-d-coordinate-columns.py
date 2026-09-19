#!/usr/bin/env python3
"""Capture native PDF coordinates for Schedule D numeric columns."""

from __future__ import annotations

import csv
import re
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "raw/primary-sources/capital-flow/apollo/athene/statutory/2025/athene-annuity-and-life-company-2025-statutory-statement.pdf"
OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-coordinate-column-diagnostic-2026-09-15.csv"
PAGES = (5969, 5970, 5971, 5972, 6276, 6312)
CUSIP_RE = re.compile(r"^[A-Z0-9@#*]{6}-[A-Z0-9]{2}-[A-Z0-9]$")
NUMERIC_RE = re.compile(r"^\(?\d[\d,]*(?:\.\d+)?\)?$")


def capture_page(reader: PdfReader, page_number: int) -> list[dict[str, str]]:
    chunks: list[tuple[str, float, float]] = []

    def visitor(text, _cm, tm, _font, _size):
        value = text.strip()
        if value:
            chunks.append((value, round(float(tm[4]), 3), round(float(tm[5]), 3)))

    reader.pages[page_number - 1].extract_text(visitor_text=visitor)
    row_ys = sorted({y for text, _x, y in chunks if CUSIP_RE.fullmatch(text)})
    output: list[dict[str, str]] = []
    for row_y in row_ys:
        row_chunks = [(text, x) for text, x, y in chunks if abs(y - row_y) < 0.2]
        cusip = next(text for text, _x in row_chunks if CUSIP_RE.fullmatch(text))
        numeric = [(text, x) for text, x in row_chunks if NUMERIC_RE.fullmatch(text.replace(" ", ""))]
        for ordinal, (text, x) in enumerate(numeric, start=1):
            output.append(
                {
                    "page": str(page_number),
                    "row_y": f"{row_y:.3f}",
                    "cusip": cusip,
                    "numeric_ordinal_on_row": str(ordinal),
                    "numeric_text": text,
                    "x_start": f"{x:.3f}",
                    "diagnostic_boundary": "native PDF coordinate evidence; not yet assigned to accounting columns",
                }
            )
    return output


def main() -> None:
    reader = PdfReader(str(PDF))
    rows = [row for page in PAGES for row in capture_page(reader, page)]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} coordinate tokens to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
