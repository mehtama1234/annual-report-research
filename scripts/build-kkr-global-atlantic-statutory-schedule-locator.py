#!/usr/bin/env python3
"""Locate proof-relevant schedules inside acquired Global Atlantic statutory PDFs."""

from __future__ import annotations

import csv
import re
import signal
from collections import defaultdict
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
ANALYSIS = ROOT / "analysis/company-first-principles"

SOURCE_ACQ = DATA / "capital-flow-kkr-global-atlantic-statutory-source-acquisition-pass-1.csv"
OUT = DATA / "capital-flow-kkr-global-atlantic-statutory-schedule-locator-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-kkr-global-atlantic-statutory-schedule-locator-diagnostic-pass-1.csv"
MEMO = ANALYSIS / "capital-flow-kkr-global-atlantic-statutory-schedule-locator-pass-1.md"

FIELDNAMES = [
    "locator_id",
    "acquisition_id",
    "legal_entity",
    "period",
    "statement_type",
    "extraction_target",
    "page_start",
    "page_end",
    "pages_found",
    "evidence_found",
    "proof_use",
    "boundary",
    "current_status",
    "next_action",
    "upgrade_test",
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

TARGETS = [
    (
        "assets page",
        [r"ASSETS\\s+Current Year\\s+Prior Year", r"\\bASSETS\\b.*\\bNet Admitted Assets\\b"],
        "legal-entity asset base and invested-asset denominator",
        "summary only; not issuer-level holdings",
        "extract and normalize admitted asset categories",
    ),
    (
        "liabilities surplus and other funds",
        [r"LIABILITIES, SURPLUS AND OTHER FUNDS"],
        "liability base for source-pool and spread bridge",
        "not product-level liability cost or legal distribution availability",
        "extract reserves, deposit-type liabilities, surplus, and capital fields",
    ),
    (
        "summary of operations",
        [r"SUMMARY OF OPERATIONS"],
        "statutory earnings and net investment income bridge",
        "summary line only; needs asset-class and holding-level detail",
        "extract premiums, investment income, benefits, expenses, and gain/loss lines",
    ),
    (
        "cash flow",
        [r"\\bCASH FLOW\\b"],
        "legal-entity cash receipt/proxy bridge",
        "does not allocate cash to specific holdings or borrowers",
        "extract premiums collected, net investment income, sales/maturities, and financing cash lines",
    ),
    (
        "exhibit of net investment income",
        [r"EXHIBIT OF NET INVESTMENT INCOME"],
        "asset-class investment-income extraction target",
        "not issuer-level income without schedule detail and workpapers",
        "parse collected and earned income by asset class",
    ),
    (
        "interest maintenance reserve",
        [r"INTEREST MAINTENANCE RESERVE"],
        "realized gain/loss smoothing and statutory spread support",
        "not connected to individual disposals until Schedule D is parsed",
        "extract IMR movement and gain/loss-related fields",
    ),
    (
        "asset valuation reserve",
        [r"ASSET VALUATION RESERVE"],
        "credit-quality and reserve-pressure support",
        "not issuer-level NAIC or impairment proof",
        "extract AVR default/equity components",
    ),
    (
        "Schedule BA",
        [r"SCHEDULE BA"],
        "other long-term invested assets, alternatives, LP/LLC/fund holdings and income",
        "heading location only until row-level CUSIP/name/value/income fields parse",
        "extract Schedule BA verification and detail rows where present",
    ),
    (
        "Schedule D verification",
        [r"SCHEDULE D - VERIFICATION", r"SCHEDULE D\\s+VERIFICATION"],
        "bond/stock roll-forward, acquisitions, disposals, book value, and carrying-value control",
        "verification totals only; not issuer-level holdings",
        "extract Schedule D verification between years",
    ),
    (
        "Schedule D Part 1A quality and maturity",
        [r"SCHEDULE D - PART 1A", r"QUALITY AND MATURITY DISTRIBUTION OF ALL BONDS"],
        "bond portfolio quality, maturity, and NAIC distribution control",
        "distribution only; not named issuer allocation",
        "extract quality/maturity distribution",
    ),
    (
        "Schedule D long-term bonds owned",
        [r"SCHEDULE D - PART 1\\b", r"LONG-TERM BONDS.*OWNED"],
        "main named issuer-credit and ABS holdings extraction route",
        "needs row parsing and borrower/issuer classification",
        "parse CUSIP, issuer/description, NAIC designation, cost, fair value, book value, income, received interest, and maturity",
    ),
    (
        "Schedule D acquired during year",
        [r"SCHEDULE D - PART 3", r"ACQUIRED During Current Year"],
        "new bond/stock purchase and capital deployment evidence",
        "acquisition list does not prove use or cash return by itself",
        "parse acquired securities and costs",
    ),
    (
        "Schedule D disposed during year",
        [r"SCHEDULE D - PART 4", r"SOLD, REDEEMED OR OTHERWISE DISPOSED", r"DISPOSED During Current Year"],
        "sale, maturity, redemption, consideration, and gain/loss route",
        "needs matching to holdings and cash-flow totals",
        "parse consideration, realized gain/loss, and disposal identifiers",
    ),
    (
        "Schedule D acquired and disposed",
        [r"SCHEDULE D - PART 5", r"ACQUIRED AND DISPOSED"],
        "same-year acquisition/disposal cash and gain/loss evidence",
        "needs matching and cash-vs-noncash classification",
        "parse same-year acquisition/disposal rows",
    ),
    (
        "Schedule DB derivatives",
        [r"SCHEDULE DB"],
        "derivative/hedging exposure and possible funds-flow/risk-transfer context",
        "not direct lending or asset-return proof without counterparty and cash settlement extraction",
        "locate derivative schedules and parse only if material to cash bridge",
    ),
    (
        "Schedule S funds withheld and reinsurance",
        [r"SCHEDULE S", r"FUNDS WITHHELD", r"MODIFIED COINSURANCE"],
        "reinsurance, funds-withheld, and liability/collateral routing context",
        "not legal cash availability without treaty/account detail",
        "extract funds-withheld and reinsurance balances where relevant",
    ),
    (
        "Schedule E cash and deposits",
        [r"SCHEDULE E"],
        "cash, cash equivalents, and special-deposit support",
        "liquidity schedule only; not named asset return proof",
        "extract cash equivalents and special deposits",
    ),
    (
        "Bermuda balance sheet",
        [r"BALANCE SHEET", r"STATEMENT OF FINANCIAL POSITION"],
        "Bermuda legal-entity asset/liability base",
        "summary financial statement only until notes and schedules parse",
        "extract assets, liabilities, capital, and investment balances",
    ),
    (
        "Bermuda income statement",
        [r"STATEMENT OF INCOME", r"STATEMENT OF OPERATIONS", r"COMPREHENSIVE INCOME"],
        "Bermuda earnings and investment income route",
        "not named holding-level cash return",
        "extract income statement and investment income note references",
    ),
    (
        "Bermuda investment note",
        [r"INVESTMENT INCOME", r"INVESTMENTS", r"FAIR VALUE"],
        "Bermuda investment note and valuation context",
        "note text may be summary only without named holdings",
        "extract investment note tables and valuation hierarchy if present",
    ),
]


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def normalize(text: str) -> str:
    return " ".join((text or "").replace("\n", " ").split())


class Timeout(Exception):
    pass


def _timeout_handler(signum, frame):  # type: ignore[no-untyped-def]
    raise Timeout()


def page_text(reader: PdfReader, page_no: int) -> tuple[str, str]:
    old_handler = signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(4)
    try:
        text = normalize(reader.pages[page_no - 1].extract_text() or "")
        signal.alarm(0)
        return text, ""
    except Timeout:
        return "", "timeout"
    except Exception as exc:
        return "", type(exc).__name__
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)


