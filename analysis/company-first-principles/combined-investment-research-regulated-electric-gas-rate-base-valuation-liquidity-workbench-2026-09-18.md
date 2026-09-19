# Regulated electric/gas rate-base valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Fortis from regulated-utility and capital-plan evidence
into a company-specific valuation and liquidity perimeter. It keeps electric
and gas rate base, regulatory recovery, construction work in progress, allowed
returns, project approval, financing, customer affordability, storm/wildfire,
currency, subsidiary capital, debt, dividends, and diluted common-owner cash
separate from American Water's water-only model and merchant-power companies.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Fortis regulated electric/gas utilities | Collected regulated earnings and common cash after placed-in-service rate base, maintenance and growth capital, regulatory lag, customer contributions, subsidiary debt, parent financing, storms, environmental costs, dividends, and dilution | Electric/gas generation, transmission, distribution, storage, information systems, storm hardening, environmental work, construction work in progress, acquisitions, and common capital | Disallowance, regulatory lag, construction inflation, affordability politics, wildfire/storm, rates, currency, debt/refinancing, equity issuance, or project delay | Rate base and capital plan grow while approved recovery, earned return, per-share earnings, customer collection, credit quality, or diluted common residual deteriorate |

## Current evidence anchors

- FY2025 revenue was approximately `C$12B`, net earnings `C$1.7B`, adjusted EPS
  `C$3.53`, and capital expenditures `C$5.6B`.
- The 2026–2030 capital plan is `C$28.8B`, with midyear rate base forecast to
  grow from `C$42.4B` in 2025 to `C$57.9B` in 2030, approximately `7%` CAGR.
  Planned rate base is not cash or earned return until placed in service and
  recovered.
- Q2 FY2026 net earnings were `C$396M`; first-half capex was `C$2.7B` against
  the `C$5.6B` annual plan. Funding, regulatory lag, and customer affordability
  remain part of the common-owner denominator.
- Fortis operates across five Canadian provinces, ten U.S. states, and the
  Caribbean. Diversification reduces single-jurisdiction risk but adds currency,
  regulatory, weather, environmental, and approval complexity.
- Tilbury Phase 1B received approval for an allowance of up to `C$2.2B`, but
  remains subject to further approvals and permitting. An allowance is not
  proof of final cost, completion, recovery, or shareholder return.

## QoE and financial-shenanigans prompts

1. Separate capital placed in service and earning a return from construction
   work in progress, regulatory assets, approved allowances, and customer-
   funded capital. Rate-base growth is not unrestricted cash.
2. Reconcile allowed return, actual project return, recovery timing, regulatory
   lag, disallowances, customer affordability, and cash collection by major
   jurisdiction.
3. Charge maintenance, storm, wildfire, environmental, reliability, and
   information-system capital before calling dividend cash distributable.
4. Track subsidiary dividends, parent financing, debt maturities, equity
   issuance, dividend-reinvestment dilution, credit metrics, and holding-company
   costs together.
5. Treat adjusted EPS and dividend growth as diagnostic until per-share earnings
   and common cash grow after the complete capital plan and financing burden.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what placed-in-service rate-base
growth, allowed returns, regulatory lag, project cost, maintenance capital,
financing, equity issuance, terminal growth, and cost of capital the valuation
requires. It should value earned, recovered returns rather than planned capex.

The Lyn Alden-style stress test asks whether utilities can fund essential
infrastructure through rates, inflation, higher interest, storms, wildfire,
currency pressure, and affordability constraints. Liquidity passes only when
subsidiary capital, debt, customer collection, regulatory recovery, dividends,
and common residual remain visible.

## Promotion boundary

`regulated-electric-gas-qualified; rate-recovery-and-per-share-return-open; no-ranking`

Promotion requires same-entity, same-period joins from capital placed in service
to approved rate recovery, collected revenue, earned return, maintenance/growth
capital, project cost, subsidiary and parent debt, storm/environmental cash,
equity issuance, dividends, and diluted common residual. Rate-base plans,
adjusted EPS, capex, dividends, and repurchases remain diagnostic inputs.

## Sources

- [Fortis company packet](../deep-company-pages/fortis-inc.md)
- [Fortis FY2025 Form 40-F](https://www.sec.gov/Archives/edgar/data/1666175/000166617526000013/fts-20251231.htm)
- [Fortis Q2 FY2026 results](https://www.sec.gov/Archives/edgar/data/1666175/000166617526000031/a2026q2ex991pressrelease.htm)
- [Next-execution handoff](combined-investment-research-next-execution-handoff-2026-09-17.md)
