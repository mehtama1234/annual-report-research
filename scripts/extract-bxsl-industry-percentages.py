#!/usr/bin/env python3
"""Extract BXSL Q2 2026 official industry percentages from the 10-Q."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "raw/primary-sources/capital-flow/blackstone-secured-lending-fund/q2-2026/bxsl-2026-q2-10q.html"
DATA_DIR = ROOT / "analysis/company-first-principles/data"
DEFAULT_OUTPUT = DATA_DIR / "capital-flow-bxsl-official-industry-percentages.csv"

REPORTED_TOTAL_FAIR_VALUE_USD_M = 13_364.295
INDUSTRY_TABLES = (106, 107)


def clean_label(value: str) -> str:
    value = " ".join(value.split())
    return re.sub(r"\s*\([^)]*\)", "", value).strip()


def parse_percent(value: str) -> float | None:
    text = value.replace("%", "").replace(",", "").strip()
    if text in {"", "—"}:
        return 0.0
    try:
        return float(text)
    except ValueError:
        return None


def clean_cells(row) -> list[str]:
    return [" ".join(cell.get_text(" ", strip=True).split()) for cell in row.find_all(["td", "th"])]


def extract_rows(source: Path) -> list[dict[str, object]]:
    soup = BeautifulSoup(source.read_text(errors="ignore"), "html.parser")
    tables = soup.find_all("table")
    rows: list[dict[str, object]] = []

    for table_index in INDUSTRY_TABLES:
        for row_index, table_row in enumerate(tables[table_index].find_all("tr")):
            cells = clean_cells(table_row)
            non_empty = [cell for cell in cells if cell]
            if len(non_empty) < 2:
                continue

            industry = clean_label(non_empty[0])
            if industry in {"", "June 30, 2026", "Total"}:
                continue

            percent = parse_percent(non_empty[1])
            if percent is None:
                continue

            rows.append(
                {
                    "claim_id": "CF-004, CF-005",
                    "company": "Blackstone Secured Lending Fund",
                    "manager": "Blackstone",
                    "vehicle": "BXSL",
                    "period": "Q2 2026 / June 30 2026",
                    "industry": industry,
                    "fair_value_usd_m": round(REPORTED_TOTAL_FAIR_VALUE_USD_M * percent / 100, 3),
                    "share_of_total_fair_value_percent": percent,
                    "portfolio_base_usd_m": REPORTED_TOTAL_FAIR_VALUE_USD_M,
                    "source_file": str(source.relative_to(ROOT)),
                    "source_table_index": table_index,
                    "source_row_index": row_index,
                    "source_basis": "Official BXSL 10-Q industry table reports percentage of total investments at fair value; fair value dollars are calculated from filed total investments at fair value.",
                    "status": "official-industry-percentage-converted-to-fair-value",
                }
            )

    return sorted(rows, key=lambda row: float(row["fair_value_usd_m"]), reverse=True)


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    rows = extract_rows(args.source)
    write_csv(args.output, rows)

    percent_total = sum(float(row["share_of_total_fair_value_percent"]) for row in rows)
    fair_value_total = sum(float(row["fair_value_usd_m"]) for row in rows)
    print(f"bxsl_industry_rows={len(rows)}")
    print(f"percent_total={percent_total:.1f}")
    print(f"fair_value_total_usd_m={fair_value_total:.3f}")
    print(f"reported_total_fair_value_usd_m={REPORTED_TOTAL_FAIR_VALUE_USD_M:.3f}")
    print(f"reconciliation_delta_usd_m={fair_value_total - REPORTED_TOTAL_FAIR_VALUE_USD_M:.3f}")
    for row in rows[:10]:
        print(f"{row['industry']}: {row['fair_value_usd_m']}M ({row['share_of_total_fair_value_percent']}%)")


if __name__ == "__main__":
    main()
