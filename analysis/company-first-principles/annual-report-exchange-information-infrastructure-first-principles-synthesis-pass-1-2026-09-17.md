# Exchange and information infrastructure: first-principles synthesis — pass 1

Research date: `2026-09-17`

This chapter compares CME Group and S&P Global as financial-infrastructure
businesses. It is a qualified diagnostic, not a ranking: CME monetizes
trading, clearing, settlement, and market access, while S&P Global monetizes
benchmarks, ratings, indices, data, and analytical workflows.

## Force and control point

Market complexity, regulation, risk transfer, passive investment, credit
intermediation, and demand for trusted information increase the value of
permissioned infrastructure. CME's control point is a liquid, regulated market
and clearing network with embedded participant workflows. S&P Global's control
point is trusted benchmark/data/ratings intellectual property embedded in
contracts, investment mandates, and issuance processes.

The main burden differs. CME carries technology, clearing, default-fund,
regulatory, cyber, liquidity, and volume-cycle burdens. S&P Global carries
data quality, model/reputational, regulatory, customer-retention, acquisition,
integration, goodwill/intangible, and debt burdens.

## End-to-end economic chain

```text
market participation and information demand
  -> exchange/clearing access or benchmark/ratings/data workflow
  -> transaction fees, clearing fees, subscriptions, licenses, ratings,
     indices, and analytics
  -> technology, personnel, data, default/risk, regulation, acquisition,
     integration, and customer-retention costs
  -> operating cash after capex and working capital
  -> collateral/restricted balances, debt, dividends, buybacks, SBC, NCI,
     and dilution
  -> common-owner residual
```

Trading volume, open interest, assets benchmarked, index-linked assets,
ratings volume, revenue, adjusted EBITDA, and recurring-revenue labels are
visibility inputs. They are not automatically common-owner cash.

## FY2025 filing-backed comparison

| Company | Revenue | OCF | PP&E / capital spending | Other visible claims | Mechanical screen |
| --- | ---: | ---: | ---: | --- | ---: |
| CME Group | `$6.521B` | `$4.277B` | `$83.5M` PP&E | `$3.933B` dividends; `$3.422B` unsecured long-term debt; `$95.6M` SBC; `$10.515B` goodwill | `$4.194B` OCF less PP&E before dividends, debt, risk/collateral, SBC, and claims |
| S&P Global | `$15.336B` | `$5.651B` | `$195M` PP&E additions | `$2.023B` acquisitions; `$5.001B` repurchases; `$1.170B` common dividends; `$321M` minority dividends; `$236M` SBC; `$13.088B` debt; `$1.745B` cash | OCF is not owner cash until acquisitions, claims, debt, SBC, and dilution are assigned |

The figures are company-level FY2025 diagnostics and are not a multiple or
owner-cash league table. CME's clearing and collateral perimeter requires
separate treatment from corporate cash; S&P's acquisition and goodwill surface
requires cash-paid and acquired-cohort attribution.

## Quality of earnings and financial-shenanigans controls

1. Decompose CME revenue into volume, rate, product mix, market-data, clearing,
   and other fees; test whether volume growth or pricing drives the result.
2. Reconcile clearing collateral, guaranty/default-fund resources, customer
   balances, restricted cash, and margin requirements to legal availability;
   do not call participant collateral owner cash.
3. For S&P Global, separate organic subscription/data/index/ratings growth from
   acquisitions, divestitures, licensing changes, and cross-sell claims.
4. Reconcile receivables, deferred revenue, performance obligations, contract
   costs, and cash collection over matched periods.
5. Test goodwill/intangible additions, amortization, impairment, integration,
   restructuring, and contingent consideration against cash paid and acquired
   revenue/operating contribution.
6. Keep technology, cybersecurity, regulatory, model, and data-quality costs in
   the durability and margin test even when management labels them recurring or
   adjusted.
7. Reconcile dividends and buybacks to post-capex cash, debt, collateral and
   restricted balances, NCI/preferred claims, SBC, and diluted shares.

## Valuation and liquidity handoff

The Damodaran-style input for CME is normalized fee revenue and clearing cash
after cycle, technology, regulatory, risk, and capital requirements. For S&P
Global it is organic recurring information/ratings/index cash after data,
retention, acquisition, debt, integration, and dilution costs. A revenue or
adjusted EBITDA multiple should not ignore the different volume and claim
perimeters.

The Lyn Alden-style stress path is market-volume contraction, credit stress,
rate changes, collateral/margin volatility, regulatory changes, cyber events,
issuance slowdowns, customer budgets, acquisition financing, and refinancing.
The thesis breaker is reported recurring growth or activity alongside weaker
cash collection, rising claims/collateral needs, acquisition dependence,
technology burden, or declining diluted owner cash.

## Promotion rule

Current status:

`qualified-financial-infrastructure-control-point; FY2025-diagnostic; collateral/acquisition/owner-cash-perimeters-open; no-ranking`

Promotion requires same-period revenue composition, volume/pricing or organic
growth, collection, capex, restricted/collateral perimeter, acquisitions,
debt, claims, SBC, dilution, and a common-owner residual. The next exact source
objects are clearing/collateral availability and acquired-cohort cash/return
schedules—not a larger volume, benchmark, or adjusted EBITDA number.

## Sources and verification

- [S&P Global filing denominator verifier](../../scripts/verify-sp-global-filing-denominators.py)
- [CME Group FY2025 10-K](../../raw/sec/financial/investment-brokerage-national/cme-group-inc/2025-10k.html)
- [S&P Global FY2025 10-K](../../raw/sec/financial/investment-brokerage-national/sp-global-inc/2025-10k.html)

