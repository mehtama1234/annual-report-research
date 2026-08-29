# Capital Flow Apollo Athene Statutory CUSIP Cash-Back Match Pass 1

## Purpose

This pass executes the next Apollo/Athene prototype step from the meaty end-to-end proof workplan:

`match Schedule D year-end holdings to Schedule D disposal/proceeds rows by CUSIP, then identify named cash-back candidates and unresolved proof boundaries.`

The structured outputs are:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-cusip-cashback-match-pass-1.csv`

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-cusip-cashback-match-diagnostic-pass-1.csv`

The builder is:

`scripts/build-athene-cusip-cashback-match.py`

## Source Inputs

| Input | Rows | Role |
|---|---:|---|
| Schedule D full-range holdings parser | `8,648` | Year-end Schedule D Section 1 and Section 2 holding rows with CUSIP, issuer, book value, fair value, NAIC marker, income fields, acquisition date, and maturity date. |
| Schedule D disposal/proceeds parser | `7,655` | Schedule D Part 4 and Part 5 disposal/proceeds rows with CUSIP, issuer, disposal date, purchaser or disposition type, consideration, book-at-disposal, realized gain/loss, and interest/dividend fields. |
| Statutory compact extraction | `30` | Provides the `72.140293824B USD` statutory reference for consideration for bonds and stocks disposed. |

## What The Match Does

The pass groups both parser outputs by CUSIP.

Each output row asks:

1. does the CUSIP appear in year-end holdings?
2. does the CUSIP appear in disposal/proceeds rows?
3. is it a standard CUSIP-like identifier, a statutory private/marker identifier, or a placeholder identifier?
4. what year-end book value, fair value, and income fields are visible?
5. what disposal consideration, book-at-disposal, realized gain/loss, and interest/dividend fields are visible?
6. what proof use and boundary should attach to the row?

## Main Result

The full audit table has `10,801` unique CUSIP rows.

| Match Status | Count |
|---|---:|
| same CUSIP in year-end holdings and disposal/proceeds output | `3,486` |
| disposal/proceeds CUSIP with no year-end holding match | `2,755` |
| year-end holding CUSIP with no disposal/proceeds match | `4,560` |

The full parser consideration total remains:

`72.807523483B USD`

against statutory reference:

`72.140293824B USD`

coverage:

`100.9249%`

## Headline Ex-Placeholder View

One CUSIP bucket, `000000-00-0`, is a placeholder-style identifier and should not drive headline claims. The workbench keeps it for audit but separates it from the headline view.

Excluding that placeholder bucket:

| Metric | Value |
|---|---:|
| headline CUSIP-like rows | `10,800` |
| headline same-CUSIP holding/proceeds bridges | `3,485` |
| headline disposal consideration | `68.251655221B USD` |
| headline coverage versus statutory disposal consideration reference | `94.6096%` |
| headline same-CUSIP matched consideration | `27.512853248B USD` |
| headline same-CUSIP matched consideration share | `40.3109%` |

This is the first real CUSIP-level bridge from Athene legal-entity holdings to named cash-back candidates.

## High-Dollar Named Cash-Back Candidates

The largest ex-placeholder same-CUSIP or disposal rows include:

| CUSIP | Match Status | Description Sample | Disposal Consideration | Boundary |
|---|---|---|---:|---|
| `L0187*-AA-0` | same-CUSIP holding/proceeds visible | AP ALKAIOS senior exposure | `2.594729570B USD` | statutory private/marker CUSIP; lot-level continuity and tax-free exchange treatment need inspection. |
| `G7741@-AC-4` | same-CUSIP holding/proceeds visible | SVF II Finco Cayman LP | `2.089548152B USD` | paydown rows need numeric-column and book/gain/loss reconciliation. |
| `L1304@-AB-2` | disposal-only visible | Bridgepoint NAV Euro finance | `1.313529575B USD` | disposed asset may not remain in year-end holdings; disposition type needs classification. |
| `00264#-AB-3` | same-CUSIP holding/proceeds visible | AP Aristotle Holdings LLC | `782.620834M USD` | same-CUSIP bridge exists but borrower cash and realized-return proof remain open. |
| `20633K-AA-6` | disposal-only visible | Concord Music Royalties LLC | `624.910660M USD` | disposal proceeds visible; no year-end holding match in current parser. |
| `69346Y-AP-8` | disposal-only visible | PK Airfinance | `497.703042M USD` | paydown/disposal treatment must be classified before return use. |
| `09261H-B@-5` | same-CUSIP holding/proceeds visible | Blackstone Private Credit Fund senior notes | `401.583100M USD` | same-CUSIP bridge exists, but fund-level note cash is not borrower-level cash. |

## What This Tells Us

In simple terms:

`Apollo/Athene is no longer just a giant insurance balance sheet in the research. We can now see thousands of named securities where the statutory filing shows holdings, income fields, disposals, consideration, and gain/loss-style numeric streams.`

That is a major move toward named cash proof.

But it is still not the finish line.

The match proves a workbench:

`CUSIP -> holding row -> disposal/proceeds row -> cash-back candidate`

It does not yet prove:

1. lot-level source/use continuity
2. final consideration and gain/loss reconciliation
3. income by CUSIP tied to page 18 categories
4. liability cost or spread by source pool
5. borrower receipt or borrower use of proceeds
6. asset-level IRR, NPV, ROIC, or realized return

## Proof Upgrade Path

The next pass should rank and inspect the highest-dollar same-CUSIP bridge rows.

The upgrade test is:

`same CUSIP + reconciled consideration + reconciled book/gain/loss + income field + credit-quality marker + liability-cost context + safe boundary`

The disproof test is:

`placeholder identifier, subtotal duplication, Part 4/Part 5 double count, mis-positioned numeric column, tax-free exchange not cash, paydown not final sale, or fund/security cash that cannot be traced to borrower cash`

## Safe Claim

`Athene Schedule D now has a CUSIP-level cash-back workbench. The pass joins 8,648 year-end holding rows and 7,655 disposal/proceeds rows into 10,801 unique CUSIP rows. Excluding the placeholder identifier bucket, 3,485 CUSIP-like rows appear in both holdings and disposal/proceeds output, representing 27.512853248B USD of same-CUSIP matched consideration and 68.251655221B USD of headline disposal consideration. This supports named cash-back candidate language, not final asset-level realized-return, borrower-cash, or liability-spread proof.`

## Decision

`apollo-athene-cusip-cashback-workbench-ready-reconciliation-hold`

Apollo/Athene has advanced from legal-entity income/proceeds and named disposal rows to a CUSIP-level cash-back matching workbench. The next work is row-level reconciliation and highest-dollar bridge inspection, not broad platform mapping.

