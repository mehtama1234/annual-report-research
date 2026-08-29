#!/usr/bin/env python3
"""Extract URI Yak note holder rows from local HTML holding schedules."""

from __future__ import annotations

import argparse
import csv
import html
import re
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:  # pragma: no cover - fallback keeps the script usable.
    BeautifulSoup = None


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_ROOT = (
    ROOT
    / "raw"
    / "primary-sources"
    / "capital-flow"
    / "united-rentals"
    / "yak-holder"
    / "sec"
)
DEFAULT_OUTPUT = (
    ROOT
    / "analysis"
    / "company-first-principles"
    / "data"
    / "capital-flow-uri-yak-holder-schedule-extractor-pass-1.csv"
)
DEFAULT_GROUPED_OUTPUT = (
    ROOT
    / "analysis"
    / "company-first-principles"
    / "data"
    / "capital-flow-uri-yak-holder-schedule-dedupe-summary-pass-1.csv"
)

FIELDS = [
    "row_id",
    "source_file",
    "source_url",
    "filing_period",
    "filing_date",
    "cik",
    "accession",
    "manager_family",
    "fund_or_vehicle",
    "source_kind",
    "row_index",
    "dedupe_scope",
    "dedupe_key",
    "matched_terms",
    "security_text",
    "cusip",
    "isin",
    "face_or_principal_usd_m",
    "value_usd_m",
    "extraction_status",
    "what_it_says",
    "what_it_does_not_say",
]

GROUPED_FIELDS = [
    "summary_id",
    "dedupe_scope",
    "manager_family",
    "fund_or_vehicle",
    "filing_period",
    "candidate_rows",
    "unique_dedupe_keys",
    "face_or_principal_usd_m_sum",
    "value_usd_m_sum",
    "source_files",
    "source_urls",
    "summary_status",
    "what_it_says",
    "what_it_does_not_say",
]

TARGET_TERMS = (
    "911365BR4",
    "US911365BR47",
    "United Rentals North America",
)

KNOWN_SOURCE_METADATA = {
    "raw/primary-sources/capital-flow/united-rentals/yak-holder/sec/federated-hermes-institutional-high-yield-2025-nport.html": {
        "source_url": "https://www.sec.gov/Archives/edgar/data/925723/000114554925019417/poi_fhinsthighyldbondfd.htm",
        "filing_period": "January 31 2025",
        "filing_date": "2025 source filing",
        "cik": "925723",
        "accession": "000114554925019417",
        "manager_family": "Federated Hermes",
        "fund_or_vehicle": "Federated Hermes Institutional High Yield Bond Fund",
    },
    "raw/primary-sources/capital-flow/united-rentals/yak-holder/sec/venerable-high-yield-2025q1-nport.txt": {
        "source_url": "https://www.sec.gov/Archives/edgar/data/1995745/000175272425116428/0001752724-25-116428.txt",
        "filing_period": "March 31 2025",
        "filing_date": "May 23 2025",
        "cik": "1995745",
        "accession": "000175272425116428",
        "manager_family": "Venerable",
        "fund_or_vehicle": "Venerable High Yield Fund",
    },
    "raw/primary-sources/capital-flow/united-rentals/yak-holder/sec/nport-1982467-primary-doc.xml": {
        "source_url": "https://www.sec.gov/Archives/edgar/data/1982467/000119312526244833/xslFormNPORT-P_X01/primary_doc.xml",
        "filing_period": "March 31 2026",
        "filing_date": "May 28 2026",
        "cik": "1982467",
        "accession": "000119312526244833",
        "manager_family": "Jackson",
        "fund_or_vehicle": "Jackson Credit Opportunities Fund",
    },
    "raw/primary-sources/capital-flow/united-rentals/yak-holder/sec/nport-863520-primary-doc.xml": {
        "source_url": "https://www.sec.gov/Archives/edgar/data/863520/000094040025005171/xslFormNPORT-P_X01/primary_doc.xml",
        "filing_period": "August 29 2025",
        "filing_date": "October 23 2025",
        "cik": "863520",
        "accession": "000094040025005171",
        "manager_family": "Western Asset",
        "fund_or_vehicle": "Western Asset Total Return Unconstrained Fund",
    },
    "raw/primary-sources/capital-flow/united-rentals/yak-holder/sec/nport-917469-2025-06.html": {
        "source_url": "https://www.sec.gov/Archives/edgar/data/917469/000175272425211983/NPORT_4869_97365354_0625.htm",
        "filing_period": "June 30 2025",
        "filing_date": "2025 source filing",
        "cik": "917469",
        "accession": "000175272425211983",
        "manager_family": "Loomis Sayles",
        "fund_or_vehicle": "Loomis Sayles Institutional High Income Fund",
    },
    "raw/primary-sources/capital-flow/united-rentals/yak-holder/sec/venerable-high-yield-2024q4-nport.txt": {
        "source_url": "https://www.sec.gov/Archives/edgar/data/809593/000175272424293276/0001752724-24-293276.txt",
        "filing_period": "October 31 2024",
        "filing_date": "December 26 2024",
        "cik": "809593",
        "accession": "000175272424293276",
        "manager_family": "American Beacon",
        "fund_or_vehicle": "American Beacon NIS Core Plus Bond Fund",
    },
    "raw/primary-sources/capital-flow/united-rentals/yak-holder/sec/calamos-nport-cgw8-2026-03.html": {
        "source_url": "https://www.sec.gov/Archives/edgar/data/1870117/000141036826054719/NPORT_CGW8_77475242_0326.htm",
        "filing_period": "March 31 2026",
        "filing_date": "2026 source filing",
        "cik": "1870117",
        "accession": "000141036826054719",
        "manager_family": "Capital Group",
        "fund_or_vehicle": "Capital Group U.S. Multi-Sector Income ETF",
        "amount_scale": "1000",
    },
    "raw/primary-sources/capital-flow/united-rentals/yak-holder/sec/fidelity-qtly-6541-2025-11.html": {
        "source_url": "https://www.sec.gov/Archives/edgar/data/35315/000003540226000486/QTLY_6541_20251130.htm",
        "filing_period": "November 30 2025",
        "filing_date": "2026 source filing",
        "cik": "35315",
        "accession": "000003540226000486",
        "manager_family": "Fidelity",
        "fund_or_vehicle": "Fidelity Sustainable Core Plus Bond Fund",
    },
    "raw/primary-sources/capital-flow/united-rentals/yak-holder/sec/fidelity-qtly-6540-2025-05.html": {
        "source_url": "https://www.sec.gov/Archives/edgar/data/35315/000175272425176732/QTLY_6540_20250531.htm",
        "filing_period": "May 31 2025",
        "filing_date": "2025 source filing",
        "cik": "35315",
        "accession": "000175272425176732",
        "manager_family": "Fidelity",
        "fund_or_vehicle": "Fidelity SAI Sustainable Core Plus Bond Fund",
    },
}


