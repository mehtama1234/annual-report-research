# Electronic test and measurement valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Keysight Technologies and Teradyne from test-demand
evidence into company-specific valuation objects. It keeps Keysight's design,
measurement, network-assurance, software, and service workflow separate from
Teradyne's semiconductor, product-test, and robotics production-test cycle.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment/denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Keysight | Design-to-deployment measurement and assurance cash after software/service attachment, customer deposits, R&D, acquisitions, inventory, debt, SBC, and dilution | Measurement hardware, calibration/service, software, R&D, customer workflow, acquisition integration, working capital, and common capital | Electronics-capex slowdown, customer acceptance, contract-liability reversal, acquisition integration, export/security limits, or high-speed-network demand reversal | Orders and revenue rise while software/service attachment, contract liabilities, R&D, customer concentration, acquisition return, or diluted cash weaken |
| Teradyne | Semiconductor and system-test cash after equipment acceptance, cycle-normalized utilization, deferred revenue, R&D, robotics/product-test mix, acquisitions, SBC, and dilution | Test systems, software/support, R&D, inventory, customer advances, robotics, acquisitions, and common capital | Memory/semiconductor capex pause, customer concentration, deferred-revenue reversal, robotics slowdown, export restrictions, or inventory build | Test revenue and AI intensity rise while utilization, customer advances, service/support, robotics economics, or diluted residual deteriorate |

## Current evidence anchors

- Keysight FY2025 revenue was `$5.375B`, operating cash flow `$1.409B`, PP&E
  spending `$128M`, and the simple cash-after-PP&E screen about `$1.281B`;
  R&D was approximately `$1.007B`.
- Keysight Q3 FY2026 revenue was `$1.85B`, with orders above `$2B`; contract
  liabilities were approximately `$767M` in the cited baseline, reflecting
  customer deposits and undelivered services.
- Teradyne FY2025 revenue was `$3.190B`, operating cash flow `$674M`, PP&E
  spending `$224M`, and non-GAAP FCF approximately `$450M`; Q2 2026 revenue
  was `$1.329B`, including `$1.122B` Semiconductor Test and `$100M` Robotics.
- Teradyne's 2025 cash flow included approximately `$52.6M` from deferred
  revenue/customer advances; the advance is useful liquidity but not permanent
  owner cash.

## QoE and financial-shenanigans prompts

1. Separate Keysight software, calibration, service, support, customer deposits,
   and repeat workflow from instrument and acquisition-driven revenue.
2. Reconcile Teradyne equipment orders through acceptance, customer advances,
   deferred revenue, utilization, support, inventory, and replacement.
3. Test semiconductor and memory capex, customer concentration, export controls,
   robotics demand, product-test mix, and cycle-normalized gross margin.
4. Keep R&D, acquisition cash, SBC, contract-liability releases, and customer
   advances visible when measuring per-share cash.
5. Treat orders, revenue, backlog/deposits, reported OCF, FCF, dividends, and
   buybacks as diagnostic or residual measures until workflow collection and
   reinvestment are joined.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what test intensity, installed-base
attachment, software/service mix, utilization, R&D, acquisition return, margin,
and cost of capital the valuation requires. The Lyn Alden-style stress test asks
whether electronics and semiconductor capex, customer budgets, inventory,
export rules, and rates can interrupt cash before the test workflow compounds.

## Promotion boundary

`electronic-test-qualified; utilization-cycle-and-acceptance-open; no-ranking`

Promotion requires same-entity, same-period joins from instrument/test demand
through acceptance and collection, service/support settlement, required R&D and
replacement capital, inventory, acquisitions, debt, and diluted common
residual. Orders, revenue, contract liabilities, deferred revenue, reported
OCF, FCF, dividends, and buybacks remain diagnostic inputs.

## Sources

- [Keysight deep company packet](../deep-company-pages/keysight-technologies-inc.md)
- [Teradyne deep company packet](../deep-company-pages/teradyne-inc.md)
