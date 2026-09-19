# Holding-company subsidiary cash valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench adds Loews as a distinct diversified holding-company and
capital-allocation lane. It separates CNA insurance, Boardwalk pipeline,
Loews Hotels, and Altium Packaging cash from parent liquidity, subsidiary
capital restrictions, holding-company discount, taxes, debt, and repurchases.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Loews | Sum-of-the-parts common value after subsidiary underwriting/claims capital, pipeline maintenance/debt, hotel renovation, packaging working capital, parent overhead/tax, trapped cash, minority claims, and diluted common residual | CNA reserves/investments/statutory capital, Boardwalk maintenance/growth capital, hotel property renewal, packaging plants/inventory, subsidiary acquisitions, parent liquidity, debt, and common capital | CNA catastrophe/reserve or capital stress, pipeline volume/regulation, hotel demand/labor/renovation, packaging input/volume, trapped cash, refinancing, tax, or allocation failure | Consolidated earnings, subsidiary EBITDA, dividends, book value, and repurchases rise while subsidiary capital, parent remittance, maintenance cash, debt, taxes, or look-through per-share value deteriorate |

## Current evidence anchors

- FY2025 net income attributable to Loews was approximately `$1.7B` or `$7.97` per diluted share; Q2 2026 net income was approximately `$444M`; six-month 2026 net income was approximately `$781M` or `$3.79` per share.
- Major subsidiaries are CNA Financial, Boardwalk Pipelines, Loews Hotels, and Altium Packaging; their economics and capital restrictions are not interchangeable.
- CNA requires reserve, catastrophe, reinsurance, investment, and regulatory-capital testing before earnings can be treated as parent cash.
- Boardwalk requires throughput, contract/customer, maintenance-capital, debt, and cash-remittance testing; hotel cash requires occupancy, ADR/RevPAR, labor, insurance, renovation, and property-capital testing.
- Altium requires price/volume, resin/input pass-through, inventory, plant maintenance, customer concentration, debt, and cash-remittance testing.

## QoE and financial-shenanigans prompts

1. Build subsidiary-level bridges from revenue and earnings to maintenance cash,
   debt/claims, required capital, dividends, and cash available to Loews.
2. Keep CNA reserve development, catastrophe, reinsurance, investment income,
   and statutory capital separate from ordinary parent cash.
3. Charge Boardwalk maintenance capital, debt service, regulation, outages,
   customer credit, and cash trapped at the subsidiary.
4. Separate hotel renovation, labor, insurance, and property cash from
   packaging inventory, input costs, plant capacity, and industrial volume.
5. Value repurchases against look-through value after parent overhead, taxes,
   subsidiary claims, debt, minority interests, and trapped cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test values CNA, Boardwalk, hotels, packaging,
parent cash/debt, taxes, minority claims, and the holding-company discount
separately. The Lyn Alden-style stress test asks whether insurance losses,
pipeline regulation, hotel demand, packaging inputs, rates, and subsidiary
capital needs can weaken parent liquidity together.

## Promotion boundary

`holding-company-qualified; subsidiary-remittance-and-SOTP-open; no-ranking`

Promotion requires same-entity, same-period joins from each subsidiary to
maintenance capital, claims/reserves, debt, required capital, cash remitted to
the parent, parent overhead/tax, repurchases, and diluted common residual.
Consolidated net income, subsidiary EBITDA, dividends, book value, reported
OCF, and buybacks remain diagnostic inputs rather than normalized owner cash.

## Sources

- [Loews company page](../deep-company-pages/loews-corporation.md)
- [Loews source ledger](../../extracted/financial/conglomerates/loews-corporation/source-ledger.md)
- [Loews company packet](../../extracted/financial/conglomerates/loews-corporation/company-packet.md)

