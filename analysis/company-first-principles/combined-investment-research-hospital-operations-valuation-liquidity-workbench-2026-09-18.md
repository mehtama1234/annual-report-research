# Hospital operations valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves HCA Healthcare from provider-demand evidence into a
company-specific care-delivery valuation object. It tests hospital throughput,
staffed capacity, payer adjudication, labor, supplies, capital renewal,
acquisitions, debt, noncontrolling interests, and common-owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment/denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| HCA Healthcare | Hospital and ambulatory care cash after admissions/acuity, payer collection, labor, supplies, uncompensated care, maintenance/growth capex, acquisitions, NCI, interest, debt, and dilution | Facilities, staffed beds, ambulatory/service-line capacity, technology, clinical labor, supplies, physician arrangements, acquisitions, and common capital | Payer mix/reimbursement, labor scarcity, occupancy/acuity, patient collections, litigation/regulation, debt/refinancing, or NCI claims | Revenue/admissions and operating cash rise while payer concessions, labor, capacity renewal, receivables, NCI, leverage, or diluted residual deteriorate |

## Current evidence anchors

- HCA FY2025 revenue was `$75.600B`, operating cash flow `$12.636B`, PP&E
  capex `$4.944B`, and post-capex diagnostic `$7.692B`.
- HCA spent `$397M` on acquisitions and distributed `$827M` to NCI in 2025;
  interest was `$2.207B` and income taxes `$1.740B`. A more conservative common
  screen must subtract these claims before dividends or repurchases.
- Approximately `$1.3B` of deferred tax payments were paid in Q4 after severe
  weather timing, so the cash increase is not a pure capacity signal.
- Year-end total debt was `$46.492B` against `$1.040B` cash. HCA repurchased
  `$2.558B` in Q4 and received a new `$10B` authorization after year-end.

## QoE and financial-shenanigans prompts

1. Reconcile admissions, acuity, service mix, outpatient growth, negotiated
   rates, payer mix, concessions, patient responsibility, and collections.
2. Track salary/benefit growth, contract labor, vacancy, productivity, physician
   arrangements, supplies, and staffed-bed capacity.
3. Separate replacement, regulatory, information-system, and growth capex; tie
   each project to added capacity, procedures, reimbursement, margin, and cash.
4. Keep acquisitions, NCI distributions, interest, taxes, weather/tax timing,
   litigation, and debt visible before treating OCF-less-capex as owner cash.
5. Treat admissions, adjusted EBITDA, operating cash, dividends, and buybacks
   as diagnostic or residual measures until payer collection and common claims
   are joined.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what admissions, acuity, payer rates,
labor productivity, service mix, renewal capex, acquisition return, leverage,
and cost of equity the valuation requires. The Lyn Alden-style stress test asks
whether labor, insurers, public budgets, household affordability, litigation,
and rates can interrupt cash before hospital capacity earns its return.

## Promotion boundary

`hospital-operations-qualified; payer-labor-capex-and-leverage-open; no-ranking`

Promotion requires same-entity, same-period joins from patient care through
payer adjudication and collection, labor/supply settlement, required capacity
renewal, acquisitions, NCI, interest, debt, legal claims, and diluted common
residual. Admissions, revenue, occupancy, adjusted EBITDA, reported OCF,
dividends, and buybacks remain diagnostic inputs.

## Sources

- [HCA deep company packet](../deep-company-pages/hca-healthcare-inc.md)
