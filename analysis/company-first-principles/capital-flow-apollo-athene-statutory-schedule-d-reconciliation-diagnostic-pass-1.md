# Capital Flow Apollo Athene Statutory Schedule D Reconciliation Diagnostic Pass 1

## Purpose

This pass tests the full-range Athene Schedule D parser against the compact statutory verification totals.

It asks:

`Is the 8,648-row Schedule D parser output reconciled enough to support legal-entity portfolio totals, spread work, or asset-return claims?`

The generated companion table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-reconciliation-diagnostic-pass-1.csv`

The diagnostic script is:

`scripts/reconcile-athene-schedule-d-parser.py`

The upstream full-range parser pass is:

`/cluster/capital-flow-apollo-athene-statutory-schedule-d-full-range-parser-pass-1.md`

The page-level diagnostic is:

`/cluster/capital-flow-apollo-athene-statutory-schedule-d-page-diagnostic-pass-1.md`

## Short Answer

`Almost, but still hold. The parser is now full-range, has the ABS blank-column correction, and has a statutory CUSIP-marker row-start correction. The issuer-credit parser book-value sum covers about 99.7306% of the statutory issuer-credit reference, the ABS parser book-value sum covers about 99.9956% of the statutory ABS reference, and the combined Section 1 plus Section 2 parser book-value sum covers about 99.8531% of the total bonds reference. This is near-reconciled Schedule D evidence, but Apollo/Athene remains below final accounting proof and below named cash-return proof until residual differences, subtotals, income, proceeds, and liability-cost spread are tied out.`

## Reconciliation Tests

| Test | Parser Value | Statutory Reference | Coverage | Status |
|---|---:|---:|---:|---|
| Schedule D Part 1 Section 1 book value | `85.158422267B USD` | `85.388493720B USD` | `99.7306%` | near-reconciled, still hold |
| Schedule D Part 1 Section 2 book value | `73.460673438B USD` | `73.463901477B USD` | `99.9956%` | near-reconciled, still hold |
| Section 1 plus Section 2 book value | `158.619095705B USD` | `158.852395201B USD` | `99.8531%` | near-reconciled, still hold |

## Coverage Diagnostics

| Field | Rows With Field | Total Rows | Coverage |
|---|---:|---:|---:|
| NAIC designation | `8,495` | `8,648` | `98.2308%` |
| actual cost | `8,498` | `8,648` | `98.2655%` |
| fair value | `8,482` | `8,648` | `98.0805%` |
| book/adjusted carrying value | `8,289` | `8,648` | `95.8488%` |
| maturity date | `8,648` | `8,648` | `100.0000%` |

## What This Means

The parser is good enough for:

1. locating named holdings
2. generating CUSIP-level worklists
3. sampling issuers, NAIC designations, maturities, and asset-type labels
4. prioritizing borrower/originator classification
5. identifying where reconciliation work must focus

The parser is close enough to support near-final reconciliation work, but it is not yet good enough for:

1. final portfolio totals
2. Schedule D proof-grade book value
3. liability-cost spread
4. investment-income roll-up
5. borrower-level cash receipt
6. asset-level return proof

## Diagnosis

The main historical issue was missed row starts. The corrected recognizer now captures statutory CUSIP markers such as `@`, `#`, and `*`, which moved Section 1 from a large reconciliation failure to near-tie. The remaining issue is proof-grade reliability: residual differences, dense PDF numeric shifts, subtotal treatment, and income/proceeds matching still need review.

The next pass should focus on:

1. page-level row counts
2. subtotal and continuation handling
3. residual Section 1 row/subtotal inspection
4. better ABS Section 2 numeric column positioning
5. reconciliation against the `85.388493720B USD` issuer-credit reference and `73.463901477B USD` ABS reference

## Decision

`apollo-athene-statutory-schedule-d-reconciliation-diagnostic-hold-column-correction-next`

The Schedule D parser has passed the bulk-extraction gate and failed the reconciliation gate. It must not be promoted to final legal-entity Schedule D proof until the numeric columns reconcile to statutory verification totals.

## Safe Claim

`The Athene Schedule D parser now has full-range row extraction and quantified reconciliation diagnostics. It produces 8,648 named Schedule D rows and now covers 99.7306% of the issuer-credit reference, 99.9956% of the ABS reference, and 99.8531% of the combined Section 1 plus Section 2 reference. The safe use is near-reconciled holding discovery and final reconciliation targeting; the unsafe use is final portfolio totals, spread proof, or asset-level cash-return proof.`

## Next Work

1. Define a proof tolerance for Schedule D book-value reconciliation.
2. Inspect residual Section 1 and Section 2 differences by page/subtotal.
3. Confirm whether the remaining `233.299496M USD` combined gap is due to excluded sections, subtotal treatment, PDF extraction loss, or field shifts.
4. Join near-reconciled rows to investment income, disposals, realized gains/losses, and impairment schedules.
5. Build the Apollo/Athene liability-cost spread bridge only after final reconciliation review.
