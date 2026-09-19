# Integrated steel, automotive contracts, and fixed-cost cycle valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Cleveland-Cliffs from the annual-report archive into a
company-specific iron-ore, pellet, DRI, scrap, integrated-steel, downstream,
automotive-contract, fixed-cost, and common-owner residual test. It keeps
Cleveland-Cliffs separate from Nucor's electric-arc model, mining producers,
chemical manufacturers, and steel-service distribution.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Cleveland-Cliffs | Through-cycle realized steel cash after contract lag, automotive and industrial volume, product mix, iron ore/pellets/DRI, scrap, energy, labor, utilization, downstream conversion, pension/OPEB, debt, capex, and dilution | Mines, pellets, DRI, blast furnaces, finishing lines, tooling, maintenance, environmental work, downstream conversion, working capital, and reliability | Automotive production shock, fixed-price contract lag, slab-contract burden, energy/weather, plant outage, steel-price decline, labor/pension, debt/refinancing, or capex deferral | Shipments and adjusted EBITDA improve while contract realization, unit cost, utilization, fixed-cost absorption, liquidity, debt, or diluted common residual deteriorate |

## Current evidence anchors

- FY2025 revenue was approximately `$18.6B`, GAAP net loss `$1.4B`, and adjusted EBITDA only `$37M`; liquidity ended the year around `$3.3B`.
- Q2 2026 revenue was `$5.2B`, GAAP net loss `$134M`, adjusted net loss `$115M`, adjusted EBITDA `$286M`, OCF `$230M`, liquidity `$3.1B`, and steel product sales `4.0M` net tons.
- Q2 2026 steelmaking revenue mix was approximately `33%` distributors/converters, `29%` direct automotive, `28%` infrastructure/manufacturing, and `10%` steel producers; product mix was `45%` hot-rolled, `31%` coated, `15%` cold-rolled, `4%` plate, `4%` stainless/electrical, and `1%` other.
- Approximately `35%` to `40%` of flat-rolled shipments are under fixed-price contracts. Price recovery therefore lags spot markets and depends on contract resets, product mix, automotive schedules, and downstream value-add.
- Q1 2026 included approximately `$80M` of one-time extreme-cold energy cost; full-year 2026 guidance included `16.5M` to `17.0M` net tons, about `$700M` capex, and approximately `$125M` cash pension/OPEB payments.

## QoE and financial-shenanigans prompts

1. Reconcile shipments through product mix, contract price, spot/index exposure,
   automotive schedules, distributor inventory, scrap, iron ore, pellets, and DRI.
2. Separate adjusted EBITDA from weather/energy items, slab-contract effects,
   labor, pension/OPEB, environmental claims, restructuring, and plant outages.
3. Test utilization and fixed-cost absorption by blast furnace, finishing line,
   mine/pellet/DRI asset, and downstream conversion rather than using volume alone.
4. Roll automotive contract lag, customer concentration, receivables, inventory,
   debt maturities, liquidity, capex, and cost-to-complete across the cycle.
5. Treat shipments, adjusted EBITDA, OCF, price recovery, dividends, and buybacks
   as diagnostic until full-cycle common cash per diluted share is evidenced.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what through-cycle steel prices,
contract reset, shipment volume, utilization, unit cost, downstream mix, capex,
pension, debt cost, and cost of capital the equity value requires. The Lyn
Alden-style stress test asks whether automotive demand, energy, labor, rates,
trade policy, industrial affordability, and refinancing preserve liquidity across
a high-fixed-cost steel downturn.

## Promotion boundary

`cleveland-cliffs-integrated-steel-qualified; contract-cycle-fixed-cost-and-owner-cash-open; no-ranking`

Promotion requires same-entity, same-period joins from steel shipments and
contracts to realized price, utilization, unit cost, working capital, pension/
OPEB, capex, debt, taxes, and diluted common residual. Revenue, shipments,
adjusted EBITDA, OCF, price recovery, liquidity, dividends, and buybacks remain
diagnostic inputs.

## Sources

- [Cleveland-Cliffs company packet](../../extracted/basic-materials/steel-iron/cleveland-cliffs-inc/company-packet.md)
- [Cleveland-Cliffs source ledger](../../extracted/basic-materials/steel-iron/cleveland-cliffs-inc/source-ledger.md)
- [Cleveland-Cliffs SEC filings](https://www.sec.gov/edgar/browse/?CIK=764065&owner=exclude)
