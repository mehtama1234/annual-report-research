# Capital Flow Apollo Athene Statutory Schedule D High-Priority Page Inspection Pass 1

## Purpose

This pass inspects raw row text for the highest-priority Schedule D ABS pages flagged by the page diagnostic.

It asks:

`Why are the worst ABS pages missing book-value parser output, and what kind of parser correction is needed?`

The generated companion table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-high-priority-page-inspection-pass-1.csv`

The inspection script is:

`scripts/inspect-athene-schedule-d-page-corrections.py`

The upstream page diagnostic is:

`/cluster/capital-flow-apollo-athene-statutory-schedule-d-page-diagnostic-pass-1.md`

## Short Answer

`The failure mode is now visible and partially corrected. The high-priority ABS pages often contain legitimate blank statutory columns represented by long dot-marker runs. The prior positional parser compacted numeric tokens and lost the blank columns, so values shifted left into the wrong fields. After the first blank-column parser correction, the inspection sample has 59 rows across the remaining high-priority pages; 47 rows still show repeated blank-column dot markers, 11 are control rows with parser book value, and 1 requires row-level inspection beyond the blank-marker diagnosis.`

## Inspection Summary

| Diagnosis | Rows |
|---|---:|
| raw row contains repeated blank-column dot markers; positional numeric parser likely shifted fields left | `47` |
| parser has book value on a high-priority page; use as control row | `11` |
| missing book value requires row-level column inspection | `1` |

## Page Coverage

The inspection covers the high-priority pages from the prior diagnostic:

`5916`, `5917`, `5927`, `5928`, `5937`, `5939`, `5940`, `5941`, `5962`, `5969`, `5970`, `5971`, `5972`

Most pages have up to `5` inspected rows: four missing-book rows and one control row where available. The sample now has `59` rows because the blank-column parser correction changed which rows and pages remain high priority.

## What This Means

The next parser correction should not simply search for more numbers.

It needs to preserve blank numeric columns.

Current rough logic:

`take the numeric tokens and assign them by position`

Required correction:

`continue parsing row text with blank-column markers preserved, then add row-boundary and subtotal handling so actual cost, par, fair value, book value, valuation change, interest income, due/accrued interest, interest received, acquired date, and maturity date do not collapse when one or more fields are blank`

That is why the reconciliation gate failed even though row extraction and field coverage looked strong.

## Boundary

This pass now documents the first parser fix result, but it does not reconcile Schedule D.

It proves the parser failure mode and creates a targeted correction sample. It still does not prove:

1. final Schedule D totals
2. book-value reconciliation
3. investment-income roll-up
4. borrower or originator destination
5. liability-cost spread
6. asset-level cash return

## Decision

`apollo-athene-statutory-schedule-d-high-priority-page-inspection-blank-column-fix-partial-next-row-boundary`

The parser correction added ABS-specific blank-column-preserving numeric extraction. The next correction should focus on remaining high-priority pages, row-boundary handling, and Section 1 issuer-credit reconciliation.

## Safe Claim

`The Athene Schedule D high-priority page inspection identifies and partially corrects the main parser failure mode: blank statutory numeric columns are represented by dot-marker runs, and compacting numeric tokens shifts fields. The safe use is parser correction design and regression checking; the unsafe use is treating the inspected rows as reconciled accounting values.`

## Next Work

1. Inspect remaining high-priority pages after the blank-column correction.
2. Add row-boundary and subtotal handling.
3. Add Section 1 issuer-credit page diagnostics.
4. Rerun full-range Schedule D parser and reconciliation diagnostics.
5. Promote only if Section 1 and Section 2 reconcile to statutory verification totals.
