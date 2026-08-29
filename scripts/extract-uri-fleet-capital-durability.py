#!/usr/bin/env python3
"""Extract United Rentals fleet-capital durability metrics from cached filings."""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw" / "sec" / "industrial-goods" / "rental-leasing-services" / "united-rentals-inc"
OUT = (
    ROOT
    / "analysis"
    / "company-first-principles"
    / "data"
    / "capital-flow-uri-fleet-capital-durability-pass-1.csv"
)


@dataclass(frozen=True)
class PeriodSource:
    period: str
    label: str
    filing: str
    release: str
    period_type: str


PERIODS = [
    PeriodSource("2024-Q1", "2024-q1", "2024-q1-10q.html", "2024-q1-ex99-earnings-release.html", "quarter"),
    PeriodSource("2024-Q2", "2024-q2", "2024-q2-10q.html", "2024-q2-ex99-earnings-release.html", "quarter"),
    PeriodSource("2024-Q3", "2024-q3", "2024-q3-10q.html", "2024-q3-ex99-earnings-release.html", "quarter"),
    PeriodSource("2024-FY", "2024-10k", "2024-10k-10k.html", "2024-10k-ex99-earnings-release.html", "annual"),
    PeriodSource("2025-Q1", "2025-q1", "2025-q1-10q.html", "2025-q1-ex99-earnings-release.html", "quarter"),
    PeriodSource("2025-Q2", "2025-q2", "2025-q2-10q.html", "2025-q2-ex99-earnings-release.html", "quarter"),
    PeriodSource("2025-Q3", "2025-q3", "2025-q3-10q.html", "2025-q3-ex99-earnings-release.html", "quarter"),
    PeriodSource("2025-FY", "2025-10k", "2025-10k-10k.html", "2025-10k-ex99-earnings-release.html", "annual"),
    PeriodSource("2026-Q1", "2026-q1", "2026-q1-10q.html", "2026-q1-ex99-earnings-release.html", "quarter"),
    PeriodSource("2026-Q2", "2026-q2", "2026-q2-10q.html", "2026-q2-ex99-earnings-release.html", "quarter"),
]


FIELDS = [
    "row_id",
    "period",
    "company",
    "ticker",
    "theme",
    "subtheme",
    "metric",
    "value",
    "unit",
    "source_file",
    "source_detail",
    "calculation_or_source",
    "evidence_status",
    "what_it_says",
    "what_it_does_not_say",
    "next_source",
]


def text(path: Path) -> str:
    return " ".join(BeautifulSoup(path.read_text(errors="ignore"), "lxml").get_text(" ").split())


def amount_to_b(value: str, unit: str | None) -> float:
    number = float(value.replace(",", ""))
    if unit and unit.lower().startswith("million"):
        return number / 1000.0
    return number


def first(pattern: str, haystack: str, default: str = "") -> str:
    match = re.search(pattern, haystack, re.I)
    return match.group(1) if match else default


def first_amount(pattern: str, haystack: str) -> str:
    match = re.search(pattern, haystack, re.I)
    if not match:
        return ""
    return f"{amount_to_b(match.group(1), match.group(2)):.3f}".rstrip("0").rstrip(".")


def first_number_after(label: str, haystack: str) -> str:
    pattern = rf"{re.escape(label)}\s+\$?\s*\(?([0-9,]+)\)?(?:\s|$)"
    match = re.search(pattern, haystack, re.I)
    if not match:
        return ""
    return match.group(1).replace(",", "")


def debt_table_text(haystack: str) -> str:
    start = haystack.lower().find("debt, net of unamortized")
    if start == -1:
        return haystack
    end = haystack.lower().find("total long-term debt", start)
    if end == -1:
        end = start + 2500
    return haystack[start : end + 300]


def debt_value(label: str, haystack: str) -> str:
    haystack = debt_table_text(haystack)
    if label == "ABL facility":
        match = re.search(r"4\.(?:25|50?|5) billion ABL facility.*?(?:\$ )?([0-9,]+)\s+(?:\$ )?[0-9,]+", haystack, re.I)
    else:
        match = re.search(rf"{re.escape(label)}.*?(?:\$ )?([0-9,]+)\s+(?:\$ )?[0-9,]+", haystack, re.I)
    value = match.group(1).replace(",", "") if match else first_number_after(label, haystack)
    if not value:
        return ""
    return f"{float(value) / 1000.0:.3f}".rstrip("0").rstrip(".")