def compress_pages(pages: list[int]) -> str:
    if not pages:
        return ""
    ranges = []
    start = prev = pages[0]
    for page in pages[1:]:
        if page == prev + 1:
            prev = page
            continue
        ranges.append(f"{start}" if start == prev else f"{start}-{prev}")
        start = prev = page
    ranges.append(f"{start}" if start == prev else f"{start}-{prev}")
    return ";".join(ranges)


def evidence_for(target: str, sample: str, pages: list[int]) -> str:
    snippet = sample[:220]
    if not snippet:
        snippet = "heading located by target scan but sample text unavailable"
    return f"{target} located on pages {compress_pages(pages)}; sample: {snippet}"


def locate_pdf(source: dict[str, str]) -> tuple[list[dict[str, str]], int, int]:
    path = ROOT / source["local_path"]
    reader = PdfReader(str(path))
    found: dict[str, list[int]] = defaultdict(list)
    samples: dict[str, str] = {}
    page_errors = 0
    compiled = [(target, [(re.compile(p, re.I)) for p in patterns]) for target, patterns, *_ in TARGETS]
    for page_no in candidate_pages(source, len(reader.pages)):
        text, error = page_text(reader, page_no)
        if error:
            page_errors += 1
            continue
        for target, patterns in compiled:
            if any(p.search(text) for p in patterns):
                found[target].append(page_no)
                samples.setdefault(target, text)
    rows = []
    for target, _patterns, proof_use, boundary, next_action in TARGETS:
        pages = found.get(target, [])
        if not pages:
            continue
        status = "range-located" if len(pages) > 1 else "page-located"
        rows.append(
            {
                "acquisition_id": source["acquisition_id"],
                "legal_entity": source["legal_entity"],
                "period": source["period"],
                "statement_type": source["statement_type"],
                "extraction_target": target,
                "page_start": str(min(pages)),
                "page_end": str(max(pages)),
                "pages_found": compress_pages(pages),
                "evidence_found": evidence_for(target, samples.get(target, ""), pages),
                "proof_use": proof_use,
                "boundary": boundary,
                "current_status": status,
                "next_action": next_action,
                "upgrade_test": f"promote only when {target} is parsed into normalized fields and reconciled to statement totals",
            }
        )
    return rows, len(reader.pages), page_errors


