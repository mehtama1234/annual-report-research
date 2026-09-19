# Semiconductor manufacturing valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Micron and Intel from semiconductor-demand evidence into
separate manufacturing valuation objects. It keeps Micron's memory-cycle and
HBM economics distinct from Intel's integrated CPU/foundry rebuild and its
large capital, incentive, dilution, and utilization burden.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment/denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Micron | Memory and storage cash after cycle-normalized pricing, HBM/DRAM/NAND yield, fab and packaging capex, inventory, contracts, export controls, debt, and dilution | Fabs, equipment, technology transitions, yield, power/water, packaging, inventory, R&D, customer qualification, and common capital | Memory price reversal, underutilization, customer concentration, strategic-contract reset, export restriction, inventory build, or capex overspend | Revenue and gross margin rise while price/yield, HBM contract economics, inventory, fab utilization, capex return, or diluted residual weaken |
| Intel | CPU plus external-foundry cash after process yield, product margin, fab utilization, gross/net capex, incentives/partner funding, inventory, debt, government-linked dilution, and dilution | Process R&D, fabs, equipment, packaging, product design, inventory, commitments, incentives, debt, and common capital | 18A/foundry delay, external customer failure, underutilization, inventory impairment, government restrictions/warrants, debt, or repeated equity issuance | Revenue/margin improve while foundry customer volume, yield, utilization, capex return, inventory, commitments, dilution, or self-funding deteriorate |

## Current evidence anchors

- Micron FY2025 revenue was `$37.378B`, up `49%` year over year, with gross
  margin rebuilding to about `40%`; strategic customer agreements and HBM/AI
  demand improve visibility but do not eliminate memory-cycle risk.
- Intel FY2025 revenue was `$52.9B`, operating cash flow `$9.697B`, net capex
  `$11.204B`, and adjusted FCF approximately negative `$1.612B`; capex
  commitments were `$12.8B` and other purchase commitments `$6.7B`.
- Intel Q2 FY2026 revenue was `$16.1B`, operating cash flow `$7.0B`, and
  adjusted FCF negative `$8.419B`. The quarter included a `$12.5B` fair-value
  loss tied to escrowed government-agreement shares and a `$11.0B` GAAP net
  loss attributable to Intel; the accounting effect and dilution/control terms
  require separate treatment.

## QoE and financial-shenanigans prompts

1. For Micron, reconcile bit/wafer shipments, price, mix, HBM/DRAM/NAND yield,
   inventory, customer qualification, take-or-pay terms, and fab utilization.
2. For Intel, reconcile product versus foundry revenue, 18A yield, external
   customer volume, wafer starts, utilization, gross/net capex, partner funding,
   incentives, finance leases, and purchase commitments.
3. Test whether inventory reduction is healthy cash conversion or reduced future
   capacity, and whether inventory growth supports launch or traps cash.
4. Keep government support, escrowed shares, warrants, equity issuance, debt,
   and strategic transactions visible as owner claims.
5. Treat revenue, gross margin, AI contracts, foundry announcements, reported
   OCF, adjusted FCF, dividends, and buybacks as diagnostic or residual measures
   until qualified production and capital returns are evidenced.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what wafer volume, price, yield,
utilization, fab return, product mix, external-foundry revenue, capex, debt
cost, and cost of capital the valuation requires. The Lyn Alden-style stress
test asks whether memory pricing, customer architecture, export policy, power,
water, labor, equipment delivery, incentives, and rates can absorb a downturn
before fabs produce durable common cash.

## Promotion boundary

`semiconductor-manufacturing-qualified; yield-utilization-capex-and-dilution-open; no-ranking`

Promotion requires same-entity, same-period joins from wafer production and
qualification through shipment/collection, yield, inventory, fab utilization,
required capex, incentive/partner obligations, debt, government-linked claims,
and diluted common residual. Revenue, gross margin, AI contracts, foundry
announcements, reported OCF, FCF, dividends, and buybacks remain diagnostic.

## Sources

- [Micron deep company packet](../deep-company-pages/micron-technology-inc.md)
- [Intel deep company packet](../deep-company-pages/intel-corporation.md)