def cash_flow_value(label: str, haystack: str) -> str:
    value = first_number_after(label, haystack)
    if not value:
        return ""
    return f"{float(value) / 1000.0:.3f}".rstrip("0").rstrip(".")


def abl_facility_size(haystack: str) -> str:
    table = debt_table_text(haystack)
    match = re.search(r"\$\s*([0-9.]+) billion ABL facility", table, re.I)
    if not match:
        match = re.search(r"([0-9.]+) billion ABL facility", table, re.I)
    return match.group(1) if match else ""


def add_row(rows: list[dict[str, str]], source: PeriodSource, metric: str, value: str, unit: str, source_file: str, source_detail: str, calc: str, status: str, says: str, not_say: str, next_source: str) -> None:
    if value == "":
        return
    rows.append(
        {
            "row_id": f"URIFCD-{len(rows) + 1:03d}",
            "period": source.period,
            "company": "United Rentals",
            "ticker": "URI",
            "theme": "capital-intensive real-economy buildout",
            "subtheme": "fleet-capital durability",
            "metric": metric,
            "value": value,
            "unit": unit,
            "source_file": f"raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/{source_file}",
            "source_detail": source_detail,
            "calculation_or_source": calc,
            "evidence_status": status,
            "what_it_says": says,
            "what_it_does_not_say": not_say,
            "next_source": next_source,
        }
    )


