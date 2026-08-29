#!/usr/bin/env python3
"""Build AMAPS source acquisition packet for Athene named cash proof."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
ISSUER_MAP = DATA / "capital-flow-apollo-athene-statutory-safe-cashlike-issuer-borrower-map-pass-1.csv"
PACKET = DATA / "capital-flow-apollo-athene-statutory-safe-cashlike-same-cusip-row-proof-packet-pass-1.csv"
COLUMN_REVIEW = DATA / "capital-flow-apollo-athene-statutory-safe-cashlike-column-review-pass-1.csv"
OUT = DATA / "capital-flow-apollo-athene-amaps-named-cash-source-acquisition-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-apollo-athene-amaps-named-cash-source-acquisition-diagnostic-pass-1.csv"

AMAPS_CUSIP = "02300A-AA-8"

FIELDNAMES = [
    "source_acquisition_id",
    "evidence_layer",
    "source_title",
    "source_url",
    "source_date",
    "source_controller",
    "source_status",
    "extracted_fact",
    "proof_upgrade",
    "cash_movement_read",
    "remaining_gap",
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


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def row_by_cusip(path: Path, cusip: str) -> dict[str, str]:
    for row in read_rows(path):
        if row["cusip"] == cusip:
            return row
    raise KeyError(cusip)


def int_money(value: str) -> str:
    return str(int(float(value)))


def main() -> None:
    issuer = row_by_cusip(ISSUER_MAP, AMAPS_CUSIP)
    packet = row_by_cusip(PACKET, AMAPS_CUSIP)
    column = row_by_cusip(COLUMN_REVIEW, AMAPS_CUSIP)
    rows = [
        {
            "source_acquisition_id": "CFAAAMAPS-001",
            "evidence_layer": "athene-statutory-same-cusip-proceeds",
            "source_title": "Athene statutory Schedule D same-CUSIP packet and column review",
            "source_url": "local Athene statutory Schedule D parser outputs",
            "source_date": "2025",
            "source_controller": "Athene Annuity and Life Company statutory filing",
            "source_status": "local-source-row-visible",
            "extracted_fact": f"Athene same-CUSIP packet shows {packet['cash_like_disposal_consideration_usd']} USD of cash-like disposal consideration, {packet['year_end_book_value_usd']} USD of year-end book value, and {packet['year_end_interest_income_usd']} USD of year-end interest income for AMAPS 1 LLC CUSIP {AMAPS_CUSIP}. Column review supports {column['interpreted_consideration_usd']} USD of consideration and {column['interpreted_interest_or_dividends_received_usd']} USD of disposal interest/dividends for the sparse disposal row.",
            "proof_upgrade": "Athene-side named AMAPS proceeds and interest visible",
            "cash_movement_read": "Athene has same-CUSIP cash-like AMAPS proceeds plus interest/dividend fields at statutory-row level.",
            "remaining_gap": "No Athene trade confirmation, allocation, custodian cash movement, remittance report, or liability-cost spread.",
            "next_action": "Connect the Athene row to AMAPS offering, collateral, waterfall, and allocation records.",
        },
        {
            "source_acquisition_id": "CFAAAMAPS-002",
            "evidence_layer": "apollo-product-definition",
            "source_title": "Introducing AMAPS - a Next-Gen Structured Credit Vehicle",
            "source_url": "https://www.apollo.com/insights-news/insights/2026/05/introducing-amaps",
            "source_date": "2026-05-06",
            "source_controller": "Apollo",
            "source_status": "public-source-found",
            "extracted_fact": "Apollo describes AMAPS as Apollo Multi-Asset Prime Securities, a structured credit product intended to provide diversified, higher-credit-quality assets with less structural leverage than a traditional broadly syndicated loan CLO.",
            "proof_upgrade": "platform wrapper and product thesis visible",
            "cash_movement_read": "AMAPS is an Apollo-created structured credit wrapper for insurance and institutional capital.",
            "remaining_gap": "Product article does not disclose AMAPS 1 collateral tape, noteholder allocation, trustee payments, or borrower-level use.",
            "next_action": "Find AMAPS 1 offering memorandum, tranche supplement, collateral schedule, and trustee reports.",
        },
        {
            "source_acquisition_id": "CFAAAMAPS-003",
            "evidence_layer": "apollo-product-collateral-route",
            "source_title": "Introducing AMAPS - a Next-Gen Structured Credit Vehicle",
            "source_url": "https://www.apollo.com/insights-news/insights/2026/05/introducing-amaps",
            "source_date": "2026-05-06",
            "source_controller": "Apollo",
            "source_status": "public-source-found",
            "extracted_fact": "Apollo says AMAPS has diversified corporate and asset-backed credit collateral, approximately 45-50% investment-grade collateral, about 9x debt/equity leverage, and 600-plus obligors in its comparison chart.",
            "proof_upgrade": "collateral-type and diversification route visible",
            "cash_movement_read": "The public collateral route points to pooled corporate and asset-backed credit rather than a single operating borrower.",
            "remaining_gap": "No underlying obligor list, collateral balances, asset marks, cash collections, or loan-level use of proceeds.",
            "next_action": "Acquire collateral tape or full rating report to identify underlying obligors and asset categories.",
        },
        {
            "source_acquisition_id": "CFAAAMAPS-004",
            "evidence_layer": "apollo-athene-investor-alignment",
            "source_title": "Introducing AMAPS - a Next-Gen Structured Credit Vehicle",
            "source_url": "https://www.apollo.com/insights-news/insights/2026/05/introducing-amaps",
            "source_date": "2026-05-06",
            "source_controller": "Apollo",
            "source_status": "public-source-found",
            "extracted_fact": "Apollo says AMAPS was built to address Athene's need for higher-quality collateral and safe yield, and says Apollo or Athene is a significant investor in each underlying AMAPS tranche.",
            "proof_upgrade": "Apollo/Athene strategic alignment visible",
            "cash_movement_read": "Public Apollo text supports why Athene would hold AMAPS, but not the exact Athene legal-entity allocation or trade path.",
            "remaining_gap": "No AMAPS 1 tranche ownership schedule or Athene-specific allocation.",
            "next_action": "Request AMAPS investor allocation and Athene investment accounting/custodian records.",
        },
        {
            "source_acquisition_id": "CFAAAMAPS-005",
            "evidence_layer": "athene-consolidated-disclosure",
            "source_title": "Apollo/Athene Investments disclosure",
            "source_url": "https://www.sec.gov/Archives/edgar/data/1527469/000152746926000013/R12.htm",
            "source_date": "2026 filing for 2025 period",
            "source_controller": "Apollo/Athene SEC filing",
            "source_status": "public-source-found",
            "extracted_fact": "Apollo/Athene investment disclosure lists investment-grade ABS debt issued by AMAPS 1, LLC at 2.550B USD as a concentration above 10% of AHL stockholders' equity at December 31, 2025.",
            "proof_upgrade": "public consolidated AMAPS 1 exposure visible",
            "cash_movement_read": "AMAPS 1 is a named material Athene/Apollo insurance investment exposure, not just a statutory Schedule D row.",
            "remaining_gap": "Consolidated disclosure does not provide CUSIP-level statutory entity allocation, cash receipts, collateral, or return.",
            "next_action": "Reconcile consolidated AMAPS 1 exposure with Athene statutory legal-entity rows and other Athene subsidiaries.",
        },
        {
            "source_acquisition_id": "CFAAAMAPS-006",
            "evidence_layer": "rating-analog-structure",
            "source_title": "KBRA AMAPS 5 preliminary/final rating releases",
            "source_url": "https://www.kbra.com/publications/KDBMTzJQ; https://www.kbra.com/publications/MSzqKhYx",
            "source_date": "2026-06",
            "source_controller": "KBRA",
            "source_status": "public-analog-source-found",
            "extracted_fact": "KBRA describes AMAPS 5 as Apollo's multi-asset investment strategy with exposure to corporate credit, asset-backed finance, private and broadly syndicated lending, and opportunistic investments; at issuance, look-through exposure was expected to include more than 500 obligors and eventual deployment about 750-1,000 obligors.",
            "proof_upgrade": "AMAPS structure analog visible",
            "cash_movement_read": "Later AMAPS public rating releases show the type of collateral and obligor diversification the AMAPS format can contain.",
            "remaining_gap": "This is AMAPS 5, not AMAPS 1; it cannot prove AMAPS 1 collateral or cash flows.",
            "next_action": "Locate AMAPS 1-specific rating reports, offering memorandum, or private placement documents.",
        },
        {
            "source_acquisition_id": "CFAAAMAPS-007",
            "evidence_layer": "private-letter-rating-context",
            "source_title": "S&P Global Market Intelligence private letter rated bonds article",
            "source_url": "https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/01/holdings-scrutiny-of-private-letter-rated-bonds-continue-to-climb",
            "source_date": "2026-01-13",
            "source_controller": "S&P Global Market Intelligence",
            "source_status": "public-source-found",
            "extracted_fact": "S&P Global Market Intelligence identifies Athene's large private-letter-rated bond holdings as including investment-grade ABS debt issued by AP Grange, AMAPS 1 LLC, and Fox Hedge, and says Athene classified AMAPS 1 as equity-backed under the NAIC issuer-type framework.",
            "proof_upgrade": "regulatory/rating opacity context visible",
            "cash_movement_read": "AMAPS 1 sits in the insurer private-letter-rated ABS bond debate, which explains why collateral and rating rationale may be less public.",
            "remaining_gap": "Article does not provide AMAPS 1 collateral tape, rating rationale report, or Athene cash receipt.",
            "next_action": "Request private rating rationale report or SVO/NAIC filing support where available.",
        },
        {
            "source_acquisition_id": "CFAAAMAPS-008",
            "evidence_layer": "legal-entity-identifier",
            "source_title": "Bloomberg LEI AMAPS 1 LLC",
            "source_url": "https://lei.bloomberg.com/leis/view/254900LXAEJYTU2O1J86",
            "source_date": "current registry view",
            "source_controller": "Bloomberg LEI / GLEIF registry route",
            "source_status": "public-source-found",
            "extracted_fact": "AMAPS 1 LLC has an LEI and Delaware legal address record, supporting legal-entity identification for document requests.",
            "proof_upgrade": "legal entity request target visible",
            "cash_movement_read": "This helps identify the exact SPV/entity for requests, but carries no cash-flow evidence.",
            "remaining_gap": "No ownership, collateral, noteholder, remittance, or return evidence.",
            "next_action": "Use LEI/legal entity identity in document and rating-report requests.",
        },
        {
            "source_acquisition_id": "CFAAAMAPS-009",
            "evidence_layer": "next-proof-requirements",
            "source_title": "AMAPS named-cash proof requirements",
            "source_url": "derived from current source gaps",
            "source_date": "current",
            "source_controller": "research control",
            "source_status": "request-package-defined",
            "extracted_fact": "The decisive missing package is AMAPS 1 offering memorandum, tranche supplement, rating rationale reports, collateral tape, trustee/remittance reports, Apollo/Athene allocation records, statutory subsidiary reconciliation, and liability-cost/spread support.",
            "proof_upgrade": "controlled-document request defined",
            "cash_movement_read": "The public route is strong enough for wrapper identity and collateral category, but not for borrower receipts or asset-level return.",
            "remaining_gap": "Controlled/private documents likely required for full named cash proof.",
            "next_action": "Build AMAPS 1 controlled-document request packet and prioritize AMAPS 1-specific rating and collateral documents.",
        },
    ]

    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    diagnostics = [
        ("source_acquisition_rows", "9", "count"),
        ("public_sources_found", "6", "count"),
        ("public_analog_sources_found", "1", "count"),
        ("local_athene_row_sources", "1", "count"),
        ("request_package_rows", "1", "count"),
        ("athene_amaps_cash_like_consideration", int_money(packet["cash_like_disposal_consideration_usd"]), "USD"),
        ("athene_amaps_year_end_book_value", int_money(packet["year_end_book_value_usd"]), "USD"),
        ("athene_amaps_year_end_interest_income", int_money(packet["year_end_interest_income_usd"]), "USD"),
        ("athene_amaps_disposal_interest_or_dividends", int_money(packet["disposal_interest_or_dividends_received_usd"]), "USD"),
        ("apollo_athene_amaps1_public_concentration", "2550000000", "USD"),
        ("mapping_status", issuer["mapping_status"], "status"),
    ]
    with DIAGNOSTIC_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DIAGNOSTIC_FIELDS)
        writer.writeheader()
        for idx, (metric, value, units) in enumerate(diagnostics, start=1):
            writer.writerow(
                {
                    "diagnostic_id": f"CFAAAMAPSD-{idx:03d}",
                    "metric": metric,
                    "value": value,
                    "units": units,
                    "proof_use": "controls AMAPS named-cash source acquisition status",
                    "boundary": "diagnostic combines local Athene statutory evidence with public AMAPS wrapper evidence; not AMAPS 1 collateral, remittance, liability spread, or return proof",
                    "next_action": "build AMAPS controlled-document request packet and pursue AMAPS 1-specific rating/collateral/remittance/allocation support",
                }
            )

    print(f"wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT.relative_to(ROOT)}")
    print(issuer["mapping_status"])


if __name__ == "__main__":
    main()
