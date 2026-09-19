# Apollo Debt Solutions BDC issuer cash/return bridge — 2026-09-16

## Purpose

This bridge uses the issuer's Q2 2026 SEC structured facts to constrain the
Apollo Debt Solutions route. It is not an allocation of issuer economics to
Athene's `03770D-AC-7` disposal candidate.

## H1 FY2026 issuer observations

| Measure | Reported value | Safe interpretation |
| --- | ---: | --- |
| Gross investment income | `$1.153510B` | Issuer-wide investment-income numerator |
| Net investment income | `$599.045M` | Issuer-wide income after operating expenses; not cash and not note-specific |
| Interest expense on borrowings | `$323.289M` | Issuer-wide borrowing-cost burden |
| Cash interest paid | `$312.890M` | H1 issuer cash outflow for interest; not allocated to the candidate note |
| Dividends paid | `$398.539M` | H1 issuer financing outflow; not proof of Apollo receipt |
| Common-stock issuance proceeds | `$782.527M` | H1 issuer financing inflow |
| Debt issuance proceeds | `$4.714695B` | H1 issuer financing inflow |
| Long-term debt repayments | `$2.031953B` | H1 issuer financing outflow |
| Net financing cash flow | `$1.617107B` | H1 issuer financing subtotal after reported financing flows |
| Cash at June 30, 2026 | `$857.638M` | Quarter-end issuer cash balance, not distributable cash |
| Debt face amount at June 30, 2026 | `$16.568B` | Issuer debt-scale denominator |

The visible financing components reconcile only partially:

```text
common-stock proceeds                    $0.782527B
debt-issuance proceeds                   $4.714695B
less long-term debt repayments          ($2.031953B)
less dividends paid                     ($0.398539B)
                                           ---------
visible component subtotal              $3.066730B
reported net financing cash flow        $1.617107B
unattributed additional financing use   $1.449623B
```

The `$1.449623B` difference is a reconciliation gap, not a cash source or an
Athene allocation. It requires the complete financing statement and related
debt/equity/distribution detail before the BDC's issuer cash waterfall can be
called complete.

The structured facts also report `$29.442M` of net amortization of investment
discount and premium during H1. This reinforces that reported investment
income and net investment income contain accounting components that cannot be
treated as note-level cash receipts without the issuer schedule and cash-flow
reconciliation.

## Relation to Athene candidate

Athene's approximately `$215.832M` disposal consideration is only `1.30%` of
the BDC's June 30 debt face amount and `35.972%` of the identified `$600M`
Apollo Debt Solutions note issue. Those ratios are scale comparisons, not
ownership or funding allocations. Issuer-wide H1 net investment income is
approximately `2.776x` the Athene consideration, but that ratio has no return
meaning for Athene's lot because the issuer's portfolio, capital structure,
and cash distributions are not joined to the statutory row.

## Proof boundary

| Layer | Status | Missing evidence |
| --- | --- | --- |
| Issuer income, cash, debt scale | `issuer-level-facts-confirmed` | Full filing-level cash-flow and debt schedule join in the named route |
| Note-level coupon carry | `illustrative-sensitivity` | Athene lot, holding period, payment history, and sale settlement |
| Borrower/portfolio cash | `held` | Underlying borrower receipts, repayment, loss, and portfolio allocation |
| Liability-adjusted return | `held` | Athene liability cost, credited rate, taxes, fees, and period-matched funding |
| Apollo common-owner cash | `held` | BDC distribution, parent receipt, debt/preferred claims, and residual availability |

Structured bridge: [issuer cash/return CSV](data/capital-flow-apollo-athene-apollo-debt-solutions-issuer-cash-return-bridge-2026-09-16.csv).

Primary source: [Apollo Debt Solutions BDC Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1837532/000119312526341358/ck0001837532-20260630.htm) and [SEC company facts API](https://data.sec.gov/api/xbrl/companyfacts/CIK0001837532.json).