def main() -> int:
    rows: list[dict[str, str]] = []

    for source in PERIODS:
        filing_path = RAW / source.filing
        release_path = RAW / source.release
        filing = text(filing_path)
        release = text(release_path)

        rental_revenue = first_amount(r"rental revenue(?: [0-9]+)?(?: of)? \$([0-9.]+) (billion|million)", release)
        fleet_productivity = first(r"fleet productivity(?: [0-9]+)? increased ([0-9.]+)%", release)
        oec_yoy = first(r"original equipment at cost.*?OEC.*?increased ([0-9.]+)%", release)
        ocf = first_amount(r"net cash provided by operating activities of \$([0-9.]+) (billion|million)", release)
        fcf = first_amount(r"free cash flow(?: [0-9]+)? of \$([0-9.]+) (billion|million)", release)
        gross_payments = first_amount(r"gross payments for purchases of rental equipment of \$([0-9.]+) (billion|million)", release)
        gross_capex = first_amount(r"gross rental capital expenditures of \$([0-9.]+) (billion|million)", release)
        liquidity = first_amount(r"total liquidity(?: [0-9]+)? of \$([0-9.]+) (billion|million)", release)
        net_leverage = first(r"net leverage ratio(?: [0-9]+)? of ([0-9.]+)x", release)

        purchase_cash = cash_flow_value("Payments for purchases of rental equipment", filing)
        sale_proceeds = cash_flow_value("Proceeds from sales of rental equipment", filing)
        if purchase_cash and sale_proceeds:
            net_fleet_cash = f"{float(purchase_cash) - float(sale_proceeds):.3f}".rstrip("0").rstrip(".")
        else:
            net_fleet_cash = ""

        ar_balance = debt_value("Accounts receivable securitization facility", filing)
        abl_balance = debt_value("ABL facility", filing)
        abl_size = abl_facility_size(filing)
        term_loan = debt_value("Term loan facility", filing)
        total_debt = debt_value("Total debt", filing)
        collateral = first_amount(r"As of [A-Za-z]+ [0-9]+, [0-9]{4}, there were \$\s*([0-9.]+) (billion|million) of receivables.*?in the collateral pool", filing)
        if collateral and ar_balance:
            collateral_coverage = f"{float(collateral) / float(ar_balance) * 100:.1f}"
            collateral_excess = f"{float(collateral) - float(ar_balance):.3f}".rstrip("0").rstrip(".")
        else:
            collateral_coverage = ""
            collateral_excess = ""
        if abl_balance and abl_size:
            abl_draw = f"{float(abl_balance) / float(abl_size) * 100:.1f}"
        else:
            abl_draw = ""

        release_source = source.release
        filing_source = source.filing
        add_row(rows, source, "Rental revenue", rental_revenue, "B USD", release_source, "SEC 8-K earnings-release exhibit", "Company disclosed rental revenue in period highlights.", "source-table-backed", "URI repeatedly converts fleet access into rental revenue.", "Rental revenue is not utilization, margin, or ROIC.", "Owned-equipment rental revenue and rental gross margin by segment")
        add_row(rows, source, "Fleet productivity increase", fleet_productivity, "percent", release_source, "SEC 8-K earnings-release exhibit", "Company-defined metric reflecting rental rates, time utilization, and mix on owned-equipment rental revenue.", "source-defined-operating-metric", "URI repeatedly reports a positive fleet productivity measure.", "The metric is aggregated and does not split rate, utilization, and mix.", "Fleet productivity bridge components")
        add_row(rows, source, "Average OEC year-over-year increase", oec_yoy, "percent", release_source, "SEC 8-K earnings-release exhibit", "Company disclosed year-over-year average OEC change.", "source-defined-scale-metric", "URI repeatedly expanded average fleet OEC versus the prior-year period.", "OEC growth can include inflation, mix, acquisitions, and replacement capital.", "Fleet OEC roll-forward by class and acquisition")
        add_row(rows, source, "Net cash provided by operating activities", ocf, "B USD", release_source, "SEC 8-K earnings-release exhibit", "Company disclosed net cash provided by operating activities.", "cash-conversion-source-table", "URI's fleet model is supported by recurring operating cash flow.", "Operating cash flow is company-level and not source-of-funds proof for specific fleet purchases.", "Quarterly cash-flow bridge with debt draws and repayments")
        add_row(rows, source, "Free cash flow", fcf, "B USD", release_source, "SEC 8-K earnings-release exhibit", "Company disclosed free cash flow in period highlights.", "non-gaap-cash-context", "Free cash flow remains positive across the extracted periods.", "Free cash flow is non-GAAP and not fleet-return proof.", "Free cash flow reconciliation by period")
        add_row(rows, source, "Gross payments for purchases of rental equipment", gross_payments, "B USD", release_source, "SEC 8-K earnings-release exhibit", "Company disclosed gross payments for rental equipment purchases.", "fleet-capex-source-table", "URI repeatedly deploys large cash amounts into rental equipment.", "Gross payments do not separate growth and replacement fleet.", "Growth versus replacement capex and fleet class detail")
        add_row(rows, source, "Gross rental capital expenditures", gross_capex, "B USD", release_source, "SEC 8-K earnings-release exhibit", "Company disclosed gross rental capital expenditures.", "fleet-capex-source-table", "URI repeatedly absorbs gross rental capex.", "Gross rental capex does not equal net fleet growth.", "Fleet additions, disposals, acquisitions, and OEC roll-forward")
        add_row(rows, source, "Payments for purchases of rental equipment", purchase_cash, "B USD", filing_source, "SEC 10-Q/10-K cash-flow statement", "Filed cash-flow statement line.", "filed-source-table", "The filed statement confirms cash paid for rental equipment.", "The line does not identify asset class or funding source.", "Cash-flow statement and capex reconciliation")
        add_row(rows, source, "Proceeds from sales of rental equipment", sale_proceeds, "B USD", filing_source, "SEC 10-Q/10-K cash-flow statement", "Filed cash-flow statement line.", "filed-source-table", "Used-equipment proceeds repeatedly recycle cash back into the model.", "Sale proceeds do not prove asset quality or margin by class.", "Used-equipment margin and OEC recovery")
        add_row(rows, source, "Net cash rental-equipment investment", net_fleet_cash, "B USD", filing_source, "SEC 10-Q/10-K cash-flow statement", "Payments for purchases of rental equipment less proceeds from sales of rental equipment.", "derived-filed-source", "URI's net fleet cash deployment can be tracked over time.", "Net cash deployment is not a growth-only or return metric.", "Fleet roll-forward and growth/replacement split")
        add_row(rows, source, "Total liquidity", liquidity, "B USD", release_source, "SEC 8-K earnings-release exhibit", "Company disclosed total liquidity, including cash plus ABL and AR securitization availability.", "funding-context-source-defined", "URI retains explicit liquidity channels alongside fleet deployment.", "Liquidity is not legal availability or use-of-proceeds proof.", "ABL and AR securitization availability schedules")
        add_row(rows, source, "Net leverage ratio", net_leverage, "x", release_source, "SEC 8-K earnings-release exhibit", "Company disclosed net leverage ratio.", "leverage-context-source-defined", "URI's leverage stayed inside a narrow disclosed range across the extracted periods.", "Net leverage is not covenant headroom or collateral coverage.", "Debt agreement covenant calculations")
        add_row(rows, source, "Accounts receivable securitization facility balance", ar_balance, "B USD", filing_source, "SEC 10-Q/10-K debt table", "Filed debt table balance.", "filed-term-summary", "The AR securitization facility is a recurring part of URI's funding stack.", "Facility balance is not collateral eligibility or advance-rate proof.", "Receivables purchase agreement and collateral reports")
        add_row(rows, source, "ABL facility balance", abl_balance, "B USD", filing_source, "SEC 10-Q/10-K debt table", "Filed debt table balance.", "filed-term-summary", "The ABL facility is a recurring secured funding layer.", "ABL balance is not legal availability or borrowing-base proof.", "ABL agreement and borrowing-base certificates")
        add_row(rows, source, "Term loan facility balance", term_loan, "B USD", filing_source, "SEC 10-Q/10-K debt table", "Filed debt table balance.", "filed-term-summary", "Term debt is another layer in the URI capital stack.", "Term debt does not map to specific fleet purchases.", "Term loan agreement and maturity schedule")
        add_row(rows, source, "Total debt", total_debt, "B USD", filing_source, "SEC 10-Q/10-K debt table", "Filed debt table balance.", "debt-stack-context", "URI carries a large debt stack beside recurring fleet investment.", "Total debt does not prove marginal funding source or return.", "Debt maturity ladder and source/use events")
        add_row(rows, source, "Receivables collateral pool net of reserves and deductions", collateral, "B USD", filing_source, "SEC 10-Q/10-K debt note", "Filed debt note collateral-pool disclosure.", "collateral-source-table", "URI discloses a receivables collateral pool for the AR securitization.", "The pool does not reveal advance rates, reserves, concentration, or legal availability.", "Securitization collateral reports")
        add_row(rows, source, "AR collateral pool to AR securitization borrowings", collateral_coverage, "percent", filing_source, "SEC 10-Q/10-K debt note", "Receivables collateral pool divided by AR securitization facility balance.", "derived-collateral-ratio", "The AR securitization collateral cushion can be tracked across filings.", "This is not full borrowing-base proof.", "Advance rates, eligibility rules, and purchaser limits")
        add_row(rows, source, "AR excess collateral pool over borrowings", collateral_excess, "B USD", filing_source, "SEC 10-Q/10-K debt note", "Receivables collateral pool less AR securitization facility balance.", "derived-collateral-ratio", "URI has a dollar cushion in the receivables pool in disclosed periods.", "Excess pool is not the same as legal availability.", "Availability schedules and reserve detail")
        add_row(rows, source, "ABL stated facility size", abl_size, "B USD", filing_source, "SEC 10-Q/10-K debt table", "Filed debt table stated ABL facility size.", "filed-term-summary", "The stated ABL platform size can be tracked across filings.", "Stated size is not legal availability.", "ABL agreement and borrowing-base certificates")
        add_row(rows, source, "ABL drawn against stated facility size", abl_draw, "percent", filing_source, "SEC 10-Q/10-K debt table", "ABL facility balance divided by the stated ABL facility size in the filed debt table.", "derived-draw-intensity", "Simple ABL draw intensity can be tracked across filings.", "Stated-size headroom is not legal availability.", "Borrowing-base certificates, L/C use, reserves, and covenants")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {OUT.relative_to(ROOT)} rows={len(rows)} cols={len(FIELDS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
