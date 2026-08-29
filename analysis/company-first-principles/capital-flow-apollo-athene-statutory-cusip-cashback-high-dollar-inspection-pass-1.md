# Capital Flow Apollo Athene Statutory CUSIP Cash-Back High-Dollar Inspection Pass 1

## Purpose

This pass ranks the highest-dollar Athene Schedule D CUSIP cash-back candidates and classifies their disposition labels before any claim promotion.

The structured outputs are:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-cusip-cashback-high-dollar-inspection-pass-1.csv`

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-cusip-cashback-high-dollar-inspection-diagnostic-pass-1.csv`

The builder is:

`scripts/build-athene-cusip-cashback-inspection.py`

## Source Input

The source input is the CUSIP cash-back workbench:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-cusip-cashback-match-pass-1.csv`

That table has `10,801` unique CUSIP rows and separates the placeholder bucket from the headline CUSIP-like view.

## What This Pass Tests

This pass asks a narrower and harder question:

`Of the largest Athene named proceeds rows, which are plausible cash-back candidates, and which are holds because the disposition may be exchange, transfer, withdrawal, or disposal-only with no year-end holding match?`

It does not treat `consideration` as one uniform economic event.

It classifies each top-dollar row into:

1. `principal-paydown-cash-candidate`
2. `maturity-proceeds-cash-candidate`
3. `redemption-or-call-cash-candidate`
4. `market-sale-or-counterparty-cash-candidate`
5. `tax-free-exchange-hold`
6. `security-withdrawal-hold`
7. `direct-or-private-transfer-hold`

## Main Diagnostic Result

The ranked inspection table covers the top `100` ex-placeholder CUSIP rows by disposal consideration.

| Metric | Value |
|---|---:|
| top-100 disposal consideration | `23.817173163B USD` |
| same-CUSIP top-100 consideration | `11.989467377B USD` |
| tier-1 same-CUSIP cash-candidate rows | `34` |
| tier-1 same-CUSIP cash-candidate consideration | `7.690348231B USD` |
| tier-2 same-CUSIP noncash/transfer hold rows | `7` |
| tier-3 disposal-only or no-year-end-holding rows | `59` |

## Economic Class Split

| Economic Disposition Class | Top-100 Count |
|---|---:|
| market-sale-or-counterparty-cash-candidate | `49` |
| principal-paydown-cash-candidate | `25` |
| tax-free-exchange-hold | `20` |
| redemption-or-call-cash-candidate | `3` |
| security-withdrawal-hold | `2` |
| direct-or-private-transfer-hold | `1` |

## Highest-Dollar Rows

| Rank | CUSIP | Candidate Tier | Class | Description Sample | Consideration | Boundary |
|---:|---|---|---|---|---:|---|
| `1` | `L0187*-AA-0` | tier-2 hold | tax-free exchange | AP ALKAIOS senior exposure | `2.594729570B USD` | same CUSIP exists, but tax-free exchange treatment must be proven cash or noncash. |
| `2` | `G7741@-AC-4` | tier-1 cash candidate | principal paydown | SVF II Finco Cayman LP | `2.089548152B USD` | same CUSIP plus paydown label; needs principal, book, gain/loss, and interest reconciliation. |
| `3` | `L1304@-AB-2` | tier-3 hold | tax-free exchange | Bridgepoint NAV Euro finance | `1.313529575B USD` | disposal-only and tax-free exchange label; not a clean year-end-holding cash row. |
| `4` | `00264#-AB-3` | tier-1 cash candidate | principal paydown | AP Aristotle Holdings LLC | `782.620834M USD` | same-CUSIP paydown candidate; borrower cash and return proof remain open. |
| `5` | `20633K-AA-6` | tier-3 hold | market sale/counterparty | Concord Music Royalties LLC | `624.910660M USD` | named proceeds visible, but no year-end holding match in the current parser. |
| `10` | `09261H-B@-5` | tier-2 hold | tax-free exchange | Blackstone Private Credit Fund senior notes | `401.583100M USD` | same-CUSIP bridge exists, but fund-note exchange is not borrower cash proof. |
| `18` | `02300A-AA-8` | tier-1 cash candidate | market sale/counterparty | AMAPS 1 LLC Tranche A Note | `268.000000M USD` | same-CUSIP sale/counterparty candidate; raw row and return fields need inspection. |

## What This Tells Us

The CUSIP cash-back workbench is real, but the top-dollar rows are not all equally claimable.

The key finding is:

`Athene has billions of named Schedule D proceeds candidates, but the cleanest next proof pool is smaller than the raw consideration pool. In the top 100 ex-placeholder rows, 34 rows are same-CUSIP cash candidates representing 7.690348231B USD of consideration.`

That is the right worklist for the next row-level proof pass.

## Why This Matters

This is the difference between a broad overclaim and a proof-controlled claim.

A weak claim would say:

`Athene had 72B USD of named asset cash returns.`

That is too broad.

A safer claim is:

`Athene's statutory filing exposes a large named proceeds universe, and the current top-dollar CUSIP workbench identifies 34 same-CUSIP high-dollar rows that are plausible cash-back candidates pending row-level reconciliation.`

## Next Row-Level Proof Move

The next pass should inspect the tier-1 rows first:

1. `G7741@-AC-4` SVF II Finco Cayman LP paydown
2. `00264#-AB-3` AP Aristotle Holdings LLC paydown
3. `28655*-AA-7` Eliant Invest Holding LP market/counterparty row
4. `Q7457#-AA-9` Turbin Finance Trust paydown
5. `02300A-AA-8` AMAPS 1 LLC market/counterparty row

Each row needs:

1. raw holding row inspection
2. raw disposal row inspection
3. consideration to book-at-disposal check
4. realized gain/loss sanity check
5. interest/dividend received sanity check
6. disposition label classification
7. proof verdict: cash candidate, noncash hold, parser hold, or borrower-return hold

## Safe Claim

`The Athene high-dollar CUSIP cash-back inspection ranks the top 100 ex-placeholder proceeds rows. Those rows carry 23.817173163B USD of disposal consideration. Within them, 34 rows are tier-1 same-CUSIP cash candidates representing 7.690348231B USD of consideration, while 7 same-CUSIP rows are noncash/transfer holds and 59 are disposal-only or no-year-end-holding rows. This supports prioritized row-level proof work, not final asset-level cash-return, borrower-cash, or liability-spread proof.`

## Decision

`apollo-athene-high-dollar-cusip-cashback-inspection-ready-tier1-row-proof-next`

The Apollo/Athene prototype has moved from broad CUSIP matching to a ranked high-dollar proof queue. The next work is row-level inspection of tier-1 same-CUSIP cash candidates.