def clean_text(value: str) -> str:
    return " ".join(value.replace("\xa0", " ").split())


def strip_markup(value: str) -> str:
    return clean_text(html.unescape(re.sub(r"<[^>]+>", " ", value)))


def numeric_value(value: str) -> float | None:
    text = clean_text(value)
    text = text.replace("$", "").replace(",", "").replace(" ", "").replace(" ", "")
    text = text.strip()
    if not text or text in {"-", "—"}:
        return None
    if text.startswith("(") and text.endswith(")"):
        text = "-" + text[1:-1]
    try:
        return float(text)
    except ValueError:
        return None


def looks_like_target(text: str) -> bool:
    lowered = text.lower()
    if "911365br4" in lowered or "us911365br47" in lowered:
        return True
    issuer_visible = (
        "united rentals north america" in lowered
        or "united rentals (north america)" in lowered
    )
    return (
        issuer_visible
        and "6.125" in lowered
        and ("2034" in lowered or "3/15/34" in lowered or "15/03/34" in lowered)
    )


def matched_terms(text: str) -> str:
    terms = []
    for term in TARGET_TERMS:
        if term.lower() in text.lower():
            terms.append(term)
    if "6.125" in text:
        terms.append("6.125%")
    if "2034" in text or "3/15/34" in text or "15/03/34" in text:
        terms.append("2034 maturity")
    return "; ".join(dict.fromkeys(terms))


def source_metadata(path: Path) -> dict[str, str]:
    rel = str(path.relative_to(ROOT))
    metadata = {
        "source_url": "",
        "filing_period": "",
        "filing_date": "",
        "cik": "",
        "accession": "",
        "manager_family": "",
        "fund_or_vehicle": "",
        "amount_scale": "1",
    }
    metadata.update(KNOWN_SOURCE_METADATA.get(rel, {}))
    if not metadata["accession"]:
        match = re.search(r"/Archives/edgar/data/(\d+)/(\d{18})/", path.read_text(errors="ignore")[:2000])
        if match:
            metadata["cik"] = match.group(1)
            metadata["accession"] = match.group(2)
    return metadata


