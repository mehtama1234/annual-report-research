# Walmart omnichannel ecosystem valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Walmart from broad mass-retail evidence into a
company-specific valuation object. It separates merchandise, eCommerce,
membership, advertising, marketplace, fulfillment services, financial services,
inventory, supplier terms, stores, labor, international operations, debt, and
diluted common residual. It does not treat revenue, eCommerce growth,
advertising growth, membership fees, adjusted operating income, operating cash
flow, free cash flow, or repurchases as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Walmart | Omnichannel mass-retail cash after basket sell-through, supplier settlement, eCommerce fulfillment, membership billing, advertising collection, marketplace and financial-services settlement, stores, labor, inventory, debt, and dilution | Stores and distribution, eCommerce fulfillment, technology and data, Walmart Connect, marketplace, membership, private label, working capital, labor, international expansion, and SBC replacement | Consumer trade-down or mix shift, supplier terms, labor inflation, eCommerce fulfillment burden, ad-market slowdown, membership churn, international or FX stress, debt refinancing, or dilution | Ecosystem revenue and adjusted profit grow while merchandise margin, collection, fulfillment economics, ad yield, membership retention, required capex, or diluted per-share cash deteriorate |

## Current evidence anchors

- Q1 2026 total revenues increased `7.3%`, operating income `5.0%`, operating
  cash flow was `$4.7B`, global advertising grew `37%`, Walmart U.S. eCommerce
  grew `26%`, and global membership fee income grew `17.4%`.
- Q4 2025 operating cash flow was `$41.6B` and free cash flow `$14.9B`; global
  advertising grew `37%`, Walmart U.S. eCommerce `27%`, and membership fee
  revenue `15.1%`.
- Q3 2025 global advertising grew `53%`, eCommerce `28%`, and management
  described digital advertising and marketplace as higher-margin ecosystem areas.
- Walmart explicitly frames membership, advertising, marketplace, fulfillment,
  and financial services as mutually reinforcing pieces of its omnichannel model;
  each has separate settlement and reinvestment burdens.

## QoE and financial-shenanigans prompts

1. Reconcile merchandise sales to customer sell-through, inventory, shrink,
   promotions, supplier terms, private label, and cash conversion.
2. Separate Walmart Connect from merchandise margin; test advertiser collection,
   measurement, privacy, incremental ad-tech cost, and the durability of yield.
3. Test eCommerce and marketplace economics after picking, delivery,
   fulfillment, returns, seller settlement, and customer acquisition.
4. Keep membership, financial services, FX, international mix, and one-time
   adjustments separate from recurring retail cash.
5. Treat dividends, buybacks, and acquisitions as residual claims only after
   stores, inventory, labor, fulfillment, technology, and debt are funded.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what traffic, basket, eCommerce
contribution, membership retention, ad yield, marketplace take rate, fulfillment
cost, reinvestment rate, and cost of capital the valuation requires. The Lyn
Alden-style stress test asks whether household budgets, supplier terms, labor,
food inflation, rates, ad demand, and global logistics remain liquid through a
low-margin retail shock without confusing ecosystem growth with owner cash.

## Promotion boundary

`walmart-qualified; omnichannel-ecosystem-cash-open; no-ranking`

Promotion requires same-entity joins from merchandise and platform activity to
collection, supplier settlement, inventory, fulfillment, membership, ad and
marketplace settlement, store and technology reinvestment, debt, claims, and
diluted common residual. Revenue, eCommerce, advertising, membership fees,
adjusted income, OCF, FCF, and repurchases remain diagnostic inputs.

## Sources

- [Walmart company packet](../../extracted/services/discount-variety-stores/walmart-inc/company-packet.md)
- [Walmart source ledger](../../extracted/services/discount-variety-stores/walmart-inc/source-ledger.md)
