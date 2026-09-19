# Power-grid valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench moves NextEra/FPL, AEP, and Duke from customer-cash and
regulatory-recovery diagnostics into company-specific valuation, capital,
liquidity, and thesis-breaker objects. It keeps category recovery, signed load,
and named generation projects separate because approval, capacity, funding,
billing, collection, and common-owner return are different proof objects.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| NextEra/FPL | FPL category/rate-base recovery plus NEER contracted-project cash after paid capital, tax-credit support, financing, and dilution | FPL distribution/generation, NEER development, nuclear fuel, storm, construction, and project/JV capital | Regulatory lag, construction inflation, rates, tax-credit dependence, load delay, storms, fuel, and customer affordability | Rate-base or project growth continues while billed/collected recovery, paid-capital return, or common residual weakens |
| AEP | Regulated rate-base and named large-load/tariff cash after customer obligations, construction, financing, and shared claims | `$77.937B` 2026–2030 plan, construction, generation acquisitions, nuclear fuel, customer-specific infrastructure, and working capital | Signed-load delay, collateral/payment failure, regulatory lag, rates, affordability, construction inflation, and equity dilution | Load and capital-plan growth continue without minimum-payment, billed-revenue, collection, or return support |
| Duke Energy | Regulated rate-base plus the Anderson County co-owned generation project after paid cost, tariff recovery, NCI, and debt | `$103B` 2026–2030 plan, accrued capex, generation, nuclear fuel, storm, shared ownership, and project funding | Fuel/gas access, construction inflation, regulatory lag, NCI funding, rates, customer affordability, and project delay | Project capacity or rate-base growth rises while Duke's paid cost, ownership share, customer recovery, or common return deteriorates |

## Current evidence anchors

- FPL H1 2026 OCF was `$5.388B` against `$5.780B` capex; its route has
  category-recovery and true-up evidence, but no public Distribution Inspection
  billed/collected cash or source-of-funds allocation.
- AEP H1 OCF was `$3.421B` against `$5.606B` construction spending; the lane
  includes `69 GW` of signed load through 2030, `$77.937B` of planned capital,
  `$52.836B` debt, and `$7.25B` liquidity, but not a named customer payment or
  collected project return.
- Duke H1 OCF was `$4.272B` against `$8.240B` capex; the lane includes
  `$6.464B` debt issued, `$2.827B` NCI contributions, `$2.501B` asset-sale
  proceeds, and the Anderson County project, but accrued capex and shared
  ownership prevent a simple project-to-common-cash conclusion.
- NextEra reported H1 OCF of `$7.276B` against `$19.389B` of capital
  expenditures, independent-power investments, and nuclear-fuel purchases,
  with approximately `$18.1B` net available liquidity. This is funding
  capacity and capital burden, not category-level collected customer cash.

## QoE and financial-shenanigans prompts

1. Do not treat approved recovery, signed load, rate-base growth, or project
   capacity as billed and collected revenue.
2. Reconcile cash paid, accrued capex, CWIP, AFUDC, regulatory assets/liabilities,
   in-service dates, and customer deposits.
3. Separate debt, equity/ATM, NCI, tax credits, asset sales, grants, DOE loans,
   securitizations, and parent funding from operating customer cash.
4. Join project ownership, paid cost, tariff/recovery, customer payment, and
   legal-entity residual before assigning a return to common owners.
5. Test regulatory credits, true-ups, asset-sale gains, mark-to-market items,
   fuel effects, storms, taxes, and financing costs for recurrence and timing.
6. Keep dividends and repurchases subordinate to replacement capital, debt,
   affordability, and dilution tests.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what rate-base growth, project
commencement, approved return, recovery timing, capital intensity, cost of
capital, and dilution the market price requires. The Lyn Alden-style stress
test asks whether rates, construction inflation, fuel and power access,
customer affordability, regulatory lag, load delays, and capital-market access
can support the funding path.

## Promotion boundary

`power-grid-qualified; valuation-liquidity-open; collection-and-return-open; no-ranking`

Promotion requires a same-entity, same-period category or project bridge from
approved cost or contract through paid capital, billing determinant, customer
collection, recovery, senior claims, and common-owner return. OCF, rate-base
growth, signed load, tax-credit proceeds, debt capacity, dividends, and project
capacity remain diagnostic inputs.

## Sources

- [Power-grid current-period synthesis](combined-investment-research-power-grid-current-period-synthesis-2026-09-17.md)
- [Power-grid valuation and liquidity handoff](combined-investment-research-power-grid-valuation-liquidity-handoff-2026-09-17.md)
- [Power-grid customer-cash evidence panel](combined-investment-research-power-grid-customer-cash-evidence-panel-2026-09-17.md)
- [Power-grid customer-contract receipt workbench](capital-flow-power-grid-customer-contract-receipt-workbench-pass-1.md)