def dedupe_key(metadata: dict[str, str], row_text: str) -> tuple[str, str]:
    security = clean_text(re.sub(r"\b\d{1,3}(?:,\d{3})+\b", "", row_text)).lower()
    security = re.sub(r"[^a-z0-9. /%-]+", " ", security)
    security = clean_text(security)
    scope_parts = [
        metadata.get("manager_family", ""),
        metadata.get("fund_or_vehicle", ""),
        metadata.get("filing_period", ""),
    ]
    scope = "|".join(part for part in scope_parts if part) or "unknown-scope"
    return scope, f"{scope}|{security}"


def base_row(path: Path, row_text: str) -> dict[str, str]:
    metadata = source_metadata(path)
    scope, key = dedupe_key(metadata, row_text)
    return {
        "source_file": str(path.relative_to(ROOT)),
        "source_url": metadata["source_url"],
        "filing_period": metadata["filing_period"],
        "filing_date": metadata["filing_date"],
        "cik": metadata["cik"],
        "accession": metadata["accession"],
        "manager_family": metadata["manager_family"],
        "fund_or_vehicle": metadata["fund_or_vehicle"],
        "dedupe_scope": scope,
        "dedupe_key": key,
    }


def tag_value(block: str, tag: str) -> str:
    match = re.search(fr"<{tag}>(.*?)</{tag}>", block, flags=re.DOTALL | re.IGNORECASE)
    return clean_text(match.group(1)) if match else ""


def isin_value(block: str) -> str:
    match = re.search(r'<isin\s+value="([^"]+)"', block, flags=re.IGNORECASE)
    return match.group(1) if match else ""


def parse_nport_xml_blocks(path: Path) -> list[dict[str, str]]:
    text = path.read_text(errors="ignore")
    rows = []
    for index, match in enumerate(re.finditer(r"<invstOrSec>(.*?)</invstOrSec>", text, flags=re.DOTALL | re.IGNORECASE), start=1):
        block = match.group(1)
        block_text = clean_text(re.sub(r"<[^>]+>", " ", block))
        if not looks_like_target(block):
            continue
        balance = numeric_value(tag_value(block, "balance"))
        value = numeric_value(tag_value(block, "valUSD"))
        title = tag_value(block, "title")
        coupon = tag_value(block, "annualizedRt")
        maturity = tag_value(block, "maturityDt")
        row_text = clean_text(" | ".join(part for part in [title or tag_value(block, "name"), coupon, maturity, block_text] if part))
        output_row = base_row(path, row_text)
        output_row.update(
            {
                "source_kind": "nport-xml-investment-block",
                "row_index": str(index),
                "matched_terms": matched_terms(block),
                "security_text": row_text,
                "cusip": tag_value(block, "cusip"),
                "isin": isin_value(block),
                "face_or_principal_usd_m": f"{balance / 1_000_000:.6f}" if balance is not None else "",
                "value_usd_m": f"{value / 1_000_000:.6f}" if value is not None else "",
                "extraction_status": "candidate-nport-xml-row-with-dedupe-metadata-visible",
                "what_it_says": "A local N-PORT XML investment block matches the URI Yak note identifiers and carries balance/value fields.",
                "what_it_does_not_say": "This does not prove original issuance allocation, unique holder exposure, transaction date, or full holder base.",
            }
        )
        rows.append(output_row)
    return rows


def first_labeled_number(text: str, label: str) -> float | None:
    if label.lower() == "value":
        match = re.search(
            r"\bValue\.\s+Report values.*?([0-9][0-9,]*(?:\.[0-9]+)?)",
            text,
            flags=re.IGNORECASE,
        )
        if match:
            return numeric_value(match.group(1))
    match = re.search(fr"\b{re.escape(label)}\b\s+([0-9][0-9,]*(?:\.[0-9]+)?)", text, flags=re.IGNORECASE)
    return numeric_value(match.group(1)) if match else None


