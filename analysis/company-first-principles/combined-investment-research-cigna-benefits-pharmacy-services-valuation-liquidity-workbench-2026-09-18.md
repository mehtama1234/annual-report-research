# Cigna benefits and pharmacy-services valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves The Cigna Group from generic managed-care evidence into a
company-specific valuation object. It separates Cigna Healthcare, Evernorth
Health Services, pharmacy-benefit and specialty services, employer and
government lives, medical-cost trend, drug rebates, claims reserves, client
retention, capital, debt, regulation, and diluted common residual. It does not
treat covered lives, revenue, adjusted income, medical margin, operating cash
flow, free cash flow, or repurchases as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Cigna | Health-benefits and pharmacy-services cash after premiums and client collections, medical claims, medical-cost trend, pharmacy rebates and dispensing, specialty-care services, network costs, capital, debt, and dilution | Claims reserves, care and specialty programs, pharmacy infrastructure, technology and navigation, client acquisition and retention, regulatory capital, working capital, acquisitions, and SBC replacement | Medical-cost spike, drug-pricing or rebate pressure, client churn, utilization shift, reimbursement or regulatory change, claims reserve weakness, debt refinancing, cyber or legal event, or dilution | Revenue and adjusted earnings grow while medical-cost ratio, claims reserves, pharmacy economics, rebate quality, client retention, capital, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2025 total revenues increased `11%` to about `$274.9B`; shareholders' net
  income was about `$6.0B`; adjusted income from operations was about `$8.0B`.
- Q2 2026 revenue was about `$71.668B`, shareholders' net income `$1.66B`, and
  adjusted income from operations `$2.054B`; SG&A expense ratio was about `4.8%`.
- Q1 2026 adjusted income from operations grew `12%`; debt-to-capitalization was
  about `42.3%`. Cigna Healthcare and Evernorth both contributed to the model.
- The company combines employer and health-benefit administration with pharmacy,
  specialty, and care-navigation services; claims and rebate settlement remain
  the central cash-quality tests.

## QoE and financial-shenanigans prompts

1. Reconcile premiums and client fees to covered lives, retention, claims,
   reserves, utilization, medical-cost trend, and cash collection.
2. Separate Cigna Healthcare from Evernorth; bridge pharmacy revenue and rebates
   to dispensing, specialty-drug costs, client contracts, and settlement.
3. Test adjusted earnings against claims development, reserve releases, one-time
   settlements, risk adjustment, and regulatory or capital requirements.
4. Connect technology, navigation, specialty-care, and network investment to
   client retention, medical outcomes, operating cost, and durable margin.
5. Treat dividends, buybacks, and acquisitions as residual claims only after
   claims, reserves, capital, debt, and regulatory obligations are funded.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what enrollment, retention, medical-cost
trend, pharmacy spread, rebate economics, SG&A efficiency, capital requirement,
reinvestment rate, and cost of equity the valuation requires. The Lyn
Alden-style stress test asks whether employment, drug prices, utilization, rates,
regulation, claims, capital, and client liquidity remain solvent through a
health-benefits shock without confusing premium volume with owner cash.

## Promotion boundary

`cigna-qualified; benefits-and-pharmacy-services-cash-open; no-ranking`

Promotion requires same-entity joins from premiums and pharmacy activity to
collection, claims and reserves, medical-cost trend, rebate and dispensing
settlement, client retention, capital, debt, claims, and diluted common
residual. Covered lives, revenue, adjusted earnings, OCF, FCF, and repurchases
remain diagnostic inputs.

## Sources

- [Cigna company packet](../../extracted/healthcare/managed-health-care/the-cigna-group/company-packet.md)
- [Cigna source ledger](../../extracted/healthcare/managed-health-care/the-cigna-group/source-ledger.md)
