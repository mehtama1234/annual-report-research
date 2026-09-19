# Apollo–Athene Schedule D Native Coordinate Diagnostic

Research date: `2026-09-15`

## Purpose

Create a reproducible native-PDF coordinate layer for the worst ABS pages
before assigning numeric tokens to statutory accounting columns.

## Evidence

The source PDF exposes stable row baselines and column geometry on pages
`5969–5972`. The repeated header anchors are approximately:

- Actual Cost: `x=304.8`
- Par Value: `x=360.9`
- Fair Value: `x=409.5`
- Book/Adjusted Carrying Value: `x=458.2`
- Unrealized Valuation Change: `x=497.8`

The companion coordinate diagnostic captures every numeric token on those
pages with its CUSIP, row baseline, ordinal, and native `x` position:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-coordinate-column-diagnostic-2026-09-15.csv`

The extraction script is:

`scripts/inspect-athene-schedule-d-coordinate-columns.py`

## Boundary

This is coordinate evidence, not an accounting-column assignment. Rates,
interest, dates, and payment fields remain on the same rows, and the x-position
must be combined with row geometry and header anchors before it can replace the
current dot-marker parser.

## Next test

Use the coordinate tokens to assign only the five leading numeric columns,
compare the resulting page and section sums with the current parser, and
promote the correction only if it reduces both issuer-credit and ABS residuals
without imputing source blanks.