def parse_rendered_nport_windows(path: Path) -> list[dict[str, str]]:
    text = path.read_text(errors="ignore")
    rows = []
    seen_windows: set[tuple[str, str, str]] = set()
    for index, match in enumerate(re.finditer(r"911365BR4|US911365BR47", text, flags=re.IGNORECASE), start=1):
        start = max(0, match.start() - 2500)
        end = min(len(text), match.end() + 5500)
        window = text[start:end]
        window_text = strip_markup(window)
        if not looks_like_target(window_text):
            continue
        balance = first_labeled_number(window_text, "Balance")
        value = first_labeled_number(window_text, "Value")
        key = (path.name, f"{balance}", f"{value}")
        if key in seen_windows:
            continue
        seen_windows.add(key)
        row_text = clean_text(window_text[:1000])
        output_row = base_row(path, row_text)
        output_row.update(
            {
                "source_kind": "rendered-nport-investment-window",
                "row_index": str(index),
                "matched_terms": matched_terms(window_text),
                "security_text": row_text,
                "cusip": "911365BR4",
                "isin": "US911365BR47" if "US911365BR47" in window_text else "",
                "face_or_principal_usd_m": f"{balance / 1_000_000:.6f}" if balance is not None else "",
                "value_usd_m": f"{value / 1_000_000:.6f}" if value is not None else "",
                "extraction_status": "candidate-rendered-nport-window-with-dedupe-metadata-visible",
                "what_it_says": "A local rendered N-PORT investment window matches the URI Yak note identifiers and carries balance/value fields.",
                "what_it_does_not_say": "This does not prove original issuance allocation, unique holder exposure, transaction date, or full holder base.",
            }
        )
        rows.append(output_row)
    return rows


def parse_target_html_row_fragments(path: Path) -> list[dict[str, str]]:
    text = path.read_text(errors="ignore")
    metadata = source_metadata(path)
    amount_scale = float(metadata.get("amount_scale", "1"))
    rows = []
    for row_number, match in enumerate(re.finditer(r"<tr\b[^>]*>.*?</tr>", text, flags=re.DOTALL | re.IGNORECASE), start=1):
        fragment = match.group(0)
        row_text = strip_markup(fragment)
        if not looks_like_target(row_text):
            continue
        numbers = [numeric_value(number) for number in re.findall(r"(?<![A-Za-z])\$?\(?[0-9][0-9,]*(?:\.[0-9]+)?\)?", row_text)]
        numbers = [number for number in numbers if number is not None and number > 1000 and number != 2034]
        face = numbers[0] / 1_000_000 if numbers else None
        value = numbers[-1] / 1_000_000 if len(numbers) >= 2 else None
        if face is not None:
            face *= amount_scale
        if value is not None:
            value *= amount_scale
        output_row = base_row(path, row_text)
        output_row.update(
            {
                "source_kind": "html-table-row-fragment",
                "row_index": str(row_number),
                "matched_terms": matched_terms(row_text),
                "security_text": row_text,
                "cusip": "911365BR4" if "911365BR4" in row_text else "",
                "isin": "US911365BR47" if "US911365BR47" in row_text else "",
                "face_or_principal_usd_m": f"{face:.6f}" if face is not None else "",
                "value_usd_m": f"{value:.6f}" if value is not None else "",
                "extraction_status": "candidate-holder-row-fragment-with-dedupe-metadata-visible",
                "what_it_says": "A local HTML schedule row fragment matches the URI Yak note and carries source metadata plus a dedupe key.",
                "what_it_does_not_say": "This does not prove original issuance allocation, unique holder exposure, transaction date, or full holder base.",
            }
        )
        rows.append(output_row)
    return rows


def parse_html_tables(path: Path) -> list[dict[str, str]]:
    if BeautifulSoup is None:
        return []
    soup = BeautifulSoup(path.read_text(errors="ignore"), "html.parser")
    rows = []
    row_number = 0
    for table in soup.find_all("table"):
        for tr in table.find_all("tr"):
            cells = [clean_text(cell.get_text(" ", strip=True)) for cell in tr.find_all(["td", "th"])]
            cells = [cell for cell in cells if cell]
            if not cells:
                continue
            row_number += 1
            row_text = " | ".join(cells)
            if not looks_like_target(row_text):
                continue
            numbers = [numeric_value(cell) for cell in cells]
            numbers = [number for number in numbers if number is not None]
            face = numbers[0] / 1_000_000 if numbers else None
            value = numbers[-1] / 1_000_000 if len(numbers) >= 2 else None
            output_row = base_row(path, row_text)
            output_row.update(
                {
                    "source_kind": "html-table-row",
                    "row_index": str(row_number),
                    "matched_terms": matched_terms(row_text),
                    "security_text": row_text,
                    "cusip": "911365BR4" if "911365BR4" in row_text else "",
                    "isin": "US911365BR47" if "US911365BR47" in row_text else "",
                    "face_or_principal_usd_m": f"{face:.6f}" if face is not None else "",
                    "value_usd_m": f"{value:.6f}" if value is not None else "",
                    "extraction_status": "candidate-holder-row-with-dedupe-metadata-visible",
                    "what_it_says": "A local HTML schedule row matches the URI Yak note and now carries source metadata plus a dedupe key.",
                    "what_it_does_not_say": "This does not prove original issuance allocation, unique holder exposure, transaction date, or full holder base.",
                }
            )
            rows.append(
                output_row
            )
    return rows


