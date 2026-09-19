# Networking-control valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench moves Arista Networks and Ciena from network-demand evidence into
company-specific valuation objects, reinvestment burdens, funding stresses, and
thesis breakers. It keeps data-center Ethernet control separate from optical
transport and carrier/cloud backlog economics.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment/denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Arista Networks | AI-fabric and cloud-network control cash after deferred-revenue normalization, working capital, manufacturing commitments, software support, SBC, customer concentration, and dilution | Switching/routing R&D, outsourced supply chain, inventory, warranty, deferred revenue, SBC replacement, acquisitions, and diluted shares | Hyperscaler capex pause, architecture change, customer concentration, deferred-revenue reversal, inventory/receivable build, margin mix, or supplier constraints | Revenue and margins rise while deferred revenue reverses, customer concentration worsens, CloudVision/EOS control weakens, or per-share cash fails after SBC and dilution |
| Ciena | Optical-transport and network-automation cash after backlog conversion, inventory quality, customer acceptance, receivables, acquisitions, SBC, debt, and dilution | Optical/R&D platform, production and component commitments, inventory, warranty, backlog fulfillment, Nubis integration, SBC, and repurchases | Carrier/cloud spending slowdown, order cancellation or modification, inventory obsolescence, acceptance delay, receivable funding, refinancing, or supply bottleneck | Orders/backlog rise while shipments, collections, gross margin, inventory quality, or diluted common residual deteriorate |

## Current evidence anchors

- Arista FY2025 revenue was `$9.006B`, operating cash flow `$4.372B`, and
  property/equipment/intangible purchases `$119.5M`; the `$2.452B` deferred-
  revenue increase supported cash while receivables, inventory, and other assets
  consumed cash. Deferred revenue is real cash but creates future service-
  delivery obligations.
- Ciena FY2025 revenue was `$4.77B`, orders `$7.8B`, and year-end backlog
  `$5.0B` versus `$2.1B` a year earlier. FY2025 operating cash flow was
  `$806.1M`, capital purchases `$140.8M`, and Nubis acquisition cash `$231.1M`;
  the first nine months of FY2026 used `$410.4M` in operating assets and
  liabilities, including `$251.5M` from receivables and `$118.3M` from
  inventory, with `$72.4M` of inventory-obsolescence provision.

## QoE and financial-shenanigans prompts

1. Reconcile Arista deferred revenue to recognized revenue, service obligations,
   customer concentration, receivables, inventory, and future gross profit.
2. Keep Arista SBC and customer prepayments visible when testing cash per
   diluted share; high margins do not by themselves establish owner cash.
3. Reconcile Ciena's order-to-cash chain: orders, backlog, production, shipment,
   acceptance, receivable collection, and cash. Backlog is not cash and may be
   modified or cancelled.
4. Test Ciena inventory reserves, component commitments, warranty, factoring or
   payment-term changes, acquisition cash, SBC, convertible debt, and buybacks
   before treating free cash flow as residual common-owner cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what AI-fabric adoption, ports and
mix, optical capacity, backlog conversion, margin, reinvestment, and cost of
capital the equity value requires. The Lyn Alden-style stress test asks whether
customer capex cycles, supplier commitments, inventory, receivables, rates,
debt, and dilution can absorb a demand pause before the control point produces
collectible owner cash.

## Promotion boundary

`networking-control-qualified; backlog-and-deferred-revenue-open; no-ranking`

Promotion requires same-entity, same-period joins from network deployment or
backlog through shipment/acceptance, collection, required reinvestment, claims,
funding, legal-entity availability, and diluted common residual. Revenue,
orders, backlog, deferred revenue, reported OCF, and buybacks remain diagnostic
inputs rather than normalized owner cash.

## Sources

- [Arista deep company packet](../deep-company-pages/arista-networks-inc.md)
- [Ciena deep company packet](../deep-company-pages/ciena-corporation.md)
- [Arista versus Ciena network-control forensic comparison](../cross-sector/arista-versus-ciena-network-control-forensic-comparison-2026-09-14.md)
