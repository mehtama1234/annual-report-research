# Capital Flow KKR Global Atlantic Accordia Compact Extraction Pass 1

## Purpose

This pass starts the actual Global Atlantic statutory extraction after source acquisition and schedule location.

It asks:

`Can KKR/Global Atlantic insurance capital be moved from route evidence into legal-entity assets, liabilities, income, cash flow, and first named Schedule D destination samples?`

The structured companion tables are:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-compact-extraction-pass-1.csv`

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-schedule-d-sample-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-compact-extraction-diagnostic-pass-1.csv`

## Short Answer

`Yes, at compact legal-entity bridge level. Accordia Q4 2025 shows 7.318322B USD of Schedule D bond assets, 1.151481B USD of first-lien mortgage loans, 339.923533M USD of Schedule BA other invested assets, 5.933275B USD of life reserves, 258.307445M USD of deposit-type liabilities, 549.713557M USD of statutory net investment income, 546.289441M USD of cash-flow net investment income, and 30 first Schedule D named security samples. This is not full named cash proof because the Schedule D numeric columns, holding-level income, proceeds, borrower use, liability-cost spread, and return model are not yet reconciled.`

## Extracted Summary Evidence

| Field | Page | Value | Proof Use |
|---|---:|---:|---|
| bonds_schedule_d_net_admitted_assets | `3` | 7318322163 | legal-entity Schedule D bond base |
| common_stocks_schedule_d_net_admitted_assets | `3` | 800482505 | equity/common-stock asset base |
| first_lien_mortgage_loans | `3` | 1151480925 | mortgage-loan asset base |
| cash_equivalents_short_term_investments | `3` | 236260959 | liquidity and cash-equivalent bridge |
| schedule_ba_other_invested_assets | `3` | 339923533 | Schedule BA other-invested-asset base |
| aggregate_reserve_for_life_contracts | `4` | 5933274992 | insurance liability source-pool context |
| deposit_type_contract_liability | `4` | 258307445 | deposit-type liability source-pool context |
| funds_held_under_coinsurance | `4` | 4183653692 | coinsurance/funds-held liability route |
| summary_net_investment_income | `5` | 549713557 | statutory investment-income bridge |
| summary_net_income | `5` | -86737835 | legal-entity earnings endpoint |
| cash_flow_net_investment_income | `6` | 546289441 | cash-flow support for investment income |
| net_cash_from_operations | `6` | -251005185 | legal-entity operating cash-flow endpoint |
| mortgage_loans_sold_matured_repaid | `6` | 113578284 | mortgage-loan repayment/disposition cash route |
| affiliate_bond_income_collected | `15` | 66926995 | affiliate bond-income bucket |
| mortgage_loan_income_collected | `15` | 57708561 | mortgage-loan income bucket |
| total_gross_investment_income_collected | `15` | 605073293 | gross investment-income denominator |
| net_investment_income_exhibit | `15` | 549713557 | income exhibit ties to summary net investment income |

## Named Schedule D Samples

| ID | Schedule | Page | CUSIP | Issuer / Description | Date |
|---|---|---:|---|---|---|
| CFKKRGACEDS-001 | Schedule D Part 3 acquired during year | 250 | 04316J-AG-4 | ARTHUR J. GALLAGHER & CO. | 05/19/2025 |
| CFKKRGACEDS-002 | Schedule D Part 3 acquired during year | 250 | 04316J-AN-9 | ARTHUR J. GALLAGHER & CO. | 07/02/2025 |
| CFKKRGACEDS-003 | Schedule D Part 3 acquired during year | 250 | 045054-AL-7 | ASHTEAD CAPITAL INC | 11/25/2025 |
| CFKKRGACEDS-004 | Schedule D Part 3 acquired during year | 250 | 045941-AA-9 | ASURION LLC | 12/10/2025 |
| CFKKRGACEDS-005 | Schedule D Part 3 acquired during year | 250 | 04621W-AF-7 | ASSURED GUARANTY US HOLDINGS INC | 11/25/2025 |
| CFKKRGACEDS-006 | Schedule D Part 3 acquired during year | 250 | 04621X-AD-0 | ASSURANT INC | 11/25/2025 |
| CFKKRGACEDS-007 | Schedule D Part 3 acquired during year | 250 | 052113-AB-3 | AUSGRID FINANCE PTY LTD | 11/25/2025 |
| CFKKRGACEDS-008 | Schedule D Part 3 acquired during year | 250 | 052528-AT-3 | AUSTRALIA AND NEW ZEALAND BANKING GROUP | 08/13/2025 |
| CFKKRGACEDS-009 | Schedule D Part 3 acquired during year | 250 | 052528-AV-8 | AUSTRALIA AND NEW ZEALAND BANKING GROUP | 08/13/2025 |
| CFKKRGACEDS-010 | Schedule D Part 3 acquired during year | 250 | 052769-AJ-5 | AUTODESK INC | 11/25/2025 |
| CFKKRGACEDS-011 | Schedule D Part 3 acquired during year | 250 | 053015-AG-8 | AUTOMATIC DATA PROCESSING INC | 11/25/2025 |
| CFKKRGACEDS-012 | Schedule D Part 3 acquired during year | 250 | 05329W-AT-9 | AUTONATION INC | 11/25/2025 |
| CFKKRGACEDS-013 | Schedule D Part 3 acquired during year | 250 | 053611-AN-9 | AVERY DENNISON CORP | 11/25/2025 |
| CFKKRGACEDS-014 | Schedule D Part 3 acquired during year | 250 | 05369A-AT-8 | AVIATION CAPITAL GROUP LLC | 11/25/2025 |
| CFKKRGACEDS-015 | Schedule D Part 3 acquired during year | 250 | 05401A-BC-4 | AVOLON HOLDINGS FUNDING LTD | 12/16/2025 |

## What This Tells Us

The KKR/Global Atlantic route now has an actual legal-entity bridge:

`KKR / Global Atlantic -> Accordia Life and Annuity Company -> statutory liabilities and coinsurance/funds-held routes -> Schedule D bonds, mortgage loans, Schedule BA assets, cash/short-term investments -> statutory investment income and cash-flow support -> named Schedule D securities`

The first named destination sample confirms the filing can expose exact securities and issuers, not just asset-class totals.

## Boundary

This is still not full named cash proof.

It does not yet prove:

1. full Schedule D position values by CUSIP
2. holding-level investment income
3. sale/redemption/disposal proceeds by CUSIP
4. borrower receipt or use of proceeds
5. liability-cost spread by reserve/funding block
6. FHLB, funds-withheld, or coinsurance economic waterfall
7. IRR, NPV, ROIC, cash-on-cash return, or platform profit

## Next Action

Build the full Accordia Schedule D parser for pages `220-270`, with separate outputs for owned bonds, acquired securities, disposed securities, and same-year acquisition/disposal rows.

## Decision

`kkr-global-atlantic-accordia-compact-extraction-legal-entity-bridge-visible-schedule-d-parser-next`
