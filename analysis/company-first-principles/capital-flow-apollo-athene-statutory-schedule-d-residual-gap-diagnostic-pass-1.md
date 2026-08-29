# Capital Flow Apollo Athene Statutory Schedule D Residual Gap Diagnostic Pass 1

## Purpose

This pass explains what remains after the Athene Schedule D parser reached near-reconciled book-value coverage.

It asks:

`Is the remaining Schedule D book-value gap a simple missed-row problem, or does it require row-level continuation, subtotal, and duplicate-risk inspection before promotion?`

The generated companion table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-residual-gap-diagnostic-pass-1.csv`

The diagnostic script is:

`scripts/diagnose-athene-schedule-d-residual-gap.py`

The upstream correction is:

`/cluster/capital-flow-apollo-athene-statutory-schedule-d-row-start-cusip-marker-correction-pass-1.md`

## Short Answer

`The residual Schedule D gap is small enough for near-reconciled use but not clean enough for final proof. Combined Section 1 plus Section 2 parser book value is short by 233.299496M USD, or about 0.1469% of the 158.852395201B USD statutory reference. Section 1 drives almost all of the residual gap at 230.071453M USD. Raw row-like unmatched candidates exist, but their apparent book-value sum is much larger than the residual gap, so automatically adding them would likely double-count continuation or tranche text. The next gate is row-level residual inspection, not another broad parser expansion.`

## Residual Gap

| Scope | Parser Rows | Parser Book Value | Statutory Reference | Residual Gap | Coverage |
|---|---:|---:|---:|---:|---:|
| Schedule D Part 1 Section 1 | `3,418` | `85.158422267B USD` | `85.388493720B USD` | `-230.071453M USD` | `99.7306%` |
| Schedule D Part 1 Section 2 | `5,230` | `73.460673438B USD` | `73.463901477B USD` | `-3.228039M USD` | `99.9956%` |
| Section 1 plus Section 2 | `8,648` | `158.619095705B USD` | `158.852395201B USD` | `-233.299496M USD` | `99.8531%` |

## Candidate Risk

| Scope | Missing Book Rows | Raw Row-Like Candidates | Apparent Candidate Book Sum | Largest Candidate | Interpretation |
|---|---:|---:|---:|---|---|
| Section 1 | `1` | `44` | `1.130284720B USD` | page `5904`, label `A-1`, `682.295215M USD` | Candidate sum is larger than the residual gap; blind fallback row starts would likely double-count continuation/tranche text. |
| Section 2 | `358` | `17` | `1.608943846B USD` | page `6023`, label `ADVANCE`, `1.412877374B USD` | Section 2 is already almost tied; large candidates are likely continuation/duplicate risks. |
| Combined | `359` | `61` | `2.739228566B USD` | page `6023`, label `ADVANCE`, `1.412877374B USD` | Candidate pool is diagnostic evidence, not addable row evidence. |

## What This Means

The row-start CUSIP marker correction solved the main problem. The remaining problem is smaller and more technical:

1. Section 1 is short by only `0.2694%`.
2. Section 2 is short by only `0.0044%`.
3. Combined Section 1 plus Section 2 is short by only `0.1469%`.
4. The remaining candidate rows are not safe to auto-add because their apparent book values exceed the residual gap.
5. Final promotion needs row-level duplicate checks, continuation checks, and a defined reconciliation tolerance.

## What It Still Does Not Prove

It does not yet prove:

1. final Schedule D statutory tie-out
2. holding-level investment income
3. disposal proceeds by holding
4. realized gains/losses by holding
5. impairments by holding
6. liability-cost spread
7. borrower cash receipt
8. asset-level return

## Decision

`apollo-athene-statutory-schedule-d-residual-gap-near-reconciled-row-level-inspection-next`

The Schedule D parser is close enough to support residual tie-out and downstream join design, but not close enough to claim final cash proof.

## Safe Claim

`The Athene Schedule D parser now reaches 99.8531% combined Section 1 plus Section 2 book-value coverage against the statutory reference. The remaining 233.299496M USD gap is too small for broad parser redesign but too unresolved for final accounting proof. The next work is row-level residual inspection and income/proceeds/liability joins.`

## Next Work

1. Inspect the largest unmatched raw candidates for duplicate or continuation status.
2. Define the final Schedule D reconciliation tolerance.
3. If residual differences are explainable, promote Schedule D to near-final legal-entity holdings base.
4. Join Schedule D holdings to statutory net investment income, disposal/proceeds, realized gain/loss, impairment, and liability-cost schedules.
