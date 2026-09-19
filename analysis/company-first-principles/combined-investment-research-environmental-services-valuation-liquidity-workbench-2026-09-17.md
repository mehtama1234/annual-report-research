# Environmental-services valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench routes Waste Management, Republic Services, Casella Waste
Systems, and Clean Harbors into separate valuation, reinvestment, liquidity,
and thesis-breaker objects. It keeps national route density, regional landfill
growth, specialized hazardous treatment, recycling, renewable energy, and
healthcare/environmental services distinct.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Waste Management | National collection/disposal and recycling/RNG/healthcare cash after fleet, landfill, sustainability, Stericycle integration, closure obligations, and debt | Trucks, transfer stations, landfills, recycling, RNG, healthcare facilities, permits, closure/post-closure, acquisitions, and dilution | Volume/price, fuel/labor, recycling prices, permitting, integration, sustainability project return, and debt | Pricing and route density rise while volume, landfill obligations, integration cash, capital, or diluted residual deteriorate |
| Republic Services | National route-density and disposal/sustainability cash after landfills, special waste, acquisitions, projects, and debt | Collection fleet, transfer stations, landfills, recycling/polymer centers, sustainability projects, environmental claims, acquisitions, and dilution | Waste volume, permits, commodities, project completion, acquisition return, environmental liability, and refinancing | Pricing/acquisitions grow while disposal capacity, project cash, claims, capex, or diluted residual weakens |
| Casella Waste Systems | Regional route-density and landfill cash after acquisitions, facility buildout, closure obligations, working capital, and debt | Collection, transfer, recycling/organics, landfill development, fleet, acquisitions, surety, interest, and dilution | Regional volume, acquisition integration, landfill permits, capex, recycling prices, leverage, and liquidity | Revenue/EBITDA grow while cash after capex/acquisitions remains thin or environmental/debt claims rise |
| Clean Harbors | Specialized hazardous-waste treatment, industrial services, Safety-Kleen, and response cash after sustaining/growth capital, liabilities, and debt | Incinerators, treatment/disposal capacity, emergency response, used-oil re-refining, remediation, permits, closure, insurance, and dilution | Hazardous volumes, regulation, environmental claims, commodity prices, utilization, insurance, and adjusted-FCF exclusions | Adjusted FCF rises while strategic growth investment, environmental liabilities, utilization, or diluted residual deteriorates |

## Current evidence anchors

- Waste Management FY2025 OCF was `$6.043B`, capex `$3.227B`, acquisitions
  `$395M`, and company-defined FCF `$2.937B`; the strict post-capex/acquisition
  screen was about `$2.421B`.
- Republic FY2025 revenue was `$16.591B`, OCF `$4.296B`, capex about `$1.887B`,
  acquisitions about `$1.1B`, and strict post-capex/acquisition cash about
  `$1.31B`; the network included `377` collection operations, `255` transfer
  stations, `207` active landfills, and `79` recycling centers.
- Casella FY2025 revenue was about `$1.837B`, OCF `$329.8M`, PP&E additions
  `$245.0M`, acquisitions `$224.2M`, and adjusted FCF `$179.9M`; its simple
  post-PP&E/acquisition screen was approximately `$60.6M` before other claims.
- Clean Harbors FY2025 revenue was `$6.031B`, OCF `$866.7M`, PP&E additions
  `$424.9M`, and reported adjusted FCF `$509.3M`; the less-adjusted cash after
  property investment and asset-sale proceeds was about `$463.4M`.

## QoE and financial-shenanigans prompts

1. Separate collection, disposal, recycling, RNG, healthcare, special waste,
   hazardous treatment, re-refining, and remediation economics.
2. Charge fleet/facility replacement, landfill development, closure and
   post-closure, environmental claims, permits, labor, and debt before owner
   cash.
3. Reconcile acquisitions, sustainability projects, renewable credits, asset
   sales, strategic growth investments, and adjusted FCF exclusions.
4. Test route density and pricing against actual volume, customer retention,
   commodity prices, disposal utilization, and cash collection.
5. Keep national scale, regional growth, and specialized hazardous capacity
   separate; no pooled waste multiple or owner-cash screen.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what route density, price/yield,
disposal utilization, project return, sustaining capital, environmental cost,
and cost of capital the valuation requires. The Lyn Alden-style stress test
asks whether industrial activity, municipalities, fuel, labor, rates,
recycling commodities, permitting, insurance, and refinancing preserve cash.

## Promotion boundary

`environmental-services-qualified; route-capacity-liability-and-replacement-cash-open; no-ranking`

Promotion requires same-period collection, route/disposal utilization,
maintenance and growth capital, acquisition return, closure/environmental
claims, debt, and diluted common-owner residual. Revenue, route count, landfill
count, adjusted FCF, EBITDA, sustainability projects, and buybacks remain
diagnostic inputs.

## Sources

- [Waste Management deep-company memo](../deep-company-pages/waste-management-inc.md)
- [Republic Services deep-company memo](../deep-company-pages/republic-services-inc.md)
- [Casella deep-company memo](../deep-company-pages/casella-waste-systems-inc.md)
- [Clean Harbors deep-company memo](../deep-company-pages/clean-harbors-inc.md)
