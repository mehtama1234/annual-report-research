#!/usr/bin/env python3
"""Build AMAPS controlled-document request packet for named cash proof."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
SOURCE_PACKET = DATA / "capital-flow-apollo-athene-amaps-named-cash-source-acquisition-pass-1.csv"
DIAG = DATA / "capital-flow-apollo-athene-amaps-named-cash-source-acquisition-diagnostic-pass-1.csv"
OUT = DATA / "capital-flow-apollo-athene-amaps-controlled-document-request-packet-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-apollo-athene-amaps-controlled-document-request-packet-diagnostic-pass-1.csv"

FIELDNAMES = [
    "request_id",
    "rank",
    "document_family",
    "specific_document_request",
    "likely_controller",
    "why_needed",
    "promotion_test",
    "hold_test",
    "current_public_evidence",
    "current_status",
    "cash_loop_link",
    "priority_reason",
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


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def diag_value(metric: str) -> str:
    for row in read_rows(DIAG):
        if row["metric"] == metric:
            return row["value"]
    raise KeyError(metric)


REQUESTS = [
    {
        "document_family": "amaps-1-offering-memorandum",
        "specific_document_request": "AMAPS 1 LLC offering memorandum, private placement memorandum, investor presentation, and tranche table, including all CUSIPs and note terms.",
        "likely_controller": "Apollo, AMAPS 1 LLC issuer files, Athene investment files, placement agents, rating agencies, note purchasers",
        "why_needed": "Defines the issuer, capital structure, tranche economics, eligible collateral, investor rights, proceeds use, and whether CUSIP 02300A-AA-8 is primary issuance, secondary trading, paydown, or redemption exposure.",
        "promotion_test": "Shows CUSIP 02300A-AA-8 tranche terms, issuance amount, payment dates, maturity, pricing, noteholder rights, and whether Athene or an Apollo/Athene account was allocated the tranche.",
        "hold_test": "If only Apollo product description or consolidated exposure is available, keep AMAPS at wrapper/alignment proof.",
        "cash_loop_link": "legal instrument and source-to-wrapper",
        "priority_reason": "Highest leverage document because it connects Athene's statutory CUSIP to AMAPS 1's actual tranche economics.",
    },
    {
        "document_family": "tranche-supplement-and-note-purchase-agreement",
        "specific_document_request": "AMAPS 1 tranche supplement, note purchase agreement, subscription agreement, transfer records, and CUSIP-specific amendments for Tranche A Note 5.859% due 07/31/70.",
        "likely_controller": "Apollo, AMAPS 1 LLC, Athene investment accounting, broker/dealer, custodian, placement agents, legal counsel",
        "why_needed": "Separates broad AMAPS product evidence from the exact Tranche A Note that appears in Athene's statutory Schedule D row.",
        "promotion_test": "Matches Athene's statutory CUSIP, coupon, maturity, and consideration to a populated AMAPS 1 tranche document and note purchase or transfer record.",
        "hold_test": "CUSIP visibility without populated tranche ownership or trade records remains named wrapper evidence, not Athene allocation proof.",
        "cash_loop_link": "CUSIP-specific allocation and trade route",
        "priority_reason": "The AMAPS proof problem is not product existence; it is the exact Athene legal-entity allocation to a tranche.",
    },
    {
        "document_family": "full-rating-rationale-reports",
        "specific_document_request": "AMAPS 1 full rating rationale reports, private letter rating files, SVO filing support, surveillance reports, and rating committee exhibits.",
        "likely_controller": "rating agencies, Apollo, Athene, state insurance examiners, NAIC/SVO filing channel where available",
        "why_needed": "Public AMAPS summaries and AMAPS 5 analogs do not disclose AMAPS 1-specific collateral, stress assumptions, asset coverage, LTV triggers, or waterfall detail.",
        "promotion_test": "Provides AMAPS 1-specific collateral categories, portfolio limits, asset coverage, LTV tests, rating assumptions, payment-priority mechanics, and surveillance performance.",
        "hold_test": "AMAPS 5 rating reports are structural analogs only and cannot prove AMAPS 1 collateral or remittance.",
        "cash_loop_link": "credit quality, collateral, and waterfall support",
        "priority_reason": "Likely the fastest controlled source for turning private-letter-rating context into AMAPS 1-specific proof.",
    },
    {
        "document_family": "collateral-tape-or-portfolio-schedule",
        "specific_document_request": "AMAPS 1 collateral tape, portfolio holdings schedule, obligor list, asset class breakout, par/fair value schedule, eligibility report, and concentration report.",
        "likely_controller": "Apollo manager files, AMAPS 1 collateral administrator, trustee, rating agencies, investors, Athene investment files",
        "why_needed": "AMAPS is pooled structured credit; borrower/use proof requires underlying asset and obligor detail rather than top-level wrapper evidence.",
        "promotion_test": "Shows AMAPS 1 underlying obligors or asset groups, balances, marks, eligibility, collateral value, cash-generating assets, and concentration limits.",
        "hold_test": "General statements about diversified corporate and asset-backed credit, 600-plus obligors, or 45-50% investment-grade collateral are not collateral tape proof.",
        "cash_loop_link": "underlying borrower/collateral destination",
        "priority_reason": "This is the document family that answers where the money went inside the pooled wrapper.",
    },
    {
        "document_family": "trustee-remittance-and-noteholder-reports",
        "specific_document_request": "AMAPS 1 trustee reports, noteholder remittance reports, payment-date statements, collection period reports, interest/principal distribution records, and reserve account statements.",
        "likely_controller": "trustee, collateral administrator, Apollo manager files, noteholders, custodian, rating agencies",
        "why_needed": "Athene statutory proceeds and interest fields do not prove actual AMAPS 1 cash remitted through the payment waterfall.",
        "promotion_test": "Shows dated AMAPS 1 collections, fees, interest, principal, deferred amounts, reserve movements, LTV tests, and payments to the Tranche A CUSIP.",
        "hold_test": "Statutory interest income and consideration stay as Athene-side row evidence without remittance reports.",
        "cash_loop_link": "cash-back and debt-service receipt",
        "priority_reason": "Most direct missing source for moving from wrapper evidence to actual noteholder cash.",
    },
    {
        "document_family": "payment-waterfall-and-ltv-test-support",
        "specific_document_request": "AMAPS 1 priority-of-payments schedule, debt payment sequence, LTV test calculations, collateral value calculations, trigger notices, and reinvestment/redemption mechanics.",
        "likely_controller": "Apollo manager files, trustee, collateral administrator, rating agencies, legal counsel, investors",
        "why_needed": "AMAPS repayment depends on structured-credit waterfall and collateral/LTV mechanics; public descriptions do not prove legal payback route.",
        "promotion_test": "Shows how current income, principal proceeds, redemptions, fees, expenses, reserves, and class-level interest/principal are allocated under AMAPS 1 documents.",
        "hold_test": "General AMAPS market or analog structure language remains route evidence, not AMAPS 1 waterfall proof.",
        "cash_loop_link": "legal payback route and waterfall",
        "priority_reason": "Required to show how cash legally moves from collateral to AMAPS 1 noteholders.",
    },
    {
        "document_family": "athene-allocation-trade-and-custodian-support",
        "specific_document_request": "Athene trade confirmation, statutory investment workpaper, custodian statement, allocation book, broker/dealer statement, paydown/redemption ticket, and cash ledger for AMAPS 1 CUSIP 02300A-AA-8.",
        "likely_controller": "Athene investment accounting, Apollo insurance asset management, custodian, broker/dealer, state insurance examiners",
        "why_needed": "Connects Athene's statutory Schedule D row to actual legal-entity cash movement and determines whether the 268.000000M USD consideration was sale, paydown, redemption, or other cash event.",
        "promotion_test": "Matches the 268.000000M USD statutory consideration and 3.986842M USD disposal interest/dividends to dated custodian cash activity and AMAPS 1 note balance movement.",
        "hold_test": "Athene statutory row visibility alone remains named proceeds evidence, not trade settlement or cash receipt proof.",
        "cash_loop_link": "Athene receipt and legal-entity cash movement",
        "priority_reason": "This is the decisive Athene-side cash receipt document package.",
    },
    {
        "document_family": "statutory-subsidiary-reconciliation",
        "specific_document_request": "Athene subsidiary-level AMAPS 1 holdings reconciliation, related-party fixed-maturity schedule, Schedule D/BA crosswalk, investment income workpaper, and consolidation bridge to Apollo/Athene's 2.550B USD AMAPS 1 concentration.",
        "likely_controller": "Athene statutory reporting, Apollo/Athene SEC reporting, auditors, state insurance examiners, investment accounting",
        "why_needed": "The local row is one Athene legal-entity CUSIP exposure, while public Apollo/Athene disclosure reports a 2.550B USD AMAPS 1 concentration.",
        "promotion_test": "Reconciles the 1.917500000B USD local year-end book value and 268.000000M USD consideration to AMAPS 1 exposure across Athene subsidiaries and the consolidated 2.550B USD disclosure.",
        "hold_test": "Do not assume one statutory legal entity equals the full public AMAPS 1 concentration without subsidiary crosswalk.",
        "cash_loop_link": "legal-entity booking and consolidation bridge",
        "priority_reason": "Needed to avoid mixing legal entities, subsidiaries, and consolidated exposure in the final claim.",
    },
    {
        "document_family": "liability-cost-and-return-model-support",
        "specific_document_request": "Athene liability funding source, credited-rate or funding-agreement cost, asset allocation model, spread workpaper, risk capital charge, impairment/CECL support, and AMAPS 1 return model.",
        "likely_controller": "Athene ALM, investment accounting, actuarial, Apollo insurance asset management, auditors, state insurance examiners",
        "why_needed": "Gross interest income and cash-like consideration do not prove that Athene earned a positive return after liability cost, expenses, capital charges, and credit risk.",
        "promotion_test": "Shows AMAPS 1 gross yield, received cash, liability cost, reserves, marks, credit losses, expenses, and realized spread/IRR/NPV/ROIC or payback.",
        "hold_test": "Do not call AMAPS profitable or return-proven from coupon, fair value, or gross statutory income alone.",
        "cash_loop_link": "return model",
        "priority_reason": "Required for the final user question: what cash came back and was the routing economically successful?",
    },
]


def current_evidence() -> str:
    consideration = diag_value("athene_amaps_cash_like_consideration")
    book = diag_value("athene_amaps_year_end_book_value")
    income = diag_value("athene_amaps_year_end_interest_income")
    disposal_interest = diag_value("athene_amaps_disposal_interest_or_dividends")
    concentration = diag_value("apollo_athene_amaps1_public_concentration")
    return (
        "Current public/local evidence: Athene AMAPS 1 CUSIP 02300A-AA-8 "
        f"cash-like consideration {consideration} USD; year-end book value {book} USD; "
        f"year-end interest income {income} USD; disposal interest/dividends {disposal_interest} USD; "
        f"Apollo/Athene public AMAPS 1 concentration {concentration} USD; "
        "Apollo AMAPS wrapper/alignment evidence visible."
    )


def main() -> None:
    evidence = current_evidence()
    source_rows = read_rows(SOURCE_PACKET)
    rows = []
    for idx, request in enumerate(REQUESTS, start=1):
        rows.append(
            {
                "request_id": f"CFAAAMAPSDR-{idx:03d}",
                "rank": str(idx),
                "document_family": request["document_family"],
                "specific_document_request": request["specific_document_request"],
                "likely_controller": request["likely_controller"],
                "why_needed": request["why_needed"],
                "promotion_test": request["promotion_test"],
                "hold_test": request["hold_test"],
                "current_public_evidence": evidence,
                "current_status": "controlled-document-needed",
                "cash_loop_link": request["cash_loop_link"],
                "priority_reason": request["priority_reason"],
                "boundary": "request row identifies proof requirements; it is not proof that the document has been obtained or that cash-all-the-way-through is complete",
                "next_action": "request or locate the named document, extract populated fields, and rerun the AMAPS proof promotion test",
            }
        )

    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    diagnostics = [
        ("request_rows", str(len(rows)), "count"),
        ("source_acquisition_rows_upstream", str(len(source_rows)), "count"),
        ("controlled_document_needed_rows", str(sum(1 for row in rows if row["current_status"] == "controlled-document-needed")), "count"),
        ("cash_loop_links_covered", str(len({row["cash_loop_link"] for row in rows})), "count"),
        ("athene_amaps_cash_like_consideration", diag_value("athene_amaps_cash_like_consideration"), "USD"),
        ("athene_amaps_year_end_book_value", diag_value("athene_amaps_year_end_book_value"), "USD"),
        ("athene_amaps_year_end_interest_income", diag_value("athene_amaps_year_end_interest_income"), "USD"),
        ("athene_amaps_disposal_interest_or_dividends", diag_value("athene_amaps_disposal_interest_or_dividends"), "USD"),
        ("apollo_athene_amaps1_public_concentration", diag_value("apollo_athene_amaps1_public_concentration"), "USD"),
        ("mapping_status", diag_value("mapping_status"), "status"),
    ]
    with DIAGNOSTIC_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DIAGNOSTIC_FIELDS)
        writer.writeheader()
        for idx, (metric, value, units) in enumerate(diagnostics, start=1):
            writer.writerow(
                {
                    "diagnostic_id": f"CFAAAMAPSCDRD-{idx:03d}",
                    "metric": metric,
                    "value": value,
                    "units": units,
                    "proof_use": "controls AMAPS controlled-document request package",
                    "boundary": "request diagnostics define missing documents; they do not prove the documents were obtained or extracted",
                    "next_action": "execute document acquisition, then promote or hold each AMAPS cash-loop link based on populated evidence",
                }
            )

    print(f"wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
