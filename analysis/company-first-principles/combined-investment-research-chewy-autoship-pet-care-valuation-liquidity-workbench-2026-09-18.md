# Chewy autoship and pet-care commerce valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Chewy from a digital-commerce packet into a company-specific valuation object. It separates merchandise, Autoship, pharmacy and prescriptions, active customers, net sales per customer, fulfillment, inventory, customer acquisition, service attachment, working capital, debt, and diluted common residual. It does not treat active customers, Autoship share, net sales, adjusted EBITDA, free cash flow, or buybacks as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Chewy | Pet-care relationship cash after merchandise sell-through, Autoship retention, pharmacy and prescription collections, fulfillment, inventory, customer acquisition, service support, debt, and dilution | Fulfillment centers, inventory, shipping, digital product and account systems, pharmacy compliance, customer acquisition and retention, working capital, technology, and repurchases | Household trade-down, pet-product margin pressure, Autoship churn, customer-acquisition inflation, shipping cost, inventory obsolescence, pharmacy/regulatory issue, debt, or dilution | Active customers and Autoship sales rise while retention, gross margin, net sales per customer, pharmacy collections, fulfillment cost, inventory turns, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2025 net sales reached about `$12.60B`, adjusted EBITDA about `$719.2M`, record free cash flow about `$562M`, and active customers `21.3M`.
- Q1 2026 net sales increased `7.7%` to about `$3.36B`, gross margin rose `50` bps to `30.1%`, net income was about `$94.8M`, and adjusted EBITDA about `$253.1M` or `7.5%` margin.
- Q3 2025 Autoship customer sales represented about `84%` of net sales, net sales per active customer were about `$595`, and active customers added about `250,000` sequentially.
- Chewy serves about `4,000` brands across roughly `190,000` products and service offerings, with merchandise, health, wellness, and prescription surfaces connected through digital accounts.
- The platform’s economics depend on repeat pet-parent behavior, but recurring behavior still carries fulfillment, shipping, inventory, customer-service, pharmacy, and acquisition costs.

## QoE and financial-shenanigans prompts

1. Reconcile active customers, Autoship orders, churn, frequency, net sales per customer, promotions, returns, and collections; an account is not recurring cash without retained contribution.
2. Separate food, hard goods, pharmacy, prescriptions, services, private-label, and other categories; gross margin and regulatory burdens differ across them.
3. Test fulfillment-center utilization, shipping cost, inventory turns, vendor terms, stock-outs, markdowns, and product obsolescence against reported margin and free cash flow.
4. Keep customer acquisition, retention incentives, loyalty benefits, pharmacy compliance, and digital-product spending visible as required reinvestment.
5. Reconcile adjusted EBITDA, free cash flow, working capital, debt, SBC, dividends, repurchases, and diluted shares before treating customer growth or buybacks as owner cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what active-customer retention, Autoship frequency, net sales per customer, gross margin, pharmacy attachment, fulfillment efficiency, reinvestment rate, and cost of capital the valuation requires. The Lyn Alden-style stress test asks whether households protect pet spending through a downturn, whether shipping and acquisition costs consume the recurring relationship, and whether inventory, rates, or regulatory events weaken liquidity before the platform earns its cost of capital.

## Promotion boundary

`chewy-autoship-petcare-qualified; retention-pharmacy-and-owner-cash-open; no-ranking`

Promotion requires same-entity joins from customers and Autoship to order collection, retention, pharmacy settlement, fulfillment, inventory turns, customer-acquisition cost, required digital and compliance spend, debt, claims, funding, and diluted common residual. Active customers, Autoship share, net sales, adjusted EBITDA, FCF, guidance, and buybacks remain diagnostic inputs.

## Sources

- [Chewy company packet](../../extracted/services/retail-catalog-mail-order-houses/chewy-inc/company-packet.md)
- [Chewy source ledger](../../extracted/services/retail-catalog-mail-order-houses/chewy-inc/source-ledger.md)

