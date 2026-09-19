# Sirius XM paid audio and Pandora valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Sirius XM from current-period evidence into a company-specific valuation object. It tests paid subscribers, churn, in-car distribution, premium content, Pandora advertising and subscriptions, podcasting, royalties, customer acquisition, free cash flow, debt, refinancing, and diluted common residual. It does not pool Sirius XM with broadcast radio, CTV, publishers, or agency platforms.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Sirius XM | Paid-audio relationship cash after subscriber billing, churn, content and royalty costs, OEM distribution, Pandora advertising, podcasting, technology, debt service, and dilution | Content and royalty commitments, customer acquisition, OEM and distribution, platform technology, working capital, debt, and shares | Churn, self-pay losses, auto/OEM changes, royalty inflation, Pandora ad weakness, content competition, refinancing, or leverage | Subscribers and adjusted EBITDA rise while churn, net adds, royalty burden, cash conversion, free cash flow after debt service, or diluted common residual deteriorate |

## Current evidence anchors

- 2025 revenue was about `$8.558B`, adjusted EBITDA about `$2.665B`, and free cash flow about `$1.256B`; SiriusXM contributed about `$6.417B` and Pandora/Off-Platform about `$2.141B`.
- Q2 2026 revenue was about `$2.16B`, adjusted EBITDA about `$691M`, and free cash flow about `$593M`.
- Q2 self-pay net additions were positive `22,000`, churn improved to `1.4%`, total subscribers stayed near `33M`, and the trial funnel was about `7.5M`.
- Pandora and Off-Platform revenue was about `$543M` in Q2, including approximately `$413M` of Pandora advertising and `$130M` of Pandora subscriber revenue.

## QoE and financial-shenanigans prompts

1. Reconcile self-pay and trial funnels, churn, pricing, OEM distribution, royalties, content, and acquisition costs before treating subscriber economics as recurring.
2. Separate SiriusXM subscriber revenue from Pandora advertising, Pandora subscriptions, podcasts, and off-platform revenue.
3. Reconcile free cash flow to royalty commitments, content, technology, working capital, debt service, refinancing, capital returns, and dilution.
4. Test whether low churn reflects durable habit and distribution or temporary pricing, promotions, and bundled access.

## Damodaran/Lyn Alden application

The expectation test asks what churn, net additions, pricing, royalty burden, Pandora ad growth, podcast monetization, margin, free cash flow, leverage, and cost of capital are embedded in the valuation. The stress test asks whether in-car distribution, content, household budgets, auto cycles, platform changes, rates, and royalties preserve the paid relationship.

## Promotion boundary

`siriusxm-qualified; paid-audio-retention-and-debt-service-open; no-ranking`

Promotion requires same-entity joins from subscribers and audio usage to collection, churn, renewal, royalty and content costs, OEM distribution, debt service, claims, funding, and diluted common residual. Subscribers, revenue, adjusted EBITDA, FCF, guidance, audience scale, and capital returns remain diagnostic inputs.

## Sources

- [Sirius XM company packet](../../extracted/services/broadcasting-radio/sirius-xm-holdings-inc/company-packet.md)
- [Sirius XM source ledger](../../extracted/services/broadcasting-radio/sirius-xm-holdings-inc/source-ledger.md)
