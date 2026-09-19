# Chemed hospice and service-route valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Chemed from current-period evidence into a company-specific
valuation, reimbursement, labor, route-density, and common-owner cash test. It keeps
VITAS hospice and Roto-Rooter separate rather than treating a mixed parent as a
generic healthcare-services or recurring-revenue company.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Chemed | Collected VITAS hospice cash after admissions, census, acuity, Medicare reimbursement and Cap, clinical labor, facilities, compliance, taxes, debt, and dilution, plus separately collected Roto-Rooter route cash | Hospice staffing, admissions, clinical systems, compliance, local market density, Roto-Rooter technicians, vehicles, dispatch, and working capital | Medicare Cap or reimbursement pressure, labor scarcity, census decline, referral slowdown, acuity shift, regulatory claims, route inefficiency, debt, or dilution | Admissions and census rise while Cap exposure, revenue per day, labor cost, collections, parent allocation, or diluted common residual deteriorate |

## Current evidence anchors

- Q2 2026 VITAS net patient revenue was `$443.3M`, up `11.9%`; average daily census was `23,687`, up `6.1%`; admissions were `19,125`, up `9.0%`.
- Q2 adjusted EBITDA excluding Medicare Cap was `$80.6M`, up `20.6%`.
- Q1 2026 VITAS net patient revenue was `$420.0M`; average daily census was `22,723`; admissions were `19,394`; adjusted EBITDA excluding Medicare Cap was `$70.8M`.
- Q4 2025 VITAS net patient revenue was `$418.8M`; average daily census was `22,462`; admissions were `17,419`; adjusted EBITDA excluding Medicare Cap was `$91.6M`.
- Chemed also owns Roto-Rooter, so consolidated revenue, parent buybacks, and guidance cannot be used as a clean proxy for hospice owner cash.

## QoE and financial-shenanigans prompts

1. Reconcile VITAS admissions to average daily census, length of stay, acuity,
   revenue per day, payer mix, Medicare Cap exposure, claims, denials, and cash
   collections.
2. Keep VITAS staffing, clinician retention, compliance, facilities, referral
   relationships, and market build-out in the reinvestment denominator.
3. Separate Roto-Rooter route density, technician labor, vehicles, dispatch,
   franchise or local-market economics, and working capital from hospice results.
4. Test whether adjusted EBITDA excluding Medicare Cap removes a recurring
   reimbursement burden rather than a genuinely unusual item.
5. Reconcile parent-level debt, taxes, buybacks, SBC, segment transfers, claims,
   and diluted shares before treating consolidated cash as common-owner surplus.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what hospice admissions, census, acuity,
revenue per day, Cap burden, labor productivity, route density, reinvestment rate,
and cost of capital the valuation requires. The Lyn Alden-style stress test asks
whether aging demand, Medicare policy, labor availability, family preferences,
inflation, and local service demand can support liquidity through a reimbursement
and labor cycle.

## Promotion boundary

`chemed-vitas-and-route-services-qualified; reimbursement-segment-and-owner-cash-open; no-ranking`

Promotion requires same-entity, same-period joins from VITAS admissions/census and
Roto-Rooter route activity to payer collections, Medicare Cap, labor and fleet
spend, compliance claims, debt, parent allocation, and diluted common residual.
Admissions, census, adjusted EBITDA, guidance, consolidated revenue, and buybacks
remain diagnostic inputs.

## Sources

- [Chemed company packet](../../extracted/healthcare/specialized-health-services/chemed-corporation/company-packet.md)
- [Chemed source ledger](../../extracted/healthcare/specialized-health-services/chemed-corporation/source-ledger.md)

