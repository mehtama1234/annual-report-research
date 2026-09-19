# Restaurant franchising valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench moves restaurant franchising from control-point and mechanical
cash diagnostics into company-specific valuation, reinvestment, liquidity, and
thesis-breaker objects. It keeps the FY2025 CAVA, Restaurant Brands
International, Wingstop, and Yum cohort separate from the current-period
McDonald's and Chipotle refresh. It does not rank franchisors or treat
systemwide sales as corporate revenue.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| CAVA | Corporate-store and franchise expansion cash after unit maturity, support, leases, and dilution | New-store build, remodel, labor/food, technology, SBC, and working capital | Store ramp shortfall, food/labor inflation, lease burden, support cash, or funding cost | Unit growth continues while mature-store productivity, cash conversion, or diluted residual weakens |
| Restaurant Brands International | Royalty, fee, property, advertising, and company-store cash after brand/support and acquisition claims | Franchise support, remodel/new-unit requirements, acquisitions, debt, leases, and advertising-fund perimeter | Franchisee distress, refinancing, currency, supplier inflation, or acquisition integration | System sales and royalties rise while franchisee health, collections, support, or per-share cash deteriorates |
| Wingstop | Highly franchised royalty and fee cash after support, repurchases, SBC, and diluted shares | Franchisee unit economics, technology, support, corporate capex, SBC replacement, and buybacks | Franchisee financing, traffic/affordability, fee collection, and repurchase funding | System growth persists while royalty collection, franchisee health, or diluted cash fails to support capital returns |
| Yum | Multi-brand royalty and company-store cash after refranchising, advertising, debt, and claims | Remodel/new-unit, franchisee support, acquisitions, technology, leases, and capital returns | Franchisee credit, China/market exposure, food/labor costs, rates, and debt | Refranchising or system sales lift margins while franchisee economics, collections, or owner cash weaken |
| McDonald's | Franchised rent/royalty/fee cash plus company-store cash, with the `$34.451B` franchised-sales base kept outside reported revenue | Franchisee-funded reinvestment versus corporate remodel, technology, company-store, lease, and support burden | Franchisee affordability and financing, traffic, rent collection, wage/food inflation, and debt | Franchised sales or reported royalties grow while franchisee reinvestment, collection, or common residual deteriorates |
| Chipotle | Company-operated restaurant cash after food, labor, real estate, new units, remodels, technology, and dilution | New-unit cohort, restaurant maintenance, labor/food, technology, and repurchase/SBC burden | Traffic, wage/food inflation, unit ramp, real-estate cost, and cash-funded repurchases | Restaurant growth continues while mature-unit margins, cash per unit, or diluted residual declines |

## Current evidence anchors

- The FY2025 cohort has reported OCF and PP&E screens, but advertising-fund
  collections/use, royalty collection, franchisee health, support, and
  maintenance-versus-growth capital remain unjoined.
- McDonald's H1 2026 refresh reports `$5.222B` OCF, `$1.516B` PP&E spending,
  `$34.451B` Q2 franchised sales, `44,016` franchised restaurants, and `2,012`
  company-operated restaurants. Franchised sales are an economic base, not
  McDonald's reported revenue or owner cash.
- Chipotle's H1 2026 refresh reports `$1.332B` OCF, `$397.601M` PP&E spending,
  `4,186` owned restaurants, and `15` international partner-operated
  restaurants. Its burden surface is more corporate-store intensive and is not
  comparable to the franchised cohort without a model-specific bridge.

## QoE and financial-shenanigans prompts

1. Reconcile systemwide sales, franchisee sales, royalty/rent/fee revenue, and
   actual collections; do not substitute unit count or system sales for cash.
2. Keep advertising-fund inflows, restricted assets/liabilities, and spending
   separate from franchisor revenue and common-owner cash.
3. Separate refranchising gains and property proceeds from recurring royalty or
   company-store economics.
4. Test franchisee closures, receivables, support, required remodels, and
   franchisee financing as early indicators of burden transfer.
5. Split maintenance, remodel, new-store, technology, and corporate capital;
   OCF less total PP&E is only a diagnostic.
6. Reconcile acquisitions, leases, taxes, debt, SBC, repurchases, dividends,
   and diluted shares before calling any residual owner cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what royalty rate, collection rate,
unit growth, mature-store margin, reinvestment rate, support burden, and cost of
capital the current price requires. The Lyn Alden-style stress test asks whether
traffic, affordability, wages, food inputs, lease costs, franchisee financing,
and refinancing conditions can support both the franchisor and the operating
franchise network.

## Promotion boundary

`restaurant-franchise-qualified; valuation-liquidity-open; no-ranking`

Promotion requires same-entity, same-period joins from franchisee or
company-store activity to collections, advertising-fund settlement, required
reinvestment, support/lease/tax costs, debt, dilution, and a common-owner
residual. Systemwide sales, royalties, reported OCF, repurchases, and
franchising margins remain diagnostic inputs.

## Sources

- [Restaurant franchising first-principles synthesis](annual-report-restaurant-franchise-first-principles-synthesis-pass-1-2026-09-17.md)
- [Restaurant-franchise owner-cash promotion workbench](combined-investment-research-restaurant-franchise-owner-cash-promotion-workbench-2026-09-17.md)
- [Restaurant current-period refresh](combined-investment-research-restaurant-current-period-refresh-2026-09-17.md)
- [Restaurant-franchise filing evidence panel](combined-investment-research-restaurant-franchise-filing-evidence-panel-2026-09-17.md)
