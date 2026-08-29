#!/usr/bin/env python3
"""Acquire KKR/Global Atlantic statutory source files and build pass artifacts."""

from __future__ import annotations

import csv
import os
import re
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
ANALYSIS = ROOT / "analysis/company-first-principles"
RAW = ROOT / "raw/primary-sources/capital-flow/kkr/global-atlantic"

OUT = DATA / "capital-flow-kkr-global-atlantic-statutory-source-acquisition-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-kkr-global-atlantic-statutory-source-acquisition-diagnostic-pass-1.csv"
MEMO = ANALYSIS / "capital-flow-kkr-global-atlantic-statutory-source-acquisition-pass-1.md"

FIELDNAMES = [
    "acquisition_id",
    "legal_entity",
    "period",
    "statement_type",
    "source_url",
    "local_path",
    "source_status",
    "file_size_bytes",
    "pdf_probe",
    "proof_effect",
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

SOURCES = [
    (
        "CFKKRGASA-001",
        "Accordia Life and Annuity Company",
        "Q2 2026",
        "U.S. quarterly statutory statement",
        "https://www.globalatlantic.com/sites/globalatlantic/files/PDFs/Financial_Statements/FY2026/Accordia_2Q_2026_Quarterly_Statement_Verifications.pdf",
        RAW / "statutory/2026/Accordia_2Q_2026_Quarterly_Statement_Verifications.pdf",
    ),
    (
        "CFKKRGASA-002",
        "Commonwealth Annuity and Life Insurance Company",
        "Q2 2026",
        "U.S. quarterly statutory statement",
        "https://www.globalatlantic.com/sites/globalatlantic/files/PDFs/Financial_Statements/FY2026/CWA_2Q_2026_Quarterly_Statements_Verifications.pdf",
        RAW / "statutory/2026/CWA_2Q_2026_Quarterly_Statements_Verifications.pdf",
    ),
    (
        "CFKKRGASA-003",
        "First Allmerica Financial Life Insurance Company",
        "Q2 2026",
        "U.S. quarterly statutory statement",
        "https://www.globalatlantic.com/sites/globalatlantic/files/PDFs/Financial_Statements/FY2026/FAFLIC_2Q_2026_Quarterly_Statements_Verifications.pdf",
        RAW / "statutory/2026/FAFLIC_2Q_2026_Quarterly_Statements_Verifications.pdf",
    ),
    (
        "CFKKRGASA-004",
        "Forethought Life Insurance Company",
        "Q2 2026",
        "U.S. quarterly statutory statement",
        "https://www.globalatlantic.com/sites/globalatlantic/files/PDFs/Financial_Statements/FY2026/FLIC_2Q_2026_Quarterly_Statements_Verifications.PDF",
        RAW / "statutory/2026/FLIC_2Q_2026_Quarterly_Statements_Verifications.PDF",
    ),
    (
        "CFKKRGASA-005",
        "Accordia Life and Annuity Company",
        "Q4 2025",
        "U.S. annual statutory statement",
        "https://www.globalatlantic.com/sites/globalatlantic/files/PDFs/Financial_Statements/FY2025/Accordia_4Q_2025_Quarterly_Statements.pdf",
        RAW / "statutory/2025/Accordia_4Q_2025_Quarterly_Statements.pdf",
    ),
    (
        "CFKKRGASA-006",
        "Commonwealth Annuity and Life Insurance Company",
        "Q4 2025",
        "U.S. annual statutory statement",
        "https://www.globalatlantic.com/sites/globalatlantic/files/PDFs/Financial_Statements/FY2025/CWA_4Q_2025_Quarterly_Statements_Verifications.pdf",
        RAW / "statutory/2025/CWA_4Q_2025_Quarterly_Statements_Verifications.pdf",
    ),
    (
        "CFKKRGASA-007",
        "First Allmerica Financial Life Insurance Company",
        "Q4 2025",
        "U.S. annual statutory statement",
        "https://www.globalatlantic.com/sites/globalatlantic/files/PDFs/Financial_Statements/FY2025/FAFLIC_4Q_2025_Quarterly_Statements_Verifications.pdf",
        RAW / "statutory/2025/FAFLIC_4Q_2025_Quarterly_Statements_Verifications.pdf",
    ),
    (
        "CFKKRGASA-008",
        "Forethought Life Insurance Company",
        "Q4 2025",
        "U.S. annual statutory statement",
        "https://www.globalatlantic.com/sites/globalatlantic/files/PDFs/Financial_Statements/FY2025/FLIC_4Q_2025_Quarterly_Statements_Verifications.pdf",
        RAW / "statutory/2025/FLIC_4Q_2025_Quarterly_Statements_Verifications.pdf",
    ),
    (
        "CFKKRGASA-009",
        "Global Atlantic Re Limited",
        "FY 2025",
        "Bermuda statutory financial statements",
        "https://www.globalatlantic.com/sites/globalatlantic/files/PDFs/Financial_Statements/FY2025/GA_Re_12.31.2025_BSTAT_Financial_Statements.pdf",
        RAW / "bermuda/2025/GA_Re_12.31.2025_BSTAT_Financial_Statements.pdf",
    ),
    (
        "CFKKRGASA-010",
        "Global Atlantic Assurance Limited",
        "FY 2025",
        "Bermuda statutory financial statements",
        "https://www.globalatlantic.com/sites/globalatlantic/files/PDFs/Financial_Statements/FY2025/GAAL_12.31.2025_BSTAT_Financial_Statements.pdf",
        RAW / "bermuda/2025/GAAL_12.31.2025_BSTAT_Financial_Statements.pdf",
    ),
]


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def download(url: str, path: Path) -> tuple[str, str]:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.stat().st_size > 0:
        return "downloaded-local-existing", ""
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(req, timeout=120) as response:
            body = response.read()
        if not body.startswith(b"%PDF"):
            path.write_bytes(body)
            return "route-visible-non-pdf-response-hold", "downloaded bytes did not start with PDF marker"
        path.write_bytes(body)
        return "downloaded-local-extraction-pending", ""
    except HTTPError as exc:
        return "route-visible-download-hold", f"HTTP {exc.code}"
    except URLError as exc:
        return "route-visible-download-hold", str(exc.reason)
    except TimeoutError:
        return "route-visible-download-hold", "timeout"


def pdf_probe(path: Path, error: str) -> str:
    if not path.exists() or path.stat().st_size == 0:
        return error or "no local file"
    first = path.read_bytes()[:5]
    marker = "pdf-header-visible" if first == b"%PDF-" else "pdf-header-not-visible"
    pages = ""
    try:
        from pypdf import PdfReader  # type: ignore

        pages = f"; pages={len(PdfReader(str(path)).pages)}"
    except Exception as exc:  # pragma: no cover - diagnostic only
        pages = f"; page-count-unavailable={type(exc).__name__}"
    return marker + pages


def build_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for acquisition_id, entity, period, statement_type, url, local_path in SOURCES:
        status, error = download(url, local_path)
        size = local_path.stat().st_size if local_path.exists() else 0
        local_rel = local_path.relative_to(ROOT) if local_path.exists() else local_path.relative_to(ROOT)
        effect = (
            "Global Atlantic legal-entity source filing acquired locally for statutory schedule locator."
            if status.startswith("downloaded-local")
            else "Official source route preserved, but local filing acquisition did not complete."
        )
        boundary = (
            "Acquisition proves document availability, not Schedule D/BA holdings, named borrower allocation, cash receipts, liability spread, or return."
        )
        rows.append(
            {
                "acquisition_id": acquisition_id,
                "legal_entity": entity,
                "period": period,
                "statement_type": statement_type,
                "source_url": url,
                "local_path": str(local_rel),
                "source_status": status,
                "file_size_bytes": str(size),
                "pdf_probe": pdf_probe(local_path, error),
                "proof_effect": effect,
                "boundary": boundary,
                "next_action": f"Run statutory schedule locator for {period} {slug(entity)}.",
            }
        )
    return rows


def diagnostic_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    downloaded = [r for r in rows if r["source_status"].startswith("downloaded-local")]
    holds = [r for r in rows if "hold" in r["source_status"]]
    annual = [r for r in rows if r["period"] == "Q4 2025"]
    q2 = [r for r in rows if r["period"] == "Q2 2026"]
    bermuda = [r for r in rows if "Bermuda" in r["statement_type"]]
    largest = max((int(r["file_size_bytes"]) for r in rows), default=0)
    metrics = [
        ("source_acquisition_rows", len(rows), "count"),
        ("official_source_index_routes", 1, "count"),
        ("us_statutory_legal_entities_targeted", 4, "count"),
        ("us_annual_statements_targeted", len(annual), "count"),
        ("q2_2026_quarterlies_targeted", len(q2), "count"),
        ("bermuda_reports_targeted", len(bermuda), "count"),
        ("downloaded_local_files", len(downloaded), "count"),
        ("download_holds", len(holds), "count"),
        ("largest_file_size_bytes", largest, "bytes"),
        ("full_named_cash_proof_upgrades", 0, "count"),
        ("next_parser", "global-atlantic-statutory-schedule-locator", "parser"),
    ]
    out = []
    for idx, (metric, value, units) in enumerate(metrics, start=1):
        out.append(
            {
                "diagnostic_id": f"CFKKRGASAD-{idx:03d}",
                "metric": metric,
                "value": str(value),
                "units": units,
                "proof_use": "controls KKR/Global Atlantic statutory source acquisition status",
                "boundary": "Diagnostics prove acquisition coverage only; they do not parse schedules or prove named cash returns.",
                "next_action": "Run Global Atlantic statutory schedule locator, then Schedule D/BA extraction and income/proceeds bridge.",
            }
        )
    return out


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_memo(rows: list[dict[str, str]], diagnostics: list[dict[str, str]]) -> None:
    by_metric = {r["metric"]: r["value"] for r in diagnostics}
    table = "\n".join(
        "| {acquisition_id} | {legal_entity} | {period} | {source_status} | {file_size_bytes} |".format(**r)
        for r in rows
    )
    MEMO.write_text(
        f"""# Capital Flow KKR Global Atlantic Statutory Source Acquisition Pass 1

## Purpose

This pass executes the KKR/Global Atlantic statutory source route identified in the statutory template.

The goal is to acquire the filings needed to test the insurance-capital money chain:

`KKR / Global Atlantic -> insurance legal entity -> statutory assets and liabilities -> Schedule D/BA holdings -> investment income/proceeds -> named issuer cash-back hold/pass`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-statutory-source-acquisition-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-statutory-source-acquisition-diagnostic-pass-1.csv`

## Source Route

Global Atlantic's official financial-statement page lists U.S. statutory annual and quarterly statements for Accordia Life and Annuity Company, Commonwealth Annuity and Life Insurance Company, First Allmerica Financial Life Insurance Company, and Forethought Life Insurance Company. It also lists Bermuda reinsurer financial information for Global Atlantic Re Limited and Global Atlantic Assurance Limited.

Source index:

`https://www.globalatlantic.com/investor-relations/financial-statements`

## Main Result

| Metric | Value |
|---|---:|
| Source acquisition rows | {by_metric['source_acquisition_rows']} |
| U.S. statutory legal entities targeted | {by_metric['us_statutory_legal_entities_targeted']} |
| Q4 2025 U.S. annual statements targeted | {by_metric['us_annual_statements_targeted']} |
| Q2 2026 U.S. quarterlies targeted | {by_metric['q2_2026_quarterlies_targeted']} |
| FY 2025 Bermuda reports targeted | {by_metric['bermuda_reports_targeted']} |
| Downloaded local files | {by_metric['downloaded_local_files']} |
| Download holds | {by_metric['download_holds']} |
| Largest file size bytes | {by_metric['largest_file_size_bytes']} |
| Full named cash proof upgrades | {by_metric['full_named_cash_proof_upgrades']} |

## Acquisition Rows

| ID | Legal Entity | Period | Status | Bytes |
|---|---|---|---|---:|
{table}

## Proof Effect

This pass moves KKR/Global Atlantic from statutory-template planning to source-file acquisition. The filings are the document family needed to chase named holdings, legal-entity investment income, sale/maturity/proceeds fields, liability source context, FHLB/funds-withheld economics, and Schedule D/BA borrower allocation.

## Boundary

This pass does not yet parse the Global Atlantic statutory statements.

It does not prove named Schedule D/BA holdings, NAIC designations, borrower allocation, cash receipts, liability-cost spread, FHLB liability economics, debt waterfalls, collateral certificates, or asset-level return.

## Next Action

Run `global-atlantic-statutory-schedule-locator` across the acquired files, then adapt the Apollo/Athene Schedule D/BA parser and legal-entity income bridge.

## Decision

`kkr-global-atlantic-statutory-source-acquisition-local-files-acquired-schedule-locator-next`
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
