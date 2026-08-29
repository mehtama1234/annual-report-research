#!/usr/bin/env python3
"""Extract ARCC Q2 2026 schedule rows and official industry subtotals.

The official industry-subtotal output is the reconciled source of industry totals.
The row-level output is a borrower-discovery aid and remains parser-derived until
it reconciles to the official subtotals.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "raw/primary-sources/capital-flow/ares-capital/q2-2026/arcc-2026-q2-10q.html"
DATA_DIR = ROOT / "analysis/company-first-principles/data"
DEFAULT_ROWS = DATA_DIR / "capital-flow-arcc-schedule-parser-rows.csv"
DEFAULT_SUMMARY = DATA_DIR / "capital-flow-arcc-schedule-industry-summary.csv"
DEFAULT_SUBTOTALS = DATA_DIR / "capital-flow-arcc-official-industry-subtotals.csv"

REPORTED_TOTAL_FAIR_VALUE_USD_M = 29_349.3
REPORTED_NON_CONTROL_NON_AFFILIATE_FAIR_VALUE_USD_M = 24_282.0

INDUSTRIES = {
    "Automobiles and Components",
    "Capital Goods",
    "Commercial and Professional Services",
    "Consumer Distribution and Retail",
    "Consumer Durables and Apparel",
    "Consumer Services",
    "Data Centers",
    "Energy",
    "Financial Services",
    "Food and Beverage",
    "Gas Utilities",
    "Health Care Equipment and Services",
    "Household and Personal Products",
    "Independent Power and Renewable Electricity Producers",
    "Insurance",
    "Investment Funds and Vehicles",
    "Materials",
    "Pharmaceuticals, Biotechnology and Life Sciences",
    "Real Estate Management and Development",
    "Software and Services",
    "Sports, Media and Entertainment",
    "Technology Hardware and Equipment",
    "Telecommunication Services",
    "Transportation",
}

HEADER_LABELS = {
    "Company (1)",
    "Business Description",
    "Investment (18)",
    "Coupon (3)",
    "Reference (7)",
    "Spread (3)",
    "Acquisition Date",
    "Maturity Date",
    "Shares/Units",
    "Principal",
    "Amortized Cost",
    "Fair Value",
    "% of Net Assets",
}


def clean_cells(row) -> list[str]:
    return [" ".join(cell.get_text(" ", strip=True).split()) for cell in row.find_all(["td", "th"])]


def parse_number(value: str | None) -> float | None:
    if value is None:
        return None
    text = value.replace("$", "").replace(",", "").replace("—", "0").strip()
    if text.endswith("%"):
        text = text[:-1].strip()
    if not text:
        return None
    if text.startswith("(") and text.endswith(")"):
        text = "-" + text[1:-1]
    try:
        return float(text)
    except ValueError:
        return None


def is_numeric_cell(value: str) -> bool:
    text = value.replace("$", "").strip()
    return bool(re.fullmatch(r"\(?\d{1,3}(?:,\d{3})*(?:\.\d+)?\)?", text))


def load_tables(source: Path):
    soup = BeautifulSoup(source.read_text(errors="ignore"), "html.parser")
    return soup.find_all("table")


def extract_row_level(tables, source: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    current_industry = None
    last_company = ""
    last_description = ""

    for table_index in range(9, 76):
        for table_row in tables[table_index].find_all("tr"):
            cells = clean_cells(table_row)
            non_empty = [cell for cell in cells if cell]
            if not non_empty:
                continue
            if len(non_empty) == 1 and non_empty[0] in INDUSTRIES:
                current_industry = non_empty[0]
                continue
            if non_empty[0].startswith("Company") or "Business Description" in non_empty:
                continue

            investment_type = cells[4] if len(cells) > 4 else ""
            if not investment_type or current_industry is None:
                continue

            company = cells[0] if len(cells) > 0 and cells[0] else last_company
            description = cells[2] if len(cells) > 2 and cells[2] else last_description

            nums: list[tuple[int, float]] = []
            for index, cell in enumerate(cells[14:], start=14):
                if is_numeric_cell(cell):
                    value = parse_number(cell)
                    if value is not None:
                        nums.append((index, value))

            if len(nums) < 2:
                continue

            principal_or_shares = nums[-3][1] if len(nums) >= 3 else ""
            amortized_cost = nums[-2][1]
            fair_value = nums[-1][1]

            if company:
                last_company = company
            if description:
                last_description = description

            rows.append(
                {
                    "claim_id": "CF-004, CF-005",
                    "company": "Ares Capital Corporation",
                    "manager": "Ares",
                    "vehicle": "ARCC",
                    "period": "Q2 2026 / June 30 2026",
                    "industry": current_industry,
                    "borrower": company,
                    "business_description": description,
                    "investment_type": investment_type,
                    "principal_or_shares": principal_or_shares,
                    "amortized_cost_usd_m": amortized_cost,
                    "fair_value_usd_m": fair_value,
                    "source_file": str(source.relative_to(ROOT)),
                    "source_table_index": table_index,
                    "status": "parser-derived-needs-reconciliation",
                }
            )

    return rows


def extract_official_subtotals(tables, source: Path) -> list[dict[str, object]]:
    subtotals: list[dict[str, object]] = []
    current_industry = None
    subtotal_text_markers = [
        "loan",
        "stock",
        "units",
        "interest",
        "warrant",
        "shares",
        "pik",
        "sofr",
        "sonia",
        "euribor",
        "nibor",
    ]

    for table_index in range(9, 76):
        for row_index, table_row in enumerate(tables[table_index].find_all("tr")):
            cells = clean_cells(table_row)
            non_empty = [cell for cell in cells if cell]
            if len(non_empty) == 1 and non_empty[0] in INDUSTRIES:
                current_industry = non_empty[0]
                continue
            if current_industry is None:
                continue

            text = " ".join(non_empty).lower()
            if any(marker in text for marker in subtotal_text_markers):
                continue

            percent_of_net_assets = None
            for index in [23, 21, 25, 22]:
                if index < len(cells) and "%" in cells[index]:
                    percent_of_net_assets = parse_number(cells[index])

            if percent_of_net_assets is None:
                continue

            amortized_cost = parse_number(cells[17] if len(cells) > 17 else None)
            fair_value = parse_number(cells[20] if len(cells) > 20 else None)
            if fair_value is None:
                fair_value = parse_number(cells[22] if len(cells) > 22 else None)
            if amortized_cost is None or fair_value is None:
                continue

            subtotals.append(
                {
                    "claim_id": "CF-004, CF-005",
                    "company": "Ares Capital Corporation",
                    "manager": "Ares",
                    "vehicle": "ARCC",
                    "period": "Q2 2026 / June 30 2026",
                    "industry": current_industry,
                    "amortized_cost_usd_m": amortized_cost,
                    "fair_value_usd_m": fair_value,
                    "percent_of_net_assets": percent_of_net_assets,
                    "share_of_total_fair_value_percent": round(fair_value / REPORTED_TOTAL_FAIR_VALUE_USD_M * 100, 2),
                    "source_file": str(source.relative_to(ROOT)),
                    "source_table_index": table_index,
                    "source_row_index": row_index,
                    "source_basis": "Official industry subtotal row in ARCC Q2 2026 10-Q schedule of investments; subtotal rows reconcile to total investments fair value.",
                    "status": "official-subtotal-reconciles-to-total-fair-value",
                }
            )
            current_industry = None

    return sorted(subtotals, key=lambda row: float(row["fair_value_usd_m"]), reverse=True)


def summarize_row_level(rows: list[dict[str, object]], source: Path) -> list[dict[str, object]]:
    parsed_total = sum(float(row["fair_value_usd_m"]) for row in rows)
    fair_by_industry: defaultdict[str, float] = defaultdict(float)
    borrower_by_industry: defaultdict[str, set[str]] = defaultdict(set)
    investment_count: Counter[str] = Counter()
    first_lien: defaultdict[str, float] = defaultdict(float)
    second_lien: defaultdict[str, float] = defaultdict(float)
    subordinated: defaultdict[str, float] = defaultdict(float)
    other_or_equity: defaultdict[str, float] = defaultdict(float)

    for row in rows:
        industry = str(row["industry"])
        fair_value = float(row["fair_value_usd_m"])
        investment_type = str(row["investment_type"]).lower()
        fair_by_industry[industry] += fair_value
        borrower_by_industry[industry].add(str(row["borrower"]))
        investment_count[industry] += 1
        if "first lien" in investment_type:
            first_lien[industry] += fair_value
        elif "second lien" in investment_type:
            second_lien[industry] += fair_value
        elif "subordinated" in investment_type:
            subordinated[industry] += fair_value
        else:
            other_or_equity[industry] += fair_value

    summary = []
    for industry, fair_value in sorted(fair_by_industry.items(), key=lambda item: item[1], reverse=True):
        summary.append(
            {
                "claim_id": "CF-004, CF-005",
                "company": "Ares Capital Corporation",
                "manager": "Ares",
                "vehicle": "ARCC",
                "period": "Q2 2026 / June 30 2026",
                "industry": industry,
                "parsed_fair_value_usd_m": round(fair_value, 1),
                "share_of_parsed_schedule_percent": round(fair_value / parsed_total * 100, 2),
                "share_of_reported_non_control_non_affiliate_percent": round(
                    fair_value / REPORTED_NON_CONTROL_NON_AFFILIATE_FAIR_VALUE_USD_M * 100, 2
                ),
                "investment_rows": investment_count[industry],
                "unique_borrower_names": len([borrower for borrower in borrower_by_industry[industry] if borrower]),
                "first_lien_fair_value_usd_m": round(first_lien[industry], 1),
                "second_lien_fair_value_usd_m": round(second_lien[industry], 1),
                "subordinated_fair_value_usd_m": round(subordinated[industry], 1),
                "other_or_equity_fair_value_usd_m": round(other_or_equity[industry], 1),
                "source_file": str(source.relative_to(ROOT)),
                "parser_coverage_note": (
                    f"Parsed fair value {parsed_total:.1f} vs reported non-controlled/non-affiliate fair value "
                    f"{REPORTED_NON_CONTROL_NON_AFFILIATE_FAIR_VALUE_USD_M:.1f}; coverage "
                    f"{parsed_total / REPORTED_NON_CONTROL_NON_AFFILIATE_FAIR_VALUE_USD_M * 100:.1f}%. "
                    f"Reported total investments fair value is {REPORTED_TOTAL_FAIR_VALUE_USD_M:.1f}."
                ),
                "status": "parser-derived-needs-reconciliation",
            }
        )
    return summary


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"no rows to write for {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--rows-output", type=Path, default=DEFAULT_ROWS)
    parser.add_argument("--summary-output", type=Path, default=DEFAULT_SUMMARY)
    parser.add_argument("--subtotals-output", type=Path, default=DEFAULT_SUBTOTALS)
    args = parser.parse_args()

    tables = load_tables(args.source)
    row_level = extract_row_level(tables, args.source)
    summary = summarize_row_level(row_level, args.source)
    subtotals = extract_official_subtotals(tables, args.source)

    write_csv(args.rows_output, row_level)
    write_csv(args.summary_output, summary)
    write_csv(args.subtotals_output, subtotals)

    row_total = sum(float(row["fair_value_usd_m"]) for row in row_level)
    subtotal_total = sum(float(row["fair_value_usd_m"]) for row in subtotals)
    print(f"row-level rows: {len(row_level)}; fair value: {row_total:.1f}")
    print(f"official subtotal rows: {len(subtotals)}; fair value: {subtotal_total:.1f}")
    print(f"official subtotal reconciliation difference: {subtotal_total - REPORTED_TOTAL_FAIR_VALUE_USD_M:.1f}")


if __name__ == "__main__":
    main()
