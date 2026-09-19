# Integrated oil and gas valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench moves ConocoPhillips and Exxon Mobil from current-period
production and cash diagnostics into company-specific valuation, replacement,
liquidity, and thesis-breaker objects. It keeps upstream, refining, chemicals,
trading, LNG, and integrated-company economics visible rather than pooling
them into a single commodity multiple or owner-cash ranking.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| ConocoPhillips | Through-cycle upstream and LNG cash after realized-price/netback, decline, royalties, taxes, replacement capital, and diluted claims | Maintenance drilling, development, exploration, LNG/vessel commitments, contingent consideration, abandonment, and working capital | Lower prices, production decline, LNG delay, service-cost inflation, debt/refinancing, and partner/royalty claims | OCF or shareholder returns rise while production, reserve replacement, realized netback, or diluted residual weakens |
| Exxon Mobil | Integrated upstream/refining/chemicals/trading cash after segment margins, replacement capital, disruption, claims, and common allocation | `$12.997B` H1 PP&E additions and `$12.974B` company-defined cash capex must be separated into upstream, refining, chemicals, sustaining, and growth objects | Commodity-price shock, refinery turnaround, geopolitical disruption, working-capital absorption, identified losses, debt, and dividend/buyback pressure | Integrated earnings or production rise while reserve quality, segment margin, replacement burden, or common cash deteriorates |

## Current evidence anchors

- ConocoPhillips H1 2026 OCF was `$11.729B`; production was `2.278M BOE/d`
  versus `2.391M BOE/d`; capital and investments were `$5.972B`; repurchases
  were `$3.006B`; dividends were `$2.057B`; and the final Surmont contingent
  consideration payment was `$81M`.
- Exxon Mobil H1 2026 OCF was `$32.260B`; production was `4.554M BOE/d`
  versus `4.591M BOE/d`; refinery throughput was `3.529M bpd`; PP&E additions
  were `$12.997B`; company-defined cash capex was `$12.974B`, including
  `$10.664B` upstream; dividends were `$8.633B`; and common-stock purchases
  were `$10.007B`.
- Exxon separately reported a `$3.857B` H1 operational working-capital use,
  a `$1.199B` upstream identified-item loss, and a `$1.886B` Energy Products
  identified-item loss. Those are reconciliation inputs, not automatically
  recurring or automatically removable items.

## QoE and financial-shenanigans prompts

1. Decompose price, volume, mix, realized netback, hedging, inventory, and
   working-capital timing before treating OCF growth as operating improvement.
2. Join production and throughput to reserves, decline, finding/development
   cost, and paid replacement capital; a capital program is not paid capex.
3. Separate maintenance, development, exploration, LNG, refining, chemicals,
   and megaproject spending before calculating owner cash.
4. Test disruption, impairment, derivative, divestiture, contingent-payment,
   environmental, and abandonment items for recurrence and cash timing.
5. Keep partner/NCI claims, royalties, taxes, debt, and dilution in the
   common-owner bridge.
6. Treat dividends and repurchases as residual claims and funding uses, not as
   proof that commodity-cycle cash is durable.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what realized price, production or
throughput, netback, margin, reserve life, replacement rate, terminal growth,
and cost of capital the market price requires. The Lyn Alden-style stress test
asks whether lower commodity prices, inflation, rates, geopolitical shocks,
working-capital absorption, project delays, and refinancing can be survived
without sacrificing reserve quality or common-owner claims.

## Promotion boundary

`integrated-oil-gas-qualified; cycle-and-replacement-open; no-ranking`

Promotion requires same-period production and realized-price decomposition,
reserve replacement, paid maintenance/development capital, project economics,
claims, debt, tax, dilution, and through-cycle common-owner cash. Production,
integrated segment earnings, mechanical OCF-less-capex, dividends, and
repurchases remain diagnostic inputs.

## Sources

- [Integrated oil and gas Q2 cash-quality refresh](combined-investment-research-integrated-oil-gas-q2-2026-cash-quality-refresh-2026-09-17.md)
- [Integrated oil and gas first-principles synthesis](annual-report-integrated-oil-gas-first-principles-synthesis-pass-1-2026-09-17.md)
- [ConocoPhillips Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1163165/000116316526000032/cop-20260630.htm)
- [Exxon Mobil Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/34088/000003408826000093/xom-20260630.htm)
