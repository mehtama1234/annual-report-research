# Apollo–Athene ARI cash-perimeter delta boundary

Research date: `2026-09-16`

## Purpose

This memo isolates the numeric difference between ARI's approximate portfolio
consideration and the broader seller cash-flow line. It prevents the
`$9.497267B` cash-flow amount from being silently substituted for the
approximately `$8.6B` sale consideration or the approximately `$8.7B` buyer
portfolio description.

## Mechanical bridge

ARI's Q2 filing describes approximately `$8.6B` of cash consideration for the
portfolio sale. The same filing reports `$9.497267B` of proceeds from repayment
and sale of commercial mortgage loans. The mechanical difference is
`$897.267M` (`$9,497.267M - $8,600M`). Because the consideration is approximate
and the cash-flow line is an aggregate repayment-and-sale category, this delta
cannot be assigned to profit, fees, accrued interest, borrower repayment,
true-up, or Athene funding.

ARI separately reports `$67.578M` of subordinate-loan and other-lending-asset
repayment proceeds. That separate line should not be added to the commercial-
mortgage-loan line when testing the sale-consideration delta. Athene's
approximately `$8.7B` buyer-side description includes accrued interest and is a
separate buyer perimeter. The filing also states that the portfolio perimeter
excluded loans repaid before closing and a Chicago hotel loan with a `$46M`
principal balance that repaid after closing. That timing exception is another
reason the aggregate cash-flow line cannot be treated as a clean closing-wire
amount.

## Proof-grade result

`seller cash-flow and sale-consideration perimeters are numerically compared;
the $897.267M delta is unresolved and not allocated`

The decisive upgrade remains a closing settlement statement, purchase-price
allocation schedule, loan-level repayment and accrued-interest schedule, and
Athene booking/receipt record. The delta is an uncertainty boundary, not a
negative conclusion about the transaction. The latest public filing search
confirms the aggregate line and the timing exception, but does not allocate the
`$897.267M` delta.

## Primary sources

- [ARI Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1467760/000119312526342628/ari-20260630.htm)
- [ARI completion announcement](https://www.sec.gov/Archives/edgar/data/1467760/000119312526177686/d24584dex991.htm)
- [Athene Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1527469/000152746926000056/ahl-20260630.htm)

Structured bridge: [cash-perimeter delta CSV](data/capital-flow-apollo-athene-ari-cash-perimeter-delta-boundary-2026-09-16.csv).
