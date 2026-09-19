# Foodservice distribution valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Sysco and US Foods from foodservice-demand evidence into
separate route-density and procurement valuation objects. It keeps distribution
cash distinct from healthcare pass-through distribution and branded consumer
staples.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment/denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Sysco | Foodservice route-density and procurement cash after inventory, vendor consideration, fleet, warehouse labor, fuel, receivables, acquisitions, debt, and dilution | Distribution centers, trucks, labor, inventory, private label, ordering technology, vendor rebates, acquisitions, and common capital | Restaurant/institutional demand, food-cost deflation, customer credit, supplier terms, receivable sales, fuel/labor, acquisition integration, or leverage | Sales and gross profit rise while case volume, realized rebates, route productivity, inventory/receivables, acquisition return, or diluted cash weaken |
| US Foods | Foodservice replenishment and ordering-workflow cash after inventory, vendor rebates, fleet/DC capex, customer credit, MOXē, debt, and dilution | Facilities, trucks, inventory, private label, sales/chef support, digital ordering, working capital, acquisitions, and common capital | Independent-restaurant failure, chain mix, food-cost inflation/deflation, vendor-rebate estimate, customer credit, debt/refinancing, or route disruption | Sales rise through food inflation while case volume, gross margin, vendor receipts, inventory, receivables, debt, or common residual deteriorate |

## Current evidence anchors

- Sysco FY2026 sales were `$84.6B`, operating cash flow `$2.638B`, net capex
  `$524M`, acquisitions `$189M`, and core residual after those uses about
  `$1.925B`; gross profit was approximately `$15.6B`.
- US Foods FY2025 sales were `$39.424B`, operating cash flow `$1.369B`, capex
  `$410M`, and reported FCF `$965M`; inventory was approximately `$1.711B`,
  accounts receivable `$2.026B`, vendor receivables `$173M`, and total debt
  `$5.2B`.
- US Foods FY2025 sales growth was `4.1%` while total case volume grew only
  `1.0%`; food-cost inflation contributed to nominal growth and vendor rebates
  remain a critical audit and cash-realization question.

## QoE and financial-shenanigans prompts

1. Separate cases/volume, food-cost inflation, price, mix, gross profit per case,
   vendor rebates, and realized cash receipts.
2. Reconcile inventory, accounts receivable, vendor receivables, accounts payable,
   LIFO/reserve effects, customer credit, and receivable sales or factoring.
3. Track route density, warehouse labor, fleet/fuel, facilities, private-label
   mix, customer retention, and acquisition integration.
4. Keep healthcare, hospitality, independent-restaurant, and chain customer
   credit and margin behavior separate.
5. Treat sales, gross profit, adjusted EBITDA, reported FCF, dividends, and
   buybacks as diagnostic or residual measures until route collection and
   renewal capital are joined.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what case growth, gross profit per
case, vendor funding, route productivity, working capital, acquisition return,
capex, debt cost, and cost of capital the valuation requires. The Lyn Alden-
style stress test asks whether restaurant and institutional budgets, food costs,
credit, labor, fuel, supplier terms, and rates can interrupt cash in a thin-
margin network.

## Promotion boundary

`foodservice-distribution-qualified; volume-rebate-credit-and-route-open; no-ranking`

Promotion requires same-entity, same-period joins from customer order through
inventory procurement, vendor settlement, delivery, collection, fleet/DC
renewal, customer-credit claims, debt, and diluted common residual. Sales,
cases, gross profit, vendor rebates, reported OCF, FCF, dividends, and buybacks
remain diagnostic inputs.

## Sources

- [Sysco deep company packet](../deep-company-pages/sysco-corp.md)
- [US Foods deep company packet](../deep-company-pages/us-foods-holding-corp.md)
