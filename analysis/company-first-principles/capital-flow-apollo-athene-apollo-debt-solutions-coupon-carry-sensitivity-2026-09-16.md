# Apollo–Athene Apollo Debt Solutions coupon-carry sensitivity — 2026-09-16

## Purpose

This is a bounded return-input screen for the exact Apollo Debt Solutions BDC
instrument identified in Athene's statutory disposal row. It does not convert
the disposal candidate into a settled trade, borrower repayment, or realized
return.

## Observable inputs

The SEC-filed indenture identifies CUSIP `03770DAC7`, Apollo Debt Solutions BDC
as issuer, a `6.700%` coupon, a July 29, 2031 maturity, and `$600M` initial
principal. Athene's statutory row carries approximately `$215.832M` of
consideration and `$8.587M` of interest/dividend fields, but the public record
does not identify whether that consideration was a par sale, the exact lot,
settlement date, or whether the interest/dividend field belongs to this note.

## Mechanical carry screen

Using the Athene consideration only as a notional share of the issue produces
`$215.832M / $600M = 35.972%`. Applying that ratio to the stated coupon gives a
gross annual coupon-carry proxy of approximately `$14.461M`:

```text
$600.000M × 6.700% × 35.972% = $14.461M
```

This is a par-equivalent carry sensitivity, not observed Athene income. It
assumes the candidate represented a proportional par-like position and that
the note remained outstanding for a full year. Five-year gross carry under the
same assumptions is approximately `$72.304M` before price, accrued interest,
tax, default/loss, fees, funding cost, and liability-crediting costs.

The separate `$8.587M` statutory interest/dividend field is retained as an
unjoined observation and is not added to the proxy. It could reflect another
lot, a shorter holding period, different instruments, or a different statutory
classification.

## Proof boundary

| Layer | Status | Missing evidence |
| --- | --- | --- |
| Issuer, CUSIP, coupon, maturity, issue size | `instrument-confirmed` | None for the stated indenture terms |
| Athene disposal consideration | `candidate-visible` | Trade confirmation, lot quantity, price, accrued interest, settlement cash |
| Gross coupon carry | `illustrative-sensitivity` | Holding period, actual principal, payment history, realized sale price |
| Net investment return | `held` | Borrower/BDC cash, losses, fees, taxes, liability cost, and Athene allocation |
| Apollo common-owner cash | `held` | BDC-to-Apollo distribution, parent receipt, debt/preferred/NCI claims, and residual |

Structured sensitivity: [coupon-carry CSV](data/capital-flow-apollo-athene-apollo-debt-solutions-coupon-carry-sensitivity-2026-09-16.csv).

Sources: [SEC second supplemental indenture](https://www.sec.gov/Archives/edgar/data/1837532/000119312524187649/d849659dex42.htm) and [Apollo Debt Solutions BDC prospectus](https://www.apollo.com/content/dam/apolloaem/documents/fund-documents/ads-prospectus.pdf).
