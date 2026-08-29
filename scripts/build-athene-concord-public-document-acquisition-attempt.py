#!/usr/bin/env python3
"""Record public acquisition attempt for Concord named-cash documents."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
REQUESTS = DATA / "capital-flow-apollo-athene-concord-controlled-document-request-packet-pass-1.csv"
OUT = DATA / "capital-flow-apollo-athene-concord-public-document-acquisition-attempt-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-apollo-athene-concord-public-document-acquisition-attempt-diagnostic-pass-1.csv"

FIELDNAMES = [
    "attempt_id",
    "request_id",
    "document_family",
    "public_route_tested",
    "route_url",
    "route_status",
    "found_document_or_signal",
    "evidence_value",
    "proof_effect",
    "cash_loop_link",
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


ATTEMPTS = [
    {
        "request_id": "CFAACNCDR-001",
        "document_family": "offering-memorandum",
        "public_route_tested": "DealX Concord Music Royalties document index",
        "route_url": "https://dealx.com/reportstream/deal/concord-music-royalties/docs",
        "route_status": "located-access-controlled",
        "found_document_or_signal": "Search result lists Offering Circular or OC posted 2025-09-12.",
        "evidence_value": "Document existence/index signal only; content not accessible in current run.",
        "proof_effect": "Upgrades from unknown to located-but-controlled.",
        "cash_loop_link": "legal instrument and source-to-wrapper",
        "remaining_gap": "Need the actual offering circular text, tranche table, CUSIP terms, and investor allocation data.",
        "next_action": "Request DealX access or obtain offering circular from investor/rating/placement-agent source.",
    },
    {
        "request_id": "CFAACNCDR-002",
        "document_family": "indenture-and-supplements",
        "public_route_tested": "DealX document index plus KBRA public release",
        "route_url": "https://dealx.com/reportstream/deal/concord-music-royalties/docs; https://www.kbra.com/publications/bcGzRKWf",
        "route_status": "located-access-controlled-plus-public-amendment-signal",
        "found_document_or_signal": "DealX search result lists Indenture Exhibits and Indenture Supplement posted 2026-02-12; KBRA public release says Series 2025 issuance involved an amendment to the indenture.",
        "evidence_value": "Document family existence and amendment signal visible; actual waterfall terms not accessible.",
        "proof_effect": "Upgrades legal waterfall route from request-only to located-but-controlled.",
        "cash_loop_link": "legal route and waterfall",
        "remaining_gap": "Need indenture/supplement text, payment priority, reserve mechanics, events/triggers, and noteholder waterfall.",
        "next_action": "Request DealX documents or seek trustee/rating-agency full report package.",
    },
    {
        "request_id": "CFAACNCDR-003",
        "document_family": "trustee-remittance-reports",
        "public_route_tested": "web search for Concord trustee remittance/distribution reports",
        "route_url": "public web search",
        "route_status": "not-found-public",
        "found_document_or_signal": "No public trustee remittance or investor distribution report was found.",
        "evidence_value": "Only KBRA deal-level timely-interest proxy remains visible.",
        "proof_effect": "No upgrade to Athene receipt or noteholder remittance.",
        "cash_loop_link": "cash-back and debt-service receipt",
        "remaining_gap": "Need actual remittance reports with collections, fees, interest, principal, reserves, and distributions by series/tranche.",
        "next_action": "Request trustee reports from trustee, servicer, noteholder, rating agency, or investor document portal.",
    },
    {
        "request_id": "CFAACNCDR-004",
        "document_family": "series-2022-1-redemption-payoff-ledger",
        "public_route_tested": "Concord, KBRA, and Asset Securitization Report public route",
        "route_url": "https://concord.com/news/concord-closes-1-765-billion-abs-to-fuel-continued-growth/; https://www.kbra.com/publications/bcGzRKWf; https://asreport.americanbanker.com/news/concord-music-prepares-to-sell-1-7-billion-in-abs-from-music-catalog-assets",
        "route_status": "public-use-proxy-found-payoff-ledger-not-found",
        "found_document_or_signal": "Concord says proceeds repay 1.65B USD 2022-1 notes and refinance/extend a 100M USD VFN; KBRA says proceeds redeem 1.750B USD Series 2022-1 notes; ASR says 2025 proceeds repay 1.7B USD outstanding 2022-1 notes and fund general corporate purposes.",
        "evidence_value": "Issuer/rating/media use-of-proceeds proxy strengthened.",
        "proof_effect": "Use-of-proceeds proxy improves; settlement cash remains unproven.",
        "cash_loop_link": "use of proceeds",
        "remaining_gap": "Need payoff statement, paying-agent cash ledger, redemption notice, accrued interest/premium/fee allocation, and final settlement confirmation.",
        "next_action": "Acquire trustee/paying-agent redemption package and reconcile Concord/KRBA/ASR repayment references.",
    },
    {
        "request_id": "CFAACNCDR-005",
        "document_family": "collateral-catalog-and-royalty-tape",
        "public_route_tested": "Concord, Apollo, KBRA, and Asset Securitization Report public route",
        "route_url": "https://concord.com/news/concord-closes-1-765-billion-abs-to-fuel-continued-growth/; https://www.apollo.com/insights-news/insights/2025/01/apollo-leads-largest-ever-music-abs-transaction-for-concord; https://asreport.americanbanker.com/news/concord-music-prepares-to-sell-1-7-billion-in-abs-from-music-catalog-assets",
        "route_status": "public-collateral-proxy-found-tape-not-found",
        "found_document_or_signal": "Public sources describe collateral as more than 1.3M music copyrights or more than 1M songs/assets, with Apollo noting a catalog valuation above 5B USD and about 52% loan-to-value as of January 2025.",
        "evidence_value": "Collateral type, scale, and value proxy visible.",
        "proof_effect": "Funded-asset route improves; royalty cash-flow tape remains missing.",
        "cash_loop_link": "funded asset and operating cash source",
        "remaining_gap": "Need catalog/royalty tape, servicer collection report, concentration data, valuation model, DSCR/LTV tests, and cash-flow history.",
        "next_action": "Request full rating reports, offering circular appendix, trustee reports, and collateral tape extracts.",
    },
    {
        "request_id": "CFAACNCDR-006",
        "document_family": "athene-allocation-and-trade-support",
        "public_route_tested": "public web and local statutory evidence",
        "route_url": "local Athene statutory row plus public web search",
        "route_status": "not-found-public",
        "found_document_or_signal": "Athene statutory CUSIP row remains visible locally, but no public trade confirmation, custodian statement, allocation book, or remittance record was found.",
        "evidence_value": "No upgrade beyond local statutory named proceeds.",
        "proof_effect": "Athene receipt remains hold.",
        "cash_loop_link": "Athene receipt and legal-entity cash movement",
        "remaining_gap": "Need Athene trade/custodian/allocation records or state-examiner workpapers.",
        "next_action": "Keep as controlled/private request to Athene, Apollo insurance asset management, custodian, broker, or regulator.",
    },
    {
        "request_id": "CFAACNCDR-007",
        "document_family": "liability-cost-and-spread-support",
        "public_route_tested": "public web and local Athene statutory evidence",
        "route_url": "local Athene statutory row plus public web search",
        "route_status": "not-found-public",
        "found_document_or_signal": "No public Concord-specific Athene liability-cost, credited-rate, ALM, or spread workpaper was found.",
        "evidence_value": "No return upgrade.",
        "proof_effect": "Return model remains hold.",
        "cash_loop_link": "return model",
        "remaining_gap": "Need funding source, credited-rate/liability cost, asset allocation economics, credit-loss treatment, and realized spread model.",
        "next_action": "Request from Athene ALM, actuarial, investment accounting, Apollo insurance asset management, or state exam files.",
    },
    {
        "request_id": "CFAACNCDR-008",
        "document_family": "rating-surveillance-full-reports",
        "public_route_tested": "KBRA report links and transaction page",
        "route_url": "https://www.kbra.com/publications/GWGHRrZS/concord-music-royalties-llc-series-2025-1-new-issue-report?format=web; https://www.kbra.com/sectors/abs/transactions?filterText=Concord+Music+Royalties,+LLC&sortField=Date",
        "route_status": "located-premium-access-controlled",
        "found_document_or_signal": "KBRA new-issue report page is visible but requires ABS Premium Subscription; KBRA transaction page lists 2026 surveillance entries for Series 2025-1, 2025-2, 2025-3, and 2024-1.",
        "evidence_value": "Full report locations and surveillance entries located, but contents remain gated.",
        "proof_effect": "Upgrades from request-only to located-premium-controlled.",
        "cash_loop_link": "surveillance and performance",
        "remaining_gap": "Need full report tables and surveillance data for collateral performance, cash-flow assumptions, DSCR/LTV, and payment metrics.",
        "next_action": "Obtain ABS premium report access or request full reports from investor/rating/issuer channels.",
    },
]

DIAGNOSTICS = [
    ("attempt_rows", "8", "count"),
    ("located_access_controlled_rows", "3", "count"),
    ("public_proxy_found_rows", "2", "count"),
    ("not_found_public_rows", "3", "count"),
    ("cash_loop_links_tested", "8", "count"),
    ("athene_receipt_upgrade_rows", "0", "count"),
    ("return_model_upgrade_rows", "0", "count"),
    ("document_families_remaining_controlled_needed", "8", "count"),
]


def main() -> None:
    request_rows = {row["request_id"]: row for row in read_rows(REQUESTS)}
    rows = []
    for idx, attempt in enumerate(ATTEMPTS, start=1):
        request = request_rows[attempt["request_id"]]
        row = {
            "attempt_id": f"CFAACNCPDA-{idx:03d}",
            **attempt,
        }
        row["document_family"] = request["document_family"]
        rows.append(row)

    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    with DIAGNOSTIC_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DIAGNOSTIC_FIELDS)
        writer.writeheader()
        for idx, (metric, value, units) in enumerate(DIAGNOSTICS, start=1):
            writer.writerow(
                {
                    "diagnostic_id": f"CFAACNCPDAD-{idx:03d}",
                    "metric": metric,
                    "value": value,
                    "units": units,
                    "proof_use": "controls Concord public document acquisition attempt",
                    "boundary": "public acquisition attempt identifies found routes, access controls, and not-found routes; it does not prove controlled document contents",
                    "next_action": "pursue located controlled routes first, then private trustee/Athene document requests",
                }
            )

    print(f"wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")
    print(f"wrote {len(DIAGNOSTICS)} rows to {DIAGNOSTIC_OUT.relative_to(ROOT)}")


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


if __name__ == "__main__":
    main()
