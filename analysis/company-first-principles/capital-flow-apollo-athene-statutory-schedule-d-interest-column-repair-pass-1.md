# Apollo/Athene Schedule D interest-column repair pass 1

Research date: `2026-09-18`

## Defect repaired

The Schedule D normalization helper previously used the final two numeric
tokens in a row as `interest_income` and `interest_received_during_year`. That
was unsafe because the final numeric token is often `Payment Due at Maturity`.
For example, a Treasury Strip row had par value `$362,000` in that final
column, and the old output labeled it received interest.

The parser now anchors on the first acquisition date in the row. The two
immediately preceding source columns are the interest-income and
interest-received fields, preserving variable blank columns and excluding
payment-at-maturity.

## Validation observations

| Object | Corrected observation | Interpretation |
|---|---:|---|
| Treasury Strip `912803-DM-2` | Interest income blank; interest received blank | Source blanks are preserved; par value is no longer treated as cash income |
| AP Grange Tranche A `G2964#-AA-7` | `$7.219623M` interest income due/accrued; `$230.263772M` interest received | Named legal-entity holding-level received-interest field is now correctly located |
| Full Schedule D Sections 1–2 | `$6.230478121B` corrected received-interest sum | Parser population now has a usable directional received-interest control, still requiring category reconciliation |

## Page-18 comparison boundary

The page-18 collected bond categories—U.S. government bonds, other
unaffiliated bonds, and bonds of affiliates—sum to `$8.127852536B`. The
corrected Schedule D Sections 1–2 received-interest sum is `$6.230478121B`, a
`$1.897374415B` difference.

This is not yet a completed reconciliation. Possible contributors include
Schedule D population scope, category classification, source-visible blanks,
interest-field semantics, and the relationship between the page-18 exhibit and
the detailed Schedule D rows. The difference is therefore retained as a join
diagnostic, not as a credit loss, uncollected receivable, or missing cash.

## Decision

`schedule-d-interest-column-repaired; received-interest-category-join-open`

The repair improves the named-asset route: AP Grange now has a correctly
located legal-entity received-interest observation. It still does not prove
borrower payment, trustee settlement, liability-adjusted return, or Apollo
common-owner cash.

The structured repair controls are in [the repair CSV](data/capital-flow-apollo-athene-statutory-schedule-d-interest-column-repair-pass-1.csv).
