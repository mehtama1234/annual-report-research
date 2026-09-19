# Consumer-credit platforms valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Affirm and Synchrony from payment and merchant evidence
into separate credit-platform valuation objects. It keeps Affirm's merchant-
conversion and funded-loan model distinct from Synchrony's large private-label
receivables balance sheet and household-credit cycle.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment/denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Affirm | Merchant-conversion and consumer-credit earnings after funding, loan-sale/securitization, provision, fraud, servicing, merchant settlement, SBC, and dilution | Underwriting/data, receivables, servicing, funding, card network, merchant integrations, securitization, SBC, and common capital | Consumer loss, funding spread, securitization access, merchant concentration, loan-sale accounting, fraud, or dilution | GMV and consumers rise while RLTC, provision, funding cost, receivable quality, loan-sale dependence, or diluted residual deteriorate |
| Synchrony | Merchant-linked revolving and installment credit earnings after funding, charge-offs, reserves, rewards/promotional cost, partner economics, capital, and dilution | Receivables, deposits/securitization, underwriting, servicing/fraud, merchant programs, rewards, technology, reserves, and common capital | Household affordability, charge-off/vintage deterioration, deposit or securitization funding, partner loss, rates, capital, or regulatory stress | Purchase volume and NIM rise while charge-offs, delinquencies, allowance, funding cost, partner concentration, or tangible common value weaken |

## Current evidence anchors

- Affirm FY2025 GMV was about `$36.7B`, revenue about `$3.2B`, and FY2026
  nine-month operating cash flow `$935M`; provision for losses was `$573M`,
  SBC `$379M`, and funding debt/securitization obligations approximately
  `$7.8B` principal at March 31, 2026.
- Synchrony FY2025 net earnings were `$3.552B`, purchase volume `$182.3B`,
  loan receivables `$103.8B`, NIM `15.24%`, net charge-off rate `5.65%`,
  allowance for credit losses approximately `$10.4B`, and deposits `$81.1B`.
- Synchrony Q2 2026 purchase volume was `$49.8B`, receivables `$102.2B`, and
  CET1 `13.2%`; purchase volume and account growth are activity inputs, not
  common-owner cash.

## QoE and financial-shenanigans prompts

1. For Affirm, separate GMV, merchant fees, interest/fee income, RLTC, loan
   originations, loan sales, servicing, provision, funding cost, and cash.
2. Reconcile Affirm securitization and loan-sale proceeds, receivable aging,
   consumer vintages, merchant settlement, fraud, and capitalized SBC.
3. For Synchrony, track purchase volume, receivables, delinquencies, charge-off
   vintages, allowance, rewards/promotional financing, deposits, securitization,
   and partner economics.
4. Test whether high NIM compensates for credit and funding risk rather than
   treating it as a software-like margin.
5. Treat GMV, purchase volume, adjusted earnings, reported OCF, loan sales,
   dividends, and buybacks as diagnostic or residual measures until credit,
   funding, capital, and diluted claims are joined.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what merchant conversion, credit loss,
funding spread, receivable growth, securitization access, partner economics,
capital ratio, payout, and cost of equity the valuation requires. The Lyn
Alden-style stress test asks whether household affordability, rates, funding
markets, consumer vintages, merchant health, and collateral can absorb a credit
cycle without forced deleveraging or common dilution.

## Promotion boundary

`consumer-credit-qualified; loss-funding-and-securitization-open; no-ranking`

Promotion requires same-entity, same-period joins from merchant transaction
through receivable collection, provision/charge-off, funding or securitization,
servicing, capital requirements, partner settlement, debt, and diluted common
residual. GMV, purchase volume, NIM, loan sales, adjusted earnings, reported
OCF, dividends, and buybacks remain diagnostic inputs.

## Sources

- [Affirm deep company packet](../deep-company-pages/affirm-holdings-inc.md)
- [Synchrony deep company packet](../deep-company-pages/synchrony-financial.md)
