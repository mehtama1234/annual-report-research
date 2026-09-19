# Urban Outfitters and Nuuly lifestyle valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Urban Outfitters from current-period evidence into a company-specific valuation object. It tests Anthropologie, Free People, Urban Outfitters, Nuuly, Retail, Subscription, Wholesale, inventory, rental utilization, returns, tariffs, stores, digital demand, leases, debt, and diluted common residual. It does not pool URBN with single-banner apparel, department stores, or off-price retailers.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Urban Outfitters | Multi-banner lifestyle and wardrobe-access cash after brand demand, retail comps, Nuuly subscription and rental utilization, wholesale, inventory, returns, stores, digital, taxes, debt, and dilution | Product and brand investment, stores, digital, rental fleet, cleaning and logistics, inventory, fulfillment, leases, debt, and shares | Fashion-cycle failure, rental churn, returns and damage, tariff/input costs, inventory aging, banner concentration, or lease burden | Revenue and comps rise while Nuuly retention/utilization, banner margins, inventory quality, rental economics, cash conversion, or diluted common residual deteriorate |

## Current evidence anchors

- FY2025 net sales were about `$6.17B`, up `11.1%`; Subscription sales rose `50.2%`; Retail comparable sales rose `6.0%`.
- FY27 Q1 revenue was about `$1.48B`, up `11.4%`; Retail comps rose `5.6%`; Subscription sales rose `34.5%`; net income was about `$115.7M`.
- FY27 Q1 comps were `9.8%` for FP Group, `9.3%` for Urban Outfitters, and `1.9%` for Anthropologie.
- The model combines multi-banner retail, wholesale, digital and stores, and Nuuly’s monthly rental-subscription layer; early inventory receipts and tariffs are current-period quality risks.

## QoE and financial-shenanigans prompts

1. Separate Anthropologie, Free People, Urban Outfitters, Nuuly, Retail, Subscription, Wholesale, store, and digital economics.
2. Test Nuuly subscriber retention, rental utilization, returns, cleaning, damage, acquisition cost, and inventory replacement rather than treating subscription revenue as pure software-like recurring cash.
3. Reconcile comps and margin to inventory, markdowns, tariffs, freight, leases, fulfillment, working capital, and dilution.
4. Determine whether portfolio growth is broad-based or increasingly dependent on one banner or the rental segment.

## Damodaran/Lyn Alden application

The expectation test asks what banner growth, Nuuly retention and utilization, rental margin, inventory turns, brand investment, store productivity, leverage, and cost of capital are embedded in the valuation. The stress test asks whether fashion cycles, tariffs, returns, shipping, rental logistics, leases, and discretionary budgets support cash after replacement and funding needs.

## Promotion boundary

`urban-outfitters-qualified; nuuly-utilization-and-banner-breadth-open; no-ranking`

Promotion requires same-entity joins from each banner and Nuuly to collection, retention, rental utilization, inventory and returns, store and digital productivity, leases, debt, claims, and diluted common residual. Revenue, comps, subscription growth, EPS, OCF, FCF, guidance, and buybacks remain diagnostic inputs.

## Sources

- [Urban Outfitters company packet](../../extracted/services/apparel-stores/urban-outfitters-inc/company-packet.md)
- [Urban Outfitters source ledger](../../extracted/services/apparel-stores/urban-outfitters-inc/source-ledger.md)
