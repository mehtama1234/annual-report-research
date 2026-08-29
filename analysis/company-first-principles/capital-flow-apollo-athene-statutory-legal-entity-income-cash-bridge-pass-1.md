# Capital Flow Apollo Athene Statutory Legal-Entity Income Cash Bridge Pass 1

## Purpose

This pass moves Apollo/Athene from near-reconciled Schedule D holdings toward the next cash question:

`Does the Athene legal entity show asset income, cash conversion, investment turnover, liability funding scale, and credit/reserve pressure?`

The generated companion table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-legal-entity-income-cash-bridge-pass-1.csv`

The bridge script is:

`scripts/build-athene-legal-entity-income-bridge.py`

The upstream Schedule D residual diagnostic is:

`/cluster/capital-flow-apollo-athene-statutory-schedule-d-residual-gap-diagnostic-pass-1.md`

## Short Answer

`Yes, at legal-entity bridge level. Athene Annuity and Life Company shows a near-reconciled Schedule D bond base, statutory net investment income, cash-flow support for investment income, collected-versus-earned income proximity, bond and mortgage-loan proceeds, liability-base scale, AVR reserve pressure, IMR mechanics, and current-year OTTI. This is a real upgrade from "where are assets?" to "did the legal entity generate cash/income from the asset base?" It is still not full named cash proof because the income, proceeds, impairments, and liability cost are not yet joined to individual holdings, borrowers, or return models.`

## Bridge Results

| Bridge | Numerator | Denominator | Ratio | Status |
|---|---:|---:|---:|---|
| Near-reconciled Schedule D parser book to statutory bond reference | `158.619095705B USD` | `158.852395201B USD` | `99.8531%` | near-reconciled hold |
| Net investment income to core invested asset base | `12.732699320B USD` | `270.261704399B USD` | `4.7112%` | legal-entity income visible |
| Cash-flow net investment income to summary net investment income | `12.281980822B USD` | `12.732699320B USD` | `96.4601%` | cash-income proxy visible |
| Gross collected investment income to gross earned investment income | `13.601183683B USD` | `14.010808604B USD` | `97.0764%` | collected-versus-earned visible |
| Collected bond income to statutory Schedule D bond base | `7.859004314B USD` | `158.852395201B USD` | `4.9474%` | bond-income category visible |
| Collected mortgage-loan income to first-lien mortgage loans | `4.557162846B USD` | `84.664838463B USD` | `5.3826%` | mortgage-income category visible |
| Bond sale/maturity/repayment proceeds to Schedule D bond base | `54.035221430B USD` | `158.852395201B USD` | `34.0160%` | bond proceeds visible |
| Mortgage-loan sale/maturity/repayment proceeds to mortgage-loan base | `12.676073505B USD` | `84.664838463B USD` | `14.9721%` | mortgage proceeds visible |
| Core invested asset base to life reserve plus deposit liability base | `270.261704399B USD` | `174.875533582B USD` | `154.5452%` | asset-liability scale visible |
| Asset valuation reserve to core invested asset base | `6.291800508B USD` | `270.261704399B USD` | `2.3280%` | statutory risk reserve visible |
| Interest maintenance reserve to bond proceeds | `219.835675M USD` | `54.035221430B USD` | `0.4068%` | realized-gain/loss smoothing visible |
| Current-year OTTI to Schedule D bond base | `110.227270M USD` | `158.852395201B USD` | `0.0694%` | impairment scale visible |

## What This Tells Us

This is the clearest Apollo/Athene money-flow statement so far:

`policyholder/reserve/deposit-type liability channel -> Athene legal entity -> bonds, mortgage loans, Schedule BA assets, and liquid assets -> statutory investment income and investment cash flow -> proceeds, reserves, IMR/AVR, and impairment pressure`

In simpler words:

Athene is not just holding a large asset book. The statutory statement shows the legal entity earned investment income, collected most of the income it earned, generated investment-income cash flow, and received large proceeds from bond and mortgage-loan turnover.

## What It Proves

This pass proves:

1. the near-reconciled Schedule D base can be used as a legal-entity asset denominator with a hold flag
2. statutory net investment income is visible against the core invested asset base
3. cash-flow net investment income supports the income line at `96.4601%`
4. collected gross investment income is close to earned gross investment income at `97.0764%`
5. bond income and mortgage-loan income are visible by statutory category
6. bond and mortgage-loan sale/maturity/repayment proceeds are visible
7. liability scale is visible through life reserves and deposit-type contracts
8. risk and realized-gain/loss reserve mechanics are visible through AVR and IMR
9. current-year OTTI is visible as a credit-cost pressure measure

## What It Still Does Not Prove

It does not yet prove:

1. income by CUSIP or issuer
2. cash received from any specific borrower
3. disposal proceeds by holding
4. realized gain/loss by holding
5. impairment by holding
6. liability cost or credited rate by product block
7. legal-entity spread after policyholder funding cost
8. asset-level IRR, NPV, ROIC, payback, or cash yield

## Decision

`apollo-athene-statutory-legal-entity-income-cash-bridge-visible-holding-join-next`

Apollo/Athene now has legal-entity asset base, income, cash-flow, proceeds, liability-scale, reserve-pressure, and impairment-scale evidence. The next gate is joining these summary/category cash lines to Schedule D/BA holdings and liability-cost schedules.

## Safe Claim

`Athene Annuity and Life Company shows a statutory legal-entity bridge from assets to income and cash-flow: 12.732699320B USD of net investment income, 12.281980822B USD of cash-flow net investment income, 13.601183683B USD of collected gross investment income, 54.035221430B USD of bond sale/maturity/repayment proceeds, and a near-reconciled 158.619095705B USD parsed Schedule D bond base. This supports legal-entity income/cash conversion language, not holding-level borrower cash or asset-return proof.`

## Next Work

1. Extract Schedule D Part 4 disposal rows and match proceeds/gains/losses to CUSIPs where possible.
2. Normalize page `18` income exhibit by asset class and compare it to Schedule D income/received-interest fields.
3. Extract Schedule BA detail for other invested assets and income.
4. Extract liability-cost or credited-rate schedules for reserves and deposit-type contracts.
5. Build the first legal-entity spread bridge after liability-cost extraction.
