#!/usr/bin/env python3
"""Build Athene legal-entity income/cash bridge from statutory extracted rows."""

from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMPACT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-compact-extraction-pass-1.csv"
RECON = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-reconciliation-diagnostic-pass-1.csv"
OUT = ROOT / "analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-legal-entity-income-cash-bridge-pass-1.csv"

FIELDNAMES = [
    "bridge_id",
    "bridge_layer",
    "metric",
    "numerator_value",
    "numerator_units",
    "denominator_value",
    "denominator_units",
    "ratio",
    "current_status",
    "what_it_proves",
    "boundary",
    "next_proof",
]


def compact_metrics() -> dict[str, Decimal]:
    metrics: dict[str, Decimal] = {}
    with COMPACT.open(newline="") as f:
        for row in csv.DictReader(f):
            units = row["units"]
            if units == "B USD":
                metrics[row["metric_name"]] = Decimal(row["metric_value"]) * Decimal("1000000000")
            elif units == "M USD":
                metrics[row["metric_name"]] = Decimal(row["metric_value"]) * Decimal("1000000")
    return metrics


def reconciliation_metrics() -> dict[str, Decimal]:
    metrics: dict[str, Decimal] = {}
    with RECON.open(newline="") as f:
        for row in csv.DictReader(f):
            if row["diagnostic_type"] != "book-value-reconciliation":
                continue
            scope = row["schedule_scope"]
            metrics[f"{scope}:parser_book"] = Decimal(row["parser_value"])
            metrics[f"{scope}:reference_book"] = Decimal(row["statutory_reference_value"])
            metrics[f"{scope}:coverage"] = Decimal(row["coverage_ratio"])
    return metrics


def billion(value: Decimal) -> str:
    return f"{(value / Decimal('1000000000')):.9f}"


def pct(num: Decimal, den: Decimal) -> str:
    if den == 0:
        return ""
    return f"{(num / den * Decimal('100')):.4f}%"


def add(
    rows: list[dict[str, str]],
    bridge_layer: str,
    metric: str,
    numerator: Decimal,
    denominator: Decimal,
    current_status: str,
    what_it_proves: str,
    boundary: str,
    next_proof: str,
) -> None:
    rows.append(
        {
            "bridge_id": f"CFAALEICB-{len(rows) + 1:03d}",
            "bridge_layer": bridge_layer,
            "metric": metric,
            "numerator_value": billion(numerator),
            "numerator_units": "B USD",
            "denominator_value": billion(denominator),
            "denominator_units": "B USD",
            "ratio": pct(numerator, denominator),
            "current_status": current_status,
            "what_it_proves": what_it_proves,
            "boundary": boundary,
            "next_proof": next_proof,
        }
    )


