# Lennar land-light homebuilder valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench tests Lennar as a direct homebuilder and housing-finance platform. It keeps home closings, incentives, mortgage affordability, cycle time, land exposure, backlog, mortgage/title capture, multifamily, working capital, and diluted common residual separate from reported revenue and backlog value.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Lennar | Land-light homebuilding cash after construction inventory, land commitments, incentives, cycle time, mortgage/title operations, multifamily, debt, and diluted common residual | Land acquisition and development, construction, finished inventory, cycle-time execution, mortgage/title capital, technology, multifamily, working capital, debt, and claims | Mortgage-rate and affordability shock, cancellation/absorption weakness, incentive escalation, land impairment, construction inflation, credit losses, or refinancing | Deliveries and backlog rise while gross margin, incentives, inventory turns, land-light conversion, mortgage capture, or diluted per-share cash weaken |

## Current evidence anchors

- FY2025 homebuilding generated roughly `$32B` of revenue, about `94%` of consolidated revenue; total deliveries including unconsolidated entities were `82,583` homes.
- Q2 2026 revenue was `$7.9B`, net earnings attributable to Lennar `$305M`, deliveries `20,519`, new orders `21,749`, and backlog `16,818` homes valued at `$6.6B`.
- Q2 incentives were approximately `12.9%`; management continued to emphasize affordability, faster cycle times, standard plans, and less than `5%` of land on balance sheet.
- The platform also includes mortgage, title, closing services, multifamily, funds, joint ventures, and technology investments, so consolidated cash is not identical to homebuilding margin.

## QoE and financial-shenanigans prompts

1. Reconcile backlog and orders to cancellations, closings, incentives, gross margin, inventory turns, and collected cash.
2. Test the land-light claim against land commitments, option obligations, unconsolidated entities, inventory aging, and future construction requirements.
3. Separate homebuilding cash from mortgage/title earnings, multifamily, funds, and technology investments.
4. Keep mortgage receivables, debt, warranty claims, impairments, dividends, buybacks, and diluted shares in the residual schedule.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what deliveries, average selling prices, incentives, gross margin, cycle time, land intensity, reinvestment rate, and cost of capital the valuation requires. The Lyn Alden-style stress test asks whether households can fund purchases through rates, labor, insurance, tax, and affordability shocks while Lennar preserves inventory liquidity and financing access.

## Promotion boundary

`lennar-qualified; affordability-and-land-light-cash-open; no-ranking`

Promotion requires same-entity joins from orders and backlog to closings, cancellations, incentives, inventory, land commitments, mortgage/title collections, required reinvestment, debt, and diluted common residual. Deliveries, backlog, revenue, adjusted earnings, OCF, and buybacks remain diagnostic inputs.

## Sources

- [Lennar company packet](../../extracted/industrial-goods/residential-construction/lennar-corporation/company-packet.md)
- [Lennar source ledger](../../extracted/industrial-goods/residential-construction/lennar-corporation/source-ledger.md)
