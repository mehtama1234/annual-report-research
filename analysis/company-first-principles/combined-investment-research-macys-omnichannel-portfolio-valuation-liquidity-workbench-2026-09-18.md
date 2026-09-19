# Macy's omnichannel portfolio and retail-credit valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Macy's from a department-store packet into a company-specific valuation object. It separates Macy's, Bloomingdale's, Bluemercury, merchandise sell-through, digital and marketplace activity, Macy's Media Network, credit-card revenue, inventory, markdowns, stores, leases, real estate, debt, and diluted common residual. It does not treat comparable sales, adjusted EBITDA, credit-card revenue, media revenue, operating cash flow, or buybacks as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Macy's | Omnichannel portfolio cash after merchandise sell-through, retailer inventory, markdowns, banners, marketplace and media collections, credit-card economics, stores, leases, real estate, debt, and dilution | Inventory and working capital, store maintenance and remodels, digital/marketplace technology, media and credit infrastructure, brand support, leases, real-estate obligations, debt, and repurchases | Middle-market trade-down, inventory build, markdown pressure, credit losses, consumer delinquency, digital acquisition cost, mall/store traffic, lease or debt refinancing, or dilution | Comparable sales and attached revenue grow while sell-through, markdowns, inventory turns, credit performance, media/marketplace collections, lease burden, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2025 net sales were about `$21.8B`, other revenue about `$857M`, net credit-card revenue about `$669M`, Macy's Media Network revenue about `$188M`, and year-end cash about `$1.2B`.
- FY2025 comparable sales increased `1.5%`; Bloomingdale's and Bluemercury grew faster than the Macy's nameplate, showing portfolio mix rather than one-banner recovery.
- Q1 2026 total revenue was about `$4.892B`, net sales about `$4.7B`, GAAP diluted EPS `$0.23`, adjusted diluted EPS `$0.13`, and adjusted EBITDA about `$290M`.
- Q1 comparable sales increased `3.0%`; Bloomingdale's increased `10.2%`, Bluemercury `6.4%`, Macy's `1.6%`; credit-card revenue was `$172M`, other revenue `$210M`, and Macy's Media Network `$38M`.
- FY2025 included `$448M` returned to shareholders; capital returns must be tested against inventory, lease, credit, real-estate, and debt needs rather than treated as proof of surplus merchandise cash.

## QoE and financial-shenanigans prompts

1. Reconcile owned, licensed, marketplace, digital, and store sales to customer sell-through, retailer inventory, returns, promotions, markdowns, and cash collections.
2. Keep Macy's, Bloomingdale's, Bluemercury, credit card, media, and marketplace economics separate; portfolio mix can improve while the core store economics remain weak.
3. Test credit-card revenue against receivables, charge-offs, delinquencies, funding, partner economics, and regulatory obligations rather than valuing it as fee-like retail revenue.
4. Keep Macy's Media Network and marketplace growth separate from advertiser/merchant collection, fulfillment, technology, and customer-acquisition costs.
5. Reconcile inventory, leases, stores, real-estate sales or proceeds, debt, pension/claims, SBC, dividends, repurchases, and diluted shares before accepting adjusted EBITDA or capital returns as owner cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what comparable-sales growth, gross margin, markdown rate, inventory turns, banner mix, credit yield/loss, media and marketplace monetization, lease burden, reinvestment rate, and cost of capital the valuation requires. The Lyn Alden-style stress test asks whether middle-market households trade down, whether inventory and mall/store obligations trap cash, and whether credit losses, rates, leases, or real-estate financing overwhelm improvement in the customer relationship stack.

## Promotion boundary

`macys-omnichannel-portfolio-qualified; sellthrough-credit-and-realestate-cash-open; no-ranking`

Promotion requires same-entity joins from merchandise and attached revenue to sell-through, collections, inventory, markdowns, credit-card receivables and losses, media/marketplace settlement, leases, real-estate obligations, debt, claims, funding, and diluted common residual. Comparable sales, adjusted EBITDA, credit-card revenue, media revenue, OCF, guidance, and buybacks remain diagnostic inputs.

## Sources

- [Macy's company packet](../../extracted/consumer-goods/department-stores/macys-inc/company-packet.md)
- [Macy's source ledger](../../extracted/consumer-goods/department-stores/macys-inc/source-ledger.md)