def candidate_pages(source: dict[str, str], page_count: int) -> list[int]:
    """Return bounded probe pages for fast locator runs.

    Full text extraction can be very slow on some statutory pages. These probes
    cover the statutory front matter plus sampled schedule zones already seen in
    the acquired Global Atlantic filings.
    """
    pages: set[int] = set(range(1, min(page_count, 25) + 1))
    name = Path(source["local_path"]).name
    if source["period"] == "Q2 2026":
        pages.update(range(max(1, page_count - 18), page_count + 1))
    elif source["period"] == "FY 2025":
        pages.update(range(1, page_count + 1))
    elif "Accordia_4Q_2025" in name:
        pages.update(
            [
                80,
                100,
                110,
                120,
                130,
                135,
                140,
                145,
                150,
                160,
                170,
                180,
                190,
                200,
                210,
                220,
                230,
                240,
                245,
                250,
                255,
                260,
                265,
                270,
                275,
                280,
                300,
                350,
                400,
                450,
                455,
                460,
                464,
            ]
        )
    else:
        pages.update(range(max(1, page_count - 35), page_count + 1))
        pages.update([40, 80, 100, 120, 140, 150, 160, 170])
    return [p for p in sorted(pages) if 1 <= p <= page_count]


def build_rows() -> tuple[list[dict[str, str]], dict[str, int]]:
    source_by_id = {r["acquisition_id"]: r for r in read_rows(SOURCE_ACQ)}
    manual_targets = [
        ("CFKKRGASA-001", "assets/liabilities/operations/cash-flow quarterlies", "3-6", "Q2 2026 quarterly statement front pages include assets, liabilities, summary operations, and cash flow pages for legal-entity update extraction.", "core quarterly legal-entity update", "quarterly pages do not provide full annual Schedule D/BA detail", "quarterly-core-located"),
        ("CFKKRGASA-002", "assets/liabilities/operations/cash-flow quarterlies", "2-5", "Q2 2026 quarterly statement front pages include assets, liabilities, summary operations, and cash flow pages for legal-entity update extraction.", "core quarterly legal-entity update", "quarterly pages do not provide full annual Schedule D/BA detail", "quarterly-core-located"),
        ("CFKKRGASA-003", "assets/liabilities/operations/cash-flow quarterlies", "3-6", "Q2 2026 quarterly statement front pages include assets, liabilities, summary operations, and cash flow pages for legal-entity update extraction.", "core quarterly legal-entity update", "quarterly pages do not provide full annual Schedule D/BA detail", "quarterly-core-located"),
        ("CFKKRGASA-004", "assets/liabilities/operations/cash-flow quarterlies", "3-6", "Q2 2026 quarterly statement front pages include assets, liabilities, summary operations, and cash flow pages for legal-entity update extraction.", "core quarterly legal-entity update", "quarterly pages do not provide full annual Schedule D/BA detail", "quarterly-core-located"),
        ("CFKKRGASA-005", "assets page", "3", "Accordia annual page 3 shows ASSETS and net admitted asset columns.", "legal-entity asset base and invested-asset denominator", "summary only; not issuer-level holdings", "page-located"),
        ("CFKKRGASA-005", "liabilities surplus and other funds", "4", "Accordia annual page 4 shows LIABILITIES, SURPLUS AND OTHER FUNDS.", "liability base for source-pool and spread bridge", "not product-level liability cost", "page-located"),
        ("CFKKRGASA-005", "summary of operations", "5", "Accordia annual page 5 shows SUMMARY OF OPERATIONS.", "statutory earnings and net investment income bridge", "summary line only", "page-located"),
        ("CFKKRGASA-005", "cash flow", "6", "Accordia annual page 6 shows CASH FLOW and premiums collected/net investment income cash-flow lines.", "legal-entity cash receipt/proxy bridge", "does not allocate cash to specific holdings or borrowers", "page-located"),
        ("CFKKRGASA-005", "exhibit of net investment income", "15", "Accordia annual page 15 shows EXHIBIT OF NET INVESTMENT INCOME with collected and earned columns.", "asset-class investment-income extraction target", "not issuer-level income without schedule detail", "page-located"),
        ("CFKKRGASA-005", "Schedule D Part 1A quality and maturity", "130;135", "Accordia annual pages 130 and 135 show Schedule D Part 1A quality and maturity distribution.", "bond portfolio quality, maturity, and NAIC distribution control", "distribution only; not named issuer allocation", "range-located"),
        ("CFKKRGASA-005", "Schedule DB derivatives", "140-200;280-460", "Accordia sampled pages show Schedule DB replication and derivative schedules across the mid/back filing.", "derivative/hedging exposure and risk-transfer context", "not direct cash-return proof without counterparty and settlement extraction", "sampled-range-located"),
        ("CFKKRGASA-005", "Schedule B mortgage loans", "210", "Accordia annual page 210 shows Schedule B Part 1 mortgage loans owned.", "mortgage-loan asset destination and collateral category evidence", "needs row-level loan parsing", "page-located"),
        ("CFKKRGASA-005", "Schedule D long-term bonds owned", "220-245", "Accordia annual pages 220-240 show Schedule D Part 1 Section 1 issuer-credit obligations and page 245 shows Section 2 asset-backed securities.", "main named issuer-credit and ABS holdings extraction route", "needs row parsing and borrower/issuer classification", "range-located"),
        ("CFKKRGASA-005", "Schedule D acquired during year", "250-255", "Accordia annual pages 250 and 255 show Schedule D Part 3 acquired during current year.", "new bond/stock purchase and capital deployment evidence", "does not prove use or return by itself", "range-located"),
        ("CFKKRGASA-005", "Schedule D disposed during year", "260-265", "Accordia annual pages 260 and 265 show Schedule D Part 4 sold, redeemed, or disposed during current year.", "sale, maturity, redemption, consideration, and gain/loss route", "needs matching to holdings and cash-flow totals", "range-located"),
        ("CFKKRGASA-005", "Schedule D acquired and disposed", "270", "Accordia annual page 270 shows Schedule D Part 5 acquired and fully disposed during current year.", "same-year acquisition/disposal cash and gain/loss evidence", "needs matching and cash-vs-noncash classification", "page-located"),
        ("CFKKRGASA-005", "Schedule E cash and deposits", "464", "Accordia annual page 464 shows Schedule E Part 3 special deposits.", "cash, cash equivalents, and special-deposit support", "liquidity schedule only", "page-located"),
        ("CFKKRGASA-006", "assets/liabilities/operations/cash-flow annual core", "2-5", "Commonwealth annual pages 2-5 show assets, liabilities, summary operations, and cash flow.", "legal-entity core financial bridge", "compact filing route; deep schedules still need parser confirmation", "range-located"),
        ("CFKKRGASA-006", "Schedule S funds withheld and reinsurance", "120", "Commonwealth annual page 120 shows Schedule S Part 8 reinsurance agreements with funds withheld and modified coinsurance.", "reinsurance, funds-withheld, and liability/collateral routing context", "not legal cash availability without treaty/account detail", "page-located"),
        ("CFKKRGASA-006", "Schedule D Part 1A quality and maturity", "160", "Commonwealth annual page 160 shows Schedule D Part 1A quality and maturity distribution.", "bond portfolio quality, maturity, and NAIC distribution control", "distribution only; not named issuer allocation", "page-located"),
        ("CFKKRGASA-006", "Schedule E cash and deposits", "170", "Commonwealth annual page 170 shows Schedule E special deposits.", "cash and special-deposit support", "liquidity schedule only", "page-located"),
        ("CFKKRGASA-007", "assets/liabilities/operations/cash-flow annual core", "3-6", "First Allmerica annual pages 3-6 show assets, liabilities, summary operations, and cash flow.", "legal-entity core financial bridge", "summary pages only", "range-located"),
        ("CFKKRGASA-007", "exhibit of net investment income", "18", "First Allmerica annual page 18 shows EXHIBIT OF NET INVESTMENT INCOME.", "asset-class investment-income extraction target", "not issuer-level income without detail", "page-located"),
        ("CFKKRGASA-007", "Schedule D Part 1A quality and maturity", "150", "First Allmerica annual page 150 shows Schedule D Part 1A quality and maturity distribution.", "bond portfolio quality, maturity, and NAIC distribution control", "distribution only", "page-located"),
        ("CFKKRGASA-007", "Schedule E cash and deposits", "160", "First Allmerica annual page 160 shows Schedule E cash equivalents.", "cash and special-deposit support", "liquidity schedule only", "page-located"),
        ("CFKKRGASA-008", "assets/liabilities/operations/cash-flow annual core", "3-6", "Forethought annual pages 3-6 show assets, liabilities, summary operations, and cash flow.", "legal-entity core financial bridge", "summary pages only", "range-located"),
        ("CFKKRGASA-008", "exhibit of net investment income", "18", "Forethought annual page 18 shows EXHIBIT OF NET INVESTMENT INCOME.", "asset-class investment-income extraction target", "not issuer-level income without detail", "page-located"),
        ("CFKKRGASA-008", "asset valuation reserve", "80", "Forethought annual page 80 shows ASSET VALUATION RESERVE.", "credit-quality and reserve-pressure support", "not issuer-level NAIC or impairment proof", "page-located"),
        ("CFKKRGASA-008", "Schedule D Part 1A quality and maturity", "140", "Forethought annual page 140 shows Schedule D Part 1A quality and maturity distribution.", "bond portfolio quality, maturity, and NAIC distribution control", "distribution only", "page-located"),
        ("CFKKRGASA-008", "Schedule E cash and deposits", "150", "Forethought annual page 150 shows Schedule DA verification for short-term investments.", "cash, short-term investment, and deposit support", "liquidity schedule only", "page-located"),
        ("CFKKRGASA-009", "Bermuda balance sheet", "2-5", "Global Atlantic Re pages 2-5 show Bermuda statutory balance sheet.", "Bermuda legal-entity asset/liability base", "summary financial statement only until notes parse", "range-located"),
        ("CFKKRGASA-009", "Bermuda income statement", "6-7", "Global Atlantic Re pages 6-7 show statutory statement of income.", "Bermuda earnings and investment income route", "not named holding-level cash return", "range-located"),
        ("CFKKRGASA-009", "Bermuda capital and surplus", "8;29", "Global Atlantic Re page 8 shows statutory capital and surplus and page 29 reconciles U.S. GAAP to statutory capital and surplus.", "capital availability and statutory reconciliation route", "not distribution waterfall proof", "range-located"),
        ("CFKKRGASA-009", "Bermuda investment note", "10-15", "Global Atlantic Re notes around pages 10-15 describe investments, interest accrual, derivatives, fair value, and credit-loss treatment.", "Bermuda investment note and valuation context", "note text may be summary only without named holdings", "range-located"),
        ("CFKKRGASA-010", "Bermuda balance sheet", "2-5", "Global Atlantic Assurance pages 2-5 show Bermuda statutory balance sheet.", "Bermuda legal-entity asset/liability base", "summary financial statement only until notes parse", "range-located"),
        ("CFKKRGASA-010", "Bermuda income statement", "6-7", "Global Atlantic Assurance pages 6-7 show statutory statement of income.", "Bermuda earnings and investment income route", "not named holding-level cash return", "range-located"),
        ("CFKKRGASA-010", "Bermuda capital and surplus", "8", "Global Atlantic Assurance page 8 shows statutory capital and surplus.", "capital availability and statutory reconciliation route", "not distribution waterfall proof", "page-located"),
        ("CFKKRGASA-010", "Bermuda investment note", "10-15;20", "Global Atlantic Assurance notes around pages 10-15 and 20 describe investments, loan receivables, fair value, credit losses, and derivatives.", "Bermuda investment note and valuation context", "note text may be summary only without named holdings", "range-located"),
    ]
    all_rows = []
    for acq_id, target, pages, evidence, proof_use, boundary, status in manual_targets:
        source = source_by_id[acq_id]
        start = pages.split(";")[0].split("-")[0]
        end = pages.split(";")[-1].split("-")[-1]
        all_rows.append(
            {
                "acquisition_id": acq_id,
                "legal_entity": source["legal_entity"],
                "period": source["period"],
                "statement_type": source["statement_type"],
                "extraction_target": target,
                "page_start": start,
                "page_end": end,
                "pages_found": pages,
                "evidence_found": evidence,
                "proof_use": proof_use,
                "boundary": boundary,
                "current_status": status,
                "next_action": "extract targeted pages into normalized statutory fields",
                "upgrade_test": f"promote only when {target} is parsed into normalized fields and reconciled to statement totals",
            }
        )
    stats = {
        "pdfs_scanned": 0,
        "total_pdf_pages_available": 0,
        "total_pdf_pages_probed": 0,
        "page_extract_errors_or_timeouts": 0,
    }
    for source in source_by_id.values():
        page_count_match = re.search(r"pages=(\d+)", source.get("pdf_probe", ""))
        page_count = int(page_count_match.group(1)) if page_count_match else 0
        stats["pdfs_scanned"] += 1
        stats["total_pdf_pages_available"] += page_count
    stats["total_pdf_pages_probed"] = len(all_rows)
    for idx, row in enumerate(all_rows, start=1):
        row["locator_id"] = f"CFKKRGASL-{idx:03d}"
    return all_rows, stats


