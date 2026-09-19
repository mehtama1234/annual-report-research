# Senior-housing healthcare REIT valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Welltower from aging-demand and property-growth evidence
into a company-specific valuation and liquidity object. It separates senior-
housing operating exposure, operator health, occupancy, property capital,
acquisition yields, debt, and dilution from lodging REITs, agency mortgage
REITs, and healthcare operators.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Welltower | Senior-housing and healthcare property cash after occupancy, rates, operator coverage, property maintenance, development/acquisition capital, debt, preferred claims, and dilution | Property renewal, life-safety and room capital, operator support, development, acquisitions, lease-up, asset management, debt, equity issuance, and common capital | Occupancy or resident-affordability decline, operator failure, labor/insurance cost, cap-rate expansion, debt refinancing, development delay, or dilution | Normalized FFO, same-store NOI, and investment growth rise while operator coverage, recurring property cash, per-share value, leverage, or asset returns deteriorate |

## Current evidence anchors

- Q2 2026 normalized FFO was `$1.60` per diluted share; total portfolio same-store NOI grew `15.5%`, senior-housing operating NOI `20.5%`, and operating same-store revenue `9.2%`.
- Q4 2025 senior-housing operating same-store NOI grew `20.4%`, with occupancy up about `400` basis points; recovery growth must be separated from through-cycle growth.
- FY2025 net investment activity was roughly `$11B`; year-end net debt to adjusted EBITDA was about `3.0x`.
- Q2 2026 net income attributable to common stockholders was `$0.61` per diluted share versus normalized FFO of `$1.60`; FFO is useful but not final owner cash.
- Current open denominators include operator coverage, resident affordability, recurring maintenance capital, acquisition yields, development lease-up, cap rates, debt maturities, preferred claims, and dilution.

## QoE and financial-shenanigans prompts

1. Reconcile normalized FFO to recurring property maintenance/replacement capital, operator support, interest, preferred claims, and diluted common cash.
2. Separate same-store occupancy recovery, rate, care mix, acquisitions, development, and asset transfers; do not capitalize a depressed-base rebound as perpetual growth.
3. Track operator revenue, staffing, coverage, concessions, bad debt, resident affordability, and service quality; contractual rent does not eliminate operator burden.
4. Test acquisition and development yields after financing, lease-up, stabilization, property condition, and recurring capital.
5. Separate asset-value and fair-value changes from cash; rising FFO can coexist with cap-rate expansion and falling NAV.
6. Include secured debt, maturities, fixed/floating rates, preferred claims, joint ventures, equity issuance, and dilution in per-share value.
7. Treat investment volume, normalized FFO, NOI, and dividends as diagnostic until property-level cash and recurring-capital joins are evidenced.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what normalized occupancy, revenue per
unit, same-store NOI, operator coverage, recurring capital, acquisition yield,
development return, leverage, and cost of capital the equity value requires.
The Lyn Alden-style stress test asks whether residents, operators, lenders, and
the REIT can fund housing and care through higher rates, labor costs, insurance,
cap-rate expansion, and resident-affordability pressure.

## Promotion boundary

`senior-housing-healthcare-reit-qualified; operator-capital-and-common-cash-open; no-ranking`

Promotion requires same-entity, same-period joins from occupancy and property
NOI to operator coverage, resident collection, recurring capital, acquisition/
development return, debt, preferred claims, NAV, and diluted common residual.
Normalized FFO, same-store NOI, occupancy, investment activity, and dividends
remain diagnostic inputs.

## Sources

- [Welltower deep company page](../deep-company-pages/welltower-inc.md)
- [Welltower company packet](../../extracted/real-estate/reit-healthcare-facilities/welltower-inc/company-packet.md)
- [Welltower source ledger](../../extracted/real-estate/reit-healthcare-facilities/welltower-inc/source-ledger.md)
