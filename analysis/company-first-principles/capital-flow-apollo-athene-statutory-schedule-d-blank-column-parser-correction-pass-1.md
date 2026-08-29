# Capital Flow Apollo Athene Statutory Schedule D Blank-Column Parser Correction Pass 1

## Purpose

This pass applies the first Schedule D ABS parser correction identified by the high-priority page inspection.

It asks:

`Does preserving blank statutory numeric columns improve the Athene Schedule D ABS parser and reconciliation diagnostics?`

The corrected parser is:

`scripts/extract-athene-statutory-detail-samples.py`

The reconciliation diagnostic is:

`/cluster/capital-flow-apollo-athene-statutory-schedule-d-reconciliation-diagnostic-pass-1.md`

The high-priority page inspection is:

`/cluster/capital-flow-apollo-athene-statutory-schedule-d-high-priority-page-inspection-pass-1.md`

## Short Answer

`Partially, at this intermediate correction step. The parser preserved blank ABS numeric columns instead of compacting numeric tokens. At this step, the full-range row count remained 7,829, but ABS book-value coverage improved from 86.5142% to 86.9519% of the statutory ABS reference, and combined Section 1 plus Section 2 coverage improved from 74.8984% to 75.1009% of the total bonds reference. A later row-start CUSIP marker correction supersedes these as the current Schedule D totals.`

## Correction Result

| Metric | Before | After | Status |
|---|---:|---:|---|
| Full-range Schedule D rows | `7,829` | `7,829` | row population unchanged |
| ABS book-value reference coverage | `86.5142%` | `86.9519%` | improved, not reconciled |
| Combined Section 1 plus Section 2 coverage | `74.8984%` | `75.1009%` | improved, not reconciled |
| Rows with book/adjusted carrying value | `7,462` | `7,470` | improved |
| High-priority pages | `13` | `12` | improved |
| Medium-priority pages | `24` | `27` | shifted from high to medium |
| Coverage-visible pages | `154` | `152` | changed after column correction |

## What Changed

The parser now looks for ABS numeric fields inside the dot-delimited statutory columns after the NAIC designation field.

That means a row like:

`blank actual cost -> par value -> blank fair value -> blank book value`

is no longer collapsed into:

`actual cost -> fair value -> interest`

This fixes part of the field-shift problem on ABS rows with blank columns.

## Boundary

This is not the final correction.

At this intermediate pass the remaining reconciliation gap was still large:

1. issuer-credit Section 1 remained at `64.9049%` of its reference
2. ABS Section 2 was only `86.9519%` of its reference
3. combined Section 1 plus Section 2 was only `75.1009%` of total bonds reference
4. some high-priority ABS pages still showed missing book-value fields
5. row-boundary and subtotal handling still needed correction

## Decision

`apollo-athene-statutory-schedule-d-blank-column-parser-correction-partial-improvement-reconciliation-still-hold`

The blank-column parser fix is accepted as a partial intermediate improvement. The later row-start CUSIP marker correction resolves the much larger issuer-credit Section 1 gap and supersedes this page as the current reconciliation state.

## Safe Claim

`The Athene Schedule D parser added a blank-column-aware ABS numeric parser as an intermediate correction. It improved ABS book-value reconciliation modestly, from 86.5142% to 86.9519% of the statutory ABS reference at that step, but these are no longer the current Schedule D totals after the later row-start CUSIP marker correction.`

## Next Work

1. Use the row-start CUSIP marker correction page as the current Schedule D reconciliation state.
2. Inspect remaining high-priority ABS pages after both corrections.
3. Explain the residual combined book-value gap.
4. Join Schedule D holdings to income, disposal, impairment, and liability-cost schedules.
5. Promote only if Schedule D sections reconcile to statutory verification totals within a defined tolerance.
