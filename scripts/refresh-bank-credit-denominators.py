#!/usr/bin/env python3
"""Refresh FRED bank-credit denominators and derived trend/comparison tables."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "raw/primary-sources/capital-flow/market-denominators/fred"
DATA_DIR = ROOT / "analysis/company-first-principles/data"
DENOMINATOR_OUTPUT = DATA_DIR / "capital-flow-bank-denominator-extractions.csv"
TREND_OUTPUT = DATA_DIR / "capital-flow-bank-credit-trends.csv"
COMPARISON_OUTPUT = DATA_DIR / "capital-flow-private-credit-bank-denominator-comparison.csv"

SERIES = [
    {
        "source_id": "fred-busloans",
        "series_id": "BUSLOANS",
        "series_name": "Commercial and Industrial Loans, All Commercial Banks",
        "units": "B USD",
        "frequency_adjustment": "monthly seasonally adjusted",
        "filename": "busloans.csv",
        "claim_use": "C&I bank-loan stock denominator for CF-005.",
    },
    {
        "source_id": "fred-totll",
        "series_id": "TOTLL",
        "series_name": "Loans and Leases in Bank Credit, All Commercial Banks",
        "units": "B USD",
        "frequency_adjustment": "weekly seasonally adjusted",
        "filename": "totll.csv",
        "claim_use": "Broad loans-and-leases denominator for CF-005.",
    },
    {
        "source_id": "fred-totbkcr",
        "series_id": "TOTBKCR",
        "series_name": "Bank Credit, All Commercial Banks",
        "units": "B USD",
        "frequency_adjustment": "weekly seasonally adjusted",
        "filename": "totbkcr.csv",
        "claim_use": "Broad bank-credit denominator for capital-routing comparison.",
    },
    {
        "source_id": "fred-creacbm",
        "series_id": "CREACBM027NBOG",
        "series_name": "Commercial Real Estate Loans, All Commercial Banks",
        "units": "B USD",
        "frequency_adjustment": "monthly not seasonally adjusted",
        "filename": "creacbm027nbog.csv",
        "claim_use": "CRE denominator for real-estate credit and infrastructure-adjacent claims.",
    },
]

PRIVATE_CREDIT_METRICS = [
    ("CF-004", "Apollo", "LTM 2Q 2026", "originations", 317.0, "B USD", "flow"),
    ("CF-004", "Apollo", "Q2 2026", "originations", 74.0, "B USD", "flow"),
    ("CF-004", "Apollo", "Q2 2026", "gross capital deployment", 111.0, "B USD", "flow"),
    ("CF-005", "Ares", "Q2 2026", "credit group AUM", 440.5, "B USD", "stock"),
    ("CF-005", "Ares", "Q2 2026", "credit group FPAUM", 266.1, "B USD", "stock"),
    ("CF-005", "Ares", "Q2 2026", "available capital", 170.0, "B USD", "stock/capacity"),
    ("CF-005", "Ares", "Q2 2026", "credit group capital deployment", 23.7, "B USD", "flow"),
    ("CF-005", "Ares", "Q2 2026", "U.S. direct lending deployment", 12.4, "B USD", "flow"),
]


def download_series(series_id: str, destination: Path) -> None:
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    request = urllib.request.Request(url, headers={"User-Agent": "annual-report-research/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        destination.write_bytes(response.read())


def read_series(path: Path) -> list[tuple[dt.date, float]]:
    with path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    parsed = []
    for row in rows:
        value = row[next(key for key in row if key != "observation_date")]
        if value in {"", "."}:
            continue
        parsed.append((dt.date.fromisoformat(row["observation_date"]), float(value)))
    return parsed


def latest_at_or_before(rows: list[tuple[dt.date, float]], target: dt.date) -> tuple[dt.date, float]:
    candidates = [row for row in rows if row[0] <= target]
    if not candidates:
        raise ValueError(f"No FRED row at or before {target}")
    return candidates[-1]


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def pct(value: float, denominator: float) -> float:
    return round(value / denominator * 100, 2)


def build_tables(download: bool) -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    latest_by_series: dict[str, tuple[dt.date, float]] = {}
    series_rows: dict[str, list[tuple[dt.date, float]]] = {}

    for series in SERIES:
        path = RAW_DIR / str(series["filename"])
        if download:
            download_series(str(series["series_id"]), path)
        rows = read_series(path)
        series_rows[str(series["series_id"])] = rows
        latest_by_series[str(series["series_id"])] = rows[-1]

    denominator_rows = []
    for series in SERIES:
        series_id = str(series["series_id"])
        latest_date, latest_value = latest_by_series[series_id]
        denominator_rows.append(
            {
                "source_id": series["source_id"],
                "series_id": series_id,
                "series_name": series["series_name"],
                "latest_date": latest_date.isoformat(),
                "metric_value": f"{latest_value:.4f}",
                "units": series["units"],
                "frequency_adjustment": series["frequency_adjustment"],
                "local_path": str((RAW_DIR / str(series["filename"])).relative_to(ROOT)),
                "source_location": "latest row",
                "source_basis": "Federal Reserve H.8 via FRED",
                "claim_use": series["claim_use"],
            }
        )

    trend_rows = []
    for series in SERIES:
        series_id = str(series["series_id"])
        latest_date, latest_value = latest_by_series[series_id]
        rows = series_rows[series_id]
        trend = {
            "series_id": series_id,
            "series_name": series["series_name"],
            "latest_date": latest_date.isoformat(),
            "latest_value_b_usd": f"{latest_value:.4f}",
            "local_path": str((RAW_DIR / str(series["filename"])).relative_to(ROOT)),
            "status": "trend-computed-local-source",
        }
        for years, label in [(1, "one_year"), (3, "three_year"), (5, "five_year")]:
            prior_date, prior_value = latest_at_or_before(rows, latest_date - dt.timedelta(days=365 * years))
            change = latest_value - prior_value
            trend[f"{label}_prior_date"] = prior_date.isoformat()
            trend[f"{label}_prior_value_b_usd"] = f"{prior_value:.4f}"
            trend[f"{label}_change_b_usd"] = f"{change:.4f}"
            trend[f"{label}_change_pct"] = f"{pct(change, prior_value):.2f}"
        trend_rows.append(trend)

    denominators = {series_id.lower(): value for series_id, (_, value) in latest_by_series.items()}
    comparison_rows = []
    for claim_id, company, period, metric, value, units, metric_type in PRIVATE_CREDIT_METRICS:
        comparison_rows.append(
            {
                "claim_id": claim_id,
                "company": company,
                "period": period,
                "private_credit_metric": metric,
                "private_credit_value": f"{value:.1f}",
                "units": units,
                "metric_type": metric_type,
                "vs_busloans_pct": f"{pct(value, denominators['busloans']):.2f}",
                "vs_totll_pct": f"{pct(value, denominators['totll']):.2f}",
                "vs_totbkcr_pct": f"{pct(value, denominators['totbkcr']):.2f}",
                "vs_creacbm_pct": f"{pct(value, denominators['creacbm027nbog']):.2f}",
                "interpretation": f"{company} {metric} is {pct(value, denominators['busloans']):.2f} percent of latest C&I bank-loan stock; this is a scale comparison, not displacement proof.",
                "status": "denominator-comparison-local-source",
            }
        )

    write_csv(
        DENOMINATOR_OUTPUT,
        denominator_rows,
        ["source_id", "series_id", "series_name", "latest_date", "metric_value", "units", "frequency_adjustment", "local_path", "source_location", "source_basis", "claim_use"],
    )
    write_csv(
        TREND_OUTPUT,
        trend_rows,
        [
            "series_id",
            "series_name",
            "latest_date",
            "latest_value_b_usd",
            "one_year_prior_date",
            "one_year_prior_value_b_usd",
            "one_year_change_b_usd",
            "one_year_change_pct",
            "three_year_prior_date",
            "three_year_prior_value_b_usd",
            "three_year_change_b_usd",
            "three_year_change_pct",
            "five_year_prior_date",
            "five_year_prior_value_b_usd",
            "five_year_change_b_usd",
            "five_year_change_pct",
            "local_path",
            "status",
        ],
    )
    write_csv(
        COMPARISON_OUTPUT,
        comparison_rows,
        ["claim_id", "company", "period", "private_credit_metric", "private_credit_value", "units", "metric_type", "vs_busloans_pct", "vs_totll_pct", "vs_totbkcr_pct", "vs_creacbm_pct", "interpretation", "status"],
    )

    for row in denominator_rows:
        print(f"{row['series_id']}: {row['latest_date']} {row['metric_value']} {row['units']}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-download", action="store_true", help="Use existing local FRED CSV files without refreshing them.")
    args = parser.parse_args()
    build_tables(download=not args.no_download)


if __name__ == "__main__":
    main()
