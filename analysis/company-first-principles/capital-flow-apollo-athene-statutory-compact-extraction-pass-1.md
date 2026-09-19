# Capital Flow Apollo Athene Statutory Compact Extraction Pass 1

## Purpose

This pass extracts the compact, high-signal pages from the acquired Athene statutory statement before attempting the long Schedule D/BA holdings tables.

It asks:

`Can the Athene Annuity and Life Company 2025 statutory statement already prove legal-entity assets, liabilities, investment income, cash flow, Schedule D/BA roll-forward, and reserve pressure at summary level?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-compact-extraction-pass-1.csv`

The upstream schedule locator is:

`/cluster/capital-flow-apollo-athene-statutory-schedule-locator-pass-1.md`

## Short Answer

`Partial statutory upgrade. The compact pages now prove that Athene Annuity and Life Company had a large legal-entity asset base, liability base, net investment income, operating cash flow, Schedule D bond/stock roll-forward, Schedule BA other-invested-asset roll-forward, and statutory reserve pressure in 2025. This is stronger than Apollo/Athene channel evidence, but still not full named cash proof because issuer-level Schedule D/BA holdings, borrower destinations, NAIC designation detail, liability-cost spread, and asset-level return are not yet extracted.`

## Extracted Summary Evidence

| Gate | Page | Extracted Evidence | Value | What It Proves | Boundary |
|---|---:|---|---:|---|---|
| Bonds | `3` | Bonds, Schedule D net admitted assets | `158.852395199B USD` | Legal entity owns a large Schedule D bond base. | Not issuer-level holdings or borrower cash. |
| Mortgage loans | `3` | First-lien mortgage loans | `84.664838463B USD` | Legal entity owns a very large mortgage-loan book. | Not borrower-level loan schedule or repayment proof. |
| Other invested assets | `3` | Schedule BA net admitted assets | `17.387119006B USD` | Legal entity owns material other long-term invested assets. | Not Schedule BA issuer/GP-level detail. |
| Cash and short-term investments | `3` | Cash, cash equivalents, and short-term investments | `9.357351729B USD` | Legal entity had material cash/liquid investment balance. | Not source/use allocation. |
| Life reserves | `4` | Aggregate reserve for life contracts | `110.615749220B USD` | Liability base is visible at legal-entity level. | Not product-level liability cost. |
| Deposit-type contracts | `4` | Liability for deposit-type contracts | `64.259784362B USD` | Funding/liability channel is visible at legal-entity level. | Not spread cost or surrender behavior. |
| Net investment income | `5` | Summary of operations net investment income | `12.732699320B USD` | Legal entity investment income is visible. | Not holding-level income. |
| Cash net investment income | `6` | Cash-flow net investment income | `12.281980822B USD` | Investment income has cash-flow statement support. | Still not allocated to asset class/holding. |
| Net cash from operations | `6` | Net cash from operations | `20.789852294B USD` | Legal entity generated positive statutory operating cash flow. | Not asset-level cash return. |
| Bond proceeds | `6` | Proceeds from bonds sold, matured, or repaid | `54.035221430B USD` | Cash from investment turnover is visible. | Not tied to specific asset disposals yet. |
| Mortgage-loan proceeds | `6` | Proceeds from mortgage loans sold, matured, or repaid | `12.676073505B USD` | Mortgage-loan repayment/disposition cash is visible. | Not loan-level payback proof. |
| Other unaffiliated bond income | `18` | Collected / earned income on other unaffiliated bonds | `5.948433327B / 5.926174946B USD` | Large bond-income bucket is visible. | Not issuer-level income. |
| Affiliated bond income | `18` | Collected / earned income on bonds of affiliates | `1.910570987B / 1.983603713B USD` | Affiliated bond income is visible. | Needs affiliate/issuer detail. |
| Mortgage-loan income | `18` | Collected / earned mortgage-loan income | `4.557162846B / 4.736361962B USD` | Mortgage-loan income is visible. | Not borrower-level cash receipt. |
| Total gross investment income | `18` | Total gross investment income | `13.601183683B collected / 14.010808604B earned` | Income denominator is extracted. | Deductions and asset-level attribution still needed. |
| Net investment income exhibit | `18` | Net investment income after deductions | `12.732699320B USD` | Ties exhibit to summary operations. | Not spread after liability cost. |
| IMR reserve | `99` | Interest maintenance reserve current year-end | `219.835675M USD` | Realized gain/loss smoothing reserve is visible. | Not tied to individual disposals. |
| AVR accumulated balance | `100` | Asset valuation reserve accumulated balance | `6.291800508B USD` | Statutory asset-risk reserve pressure is visible. | Not issuer-level NAIC designation proof. |
| Schedule BA statement value | `450` | Schedule BA statement value at current period end | `17.387119006B USD` | BA roll-forward ties to assets page. | Not detail extraction. |
| Schedule D statement value | `451` | Schedule D statement value at current period end | `161.896884148B USD` | Schedule D roll-forward ties bond/stock base. | Not issuer-level detail. |
| Schedule D issuer-credit obligations | `451` | Issuer-credit obligations book/adjusted carrying value | `85.388493720B USD` | Issuer-credit bucket is quantified. | Not issuer-level holdings. |
| Schedule D asset-backed securities | `451` | Asset-backed securities book/adjusted carrying value | `73.463901477B USD` | ABF/ABS bucket is quantified at statutory level. | Not originator/borrower-level detail. |
| Schedule D disposals consideration | `451` | Consideration for bonds/stocks disposed | `72.140293824B USD` | Statutory disposal cash/proceeds are visible. | Not matched to individual realized return rows. |
| Schedule D other-than-temporary impairment | `451` | Current-year OTTI recognized | `110.227270M USD` | Credit/impairment pressure is visible. | Not issuer-level impairment detail. |
| Schedule D total bonds summary | `452` | Total bonds book/adjusted carrying value | `158.852395201B USD` | Country summary confirms total bond base. | Rounding differs by `2 USD` from assets page. |

