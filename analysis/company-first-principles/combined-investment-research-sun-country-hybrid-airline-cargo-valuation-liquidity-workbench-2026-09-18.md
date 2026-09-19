# Sun Country hybrid airline and cargo valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Sun Country from an airline packet into a company-specific valuation object. It separates scheduled passenger, charter, and Amazon cargo flying, then tests fleet and crew utilization, seasonality, fuel, labor, aircraft ownership and leases, maintenance, customer concentration, merger consideration, debt, and diluted common residual. It does not treat passengers, departures, cargo revenue, adjusted EBITDA, operating cash flow, or merger value as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Sun Country | Hybrid fleet-utilization cash after passenger fares, charter settlement, Amazon cargo flying, aircraft and crew deployment, fuel, labor, maintenance, leases, fleet renewal, merger costs, debt, and dilution | Aircraft ownership and leases, engine and airframe maintenance, crew training, labor, airport and handling contracts, technology, fuel hedging, seasonal working capital, and fleet transition | Passenger demand or yield decline, Amazon concentration or contract change, fuel shock, labor disruption, aircraft grounding, maintenance event, merger failure, lease/debt refinancing, or dilution | Cargo and charter growth continues while passenger yield, Amazon contract economics, fleet utilization, maintenance cash, merger consideration, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2025 operating revenue was about `$1.127B`, operating income about `$100.6M`, and net income about `$52.8M`.
- At year-end 2025 the fleet included `47` passenger aircraft, `20` cargo aircraft flying for Amazon, and `3` aircraft leased to unaffiliated airlines.
- FY2025 revenue mix was about `$971.7M` passenger and `$155.0M` cargo; fleet allocation and customer concentration matter more than total revenue alone.
- Q1 2026 revenue was about `$338.4M`, net income about `$24.1M`, adjusted net income about `$32.9M`, and adjusted EBITDA about `$73.5M`; cargo revenue rose `64%` year over year to about `$46.1M` while scheduled departures fell `14%`.
- Sun Country entered an Allegiant merger agreement on `2026-01-11`; the transaction introduces a legal, financing, approval, and common-owner consideration perimeter that must remain separate from standalone airline cash.

## QoE and financial-shenanigans prompts

1. Separate passenger fare, charter, cargo, and aircraft-lease revenue, then reconcile flying hours, departures, load factors, yield, cargo contract terms, and collections.
2. Test Amazon concentration, minimum-volume or termination rights, aircraft deployment, and customer economics; cargo expansion is not automatically diversified cash.
3. Keep fuel, labor, maintenance, aircraft ownership, leases, airport fees, and crew utilization in the recurring-cost bridge; adjusted operating metrics may exclude real cash burdens.
4. Reconcile aircraft deliveries, retirements, maintenance reserves, debt, lease liabilities, seasonal working capital, and merger costs before treating operating cash flow as owner cash.
5. Separate merger consideration, approval costs, break fees, financing, and post-close ownership from standalone dividends, repurchases, or per-share metrics.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what passenger yield, charter utilization, cargo contract margin, fleet turns, maintenance burden, reinvestment rate, and cost of capital the valuation requires. The Lyn Alden-style stress test asks whether travel demand, Amazon logistics, fuel, labor, aircraft availability, and financing remain liquid through a recession or operational disruption, especially while merger terms are unsettled.

## Promotion boundary

`sun-country-hybrid-airline-qualified; fleet-utilization-amazon-and-merger-cash-open; no-ranking`

Promotion requires same-entity joins from passenger, charter, and cargo flying to customer collections, fleet and crew utilization, maintenance settlement, fuel and labor cost, lease and debt obligations, merger consideration, claims, funding, and diluted common residual. Passengers, departures, cargo revenue, adjusted EBITDA, OCF, guidance, and merger value remain diagnostic inputs.

## Sources

- [Sun Country company packet](../../extracted/services/air-delivery-freight-services/sun-country-airlines-holdings-inc/company-packet.md)
- [Sun Country source ledger](../../extracted/services/air-delivery-freight-services/sun-country-airlines-holdings-inc/source-ledger.md)

