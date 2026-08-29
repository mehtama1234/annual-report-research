#!/usr/bin/env python3
"""Build the normalized ARCC/OBDC/BXSL industry-lane comparison."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "analysis/company-first-principles/data"
ARCC_SOURCE = DATA_DIR / "capital-flow-arcc-official-industry-subtotals.csv"
OBDC_SOURCE = DATA_DIR / "capital-flow-obdc-industry-summary.csv"
BXSL_SOURCE = DATA_DIR / "capital-flow-bxsl-official-industry-percentages.csv"
CROSS_SOURCE = DATA_DIR / "capital-flow-cross-bdc-industry-lane-comparison.csv"
CROSS_OUTPUT = CROSS_SOURCE

ARCC_PORTFOLIO_BASE_USD_M = 29_349.3
OBDC_PORTFOLIO_BASE_USD_M = 14_955.049
BXSL_PORTFOLIO_BASE_USD_M = 13_364.295

FIELDNAMES = [
    "claim_id",
    "manager",
    "vehicle",
    "company",
    "period",
    "normalized_lane",
    "reported_lane",
    "exposure_value_usd_m",
    "exposure_percent_of_portfolio",
    "portfolio_base_usd_m",
    "measurement_basis",
    "source_file",
    "confidence",
    "status",
    "interpretation",
]


NORMALIZED_LANES = {
    "Advertising and media": "Sports, Media and Entertainment",
    "Air Freight & Logistics": "Transportation",
    "Aerospace and defense": "Capital Goods",
    "Aerospace & Defense": "Capital Goods",
    "Automobile Components": "Automobiles and Components",
    "Asset based lending and fund finance": "Financial Services",
    "Automotive services": "Consumer Services",
    "Building Products": "Capital Goods",
    "Buildings and real estate": "Real Estate Management and Development",
    "Business services": "Commercial and Professional Services",
    "Chemicals": "Materials",
    "Commercial Services & Supplies": "Commercial and Professional Services",
    "Construction and engineering": "Capital Goods",
    "Construction & Engineering": "Capital Goods",
    "Consumer products": "Consumer Distribution and Retail",
    "Consumer Staples Distribution & Retail": "Consumer Distribution and Retail",
    "Containers and packaging": "Materials",
    "Containers & Packaging": "Materials",
    "Distribution": "Transportation",
    "Distributors": "Transportation",
    "Diversified Consumer Services": "Consumer Services",
    "Diversified Telecommunication Services": "Telecommunication Services",
    "Electric Utilities": "Utilities",
    "Electrical Equipment": "Capital Goods",
    "Electronic Equipment, Instruments & Components": "Technology Hardware and Equipment",
    "Energy equipment and services": "Energy",
    "Energy Equipment & Services": "Energy",
    "Financial services": "Financial Services",
    "Food and beverage": "Food and Beverage",
    "Ground Transportation": "Transportation",
    "Health Care Equipment & Supplies": "Health Care Equipment and Services",
    "Healthcare equipment and services": "Health Care Equipment and Services",
    "Healthcare providers and services": "Health Care Equipment and Services",
    "Healthcare technology": "Health Care Equipment and Services",
    "Health Care Providers & Services": "Health Care Equipment and Services",
    "Health Care Technology": "Health Care Equipment and Services",
    "Interactive Media & Services": "Sports, Media and Entertainment",
    "Household products": "Household and Personal Products",
    "Human resource support services": "Commercial and Professional Services",
    "Infrastructure and environmental services": "Commercial and Professional Services",
    "Internet software and services": "Software and Services",
    "IT Services": "Software and Services",
    "Leisure and entertainment": "Consumer Services",
    "Life Sciences Tools & Services": "Pharmaceuticals, Biotechnology and Life Sciences",
    "Machinery": "Capital Goods",
    "Marine Transportation": "Transportation",
    "Media": "Sports, Media and Entertainment",
    "Manufacturing": "Capital Goods",
    "Oil, Gas & Consumable Fuels": "Energy",
    "Paper & Forest Products": "Materials",
    "Pharmaceuticals": "Pharmaceuticals, Biotechnology and Life Sciences",
    "Professional services": "Commercial and Professional Services",
    "Professional Services": "Commercial and Professional Services",
    "Software": "Software and Services",
    "Specialty retail": "Consumer Distribution and Retail",
    "Specialty Retail": "Consumer Distribution and Retail",
    "Technology Hardware, Storage & Peripherals": "Technology Hardware and Equipment",
    "Telecommunications": "Telecommunication Services",
    "Trading Companies & Distributors": "Transportation",
    "Transportation Infrastructure": "Transportation",
    "Wireless Telecommunication Services": "Telecommunication Services",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def normalize(lane: str) -> str:
    return NORMALIZED_LANES.get(lane, lane)


def base_row(
    *,
    claim_id: str,
    manager: str,
    vehicle: str,
    company: str,
    period: str,
    normalized_lane: str,
    reported_lane: str,
    exposure_value_usd_m: float,
    exposure_percent_of_portfolio: float | str,
    portfolio_base_usd_m: float,
    measurement_basis: str,
    source_file: str,
    confidence: str,
    status: str,
    interpretation: str,
) -> dict[str, object]:
    return {
        "claim_id": claim_id,
        "manager": manager,
        "vehicle": vehicle,
        "company": company,
        "period": period,
        "normalized_lane": normalized_lane,
        "reported_lane": reported_lane,
        "exposure_value_usd_m": round(exposure_value_usd_m, 3),
        "exposure_percent_of_portfolio": exposure_percent_of_portfolio,
        "portfolio_base_usd_m": round(portfolio_base_usd_m, 3),
        "measurement_basis": measurement_basis,
        "source_file": source_file,
        "confidence": confidence,
        "status": status,
        "interpretation": interpretation,
    }


def build_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    for row in read_csv(ARCC_SOURCE):
        fair_value = float(row["fair_value_usd_m"])
        rows.append(
            base_row(
                claim_id=row["claim_id"],
                manager=row["manager"],
                vehicle=row["vehicle"],
                company=row["company"],
                period=row["period"],
                normalized_lane=normalize(row["industry"]),
                reported_lane=row["industry"],
                exposure_value_usd_m=fair_value,
                exposure_percent_of_portfolio=float(row["share_of_total_fair_value_percent"]),
                portfolio_base_usd_m=ARCC_PORTFOLIO_BASE_USD_M,
                measurement_basis="official industry subtotal fair value",
                source_file=row["source_file"],
                confidence="high",
                status=row["status"],
                interpretation="ARCC official schedule subtotal; use as primary evidence for Ares-managed BDC industry destination.",
            )
        )

    for row in read_csv(OBDC_SOURCE):
        fair_value = float(row["fair_value_usd_m"])
        rows.append(
            base_row(
                claim_id=row["claim_id"],
                manager=row["manager"],
                vehicle=row["vehicle"],
                company=row["company"],
                period=row["period"],
                normalized_lane=normalize(row["industry"]),
                reported_lane=row["industry"],
                exposure_value_usd_m=fair_value,
                exposure_percent_of_portfolio=float(row["share_of_total_fair_value_percent"]),
                portfolio_base_usd_m=OBDC_PORTFOLIO_BASE_USD_M,
                measurement_basis="official industry subtotal fair value",
                source_file=row["source_file"],
                confidence="high",
                status=row["status"],
                interpretation="OBDC official schedule subtotal; use as primary evidence for Blue Owl-managed BDC industry destination.",
            )
        )

    for row in read_csv(BXSL_SOURCE):
        fair_value = float(row["fair_value_usd_m"])
        rows.append(
            base_row(
                claim_id=row["claim_id"],
                manager=row["manager"],
                vehicle=row["vehicle"],
                company=row["company"],
                period=row["period"],
                normalized_lane=normalize(row["industry"]),
                reported_lane=row["industry"],
                exposure_value_usd_m=fair_value,
                exposure_percent_of_portfolio=float(row["share_of_total_fair_value_percent"]),
                portfolio_base_usd_m=BXSL_PORTFOLIO_BASE_USD_M,
                measurement_basis="official industry percentage converted to fair value",
                source_file=row["source_file"],
                confidence="medium-high",
                status=row["status"],
                interpretation="BXSL official 10-Q industry percentage converted to dollars using filed total investments fair value.",
            )
        )

    aggregate: defaultdict[str, float] = defaultdict(float)
    for row in rows:
        aggregate[str(row["normalized_lane"])] += float(row["exposure_value_usd_m"])

    aggregate_base = ARCC_PORTFOLIO_BASE_USD_M + OBDC_PORTFOLIO_BASE_USD_M + BXSL_PORTFOLIO_BASE_USD_M
    for lane, value in sorted(aggregate.items(), key=lambda item: item[1], reverse=True):
        rows.append(
            base_row(
                claim_id="CF-004, CF-005",
                manager="cross-manager",
                vehicle="ARCC + OBDC + BXSL",
                company="Ares Capital Corporation + Blue Owl Capital Corporation + Blackstone Secured Lending Fund",
                period="Q2 2026 / June 30 2026",
                normalized_lane=lane,
                reported_lane="aggregate normalized lane",
                exposure_value_usd_m=value,
                exposure_percent_of_portfolio="",
                portfolio_base_usd_m=aggregate_base,
                measurement_basis="ARCC and OBDC official fair value plus BXSL official industry percentages converted to fair value",
                source_file="analysis/company-first-principles/data/capital-flow-arcc-official-industry-subtotals.csv; analysis/company-first-principles/data/capital-flow-obdc-industry-summary.csv; analysis/company-first-principles/data/capital-flow-bxsl-official-industry-percentages.csv",
                confidence="high for ARCC/OBDC exact fair values; medium-high for BXSL percentage-derived fair values",
                status="cross-bdc-aggregate-uses-official-source-values-and-official-percentage-derived-values",
                interpretation="Cross-BDC lane comparison using official ARCC and OBDC fair-value subtotals plus BXSL filed industry percentages converted to dollars.",
            )
        )

    return rows


def main() -> None:
    rows = build_rows()
    with CROSS_OUTPUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    aggregates = [row for row in rows if row["vehicle"] == "ARCC + OBDC + BXSL"]
    print(f"cross_bdc_rows={len(rows)}")
    print(f"aggregate_lanes={len(aggregates)}")
    for row in aggregates[:10]:
        print(f"{row['normalized_lane']}: {float(row['exposure_value_usd_m']) / 1000:.3f}B")


if __name__ == "__main__":
    main()
