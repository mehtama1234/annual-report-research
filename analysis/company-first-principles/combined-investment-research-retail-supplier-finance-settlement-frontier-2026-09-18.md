# Retail supplier-finance settlement frontier

Research date: `2026-09-18`

## Purpose

This control separates supplier-finance obligation balances from actual
settlement cash. It prevents the same payable movement from being counted once
as operating-cash support and again as a cash deduction from owner cash.

## Current-period evidence

| Company / period | Reported OCF | Accounts-payable cash source | Eligible/outstanding supplier-finance obligation | Comparable opening obligation | Mechanical obligation change | Safe interpretation |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Target H1 2026 | `$4.519B` | `$612M` | `$3.2B` | `$3.0B` | `+$200M` | Obligation perimeter and payable support are visible; actual invoice settlement is not |
| Walmart H1 FY2027 | `$19.710B` | `$1.257B` | `$6.4B` | `$6.0B` | `+$400M` | Outstanding obligation and payable support are visible; confirmed-invoice cash settlement is not |
| TJX H1 FY2027 | `$3.345B` | Filing does not provide a comparable supplier-finance roll-forward | No comparable current supplier-finance balance in the reviewed packet | — | — | Do not infer absence, cash support, or settlement from the missing note |

Target states that vendor early payment is optional and does not change
Target's remittance amount or payment date; the remittance date may be up to
120 days from invoice date. Target's Q2 2026 filing also expressly states that
the `$3.2B` eligible-obligation balance does **not** represent actual early
payments and that actual early payments have historically been lower. Walmart
states that it pays financial institutions the confirmed invoice amount on the
due date. Neither filing provides the
complete opening-invoice, confirmation, early-payment, financial-institution
payment, retailer-remittance, and closing-obligation waterfall.

This is a useful asymmetry: Target directly disclaims the most tempting
interpretation of its period-end balance, while Walmart gives the payment
obligation mechanics but not the period-matched confirmation and settlement
population. Neither disclosure closes Q-04.

## Settlement attribution frontier

The mechanical obligation changes create only a bounded sensitivity surface:

| Company | 0% of change | 25% | 50% | 75% | 100% |
| --- | ---: | ---: | ---: | ---: | ---: |
| Target | `$0M` | `$50M` | `$100M` | `$150M` | `$200M` |
| Walmart | `$0M` | `$100M` | `$200M` | `$300M` | `$400M` |

These columns are not observed cash settlements. They show the range of
possible attribution if a later invoice-level schedule establishes that some
or all of the period-end obligation change corresponds to a cash-timing event.
Until then, none of the columns may be subtracted from OCF, added to owner
cash, or treated as permanent financing.

## Denominator rule

The current safe screen remains:

```text
reported OCF - reported property spending
```

No additional deduction is made for the full supplier-finance balance or its
mechanical change. A future promotion requires a same-period roll-forward
joining opening obligation, confirmed invoices, invoices paid by the financial
institution, retailer remittance dates, early-payment elections, AP movement,
cash-flow classification, and closing obligation.

## Promotion result

`Q-04-settlement-unproven; CA-06-partial; no-ranking`

This frontier upgrades the non-double-counting and falsifiability controls. It
does not promote Target or Walmart supplier financing into normalized cash and
does not classify TJX's missing comparable note as a negative finding.

The machine-readable [settlement-frontier control](data/combined-investment-research-retail-supplier-finance-settlement-frontier-2026-09-18.csv)
preserves the two current-period disclosure boundaries and their distinct
missing fields.

## Sources

- [Target Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm)
- [Walmart Q2 FY2027 Form 10-Q](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm)
- [Retail Q2 supplier-finance obligation refresh](combined-investment-research-retail-q2-2026-supplier-finance-obligation-refresh-2026-09-17.md)
