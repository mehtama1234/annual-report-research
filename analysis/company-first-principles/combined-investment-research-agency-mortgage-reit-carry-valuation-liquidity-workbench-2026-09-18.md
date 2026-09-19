# Agency mortgage-REIT carry and book-value valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench adds AGNC Investment as a distinct levered Agency mortgage-REIT
asset/liability-spread lane. It separates Agency RMBS carry, repo financing,
interest-rate hedges, prepayment and spread risk, tangible book value, and
dividend sustainability from banks, insurers, asset managers, and operating
companies.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| AGNC Investment | Normalized net spread and dollar-roll income plus tangible-book-value preservation after repo funding, hedges, operating costs, leverage, prepayment, mortgage spreads, dividend, and diluted common residual | Agency RMBS/TBA portfolio, repo collateral, hedge book, liquidity, unencumbered assets, duration management, capital issuance, and common capital | Rate shock, mortgage-spread widening, prepayment/extension, repo haircut or margin call, counterparty failure, forced sales, dividend excess, or dilutive issuance | Spread income and dividend rise while comprehensive income, tangible book value, leverage, hedge effectiveness, repo access, or per-share residual deteriorate |

## Current evidence anchors

- FY2025 portfolio was approximately `$94.8B`, approximately `95%` Agency RMBS/TBAs; at-risk leverage was about `7.2x`; net spread and dollar-roll income about `$1.535B`; economic return on tangible common equity about `22.7%`.
- Q1 2026 spread income remained approximately `$475M`, but comprehensive loss was about `$200M`, economic return `-1.6%`, and tangible book value per share fell from `$8.88` to `$8.38`.
- Q2 2026 net and comprehensive income were approximately `$603M`, economic return `6.7%`, tangible book value per share `$8.58`, spread income about `$462M`, and at-risk leverage about `7.4x`.
- Q2 2026 common dividend was approximately `$0.36` per share; the dividend must be tested against normalized economic earnings and book-value preservation, not carry alone.

## QoE and financial-shenanigans prompts

1. Build the bridge from asset interest and dollar-roll income to repo funding,
   hedge expense, operating costs, net spread, comprehensive income, book value,
   dividend, and total return.
2. Track coupon, asset yield, premium amortization, duration, prepayment,
   mortgage spread, TBA exposure, realized/unrealized marks, and hedge basis.
3. Stress 7x-plus leverage through rates, spreads, convexity, repo haircuts,
   margin calls, collateral, counterparties, and forced sales.
4. Compare dividends with normalized economic return and tangible book value;
   carry coverage does not prove capital preservation.
5. Treat equity issuance, preferred capital, repurchases, and share count as
   per-share book-value and future-spread claims rather than neutral financing.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what sustainable asset yield, funding
cost, hedge cost, leverage, duration gap, prepayment, spread, book-value return,
and cost of equity the market price requires. The Lyn Alden-style stress test
asks whether Treasury rates, mortgage spreads, repo liquidity, collateral,
housing finance, and counterparty access preserve the portfolio through a
volatile rate cycle.

## Promotion boundary

`agency-mortgage-reit-qualified; carry-book-value-and-funding-open; no-ranking`

Promotion requires same-entity, same-period joins from Agency RMBS/TBA assets to
repo funding, hedge results, collateral, prepayment, comprehensive income,
tangible book value, leverage, dividend, capital actions, and diluted common
residual. Spread income, economic return, book value, dividends, reported OCF,
and yield remain diagnostic inputs rather than normalized owner cash.

## Sources

- [AGNC company page](../deep-company-pages/agnc-investment-corp.md)
- [AGNC source ledger](../../extracted/financial/reit-mortgage/agnc-investment-corp/source-ledger.md)
- [AGNC company packet](../../extracted/financial/reit-mortgage/agnc-investment-corp/company-packet.md)

