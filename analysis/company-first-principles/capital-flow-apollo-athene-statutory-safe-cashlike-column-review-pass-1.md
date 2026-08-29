# Capital Flow Apollo Athene Statutory Safe Cash-Like Column Review Pass 1

## Purpose

This pass resolves the two short numeric-stream holds from the clean same-CUSIP raw-text inspection.

The question is:

`Are the short rows on pages 6276 and 6312 parser failures, or sparse statutory rows where consideration and interest/dividend fields can still be read safely?`

The review table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-safe-cashlike-column-review-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-safe-cashlike-column-review-diagnostic-pass-1.csv`

The builder is:

`scripts/build-athene-safe-cashlike-column-review.py`

## Main Result

Both short numeric-stream rows are found to be sparse rows with interpretable consideration and interest/dividend fields.

| CUSIP | Page | Schedule | Interpreted consideration | Interpreted interest/dividends | Decision |
|---|---:|---|---:|---:|---|
| `28655*-AA-7` | `6312` | Schedule D Part 5 | `1.806570M USD` | `43,047 USD` | consideration and interest promotable; gain/loss blank hold |
| `02300A-AA-8` | `6276` | Schedule D Part 4 | `268.000000M USD` | `3.986842M USD` | consideration and interest promotable; gain/loss blank hold |

Combined:

| Metric | Value |
|---|---:|
| reviewed rows | `2` |
| pages reviewed | `2` |
| CUSIPs reviewed | `2` |
| consideration-promotable rows | `2` |
| interest-promotable rows | `2` |
| gain/loss blank-hold rows | `2` |
| interpreted consideration total | `269.806570M USD` |
| interpreted interest/dividends total | `4.029889M USD` |

## Interpretation

The page headers explain the short streams.

For Schedule D Part 5 page `6312`, the relevant row order is:

`par/shares -> actual cost -> consideration -> book value at disposal -> gain/loss fields -> interest/dividends`

The Eliant `28655*-AA-7` row carries four repeated `1,806,570` values followed by `43,047`. The safe interpretation is that consideration and interest/dividends are readable, while gain/loss remains blank.

For Schedule D Part 4 page `6276`, the relevant row order is:

`consideration -> par value -> actual cost -> prior-year book -> book value at disposal -> gain/loss fields -> interest/dividends`

The AMAPS `02300A-AA-8` row carries repeated `268,000,000` values followed by `3,986,842`. The safe interpretation is that consideration and interest/dividends are readable, while gain/loss remains blank.

## What This Tells Us In Simple Terms

The two “short numeric stream” rows were not missing-source problems. They were sparse rows where many statutory columns are blank.

So the clean same-CUSIP packet is stronger now:

1. all selected rows were already found in raw PDF text
2. the two short rows now have consideration and interest/dividend interpretation
3. no selected clean row is blocked by missing source text
4. gain/loss still stays conservative and unpromoted where not visible

## What This Proves

This pass proves:

1. the Eliant `28655*-AA-7` Part 5 row on page `6312` supports `1.806570M USD` of consideration and `43,047 USD` of interest/dividends
2. the AMAPS `02300A-AA-8` Part 4 row on page `6276` supports `268.000000M USD` of consideration and `3.986842M USD` of interest/dividends
3. both rows should move from short-stream column hold to consideration/interest-promotable status
4. gain/loss should remain blank/held for both rows

## What It Does Not Prove

This pass does not prove:

1. borrower receipt or use of proceeds
2. lot-level continuity
3. Apollo/Athene source-of-funds allocation
4. liability-cost spread
5. full realized gain/loss
6. IRR, NPV, ROIC, cash-on-cash return, or platform profit

## Safe Claim

`The two short numeric-stream rows in the clean Athene same-CUSIP cash-like packet are sparse statutory rows, not missing-source failures. Page-specific column review supports 269.806570M USD of consideration and 4.029889M USD of interest/dividends across Eliant 28655*-AA-7 and AMAPS 02300A-AA-8, while realized gain/loss remains blank/held. This strengthens row-level proceeds evidence, not borrower receipt, liability spread, or final return proof.`

## Decision

`apollo-athene-short-stream-column-review-consideration-interest-promotable`

The next move is borrower/issuer mapping for the clean non-Treasury same-CUSIP candidates.