## What This Tells Us

The legal-entity statutory statement gives a much better answer than platform AUM:

`insurance liabilities -> Athene legal entity -> statutory assets -> investment income and cash flow`

The current extraction proves summary-level legal-entity mechanics:

1. Athene Annuity and Life Company has a huge Schedule D bond base.
2. It has a very large mortgage-loan book.
3. It has a material Schedule BA alternatives/other-invested-assets bucket.
4. It generated statutory net investment income and operating cash flow in `2025`.
5. The Schedule D/BA roll-forwards expose acquisitions, disposals, impairments, income, and book/fair values.
6. AVR and IMR show statutory risk and gain/loss reserve mechanics.

## What It Still Does Not Prove

This is still not full named cash proof.

The extraction does not yet show:

1. which exact issuers or borrowers sit in Schedule D
2. which exact funds, partnerships, or other assets sit in Schedule BA
3. NAIC designation distribution by holding
4. investment income by issuer/CUSIP
5. realized gain/loss or impairment by asset
6. liability cost by product or reserve block
7. legal-entity spread by asset class
8. borrower/project cash use
9. cash back to Apollo/Athene by named asset
10. asset-level IRR, NPV, ROIC, or payback

## Decision

`apollo-athene-statutory-compact-extraction-summary-proof-visible-detail-extraction-pending`

Apollo/Athene improves from local-source-acquired to summary statutory extraction. It remains below named cash proof until Schedule D/BA details and liability-cost spread are extracted.

## Safe Claim

`Athene Annuity and Life Company has summary-level statutory proof of legal-entity assets, liabilities, investment income, cash flow, Schedule D/BA roll-forward, and reserve pressure for 2025. This supports an insurance-liability-to-asset-income bridge for Apollo/Athene. It does not yet prove issuer-level holdings, NAIC designations by holding, borrower destination, holding-level investment income, liability-cost spread, or asset-level cash return.`

## Next Work

1. Extract Schedule D Part 1 Section 1 issuer-credit obligations from pages `5836-5911`.
2. Extract Schedule D Part 1 Section 2 asset-backed securities from pages `5912-6027`.
3. Extract Schedule BA Part 1, Part 2, and Part 3 from pages `5813-5833`.
4. Build a first legal-entity spread bridge using statutory income, reserves/liabilities, and invested-asset base.
