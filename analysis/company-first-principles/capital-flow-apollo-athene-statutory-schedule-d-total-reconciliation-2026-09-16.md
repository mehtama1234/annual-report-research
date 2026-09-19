# Apollo–Athene Schedule D aggregate-total reconciliation

Research date: `2026-09-16`

## Purpose

The residual row-boundary inspection showed that the raw candidate pool does
not represent additional holdings. This pass records the exact aggregate
comparison that can safely be used for the Athene legal-entity holdings base.

## Reconciliation

The current diagnostic reports the following section totals:

| Scope | Parsed book value | Statutory reference | Difference |
| --- | ---: | ---: | ---: |
| Schedule D Part 1 Section 1 | `$85,388,493,721` | `$85,388,493,720` | `+$1` |
| Schedule D Part 1 Section 2 | `$73,463,901,478` | `$73,463,901,477` | `+$1` |
| Combined source reference | `$158,852,395,199` | `$158,852,395,201` | `-$2` |

The machine-readable section comparison is in the [reconciliation table](data/capital-flow-apollo-athene-statutory-schedule-d-total-reconciliation-2026-09-16.csv).

The two section references sum to `$158,852,395,197`, whereas the separately
stored total-bonds reference is `$158,852,395,201`. The parser's combined total
is `$158,852,395,199`, two dollars below that total reference. Accordingly,
the section-level ties and the combined two-dollar variance are both retained
explicitly; no reference mismatch is silently normalized.

## Constrained promotion

The Schedule D parser can now be promoted to an `aggregate-total-reconciled`
legal-entity holdings denominator for Section 1 and Section 2. The promotion
is limited to aggregate book-value coverage and does not certify every parsed
row's non-book columns. Blank statutory fields and positional extraction risks
still matter for interest income, proceeds, realized gains, impairments, and
lot chronology.

## What this proves

1. The section-level Schedule D book-value totals are reproduced within one
   dollar of their statutory references.
2. The 61 raw row-like candidates should not be added to the holdings base.
3. The legal-entity denominator can support aggregate exposure and coverage
   calculations.

## What it does not prove

It does not prove holding-level investment income, disposal proceeds, realized
gain/loss, impairment, liability funding cost, borrower repayment, trustee
remittance, parent receipt, or asset-level return. The two same-CUSIP routes
remain separate bridge observations until lot continuity and settlement are
documented.

## Safe claim

`Athene's Schedule D Part 1 Sections 1 and 2 are aggregate-book-value
reconciled within one dollar of their statutory section references after raw
candidate duplicates and continuation text are excluded. This establishes a
legal-entity holdings denominator, not asset-level cash-return proof.`
