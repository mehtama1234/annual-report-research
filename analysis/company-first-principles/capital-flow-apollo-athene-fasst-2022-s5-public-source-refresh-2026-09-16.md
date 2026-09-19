# Athene FASST 2022-S5 public-source refresh

Research date: `2026-09-16`

## Question

Can public sources connect Athene's `317384-AA-3` disposal candidate to the
Finance of America Structured Securities Trust 2022-S5 residential-mortgage
pool and a return-relevant trustee/cash-flow path?

## Result

`partial-upgrade` for exact issuer/series, RMBS collateral class, rating,
trustee-report route, and waterfall context; `evidence-insufficient` for exact
Athene settlement, loan-level borrower cash, trustee remittance, liability-
adjusted return, or common-owner cash.

The local Athene Schedule D parser identifies `317384-AA-3`, Finance of
America Structured Securities Trust FASST 2022-S5 Class A1 3.000% due
05/25/62, as a disposal-only `Paydown` candidate with approximately
`$219.082M` of consideration and `$5.143M` of interest/dividend fields from
May 13 through December 25, 2025.

Morningstar DBRS publicly identifies FASST 2022-S5 as a mortgage-backed-note
transaction and lists its classes and ratings, including Class A1 and A2 at
AAA, Class A3 at AA (low), and subordinate M1/M2 classes. U.S. Bank's Trust
Investor Reporting portal lists FASST deals and indicates that detailed
documents require authorized login. Public rating and portal sources establish
the structured mortgage and remittance architecture, but not the actual
loan-level tape, Athene lot settlement, or cash distribution.

## Decision

Promote FASST 2022-S5 to a named RMBS and trustee-report research target. Do
not promote the `$219.1M` statutory consideration to a proven Athene receipt,
borrower repayment, trustee remittance, liability-adjusted return, or Apollo
common-owner cash.

## Next documents

Request the FASST 2022-S5 offering document, loan tape, trustee distribution
reports, paydown/redemption notices, Athene trade confirmation and custodian
ledger, and any servicer loss, prepayment, and delinquency reports. Reconcile
class principal, mortgage collections, servicing/trustee fees, losses,
waterfall priority, insurance liability cost, and taxes before calculating a
return.

## Safe claim

`Public rating and trustee sources identify FASST 2022-S5 as a rated
residential-mortgage transaction with a defined class structure and controlled
reporting route. Athene's $219.1M 317384-AA-3 Paydown row remains a named
cash-like candidate, not proven Athene settlement, mortgage-pool cash,
trustee remittance, or liability-adjusted return.`

## Sources

- [Morningstar DBRS FASST 2022-S5 ratings](https://dbrs.morningstar.com/research/415736/dbrs-morningstar-assigns-ratings-to-23-us-rmbs-transactions)
- [U.S. Bank Trust Investor Reporting portal](https://trustinvestorreporting.usbank.com/TIR/public/dealList/search/76125)
- [Morningstar DBRS FASST waterfall/context example](https://dbrs.morningstar.com/research/419874/db-rs-morningstar-assigns-ratings-to-finance-of-america-structured-securities-trust-2023-s3)

