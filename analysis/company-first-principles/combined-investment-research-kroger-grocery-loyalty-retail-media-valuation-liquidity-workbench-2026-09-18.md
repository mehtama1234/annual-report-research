# Kroger grocery, loyalty, and retail-media valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Kroger from grocery and retail-media evidence into a
company-specific valuation object. It separates grocery baskets, fuel,
pharmacy, eCommerce, loyalty and personalization, Kroger Precision Marketing,
private label, inventory, supplier terms, labor, stores, debt, merger or
portfolio claims, and diluted common residual. It does not treat sales,
eCommerce growth, retail-media profit, adjusted FIFO operating profit, operating
cash flow, free cash flow, or repurchases as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Kroger | Grocery-and-data-platform cash after basket sell-through, supplier settlement, loyalty collection, pharmacy and fuel economics, eCommerce fulfillment, store maintenance, labor, inventory, debt, and dilution | Stores, distribution, eCommerce fulfillment, pharmacy, private-label product, technology and personalization, retail-media systems, working capital, labor, acquisitions, and SBC replacement | Food inflation or deflation, consumer trade-down, supplier pressure, labor cost, pharmacy reimbursement, eCommerce fulfillment burden, retail-media slowdown, merger or debt stress, or dilution | Alternative-profit growth continues while grocery margin, inventory turns, supplier terms, eCommerce fulfillment, pharmacy economics, retail-media collection, or diluted per-share cash deteriorate |

## Current evidence anchors

- Fiscal 2025 delivered more than `$16B` in eCommerce sales and `$1.5B` in
  operating profit from alternative profit businesses.
- Q1 2026 sales were `$46.1B`; adjusted eCommerce sales grew `19%`; Kroger
  Precision Marketing profit grew more than `20%`; operating profit was `$1.407B`.
- Kroger Precision Marketing uses first-party data from millions of loyal
  households across on-site search, display, social, connected TV, and in-store
  placements. Media scale is attached to a grocery relationship, not separate
  from basket economics.
- Grocery, fuel, pharmacy, eCommerce, private label, and retail media each have
  different collection, margin, working-capital, and reinvestment burdens.

## QoE and financial-shenanigans prompts

1. Reconcile grocery sales to customer sell-through, shrink, promotions,
   supplier allowances, inventory turns, payables, and cash conversion.
2. Separate Kroger Precision Marketing revenue and profit from grocery margin;
   test advertiser collection, measurement, privacy, incremental spend, and
   the cost of maintaining first-party data and digital reach.
3. Test eCommerce economics after picking, delivery, fulfillment, substitutions,
   returns, pharmacy, and customer-acquisition costs rather than using growth
   alone.
4. Keep fuel, pharmacy reimbursement, inflation, merger effects, and alternative
   profit add-backs separate from durable retail cash.
5. Treat dividends, buybacks, and merger funding as residual claims only after
   stores, distribution, inventory, labor, debt, and technology investment are
   funded.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what identical-store growth, grocery
margin, loyalty retention, retail-media yield, eCommerce contribution, pharmacy
economics, reinvestment rate, and cost of capital the valuation requires. The
Lyn Alden-style stress test asks whether household budgets, food prices, labor,
supplier terms, pharmacy reimbursement, rates, and data monetization remain
liquid through a low-margin retail shock without confusing basket volume or
media profit with durable owner cash.

## Promotion boundary

`kroger-qualified; grocery-and-retail-media-cash-open; no-ranking`

Promotion requires same-entity joins from basket and media activity to
collection, supplier settlement, inventory, fulfillment, pharmacy and fuel
economics, store and technology reinvestment, debt, claims, and diluted common
residual. Sales, eCommerce growth, retail-media profit, adjusted FIFO profit,
OCF, FCF, and repurchases remain diagnostic inputs.

## Sources

- [Kroger company packet](../../extracted/services/retail-grocery-stores/the-kroger-company/company-packet.md)
- [Kroger source ledger](../../extracted/services/retail-grocery-stores/the-kroger-company/source-ledger.md)
