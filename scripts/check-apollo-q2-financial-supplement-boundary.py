#!/usr/bin/env python3
"""Reproduce the Apollo Q2 financial-supplement search boundary."""

from __future__ import annotations

import re
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
WORKBOOK = ROOT / "raw" / "primary-sources" / "capital-flow" / "apollo" / "q2-2026" / "apollo-q2-2026-financial-supplement.xlsx"
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
SEARCH = re.compile(r"dividend|cash|subsidiar|distribution|intercompany|parent", re.I)
FORBIDDEN_RECEIPT = re.compile(r"athene.{0,40}agm|receiving account|intercompany settlement|subsidiary distribution", re.I)


def shared_strings(book: zipfile.ZipFile) -> list[str]:
    root = ET.fromstring(book.read("xl/sharedStrings.xml"))
    return ["".join(node.itertext()) for node in root]


def main() -> int:
    if not WORKBOOK.is_file():
        raise SystemExit(f"FAIL: missing {WORKBOOK.relative_to(ROOT)}")
    with zipfile.ZipFile(WORKBOOK) as book:
        sheets = sorted(name for name in book.namelist() if name.startswith("xl/worksheets/sheet") and name.endswith(".xml"))
        if len(sheets) != 8:
            raise SystemExit(f"FAIL: expected 8 worksheets, found {len(sheets)}")
        strings = shared_strings(book)
        matches: list[str] = []
        forbidden: list[str] = []
        for name in sheets:
            root = ET.fromstring(book.read(name))
            for row in root.findall(".//m:row", NS):
                values: list[str] = []
                for cell in row.findall("m:c", NS):
                    value = cell.find("m:v", NS)
                    text = "" if value is None else (value.text or "")
                    if cell.get("t") == "s" and text:
                        text = strings[int(text)]
                    values.append(text)
                line = " | ".join(values)
                if SEARCH.search(line):
                    matches.append(f"{name}:{line}")
                if FORBIDDEN_RECEIPT.search(line):
                    forbidden.append(f"{name}:{line}")
    if forbidden:
        raise SystemExit(f"FAIL: unexpected parent-receipt candidate rows: {forbidden}")
    required = ("Preferred stock dividends", "Unvested RSUs Eligible for Dividend Equivalents", "Dedicated Investment Program")
    joined = "\n".join(matches)
    missing = [term for term in required if term not in joined]
    if missing:
        raise SystemExit(f"FAIL: expected supplement fields missing: {missing}")
    print(f"Apollo Q2 financial-supplement boundary passed: {len(sheets)} worksheets, {len(matches)} matched rows, 0 separately tagged parent-receipt rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
