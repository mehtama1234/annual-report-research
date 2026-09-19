# Milestone jewelry retail valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Signet Jewelers from occasion-demand evidence into a
company-specific valuation and liquidity object. It separates milestone and
identity demand, price/AUR, jewelry inventory, gold and diamond costs, store
and digital conversion, and portfolio transition from general consumer goods
and home-furnishings retail.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Signet Jewelers | Occasion and jewelry-brand cash after unit demand, AUR, gross margin, inventory, markdowns, stores, digital fulfillment, commodity/tariff cost, restructuring, debt, SBC, and dilution | Diamond/gold inventory, stores, technology, marketing, James Allen repositioning, fulfillment, working capital, portfolio investment, and common capital | Milestone affordability, gold/diamond inflation, tariffs, traffic/unit decline, inventory aging, markdowns, store transition, debt, or dilution | AUR, same-store sales, adjusted EPS, or FCF rise while units, inventory turns, gross margin, maintenance cash, or diluted common residual deteriorate |

## Current evidence anchors

- FY26 sales were `$6.81B`, full-year same-store sales rose `1.3%`, and reported FY26 free cash flow was `$525M`.
- Q1 FY27 same-store sales rose `1.8%`; merchandise AUR rose about `5%`, but adjusted operating income `$78.6M` substantially exceeded reported operating income `$36.9M`.
- Q3 FY26 same-store sales rose `3.0%`; Bridal AUR rose `6%` and Fashion AUR `8%`. AUR improvement must be separated from units, traffic, and affordability.
- Q4 FY26 sales were `$2.35B`, but same-store sales fell `0.7%`, showing that the full-year recovery was not uniform.
- The FY26 FCF figure lacks a complete locally preserved line-by-line owner-cash bridge; inventory, capex, leases, restructuring, debt, repurchases, SBC, and dilution remain open denominators.

## QoE and financial-shenanigans prompts

1. Join same-store sales and AUR to transactions, units, traffic, category mix, gross margin, and promotions; price-led growth is not automatically demand strength.
2. Track inventory turns, age, markdowns, vendor terms, gold/diamond cost, tariffs, and category availability; inventory reduction can be either discipline or under-assortment.
3. Reconcile reported operating income and FCF to restructuring, James Allen transition, store/digital investment, leases, SBC, debt, and diluted shares.
4. Separate Bridal, Fashion, gifting, self-purchase, and specialty-brand economics; occasion resilience does not eliminate discretionary-budget risk.
5. Test store productivity, digital conversion, fulfillment, returns, marketing, and customer acquisition after portfolio repositioning.
6. Treat adjusted EPS, adjusted operating income, and buybacks as diagnostic until recurring cash per diluted share improves after inventory and maintenance capital.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what same-store transactions, AUR,
gross margin, inventory turns, store productivity, digital conversion,
maintenance spending, restructuring, and diluted-share outcome the valuation
requires. The Lyn Alden-style stress test asks whether households can fund
milestone purchases as wages, rates, gold/diamond costs, tariffs, and competing
experiences pressure purchasing power.

## Promotion boundary

`milestone-jewelry-retail-qualified; inventory-and-common-cash-open; no-ranking`

Promotion requires same-entity, same-period joins from occasion demand and
transactions to inventory turns, markdowns, commodity cost, gross margin,
store/digital investment, restructuring, debt, SBC, repurchases, and diluted
common residual. AUR, same-store sales, adjusted earnings, FCF, and buybacks
remain diagnostic inputs.

## Sources

- [Signet deep company page](../deep-company-pages/signet-jewelers-limited.md)
- [Signet company packet](../../extracted/services/jewelry-stores/signet-jewelers-limited/company-packet.md)
- [Signet source ledger](../../extracted/services/jewelry-stores/signet-jewelers-limited/source-ledger.md)
