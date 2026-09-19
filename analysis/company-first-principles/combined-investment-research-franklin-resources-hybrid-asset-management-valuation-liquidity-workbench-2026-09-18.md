# Franklin Resources hybrid asset-management valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Franklin Resources from broad asset-management evidence
into a company-specific valuation object. It separates public-market funds,
ETFs, SMAs, alternatives, private markets, institutional mandates, cash
management, Western Asset, AUM flows, fee rates, distribution, performance,
working capital, debt, capital returns, and diluted common residual. It does not
treat AUM, net inflows, operating revenue, adjusted earnings, operating cash
flow, free cash flow, or repurchases as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Franklin Resources | Hybrid asset-management cash after client-fee collection, AUM and flow mix, fee-rate pressure, distribution, performance, alternatives fundraising, private-market deployment, Western Asset remediation, debt, and dilution | Investment teams, distribution, technology, seed capital, private-market origination, compliance, acquisitions, retention, working capital, and SBC replacement | Market drawdown, sustained outflows, fee compression, underperformance, private-asset fundraising slowdown, Western Asset losses, client or distributor concentration, debt refinancing, or dilution | AUM and adjusted earnings rise while fee rates, net flows, retention, performance, fundraising, deployment, remediation cost, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2025 AUM was `$1.661T`; long-term net outflows were `-$97.4B`; operating
  revenue was `$8.771B`; effective investment-management fee rate was `40.5`
  basis points versus `41.1` basis points in FY2024.
- FY2025 dividends were `$683.7M` and repurchases `$240.3M`; these are residual
  claims, not proof that fee cash is unencumbered.
- Q3 2026 AUM reached `$1.792T`, alternatives AUM `$294.2B`, and won-but-
  unfunded pipeline `$28.6B`; Q2 alternatives fundraising was `$14.3B`.
- The platform spans public markets, ETFs, SMAs, alternatives, private markets,
  institutional mandates, and cash management; Western Asset remains an
  internal quality split rather than a consolidated success signal.

## QoE and financial-shenanigans prompts

1. Reconcile AUM changes into market performance, flows, FX, acquisitions,
   redemptions, fee rates, and cash fee collection; AUM growth is not revenue.
2. Separate gross inflows from net flows, funded from unfunded alternatives
   commitments, and fundraising from deployed capital and realized fees.
3. Test Western Asset and other underperforming franchises for retention,
   remediation, compensation, legal, and distribution costs that adjusted
   earnings can obscure.
4. Connect ETFs, SMAs, Canvas, private markets, and international growth to
   marginal technology, talent, seed, compliance, and acquisition spend.
5. Treat dividends, repurchases, and acquisitions as residual claims only after
   client-service, platform, private-market, debt, and remediation needs are funded.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what AUM growth, net flows, fee rate,
performance, alternatives deployment, fundraising, reinvestment rate, and cost
of capital the valuation requires. The Lyn Alden-style stress test asks whether
market drawdowns, investor liquidity, private-asset marks, rates, distribution,
outflows, and franchise remediation remain liquid through a capital-markets
shock without confusing entrusted assets with owner cash.

## Promotion boundary

`franklin-qualified; hybrid-asset-management-cash-open; no-ranking`

Promotion requires same-entity joins from client assets to fee collection,
flows, performance and retention, alternatives fundraising and deployment,
franchise remediation, platform reinvestment, debt, claims, and diluted common
residual. AUM, inflows, revenue, adjusted earnings, OCF, FCF, and repurchases
remain diagnostic inputs.

## Sources

- [Franklin Resources company packet](../../extracted/financial/asset-management/franklin-resources-inc/company-packet.md)
- [Franklin Resources source ledger](../../extracted/financial/asset-management/franklin-resources-inc/source-ledger.md)
