# First Solar thin-film manufacturing and contracted-energy-hardware valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves First Solar from a solar packet into a company-specific valuation object. It separates thin-film module manufacturing, factory ramp, contracted backlog, customer deposits, delivery and termination risk, domestic policy support, third-party volume, working capital, underutilization, capex, and diluted common residual. It does not treat gigawatts of backlog, module volume, adjusted EBITDA, tax credits, net cash, or guidance as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| First Solar | Contracted utility-scale module cash after thin-film qualification, factory utilization, domestic manufacturing, customer acceptance, delivery, policy credits, warranty, capex, working capital, debt, and dilution | Louisiana and South Carolina factory ramp, production equipment, underutilization and start-up, semiconductor/material inputs, R&D, recycling, inventory, customer deposits, warranty, and maintenance/growth capex | Customer termination or renegotiation, policy/45X change, tariff or export-control shift, factory delay, module price pressure, underutilization, working-capital draw, project financing stress, or dilution | Backlog and module volume grow while customer acceptance, contract economics, tax-credit durability, factory utilization, cash conversion, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2025 net sales were about `$5.2B`, diluted EPS about `$14.21`, net cash about `$2.4B`, contracted backlog about `50.1 GW` valued at roughly `$15.0B`, and U.S. annual nameplate capacity about `13 GW`.
- Q2 2026 net sales were about `$1.06B`, net income about `$423M`, diluted EPS `$3.92`, adjusted EBITDA about `$644M`, gross and net cash about `$1.7B`, and contracted backlog `45.1 GW`.
- Q1 2026 backlog was `47.9 GW`; net cash declined from year-end because of seasonal working capital and South Carolina finishing-facility capex.
- Q2 revenue fell `4%` year over year, primarily from lower revenue associated with customer contract terminations, partially offset by higher third-party module volume.
- FY2026 guidance included net sales of about `$4.9B`–`$5.2B`, adjusted EBITDA `$2.6B`–`$2.8B`, capex `$0.8B`–`$1.0B`, and year-end net cash `$1.7B`–`$2.3B`; these ranges define expectations, not realized owner cash.

## QoE and financial-shenanigans prompts

1. Reconcile contracted gigawatts to named customer, price, delivery schedule, deposits, acceptance, termination rights, cancellation economics, and collected cash; backlog is not a receivable.
2. Separate 45X and other policy support from product margin, and test the cash timing, eligibility, transferability, and durability of credits.
3. Keep factory ramp, start-up, underutilization, production yield, warranty, recycling, and expansion capex distinct from maintenance capital and reported EBITDA.
4. Test thin-film product qualification, customer concentration, third-party volume, module pricing, input costs, tariffs, and export controls against gross margin and cash conversion.
5. Reconcile net cash, customer advances, inventory, contract assets/liabilities, tax-credit receipts, debt, SBC, and diluted shares before treating buybacks or guidance as owner cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what contracted price, module volume, factory utilization, policy-credit contribution, backlog conversion, reinvestment rate, and cost of capital the valuation requires. The Lyn Alden-style stress test asks whether utility-scale buyers and project financiers can carry long-duration module commitments through rates and policy changes, and whether factories, inventory, customer claims, or expansion capex consume liquidity before the energy-transition thesis reaches common owners.

## Promotion boundary

`first-solar-thin-film-qualified; backlog-policy-and-factory-cash-open; no-ranking`

Promotion requires same-entity joins from backlog and modules to customer acceptance, deposits, delivery, termination settlement, factory utilization, policy-credit receipt, required capex, warranty claims, funding, and diluted common residual. Gigawatts, module volume, adjusted EBITDA, tax credits, net cash, guidance, and buybacks remain diagnostic inputs.

## Sources

- [First Solar company packet](../../extracted/technology/solar/first-solar-inc/company-packet.md)
- [First Solar source ledger](../../extracted/technology/solar/first-solar-inc/source-ledger.md)

