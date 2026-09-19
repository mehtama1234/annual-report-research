# Retail supplier-finance roll-forward screen — 2026-09-16

This screen advances Q-04 from a single period-end supplier-finance balance to
a dated comparative movement surface. It is still a liability roll-forward
screen, not a settlement ledger or an owner-cash adjustment.

## Reported comparative balances

| Company | As-of date | Eligible / outstanding obligation | Comparison | Mechanical change | Safe reading |
| --- | --- | ---: | --- | ---: | --- |
| Target | August 1, 2026 | `$3.2B` | January 31, 2026: `$3.0B` | `+$0.2B` | Period-end eligible vendor obligation increased; settlement cash is not disclosed here |
| Target | August 1, 2026 | `$3.2B` | August 2, 2025: `$2.9B` | `+$0.3B` | Year-over-year obligation increased; this is not a cash-flow attribution |
| Walmart | July 31, 2026 | `$6.4B` | January 31, 2026: `$6.0B` | `+$0.4B` | Period-end obligation increased; the H1 AP cash-flow row remains a separate period screen |
| Walmart | July 31, 2026 | `$6.4B` | July 31, 2025: `$5.7B` | `+$0.7B` | Year-over-year obligation increased; settlement timing and cash disbursement remain open |

The changes are calculated from the comparative balances disclosed in each
company’s latest Q2 filing. They show obligation scale and direction, not the
amount of supplier invoices paid during the period. Target explicitly states
that the balances do not represent actual early payments made under the
programs; Walmart describes the obligations as amounts payable to financial
institutions on invoice due dates.

## Annual Walmart settlement-flow upgrade — September 17, 2026

Walmart's FY2026 annual filing adds an actual annual program roll-forward:
beginning confirmed obligations of `$5.725B`, invoices confirmed of `$40.342B`,
confirmed invoices paid of `$40.062B`, translation and other of `-$16M`, and
ending obligations of `$5.989B`. The arithmetic reconciles exactly:
`5.725 + 40.342 - 40.062 - 0.016 = 5.989` (billions).

This upgrades Walmart from period-end obligation visibility to an annual
settlement-flow observation. It does not allocate the paid invoices to the
current H1 period, identify the portion affecting operating-cash timing, or
close Target's settlement gap. Q-04 remains partial and no supplier-finance
balance is subtracted from H1 owner cash without a matched-period bridge.

Target's FY2025 annual filing supplies a comparable annual roll-forward:
beginning obligations of `$3.666B`, invoices confirmed of `$11.426B`, confirmed
invoices paid of `$12.066B`, and ending obligations of `$3.026B`. It reconciles
as `3.666 + 11.426 - 12.066 = 3.026` (billions). Target also warns that
eligible obligations do not represent actual early payments made under the
programs; the paid-invoice row is settlement-flow evidence, not a matched H1
cash adjustment or a measure of vendor receivables sold.

## Denominator boundary

The roll-forward must not be added to or subtracted from operating cash flow
without a settlement-date bridge. The existing H1 AP cash-flow rows are already
part of operating cash flow. Adding the full period-end supplier-finance
balance, or adding its mechanical change without proving the cash settlement,
would double count working-capital timing.

This screen therefore upgrades Q-04 to `dated-supplier-finance-movement-visible`
for Target and Walmart, while normalized recurring owner cash remains open.
TJX remains `not-separately-quantified` in this source perimeter.

## Next test

Obtain the next filing's supplier-finance comparative table and, if disclosed,
the settlement or payment-date reconciliation to accounts payable and cash
disbursements. A promotion requires the legal obligation, reporting date,
settlement timing, and cash-flow classification to join without double counting.

Sources: [Target Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm), Note 7; [Target FY2025 annual filing, Note 14](https://corporate.target.com/investors/annual/2025-annual-report/10-k-report/10-k-part-ii/item-8-financial-statements-and-supplementary-data); [Walmart Q2 FY2027 Form 10-Q](https://stock.walmart.com/sec-filings/all-sec-filings/content/0000104169-26-000154/wmt-20260731.htm), Supplier Financing Program Obligations; and [Walmart FY2026 annual filing](https://stock.walmart.com/sec-filings/all-sec-filings/content/0000104169-26-000055/wmt-20260131.htm).
