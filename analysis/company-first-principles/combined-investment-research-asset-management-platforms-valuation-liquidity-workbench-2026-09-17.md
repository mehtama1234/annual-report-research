# Asset-management platforms valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench moves BlackRock, Blackstone, and Brookfield from company
observations into distinct valuation, reinvestment, liquidity, and thesis-
breaker objects. It does not pool AUM, fee-related earnings, distributable
earnings, carried interest, owned-asset income, insurance capital, or common-
owner cash across unlike platforms.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| BlackRock | Public-market, ETF, technology, data, and private-market fee cash after platform investment, acquisitions, compensation, and capital claims | Aladdin/data infrastructure, distribution, product support, Preqin/HPS integration, technology R&D, SBC, and diluted shares | Market drawdown, fee compression, flow reversal, acquisition integration, technology competition, regulatory/political pressure | AUM and flows remain high while fee rates, technology economics, integration cash, or per-share residual deteriorate |
| Blackstone | Fee-related earnings plus realization/performance economics after perpetual-capital support, credit losses, product liquidity, compensation, and dilution | Origination, fundraising, wealth/insurance channels, private-credit underwriting, product support, SBC, and diluted shares | Exit-market closure, NAV/redemption pressure, private-credit loss, real-estate valuation, fundraising slowdown, and leverage | AUM/fee earnings grow while realizations, credit quality, product liquidity, or diluted common residual deteriorate |
| Brookfield | Fee-bearing capital plus operating-asset, insurance, and principal economics after leverage, monetization, and entity claims | Asset operations, insurance capital, infrastructure/real estate reinvestment, acquisitions, leverage, SBC, and ownership dilution | Asset valuation, refinancing, monetization timing, insurance claims, leverage, and complex legal-entity availability | Distributable earnings rise while asset cash, monetization, insurance capital, leverage, or common residual weakens |

## Current evidence anchors

- BlackRock FY2025 AUM was `$14.0T`, net inflows `$698B`, adjusted operating
  margin `44.1%`, and technology-services/subscription revenue `$1.981B`; Q2
  2026 AUM reached `$15.3T` with first-half net inflows `$321B`.
- Blackstone FY2025 AUM was about `$1.27T`, fee-earning AUM `$921.7B`, and
  perpetual-capital AUM `$523.6B`; fee-related earnings were about `$5.7B` and
  distributable earnings about `$7.1B`; realizations were about `$125.6B`.
- Brookfield FY2025 distributable earnings before realizations were about
  `$5.4B`, total distributable earnings about `$6.0B`, and net income about
  `$3.2B`; Q1 2026 highlighted `$44B` of insurance capital raised and about
  `$180B` of insurance assets.

## QoE and financial-shenanigans prompts

1. Separate AUM, fee-earning AUM, flows, fee rates, performance fees, realized
   gains, owned-asset income, and actual legal-entity cash.
2. Test compensation, carried interest, incentive allocation, SBC, acquisition
   integration, and dilution before using adjusted earnings per share.
3. Keep client capital, insurance/statutory capital, fund cash, balance-sheet
   capital, and common-owner cash in separate ledgers.
4. Stress realization timing, NAV financing, redemption terms, private-credit
   losses, real-estate marks, refinancing, and asset-level leverage.
5. For Brookfield, trace operating-asset cash through ownership, debt,
   preferred/NCI claims, insurance entities, and parent availability.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what fee rates, flows, performance
economics, realization cadence, reinvestment, cost of capital, and diluted
ownership the market price requires. The Lyn Alden-style stress test asks how
market drawdowns, rates, refinancing, liquidity windows, insurance claims,
private-credit losses, and asset marks affect durability.

## Promotion boundary

`asset-management-platforms-qualified; fee-realization-and-legal-entity-cash-open; no-ranking`

Promotion requires same-entity fee collection, performance/realization cash,
client-versus-parent capital allocation, compensation and dilution, debt,
insurance or fund claims, and common-owner residual. AUM, flows, fee-related
earnings, distributable earnings, carried interest, and adjusted EPS remain
diagnostic inputs.

## Sources

- [BlackRock company analysis](financial/asset-management/blackrock-inc/company-analysis.md)
- [Blackstone company analysis](financial/asset-management/blackstone-inc/company-analysis.md)
- [Brookfield company analysis](financial/asset-management/brookfield-corporation/company-analysis.md)
