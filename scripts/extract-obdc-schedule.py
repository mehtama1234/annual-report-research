#!/usr/bin/env python3
"""Extract OBDC Q2 2026 official industry subtotals from the 10-Q schedule."""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "raw/primary-sources/capital-flow/blue-owl-capital-corporation/q2-2026/obdc-2026-q2-10q.html"
DATA_DIR = ROOT / "analysis/company-first-principles/data"
DEFAULT_SUBTOTALS = DATA_DIR / "capital-flow-obdc-official-industry-subtotals.csv"
DEFAULT_SUMMARY = DATA_DIR / "capital-flow-obdc-industry-summary.csv"

REPORTED_TOTAL_FAIR_VALUE_USD_THOUSANDS = 14_955_049.0
SCHEDULE_TABLE_START = 13
SCHEDULE_TABLE_END = 33

SECTION_MARKERS = (
    "Non-controlled/non-affiliated portfolio company investments",
    "Non-controlled/affiliated portfolio company investments",
    "Controlled/affiliated portfolio company investments",
)

NON_INDUSTRY_SINGLETONS = {
    "Debt Investments(7)",
    "Equity Investments",
    "Company",
    "Investment",
    "Interest",
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
    text = re.sub(r"^\(\s*", "(", text)
    text = re.sub(r"\s*\)$", ")", text)
    if text.startswith("(") and text.endswith(")"):
        text = "-" + text[1:-1].strip()
    try:
        return float(text)
    except ValueError:
        return None


def is_number_like(value: str) -> bool:
    text = value.replace("$", "").strip()
    return bool(re.fullmatch(r"\(?\s*\d{1,3}(?:,\d{3})*(?:\.\d+)?\s*\)?|—", text))


def load_tables(source: Path):
    soup = BeautifulSoup(source.read_text(errors="ignore"), "html.parser")
    return soup.find_all("table")


def value_after_dollar(cells: list[str], dollar_number: int) -> float | None:
    dollar_positions = [index for index, cell in enumerate(cells) if cell == "$"]
    if len(dollar_positions) >= dollar_number:
        value_index = dollar_positions[dollar_number - 1] + 1
        if value_index < len(cells):
            return parse_number(cells[value_index])
    numeric_values = [parse_number(cell) for cell in cells if is_number_like(cell)]
    numeric_values = [value for value in numeric_values if value is not None]
    if len(numeric_values) >= dollar_number:
        return numeric_values[dollar_number - 1]
    return None


def row_percent(cells: list[str]) -> float | None:
    for index, cell in enumerate(cells):
        if cell == "%" and index > 0:
            return parse_number(cells[index - 1])
        if cell.endswith("%"):
            return parse_number(cell)
    return None


def is_industry_header(non_empty: list[str]) -> bool:
    if len(non_empty) != 1:
        return False
    label = non_empty[0]
    if label in NON_INDUSTRY_SINGLETONS:
        return False
    if label.startswith("Total "):
        return False
    if any(char.isdigit() for char in label):
        return False
    return True


def extract_official_subtotals(tables, source: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    current_section = ""
    current_industry = ""

    for table_index in range(SCHEDULE_TABLE_START, SCHEDULE_TABLE_END + 1):
        for row_index, table_row in enumerate(tables[table_index].find_all("tr")):
            cells = clean_cells(table_row)
            non_empty = [cell for cell in cells if cell]
            if not non_empty:
                continue

            first = non_empty[0]
            for marker in SECTION_MARKERS:
                if first.startswith(marker):
                    current_section = first
                    current_industry = ""
                    break

            if is_industry_header(non_empty):
                current_industry = first
                continue

            row_text = " ".join(non_empty)
            if "misc. debt commitments" in row_text:
                amortized_cost = value_after_dollar(cells, 1)
                fair_value = value_after_dollar(cells, 2)
                percent = row_percent(cells)
                if fair_value is None:
                    continue
                rows.append(
                    {
                        "claim_id": "CF-004, CF-005",
                        "company": "Blue Owl Capital Corporation",
                        "manager": "Blue Owl",
                        "vehicle": "OBDC",
                        "period": "Q2 2026 / June 30 2026",
                        "investment_section": current_section,
                        "industry": "Misc. debt commitment adjustment",
                        "amortized_cost_usd_thousands": amortized_cost,
                        "fair_value_usd_thousands": fair_value,
                        "fair_value_usd_m": round(fair_value / 1000, 3),
                        "percent_of_net_assets": percent,
                        "source_file": str(source.relative_to(ROOT)),
                        "source_table_index": table_index,
                        "source_row_index": row_index,
                        "source_basis": "Official OBDC schedule miscellaneous debt commitment adjustment row; included to reconcile industry subtotals to total investments fair value.",
                        "status": "official-adjustment-reconciles-to-total-fair-value",
                    }
                )
                continue

            if not current_industry:
                continue

            if cells[0]:
                continue

            fair_value = value_after_dollar(cells, 2)
            amortized_cost = value_after_dollar(cells, 1)
            if fair_value is None or amortized_cost is None:
                continue

            rows.append(
                {
                    "claim_id": "CF-004, CF-005",
                    "company": "Blue Owl Capital Corporation",
                    "manager": "Blue Owl",
                    "vehicle": "OBDC",
                    "period": "Q2 2026 / June 30 2026",
                    "investment_section": current_section,
                    "industry": current_industry,
                    "amortized_cost_usd_thousands": amortized_cost,
                    "fair_value_usd_thousands": fair_value,
                    "fair_value_usd_m": round(fair_value / 1000, 3),
                    "percent_of_net_assets": row_percent(cells),
                    "source_file": str(source.relative_to(ROOT)),
                    "source_table_index": table_index,
                    "source_row_index": row_index,
                    "source_basis": "Official industry subtotal row in OBDC Q2 2026 10-Q schedule of investments; rows are in thousands.",
                    "status": "official-subtotal-reconciles-with-adjustments",
                }
            )
            current_industry = ""

    return rows


def summarize_industries(rows: list[dict[str, object]], source: Path) -> list[dict[str, object]]:
    by_industry: dict[str, dict[str, object]] = {}
    sections_by_industry: defaultdict[str, set[str]] = defaultdict(set)

    for row in rows:
        industry = str(row["industry"])
        if industry == "Misc. debt commitment adjustment":
            continue
        entry = by_industry.setdefault(
            industry,
            {
                "claim_id": "CF-004, CF-005",
                "company": "Blue Owl Capital Corporation",
                "manager": "Blue Owl",
                "vehicle": "OBDC",
                "period": "Q2 2026 / June 30 2026",
                "industry": industry,
                "fair_value_usd_m": 0.0,
                "share_of_total_fair_value_percent": 0.0,
                "percent_of_net_assets_sum": 0.0,
                "sections_seen": "",
                "component_rows": 0,
                "source_file": str(source.relative_to(ROOT)),
                "reconciliation_note": "Aggregates official OBDC industry subtotal rows across non-controlled, affiliated, and controlled sections; misc commitment adjustments are excluded from industry lane ranking.",
                "status": "official-industry-summary-reconciles-to-source-subtotals",
            },
        )
        fair_value = float(row["fair_value_usd_m"])
        entry["fair_value_usd_m"] = float(entry["fair_value_usd_m"]) + fair_value
        if row["percent_of_net_assets"] not in ("", None):
            entry["percent_of_net_assets_sum"] = float(entry["percent_of_net_assets_sum"]) + float(row["percent_of_net_assets"])
        entry["component_rows"] = int(entry["component_rows"]) + 1
        sections_by_industry[industry].add(str(row["investment_section"]))

    for industry, entry in by_industry.items():
        fair_value = float(entry["fair_value_usd_m"])
        entry["fair_value_usd_m"] = round(fair_value, 3)
        entry["share_of_total_fair_value_percent"] = round(fair_value / (REPORTED_TOTAL_FAIR_VALUE_USD_THOUSANDS / 1000) * 100, 2)
        entry["percent_of_net_assets_sum"] = round(float(entry["percent_of_net_assets_sum"]), 2)
        entry["sections_seen"] = "; ".join(sorted(sections_by_industry[industry]))

    return sorted(by_industry.values(), key=lambda row: float(row["fair_value_usd_m"]), reverse=True)


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--subtotals", type=Path, default=DEFAULT_SUBTOTALS)
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY)
    args = parser.parse_args()

    tables = load_tables(args.source)
    rows = extract_official_subtotals(tables, args.source)
    summary = summarize_industries(rows, args.source)
    write_csv(args.subtotals, rows)
    write_csv(args.summary, summary)

    fair_value_total = sum(float(row["fair_value_usd_thousands"]) for row in rows)
    industry_total = sum(float(row["fair_value_usd_m"]) for row in summary)
    adjustment_total = sum(
        float(row["fair_value_usd_m"])
        for row in rows
        if row["industry"] == "Misc. debt commitment adjustment"
    )
    print(f"official_subtotal_rows={len(rows)}")
    print(f"industry_summary_rows={len(summary)}")
    print(f"fair_value_total_usd_m={fair_value_total / 1000:.3f}")
    print(f"industry_total_ex_adjustments_usd_m={industry_total:.3f}")
    print(f"misc_adjustments_usd_m={adjustment_total:.3f}")
    print(f"reconciliation_diff_usd_m={(fair_value_total - REPORTED_TOTAL_FAIR_VALUE_USD_THOUSANDS) / 1000:.6f}")


if __name__ == "__main__":
    main()
