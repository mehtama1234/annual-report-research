# Freight and logistics valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench routes C.H. Robinson and UPS as contrasting freight models:
asset-light brokerage/forwarding versus asset-heavy parcel and logistics
infrastructure. It keeps gross profit per shipment, route density, labor,
working capital, aircraft/vehicle/facility capital, acquisitions, and customer
concentration separate.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| C.H. Robinson | Gross-profit-per-shipment and brokerage/forwarding cash after carrier purchases, receivables, contract assets, technology, compensation, and dilution | Technology, broker workforce, carrier/customer systems, working capital, acquisitions, SBC, and debt | Freight cycle, carrier-price mismatch, receivable timing, customer concentration, credit, and rates | Revenue/shipments improve while gross profit per shipment, receivable conversion, carrier cost, or diluted residual deteriorates |
| UPS | Parcel-density and network cash after labor, vehicles, aircraft, hubs, automation, transformation, healthcare logistics, acquisitions, and debt | Fleet, aircraft, hubs, sorting automation, labor agreements, network reconstruction, healthcare compliance, acquisitions, and dilution | Package mix, Amazon/customer concentration, labor, fuel, trade, aircraft/vehicle cost, transformation, and refinancing | Revenue quality improves while package density, labor productivity, network capex, transformation cash, or diluted residual weakens |

## Current evidence anchors

- C.H. Robinson FY2025 revenue was `$16.233B`, operating income `$795.0M`, OCF
  `$914.5M`, capex `$70.5M`, acquisitions `$11.9M`, and core residual about
  `$832.1M`; OCF benefited from a `$95.4M` receivables release and `$44.3M`
  contract-asset release.
- UPS FY2025 revenue was `$88.7B`, OCF `$8.450B`, capex `$3.685B`, acquisitions
  `$1.968B`, and strict post-capex/acquisition residual about `$2.797B` versus
  company-defined FCF `$5.470B`.

## QoE and financial-shenanigans prompts

1. C.H. Robinson: use gross profit, shipments, carrier cost, receivables,
   contract assets, and collection rather than gross billed revenue.
2. UPS: separate parcel revenue, package mix, labor, transformation costs,
   network capex, disposal proceeds, acquisitions, and healthcare claims.
3. Test working-capital releases, customer/carrier concentration, fuel,
   surcharges, credits, and nonrecurring disposal or restructuring effects.
4. Carry technology, vehicles, aircraft, hubs, automation, labor, and debt as
   recurring reinvestment claims before owner cash.
5. Keep asset-light brokerage residuals separate from asset-heavy network cash;
   no pooled freight multiple.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what gross profit per shipment,
package density, pricing, labor productivity, network utilization,
reinvestment, and cost of capital the valuation requires. The Lyn Alden-style
stress test asks whether trade, fuel, labor, rates, customer liquidity,
e-commerce mix, and carrier capacity preserve cash through a freight reversal.

## Promotion boundary

`freight-logistics-qualified; shipment-density-and-network-reinvestment-open; no-ranking`

Promotion requires same-period shipper collection, carrier or labor settlement,
working-capital normalization, maintenance/growth capital, acquisition return,
debt, claims, SBC, and diluted common-owner residual. Revenue, shipment count,
package count, gross billed volume, adjusted FCF, and buybacks remain diagnostic
inputs.

## Sources

- [C.H. Robinson deep-company memo](../deep-company-pages/ch-robinson-worldwide-inc.md)
- [UPS deep-company memo](../deep-company-pages/united-parcel-service-inc.md)
