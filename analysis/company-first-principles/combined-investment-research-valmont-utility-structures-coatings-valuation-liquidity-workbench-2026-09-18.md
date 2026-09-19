# Valmont utility structures, coatings, and irrigation valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Valmont from an industrial-conglomerate packet into a company-specific valuation object. It separates utility structures and coatings from telecommunications, irrigation, agriculture, water, and portfolio exits, then tests backlog conversion, steel and tariff exposure, capacity investment, working capital, ConcealFab integration, legal claims, debt, and diluted common residual. It does not treat backlog, infrastructure demand, adjusted operating income, guidance, operating cash flow, or buybacks as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Valmont | Physical infrastructure and agricultural-productivity cash after utility structures, coatings, telecom hardware, irrigation, water systems, steel inputs, capacity, portfolio exits, claims, debt, and dilution | Pole and structure capacity, coatings plants, steel and inventory, customer deposits and receivables, irrigation and aftermarket, ConcealFab integration, maintenance/growth capex, environmental/legal claims, and repurchases | Utility capex slowdown, carrier spending weakness, farm-cycle pressure, steel/tariff shock, Brazil or Middle East disruption, portfolio-exit costs, acquisition integration, debt refinancing, or dilution | Utility backlog and coatings growth continue while telecom/irrigation mix, price-cost, inventory, required capacity, claims, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2025 net sales were about `$4.10B`, adjusted operating income about `$537.9M`, diluted EPS `$16.79`, and operating cash flow about `$456.5M`.
- FY2025 backlog increased by about `$217.0M` or `15.1%` to approximately `$1.65B`, driven primarily by utility demand.
- Q2 2026 net sales increased `6.5%` to about `$1.12B`, operating income was about `$166.1M`, diluted EPS `$6.14`, and operating cash flow `$148.1M`.
- Q2 North America Coatings sales increased `16.6%` on infrastructure and data-center-related volumes, while North America Telecommunications sales decreased `26.1%` with lower carrier spending.
- Valmont exited solar, wound down Prospera, and deployed about `$72.9M` in Q4 2025 to acquire the remaining ConcealFab interest; portfolio shape and acquired return therefore remain explicit cash questions.

## QoE and financial-shenanigans prompts

1. Split utility, coatings, telecommunications, agriculture, irrigation, and water economics by same-entity period; do not flatten divergent demand into one infrastructure growth rate.
2. Reconcile backlog, orders, customer acceptance, steel and zinc inputs, tariffs, price-cost, inventory, receivables, and cash collections before treating backlog as future cash.
3. Keep capacity investment, plant utilization, coatings quality, pole sourcing, ConcealFab integration, Prospera wind-down, and solar exit costs separate from maintenance capex.
4. Test utility and data-center-linked demand against carrier spending, farm economics, grain prices, trade policy, Brazil, and Middle East exposure.
5. Reconcile adjusted operating income, OCF, guidance, legal charges, debt, dividends, repurchases, SBC, and diluted shares before accepting per-share cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what utility backlog conversion, coatings volume, price-cost, capacity return, telecom recovery, agricultural margin, reinvestment rate, and cost of capital the valuation requires. The Lyn Alden-style stress test asks whether grids and farms can fund physical investment through rate, commodity, tariff, and geopolitical shocks, and whether steel inputs, inventory, claims, portfolio exits, or debt consume liquidity before infrastructure demand reaches common owners.

## Promotion boundary

`valmont-physical-infrastructure-qualified; utility-backlog-and-mix-open; no-ranking`

Promotion requires same-entity joins from backlog and products to customer acceptance, collections, steel and tariff settlement, capacity utilization, required capex, portfolio and acquisition return, claims, funding, and diluted common residual. Backlog, infrastructure demand, adjusted operating income, guidance, OCF, and buybacks remain diagnostic inputs.

## Sources

- [Valmont company packet](../../extracted/industrial-goods/conglomerates/valmont-industries-inc/company-packet.md)
- [Valmont source ledger](../../extracted/industrial-goods/conglomerates/valmont-industries-inc/source-ledger.md)

