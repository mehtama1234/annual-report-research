#!/usr/bin/env python3
"""Build Concord controlled-document request packet for named cash proof."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "analysis/company-first-principles/data"
SOURCE_PACKET = DATA / "capital-flow-apollo-athene-concord-named-cash-source-acquisition-pass-1.csv"
DIAG = DATA / "capital-flow-apollo-athene-concord-named-cash-source-acquisition-diagnostic-pass-1.csv"
OUT = DATA / "capital-flow-apollo-athene-concord-controlled-document-request-packet-pass-1.csv"
DIAGNOSTIC_OUT = DATA / "capital-flow-apollo-athene-concord-controlled-document-request-packet-diagnostic-pass-1.csv"

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
        "document_family": "offering-memorandum",
        "specific_document_request": "Concord Music Royalties LLC Series 2025-1/2025-2/2025-3 offering memorandum or investor presentation, including tranche table and CUSIP list.",
        "likely_controller": "Concord, Apollo Capital Solutions, ATLAS SP Partners, Redding Ridge, placement agents, rating agencies, note purchasers",
        "why_needed": "Defines issuer, note series, tranche economics, eligible collateral, noteholder rights, proceeds use, and investor allocation context.",
        "promotion_test": "Shows Series 2025-3 / CUSIP 20633K-AN-8 tranche terms and whether Athene or Apollo-managed insurance accounts were allocated the tranche.",
        "hold_test": "If only aggregate issuance or marketing language is available, keep the row at borrower/wrapper-use proxy.",
        "cash_loop_link": "legal instrument and source-to-wrapper",
        "priority_reason": "Highest leverage document because it can connect Athene's statutory CUSIP to the deal's tranche economics and investor allocation route.",
    },
    {
        "document_family": "indenture-and-supplements",
        "specific_document_request": "Base indenture, Series 2025 supplemental indenture, note purchase agreement, and variable funding note amendment.",
        "likely_controller": "Concord, trustee, legal counsel, rating agencies, Apollo/ATLAS transaction files",
        "why_needed": "Defines payment waterfall, collateral pledge, note terms, covenants, VFN terms, redemption mechanics, and investor payment rights.",
        "promotion_test": "Shows the exact waterfall and legal payment route for Series 2025 noteholders, including 2022-1 redemption mechanics and VFN refinance/extension.",
        "hold_test": "If no populated payment mechanics or CUSIP-specific series terms are available, do not claim repayment route or waterfall proof.",
        "cash_loop_link": "legal route and waterfall",
        "priority_reason": "Required to prove how cash legally moves from catalog collections through trustee accounts to noteholders.",
    },
    {
        "document_family": "trustee-remittance-reports",
        "specific_document_request": "Monthly or quarterly trustee distribution/remittance reports from closing through at least the July 2026 payment date.",
        "likely_controller": "trustee, servicer, Concord treasury, noteholders/custodians, rating agencies",
        "why_needed": "Provides actual collections, fees, interest, principal, reserve movements, coverage tests, and noteholder payment amounts.",
        "promotion_test": "Shows Series 2025-3 interest/principal distributions and lets the Athene CUSIP be tied to actual cash remittance amounts.",
        "hold_test": "KBRA timely-interest language alone remains deal-level servicing proxy, not Athene receipt.",
        "cash_loop_link": "cash-back and debt-service receipt",
        "priority_reason": "Most direct missing source for turning timely-interest proxy into cash receipt evidence.",
    },
    {
        "document_family": "series-2022-1-redemption-payoff-ledger",
        "specific_document_request": "Series 2022-1 redemption notice, payoff statement, paying-agent ledger, and settlement statement.",
        "likely_controller": "Concord, trustee, paying agent, prior noteholders, rating agencies",
        "why_needed": "Public sources say Series 2025 proceeds were used to redeem/refinance prior 2022-1 notes; this proves the actual cash use.",
        "promotion_test": "Reconciles 2025 note proceeds to 2022-1 principal, accrued interest, premiums, fees, and paying-agent cash transfer.",
        "hold_test": "If only public use-of-proceeds language is available, keep use as proxy and do not claim settlement cash.",
        "cash_loop_link": "use of proceeds",
        "priority_reason": "Concord's strongest public use claim is refinancing; payoff records are the decisive proof.",
    },
    {
        "document_family": "collateral-catalog-and-royalty-tape",
        "specific_document_request": "Collateral catalog schedule, royalty receivable tape, concentration report, valuation model, and eligibility/reserve calculations.",
        "likely_controller": "Concord, servicer, trustee, rating agencies, valuation advisor",
        "why_needed": "Identifies what operating cash-flow assets support the notes and whether cash comes from music royalty collections.",
        "promotion_test": "Shows collateral assets, royalty collection streams, obligor/platform sources, advance rates, reserves, and coverage tests supporting the notes.",
        "hold_test": "A statement that the deal is backed by more than 1.3M copyrights is collateral-type evidence, not cash-flow proof.",
        "cash_loop_link": "funded asset and operating cash source",
        "priority_reason": "Needed to convert music-catalog collateral from label to cash-generating asset evidence.",
    },
    {
        "document_family": "athene-allocation-and-trade-support",
        "specific_document_request": "Athene trade confirmation, custodian statement, statutory investment workpaper, allocation book, and sale/paydown/redemption ticket for CUSIP 20633K-AN-8.",
        "likely_controller": "Athene investment accounting, Apollo insurance asset management, custodian, broker/dealer, state examiners",
        "why_needed": "Connects the statutory CUSIP row to Athene's actual purchase/sale/receipt records and determines whether the proceeds were primary issuance, secondary sale, paydown, or redemption.",
        "promotion_test": "Matches Athene's 229.053398M USD cash-like consideration to dated trade or custodian cash movement and note balance activity.",
        "hold_test": "Statutory row presence remains named proceeds evidence but not actual cash receipt or trade settlement proof.",
        "cash_loop_link": "Athene receipt and legal-entity cash movement",
        "priority_reason": "The key missing Athene-side receipt document.",
    },
    {
        "document_family": "liability-cost-and-spread-support",
        "specific_document_request": "Athene liability funding source, credited-rate/funding-agreement cost, investment spread workpaper, and asset allocation return model for the Concord note.",
        "likely_controller": "Athene ALM, investment accounting, actuarial, Apollo insurance asset management, state examiners",
        "why_needed": "Turns gross proceeds and interest into net economic return after policyholder or funding liability cost.",
        "promotion_test": "Shows gross yield, cash receipt, liability cost, expenses, credit loss/reserve treatment, and realized spread or return for the Concord exposure.",
        "hold_test": "Do not use gross interest or proceeds as return without liability-cost and allocation support.",
        "cash_loop_link": "return model",
        "priority_reason": "Required for the user's final question: did the money come back profitably after cost of funds?",
    },
    {
        "document_family": "rating-surveillance-full-reports",
        "specific_document_request": "Full KBRA/Fitch/Moody's/S&P reports for Series 2025 issuance and 2026 surveillance, including tables omitted from public summaries.",
        "likely_controller": "rating agencies, Concord, investors, Apollo/ATLAS transaction files",
        "why_needed": "May contain deal terms, cash-flow assumptions, debt-service coverage, collateral performance, reserve levels, and payment-date metrics.",
        "promotion_test": "Shows quantitative surveillance tables that corroborate remittance, coverage, collateral performance, and waterfall operation.",
        "hold_test": "Rating press releases alone remain public proxy evidence and do not prove noteholder-level cash.",
        "cash_loop_link": "surveillance and performance",
        "priority_reason": "Likely obtainable before private allocation books and can improve cash-flow confidence quickly.",
    },
]


def current_evidence() -> str:
    athene = diag_value("athene_concord_cash_like_consideration")
    issuance = diag_value("concord_issuance_amount")
    repay = diag_value("concord_company_repayment_reference")
    kbra = diag_value("kbra_2022_1_redemption_reference")
    return (
        f"Current public/local evidence: Athene same-CUSIP cash-like consideration {athene} USD; "
        f"Concord issuance {issuance} USD; Concord repayment reference {repay} USD; "
        f"KBRA redemption reference {kbra} USD; deal-level timely-interest proxy visible."
    )


def main() -> None:
    evidence = current_evidence()
    source_rows = read_rows(SOURCE_PACKET)
    rows = []
    for idx, request in enumerate(REQUESTS, start=1):
        rows.append(
            {
                "request_id": f"CFAACNCDR-{idx:03d}",
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
                "next_action": "request or locate the named document, extract populated fields, and rerun the Concord proof promotion test",
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
        ("athene_concord_cash_like_consideration", diag_value("athene_concord_cash_like_consideration"), "USD"),
        ("concord_issuance_amount", diag_value("concord_issuance_amount"), "USD"),
        ("concord_company_repayment_reference", diag_value("concord_company_repayment_reference"), "USD"),
        ("concord_vfn_refinance_reference", diag_value("concord_vfn_refinance_reference"), "USD"),
        ("kbra_2022_1_redemption_reference", diag_value("kbra_2022_1_redemption_reference"), "USD"),
    ]
    with DIAGNOSTIC_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DIAGNOSTIC_FIELDS)
        writer.writeheader()
        for idx, (metric, value, units) in enumerate(diagnostics, start=1):
            writer.writerow(
                {
                    "diagnostic_id": f"CFAACNCDRD-{idx:03d}",
                    "metric": metric,
                    "value": value,
                    "units": units,
                    "proof_use": "controls Concord controlled-document request package",
                    "boundary": "request diagnostics define missing documents; they do not prove the documents were obtained or extracted",
                    "next_action": "execute document acquisition, then promote or hold each cash-loop link based on populated evidence",
                }
            )

    print(f"wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")
    print(f"wrote {len(diagnostics)} rows to {DIAGNOSTIC_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
