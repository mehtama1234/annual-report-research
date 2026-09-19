# Single-asset gold mine valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Lundin Gold's Fruta del Norte from strong current-period
mine evidence into a company-specific valuation, reinvestment, country-risk,
and liquidity test. It treats district exploration and FDNS as options rather
than current production and does not confuse a high spot-gold margin with
normalized common-owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Lundin Gold / Fruta del Norte | Producing mine cash after realized gold price, grade/recovery, throughput, royalties, tax, employee and government profit sharing, sustaining capital, development, closure, debt, and dilution | Underground development, mill and tailings, sustaining capital, exploration, FDNS, mine-to-mill expansion, reclamation, and operating-cost inflation | Gold-price decline, production/grade/recovery miss, Ecuador tax or security change, community/environmental interruption, delayed expansion, or payout crowding out mine renewal | Production and cash remain strong while AISC, reserve replacement, mine life, Ecuador claims, development capital, or diluted per-share residual deteriorate |

## Current evidence anchors

- FY2025 revenue was about `$1.780B` on `503,330` ounces sold at a `$3,594`
  realized price; production was `498,315` ounces.
- FY2025 operating cash flow was about `$1.023B`, investing cash outflow was
  `$97M`, and management free cash flow was `$926M`; shareholder distributions
  were `$664M` and ending cash was `$630M` with no debt.
- Cash operating cost and AISC were `$838` and `$1,015` per ounce. The margin
  was exceptional, but the 2025 guidance price assumption was `$2,500`; each
  `$100` per ounce price move was estimated to change royalties and statutory
  profit sharing by roughly `$10` per ounce.
- Q1 and Q2 2026 show cash timing risk: Q1 free cash flow was about `$349M`
  with quarter-end cash of `$704M`, while tax, profit-sharing, and distributions
  brought Q2 cash to about `$507M` despite a higher gold price.
- FDNS, FDN East, Sandia, Trancaloma, and Castillo are exploration or extension
  options requiring drilling, studies, permits, capital, and execution; they
  are not current reserves that can be valued at full production.

## QoE and financial-shenanigans prompts

1. Recalculate cash operating cost, AISC, tax, profit sharing, and free cash
   flow at `$2,000`, `$2,500`, and `$3,000` gold, separating price, grade,
   recovery, tonnes, inflation, and government or employee claims.
2. Split sustaining capital, non-sustaining capital, exploration, FDNS,
   tailings, closure, and mine-to-mill expansion before treating dividends as
   residual cash.
3. Track one-asset operating evidence: grade, recovery, throughput, mill
   availability, underground access, safety, labor, water, tailings, and
   transport.
4. Probability-weight district projects by drilling, resource conversion,
   engineering, permits, capital, schedule, and incremental return rather than
   capitalizing exploration language as reserves.
5. Reconcile Ecuador corporate tax, royalties, withholding, government and
   employee profit sharing, procurement, community, security, environmental,
   and water obligations to the common residual.
6. Treat dividends and management free cash flow as diagnostic until mine
   renewal, reclamation, country claims, and diluted shares are joined.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test values Fruta del Norte's producing cash
separately from FDNS and district options, using a mid-cycle gold price,
explicit sustaining capital, mine life, taxes, and probability-weighted growth.
The Lyn Alden-style stress test asks whether gold strength offsets energy,
labor, equipment, currency, Ecuador, tax, and community risks. A low-cost mine
can be resilient while still being a poor owner-cash asset if its payout defers
mine renewal or assumes permanent peak prices.

## Promotion boundary

`single-asset-gold-qualified; production-cost-and-reserve-cash-open; no-ranking`

Promotion requires same-entity, same-period joins from production, grade,
recovery, realized price, royalties, taxes, profit sharing, sustaining and
development capital, reserves/mine life, reclamation, Ecuador obligations,
cash, debt, and diluted common residual. Production, AISC, OCF, FCF, gold
price, dividends, and exploration options remain diagnostic inputs.

## Sources

- [Lundin Gold company packet](../deep-company-pages/lundin-gold-inc.md)
- [2025 annual report](https://lundingold.com/site/assets/files/111721/lug_2025_annual_report_final_23apr.pdf)
- [2025 annual information form](https://lundingold.com/site/assets/files/111751/f2025-lug-aif-final.pdf)
- [2026 quarterly and annual financial statements](https://lundingold.com/en/investors/quarterly-and-annual-financial-statements/)
