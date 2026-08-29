#!/usr/bin/env python3
"""Build issuer/borrower mapping workbench for Athene same-CUSIP candidates."""

from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
PACKET = DATA / "capital-flow-apollo-athene-statutory-safe-cashlike-same-cusip-row-proof-packet-pass-1.csv"
OUT = DATA / "capital-flow-apollo-athene-statutory-safe-cashlike-issuer-borrower-map-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-apollo-athene-statutory-safe-cashlike-issuer-borrower-map-diagnostic-pass-1.csv"

FIELDNAMES = [
    "issuer_map_id",
    "proof_packet_id",
    "safe_summary_rank",
    "cusip",
    "issuer_or_description_sample",
    "athene_cash_like_consideration_usd",
    "athene_year_end_book_value_usd",
    "instrument_or_wrapper",
    "destination_lane",
    "mapped_platform_or_sponsor",
    "borrower_or_collateral_read",
    "source_backing_type",
    "source_url",
    "source_evidence_summary",
    "mapping_status",
    "cash_movement_read",
    "remaining_named_cash_documents",
    "safe_claim",
    "boundary",
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

SOURCE_MAP = {
    "00264#-AB-3": {
        "instrument_or_wrapper": "Apollo-related private/affiliated credit instrument",
        "destination_lane": "apollo_affiliated_private_credit_or_finance_vehicle",
        "mapped_platform_or_sponsor": "Apollo-linked entity hold",
        "borrower_or_collateral_read": "AP Aristotle Holdings LLC; borrower/use not proven from current public packet",
        "source_backing_type": "local-statutory-plus-apollo-name-marker",
        "source_url": "local Athene statutory Schedule D rows",
        "source_evidence_summary": "Athene statutory rows identify AP Aristotle under the same CUSIP with paydown and exchange activity; external borrower/use support is still missing.",
        "mapping_status": "issuer-named-platform-marker-borrower-use-hold",
        "cash_movement_read": "Athene cash-like proceeds candidate from a named Apollo-style private issuer, mixed with noncash exchange evidence.",
        "remaining_named_cash_documents": "issuer financing documents; note purchase agreement; borrower use-of-proceeds; repayment ledger; Apollo/Athene allocation support; liability-cost schedule",
    },
    "28655*-AA-7": {
        "instrument_or_wrapper": "Apollo-related Eliant private credit instrument",
        "destination_lane": "apollo_affiliated_private_credit_or_finance_vehicle",
        "mapped_platform_or_sponsor": "Apollo Global Management related-entity evidence",
        "borrower_or_collateral_read": "Eliant Invest Holding LP; underlying borrower/collateral not proven",
        "source_backing_type": "SEC exhibit plus local statutory rows",
        "source_url": "https://www.sec.gov/Archives/edgar/data/1411494/000141149422000014/exhibit211q42021.htm",
        "source_evidence_summary": "Apollo SEC subsidiary exhibit lists Eliant Invest Holding LP, Eliant Invest GP LP, Eliant Invest Management LP, and related Apollo Eliant entities; Athene rows show same-CUSIP holding and proceeds.",
        "mapping_status": "platform-related-issuer-visible-borrower-use-hold",
        "cash_movement_read": "Athene has cash-like proceeds from a same-CUSIP Eliant instrument; this maps to an Apollo-related issuer lane, not yet to a borrower use.",
        "remaining_named_cash_documents": "Eliant offering memorandum; borrower/collateral schedule; note purchase agreement; repayment or redemption notice; liability-cost spread support",
    },
    "00024D-AL-7": {
        "instrument_or_wrapper": "infrastructure fund debt or ABS-style note",
        "destination_lane": "infrastructure_and_real_assets_hold",
        "mapped_platform_or_sponsor": "Apollo marker unproven in current source set",
        "borrower_or_collateral_read": "AA Infrastructure Fund 2 LLC; underlying assets and cash use not proven",
        "source_backing_type": "local-statutory-only",
        "source_url": "local Athene statutory Schedule D rows",
        "source_evidence_summary": "Athene statutory rows name AA Infrastructure Fund 2 LLC, but the selected packet is mixed because the same CUSIP includes tax-free exchange hold evidence.",
        "mapping_status": "issuer-named-mixed-row-hold",
        "cash_movement_read": "Cash-like proceeds exist in the packet, but the row set remains mixed with noncash exchange evidence.",
        "remaining_named_cash_documents": "fund/offering documents; collateral or project schedule; investor reports; transaction cash ledger; source/use; return model",
    },
    "02300A-AA-8": {
        "instrument_or_wrapper": "Apollo Multi-Asset Prime Securities structured credit note",
        "destination_lane": "structured_credit_and_asset_backed_credit",
        "mapped_platform_or_sponsor": "Apollo / AMAPS",
        "borrower_or_collateral_read": "AMAPS 1 LLC diversified corporate and asset-backed credit; underlying collateral not visible in local packet",
        "source_backing_type": "Apollo product disclosure plus Apollo/Athene investment disclosure plus local statutory rows",
        "source_url": "https://www.apollo.com/insights-news/insights/2026/05/introducing-amaps; https://www.sec.gov/Archives/edgar/data/1527469/000152746926000013/R12.htm",
        "source_evidence_summary": "Apollo describes AMAPS as a structured credit product with diversified corporate and asset-backed credit collateral and tranche CUSIPs. Apollo/Athene investment disclosure identifies investment-grade ABS debt issued by AMAPS 1 LLC.",
        "mapping_status": "platform-wrapper-visible-underlying-collateral-hold",
        "cash_movement_read": "Athene same-CUSIP proceeds map to an Apollo AMAPS structured-credit wrapper; the underlying borrowers remain pooled and not individually proven.",
        "remaining_named_cash_documents": "AMAPS 1 offering memorandum; collateral pool; trustee reports; noteholder remittance reports; tranche waterfall; Apollo/Athene allocation and liability-cost support",
    },
    "20633K-AN-8": {
        "instrument_or_wrapper": "music-royalty ABS note",
        "destination_lane": "intellectual_property_royalty_backed_finance",
        "mapped_platform_or_sponsor": "Concord Music Royalties",
        "borrower_or_collateral_read": "Concord music royalty catalog ABS; Series 2025 notes refinance prior 2022 notes and support corporate purposes",
        "source_backing_type": "issuer/company release plus rating-agency summary plus local statutory rows",
        "source_url": "https://concord.com/news/concord-closes-1-765-billion-abs-to-fuel-continued-growth/; https://www.kbra.com/publications/ZLhcMNKm",
        "source_evidence_summary": "Concord says it issued 1.765B USD of senior notes; KBRA says Series 2025 proceeds redeem Series 2022-1 notes and support general corporate purposes.",
        "mapping_status": "borrower-wrapper-and-use-proxy-visible-cash-receipt-hold",
        "cash_movement_read": "Athene has same-CUSIP cash-like proceeds from Concord royalty ABS; public sources identify the borrower wrapper and broad refinance/growth use, not Athene-specific receipt/use.",
        "remaining_named_cash_documents": "offering memorandum; indenture; collateral catalog schedule; trustee remittance; redemption/payoff ledger; Athene trade confirmation; liability-cost support",
    },
    "592918-AA-4": {
        "instrument_or_wrapper": "commercial real estate / mortgage securitization note",
        "destination_lane": "real_estate_credit_and_cmbs",
        "mapped_platform_or_sponsor": "MF1 / mortgage securitization parties",
        "borrower_or_collateral_read": "MF1 2025-B2 LLC; securitization and companion-interest/future-funding structure visible, loan collateral not mapped here",
        "source_backing_type": "SEC transaction agreement plus rating page plus local statutory rows",
        "source_url": "https://www.sec.gov/Archives/edgar/data/2134864/000153949726001596/exh4_2-mf1psa.htm; https://www.fitchratings.com/entity/mf1-2025-b2-llc-97720910",
        "source_evidence_summary": "SEC agreement names MF1 2025-B2 LLC in transaction exhibits and future-funding servicing mechanics; Fitch identifies MF1 2025-B2 LLC as a rated structured-finance entity.",
        "mapping_status": "securitization-vehicle-visible-loan-collateral-hold",
        "cash_movement_read": "Athene has same-CUSIP cash-like proceeds from a mortgage/real-estate securitization vehicle; individual property loans and borrower cash remain unproven.",
        "remaining_named_cash_documents": "loan schedule; pooling/servicing exhibits; collateral tape; trustee remittance; property-level cash flow; note waterfall; Athene allocation and liability-cost support",
    },
    "91282C-LW-9": {
        "instrument_or_wrapper": "U.S. Treasury note/bond",
        "destination_lane": "government_liquidity_or_reserve_asset",
        "mapped_platform_or_sponsor": "U.S. Treasury",
        "borrower_or_collateral_read": "sovereign Treasury obligation",
        "source_backing_type": "local-statutory-row-sufficient-for-issuer-class",
        "source_url": "local Athene statutory Schedule D rows",
        "source_evidence_summary": "CUSIP description is a U.S. Treasury note/bond; borrower identity is sovereign and not an operating private borrower.",
        "mapping_status": "sovereign-reserve-asset-mapped-operating-use-not-applicable",
        "cash_movement_read": "Athene proceeds from a liquid reserve/security sale or disposal, not a private borrower cash-use case.",
        "remaining_named_cash_documents": "trade confirmation if exact sale proceeds are needed; no borrower-use package applicable",
    },
    "28655*-AB-5": {
        "instrument_or_wrapper": "Apollo-related Eliant private credit instrument",
        "destination_lane": "apollo_affiliated_private_credit_or_finance_vehicle",
        "mapped_platform_or_sponsor": "Apollo Global Management related-entity evidence",
        "borrower_or_collateral_read": "Eliant Invest Holding LP; underlying borrower/collateral not proven",
        "source_backing_type": "SEC exhibit plus local statutory rows",
        "source_url": "https://www.sec.gov/Archives/edgar/data/1411494/000141149422000014/exhibit211q42021.htm",
        "source_evidence_summary": "Apollo SEC subsidiary exhibit lists Eliant Invest Holding LP and related Apollo Eliant entities; Athene rows show same-CUSIP holding and proceeds for a separate Eliant tranche.",
        "mapping_status": "platform-related-issuer-visible-borrower-use-hold",
        "cash_movement_read": "Athene has cash-like proceeds from a second same-CUSIP Eliant instrument; this maps to an Apollo-related issuer lane, not yet to borrower use.",
        "remaining_named_cash_documents": "Eliant offering memorandum; borrower/collateral schedule; note purchase agreement; redemption ledger; liability-cost spread support",
    },
    "912810-TW-8": {
        "instrument_or_wrapper": "U.S. Treasury note/bond",
        "destination_lane": "government_liquidity_or_reserve_asset",
        "mapped_platform_or_sponsor": "U.S. Treasury",
        "borrower_or_collateral_read": "sovereign Treasury obligation",
        "source_backing_type": "local-statutory-row-sufficient-for-issuer-class",
        "source_url": "local Athene statutory Schedule D rows",
        "source_evidence_summary": "CUSIP description is a U.S. Treasury note/bond; borrower identity is sovereign and not an operating private borrower.",
        "mapping_status": "sovereign-reserve-asset-mapped-operating-use-not-applicable",
        "cash_movement_read": "Athene proceeds from a liquid reserve/security sale or disposal, not a private borrower cash-use case.",
        "remaining_named_cash_documents": "trade confirmation if exact sale proceeds are needed; no borrower-use package applicable",
    },
    "91282C-MG-3": {
        "instrument_or_wrapper": "U.S. Treasury note/bond",
        "destination_lane": "government_liquidity_or_reserve_asset",
        "mapped_platform_or_sponsor": "U.S. Treasury",
        "borrower_or_collateral_read": "sovereign Treasury obligation",
        "source_backing_type": "local-statutory-row-sufficient-for-issuer-class",
        "source_url": "local Athene statutory Schedule D rows",
        "source_evidence_summary": "CUSIP description is a U.S. Treasury note/bond; borrower identity is sovereign and not an operating private borrower.",
        "mapping_status": "sovereign-reserve-asset-mapped-operating-use-not-applicable",
        "cash_movement_read": "Athene proceeds from a liquid reserve/security sale or disposal, not a private borrower cash-use case.",
        "remaining_named_cash_documents": "trade confirmation if exact sale proceeds are needed; no borrower-use package applicable",
    },
}


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def money(value: str) -> Decimal:
    value = (value or "").strip()
    if not value:
        return Decimal(0)
    try:
        return Decimal(value)
    except Exception:
        return Decimal(0)


def row_out(seq: int, packet_row: dict[str, str]) -> dict[str, str]:
    source = SOURCE_MAP[packet_row["cusip"]]
    return {
        "issuer_map_id": f"CFAASCIBM-{seq:03d}",
        "proof_packet_id": packet_row["proof_packet_id"],
        "safe_summary_rank": packet_row["safe_summary_rank"],
        "cusip": packet_row["cusip"],
        "issuer_or_description_sample": packet_row["issuer_or_description_sample"],
        "athene_cash_like_consideration_usd": packet_row["cash_like_disposal_consideration_usd"],
        "athene_year_end_book_value_usd": packet_row["year_end_book_value_usd"],
        "instrument_or_wrapper": source["instrument_or_wrapper"],
        "destination_lane": source["destination_lane"],
        "mapped_platform_or_sponsor": source["mapped_platform_or_sponsor"],
        "borrower_or_collateral_read": source["borrower_or_collateral_read"],
        "source_backing_type": source["source_backing_type"],
        "source_url": source["source_url"],
        "source_evidence_summary": source["source_evidence_summary"],
        "mapping_status": source["mapping_status"],
        "cash_movement_read": source["cash_movement_read"],
        "remaining_named_cash_documents": source["remaining_named_cash_documents"],
        "safe_claim": "Athene has a named same-CUSIP cash-like proceeds candidate that can be routed to this issuer/wrapper lane.",
        "boundary": "issuer mapping does not prove borrower receipt, source/use, lot continuity, liability spread, or final asset return",
        "next_action": "acquire the remaining named cash documents and build borrower/use plus liability-cost proof before promotion",
    }


def diagnostic_row(seq: int, metric: str, value: str, units: str) -> dict[str, str]:
    return {
        "diagnostic_id": f"CFAASCIBMD-{seq:03d}",
        "metric": metric,
        "value": value,
        "units": units,
        "proof_use": "controls issuer/borrower mapping for Athene same-CUSIP cash-like proceeds candidates",
        "boundary": "mapping diagnostic is route evidence, not borrower receipt, source/use, spread, or return proof",
        "next_action": "prioritize source acquisition for platform-related and securitization rows with visible Athene proceeds",
    }


def main() -> None:
    packet = read_rows(PACKET)
    output = [row_out(idx, row) for idx, row in enumerate(packet, start=1)]
    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(output)

    def count_status(prefix: str) -> int:
        return sum(1 for row in output if row["mapping_status"].startswith(prefix))

    platform_related = sum(1 for row in output if "platform" in row["mapping_status"] or "wrapper" in row["mapping_status"])
    clean_operating = [row for row in output if row["destination_lane"] not in {"government_liquidity_or_reserve_asset"}]
    diagnostics = [
        ("issuer_map_rows", str(len(output)), "count"),
        ("non_treasury_or_operating_wrapper_rows", str(len(clean_operating)), "count"),
        ("sovereign_reserve_rows", str(count_status("sovereign")), "count"),
        ("platform_related_or_wrapper_visible_rows", str(platform_related), "count"),
        ("mixed_row_hold_rows", str(sum(1 for row in output if "mixed" in row["mapping_status"])), "count"),
        ("borrower_use_hold_rows", str(sum(1 for row in output if "hold" in row["mapping_status"] and not row["mapping_status"].startswith("sovereign"))), "count"),
        ("athene_cash_like_consideration_total", str(int(sum(money(row["athene_cash_like_consideration_usd"]) for row in output))), "USD"),
        ("non_treasury_cash_like_consideration_total", str(int(sum(money(row["athene_cash_like_consideration_usd"]) for row in clean_operating))), "USD"),
    ]
    with DIAGNOSTIC_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DIAGNOSTIC_FIELDS)
        writer.writeheader()
        for idx, (metric, value, units) in enumerate(diagnostics, start=1):
            writer.writerow(diagnostic_row(idx, metric, value, units))

    print(f"wrote {len(output)} rows to {OUT.relative_to(ROOT)}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
