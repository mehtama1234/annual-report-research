# Capital Flow Apollo Athene Statutory Schedule Locator Pass 1

## Purpose

This pass converts the acquired Athene statutory PDF into a targeted extraction map.

It asks:

`Where inside the 9,612-page Athene Annuity and Life Company 2025 statutory statement are the schedules needed to test legal-entity holdings, asset income, credit quality, liabilities, and cash flow?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-locator-pass-1.csv`

The upstream source acquisition pass is:

`/cluster/capital-flow-apollo-athene-statutory-source-acquisition-pass-1.md`

## Short Answer

`The Athene statutory statement is now usable for targeted extraction. The PDF outline and targeted page reads locate the main proof zones: balance-sheet assets on page 3, liabilities on page 4, summary operations on page 5, cash flow on page 6, net investment income on page 18, IMR/AVR pages around 99-100, Schedule BA verification around page 450, Schedule D verification and country summary around pages 451-452, Schedule BA detail starting around page 5813, and Schedule D detail starting around page 5836.`

## Locator Table

| Extraction Target | Page / Range Start | Evidence Found | Proof Use | Boundary |
|---|---:|---|---|---|
| Assets page | `3` | Net admitted assets include bonds, preferred stock, common stock, mortgage loans, and other investment categories. | Legal-entity asset base and Schedule D denominator. | Summary only; not issuer-level holdings. |
| Liabilities, surplus, and other funds | `4` | Aggregate reserve for life contracts and liability for deposit-type contracts are visible. | Liability base for spread and funding-cost bridge. | Not yet full liability-cost or product-level reserve analysis. |
| Summary of operations | `5` | Net investment income line is visible. | Income bridge from invested assets to statutory earnings. | Summary line only; needs asset-class detail. |
| Cash flow | `6` | Premiums collected and net investment income cash-flow lines are visible. | Cash receipt/proxy bridge at legal-entity level. | Does not allocate cash to specific holdings or borrowers. |
| Exhibit of net investment income | `18` | Collected and earned investment income columns are visible for U.S. government bonds, other unaffiliated bonds, and other categories. | Key source for asset-income extraction. | Needs full-page/table extraction and category normalization. |
| Interest maintenance reserve | `99` | IMR calculation page is visible. | Realized gain/loss smoothing and statutory spread support. | Not yet connected to asset disposals. |
| Asset valuation reserve | `100` | AVR default/equity components are visible. | Credit-quality and statutory reserve pressure. | Not issuer-level NAIC migration proof. |
| Schedule BA verification | `450` | Other long-term invested assets verification between years is visible. | Roll-forward for alternatives/other invested assets. | Not issuer/general-partner detail. |
| Schedule D verification | `451` | Bonds and stocks verification between years is visible. | Roll-forward for bonds/stocks acquisition, disposal, and carrying values. | Not issuer-level detail. |
| Schedule D summary by country | `452` | Long-term bonds and stocks owned by country are visible. | Geographic summary for bond/stock portfolio. | Not issuer-level holdings. |
| Schedule BA Part 1 | `5813` | Other long-term invested assets owned at year-end; columns include CUSIP, name, vendor/GP, NAIC designation, actual cost, fair value, book value, investment income, and commitments. | Main Schedule BA holdings and income extraction target. | Needs tabular parsing across detail pages. |
| Schedule BA Part 2 | `5826` | Other long-term invested assets acquired/additions made; columns include CUSIP, name, vendor/GP, acquisition date, type/strategy, actual cost, and additional investment. | Alternative-asset acquisition/use evidence. | Needs detail extraction; not cash return by itself. |
| Schedule D Part 1 Section 1 | `5836` | Long-term issuer-credit obligations; columns include CUSIP, description, NAIC designation, actual cost, par, fair value, book value, effective rate, interest income, due/accrued interest, interest received, acquisition, maturity. | Main issuer-credit bond/loan holdings and income extraction target. | Needs issuer/CUSIP normalization and possibly borrower matching. |
| Schedule D Part 1 Section 2 | `5912` | Asset-backed securities detail; columns include CUSIP, description, NAIC designation, cost, par, fair value, book value, interest income, received interest, maturity, and origination fields. | Main ABF holdings and income extraction target. | Needs ABS type/issuer/originator classification. |
| Schedule D Part 2 Section 1 | `6028` | Preferred stock holdings and dividends received fields are visible. | Equity/preferred income and holding support. | Not central to private-credit proof unless issuer is relevant. |
| Schedule D Part 4 | `6074` | Bonds/stocks sold, redeemed, or disposed during the year with consideration and realized gain/loss fields. | Realized cash/disposal and gain/loss proof. | Needs extraction and matching to holdings. |
| Schedule D Part 5 | `6284` | Bonds/stocks acquired and fully disposed during the current year. | Same-year acquisition/disposal cash and gain/loss evidence. | Needs extraction and matching. |

## What This Lets Us Do Next

This pass turns Apollo/Athene from:

`local statutory PDF acquired`

into:

`targeted extraction-ready statutory source`

The next extraction should not try to parse all `9,612` pages. It should extract and normalize these zones first:

1. pages `3-6` for assets, liabilities, summary operations, and cash flow
2. page `18` for net investment income
3. pages `99-100` for IMR and AVR
4. pages `450-452` for Schedule BA/D verification and summary
5. pages `5813-5835` for Schedule BA detail
6. pages `5836-6336` for Schedule D detail

## Decision

`apollo-athene-statutory-schedule-locator-ready-targeted-extraction-next`

The Athene statutory source is no longer just a downloaded file. It has an executable schedule locator. The proof is still incomplete until the located pages are parsed into holdings, income, credit-quality, liability, realized-gain/loss, and spread rows.

## Safe Claim

`The year-end 2025 Athene Annuity and Life Company statutory statement is locally acquired and schedule-located. The current locator identifies the pages needed for legal-entity assets, liabilities, cash flow, net investment income, IMR, AVR, Schedule BA, and Schedule D extraction. It does not yet prove issuer-level holdings, NAIC designations, investment income by holding, liability-cost spread, realized cash return, borrower destination, or asset-level cash return.`

## Next Work

1. Build a parser that extracts pages `3-6`, `18`, `99-100`, `450-452`, `5813-5835`, and `5836-6336`.
2. Normalize Schedule D and BA rows into issuer/CUSIP, asset class, NAIC designation, cost, fair value, book value, income, interest received, maturity, and impairment fields.
3. Separate Schedule D issuer-credit obligations from Schedule D asset-backed securities.
4. Build a first legal-entity spread bridge from net investment income, liabilities/reserves, and asset base.
