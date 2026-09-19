# Loews subsidiary allocator valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Loews Corporation from generic holding-company evidence
into a company-specific valuation object. It separates CNA insurance, Boardwalk
Pipelines, Loews Hotels, Altium Packaging, subsidiary dividends, insurance
float, energy infrastructure, hospitality, packaging, parent liquidity, debt,
capital allocation, and diluted common residual. It does not treat subsidiary
net income, consolidated earnings, operating cash flow, asset values, dividends,
or repurchases as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Loews | Parent common cash after subsidiary underwriting and claims, pipeline throughput, hotel demand, packaging operations, subsidiary distributions, parent expenses, debt, and dilution | Subsidiary capital, insurance reserves, energy maintenance and expansion, hotels, packaging plants, acquisitions, parent liquidity, and SBC replacement | Catastrophe or reserve shock, energy regulation or throughput decline, hotel demand, packaging margin, subsidiary dividend restriction, parent debt, or dilution | Consolidated earnings and asset values rise while subsidiary cash distributions, reserves, capex, parent liquidity, claims, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2025 net income attributable to Loews was about `$1.7B`, or roughly `$7.97`
  diluted EPS.
- Q2 2026 net income was about `$444M`; six-month net income was about `$781M`.
  Q1 was about `$337M` and Q4 2025 about `$402M`.
- The portfolio spans CNA, Boardwalk Pipelines, Loews Hotels, and Altium
  Packaging; diversified earnings are not interchangeable with cash available
  to the parent.
- Loews is a smaller, operating-mix-dependent allocator: insurance, energy,
  hospitality, and packaging move on different cycles and distribute cash under
  different legal, regulatory, and reinvestment constraints.

## QoE and financial-shenanigans prompts

1. Bridge subsidiary earnings to actual parent dividends, intercompany flows,
   reserves, capital requirements, and parent cash.
2. Separate CNA underwriting and investment returns, Boardwalk throughput and
   regulatory economics, hotel demand, and packaging margin.
3. Keep asset values, unrealized gains, subsidiary transactions, catastrophe
   reserves, and one-time items separate from distributable common cash.
4. Test whether parent capital allocation creates value after subsidiary
   reinvestment, legal-entity constraints, debt, and minority or preferred claims.
5. Treat buybacks and dividends as residual claims only after parent liquidity,
   subsidiary capital, claims, capex, and debt are funded.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what subsidiary cash yield, underwriting
return, energy throughput, hotel occupancy, packaging margin, reinvestment rate,
holding-company discount, and cost of capital the valuation requires. The Lyn
Alden-style stress test asks whether insurance claims, energy regulation,
hospitality demand, packaging costs, rates, and parent liquidity remain solvent
through a multi-subsidiary shock without confusing accounting diversification with
common-owner cash.

## Promotion boundary

`loews-qualified; subsidiary-distribution-and-parent-cash-open; no-ranking`

Promotion requires same-entity joins from each subsidiary to collection,
reserves, legal-entity distribution, capex, parent liquidity, debt, claims,
capital allocation, and diluted common residual. Subsidiary earnings, asset
values, OCF, dividends, and repurchases remain diagnostic inputs.

## Sources

- [Loews company packet](../../extracted/financial/conglomerates/loews-corporation/company-packet.md)
- [Loews source ledger](../../extracted/financial/conglomerates/loews-corporation/source-ledger.md)
