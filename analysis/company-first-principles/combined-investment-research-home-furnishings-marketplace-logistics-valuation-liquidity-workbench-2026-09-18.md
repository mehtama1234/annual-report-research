# Home-furnishings marketplace and logistics valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Wayfair from home-demand and marketplace evidence into a
company-specific valuation and liquidity object. It separates supplier access,
digital merchandising, bulky-goods delivery, fulfillment, returns, and stock
compensation from eBay's transaction marketplace, Shopify's merchant platform,
and branded home retail.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Wayfair | Retained order and supplier-network cash after advertising, payment, delivery, fulfillment, returns, customer service, logistics infrastructure, software, leases, SBC, and dilution | Customer acquisition, merchandising, catalog/data, CastleGate, Delivery Network, warehouses, technology, supplier support, working capital, and common capital | Home-demand/credit weakness, supplier failure, delivery under-pricing, returns, fixed logistics cost, tariffs, working-capital reversal, leases, or dilution | Customers, orders, gross profit, and adjusted EBITDA rise while contribution per order, repeat economics, delivery/return cost, SBC-adjusted cash, or diluted residual deteriorate |

## Current evidence anchors

- FY2025 revenue was `$12.5B` with more than `21M` active customers and more than `22,000` suppliers.
- Q2 2026 revenue was `$3.5B`, up `7.5%`; active customers were `21.7M`, orders delivered `10.6M`, gross profit `$1.054B` or `30.0%` of revenue, and adjusted EBITDA `$242M`.
- FY2025 OCF was `$534M` and PP&E purchases `$70M`, but SBC was about `$335M`; the initial residual after PP&E and SBC was about `$129M` before leases, logistics, and growth investment.
- Q2 2026 GAAP diluted EPS was a loss of `$0.01` versus adjusted diluted EPS of `$0.95`; adjusted profitability therefore requires a full reconciliation.
- CastleGate and the Wayfair Delivery Network improve delivery and supplier access but carry warehouse, labor, fleet, lease, maintenance, return, and utilization claims.

## QoE and financial-shenanigans prompts

1. Track contribution per order and active customer after advertising, payment, delivery, fulfillment, returns, support, and discounts; active customers and GMV are not owner cash.
2. Reconcile gross profit and adjusted EBITDA to GAAP operating income, OCF, SBC, capitalized software, leases, restructuring, and network capital.
3. Separate supplier-held inventory from Wayfair-funded inventory and test supplier payment terms, quality, cancellations, and returns.
4. Separate category recovery, price/mix, new customers, repeat orders, specialty brands, and share gains; do not treat outperformance as durable without cash economics.
5. Test CastleGate and Delivery Network incremental order density, delivery cost, damage, return, utilization, and capital returns.
6. Treat employee tax-withholding cash, SBC, and buybacks as common-owner claims rather than assuming repurchases prove surplus cash.
7. Keep Perigold and other specialty-brand growth separate from core Wayfair retention, acquisition cost, and fulfillment economics.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what active-customer retention, order
frequency, average order value, retained contribution, logistics utilization,
SBC-adjusted cash, and reinvestment rate the valuation requires. The Lyn
Alden-style stress test asks whether households and suppliers can fund bulky
discretionary purchases while housing, rates, tariffs, freight, and consumer
credit pressure the platform and its logistics network.

## Promotion boundary

`home-furnishings-marketplace-logistics-qualified; contribution-and-cash-open; no-ranking`

Promotion requires same-entity, same-period joins from customers and orders to
retained contribution, advertising, delivery and return cost, supplier health,
inventory/fulfillment exposure, leases, software, SBC, and diluted common
residual. Customers, orders, gross profit, adjusted EBITDA, OCF, and buybacks
remain diagnostic inputs.

## Sources

- [Wayfair deep company page](../deep-company-pages/wayfair-inc.md)
- [Wayfair company packet](../../extracted/services/home-furnishing-stores/wayfair-inc/company-packet.md)
- [Wayfair source ledger](../../extracted/services/home-furnishing-stores/wayfair-inc/source-ledger.md)
