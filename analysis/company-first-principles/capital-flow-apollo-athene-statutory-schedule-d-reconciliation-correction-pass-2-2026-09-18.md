# Apollo–Athene Schedule D Reconciliation Correction Pass 2

## Purpose

This pass reruns the full-range Athene statutory Schedule D parser after the
current row-start and numeric-column corrections, then compares the generated
book-value fields with the compact statutory verification references.

## Current result

The parser produces `8,648` rows across Schedule D Part 1 Section 1 and
Section 2. The aggregate book-value tie is now effectively exact at whole-dollar
scale:

| Scope | Parser book/adjusted carrying value | Statutory reference | Difference | Interpretation |
|---|---:|---:|---:|---|
| Section 1 issuer-credit | `$85,388,493,721` | `$85,388,493,720` | `+$1` | Near-exact aggregate tie; still requires tolerance policy and row-level review. |
| Section 2 ABS | `$73,463,901,478` | `$73,463,901,477` | `+$1` | Near-exact aggregate tie; page-level numeric blanks remain on selected pages. |
| Sections 1 + 2 | `$158,852,395,199` | `$158,852,395,201` | `-$2` | Near-exact combined tie; not yet final accounting proof. |

The current page diagnostic covers `192` pages: `156` coverage-visible,
`25` medium-priority column-correction, and `11` high-priority
column-correction pages. The highest-risk pages are concentrated in ABS pages
`5970`, `5971`, `5937`, `5972`, `5917`, `5939`, `5969`, `5916`, `5927`,
`5962`, and `5940`, where extracted numeric columns contain substantial blanks
or wrapping artifacts despite the aggregate tie.

## Raw ABS page inspection

Direct extraction of pages `5916`, `5917`, `5937`, `5939`, `5940`, `5969`,
`5970`, `5971`, and `5972` shows that the low field-coverage signal has two
different causes:

| Page pattern | Observation | Correct treatment |
|---|---|---|
| NIM-heavy pages `5970`–`5971` | Many source rows visibly leave actual cost, fair value, and book/adjusted carrying value blank while still reporting par value, rates, dates, or small payment fields. | Preserve source blanks; do not backfill trailing numeric tokens into asset-value columns. |
| Mixed legacy ABS page `5937` | Fully populated mortgage/securitization rows sit beside NIM or otherwise sparse rows. | Normalize row-by-row using explicit dot-delimited column positions and asset subtype, not page-wide imputation. |
| Mixed pages `5916`–`5917`, `5939`–`5940`, `5969`, `5972` | Regular ABS rows have complete value fields, while selected sparse rows remain visibly blank in the source. | Keep the page flagged for semantic review, but distinguish source-visible blanks from extraction loss. |

This inspection lowers confidence in a blanket “missing-column” explanation.
The next repair should classify source-visible blanks versus parser shifts and
should not fill blank statutory values merely to improve field coverage.
The reusable [sparse-row classification worklist](capital-flow-apollo-athene-statutory-sparse-row-classification-pass-1.md)
now identifies `608` sparse rows: `107` NIM-pattern rows to preserve without
imputation, `298` source-visible or legacy-ABS sparse rows for row review, and
`203` non-NIM sparse rows for highest-priority column review.

## What this proves

- The current row recognizer and aggregate numeric mapping capture the two
  principal Schedule D populations at near-exact total scale.
- The earlier apparent hundreds-of-millions residual was a stale diagnostic
  relative to the current generated output; it should not be used as the
  current gap.
- The output is strong enough for named-holding discovery, page-level repair
  targeting, issuer/CUSIP worklists, and the next income/proceeds join.

## What this does not prove

The aggregate tie does not by itself prove every row's book value, investment
income, realized gain/loss, impairment, liability cost, borrower receipt,
trustee remittance, or asset-level return. A parser can offset row-level
column errors while still matching a total.

## Promotion boundary

Keep the status at:

`near-reconciled-schedule-d; row-level-ABS-repair-and-income-join-open`

Do not promote the Schedule D output to final statutory portfolio accounting,
liability-adjusted spread, borrower cash, or return evidence until the
high-priority ABS pages are classified at row/subtype level and the rows are
joined to investment income, disposal/proceeds, realized-gain/loss, impairment,
and liability-cost fields.

## Reproducibility

Parser:

`python3 scripts/extract-athene-statutory-detail-samples.py`

Reconciliation:

`python3 scripts/reconcile-athene-schedule-d-parser.py`

Current outputs:

- `analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-full-range-parser-pass-1.csv`
- `analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-reconciliation-diagnostic-pass-1.csv`
- `analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-page-diagnostic-pass-1.csv`

Decision: `apollo-athene-schedule-d-near-exact-aggregate-tie; row-level-repair-open`
