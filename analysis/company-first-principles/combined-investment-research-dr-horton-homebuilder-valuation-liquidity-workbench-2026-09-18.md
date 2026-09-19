# D.R. Horton homebuilder and housing-finance valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves D.R. Horton from a residential-construction packet into a company-specific valuation object. It separates home closings, orders, cancellations, incentives, land and lot control, construction-cycle cash, rental operations, Forestar, mortgage and title activity, inventory, debt, and diluted common residual. It does not treat order value, homes closed, revenue, adjusted earnings, operating cash flow, or repurchases as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| D.R. Horton | Homebuilding cash after land and lot acquisition, construction, completed-home inventory, incentives, customer deposits, mortgage/title capture, rental and Forestar exposure, debt, claims, and dilution | Land and lot commitments, construction costs, inventory turns, community development, subcontractors, mortgage/title infrastructure, Forestar capital, warranty, debt, and repurchases | Mortgage-rate and affordability shock, cancellation rise, unsold completed homes, land impairment, subcontractor or material inflation, regional concentration, debt refinancing, or dilution | Closings and order value rise while incentives, cancellations, inventory days, lot commitments, mortgage capture, operating cash, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2025 revenue was about `$34.3B`, net income attributable to D.R. Horton about `$3.6B`, diluted EPS `$11.57`, and cash provided by operations about `$3.4B`.
- D.R. Horton closed `84,863` homes in FY2025 at an average closing price of about `$370,400`, operated in `126` markets across `36` states, and also had rental, Forestar, mortgage, and title activities.
- Q3 2026 revenue was about `$9.2B`, homebuilding revenue about `$8.7B`, homes closed `23,983` up `4%`, and net sales orders `23,084` homes with order value about `$8.4B`.
- Q3 2026 cancellation rates rose to `20%`; fiscal 2026 guidance was reduced to consolidated revenue of `$32.5B`–`$33.0B` and closings of `83,800`–`84,300`, while affordability and incentives remained central.
- Q2 2026 reduced unsold completed homes by `35%` year over year and the company returned roughly `$1.0B` through dividends and repurchases; those actions must be reconciled against land, inventory, and customer-affordability cash needs.

## QoE and financial-shenanigans prompts

1. Reconcile orders, closings, cancellations, incentives, average selling price, customer deposits, backlog, and collections; order value is not a delivered-home receivable.
2. Test land and lot commitments, owned versus controlled lots, construction-in-process, completed-home inventory, impairments, and inventory turns against operating cash.
3. Separate mortgage and title economics, Forestar, rental operations, and homebuilding cash; consolidated earnings can conceal different funding and risk perimeters.
4. Treat affordability pressure and incentives as operating economics, not merely macro commentary; a closing maintained through incentives may weaken per-home owner cash.
5. Reconcile warranty claims, subcontractor and material costs, debt, dividends, repurchases, SBC, and diluted shares before accepting EPS or capital returns as owner cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what closing volume, price, incentive rate, land turns, construction margin, capital intensity, and cost of capital the valuation requires. The Lyn Alden-style stress test asks whether households can fund homes through higher rates and weak affordability, whether inventory and land commitments trap cash, and whether debt, regional concentration, or financial-services exposure amplifies a housing downturn.

## Promotion boundary

`dr-horton-homebuilder-qualified; affordability-and-inventory-open; no-ranking`

Promotion requires same-entity joins from orders and closings to customer collections, incentives, construction delivery, land and lot obligations, inventory turns, mortgage/title settlement, warranty claims, debt, funding, and diluted common residual. Orders, backlog, closing volume, revenue, EPS, operating cash flow, and repurchases remain diagnostic inputs.

## Sources

- [D.R. Horton company packet](../../extracted/industrial-goods/residential-construction/d-r-horton-inc/company-packet.md)
- [D.R. Horton source ledger](../../extracted/industrial-goods/residential-construction/d-r-horton-inc/source-ledger.md)

