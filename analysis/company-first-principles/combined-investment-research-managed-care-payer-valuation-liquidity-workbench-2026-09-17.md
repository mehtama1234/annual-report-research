# Managed-care payer valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench moves UnitedHealth and Cigna from managed-care company analyses
into company-specific valuation, reinvestment, liquidity, and thesis-breaker
objects. It keeps risk-bearing insurance, medical claims, pharmacy benefits,
care services, reserves, policy, and trust costs separate from healthcare
distribution and provider cash models.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| UnitedHealth | Benefits risk plus Optum care/pharmacy/services cash after medical-cost trend, claims, reserve development, cyber, policy, and diluted claims | Medical claims, provider payments, pharmacy, care delivery, technology/cyber, prior authorization, capital, debt, and dilution | Medical-cost trend, Medicare/Medicaid funding, cyber, policy, trust, reserve development, provider relations, and liquidity | Revenue/enrollment and adjusted EPS rise while medical cost, claims payable, reserve quality, cyber/trust cost, or diluted residual deteriorates |
| Cigna | Benefits underwriting plus Evernorth pharmacy/services cash after drug cost, rebates, client retention, claims, PBM scrutiny, and dilution | Claims, pharmacy inventory/rebates, specialty therapies, network/services, SG&A, technology, acquisitions, debt, and diluted shares | Medical-cost trend, PBM regulation, client loss, specialty-drug cost, member access, rebates, and financing | Adjusted earnings and client scale rise while claims, pharmacy economics, access/regulatory burden, or diluted common cash weakens |

## Current evidence anchors

- UnitedHealth FY2025 revenue was `$447.6B`; Q2 2026 revenue was `$112.0B`,
  earnings from operations `$8.0B`, net margin `4.9%`, and adjusted EPS `$6.38`;
  2026 adjusted EPS guidance was `$19.50-$20.00`.
- Cigna FY2025 revenue increased `11%` to about `$274.9B`, with adjusted income
  from operations about `$8.0B`; Q2 2026 revenue was about `$71.668B` and
  adjusted income from operations about `$2.054B`.
- Cigna's Q2 adjusted SG&A was near `4.6%`, and full-year 2026 adjusted income
  from operations outlook was raised to at least `$30.45` per share.

## QoE and financial-shenanigans prompts

1. Reconcile premiums, claims incurred, claims paid, unpaid claims, IBNR,
   reserve development, provider payments, and receivables; adjusted EPS is not
   collected owner cash.
2. Separate medical-cost trend, pharmacy rebates, specialty-drug economics,
   risk adjustment, government funding, client retention, and SG&A efficiency.
3. Carry cyber, prior-authorization, transparency, regulatory, trust, and
   remediation costs as operating burdens, not only narrative risks.
4. Keep Optum/Evernorth services, insurer legal entities, provider payments,
   parent cash, debt, and common-owner residual from being pooled.
5. Test capital, reserve adequacy, debt, acquisitions, SBC, and dilution before
   promoting buybacks or adjusted earnings.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what premium/member growth, medical
loss ratio, claims timing, pharmacy spread, retention, SG&A, reinvestment, and
cost of capital the valuation requires. The Lyn Alden-style stress test asks
whether medical inflation, labor, policy, rates, government budgets, drug
prices, cyber costs, and member affordability impair liquidity.

## Promotion boundary

`managed-care-qualified; claims-pharmacy-and-legal-entity-cash-open; no-ranking`

Promotion requires same-period premium or service collection, claims paid and
reserve settlement, pharmacy economics, risk/legal-entity allocation,
maintenance technology/cyber cost, debt, SBC, and diluted common-owner
residual. Revenue, membership, MCR, adjusted EPS, SG&A, and reported OCF remain
diagnostic inputs.

## Sources

- [UnitedHealth company analysis](healthcare/managed-health-care/unitedhealth-group-inc/company-analysis.md)
- [Cigna company analysis](healthcare/managed-health-care/the-cigna-group/company-analysis.md)
