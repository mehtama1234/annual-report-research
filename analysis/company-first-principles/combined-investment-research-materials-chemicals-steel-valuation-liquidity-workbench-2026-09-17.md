# Materials, chemicals, and steel valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench moves Ecolab, Sherwin-Williams, and Nucor from physical-input
and cash-quality diagnostics into company-specific valuation, reinvestment,
liquidity, and thesis-breaker objects. It keeps embedded service chemistry,
coatings/distribution, and steel capacity separate; the cohort is not a
multiple or normalized owner-cash ranking.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Ecolab | Recurring chemistry/service cash after labor, equipment, working capital, acquisition integration, and dilution | Dispensing/equipment, R&D, service labor, receivables, inventory, Ovivo integration, debt, and SBC | Industrial/customer slowdown, water/compliance spending, input inflation, collection, acquisition financing, and rates | Revenue or adjusted margin rises while retention, service cash, working-capital settlement, acquisition returns, or diluted residual weakens |
| Sherwin-Williams | Brand/coatings/distribution cash after channel inventory, raw materials, stores, acquisitions, and claims | Stores, technology, distribution, manufacturing, working capital, acquisitions, leases, and debt; capex classification must be restored | Construction/renovation slowdown, contractor/dealer stress, raw-material inflation, inventory destocking, rates, and acquisition funding | Pricing or sales growth continues while channel inventory, collections, margins, acquisition return, or common cash deteriorates |
| Nucor | Through-cycle steel spread and utilization cash after scrap, energy, maintenance, expansion, environmental claims, and dilution | `$2.50B` 2026 capex estimate, West Virginia sheet mill, NTS expansion, maintenance, energy, labor, and working capital | Steel-price and spread compression, scrap/energy inflation, project ramp, customer credit, debt, environmental costs, and shareholder returns | Shipments or EBITDA rise while reserve/asset utilization, working-capital settlement, project return, or post-replacement residual weakens |

## Current evidence anchors

- Ecolab H1 2026 OCF was `$1.1754B`, capex `$588.6M`, receivables used
  `$197.0M`, inventory used `$131.4M`, SBC `$75.1M`, and one-time
  equity-incentive payments `$60M` tied to the Ovivo acquisition.
- Nucor H1 2026 OCF was `$2.286B`, capex `$1.232B`, receivables used `$952M`,
  inventory used `$560M`, and payables supplied `$454M`; its 2026 capex
  estimate is `$2.50B` and West Virginia/NTS projects remain utilization and
  return objects.
- The FY2025 comparison keeps Sherwin-Williams' missing selected capex
  classification open; Ecolab's `$1.621B` acquisition/investment burden and
  Nucor's `$3.422B` PP&E line prevent mechanical OCF screens from becoming
  owner cash.

## QoE and financial-shenanigans prompts

1. Separate price, volume, mix, service, raw-material pass-through, and
   acquisition effects from recurring collection and margin.
2. Reconcile receivables, inventory, payables, rebates, channel inventory,
   scrap, energy, and customer programs over matched periods.
3. Split maintenance, expansion, equipment, store, technology, and project
   capital; do not substitute guidance for paid capex.
4. Test acquisition integration, goodwill, restructuring, environmental/legal
   claims, service labor, SBC, debt, and dilution in the common-owner bridge.
5. Treat buybacks, dividends, and favorable price/mix as residual claims or
   cycle outputs, not proof of durable surplus cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what recurring service cash,
price/volume/mix, steel spread, utilization, reinvestment rate, acquisition
return, terminal growth, and cost of capital the market price requires. The
Lyn Alden-style stress test asks whether industrial recession, input and energy
inflation, rates, customer credit, inventory destocking, and acquisition
financing can be absorbed without eroding the control point.

## Promotion boundary

`materials-qualified; cycle-and-acquisition-return-open; no-ranking`

Promotion requires same-entity, same-period joins from product/service activity
to collections, working-capital settlement, maintenance/growth capital,
acquisition return, environmental/debt claims, dilution, and common-owner
residual. Revenue, volume, EBITDA, OCF, price/mix, buybacks, and dividends
remain diagnostic inputs.

## September 18, 2026 valuation expectation refresh

The current market snapshot reports Ecolab equity value of approximately
`$76.042B` at `$269.46` per share, Sherwin-Williams equity value of
approximately `$78.900B` at `$320.73`, and Nucor equity value of approximately
`$56.755B` at `$248.38`. Only Ecolab and Nucor have a current comparable
H1 OCF-and-capex screen in this workbench; Sherwin-Williams' selected current
capex denominator remains open.

| Company | Screen denominator | Mechanical market-cap / screen | Boundary |
| --- | ---: | ---: | --- |
| Ecolab | `($1.1754B - $0.5886B) × 2 = $1.1736B` | `64.8x` | H1 receivables and inventory used `$328.4M`; acquisition and service/equipment burden remain open |
| Nucor | `($2.286B - $1.232B) × 2 = $2.108B` | `26.9x` | H1 working capital invested `$1.512B`; `$130M` raw-material refund and project ramp make the cycle denominator unstable |
| Sherwin-Williams | No current comparable screen | — | Current capex, acquisition-return, channel-inventory, and owner-cash denominator remain unjoined |

These are expectation screens, not normalized owner-cash multiples. Ecolab's
screen still contains working-capital funding, SBC, acquisition/integration,
and service-equipment burden; Nucor's contains a steel-cycle working-capital
investment and a named non-recurring procurement refund. The cross-company
spread is not a ranking across incompatible control points.

## Sources

- [Materials/chemicals/steel Q2 cash-quality refresh](combined-investment-research-materials-chemicals-steel-q2-2026-cash-quality-refresh-2026-09-17.md)
- [Materials specialty chemicals and steel synthesis](annual-report-materials-specialty-chemicals-steel-first-principles-synthesis-pass-1-2026-09-17.md)
- [Materials Q2 structured table](data/combined-investment-research-materials-chemicals-steel-q2-2026-cash-quality-refresh-2026-09-17.csv)
