# Con Edison urban regulated utility valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Consolidated Edison from an electric-utility packet into a company-specific valuation object. It separates regulated electric, gas, steam, transmission, and holding-company activity, then tests rate-base recovery, customer collections, affordability, reliability, resilience, substations, capital programs, forward equity, debt, and diluted common residual. It does not treat utility EPS, rate-base growth, capital spending, operating cash flow, dividends, or share issuance as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Consolidated Edison | Urban regulated utility cash after electric/gas/steam service, rate-plan recovery, customer collections, reliability, resilience, electrification, transmission, capex, holding-company debt, equity funding, and dilution | Substations, grid hardening, storm and reliability work, gas and steam infrastructure, electrification, maintenance/growth capex, regulatory compliance, pension/claims, interest, and equity issuance | Rate-case disallowance, affordability pressure, storm or reliability event, customer arrears, capex overruns, regulatory lag, rates, debt refinancing, forward equity, or dilution | EPS and rate-base growth continue while collections, approved recovery, capex completion, customer affordability, financing burden, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2025 net income for common stock was about `$2.023B` or `$5.66` per share; adjusted earnings were about `$2.038B` or `$5.70` per share.
- Q2 2026 net income for common stock and adjusted earnings were both about `$308M` or `$0.83` per share; full-year adjusted EPS guidance was `$6.00`–`$6.20`.
- Con Edison’s regulated footprint includes Consolidated Edison Company of New York, Orange and Rockland Utilities, and Con Edison Transmission, serving New York City, Westchester, southeastern New York, and northern New Jersey.
- Management described a multi-year capital program of about `$6.595B` in 2026, `$6.759B` in 2027, and `$24.339B` in aggregate for 2028–2030, with `28` new substations expected in service by 2035.
- Q1 2026 included a settled forward sale agreement for `7M` shares and total consideration of about `$357.5M` from the MVP interest sale; equity funding and non-core proceeds must remain distinct from regulated cash generation.

## QoE and financial-shenanigans prompts

1. Reconcile customer bills, collections, arrears, regulatory assets/liabilities, rate-plan recovery, allowed returns, and actual cash receipt; approved investment is not automatically collected owner cash.
2. Separate electric, gas, steam, transmission, and holding-company activity; rate, weather, fuel, and capex mechanisms differ by entity and service.
3. Test capital programs for maintenance versus growth, construction-in-progress, completion, prudence, disallowance, and regulatory lag.
4. Keep affordability programs, reliability, storm, environmental, pension, and safety obligations visible as claims on common cash.
5. Reconcile utility OCF, capex, dividends, forward equity, debt, interest, non-core asset proceeds, SBC, and diluted shares before treating EPS or payouts as owner cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what rate-base growth, allowed return, customer growth, capital program, recovery lag, payout ratio, and cost of equity the valuation requires. The Lyn Alden-style stress test asks whether a dense urban utility can fund resilience and electrification through rate, affordability, storm, regulatory, and refinancing shocks without converting rate-base rhetoric into distributable common cash.

## Promotion boundary

`con-ed-urban-regulated-qualified; ratebase-recovery-affordability-and-owner-cash-open; no-ranking`

Promotion requires same-entity joins from service and rate-base investment to customer collections, approved recovery, capex completion, regulatory assets/liabilities, reliability and storm claims, funding, debt, equity issuance, dividends, and diluted common residual. Utility EPS, rate-base growth, capex, OCF, guidance, dividends, and share issuance remain diagnostic inputs.

## Sources

- [Con Edison company packet](../../extracted/utilities/electric-utilities/consolidated-edison-inc/company-packet.md)
- [Con Edison source ledger](../../extracted/utilities/electric-utilities/consolidated-edison-inc/source-ledger.md)

