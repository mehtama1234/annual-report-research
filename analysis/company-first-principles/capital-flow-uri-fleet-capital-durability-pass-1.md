# Capital Flow URI Fleet-Capital Durability Pass 1

## Purpose

This pass tests whether the United Rentals finding is only a one-quarter snapshot or a repeated pattern.

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-fleet-capital-durability-pass-1.csv`

The extractor is:

`scripts/extract-uri-fleet-capital-durability.py`

## Source Coverage

This pass uses cached URI quarterly and annual filings plus earnings-release exhibits from Q1 `2024` through Q2 `2026`.

The period set is:

`2024-Q1, 2024-Q2, 2024-Q3, 2024-FY, 2025-Q1, 2025-Q2, 2025-Q3, 2025-FY, 2026-Q1, 2026-Q2`

The CSV contains `210` rows across `10` periods and `21` metrics.

## Period Summary

| Period | Rental Revenue | Fleet Productivity | Avg OEC YoY | OCF | Gross Rental Capex | Net Fleet Cash Investment | Liquidity | Total Debt | AR Collateral Coverage | ABL Draw Intensity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `2024-Q1` | `2.929B` | `4.0%` | `3.6%` | `1.029B` | `0.595B` | `0.128B` | `3.561B` | `12.405B` | `132.0%` | `32.3%` |
| `2024-Q2` | `3.215B` | `4.6%` | `2.7%` | `2.294B` | `2.016B` | `1.118B` | `3.267B` | `12.889B` | `111.5%` | `37.0%` |
| `2024-Q3` | `3.463B` | `3.5%` | `3.8%` | `3.498B` | `3.287B` | `2.109B` | `2.866B` | `13.394B` | `107.2%` | `45.1%` |
| `2024-FY` | `3.422B` | `4.3%` | `4.1%` | `4.546B` | `3.756B` | `2.232B` | `2.845B` | `13.406B` | `141.7%` | `53.0%` |
| `2025-Q1` | `3.145B` | `3.1%` | `3.3%` | `1.425B` | `0.707B` | `0.284B` | `3.345B` | `12.922B` | `106.0%` | `35.4%` |
| `2025-Q2` | `3.415B` | `3.3%` | `3.6%` | `2.753B` | `2.274B` | `1.427B` | `2.996B` | `13.385B` | `130.0%` | `49.2%` |
| `2025-Q3` | `3.665B` | `2.0%` | `4.2%` | `3.934B` | `3.760B` | `2.549B` | `2.452B` | `14.148B` | `118.8%` | `57.5%` |
| `2025-FY` | `3.581B` | `0.5%` | `4.5%` | `5.190B` | `4.189B` | `2.736B` | `3.322B` | `14.229B` | `117.4%` | `36.6%` |
| `2026-Q1` | `3.419B` | `2.3%` | `5.7%` | `1.514B` | `0.874B` | `0.417B` | `3.377B` | `13.886B` | `101.8%` | `27.7%` |
| `2026-Q2` | `3.849B` | `3.4%` | `7.1%` | `3.305B` | `2.931B` | `2.040B` | `2.999B` | `14.230B` | `125.8%` | `37.0%` |

## What The Time Series Says

### Fleet Demand And Output

Rental revenue rose from `2.929B USD` in Q1 `2024` to `3.849B USD` in Q2 `2026`, up about `31.4%`.

Fleet productivity was positive in every extracted period, ranging from `0.5%` to `4.6%`.

Average OEC growth was also positive in every extracted period, ranging from `2.7%` to `7.1%` year over year.

This supports the claim that URI is not merely holding a static equipment base. It is repeatedly expanding and monetizing fleet access.

### Fleet Capital Absorption

H1 `2026` gross rental capex was `2.931B USD`, up `28.9%` from `2.274B USD` in H1 `2025`.

H1 `2026` net fleet cash investment was `2.040B USD`, up `43.0%` from `1.427B USD` in H1 `2025`.

That means the URI capital-flow question is not only "how much debt does it have?"

The better question is:

`How much recurring fleet cash investment can the platform absorb while still generating operating cash flow and preserving funding access?`

### Cash Conversion

H1 `2026` operating cash flow was `3.305B USD`, up about `20.1%` from H1 `2025`.

H1 `2026` operating cash flow covered:

- `112.8%` of H1 `2026` gross rental capex
- `162.0%` of H1 `2026` net fleet cash investment after sale proceeds

This strengthens the URI claim. The fleet-capital program is not only externally financed in the extracted window; it is paired with large operating cash generation.

### Collateralized Funding Support

The AR collateral pool coverage ratio stayed above `100%` in every extracted period.

Its range was:

- low: `101.8%` in Q1 `2026`
- high: `141.7%` in FY `2024`
- Q2 `2026`: `125.8%`

The ABL draw-intensity ratio ranged from `27.7%` to `57.5%` of stated ABL facility size.

That is useful evidence, but it remains a bounded ratio:

`ABL balance / stated ABL facility size`

It is not legal availability.

Legal availability still depends on the borrowing base, reserves, L/Cs, eligible collateral, covenants, and other constraints.

## Safe Claim

`United Rentals now has time-series support for the fleet-access capital-absorption pattern: repeated rental revenue growth, positive fleet productivity, recurring gross and net fleet cash investment, operating cash flow coverage, recurring liquidity, AR collateral-pool coverage above 100%, and bounded ABL draw-intensity evidence.`

## Claims Not To Make Yet

Do not say:

- URI has proven fleet ROIC by asset class
- all fleet capex is high-return growth capex
- the ABL borrowing base is fully proven
- stated facility headroom equals legal availability
- AR excess collateral equals immediately drawable cash
- specific debt instruments funded specific fleet purchases
- OEC growth is purely organic physical capacity growth

## What This Adds To The Funding-Type Question

This pass strengthens the hypothesis that URI's funding wrapper differs from Sterling's because the underlying economic asset differs.

URI has reusable fleet assets and receivables, so the visible wrapper includes ABL, AR securitization, term debt, notes, leases, equipment recycling, and liquidity.

Sterling has customer projects, backlog, retainage, and performance obligations, so its wrapper emphasizes revolver capacity, L/Cs, surety, working-capital timing, and acquisition flexibility.

## Next Concrete Work

The next URI pass should extract:

1. ABL agreement definitions for eligible collateral, advance rates, reserves, borrowing base, L/C treatment, and covenants.
2. AR securitization agreement definitions for eligible receivables, purchaser limits, dilution/loss triggers, reserves, and concentration caps.
3. Fleet class mix and utilization by general rentals versus specialty.
4. Growth versus replacement fleet capex.
5. Used-equipment margin and OEC recovery over the same period set.
6. A true return bridge from fleet OEC to rental revenue, rental gross margin, operating cash flow, capex, and sale proceeds.
