# Apollo–Athene Schedule D Reconciliation Upgrade

Research date: `2026-09-15`

## Root cause corrected

The Schedule D parser's plain NAIC marker expression matched the prefix of
coupon decimals such as `3.935` as if `3.` were a designation. That shifted the
five leading numeric fields on affected rows. The parser now requires a plain
designation marker not to be followed by another digit.

## Reconciliation result

The corrected full-range parser still produces `8,648` Schedule D Part 1 rows,
but now reconciles the two located sections to their compact statutory
verification references within one dollar:

| Section | Parser book/adjusted carrying value | Verification reference | Difference |
| --- | ---: | ---: | ---: |
| Issuer credit | `$85,388,493,721` | `$85,388,493,720` | `$1` |
| Asset-backed securities | `$73,463,901,478` | `$73,463,901,477` | `$1` |
| Combined sections | `$158,852,395,199` | `$158,852,395,201` | `$(2)` |

The exact reconciliation diagnostic remains at:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-schedule-d-reconciliation-diagnostic-pass-1.csv`

## What this proves

The full located issuer-credit and ABS Schedule D population is now suitable
for reconciled legal-entity portfolio analysis at the section-total level.
This materially upgrades the statutory asset denominator and makes named
holding, income, disposal, impairment, and liability-cost joins actionable.

## Boundary

Section-total reconciliation does not by itself prove every row's accounting
column, borrower destination, asset-level cash receipt, realized return,
liability-cost spread, regulated-capital allocation, or Apollo common-owner
cash. Those remain separate joins.

## Next test

Use the reconciled rows to join named holdings to statutory investment income,
disposal proceeds, impairments, funding cost, liability spread, and parent
receipt routes. Promote asset-level return claims only where the row-level
counterparty and cash path also reconcile.

## Safe claim

`Athene's full located Schedule D issuer-credit and ABS sections now reconcile
to compact statutory verification references within one dollar after fixing a
coupon-decimal/NAIC-marker parser collision. This proves a reconciled
legal-entity portfolio denominator, not yet asset-level return or common-owner
cash.`