def main() -> None:
    compact = compact_metrics()
    recon = reconciliation_metrics()

    schedule_d_book = compact["total_bonds_book_adjusted_carrying_value"]
    near_reconciled_schedule_d = recon["Schedule D Part 1 Section 1 plus Section 2:parser_book"]
    mortgage_loans = compact["first_lien_mortgage_loans"]
    schedule_ba = compact["schedule_ba_net_admitted_assets"]
    cash_short = compact["cash_cash_equivalents_short_term_investments"]
    life_reserve = compact["aggregate_reserve_for_life_contracts"]
    deposit_liability = compact["liability_for_deposit_type_contracts"]
    liability_base = life_reserve + deposit_liability
    invested_base = schedule_d_book + mortgage_loans + schedule_ba + cash_short
    nii = compact["net_investment_income"]
    cash_nii = compact["cash_flow_net_investment_income"]
    gross_collected = compact["total_gross_investment_income_collected"]
    gross_earned = compact["total_gross_investment_income_earned"]
    other_bond_collected = compact["other_unaffiliated_bond_income_collected"]
    affiliated_bond_collected = compact["affiliated_bond_income_collected"]
    mortgage_collected = compact["mortgage_loan_income_collected"]
    bond_income_collected = other_bond_collected + affiliated_bond_collected
    bond_proceeds = compact["bond_proceeds_sold_matured_repaid"]
    mortgage_proceeds = compact["mortgage_loan_proceeds_sold_matured_repaid"]
    imr = compact["current_year_end_imr"]
    avr = compact["avr_accumulated_balance"]
    otti = compact["current_year_otti_recognized"]

    rows: list[dict[str, str]] = []
    add(
        rows,
        "asset-base",
        "near_reconciled_schedule_d_parser_book_to_statutory_bond_reference",
        near_reconciled_schedule_d,
        schedule_d_book,
        "near-reconciled-hold",
        "The parsed Schedule D bond population is close to the statutory bond base and can support residual tie-out work.",
        "Not final accounting proof until residual difference is explained.",
        "Define final reconciliation tolerance and inspect residual continuation/subtotal candidates.",
    )
    add(
        rows,
        "asset-income",
        "net_investment_income_to_core_invested_asset_base",
        nii,
        invested_base,
        "legal-entity-income-visible",
        "Athene generated statutory net investment income against the extracted bond, mortgage, BA, and liquid asset base.",
        "This is entity-level yield, not holding-level income or borrower cash receipt.",
        "Join Schedule D/BA holdings to income, disposals, impairments, and realized gain/loss schedules.",
    )
    add(
        rows,
        "cash-conversion",
        "cash_flow_net_investment_income_to_summary_net_investment_income",
        cash_nii,
        nii,
        "cash-income-proxy-visible",
        "The cash-flow statement supports most of the summary net investment income as cash-flow net investment income.",
        "Cash-flow net investment income is not allocated to individual holdings.",
        "Normalize the page 18 income exhibit and test received-interest fields by Schedule D category.",
    )
    add(
        rows,
        "income-quality",
        "gross_collected_investment_income_to_gross_earned_investment_income",
        gross_collected,
        gross_earned,
        "collected-versus-earned-visible",
        "Collected investment income is close to earned investment income at the legal-entity level.",
        "Collected/earned proximity does not prove collection by issuer or asset.",
        "Map collected and earned income categories to Schedule D, mortgage loan, and Schedule BA holdings.",
    )
    add(
        rows,
        "bond-income",
        "collected_bond_income_to_statutory_schedule_d_bond_base",
        bond_income_collected,
        schedule_d_book,
        "bond-income-category-visible",
        "Other unaffiliated plus affiliated bond income is visible against the Schedule D bond base.",
        "The statutory exhibit is category-level and does not assign income to CUSIPs.",
        "Separate affiliated, unaffiliated, issuer-credit, ABS, and other bond income where page detail allows.",
    )
    add(
        rows,
        "mortgage-income",
        "collected_mortgage_loan_income_to_first_lien_mortgage_loans",
        mortgage_collected,
        mortgage_loans,
        "mortgage-income-category-visible",
        "Mortgage-loan income is visible against the first-lien mortgage-loan base.",
        "This does not identify borrowers or loan-level repayment behavior.",
        "Locate mortgage loan schedules and repayment/maturity detail if available.",
    )
    add(
        rows,
        "investment-turnover",
        "bond_sale_maturity_repayment_proceeds_to_schedule_d_bond_base",
        bond_proceeds,
        schedule_d_book,
        "bond-proceeds-visible",
        "The cash-flow statement shows large proceeds from bonds sold, matured, or repaid.",
        "Not matched to Schedule D Part 4 disposal rows or realized gains/losses by asset.",
        "Extract Schedule D Part 4 and match disposal proceeds to CUSIP/issuer where possible.",
    )
    add(
        rows,
        "investment-turnover",
        "mortgage_loan_sale_maturity_repayment_proceeds_to_mortgage_loan_base",
        mortgage_proceeds,
        mortgage_loans,
        "mortgage-proceeds-visible",
        "The cash-flow statement shows material mortgage-loan proceeds from sale, maturity, or repayment.",
        "Not loan-level payback proof.",
        "Extract mortgage loan disposal/repayment schedules if available.",
    )
    add(
        rows,
        "liability-funding",
        "core_invested_asset_base_to_life_reserve_plus_deposit_liability_base",
        invested_base,
        liability_base,
        "asset-liability-scale-visible",
        "The extracted core invested asset base is larger than the life reserve plus deposit-type liability base.",
        "This is not liability-cost, duration, credited-rate, or spread proof.",
        "Extract reserve interest, deposit-type contract cost, credited rates, surrender behavior, and ALM detail.",
    )
    add(
        rows,
        "reserve-pressure",
        "asset_valuation_reserve_to_core_invested_asset_base",
        avr,
        invested_base,
        "statutory-risk-reserve-visible",
        "The asset valuation reserve gives a legal-entity credit/equity risk reserve scale against invested assets.",
        "AVR is not issuer-level loss or realized cash return.",
        "Join AVR components to NAIC distribution and impairments.",
    )
    add(
        rows,
        "reserve-pressure",
        "interest_maintenance_reserve_to_bond_proceeds",
        imr,
        bond_proceeds,
        "realized-gain-loss-smoothing-visible",
        "The IMR scale is visible against bond sale/maturity/repayment proceeds.",
        "IMR does not itself identify the sold holdings or realized gains/losses.",
        "Extract Schedule D Part 4 realized gain/loss rows.",
    )
    add(
        rows,
        "credit-cost",
        "current_year_otti_to_statutory_schedule_d_bond_base",
        otti,
        schedule_d_book,
        "impairment-scale-visible",
        "Current-year OTTI is visible against the Schedule D bond base.",
        "OTTI is not yet assigned to issuers or borrowers.",
        "Locate issuer-level impairment detail and join to Schedule D holdings.",
    )

    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
