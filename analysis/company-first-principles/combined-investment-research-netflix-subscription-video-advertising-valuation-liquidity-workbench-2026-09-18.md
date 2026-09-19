# Netflix subscription video and advertising valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Netflix from recurring-attention evidence into a
company-specific valuation object. It separates paid memberships, engagement,
pricing, advertising, content production and licensing, content amortization,
regional economics, live and gaming extensions, working capital, debt, and
diluted common residual. It does not treat memberships, viewing hours, revenue,
operating margin, operating cash flow, free cash flow, or ad revenue as
normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Netflix | Global subscription-video and advertising cash after billing and collection, churn and retention, content commitments, production and licensing, amortization, ad technology, regional delivery, live and gaming investment, debt, and dilution | Original and licensed content, production facilities, technology and delivery, advertising systems, customer acquisition, live and gaming formats, working capital, debt, and SBC replacement | Churn or pricing resistance, content underperformance, ad-market weakness, content-cost inflation, regional FX or regulation, production disruption, debt refinancing, or dilution | Memberships and ad revenue grow while retention, pricing power, content return, ad yield, content commitments, cash conversion, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2025 revenue was about `$45.2B`, operating margin `29.5%`, ad revenue over
  `$1.5B`, paid memberships above `325M` in Q4, and free cash flow about `$9.5B`.
- Q2 2026 revenue was `$12.560B`, operating income `$4.193B`, operating margin
  `33.4%`, and free cash flow `$1.525B`; Q1 revenue was `$12.250B` and FCF
  `$5.094B`.
- Netflix said members watched more than `97B` hours in the first half of 2026;
  the platform is adding advertising, live programming, games, and adjacent
  entertainment formats to the subscription relationship.
- Content commitments, amortization, production timing, regional mix, and ad
  infrastructure determine whether accounting margin becomes owner cash.

## QoE and financial-shenanigans prompts

1. Reconcile paid memberships and viewing hours to retention, churn, pricing,
   plan mix, household behavior, billing collection, and regional currency.
2. Bridge content expense and commitments to releases, licensing rights,
   amortization, production cash, cancellations, impairments, and audience
   return rather than treating engagement as monetization.
3. Separate advertising revenue from subscriptions; test ad inventory, fill,
   yield, measurement, sales cost, privacy, and incremental technology spend.
4. Keep live, gaming, and other format investments separate from the mature
   subscription engine until their cash returns are evidenced.
5. Treat capital returns as residual claims only after content commitments,
   platform investment, working capital, and debt are funded.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what membership growth, retention,
pricing, content return, ad yield, regional mix, reinvestment rate, and cost of
capital the valuation requires. The Lyn Alden-style stress test asks whether
household budgets, ad demand, content costs, rates, FX, regulation, and
production availability remain liquid through a consumer-attention shock
without confusing viewing scale with durable common-owner cash.

## Promotion boundary

`netflix-qualified; subscription-video-and-ad-cash-open; no-ranking`

Promotion requires same-entity joins from memberships and advertising to billing
and collection, retention, content delivery and return, commitments,
amortization, platform reinvestment, debt, claims, and diluted common residual.
Memberships, viewing hours, revenue, margin, OCF, FCF, and ad revenue remain
diagnostic inputs.

## Sources

- [Netflix company packet](../../extracted/services/music-video-stores/netflix-inc/company-packet.md)
- [Netflix source ledger](../../extracted/services/music-video-stores/netflix-inc/source-ledger.md)