def parse_plain_text(path: Path) -> list[dict[str, str]]:
    text = path.read_text(errors="ignore")
    lines = [clean_text(line) for line in text.splitlines()]
    rows = []
    for index, line in enumerate(lines, start=1):
        if not line or not looks_like_target(line):
            continue
        output_row = base_row(path, line)
        output_row.update(
            {
                "source_kind": "html-text-line",
                "row_index": str(index),
                "matched_terms": matched_terms(line),
                "security_text": line,
                "cusip": "911365BR4" if "911365BR4" in line else "",
                "isin": "US911365BR47" if "US911365BR47" in line else "",
                "face_or_principal_usd_m": "",
                "value_usd_m": "",
                "extraction_status": "candidate-text-line-with-dedupe-metadata-visible",
                "what_it_says": "A local text line matches the URI Yak note and now carries source metadata plus a dedupe key.",
                "what_it_does_not_say": "This is locator evidence only until table context is parsed.",
            }
        )
        rows.append(
            output_row
        )
    return rows


def iter_sources(paths: list[Path], source_root: Path) -> list[Path]:
    if paths:
        return paths
    return sorted([*source_root.glob("**/*.htm*"), *source_root.glob("**/*.xml"), *source_root.glob("**/*.txt")])


def parse_float(value: str) -> float:
    if not value:
        return 0.0
    try:
        return float(value)
    except ValueError:
        return 0.0


def summarize_by_dedupe_scope(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["dedupe_scope"], []).append(row)

    summaries: list[dict[str, str]] = []
    for index, (scope, group_rows) in enumerate(sorted(grouped.items()), start=1):
        first = group_rows[0]
        face_sum = sum(parse_float(row["face_or_principal_usd_m"]) for row in group_rows)
        value_sum = sum(parse_float(row["value_usd_m"]) for row in group_rows)
        summaries.append(
            {
                "summary_id": f"URIYHSS-001-{index:03d}",
                "dedupe_scope": scope,
                "manager_family": first["manager_family"],
                "fund_or_vehicle": first["fund_or_vehicle"],
                "filing_period": first["filing_period"],
                "candidate_rows": str(len(group_rows)),
                "unique_dedupe_keys": str(len({row["dedupe_key"] for row in group_rows})),
                "face_or_principal_usd_m_sum": f"{face_sum:.6f}" if face_sum else "",
                "value_usd_m_sum": f"{value_sum:.6f}" if value_sum else "",
                "source_files": "; ".join(sorted({row["source_file"] for row in group_rows})),
                "source_urls": "; ".join(sorted({row["source_url"] for row in group_rows if row["source_url"]})),
                "summary_status": "dedupe-scope-summary-visible",
                "what_it_says": "Rows are grouped by manager family, fund or vehicle, and filing period before any broader holder total is promoted.",
                "what_it_does_not_say": "This grouped summary is still not a full holder base, not manager-family deduped across periods, and not original issuance allocation.",
            }
        )
    return summaries


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE_ROOT)
    parser.add_argument("--source", type=Path, action="append", default=[])
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--grouped-output", type=Path, default=DEFAULT_GROUPED_OUTPUT)
    args = parser.parse_args()

    extracted: list[dict[str, str]] = []
    for source in iter_sources(args.source, args.source_root):
        path = source if source.is_absolute() else ROOT / source
        if not path.exists() or path.suffix.lower() not in {".html", ".htm", ".xml", ".txt"}:
            continue
        xml_rows = parse_nport_xml_blocks(path)
        if xml_rows:
            extracted.extend(xml_rows)
            continue
        rendered_rows = parse_rendered_nport_windows(path)
        if rendered_rows:
            extracted.extend(rendered_rows)
            continue
        fragment_rows = parse_target_html_row_fragments(path)
        if fragment_rows:
            extracted.extend(fragment_rows)
            continue
        table_rows = parse_html_tables(path)
        if table_rows:
            extracted.extend(table_rows)
        else:
            extracted.extend(parse_plain_text(path))

    for index, row in enumerate(extracted, start=1):
        row["row_id"] = f"URIYHSE-001-{index:03d}"

    grouped = summarize_by_dedupe_scope(extracted)
    write_csv(args.output, FIELDS, extracted)
    write_csv(args.grouped_output, GROUPED_FIELDS, grouped)

    print(f"wrote {len(extracted)} rows to {display_path(args.output)}")
    print(f"wrote {len(grouped)} grouped rows to {display_path(args.grouped_output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
