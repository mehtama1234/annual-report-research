# CRH connected infrastructure materials valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves CRH from current-period evidence into a company-specific valuation object. It tests a diversified infrastructure-materials allocator spanning aggregates, roads, water, utility products, building solutions, and acquisitions. It keeps pricing, portfolio churn, Arcosa funding, residential weakness, capex, debt, and diluted common residual separate from reported EBITDA and guidance.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| CRH | Connected infrastructure-materials cash after local pricing, materials volume, water and utility products, acquisitions, divestitures, taxes, debt, and dilution | Quarries and plants, road and water systems, acquisitions, integration, working capital, environmental obligations, debt, and shares | Residential weakness, cost inflation, freight, acquisition leverage, Arcosa funding, divestiture noise, or public-project timing | EBITDA and margin rise while organic volume, price realization, acquired-asset returns, net debt, cash conversion, or diluted common residual deteriorate |

## Current evidence anchors

- 2025 revenue was `$37.4B`, net income was `$3.8B`, adjusted EBITDA was `$7.7B`, and adjusted EBITDA margin was `20.5%`.
- CRH deployed `$5.8B` in value-accretive growth investments in 2025 while returning `$2.2B` through dividends and buybacks.
- Q2 2026 revenue rose `6%` to `$10.8B`, net income rose `13%` to `$1.5B`, and adjusted EBITDA rose `7%` to `$2.6B`; aggregates pricing rose `5%` and asphalt pricing rose `6%` in cited Americas categories.
- At 2026-06-30, net debt was `$15.4B`; CRH expected approximately `$8.75B` of additional debt for the `$8.5B` Arcosa acquisition.
- The portfolio spans Americas Materials Solutions, Americas Building Solutions, International Solutions, Axius Water, roads, utility infrastructure, data-center and industrial projects, and outdoor living.

## QoE and financial-shenanigans prompts

1. Separate organic price, volume, mix, acquisitions, divestitures, and foreign exchange before treating margin expansion as recurring.
2. Reconcile acquisition returns and integration costs, particularly Arcosa, against incremental debt and promised synergies.
3. Test whether pricing stays ahead of freight, labor, energy, input, and financing costs while residential demand remains soft.
4. Reconcile operating cash flow to working capital, tax payments, capex, environmental obligations, dividends, buybacks, debt, and dilution.

## Damodaran/Lyn Alden application

The expectation test asks what pricing, volume, portfolio mix, acquisition returns, margin, capex, leverage, and cost of capital are embedded in the valuation. The stress test asks whether infrastructure, water, utility, industrial, and data-center demand can offset housing weakness while higher rates, debt-funded deals, freight, inflation, and public-budget timing pressure liquidity.

## Promotion boundary

`crh-qualified; connected-infrastructure-price-and-acquisition-return-open; no-ranking`

Promotion requires same-entity joins from materials and infrastructure products to collection, price/volume, maintenance and growth capital, acquisition return, claims, debt funding, and diluted common residual. Revenue, EBITDA, OCF, FCF, guidance, dividends, and acquisition proceeds remain diagnostic inputs.

## Sources

- [CRH company packet](../../extracted/basic-materials/general-building-materials/crh-plc/company-packet.md)
- [CRH source ledger](../../extracted/basic-materials/general-building-materials/crh-plc/source-ledger.md)
