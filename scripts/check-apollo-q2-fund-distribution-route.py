#!/usr/bin/env python3
"""Check the two Apollo Q2 2026 10-Q distribution observations used by APO-104."""

from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "raw/primary-sources/capital-flow/apollo/q2-2026/apollo-2026-q2-10q.pdf"


def main() -> int:
    reader = PdfReader(str(SOURCE))
    found_fund_distribution = False
    found_broad_investing_line = False
    rollforward_page = None
    investing_page = None
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if "Fund distributions to the Company" in text and "3,230" in text:
            found_fund_distribution = True
            rollforward_page = page_number
        if "Investment funds and distributions from equity method investments" in text and "2,040" in text:
            found_broad_investing_line = True
            investing_page = page_number
    if not found_fund_distribution:
        raise SystemExit("FAIL: Q2 10-Q fund-distributions-to-the-Company rollforward not found")
    if not found_broad_investing_line:
        raise SystemExit("FAIL: Q2 10-Q broader $2,040M investing line not found")
    print(
        "Apollo Q2 fund-distribution route passed: "
        f"$799M rollforward on PDF page {rollforward_page}; "
        f"$2,040M broader investing line on PDF page {investing_page}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
