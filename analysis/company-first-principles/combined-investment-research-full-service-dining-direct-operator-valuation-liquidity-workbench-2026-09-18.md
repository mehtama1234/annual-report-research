# Full-service dining direct-operator valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Darden Restaurants from current-period restaurant evidence
into a company-specific valuation, reinvestment, acquisition, lease, and
liquidity test. It keeps company-operated restaurant economics separate from
franchise royalties and does not treat same-restaurant sales, adjusted EPS,
EBITDA, or buybacks as normalized common-owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Darden | Mature brand-portfolio cash after guest traffic, food, labor, occupancy, maintenance/remodel capital, new units, Chuy's integration, leases, debt, taxes, and dilution | Maintenance and remodel capex per existing unit, new-store cost and ramp, acquisition price and integration cash, labor and technology investment, leases, and common capital | Household trade-down, traffic decline, wage/food inflation, service deterioration, Chuy's underperformance, lease/debt pressure, or deferred maintenance | Same-restaurant sales rise only through price, traffic or service weakens, new-unit returns fall, Chuy's requires repeated cash, or per-share residual deteriorates despite adjusted EPS growth |

## Current evidence anchors

- FY2025 sales were `$12.1B`, blended same-restaurant sales rose `2.0%`, and
  adjusted diluted EPS was `$9.553`; Darden served more than `440M` guests,
  added `25` net restaurants, and acquired `103` Chuy's restaurants.
- FY2025 capital return was about `$1.1B`, including `$659M` of dividends and
  `$418M` of repurchases; those uses require a maintenance-capital and
  acquisition-cash test before being called surplus.
- Q1 FY2026 sales rose `10.4%` to `$3.0B` and blended same-restaurant sales rose
  `4.7%`, but brand results differed and the comparison included Chuy's and
  recently opened restaurants.
- Darden owned and operated `2,202` restaurants at May 31, 2026, versus `167`
  franchised restaurants. FY2026 operating cash was `$1.853B`, land/building/
  equipment purchases were `$734M`, and the resulting `$1.119B` screen remains
  before leases, debt, taxes, dilution, and the maintenance/growth split.

## QoE and financial-shenanigans prompts

1. Decompose same-restaurant sales into traffic, price, mix, calendar, and
   channel; price-led sales are not proof of durable demand.
2. Separate company-operated sales and costs from franchise royalties; the
   former carries food, labor, occupancy, repair, and remodel burdens.
3. Reconcile adjusted EPS and EBITDA to Chuy's transaction/integration costs,
   closed restaurants, divestitures, recurring remodels, and buybacks.
4. Split land/building/equipment spending into maintenance, remodel, technology,
   safety, and growth capital, then test mature-unit cash returns.
5. Track Chuy's acquired sales, margin, labor, leases, remodel needs, and
   integration cash against the purchase price and diluted share count.
6. Test labor hours, turnover, management coverage, food waste, occupancy, and
   service quality; cost cuts that impair the guest experience are deferred
   revenue destruction.
7. Charge leases, debt, interest, taxes, and diluted shares before promoting
   the residual to common-owner cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what guest traffic, check growth,
brand-level margins, mature unit returns, maintenance capital, Chuy's return,
and cost of capital the equity price requires. The Lyn Alden-style stress test
asks whether household liquidity, wage and food inflation, occupancy costs,
commodity cycles, and debt obligations can be absorbed without sacrificing
service or maintenance.

## Promotion boundary

`full-service-dining-qualified; traffic-unit-return-and-lease-cash-open; no-ranking`

Promotion requires same-period joins from guest traffic and check to
restaurant-level margin, maintenance/growth capital, lease and debt burden,
Chuy's integration return, and diluted common residual. Same-restaurant sales,
adjusted EPS, EBITDA, OCF, dividends, and repurchases remain diagnostic inputs.

## Sources

- [Darden deep company page](../deep-company-pages/darden-restaurants-inc.md)
- [Darden company packet](../../extracted/services/restaurants/darden-restaurants-inc/company-packet.md)
- [Darden source ledger](../../extracted/services/restaurants/darden-restaurants-inc/source-ledger.md)
