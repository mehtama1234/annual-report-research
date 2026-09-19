# Industrial uptime valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench consolidates Sterling Infrastructure, WESCO, Fastenal, and
United Rentals into company-specific valuation, reinvestment, liquidity, and
thesis-breaker objects. It preserves the differences between project
execution, electrical distribution, recurring replenishment, and rental-fleet
access; it does not rank the cohort on mechanical cash conversion.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Sterling | Signed and collected project cash after cost-to-complete, claims, acquisitions, JV effects, debt, and dilution | Contract assets/retainage, labor/materials, fleet/property, CEC/Stone Ridge acquisition cash, and working capital | Backlog delay, estimate revisions, customer concentration, acquisition financing, rates, and cost inflation | Signed backlog grows while project collection, margin, acquired-cohort cash return, or diluted residual deteriorates |
| WESCO | Electrical distribution cash after receivables, inventory, supplier terms, acquisitions, property, leases, debt, and dilution | Distribution inventory/receivables, technology/branches, acquisitions, supplier financing, maintenance property, and working capital | Receivable/inventory funding, supplier terms, project delay, customer concentration, rates, and revolver use | Sales/backlog growth continues while working-capital conversion, gross margin, supplier settlement, or common cash weakens |
| Fastenal | Recurring replenishment, onsite, vending, and digital-channel cash after service cost, inventory, property, leases, and dilution | Inventory turns, onsite/vending deployment, branches, technology, labor/service, maintenance capital, and buybacks | Industrial slowdown, large-account mix, inventory/credit pressure, labor/service cost, rates, and capital returns | Unit/channel growth continues while service-adjusted margin, turns, collection, or diluted residual weakens |
| United Rentals | Fleet cohort lifecycle cash after utilization, rental rates, replacement capex, resale, debt, borrowing-base claims, and parent restrictions | Replacement versus growth fleet, used-equipment recovery, fleet funding, maintenance, debt, and legal availability | Utilization decline, resale haircut, borrowing-base reserves, rates, debt, parent transfer limits, and project delay | Fleet growth or reported FCF rises while legal availability, replacement coverage, utilization, or lifecycle residual deteriorates |

## Current evidence anchors

- Sterling's H1 mechanical OCF-less-capex screen was `$258.375M`; signed
  backlog and acquired backlog remain separate from funded project cash, and
  CEC/Stone Ridge acquisition contribution requires a cohort return bridge.
- WESCO's H1 OCF less property spending was `$223.5M`, with receivables up
  `$615.4M`, inventory up `$409.2M`, and payables up `$709.8M`; the balance
  bridge is a diagnostic and cannot be deducted again from OCF.
- Fastenal's H1 OCF less property spending was `$521.1M`; receivables were
  `$1,557.4M`, inventory `$1,735.2M`, and payables `$399.8M` at June 30, 2026.
- URI's H1 OCF, fleet purchases, resale, stated liquidity, ABL capacity,
  borrowing-base, and lifecycle objects remain separate; a populated
  certificate and cohort return are still missing.

## QoE and financial-shenanigans prompts

1. Separate signed backlog, unsigned awards, acquisitions, contract assets,
   retainage, inventory, receivables, and actual customer collections.
2. Do not subtract balance-sheet working-capital movements a second time from
   reported OCF.
3. Split maintenance, replacement, technology, branch, fleet, and growth
   capital; include leases, taxes, debt, SBC, NCI, and dilution.
4. Test percentage-of-completion estimates, claims, change orders, resale
   gains, supplier terms, acquisition integration, and borrowing-base reserves.
5. Treat buybacks and reported FCF as outputs requiring a senior-claim bridge,
   not proof of recurring common-owner cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what funded backlog, collection rate,
project margin, recurring replenishment, utilization, replacement rate, resale
recovery, acquisition return, and cost of capital the price requires. The Lyn
Alden-style stress test asks whether rates, infrastructure spending, customer
liquidity, labor/material inflation, inventory funding, fleet financing, and
credit tightening can be absorbed before the operating control point converts
to cash.

## Promotion boundary

`industrial-uptime-qualified; denominator-and-lifecycle-open; no-ranking`

Promotion requires same-entity, same-period joins from demand or backlog to
collection, working-capital settlement, maintenance/replacement capital,
acquisition return, lease/tax/debt claims, legal availability, dilution, and
common-owner residual. Backlog, OCF-less-capex, utilization, resale proceeds,
repurchases, and reported FCF remain diagnostic inputs.

## Sources

- [Industrial uptime valuation and macro handoff](combined-investment-research-industrial-uptime-valuation-macro-handoff-2026-09-17.md)
- [Industrial uptime conversion screen](combined-investment-research-industrial-uptime-conversion-screen-2026-09-17.md)
- [Industrial uptime thesis-breaker register](combined-investment-research-industrial-uptime-thesis-breaker-register-2026-09-17.md)
- [Industrial uptime structured valuation workbench](data/combined-investment-research-industrial-uptime-valuation-workbench-2026-09-17.csv)
