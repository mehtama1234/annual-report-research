# Nutrien agricultural-inputs and crop-cycle valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Nutrien from an agricultural-chemicals packet into a company-specific valuation object. It separates upstream potash and nitrogen production from retail agronomy and distribution, then tests crop-cycle demand, fertilizer prices, natural-gas exposure, mine and plant reliability, inventory, grower credit, portfolio simplification, debt, and diluted common residual. It does not treat fertilizer tonnage, adjusted EBITDA, free cash flow, divestiture proceeds, dividends, or repurchases as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Nutrien | Crop-cycle cash after potash mines, nitrogen and phosphate facilities, retail locations, agronomy, proprietary products, logistics, grower financing, sustaining and expansion capex, environmental obligations, debt, and dilution | Mine automation and sustaining capital, plant turnarounds, natural gas, inventory, receivables and grower credit, retail locations, agronomy, logistics, portfolio exits, R&D, and repurchases | Fertilizer-price collapse, acreage or crop-margin pressure, natural-gas shock, trade restrictions, mine or plant outage, grower-credit deterioration, divestiture execution, debt refinancing, or dilution | Potash volume and retail EBITDA remain strong while price realization, retail working capital, plant reliability, required capex, or diluted per-share cash deteriorate |

## Current evidence anchors

- Nutrien operates more than `1,800` retail locations, more than `4,200` crop consultants, more than `600,000` customer accounts, `6` potash mines, `12` nitrogen facilities, and `6` phosphate facilities.
- FY2025 net earnings were about `$2.30B` and adjusted EBITDA about `$6.05B`; Retail adjusted EBITDA was about `$1.74B`, Potash `$2.25B`, Nitrogen `$2.15B`, and Phosphate `$382M`.
- Q2 2026 net earnings were about `$1.22B`, diluted EPS `$2.53`, adjusted EBITDA `$2.43B`; first-half Retail adjusted EBITDA was `$1.24B`, Potash `$1.24B`, and Nitrogen `$1.12B`.
- Nutrien reported approximately `$848M` of shareholder returns in the first half of 2026 and raised potash volume guidance while lowering capital-expenditure guidance; those are capital-allocation inputs, not proof of surplus owner cash.
- Portfolio simplification includes strategic alternatives for phosphate, the Trinidad nitrogen facility, and Brazilian retail; proceeds, stranded costs, taxes, and reinvestment consequences must remain explicit.

## QoE and financial-shenanigans prompts

1. Split potash, nitrogen, phosphate, and retail cash by same-entity period; do not let a high fertilizer-price quarter conceal mine depletion, plant maintenance, or retail working-capital needs.
2. Reconcile tons, realized prices, natural-gas and other input costs, freight, inventory, customer receivables, grower financing, and cash collections.
3. Test retail proprietary-product margins and agronomy relationships for repeatability, customer credit quality, and required location and logistics investment.
4. Keep mine automation, turnarounds, environmental obligations, divestiture proceeds, restructuring, and strategic alternatives separate from maintenance capex and normalized free cash flow.
5. Reconcile adjusted EBITDA, dividends, repurchases, debt, foreign exchange, and diluted shares before accepting capital returns as common-owner cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what potash and nitrogen prices, volumes, retail margin, crop-cycle retention, reinvestment rate, asset life, and cost of capital the valuation requires. The Lyn Alden-style stress test asks whether farmers can fund inputs through a weak crop-margin period, whether gas and logistics consume the spread, and whether geopolitics, trade policy, outages, debt, or portfolio exits impair liquidity before the structural agricultural platform earns its cost of capital.

## Promotion boundary

`nutrien-agricultural-inputs-qualified; crop-cycle-and-owner-cash-open; no-ranking`

Promotion requires same-entity joins from production and retail sale to customer collection, input-cost settlement, sustaining capex, mine and plant reliability, grower-credit performance, environmental claims, funding, and diluted common residual. Production, fertilizer prices, adjusted EBITDA, guidance, dividends, repurchases, and divestiture proceeds remain diagnostic inputs.

## Sources

- [Nutrien company packet](../../extracted/basic-materials/agricultural-chemicals/nutrien/company-packet.md)
- [Nutrien source ledger](../../extracted/basic-materials/agricultural-chemicals/nutrien/source-ledger.md)

