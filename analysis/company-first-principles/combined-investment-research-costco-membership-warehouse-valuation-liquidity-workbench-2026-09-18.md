# Costco membership warehouse valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Costco from membership-retail evidence into a
company-specific valuation object. It separates merchandise sales, membership
fees, warehouse traffic, digitally enabled sales, gasoline, pharmacy, private
label, inventory, supplier terms, real estate, labor, international operations,
debt, capital returns, and diluted common residual. It does not treat sales,
comparable sales, membership counts, membership fees, operating cash flow, free
cash flow, or repurchases as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Costco | Membership-funded warehouse cash after member and merchandise collection, supplier settlement, inventory turns, warehouse and digital fulfillment, gasoline and pharmacy economics, real estate, labor, debt, and dilution | Warehouse openings and maintenance, distribution, inventory, private label, eCommerce and technology, fuel and pharmacy infrastructure, labor, international expansion, and SBC replacement | Membership renewal slowdown, value proposition erosion, consumer trade-down, supplier pressure, labor or real-estate cost, inventory or shrink, digital fulfillment burden, debt refinancing, or dilution | Sales and membership fees grow while renewal, traffic, margin, inventory turns, supplier terms, warehouse productivity, required capex, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2025 net sales were `$269.9B`, total revenue `$275.235B`, membership fees
  `$5.323B`, net income `$8.099B`, and diluted EPS `$18.21`.
- Q3 2026 net sales were `$69.15B`, digitally enabled comparable sales grew
  `21.5%`, net income was `$2.19B`, and quarter-end cash was `$18.946B`.
- Costco operated `923` warehouses at Q1 2026 quarter-end; digitally enabled
  comparable sales grew `20.5%` in Q1 and `22.6%` in Q2.
- The model depends on a loop among perceived value, warehouse volume,
  membership renewal, supplier terms, private label, and convenience; each
  requires separate collection, reinvestment, and resilience testing.

## QoE and financial-shenanigans prompts

1. Reconcile warehouse and digital sales to traffic, basket, renewal, member
   cohorts, returns, shrink, inventory turns, supplier terms, and cash.
2. Separate membership fees from merchandise margin and test whether renewal,
   household penetration, and value perception support durable fee economics.
3. Connect digital growth to picking, delivery, fulfillment, returns, and
   technology costs rather than treating digitally enabled sales as equivalent
   to warehouse contribution.
4. Keep gasoline, pharmacy, private label, currency, and special dividends or
   capital returns separate from the recurring warehouse cash engine.
5. Treat dividends, special distributions, and buybacks as residual claims only
   after warehouse, inventory, supplier, labor, real-estate, and debt needs are funded.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what renewal, traffic, basket growth,
membership-fee rate, merchandise margin, digital contribution, warehouse
productivity, reinvestment rate, and cost of capital the valuation requires. The
Lyn Alden-style stress test asks whether household budgets, food and fuel costs,
supplier terms, labor, rates, real estate, and inventory remain liquid through a
value-retail shock without confusing member scale or fees with durable owner cash.

## Promotion boundary

`costco-qualified; membership-warehouse-cash-open; no-ranking`

Promotion requires same-entity joins from member and merchandise activity to
collection, renewal, supplier settlement, inventory, warehouse and digital
reinvestment, fuel and pharmacy economics, debt, claims, and diluted common
residual. Sales, comparable sales, membership fees, OCF, FCF, and repurchases
remain diagnostic inputs.

## Sources

- [Costco company packet](../../extracted/services/discount-variety-stores/costco-wholesale-corp/company-packet.md)
- [Costco source ledger](../../extracted/services/discount-variety-stores/costco-wholesale-corp/source-ledger.md)
