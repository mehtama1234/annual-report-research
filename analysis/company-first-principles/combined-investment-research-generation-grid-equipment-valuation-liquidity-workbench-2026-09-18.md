# Generation and grid equipment valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves GE Vernova from electrification and data-center demand
evidence into a company-specific valuation and liquidity perimeter. It keeps
Power, Electrification, Wind, equipment RPO, service RPO, contract-liability
funding, project execution, Prolec GE acquisition economics, inventory,
warranty, pensions, debt, and diluted common-owner cash separate from utility
rate-base economics and Cummins' engine franchise.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| GE Vernova generation and grid equipment | Segment-level equipment and service cash after factories, project execution, customer deposits, contract losses, inventory, Prolec GE integration, warranty, pension, debt, tax, and dilution | Turbine/transformer/switchgear capacity, inventory, engineering, installation, service parts, wind remediation, acquisitions, pensions, working capital, and replacement capex | Project delay, customer cancellation, contract-liability reversal, wind losses, Prolec GE underperformance, supply bottleneck, warranty claim, power-policy change, rates, or refinancing | RPO and contract cash rise while equipment margin, service utilization, project acceptance, acquisition return, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2025 orders were `$59.315B`, revenue `$38.068B`, RPO `$150.238B`, OCF
  `$4.987B`, capital additions `$1.277B`, and FCF `$3.710B`.
- Q2 FY2026 year-to-date revenue was `$20.442B`, OCF `$10.680B`, capital
  additions `$783M`, and RPO `$176.284B`; the cash result included `$13.695B`
  from contract liabilities and current deferred income.
- June 30, 2026 inventory was `$12.692B`, current contract assets `$9.522B`,
  and first-half cash uses included `$1.744B` of inventory and `$358M` of
  contract assets.
- Equipment RPO was `$87.821B` and services RPO `$88.463B`; their recognition
  horizons and capital burdens differ materially.
- GE Vernova acquired the remaining 50% of Prolec GE for approximately `$5.254B`
  in cash. Prolec GE generated `$1.344B` of revenue and a pre-tax loss of
  `$166M` from acquisition date through June 30, 2026.
- Wind carried higher offshore project costs and contract losses, with 2026
  guidance still expecting approximately `$400M` of Wind segment EBITDA loss.

## QoE and financial-shenanigans prompts

1. Separate Power, Electrification, and Wind by equipment, service, margin,
   contract type, and cash burden. Consolidated RPO can hide profitable service
   demand beside loss-making equipment or wind contracts.
2. Treat contract-liability inflows and slot-reservation deposits as customer
   funding with future delivery obligations, not earned margin or distributable
   owner cash.
3. Reconcile equipment and service RPO to shipment, installation, acceptance,
   margin, contract assets, inventory, claims, and cash collection.
4. Track Prolec GE revenue, margin, inventory step-up, integration costs,
   goodwill, debt, capacity utilization, and cash return separately from the
   RPO it added.
5. Keep wind contract losses, warranties, pensions, tax, acquisitions, debt,
   SBC, and diluted shares in the owner-cash denominator until the physical
   project obligations are settled.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what equipment volume, service
attachment, project margin, RPO conversion, manufacturing return, acquisition
return, wind normalization, reinvestment rate, and cost of capital the valuation
requires. RPO must be converted into segment cash after delivery and claims.

The Lyn Alden-style stress test asks whether utilities, developers, governments,
and industrial customers can fund generation and grid projects through higher
rates, power-policy changes, construction delays, supply shortages, and weaker
economic growth. Liquidity passes only when customer deposits, contract claims,
inventory, debt, pension, and common residual remain visible.

## Promotion boundary

`generation-grid-equipment-qualified; rpo-project-return-and-liquidity-open; no-ranking`

Promotion requires same-entity, same-period joins from equipment/service RPO to
shipment, acceptance, project margin, contract-liability settlement, inventory,
capacity utilization, Prolec GE return, wind cash, warranty, pension, debt, and
diluted common residual. RPO, orders, adjusted EBITDA, OCF, FCF, deposits, and
buybacks remain diagnostic inputs.

## Sources

- [GE Vernova company packet](../deep-company-pages/ge-vernova-inc.md)
- [Next-execution handoff](combined-investment-research-next-execution-handoff-2026-09-17.md)

