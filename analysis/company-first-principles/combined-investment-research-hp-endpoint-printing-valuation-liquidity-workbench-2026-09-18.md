# HP endpoint and printing valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves HP Inc. from broad hardware evidence into a
company-specific valuation object. It separates Personal Systems from Printing,
then tests endpoint replacement, commercial demand, channel inventory, supplies
attachment, pricing, tariffs, supplier commitments, restructuring, working
capital, debt, capital returns, and diluted common residual. It does not treat
net revenue, PC units, adjusted EPS, operating cash flow, free cash flow, or
repurchases as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| HP | Endpoint-device and printing cash after end-user sell-through, channel settlement, supplies attachment, manufacturing and supplier commitments, R&D, restructuring, tariffs, debt, and dilution | Product design and R&D, inventory, channel support, printing supplies and service infrastructure, manufacturing commitments, software, restructuring, working capital, acquisitions, and SBC replacement | Enterprise PC or office-spend slowdown, channel inventory correction, print-base decline, tariff shock, supply interruption, pricing pressure, restructuring cash, debt refinancing, or dilution | Revenue or EPS stabilizes while end-user sell-through, channel inventory, supplies attachment, pricing, required reinvestment, margin quality, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2025 net revenue was `$53.6B`; diluted EPS was `$2.82` and non-GAAP diluted
  EPS was `$3.39`.
- Q4 FY2025 revenue was `$14.1B`, Q1 FY2026 revenue `$13.5B`, and Q2 FY2026
  revenue `$13.2B`; Personal Systems remains the growth engine while Printing
  is more mature and pressured.
- Tariff mitigation, pricing, and cost actions are explicit current-period
  variables; tariff recovery or price increases are not automatically durable
  customer cash.
- HP is a useful contrast with Apple’s premium ecosystem and Dell’s
  AI-server-plus-PC model: its return depends more heavily on replacement,
  channel discipline, supplies, and mature-hardware mix.

## QoE and financial-shenanigans prompts

1. Reconcile PC and printer shipments to end-user sell-through, channel
   inventory, returns, receivables, supplier commitments, and cash settlement.
2. Separate Personal Systems growth from Printing decline and test supplies and
   services attachment, installed-base replacement, and customer retention.
3. Keep tariff mitigation, price, mix, currency, restructuring, and cost actions
   separate from durable gross-margin improvement.
4. Test whether buybacks and dividends are funded after inventory, supplier,
   warranty, restructuring, debt, and required product investment.
5. Track adjusted EPS add-backs and capitalized or deferred costs against the
   cash actually required to preserve the endpoint and printing franchises.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what endpoint replacement, commercial
volume, supplies attachment, pricing, mix, reinvestment rate, and cost of
capital the valuation requires. The Lyn Alden-style stress test asks whether
office demand, tariffs, channel finance, component supply, rates, and household
or enterprise budgets remain liquid through a hardware downcycle without
confusing shipments or buybacks with durable owner cash.

## Promotion boundary

`hp-qualified; endpoint-and-printing-cycle-open; no-ranking`

Promotion requires same-entity joins from shipments to sell-through, collection,
channel inventory, supplies and service attachment, supplier settlement,
restructuring, debt, and diluted common residual. Revenue, units, adjusted EPS,
OCF, FCF, and repurchases remain diagnostic inputs.

## Sources

- [HP company packet](../../extracted/technology/computer-hardware/hp-inc/company-packet.md)
- [HP source ledger](../../extracted/technology/computer-hardware/hp-inc/source-ledger.md)
