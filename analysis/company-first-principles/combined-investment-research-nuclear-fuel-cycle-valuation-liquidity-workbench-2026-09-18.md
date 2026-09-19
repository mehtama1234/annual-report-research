# Nuclear-fuel-cycle valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench adds Cameco as a distinct nuclear-fuel-cycle lane. It separates
uranium mining, procurement and inventory, Fuel Services conversion, and the
Westinghouse equity stake from merchant power, generic mining, oil and gas, and
materials-cycle economics.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Cameco | Nuclear-fuel cash after realized contract pricing, mine production, sustaining capital, procurement, inventory replacement, conversion, JV/Westinghouse claims, reclamation, debt, and diluted common residual | Mine development and sustaining capital, conversion facilities, inventory, receivables, Fuel Services maintenance, Westinghouse equity funding, reclamation, joint ventures, and common capital | Uranium-price/contract mismatch, production shortfall, inventory absorption, permitting/reclamation, Westinghouse project execution, sanctions/export controls, reactor delays, or JV funding | Deliveries, realized price, OCF, equity-method earnings, and inventory gains rise while mine return, replacement cost, JV distributions, reclamation, or diluted residual deteriorate |

## Current evidence anchors

- FY2025 revenue was approximately `CAD $3.482B`; uranium contributed about `CAD $2.874B`; profit attributable to owners was `CAD $590M`; OCF was `CAD $1.408B`; productive-asset spending was `CAD $333M`; and the screen after productive-asset spending was `CAD $1.075B`.
- FY2025 uranium production was `21.0M` pounds versus `33.0M` pounds delivered; ending uranium inventory was `9.7M` pounds at an average cost of `$61.85` per pound.
- Cameco reported roughly `230M` pounds of long-term delivery commitments after 2025, with average annual deliveries of about `28M` pounds over the following five years.
- Fuel Services produced `14.0M` kgU in 2025. Westinghouse makes earnings and cash attribution less transparent because equity-method profit, distributions, project margins, and required investment can occur in different periods.
- Cash and cash equivalents were about `CAD $1.115B`; debt was approximately `CAD $1.0B`; dividends paid were `CAD $104M`.

## QoE and financial-shenanigans prompts

1. Reconcile profit to OCF through equity-method earnings, contract timing,
   inventory purchases/releases, receivables, taxes, and working capital.
2. Separate uranium production from deliveries and procurement; delivery volume
   can exceed mine output while creating replacement-cost exposure.
3. Split sustaining from expansion capital and test grades, recovery, mine
   life, permitting, labor, processing, and reclamation.
4. Reconcile Westinghouse share of earnings to distributions, project margins,
   guarantees, construction claims, working capital, and required investment.
5. Test long-term contracts for fixed/escalated/market-linked pricing, floors,
   ceilings, volume flexibility, penalties, customer credit, and replacement
   procurement.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test values uranium mining, Fuel Services,
inventory/contracting, and Westinghouse independently using mid-cycle pricing,
sustaining capital, project timing, probability of completion, and Cameco's
share of cash. The Lyn Alden-style stress test asks whether strategic nuclear
fuel demand survives policy shifts, sanctions, export controls, reactor delays,
high financing costs, and inventory funding without weakening liquidity.

## Promotion boundary

`nuclear-fuel-cycle-qualified; delivery-inventory-jv-return-open; no-ranking`

Promotion requires same-entity, same-period joins from contract deliveries and
mine/Fuel Services output to customer receipts, inventory replacement,
sustaining capital, reclamation, Westinghouse distributions and funding, debt,
and diluted common residual. Production, deliveries, realized price, OCF,
equity-method profit, inventory gains, and dividends remain diagnostic inputs
rather than normalized owner cash.

## Sources

- [Cameco company page](../deep-company-pages/cameco-corporation.md)
- [Cameco company packet](../../extracted/basic-materials/uranium/cameco-corp/company-packet.md)

