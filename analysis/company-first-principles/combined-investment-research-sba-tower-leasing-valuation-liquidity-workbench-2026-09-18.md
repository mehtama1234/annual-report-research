# SBA Communications tower-leasing valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves SBA Communications from a wireless-infrastructure packet into a company-specific valuation object. It separates recurring site leasing, domestic and international towers, carrier amendments, tenant density, land control, churn, FX, acquisitions, AFFO, capex, debt, REIT distribution requirements, and diluted common residual. It does not treat site count, mobile-data growth, AFFO, adjusted EBITDA, backlog, or dividends as normalized owner cash without tower-level collection and capital-structure joins.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| SBA Communications | Tower-site rent cash after carrier collections, escalators, amendments, tenant additions, land control, domestic/international mix, acquisitions, tower construction, maintenance, debt, REIT distributions, and dilution | Tower construction, ground leases, site upgrades, land and renewal rights, acquisition integration, permitting, FX, interest expense, refinancing, and common capital | Carrier consolidation or capex slowdown, EchoStar churn, rates, international FX/political risk, lease or land loss, acquisition financing, debt refinancing, or dilution | Site leasing and AFFO grow while domestic churn, carrier capex, tenant density, land control, interest burden, or diluted per-share cash deteriorate |

## Current evidence anchors

- SBA ended 2025 with `46,328` sites, including `17,394` in the United States and territories and `28,934` internationally; site leasing generated `97.9%` of 2025 segment operating profit.
- Average tenants per site were `1.8`; about `71%` of tower structures were on land owned or controlled for more than `20` years, with average remaining life about `35` years including controlled renewals.
- Q2 2026 site-leasing revenue was about `$663.9M`, adjusted EBITDA `$483.8M`, AFFO `$324.4M`, and AFFO per share `$3.05`; domestic site-leasing revenue fell `3.7%` while international revenue rose `30.5%`.
- Q2 2026 included `109` towers built and a total portfolio of `46,390` sites; the domestic/international split and FX matter more than aggregate site count.
- Management reset 2026 outlook to exclude EchoStar contracted revenue and continued operating with net leverage in the `6.0x`–`7.0x` target range; recurring rent does not eliminate refinancing risk.

## QoE and financial-shenanigans prompts

1. Reconcile site count, tenants per site, amendments, escalators, churn, carrier collections, and backlog; a tower is not valuable owner cash without a paying tenant and controlled land.
2. Separate domestic, international, acquired, and newly built sites; test FX, permitting, political risk, ground-lease renewals, and acquisition return.
3. Keep AFFO adjustments, maintenance and growth capex, lease obligations, interest, refinancing, and REIT distribution requirements visible rather than treating AFFO as free common cash.
4. Test carrier concentration, customer capex, spectrum deployment, 5G/6G claims, fixed-wireless demand, and EchoStar effects against actual amendments and colocations.
5. Reconcile debt, preferred or other claims, dividends, repurchases, SBC, share count, and per-share AFFO before accepting capital return as owner cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what site growth, tenant additions, escalators, churn, international mix, reinvestment rate, leverage, and cost of capital the valuation requires. The Lyn Alden-style stress test asks whether carriers can keep funding densification through higher rates and consolidation, and whether tower landlords retain liquidity when customer capex slows, FX weakens, or debt maturities arrive.

## Promotion boundary

`sba-tower-leasing-qualified; carrier-churn-land-and-owner-cash-open; no-ranking`

Promotion requires same-entity joins from sites and tenants to carrier collections, amendments, churn, land control, required tower capex, acquisition return, FX, debt and refinancing, REIT distributions, claims, funding, and diluted common residual. Site count, mobile traffic, AFFO, adjusted EBITDA, backlog, guidance, and dividends remain diagnostic inputs.

## Sources

- [SBA Communications company packet](../../extracted/real-estate/reit-specialty-real-estate/sba-communications-corporation/company-packet.md)
- [SBA Communications source ledger](../../extracted/real-estate/reit-specialty-real-estate/sba-communications-corporation/source-ledger.md)

