#!/usr/bin/env python3
"""Build Concord source acquisition packet for Athene named cash proof."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
ISSUER_MAP = DATA / "capital-flow-apollo-athene-statutory-safe-cashlike-issuer-borrower-map-pass-1.csv"
PACKET = DATA / "capital-flow-apollo-athene-statutory-safe-cashlike-same-cusip-row-proof-packet-pass-1.csv"
OUT = DATA / "capital-flow-apollo-athene-concord-named-cash-source-acquisition-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-apollo-athene-concord-named-cash-source-acquisition-diagnostic-pass-1.csv"

CONCORD_CUSIP = "20633K-AN-8"

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


def main() -> None:
    issuer = row_by_cusip(ISSUER_MAP, CONCORD_CUSIP)
    packet = row_by_cusip(PACKET, CONCORD_CUSIP)
    rows = [
        {
            "source_acquisition_id": "CFAACNCSP-001",
            "evidence_layer": "athene-statutory-same-cusip-proceeds",
            "source_title": "Athene statutory Schedule D same-CUSIP packet",
            "source_url": "local Athene statutory Schedule D parser outputs",
            "source_date": "2025",
            "source_controller": "Athene Annuity and Life Company statutory filing",
            "source_status": "local-source-row-visible",
            "extracted_fact": f"Athene same-CUSIP packet shows {packet['cash_like_disposal_consideration_usd']} USD of cash-like disposal consideration for Concord Music Royalties CUSIP {CONCORD_CUSIP}, with {packet['year_end_book_value_usd']} USD of year-end book value.",
            "proof_upgrade": "Athene-side named proceeds visible",
            "cash_movement_read": "Athene held and had cash-like proceeds activity for a named Concord Music Royalties ABS note.",
            "remaining_gap": "No Athene trade confirmation, allocation, trustee remittance, or liability-cost spread.",
            "next_action": "Connect the Athene CUSIP row to Concord transaction documents and trustee/remittance evidence.",
        },
        {
            "source_acquisition_id": "CFAACNCSP-002",
            "evidence_layer": "issuer-closing-and-collateral",
            "source_title": "Concord Closes $1.765 Billion ABS to Fuel Continued Growth",
            "source_url": "https://concord.com/news/concord-closes-1-765-billion-abs-to-fuel-continued-growth/",
            "source_date": "2025-07-22",
            "source_controller": "Concord",
            "source_status": "public-source-found",
            "extracted_fact": "Concord announced 1.765B USD of five-year, seven-year, and ten-year senior notes secured by a catalog of more than 1.3 million music copyrights.",
            "proof_upgrade": "borrower/wrapper issuance and collateral pool visible",
            "cash_movement_read": "The issuer-side financing wrapper is a music royalty ABS backed by Concord catalog assets.",
            "remaining_gap": "Announcement does not identify Athene as buyer or show noteholder remittance.",
            "next_action": "Acquire indenture, offering memorandum, trustee report, and investor distribution records.",
        },
        {
            "source_acquisition_id": "CFAACNCSP-003",
            "evidence_layer": "apollo-structuring-role",
            "source_title": "Concord Closes $1.765 Billion ABS to Fuel Continued Growth",
            "source_url": "https://concord.com/news/concord-closes-1-765-billion-abs-to-fuel-continued-growth/",
            "source_date": "2025-07-22",
            "source_controller": "Concord",
            "source_status": "public-source-found",
            "extracted_fact": "Concord says Apollo, through Capital Solutions and affiliates ATLAS SP Partners and Redding Ridge Asset Management, structured the ABS transaction and formed an investor syndicate led by Apollo-managed funds and affiliates.",
            "proof_upgrade": "Apollo transaction routing role visible",
            "cash_movement_read": "Apollo was not just a passive name; public issuer text puts Apollo and affiliates in structuring/syndication roles.",
            "remaining_gap": "Does not prove Athene allocation or Apollo-managed-fund purchase amount by CUSIP.",
            "next_action": "Find allocation books, investor lists, or statutory/NAIC/private-placement records tying Athene to the tranche.",
        },
        {
            "source_acquisition_id": "CFAACNCSP-004",
            "evidence_layer": "use-of-proceeds",
            "source_title": "Concord Closes $1.765 Billion ABS to Fuel Continued Growth",
            "source_url": "https://concord.com/news/concord-closes-1-765-billion-abs-to-fuel-continued-growth/",
            "source_date": "2025-07-22",
            "source_controller": "Concord",
            "source_status": "public-source-found",
            "extracted_fact": "Concord says proceeds will repay the company's 1.65B USD 2022-1 note series and refinance and extend its 100M USD variable funding note.",
            "proof_upgrade": "issuer-side use-of-proceeds proxy visible",
            "cash_movement_read": "The transaction proceeds route primarily into debt refinancing rather than a currently proven operating capex or acquisition spend.",
            "remaining_gap": "No trustee payoff ledger, note redemption cash movement, or remaining proceeds allocation.",
            "next_action": "Acquire redemption notice, trustee payoff statement, VFN amendment, and cash waterfall report.",
        },
        {
            "source_acquisition_id": "CFAACNCSP-005",
            "evidence_layer": "rating-agency-transaction-structure",
            "source_title": "KBRA Assigns Ratings to Concord Music Royalties, LLC, Series 2025-1, Series 2025-2, and Series 2025-3",
            "source_url": "https://www.kbra.com/publications/bcGzRKWf",
            "source_date": "2025-07-21",
            "source_controller": "KBRA",
            "source_status": "public-source-found",
            "extracted_fact": "KBRA says the Series 2025-1, 2025-2, and 2025-3 notes are the fourth, fifth, and sixth series issued by Concord Music Royalties, all series share the same collateral pool, and no additional collateral is contributed with the 2025 issuance.",
            "proof_upgrade": "series/trust collateral structure visible",
            "cash_movement_read": "The financing appears to sit inside an existing music royalty securitization platform sharing one collateral pool.",
            "remaining_gap": "No collateral tape, tranche waterfall, or noteholder distribution schedule.",
            "next_action": "Acquire KBRA full report, indenture amendment, collateral pool data, and trustee reports.",
        },
        {
            "source_acquisition_id": "CFAACNCSP-006",
            "evidence_layer": "rating-agency-use-of-proceeds",
            "source_title": "KBRA Assigns Ratings to Concord Music Royalties, LLC, Series 2025-1, Series 2025-2, and Series 2025-3",
            "source_url": "https://www.kbra.com/publications/bcGzRKWf",
            "source_date": "2025-07-21",
            "source_controller": "KBRA",
            "source_status": "public-source-found",
            "extracted_fact": "KBRA says Series 2025 proceeds will fully redeem the 1.750B USD Series 2022-1 notes outstanding and support other general corporate purposes.",
            "proof_upgrade": "independent use-of-proceeds confirmation visible",
            "cash_movement_read": "A rating source independently confirms the refinancing route and gives a 1.750B USD redemption reference.",
            "remaining_gap": "No cash settlement, waterfall, or Athene-specific receipt record.",
            "next_action": "Reconcile Concord's 1.65B USD note-series statement with KBRA's 1.750B USD outstanding-note reference.",
        },
        {
            "source_acquisition_id": "CFAACNCSP-007",
            "evidence_layer": "ongoing-servicing-cash-proxy",
            "source_title": "KBRA Affirms Ratings for Concord Music Royalties, LLC",
            "source_url": "https://www.kbra.com/publications/xpNPQytP",
            "source_date": "2026-07-21",
            "source_controller": "KBRA",
            "source_status": "public-source-found",
            "extracted_fact": "KBRA's July 2026 review affirms Series 2024-1 and 2025-1/2/3 notes, uses data as of the July 2026 quarterly payment date, and says the securities have received timely interest payments.",
            "proof_upgrade": "post-issuance debt-service proxy visible",
            "cash_movement_read": "The securitization appears to be servicing note interest after issuance, but not at noteholder-specific distribution detail.",
            "remaining_gap": "No Athene noteholder receipt, principal distribution, remittance report, or waterfall allocation.",
            "next_action": "Acquire July 2026 trustee/remittance report and noteholder or custodian receipt evidence.",
        },
        {
            "source_acquisition_id": "CFAACNCSP-008",
            "evidence_layer": "next-proof-requirements",
            "source_title": "Concord named-cash proof requirements",
            "source_url": "derived from current source gaps",
            "source_date": "current",
            "source_controller": "research control",
            "source_status": "request-package-defined",
            "extracted_fact": "The decisive missing package is offering memorandum, indenture/amendment, collateral catalog or receivable tape, trustee remittance reports, Series 2022-1 redemption/payoff ledger, VFN amendment, Athene allocation/trade records, and liability-cost support.",
            "proof_upgrade": "controlled-document request defined",
            "cash_movement_read": "The public route is strong enough to request decisive documents rather than continue broad screening.",
            "remaining_gap": "Controlled/private documents likely required for full named cash proof.",
            "next_action": "Create Concord as a priority named-cash request package and stop short of final receipt/return claims until documents are acquired.",
        },
    ]

    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    diagnostics = [
        ("source_acquisition_rows", "8", "count"),
        ("public_sources_found", "5", "count"),
        ("local_athene_row_sources", "1", "count"),
        ("request_package_rows", "1", "count"),
        ("athene_concord_cash_like_consideration", str(int(float(packet["cash_like_disposal_consideration_usd"]))), "USD"),
        ("athene_concord_year_end_book_value", str(int(float(packet["year_end_book_value_usd"]))), "USD"),
        ("concord_issuance_amount", "1765000000", "USD"),
        ("concord_company_repayment_reference", "1650000000", "USD"),
        ("concord_vfn_refinance_reference", "100000000", "USD"),
        ("kbra_2022_1_redemption_reference", "1750000000", "USD"),
    ]
    with DIAGNOSTIC_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DIAGNOSTIC_FIELDS)
        writer.writeheader()
        for idx, (metric, value, units) in enumerate(diagnostics, start=1):
            writer.writerow(
                {
                    "diagnostic_id": f"CFAACNCSPD-{idx:03d}",
                    "metric": metric,
                    "value": value,
                    "units": units,
                    "proof_use": "controls Concord named-cash source acquisition status",
                    "boundary": "diagnostic combines local Athene statutory evidence with public issuer/rating evidence; not Athene-specific remittance or final return proof",
                    "next_action": "acquire Concord offering, indenture, trustee remittance, redemption, allocation, and liability-cost documents",
                }
            )

    print(f"wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT.relative_to(ROOT)}")
    print(issuer["mapping_status"])


if __name__ == "__main__":
    main()
