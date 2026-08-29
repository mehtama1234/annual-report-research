# Capital Flow Apollo Athene Statutory Schedule D Row-Start CUSIP Marker Correction Pass 1

## Purpose

This pass fixes the highest-impact Athene Schedule D parser failure after the ABS blank-column correction.

It asks:

`Were real Schedule D holding rows being missed because statutory CUSIP-like identifiers contain marker characters such as @, #, or *?`

The generated companion table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-full-range-parser-pass-1.csv`

The extraction script is:

`scripts/extract-athene-statutory-detail-samples.py`

The reconciliation diagnostic is:

`/cluster/capital-flow-apollo-athene-statutory-schedule-d-reconciliation-diagnostic-pass-1.md`

## Short Answer

`Yes. The row-start recognizer was missing many real Schedule D rows with statutory CUSIP marker characters inside the identifier body, such as 05647@-AA-4, P4003#-AA-6, 003009-B@-5, and 04317N-A#-6. Expanding the row-start pattern moves the full Schedule D parser from 7,829 rows to 8,648 rows, moves Section 1 issuer-credit coverage from 64.9049% to 99.7306%, moves Section 2 ABS coverage to 99.9956%, and moves combined Section 1 plus Section 2 coverage to 99.8531%. This is near-reconciled Schedule D evidence, but not yet final named cash-return proof.`

## Correction Evidence

| Metric | Before | After | Status |
|---|---:|---:|---|
| Full Schedule D parser rows | `7,829` | `8,648` | improved |
| Schedule D Part 1 Section 1 rows | `2,705` | `3,418` | improved |
| Schedule D Part 1 Section 2 rows | `5,124` | `5,230` | improved |
| Section 1 book-value coverage | `64.9049%` | `99.7306%` | near-reconciled |
| Section 2 book-value coverage | `86.9519%` | `99.9956%` | near-reconciled |
| Combined Section 1 plus Section 2 coverage | `75.1009%` | `99.8531%` | near-reconciled |

## Example Rows Recovered

| Page | Identifier | Example Holding | Book/Adjusted Carrying Value |
|---:|---|---|---:|
| `5838` | `04317N-A#-6` | Aruba Government senior secured notes | `10.000000M USD` |
| `5840` | `05647@-AA-4` | BX Frontier Member I LLC senior secured notes | `282.675379M USD` |
| `5841` | `P4003#-AA-6` | DSWS SPA Minera Los Pelambres | `283.200000M USD` |
| `5842` | `003009-B@-5` | Aberdeen Asia Pacific Income Fund senior secured notes | `16.000000M USD` |

## What This Proves

This proves that a major Section 1 reconciliation failure was technical, not economic. The statutory filing contained the rows; the parser was failing to recognize marker-bearing identifiers as row starts.

The correction materially upgrades Apollo/Athene from bulk named-holding discovery to near-reconciled Schedule D extraction for the two located bond sections.

## What It Still Does Not Prove

It does not yet prove:

1. final statutory tie-out under an explicit tolerance policy
2. correct income, proceeds, realized gain/loss, or impairment assignment by holding
3. liability-cost spread between Athene reserves/deposit-type contracts and the asset book
4. borrower-level cash receipts
5. asset-level IRR, NPV, repayment, or cash-return proof

## Decision

`apollo-athene-statutory-schedule-d-row-start-cusip-marker-correction-near-reconciled-still-hold`

The Schedule D parser is now near-reconciled for book-value totals, but the proof boundary remains active until residual differences, income/proceeds, liability-cost spread, and borrower cash links are tied out.

## Safe Claim

`The Athene Schedule D parser now recognizes statutory CUSIP marker characters in row starts. This increases the full Schedule D parser to 8,648 rows and moves combined Section 1 plus Section 2 book-value coverage to 99.8531% of the statutory reference. The safe use is near-reconciled legal-entity holding extraction; the unsafe use is claiming liability-cost spread, borrower cash receipts, or asset-level returns.`

## Next Work

1. Explain the remaining `233.299496M USD` combined book-value gap.
2. Inspect whether residual differences are excluded sections, subtotals, PDF extraction loss, or remaining field shifts.
3. Join holdings to investment income, disposals, realized gains/losses, and impairments.
4. Build the Apollo/Athene liability-cost spread bridge after final Schedule D tie-out.
