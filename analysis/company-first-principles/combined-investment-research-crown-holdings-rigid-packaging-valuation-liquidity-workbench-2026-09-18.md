# Crown Holdings rigid packaging valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Crown Holdings from current-period packaging evidence into a
company-specific valuation, plant-network, commodity-pass-through, leverage, and
common-owner cash test. It does not pool beverage cans, food cans, closures,
aerosol, equipment, and paper or aluminum packaging into a generic container
multiple.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Crown Holdings | Collected rigid-packaging cash after aluminum and steel inputs, energy, freight, plant utilization, customer pass-through, maintenance/growth capex, debt, buybacks, and dilution | Can and closure lines, beverage-capacity expansion, plant conversions, tooling/equipment, maintenance, working capital, and geographic network investment | Metal or energy inflation, volume decline, customer concentration, plant disruption, FX, freight, leverage, refinancing, or failed capacity returns | Beverage volumes and adjusted EBITDA rise while utilization, pass-through, capex returns, leverage, FCF, or diluted common residual deteriorate |

## Current evidence anchors

- Full-year 2025 net sales were `$12.365B`, income from operations `$1.553B`, adjusted EBITDA `$2.092B`, net debt about `$5.2B`, and adjusted net leverage `2.5x`.
- Q2 2026 net sales were `$3.668B`, income from operations `$464M`, segment income `$501M`, net income attributable to Crown `$245M`, and adjusted diluted EPS `$2.49`.
- Global beverage-can volumes increased `5%` in Q2 2026; full-year adjusted diluted EPS guidance was raised to `$8.30-$8.50`.
- Expected 2026 adjusted free cash flow remained at least `$900M` after approximately `$550M` of capex.
- Q2 2026 repurchases were `$305M`, and nearly `7%` of shares had been repurchased over the prior twelve months while leverage remained `2.5x`.

## QoE and financial-shenanigans prompts

1. Reconcile can and packaging volume to price, metal pass-through, mix, plant
   utilization, customer contracts, energy, freight, and cash collections.
2. Separate beverage, food, aerosol, closures, tooling, transit, and equipment
   economics; strong beverage volume does not validate every segment's returns.
3. Keep maintenance and growth capex, plant conversions, capacity projects,
   working capital, energy and sourcing obligations, debt service, and buybacks
   in the owner-cash denominator.
4. Test whether adjusted EBITDA and adjusted FCF exclude recurring plant,
   restructuring, currency, environmental, litigation, or integration burdens.
5. Reconcile net debt, leverage, interest, pension or other claims, repurchases,
   SBC, taxes, and diluted shares before treating capital returns as surplus cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what beverage volume, utilization,
pass-through, margin, capacity returns, capex rate, leverage, and cost of capital
the valuation requires. The Lyn Alden-style stress test asks whether aluminum and
steel, energy, freight, FX, global sourcing, customer budgets, and refinancing can
be absorbed without weakening liquidity or the common residual.

## Promotion boundary

`crown-holdings-rigid-packaging-qualified; throughput-capex-and-owner-cash-open; no-ranking`

Promotion requires same-entity, same-period joins from packaging throughput and
pricing to customer collections, input pass-through, plant utilization, required
capex, debt service, claims, repurchases, and diluted common residual. Volume,
adjusted EBITDA, adjusted EPS, adjusted FCF, guidance, and buybacks remain
diagnostic inputs.

## Sources

- [Crown Holdings company packet](../../extracted/consumer-goods/packaging-containers/crown-holdings/company-packet.md)
- [Crown Holdings source ledger](../../extracted/consumer-goods/packaging-containers/crown-holdings/source-ledger.md)

