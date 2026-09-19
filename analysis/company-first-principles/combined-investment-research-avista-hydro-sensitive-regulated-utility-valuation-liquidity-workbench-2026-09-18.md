# Hydro-sensitive regulated utility valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Avista from current-period utility evidence into a company-specific valuation, rate-case, hydro, customer-concentration, capital, and owner-cash test. It treats Avista as a smaller Pacific Northwest mixed electric-and-gas utility, not as a generic large-load or merchant-power proxy.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Avista | Collected regulated electric-and-gas utility cash after hydro and wholesale exposure, weather, rate-base investment, wildfire and reliability obligations, customer affordability, debt, and diluted common claims | Utility capital expenditures, transmission and distribution, generation and hydro maintenance, wildfire and safety work, rate-case spending, working capital, interest, and dividends | Hydro and weather variance, wholesale prices, large-customer procurement changes, affordability, regulatory lag, wildfire, capex funding, refinancing, and dilution | Utility EPS and guidance rise while hydro-normal assumptions, customer retention, rate recovery, collection, capital execution, debt service, or diluted common residual deteriorate |

## Current evidence anchors

- Avista serves about `429,000` electric customers and `386,000` natural-gas customers across Washington, Idaho, and Oregon, with AEL&P adding a smaller Alaska electric business.
- Utilities capital expenditures were about `$553M` in `2025`, while management's `2026` capital-expenditure assumption was about `$615M`.
- Q2 `2026` GAAP EPS were `$0.43` and non-GAAP utility EPS were `$0.29`; management reaffirmed `2026` utility guidance of `$2.52` to `$2.72`.
- Q1 `2026` GAAP EPS were `$1.11` and non-GAAP utility EPS were `$1.10`, with about `$147M` of first-quarter utility capex.
- Full-year `2025` GAAP EPS were `$2.38` and non-GAAP utility EPS were `$2.55`; management disclosed a roughly `$0.12` 2026 guidance headwind from a large industrial customer returning to market procurement sooner than expected.

## QoE and financial-shenanigans prompts

1. Reconcile utility revenue and EPS to rate-base additions, rate-case recovery, customer collection, hydro output, weather normalization, wholesale purchases, and fuel or power costs.
2. Keep the electric, gas, Alaska, hydro, and large-customer cohorts separate; a smaller-system customer departure can change guidance without proving broad demand deterioration.
3. Test capex through named projects, maintenance versus growth allocation, regulatory recovery, construction timing, financing, and service reliability rather than treating all utility investment as value-creating.
4. Separate non-GAAP utility EPS, weather effects, wildfire and safety costs, regulatory timing, and wholesale volatility from recurring collected common-owner cash.
5. Reconcile debt, interest, dividends, equity issuance, tax, and dilution before promoting rate-base growth or guidance into normalized owner cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what customer growth, rate-base expansion, allowed returns, hydro and weather assumptions, regulatory recovery, capital intensity, and cost of capital the valuation requires. The Lyn Alden-style stress test asks whether affordability, wildfire, drought or hydro variability, wholesale prices, industrial customer procurement, rates, and funding needs impair the utility's ability to convert regulated investment into durable common-owner cash.

## Promotion boundary

`avista-hydro-sensitive-qualified; regulated-collection-and-owner-cash-open; no-ranking`

Promotion requires same-entity, same-period joins from rate-base and hydro operations to customer collection, named capex recovery, fuel and purchased-power cost, debt service, taxes, dividends, and diluted common residual. Utility EPS, guidance, capex, customer counts, hydro output, and non-GAAP measures remain diagnostic inputs.

## Sources

- [Avista company packet](../../extracted/utilities/diversified-utilities/avista-corp/company-packet.md)
- [Avista source ledger](../../extracted/utilities/diversified-utilities/avista-corp/source-ledger.md)

