# Apollo/Athene statutory page-18 net investment income full-table pass 1

Research date: `2026-09-18`

## Result

The full Exhibit of Net Investment Income on statutory page `18` is now
normalized in the [structured table](data/capital-flow-apollo-athene-statutory-page18-net-investment-income-full-table-pass-1.csv).
It contains `16` source rows, including blank source cells, category rows, and
the total gross-income control.

The category amounts reconcile to the reported total gross investment income
within the source/control tolerance:

- Collected during year: category rows `$13,601,183,682` versus total control
  `$13,601,183,683` — `$1` difference.
- Earned during year: `$14,010,808,604`.

The table adds the rows omitted from the earlier compact extraction: U.S.
government bonds, preferred and common stocks, real estate, contract loans,
cash/short-term investments, derivatives, and aggregate write-ins. It also
preserves the negative `Other invested assets` row rather than treating it as a
Schedule BA loss.

## Boundary

This closes the page-18 extraction gap, not the named-asset cash gap. The
categories remain legal-entity income presentations. They do not identify a
CUSIP, borrower, property, derivative counterparty, settlement account,
liability cost, or Apollo parent receipt. The blank rows are source blanks, not
zeroes.

The normalized table supports the next reconciliation: map category rows to
Schedule D/BA populations and the statutory cash-flow statement, while keeping
Part 1 Schedule BA row income and Part 3 event income separate until their
perimeters are proven equivalent.

## Primary evidence

Athene Annuity and Life Company 2025 statutory statement, page `18`, Exhibit of
Net Investment Income and Details of Write-ins.
