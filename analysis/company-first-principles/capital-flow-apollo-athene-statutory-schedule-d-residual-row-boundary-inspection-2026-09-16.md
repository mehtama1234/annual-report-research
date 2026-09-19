# Apollo–Athene Schedule D residual row-boundary inspection

Research date: `2026-09-16`

## Purpose

The residual diagnostic identified 61 raw row-like candidates whose apparent
book values must not be added automatically. This targeted pass inspects the
two largest candidates, one from each Schedule D section, against the current
full-range parser output.

## Findings

| Page | Raw candidate | Existing parsed row | Apparent book value | Finding |
| ---: | --- | --- | ---: | --- |
| 5904 | `A-1` | `00240#-AA-4` / `CFAASDFR-3128` | `$682.295M` | Continuation or tranche label inside the existing AP Fides row; the apparent value exactly matches the parsed row. |
| 6023 | `ADVANCE` | `049400-AA-2` / `CFAASDFR-8514` | `$1.413B` | Wrapped description continuation inside the existing Atlas Secured Advance Funding row; the apparent value exactly matches the parsed row. |

The machine-readable inspection is in the [residual row-boundary table](data/capital-flow-apollo-athene-statutory-schedule-d-residual-row-boundary-inspection-2026-09-16.csv).

## Full candidate classification

The same-page comparison across the full raw-candidate pool finds `59` of `61`
candidates with an apparent book value that exactly matches an existing parsed
row on the same page: all `44` Section 1 candidates and `15` of `17` Section 2
candidates. The remaining two Section 2 candidates are continuation text on
pages `5972` and `5976` (`NOTE` and `IO`); their apparent numeric tokens are
compacted non-book fields and do not produce omitted holding rows. Thus all 61
candidates are classified as duplicate or continuation text, with page-level
column review retained for parser quality. The aggregate classification is in
the [candidate classification table](data/capital-flow-apollo-athene-statutory-schedule-d-residual-candidate-classification-2026-09-16.csv).

## Decision

The `59` matched candidates are `duplicate-risk-confirmed` or
`continuation-risk-confirmed`; the two remaining candidates are
`continuation-confirmed`. None must be counted as an additional holding. This
materially explains why the raw candidate pool is larger than the combined
`$233.299M` residual gap, but it does not establish final Schedule D
reconciliation or validate the shifted non-book fields.

The Schedule D parser is now aggregate-total reconciled rather than merely
near-reconciled: current combined parsed book value is
`$158,852,395,199` against the `$158,852,395,201` total reference. The remaining
work is not raw-row recovery; it is validating row-level non-book fields,
subtotal treatment, income, proceeds, liability cost, and return joins.

## Safe claim

`All 61 raw Schedule D residual candidates are classified as duplicate or
continuation text: 59 match existing same-page book values and 2 are
continuation-only rows without a valid omitted book value. None is added to the
holdings total; the Schedule D reconciliation residual remains unresolved.`
