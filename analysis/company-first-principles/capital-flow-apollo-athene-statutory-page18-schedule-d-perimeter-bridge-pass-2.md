# Apollo/Athene page-18 to Schedule D perimeter bridge pass 2

Research date: `2026-09-18`

## What the source clarifies

The Athene 2025 statutory PDF presents page 18 as an **Exhibit of Net
Investment Income**. Its bond categories show `$8.127852536B` collected and
`$8.279777653B` earned across U.S. government bonds, other unaffiliated bonds,
and bonds of affiliates. Footnote (a) separately identifies `$400.899897M` of
discount accrual, `$223.877582M` of premium amortization, and `$487.050806M`
paid for accrued interest on purchases.

The corrected Schedule D parser presents a different object: row-level fields
named **Interest Income Due & Accrued** and **Interest Received During Year**.
Across the located issuer-credit and asset-backed-security population, those
fields sum to `$1.504450447B` and `$6.230478121B`, respectively.

## Controlled comparisons

| Comparison | Amount | Status |
|---|---:|---|
| Page-18 collected bond categories | `$8.127852536B` | source-controlled gross category |
| Page-18 earned bond categories | `$8.279777653B` | source-controlled gross category |
| Schedule D interest income due/accrued | `$1.504450447B` | source-controlled row-field sum |
| Schedule D interest received during year | `$6.230478121B` | source-controlled row-field sum |
| Page-18 collected less Schedule D received | `$1.897374415B` | cross-object diagnostic |
| Page-18 collected less both Schedule D fields | `$392.923968M` | definition diagnostic, not a reconciliation |

The second comparison is useful only as a warning: adding due/accrued income to
received interest does not make the objects comparable. The source does not
yet establish that the page-18 columns and the Schedule D fields share the
same recognition, population, or adjustment perimeter.

## Decision

`page18-schedule-d-definition-boundary-strengthened; received-interest-join-open`

The earlier `$1.897374415B` residual remains a category/perimeter diagnostic.
It is not a loss, missing bank receipt, uncollected receivable, borrower
shortfall, or Apollo owner cash. The structured controls are in the [perimeter
bridge CSV](data/capital-flow-apollo-athene-statutory-page18-schedule-d-perimeter-bridge-pass-2.csv).

The next promotion-quality evidence would be a statutory workpaper or
same-definition reconciliation that maps page-18 bond categories to Schedule D
row fields, including the footnote adjustments and source-visible blanks. In
parallel, AP Grange's corrected `$230.263772M` received-interest field still
requires custody, trustee, bank, or legal-entity settlement evidence before it
can become a borrower receipt or Apollo owner-cash observation.
