# Capital Flow Bank Denominator Comparison

## Why This Pass Exists

The Apollo/Ares source work proves that private-credit platforms have large inflows, originations, AUM, and deployment.

It does not by itself prove that private credit is replacing bank lending.

To test that harder claim, we need a denominator: the size of bank credit and bank lending categories. This pass adds Federal Reserve H.8 data via FRED and compares the Apollo/Ares numbers against bank-credit stocks.

## Local Data Files

- Bank denominator extractions: `analysis/company-first-principles/data/capital-flow-bank-denominator-extractions.csv`
- Private-credit comparison table: `analysis/company-first-principles/data/capital-flow-private-credit-bank-denominator-comparison.csv`
- Bank-credit trend table: `analysis/company-first-principles/data/capital-flow-bank-credit-trends.csv`
- Cross-BDC bank scale comparison: `analysis/company-first-principles/data/capital-flow-cross-bdc-bank-scale-comparison.csv`
- Raw FRED files: `raw/primary-sources/capital-flow/market-denominators/fred/`
- Refresh script: `scripts/refresh-bank-credit-denominators.py`

Refresh status: rerun on `2026-08-24`. FRED returned the same latest available rows as the local files: weekly series through `2026-08-12` and monthly series through `2026-07-01`.

## Bank-Credit Denominators

| Series | Latest Date | Latest Value | Why It Matters |
|---|---:|---:|---|
| Commercial and Industrial Loans, All Commercial Banks (`BUSLOANS`) | `2026-07-01` | `2.899T USD` | Best broad U.S. bank denominator for corporate lending displacement. |
| Loans and Leases in Bank Credit, All Commercial Banks (`TOTLL`) | `2026-08-12` | `13.983T USD` | Broad all-bank loan book denominator. |
| Bank Credit, All Commercial Banks (`TOTBKCR`) | `2026-08-12` | `19.796T USD` | Broadest commercial-bank credit stock denominator. |
| Commercial Real Estate Loans, All Commercial Banks (`CREACBM027NBOG`) | `2026-07-01` | `3.119T USD` | Useful for real-estate credit and infrastructure-adjacent comparisons. |

## First Scale Comparisons

| Company | Metric | Value | Compared With C&I Loans |
|---|---:|---:|---:|
| Apollo | LTM 2Q 2026 originations | `317.0B USD` | `10.94%` |
| Apollo | Q2 2026 originations | `74.0B USD` | `2.55%` |
| Apollo | Q2 2026 gross capital deployment | `111.0B USD` | `3.83%` |
| Ares | Q2 2026 credit group AUM | `440.5B USD` | `15.20%` |
| Ares | Q2 2026 credit group FPAUM | `266.1B USD` | `9.18%` |
| Ares | Q2 2026 available capital | `170.0B USD` | `5.86%` |
| Ares | Q2 2026 credit group deployment | `23.7B USD` | `0.82%` |
| Ares | Q2 2026 U.S. direct-lending deployment | `12.4B USD` | `0.43%` |

## What This Proves

The private-credit platform numbers are big enough to matter against bank-lending categories.

Ares credit AUM at `440.5B USD` equals about `15.20%` of latest commercial and industrial loans at all commercial banks. Apollo LTM originations at `317.0B USD` equal about `10.94%` of that same bank C&I loan stock.

That is a meaningful scale signal.

## What This Does Not Prove

This still does not prove one-for-one displacement.

Reasons:

- AUM is a stock; originations and deployment are flows.
- C&I loans are bank balance-sheet loans; private-credit deployment can include refinancing, acquisition financing, asset-backed finance, and non-C&I borrowers.
- Ares and Apollo figures are company/platform metrics, while the bank series are market-level aggregates.
- Borrower-level matching is still missing.

## Better Claim After Denominator Pass

Old claim:

`Private credit is replacing part of bank lending.`

Better claim:

`Apollo and Ares have private-credit origination, AUM, and deployment scale that is large enough to be material against U.S. commercial-bank lending categories; proving direct replacement requires borrower-level or category-matched evidence.`

## Next Evidence Needed

The next pass should add borrower and credit-quality evidence:

- BDC filings for direct-lending portfolios, borrower counts, non-accruals, and yields.
- Federal Reserve H.8 history to compare growth rates, not only latest levels.
- FDIC loan category data for bank-market composition.
- Rating-agency or private-credit default data.
- Ares credit-segment non-accrual and fund-performance detail.
- Apollo/Athene asset allocation, impairments, and spread-quality trend.

## Simple Version

The company data says Apollo and Ares are big capital routers.

The bank data says the relevant bank-lending pools are also huge.

The first serious conclusion is not "banks are gone." It is:

`Private credit has become large enough to be a real parallel lending system, but we still need borrower-level evidence to measure substitution.`

## Trend Test Added

The FRED history shows bank credit is still growing in aggregate:

- C&I loans were up `8.64%` over one year and `18.31%` over five years.
- Total loans and leases were up `7.44%` over one year and `34.33%` over five years.
- Total bank credit was up `6.30%` over one year and `25.91%` over five years.

This changes the framing:

`Private credit is not replacing the banking system in the aggregate. It is building a parallel lending channel inside specific borrower and transaction lanes.`

## RNQ-002 Status

The denominator refresh did not weaken the prior conclusion.

| Test | Result |
|---|---|
| Latest bank-credit refresh | FRED latest rows unchanged as of `2026-08-24` refresh. |
| Aggregate bank-credit trend | C&I loans, loans and leases, total bank credit, and CRE loans are still up over one-, three-, and five-year windows. |
| Claim effect | Keep the broad claim as parallel-channel growth, not aggregate bank replacement. |
| Next required evidence | FDIC loan-category data, private-credit AUM/origination rows for more managers, and borrower-level bank-to-private-credit substitution evidence. |