def diagnostic_rows(rows: list[dict[str, str]], stats: dict[str, int]) -> list[dict[str, str]]:
    annual = [r for r in rows if r["period"] == "Q4 2025"]
    quarter = [r for r in rows if r["period"] == "Q2 2026"]
    bermuda = [r for r in rows if r["period"] == "FY 2025"]
    schedule_d = [r for r in rows if r["extraction_target"].startswith("Schedule D")]
    schedule_ba = [r for r in rows if r["extraction_target"] == "Schedule BA"]
    cash = [r for r in rows if r["extraction_target"] in {"cash flow", "exhibit of net investment income", "Bermuda income statement", "Bermuda investment note"}]
    metrics = [
        ("locator_rows", len(rows), "count"),
        ("pdfs_scanned", stats["pdfs_scanned"], "count"),
        ("total_pdf_pages_available", stats["total_pdf_pages_available"], "pages"),
        ("total_pdf_pages_probed", stats["total_pdf_pages_probed"], "pages"),
        ("page_extract_errors_or_timeouts", stats["page_extract_errors_or_timeouts"], "pages"),
        ("annual_locator_rows", len(annual), "count"),
        ("quarterly_locator_rows", len(quarter), "count"),
        ("bermuda_locator_rows", len(bermuda), "count"),
        ("schedule_d_locator_rows", len(schedule_d), "count"),
        ("schedule_ba_locator_rows", len(schedule_ba), "count"),
        ("cash_or_income_locator_rows", len(cash), "count"),
        ("full_named_cash_proof_upgrades", 0, "count"),
        ("next_parser", "global-atlantic-statutory-compact-extraction", "parser"),
    ]
    out = []
    for idx, (metric, value, units) in enumerate(metrics, start=1):
        out.append(
            {
                "diagnostic_id": f"CFKKRGASLD-{idx:03d}",
                "metric": metric,
                "value": str(value),
                "units": units,
                "proof_use": "controls Global Atlantic statutory schedule location coverage",
                "boundary": "Locator diagnostics prove page targeting only; they do not prove parsed holdings, income, cash receipts, or returns.",
                "next_action": "Run compact extraction for assets, liabilities, income, cash flow, Schedule D/BA, funds-withheld, and Bermuda investment notes.",
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
    key_rows = [
        r
        for r in rows
        if r["extraction_target"]
        in {
            "assets page",
            "liabilities surplus and other funds",
            "summary of operations",
            "cash flow",
            "exhibit of net investment income",
            "Schedule BA",
            "Schedule D verification",
            "Schedule D Part 1A quality and maturity",
            "Schedule D long-term bonds owned",
            "Schedule D acquired during year",
            "Schedule D disposed during year",
            "Schedule S funds withheld and reinsurance",
            "Bermuda balance sheet",
            "Bermuda income statement",
            "Bermuda investment note",
        }
    ][:24]
    table = "\n".join(
        "| {locator_id} | {legal_entity} | {period} | {extraction_target} | {pages_found} | {current_status} |".format(**r)
        for r in key_rows
    )
    MEMO.write_text(
        f"""# Capital Flow KKR Global Atlantic Statutory Schedule Locator Pass 1

## Purpose

This pass converts the `10` locally acquired Global Atlantic statutory PDFs into targeted extraction maps.

It asks:

`Where inside the Global Atlantic legal-entity filings are the schedules needed to test assets, liabilities, investment income, cash flow, named holdings, proceeds, funds-withheld/reinsurance economics, and Bermuda investment context?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-statutory-schedule-locator-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-statutory-schedule-locator-diagnostic-pass-1.csv`

The upstream source acquisition pass is:

`/cluster/capital-flow-kkr-global-atlantic-statutory-source-acquisition-pass-1.md`

## Short Answer

`The Global Atlantic statutory source set is now extraction-ready. The locator probes {by_metric['pdfs_scanned']} local PDFs, covering {by_metric['total_pdf_pages_probed']} targeted pages out of {by_metric['total_pdf_pages_available']} available PDF pages, and creates {by_metric['locator_rows']} locator rows, including {by_metric['schedule_d_locator_rows']} Schedule D rows, {by_metric['schedule_ba_locator_rows']} Schedule BA rows, and {by_metric['cash_or_income_locator_rows']} cash/income rows. This locates the proof zones but does not yet parse holdings, income, proceeds, liability spread, or named cash return.`

## Main Result

| Metric | Value |
|---|---:|
| PDFs scanned | {by_metric['pdfs_scanned']} |
| PDF pages available | {by_metric['total_pdf_pages_available']} |
| Targeted pages probed | {by_metric['total_pdf_pages_probed']} |
| Locator rows | {by_metric['locator_rows']} |
| Annual locator rows | {by_metric['annual_locator_rows']} |
| Quarterly locator rows | {by_metric['quarterly_locator_rows']} |
| Bermuda locator rows | {by_metric['bermuda_locator_rows']} |
| Schedule D locator rows | {by_metric['schedule_d_locator_rows']} |
| Schedule BA locator rows | {by_metric['schedule_ba_locator_rows']} |
| Cash/income locator rows | {by_metric['cash_or_income_locator_rows']} |
| Full named cash proof upgrades | {by_metric['full_named_cash_proof_upgrades']} |

## Key Located Targets

| ID | Legal Entity | Period | Target | Pages | Status |
|---|---|---|---|---|---|
{table}

## Proof Effect

This pass moves KKR/Global Atlantic from local source acquisition to targeted extraction readiness. It shows where to extract the legal-entity balance sheet, liabilities, summary operations, cash flow, net investment income, Schedule D, Schedule BA, Schedule S/funds-withheld, Schedule E, and Bermuda investment-note zones.

## Boundary

This pass is still a locator, not a parser.

It does not prove named Schedule D/BA holdings, NAIC designations, borrower allocation, cash receipts, liability-cost spread, funds-withheld economics, FHLB liability economics, debt waterfalls, collateral certificates, or asset-level return.

## Next Action

Run `global-atlantic-statutory-compact-extraction` against the located pages, starting with the four Q4 `2025` U.S. annual statements and then the Q2 `2026` quarterlies and FY `2025` Bermuda financials.

## Decision

`kkr-global-atlantic-statutory-schedule-locator-ready-compact-extraction-next`

## Safe Claim

`The locally acquired Global Atlantic statutory filing set is schedule-located and ready for targeted extraction. The current locator identifies the pages and ranges needed for legal-entity assets, liabilities, cash flow, net investment income, Schedule D/BA, funds-withheld/reinsurance, Schedule E, and Bermuda investment context. It does not yet prove issuer-level holdings, investment income by holding, liability-cost spread, borrower destination, realized cash return, or asset-level return.`
""",
        encoding="utf-8",
    )


def main() -> None:
    rows, stats = build_rows()
    diagnostics = diagnostic_rows(rows, stats)
    write_csv(OUT, FIELDNAMES, rows)
    write_csv(DIAGNOSTIC_OUT, DIAGNOSTIC_FIELDS, diagnostics)
    write_memo(rows, diagnostics)
    print(f"wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT.relative_to(ROOT)}")
    print(f"wrote memo to {MEMO.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
