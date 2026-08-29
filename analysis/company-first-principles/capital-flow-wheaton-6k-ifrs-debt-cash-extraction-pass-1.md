# Capital Flow Wheaton 6-K IFRS Debt/Cash Extraction Pass 1

## Purpose

This page resolves the Wheaton metric hold from the debt/refinancing SEC source-denominator pass.

The question is:

`Can Wheaton's Q2 2026 foreign-issuer 6-K be parsed into cash, debt, operating cash flow, and stream-acquisition funding denominators?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-wheaton-6k-ifrs-debt-cash-extraction-pass-1.csv`

The upstream debt/refinancing pass is:

`/cluster/capital-flow-debt-refinancing-sec-source-denominator-pass-1.md`

## Current Answer

`Yes, at source-visible denominator level. Wheaton's wrapper 6-K was not enough by itself, but the SEC exhibit and rendered XBRL report files expose the needed tables. The pass extracts 10 rows covering sales, operating cash flow, cash, bank debt, revolver debt, term-loan debt, bank-debt draw/repayment, and BHP Antamina / PMPA upfront-payment context.`

## Key Extracted Metrics

| Metric | Period | Value | Source |
|---|---|---:|---|
| Sales | Q2 `2026` | `929.201M USD` | SEC rendered earnings statement |
| Sales | YTD `2026` | `1.830670B USD` | SEC rendered earnings statement |
| Operating cash flow | Q2 `2026` | `649.518M USD` | SEC rendered cash-flow statement |
| Operating cash flow | YTD `2026` | `1.415340B USD` | SEC rendered cash-flow statement |
| Cash and cash equivalents | June `30`, `2026` | `100.192M USD` | SEC rendered supplemental cash table |
| Gross bank debt outstanding | June `30`, `2026` | `1.972B USD` | SEC rendered credit-facility table |
| Revolving Credit Facility gross debt | June `30`, `2026` | `472.000M USD` | SEC rendered credit-facility table |
| Term Loan gross debt | June `30`, `2026` | `1.500B USD` | SEC rendered credit-facility table |
| Bank debt drawn / repaid | Q2 `2026` | `2.700B USD` drawn; `728.000M USD` repaid | SEC rendered cash-flow statement |
| Upfront cash payments | Q2 `2026` | `4.5B USD` total; `4.3B USD` BHP Antamina PMPA | MD&A |

## What This Adds

Wheaton moves from:

`source-route-visible-metric-hold`

to:

`source-visible-denominator-started`

This matters because the debt/refinancing lane now has first-pass SEC denominator evidence for all five pilot rows.

## Boundary

This pass still does not prove:

- stream-level return
- mine delivery timing
- PMPA cash margin by asset
- debt-service waterfall
- full source/use table for the BHP Antamina PMPA
- lender allocation or credit pricing

## Decision

`wheaton-6k-ifrs-debt-cash-extracted`

The Wheaton foreign-issuer route is no longer only a route. It now has Q2 `2026` cash, debt, financing, sales, operating cash flow, and stream-acquisition funding context extracted from SEC-hosted exhibits and rendered XBRL report files.

## Safe Claim

`Wheaton has source-visible Q2 2026 debt/cash denominators: 100.192M USD cash, 1.972B USD gross bank debt, 1.500B USD term-loan debt, 472.000M USD revolver debt, 649.518M USD Q2 operating cash flow, 1.415340B USD YTD operating cash flow, and MD&A context tying the quarter to 4.5B USD of upfront PMPA/royalty cash payments including 4.3B USD for BHP Antamina. This is not stream-level return proof.`

## Next Work

1. Extract the Antamina PMPA terms and expected delivery schedule.
2. Add debt facility pricing, covenant, maturity, and lender detail.
3. Build a stream-level source/use/output/cash bridge only if PMPA and production-delivery evidence can be joined.
