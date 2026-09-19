# Apollo/Athene page-18 to Schedule D income reconciliation pass 3

Research date: `2026-09-18`

## Breakthrough reconciliation

The earlier `$1.897374415B` difference between page-18 collected bond income
and year-end Schedule D Part 1 received interest is now explained by the
filing's own population and footnote controls:

```text
Schedule D Part 1 interest received                         6,230,478,121
Schedule D Part 4/5 bond interest/dividends received        2,207,402,908
Page-18 footnote net bond collection adjustment               (310,028,491)
Reconstructed page-18 bond collected income                 8,127,852,538
Page-18 reported bond collected income                      8,127,852,536
Source difference                                                     (2)
```

The Part 4/5 amount is controlled by the Schedule D “Total - issuer credit
obligations and asset-backed securities” row on page 6282, whose bond
interest/dividends received total is `$2.207402908B`. The Part 1 amount is
controlled by the issuer-credit and ABS subtotal rows on pages 5911 and 6027.
The page-18 adjustment is the filing footnote: `$400.899897M` discount accrual
less `$223.877582M` premium amortization less `$487.050806M` accrued interest
paid on purchases, or negative `$310.028491M`.

## What this closes

This is a near-exact statutory reconciliation of the page-18 **collected bond
category** to the year-end and disposed-population Schedule D fields, within
`$2`. It removes the prior residual as an unexplained missing-row or generic
category gap.

The structured control is in the [reconciliation CSV](data/capital-flow-apollo-athene-statutory-page18-schedule-d-income-reconciliation-pass-3.csv).

## What this does not close

The result remains statutory legal-entity evidence. It does not prove:

- a named borrower made a bank payment;
- a trustee, custodian, or paying agent remitted the amount;
- liability funding cost or credited-rate burden;
- asset-level realized return; or
- Apollo parent or common-owner cash.

The page-18 **earned** column remains a separate accounting bridge and is not
substituted into this collected-income reconciliation.

## Decision

`page18-schedule-d-bond-collected-income-near-reconciled-within-2; owner-cash-and-borrower-receipt-open`

The next step is to carry the controlled `$2` source difference into the legal-
entity bridge and then pursue liability-cost and named-settlement evidence.
