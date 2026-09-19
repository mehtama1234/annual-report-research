# Transaction marketplace valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves eBay into a company-specific transaction-marketplace
valuation/liquidity object. It keeps goods marketplace economics separate from
travel marketplaces, advertising measurement, participation platforms, and
retailers. The object tests GMV conversion, take rate, seller/buyer retention,
payments, fraud and transaction losses, advertising, platform reinvestment,
acquisitions, debt, SBC, buybacks, and diluted common residual.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment/denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| eBay | Marketplace transaction and advertising cash after seller/buyer collection, payment processing, fraud and buyer-protection losses, marketing, capitalized platform development, trust/support, acquisitions, debt, SBC, and diluted common residual | GMV/take rate, category and buyer/seller cohorts, ad penetration, transaction losses, payment costs, capitalized software, product/R&D, Depop and other acquisitions, debt, SBC, and buybacks | Buyer/seller churn, fraud/recovery-rate deterioration, platform/discovery disintermediation, ad yield pressure, payment losses, acquisition payback, rates, debt, and regulatory/privacy change | GMV, active buyers, take rate, advertising, adjusted earnings, OCF, or repurchases rise while transaction-loss rate, cohort health, capitalized development, Depop return, or per-share cash deteriorates |

## Current evidence anchors

- FY2025 revenue was `$11.100B`, GMV `$79.609B`, continuing OCF `$2.009B`,
  PP&E spending `$525M`, and acquisitions `$208M`, leaving a simple continuing
  cash screen of about `$1.276B` before SBC, dividends, buybacks, and debt.
- The 2025 take rate was about `13.94%`, up from `13.77%` in 2024; revenue grew
  8% while GMV grew 7%. A higher take rate does not establish pricing power if
  seller incentives, mix, or advertising substitution drive the change.
- Q2 2026 revenue was `$3.134B`, GMV `$22.398B`, take rate `13.99%`, and active
  buyers `136M`, while first-party advertising was `$570M`. GMV grew faster than
  buyers, so frequency, mix, and cohort quality require testing.
- First-half 2026 transaction losses were `$271M` versus `$167M` prior year;
  the filing attributed part of the increase to fraud and recovery-rate changes.
  The loss rate per GMV is a core trust-and-cash denominator.
- eBay capitalized `$134M` of platform development in 2025, paid `$607M` of
  SBC, and repurchased about `$2.5B`. The Depop acquisition required `$1.4B`
  cash after the quarter, so acquired audience and seller supply need a return
  bridge rather than immediate value credit.
- Year-end cash was `$1.867B` against approximately `$5.996B` debt and capital
  leases. Liquidity cannot be judged from the marketplace's low inventory burden
  alone.

## QoE and financial-shenanigans prompts

1. Separate GMV, retained revenue, take rate, advertising, payments, and seller
   incentives; GMV is not eBay revenue or owner cash.
2. Reconcile transaction losses, fraud, chargebacks, refunds, recovery rates,
   and buyer protection to GMV and repeat activity.
3. Test advertising for incremental seller demand versus paid displacement of
   organic placement; track seller return and retention.
4. Treat capitalized platform development as recurring replacement investment,
   not as zero maintenance capex; include SBC and diluted shares.
5. Keep Depop and other acquisitions, debt, dividends, and buybacks separate
   until acquired cohorts produce collection, contribution, and common cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what GMV growth, take rate, category
mix, ad penetration, transaction-loss rate, buyer/seller retention, platform
investment, acquisition return, and cost of capital the price requires. The Lyn
Alden-style stress test asks whether household demand, seller liquidity, fraud,
payment-system dependence, AI/discovery disintermediation, rates, regulation,
and credit conditions preserve marketplace cash in a downturn.

## Promotion boundary

`transaction-marketplace-qualified; trust-loss-and-acquisition-return-open; no-ranking`

Promotion requires same-entity, same-period joins from GMV and marketplace
cohorts to retained revenue, take rate, seller/buyer retention, payment and
fraud losses, collection, platform replacement investment, acquisition return,
debt, SBC, diluted shares, and common-owner residual. GMV, active buyers,
advertising, adjusted earnings, OCF, FCF, dividends, and buybacks remain
diagnostic inputs.

## Sources

- [eBay deep-company packet](../deep-company-pages/ebay-inc.md)
- [eBay company packet](../../extracted/consumer-goods/internet-service-providers/ebay/company-packet.md)
