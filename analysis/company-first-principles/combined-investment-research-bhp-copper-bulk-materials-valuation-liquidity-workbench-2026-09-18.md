# BHP copper and bulk-materials portfolio valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves BHP Group from diversified-miner evidence into a
company-specific valuation object. It separates copper, iron ore, potash, and
portfolio-recycling economics, then tests mine throughput, realized prices,
unit costs, mine life, development pathways, royalties and streams, permitting,
capital intensity, host-country exposure, debt, dividends, and diluted common
residual. It does not treat production, EBITDA, operating cash flow, free cash
flow, dividends, or divestiture proceeds as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| BHP | Copper-and-bulk-materials cash after realized prices, throughput, grades, recoveries, unit costs, royalties, sustaining and growth capex, mine-life extension, portfolio recycling, debt, and dilution | Mine replacement and development, processing and rail/port systems, exploration, tailings and closure, potash buildout, decarbonization, royalties, working capital, and SBC replacement | Copper or iron-ore price shock, grade or throughput failure, diesel and consumables inflation, permitting or host-country risk, potash delay, tailings event, debt refinancing, FX, or dilution | Production and copper share grow while realized prices, unit costs, recovery, sustaining capex, project returns, portfolio proceeds, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2025 annual materials highlighted record copper production of `2 Mt`,
  profit from operations of `$19.5B`, economic contribution of `$46.8B`, and
  payments to governments of `$10.4B`.
- FY2026 year-end review reported another year around `2 Mt` of copper and
  record iron-ore production, with copper prices about `35%` higher year over
  year and every asset within unit-cost guidance.
- FY2026 half-year operating cash flow was `$9.4B`, net debt `$14.7B`, and
  copper contributed `51%` of Underlying EBITDA; copper guidance was raised to
  `1.9–2.0 Mt`.
- Antamina silver streaming, Carajas, Blackwater, and Daunia transactions
  produced about `$4.8B` of realized portfolio proceeds; those proceeds are
  capital-recycling evidence, not recurring mine cash.

## QoE and financial-shenanigans prompts

1. Reconcile production to grades, recoveries, throughput, realized prices,
   treatment charges, royalties, unit costs, inventory, and customer collection.
2. Separate copper growth from iron-ore cash and potash optionality; test
   whether portfolio mix changes actually improve return on invested capital.
3. Keep divestiture proceeds, streaming transactions, asset-sale gains, and
   guidance separate from recurring operating cash.
4. Connect each development pathway to permitting, sustaining and growth capex,
   host-country terms, construction, closure, tailings, and environmental costs.
5. Treat dividends and buybacks as residual claims only after mine replacement,
   debt, safety, closure, development, and working-capital obligations are funded.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what copper and iron-ore prices,
production, grades, unit costs, mine life, potash ramp, reinvestment rate, and
cost of capital the valuation requires. The Lyn Alden-style stress test asks
whether electrification demand, China, diesel, rates, permitting, resource
nationalism, host-country claims, and project funding remain liquid through a
commodity shock without confusing production or divestiture proceeds with owner cash.

## Promotion boundary

`bhp-qualified; copper-and-bulk-portfolio-cash-open; no-ranking`

Promotion requires same-entity joins from each commodity to collection,
production and recovery, unit costs, sustaining and growth capex, permitting,
portfolio proceeds, debt, claims, and diluted common residual. Production,
EBITDA, OCF, FCF, dividends, and divestiture proceeds remain diagnostic inputs.

## Sources

- [BHP company packet](../../extracted/basic-materials/industrial-metals-minerals/bhp-group-plc/company-packet.md)
- [BHP source ledger](../../extracted/basic-materials/industrial-metals-minerals/bhp-group-plc/source-ledger.md)
