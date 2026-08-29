# Capital Flow Debt Refinancing SEC Source/Denominator Pass 1

## Purpose

This page starts upgrading the `debt_refinancing_and_facilities` lane from queued status inside the `35` company cash-realization pilot.

The question is:

`Can the debt/refinancing pilot rows move from queued to SEC source-visible denominator evidence?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-debt-refinancing-sec-source-denominator-pass-1.csv`

The upstream denominator control pass is:

`/cluster/capital-flow-519-company-denominator-control-pass-1.md`

The Wheaton metric extraction is:

`/cluster/capital-flow-wheaton-6k-ifrs-debt-cash-extraction-pass-1.md`

## Current Answer

`Yes at first-pass denominator level. PBF, Devon, Matador, Liberty Broadband, and Wheaton now have current SEC source routes, local filing copies, and first-pass cash/debt/cash-flow denominators. Wheaton required a separate SEC-rendered IFRS table parse from the 6-K exhibits, which is now captured in the Wheaton 6-K IFRS debt/cash extraction pass.`

## Source Coverage

| Company | Filing | Local Status | Current Upgrade |
|---|---|---|---|
| PBF Energy | Q2 `2026` `10-Q`, filed `2026-07-30` | SEC filing and companyfacts cached | `source-visible-denominator-started` |
| Devon Energy | Q2 `2026` `10-Q`, filed `2026-08-05` | SEC filing and companyfacts cached | `source-visible-denominator-started` |
| Matador Resources | Q2 `2026` `10-Q`, filed `2026-08-07` | SEC filing and companyfacts cached | `source-visible-denominator-started` |
| Liberty Broadband | Q2 `2026` `10-Q`, filed `2026-07-29` | SEC filing and companyfacts cached | `source-visible-denominator-started` |
| Wheaton Precious Metals | Q2 `2026` `6-K`, filed `2026-08-07` | SEC filing, exhibits, rendered XBRL reports, and companyfacts cached | `source-visible-denominator-started` |

## First Denominators

| Company | Cash / Liquidity | Debt | Cash Flow / Repayment |
|---|---|---|---|
| PBF Energy | Cash and cash equivalents `894.1M USD` at `2026-06-30` | Debt carrying amount `1.800B USD`; noncurrent long-term debt `1.7491B USD` | YTD operating cash flow `1.2651B USD`; PP&E payments `476.5M USD`; debt/capital lease repayments `6.0M USD` |
| Devon Energy | Cash and cash equivalents `950.0M USD` at `2026-06-30` | Long-term debt `11.388B USD`; current long-term debt `1.497B USD` | YTD operating cash flow `5.329B USD`; Q2 operating cash flow `3.674B USD`; long-term debt repayments `500.0M USD`; dividends `521.0M USD` YTD; repurchases `266.0M USD` YTD |
| Matador Resources | Cash and cash equivalents `26.318M USD` at `2026-06-30` | Long-term debt `4.216410B USD`; secured long-term debt `911.0M USD`; debt instrument face amount `2.366410B USD` | YTD operating cash flow `1.407674B USD`; secured debt proceeds `209.0M USD`; unsecured debt proceeds `750.0M USD`; secured debt repayments `181.0M USD` |
| Liberty Broadband | Cash and cash equivalents `43.0M USD` at `2026-06-30` | Current debt `864.0M USD`; long-term debt `1.223B USD`; noncurrent long-term debt `359.0M USD` | YTD continuing-operations operating cash flow `-118.0M USD`; long-term debt proceeds `1.239B USD`; long-term debt repayments `1.771B USD` |
| Wheaton Precious Metals | Cash and cash equivalents `100.192M USD` at `2026-06-30` | Gross bank debt `1.972B USD`; Term Loan `1.500B USD`; Revolving Credit Facility `472.000M USD` | Q2 operating cash flow `649.518M USD`; YTD operating cash flow `1.415340B USD`; Q2 bank debt drawn `2.700B USD`; Q2 bank debt repaid `728.000M USD`; Q2 upfront PMPA/royalty cash payments `4.5B USD`, including `4.3B USD` BHP Antamina PMPA |

## What This Adds

This pass moves the debt/refinancing lane from:

`queued denominator class`

to:

`SEC source route -> local filing copy -> companyfacts cache -> first cash/debt/cash-flow denominator`

for all five companies.

## What It Does Not Prove

This pass does not prove:

- exact use of proceeds
- refinancing purpose
- covenant headroom
- debt-service capacity after all adjustments
- asset-level or project-level cash return
- whether shareholder returns were debt-funded or internally funded
- Wheaton's stream-level cash return, PMPA margin, debt-service waterfall, and lender allocation

## Decision

`debt-refinancing-sec-source-denominator-started`

The first queued lane is no longer purely queued. All five companies now have first-pass SEC denominator evidence. The next standard is not route discovery; it is debt-footnote, use-of-proceeds, covenant, and asset-level cash-return extraction.

## Safe Claim

`The debt/refinancing pilot lane now has first-pass SEC source coverage. PBF, Devon, Matador, Liberty Broadband, and Wheaton have source-visible cash, debt, and cash-flow denominators. These rows support denominator work, not final refinancing-use, covenant-headroom, lender-allocation, or asset-return claims.`

## Next Work

1. Parse debt footnotes and liquidity sections from the four source-visible `10-Q` filings.
2. Parse Wheaton's Antamina PMPA terms, expected deliveries, credit-facility pricing, and debt-service implications.
3. Update the 35-company source table and denominator control table only when debt-lane metrics clear the stricter source/use test.
