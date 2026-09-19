# Exchange and information infrastructure valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench separates two control-point models: CME monetizes trusted
clearing and market liquidity; S&P Global monetizes institutional information,
ratings, indexes, and workflow. Their reported cash surfaces cannot be pooled.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment/denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| CME Group | Clearing/transaction fees and market-data cash after default-risk capital, collateral mechanics, technology, regulation, and diluted distributions | Clearing infrastructure, guaranty-fund/default resources, technology, capital requirements, customer collateral, debt, and buybacks | Volume/rate shock, clearing member default, collateral call, guaranty-fund replenishment, regulatory capital, cyber event, or funding stress | Operating cash rises with volume while collateral, default-risk capital, or required technology/regulatory spending consumes the common residual |
| S&P Global | Organic subscription, ratings, index, and data cash after acquired-cohort integration, intangible replacement, SBC, debt, and dilution | Acquisition cash, disposition proceeds, amortization, data/platform investment, SBC replacement, working capital, debt, and repurchases | Ratings-cycle slowdown, issuance-volume shock, acquisition financing, refinancing, cyber/data disruption, or customer budget pressure | FCF rises with disposition proceeds or amortization add-backs while organic retention, acquired-cohort return, or diluted common cash weakens |

## Current evidence anchors

- CME H1 revenue was `$3.586B`, clearing and transaction fees `$2.895B`, market
  data `$462.2M`, and operating cash `$2.207B`; its Federal Reserve cash account
  was `$138.5B` and performance-bond/guaranty-fund contributions decreased
  `$1.545B`. These collateral and clearing-resource balances are not
  automatically owner cash.
- S&P Global H1 revenue increased `10%`, operating cash was `$2.476B`, capex
  `$65M`, acquisitions `$26M`, disposition proceeds `$361M`, reported FCF
  `$2.249B`, amortization `$551M`, and SBC `$95M`. Disposition proceeds and
  purchased-intangible amortization require separate organic-cash treatment.

## QoE and financial-shenanigans prompts

1. Separate CME customer collateral, Federal Reserve cash, guaranty funds, and
   default-risk resources from corporate cash and common distributions.
2. Reconcile CME volume and rate per contract to technology, capital,
   guaranty-fund, and member-liquidity claims before capitalizing growth.
3. Remove S&P disposition proceeds from recurring information cash and test
   acquired-cohort retention, integration, and return.
4. Do not add back S&P amortization mechanically; test whether acquired
   intangible replacement and platform investment are recurring burdens.
5. Carry SBC, repurchases, debt, and NCI/other claims into diluted per-share
   cash rather than treating reported FCF as a complete numerator.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what fee/subscription retention,
clearing spread, acquired-cohort return, regulatory capital, and reinvestment
the price requires. The Lyn Alden-style stress test asks whether market volume,
collateral, member liquidity, rates, issuance cycles, acquisitions, cyber risk,
and refinancing can transmit into common distributions.

## Promotion boundary

`exchange-information-qualified; collateral-and-organic-cash-open; no-ranking`

Promotion requires a same-entity bridge from clearing or information activity
to collected corporate cash, required risk/infrastructure capital, acquired-
cohort return, legal availability, and diluted common residual. Collateral,
volume, disposition proceeds, FCF, amortization, and SBC remain diagnostic
inputs.

## Sources

- [Exchange/information Q2 2026 cash-quality refresh](combined-investment-research-exchange-information-infrastructure-q2-2026-cash-quality-refresh-2026-09-17.md)
- [CME Group Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1156375/000115637526000047/cme-20260630.htm)
- [S&P Global Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/64040/000006404026000045/spgi-20260630.htm)

