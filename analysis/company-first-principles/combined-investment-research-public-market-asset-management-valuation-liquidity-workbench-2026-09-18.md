# Public-market asset-management valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Franklin Resources from AUM and flow evidence into a
company-specific fee, product-migration, talent, distribution, alternatives,
and capital-return test. It treats retained fee relationships—not client AUM—as
the economic asset and does not treat headline AUM, adjusted earnings, market
appreciation, performance income, dividends, or repurchases as normalized
common-owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Franklin Resources | Common cash after average fee-paying AUM, durable fee rates, flows, product mix, investment talent, distribution, technology, compliance, alternatives cost, remediation, tax, debt, and dilution | Research and investment professionals, distribution, product migration, technology, operations, compliance, acquisitions, and client/liquidity infrastructure | Market decline, active-fund outflows, fee compression, alternatives fundraising/realization slowdown, Western Asset drag, fixed cost, or acquisition/buyback cash use | AUM rises through market appreciation or low-fee products while flows, fee rate, Western Asset economics, recurring costs, cash conversion, or per-share value deteriorate |

## Current evidence anchors

- FY2025 ending AUM was approximately `$1.661T`, long-term net outflows were
  `$97.4B`, operating revenue `$8.771B`, and the effective investment-management
  fee rate fell to `40.5` basis points from `41.1`.
- Q1-Q3 FY2026 long-term inflows were approximately `$28.0B`, `$16.9B`, and
  `$18.4B`; Q3 AUM was `$1.792T`, revenue `$2.358B`, adjusted net income
  `$386.3M`, and adjusted EPS `$0.72`.
- Q3 alternatives AUM was approximately `$294.2B`; Q2 alternatives fundraising
  was about `$14.3B`. Fee-paying AUM, realizations, marks, talent cost, and
  liquidity terms remain separate tests.
- FY2025 dividends were about `$683.7M` and repurchases `$240.3M`. Capital
  returns require comparison with product investment, distribution, technology,
  acquisitions, debt, and per-share cash conversion.

## QoE and financial-shenanigans prompts

1. Reconcile ending and average AUM to market appreciation, gross flows,
   redemptions, net flows, fee-paying AUM, fee rate, and revenue.
2. Split legacy active funds, ETFs/index/SMAs, alternatives/private markets,
   fixed income, international, and cash management by flow and economics.
3. Test whether alternatives AUM produces recurring fees and realizations after
   talent, fundraising, valuation, distribution, and client-liquidity costs.
4. Isolate Western Asset and other weak units by AUM, flows, performance, fee
   rate, personnel, remediation, and parent subsidy.
5. Reconcile GAAP and adjusted earnings to compensation, restructuring,
   acquisition/integration, impairment, legal/remediation, SBC, tax, and cash.
6. Treat product migration, technology, distribution, and recurring talent spend
   as owner-cash requirements when they recur.
7. Compare dividends and repurchases with fee-paying cash, debt, product
   investment, acquisition spending, and diluted shares.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what fee-paying AUM, flow breadth,
fee rate, product mix, operating margin, alternatives realization, and cost of
capital the equity price requires. The Lyn Alden-style stress test asks whether
market declines, investor liquidity, retirement flows, rates, credit, private-
market marks, and distribution pressure can be absorbed while talent and client
service are retained.

## Promotion boundary

`public-asset-management-qualified; fee-paying-flow-and-cash-open; no-ranking`

Promotion requires same-period joins from product-level flows and average
fee-paying AUM to fee rates, revenue, recurring talent/distribution/technology
cost, alternatives cash economics, remediation, debt, and diluted common
residual. Headline AUM, adjusted earnings, market appreciation, performance
income, dividends, and repurchases remain diagnostic inputs.

## Sources

- [Franklin deep company page](../deep-company-pages/franklin-resources-inc.md)
- [Franklin company packet](../../extracted/financial/asset-management/franklin-resources-inc/company-packet.md)
- [Franklin source ledger](../../extracted/financial/asset-management/franklin-resources-inc/source-ledger.md)
