# Apollo–Athene Schedule D Blank-Column Parser Boundary

Research date: `2026-09-15`

## Purpose

Determine whether the residual Athene Schedule D book-value gap can be closed
by filling missing numeric fields, or whether the source contains legitimate
blank statutory columns that must remain blank.

## Evidence

The full-range parser currently has `390` rows without a parsed
book/adjusted-carrying-value field: `383` in Schedule D Part 1 Section 2 and
`7` in Section 1. Raw-text inspection of the highest-priority ABS pages shows
repeated dot-marker runs in the statutory columns. Examples include IO and
structured-credit rows where fair value is visible while actual cost, par,
book value, or valuation change is intentionally blank in the extracted table.

## Conclusion

The missing-field count is not evidence that every blank should be imputed.
The parser must preserve blank columns and reconstruct row geometry before
assigning numeric fields. A numeric-token-only repair could shift fair value,
book value, unrealized change, or income into the wrong column and worsen the
reconciliation.

## Boundary

This confirms a parser failure mode and a safe correction rule; it does not
reconcile Schedule D totals or prove asset-level cash return.

## Next test

Use column geometry and row-boundary markers to distinguish a source-blank
field from a missed token, then rerun section-level sums against the compact
statutory verification references. Promote only rows whose source column is
unambiguous.

## Safe claim

`Athene Schedule D residual missing-book rows are concentrated in ABS pages
with legitimate blank-column dot markers. The next correction must preserve
blank statutory columns; positional imputation is not evidence-based.`
