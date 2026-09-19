# New York Times trust, subscription, and bundle valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves The New York Times Company from attention-economy evidence
into a company-specific valuation object. It separates digital subscriptions,
newsroom and editorial investment, The Athletic, Audio, Cooking, Games,
Wirecutter, podcasts, advertising, affiliate and licensing revenue, content
rights, churn, product bundle economics, working capital, debt, and diluted
common residual. It does not treat subscribers, engagement, revenue, adjusted
operating profit, operating cash flow, free cash flow, or advertising growth as
normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| The New York Times | Direct subscription and premium-information cash after billing and collection, churn and retention, newsroom investment, product bundle costs, content rights, advertising, affiliate settlement, licensing, debt, and dilution | Journalism and editorial labor, product and technology, The Athletic and other bundle content, audio/video/games, customer acquisition, rights, working capital, and SBC replacement | Subscriber churn, price resistance, advertising slowdown, platform/search/AI distribution shift, newsroom cost inflation, content impairment, product failure, debt refinancing, or dilution | Subscribers and ARPU grow while retention, bundle contribution, newsroom productivity, content rights, ad yield, collection, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2025 revenue was about `$2.825B`, including subscription revenue `$1.951B`,
  advertising `$566.0M`, and affiliate/licensing/other `$308.1M`.
- The company exited 2025 with about `12.78M` total subscribers, operating cash
  flow about `$584.5M`, and free cash flow about `$550.5M`.
- Q2 2026 total subscribers reached `13.35M`, digital-only subscribers `12.80M`,
  digital-only ARPU `$9.94`, and digital advertising grew `20.7%`.
- The bundle spans News, The Athletic, Audio, Cooking, Games, Wirecutter,
  podcasts, and video; direct billing and recurring habit are valuable only
  after content, labor, product, and retention costs.

## QoE and financial-shenanigans prompts

1. Reconcile subscribers and ARPU to churn, cohort retention, price increases,
   bundle mix, billing collection, refunds, and product-level contribution.
2. Separate news and newsroom costs from Athletic, Audio, Cooking, Games,
   Wirecutter, podcast, and video economics; test rights and incremental
   engagement rather than treating the bundle as free adjacency.
3. Bridge advertising, affiliate, and licensing revenue to inventory quality,
   platform dependence, commissions, settlement, and cyclicality.
4. Keep one-time rights, restructuring, acquisitions, and platform changes apart
   from recurring subscription cash.
5. Treat capital returns as residual claims only after newsroom, product, content,
   rights, working capital, and debt obligations are funded.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what subscriber growth, retention,
ARPU, bundle attachment, ad yield, content return, newsroom investment,
reinvestment rate, and cost of capital the valuation requires. The Lyn
Alden-style stress test asks whether household budgets, advertising demand,
platform distribution, journalism costs, rates, and content rights remain liquid
through an information shock without confusing subscriber scale with durable owner cash.

## Promotion boundary

`nyt-qualified; trust-subscription-and-bundle-cash-open; no-ranking`

Promotion requires same-entity joins from subscribers and advertising to billing
and collection, retention, newsroom and product reinvestment, rights and bundle
contribution, affiliate settlement, debt, claims, and diluted common residual.
Subscribers, ARPU, revenue, adjusted earnings, OCF, FCF, and ad growth remain
diagnostic inputs.

## Sources

- [New York Times company packet](../../extracted/services/publishing-newspapers/the-new-york-times-company/company-packet.md)
- [New York Times source ledger](../../extracted/services/publishing-newspapers/the-new-york-times-company/source-ledger.md)
