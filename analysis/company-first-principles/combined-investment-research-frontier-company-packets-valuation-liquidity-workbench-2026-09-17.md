# Frontier company-packet valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench routes four previously unintegrated annual-report company
packets into separate valuation, reinvestment, liquidity, and thesis-breaker
objects. It deliberately does not pool Host Hotels, F5, Veralto, or Caterpillar:
their denominators are physical lodging property, application-control software,
embedded water/product-quality measurement, and heavy-equipment installed-base
economics.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Host Hotels & Resorts | Property-level hotel cash after labor, insurance, interest, renewal capex, asset sales, OP-unit claims, and debt | Hotel renewal/replacement, renovations, property taxes, insurance, labor, acquisitions, interest, and diluted OP/common claims | RevPAR/occupancy, group/leisure demand, refinancing, insurance, labor, property values, and capex cycle | RevPAR and EBITDAre rise while property cash after renewal capex, interest, claims, or asset value deteriorates |
| F5 | Application-control cash after systems/software/services, subscription renewal, support, cyber remediation, acquisition integration, SBC, and dilution | Software/R&D, systems compatibility, cloud hosting, support labor, security response, CalypsoAI integration, SBC, and debt | Customer consolidation, cyber incident, renewal, cloud competition, services mix, acquisition return, and liquidity | Revenue/OCF rise while software renewal, cyber/remediation cost, services burden, acquisition return, or per-share cash weakens |
| Veralto | Embedded water/product-quality measurement cash after R&D, service, instruments, acquisitions, working capital, debt, and dilution | Instruments, analytics, R&D, qualification/support, service, bolt-on acquisitions, working capital, SBC, and debt | Industrial/water budgets, acquisition quality, working-capital growth, debt, compliance spending, and pricing | OCF conversion remains high while acquired cohorts, receivables/inventory, R&D/service burden, debt, or diluted residual deteriorates |
| Caterpillar | Equipment plus aftermarket and Cat Financial cash after dealer inventory, finance receivables, plant capex, warranty, tariffs, debt, and capital returns | Manufacturing plants, dealer support, services, inventory, Cat Financial funding, warranty, acquisitions, capex, and dilution | Construction/mining cycle, dealer inventory, finance losses, tariffs, backlog conversion, rates, and liquidity | Backlog/sales rise while dealer inventory, finance receivables, tariff recovery, warranty, capex, or diluted owner cash weakens |

## Current evidence anchors

- Host 2025 comparable Total RevPAR rose `4.2%`, net income was `$776M`,
  Adjusted EBITDAre `$1.757B`, OCF `$1.510B`, capex `$644M`, and 2026 capex
  budget `$525M-$625M`; GAAP included `$148M` property-sale gains and `$17M`
  condominium income.
- F5 FY2025 revenue was about `$3.088B`, OCF `$949.7M`, capex `$43.3M`, and
  acquisitions `$171.1M`, including `$145.2M` cash for CalypsoAI; cash and
  investments were approximately `$1.360B`.
- Veralto FY2025 revenue was `$5.503B`, OCF `$1.077B`, PP&E spending `$63M`,
  cash after PP&E about `$1.014B`, goodwill `$2.838B`, and debt including current
  maturities `$2.673B`; receivables were `$897M` and inventory `$307M`.
- Caterpillar FY2025 sales were `$67.589B`, OCF `$11.739B`, PP&E capex `$2.821B`,
  inventory `$18.135B`, finance receivables roughly `$25.191B`, noncurrent debt
  `$30.696B`, and OCF less PP&E/acquisitions `$8.871B` versus `$7.978B` of
  dividends and repurchases. Q2 2026 sales reached `$20.5B`, with about `$63B`
  backlog and `$392M` expected tariff recovery.

## QoE and financial-shenanigans prompts

1. Host: keep Adjusted FFO/EBITDAre, asset-sale gains, renewal capex, interest,
   labor, insurance, and OP-unit claims separate.
2. F5: separate software/subscription, systems, services, deferred revenue,
   unbilled receivables, cyber remediation, acquisition cash, SBC, and renewal.
3. Veralto: test high OCF conversion against working-capital growth, recurring
   R&D/service, goodwill, bolt-on acquisitions, and debt.
4. Caterpillar: reconcile backlog to dealer inventory, acceptance, receivables,
   Cat Financial collections/losses, warranty, tariffs, capex, and buybacks.
5. For all four, keep adjusted metrics, asset sales, policy recoveries, and
   capital returns out of normalized owner cash until same-entity joins exist.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what RevPAR and property renewal,
application-control renewal, measurement/service retention, equipment cycle and
aftermarket attachment, reinvestment, and cost of capital the price requires.
The Lyn Alden-style stress test asks whether rates, labor, insurance, cyber,
industrial budgets, housing/mining cycles, dealer credit, tariffs, and
refinancing preserve liquidity.

## Promotion boundary

`frontier-packets-qualified; property-control-software-measurement-installed-base-cash-open; no-ranking`

Promotion requires same-period collection, maintenance/replacement capital,
acquisition return, claims, debt, legal-entity availability, SBC, and diluted
common-owner residual for each company. RevPAR, EBITDAre, FFO, ARR, backlog,
OCF, reported FCF, capacity, and buybacks remain diagnostic inputs.

## Sources

- [Host deep-company forensic memo](../deep-company-pages/host-hotels-resorts-inc.md)
- [F5 deep-company forensic memo](../deep-company-pages/f5-inc.md)
- [Veralto deep-company forensic memo](../deep-company-pages/veralto-corporation.md)
- [Caterpillar deep-company forensic memo](../deep-company-pages/caterpillar-inc.md)
