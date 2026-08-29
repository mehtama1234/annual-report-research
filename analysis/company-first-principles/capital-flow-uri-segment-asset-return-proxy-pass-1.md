# Capital Flow URI Segment Asset-Return Proxy Pass 1

## Purpose

This pass answers the next narrow URI question:

`Can we pair URI's segment gross-profit trend with a filed segment asset denominator without overclaiming ROIC?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-segment-asset-return-proxy-pass-1.csv`

## Source Boundary

This uses filed segment tables from:

- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-10k-10k.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-q2-10q.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q2-10q.html`

The source gives:

- segment equipment-rentals gross profit
- segment equipment-rentals gross margin
- segment capital expenditures
- segment total assets

This is still not ROIC.

The denominator is segment total assets, not fleet OEC or invested capital. The numerator is equipment-rentals gross profit, not operating income, EBITDA, net income, or free cash flow.

## Annual Segment Asset Denominator

| Metric | FY 2023 | FY 2024 | FY 2025 |
|---|---:|---:|---:|
| General rentals total assets | `20.411B USD` | `21.044B USD` | `21.787B USD` |
| Specialty total assets | `5.178B USD` | `7.119B USD` | `8.079B USD` |
| Total segment assets | `25.589B USD` | `28.163B USD` | `29.866B USD` |
| Specialty share of segment assets | `20.2%` | `25.3%` | `27.1%` |

Specialty asset share rose materially from FY `2023` to FY `2025`.

## Annual Gross-Profit/Assets Proxy

| Metric | FY 2023 | FY 2024 | FY 2025 |
|---|---:|---:|---:|
| General rentals equipment-rentals gross profit / segment assets | `15.8%` | `15.4%` | `14.8%` |
| Specialty equipment-rentals gross profit / segment assets | `30.8%` | `27.6%` | `25.0%` |
| Total equipment-rentals gross profit / segment assets | `18.8%` | `18.5%` | `17.6%` |

The useful reading is:

`Specialty produces more equipment-rentals gross profit per filed segment asset than general rentals, but the specialty proxy declined from 30.8% in FY2023 to 25.0% in FY2025.`

## H1 Average-Asset Proxy

| Metric | H1 2025 | H1 2026 |
|---|---:|---:|
| General rentals annualized equipment-rentals gross profit / average segment assets | `13.9%` | `14.7%` |
| Specialty annualized equipment-rentals gross profit / average segment assets | `26.4%` | `26.4%` |
| Total annualized equipment-rentals gross profit / average segment assets | `17.1%` | `18.0%` |
| Specialty share of average segment assets | `25.8%` | `28.0%` |

The H1 proxy says specialty's gross-profit/assets relationship held steady from H1 `2025` to H1 `2026`, while specialty's average asset share rose.

## Why This Matters

This improves the URI fleet economics chain:

`segment revenue -> segment gross profit -> segment capex -> segment assets -> bounded gross-profit/assets proxy`

It is a stronger denominator than the prior segment trend page, but it is still not a true return calculation.

## Safe Claim

`URI now has a bounded filed segment asset-return proxy: specialty produced more equipment-rentals gross profit per segment total asset than general rentals in FY2023-FY2025, but the proxy declined from 30.8% in FY2023 to 25.0% in FY2025. In H1 2026, specialty's annualized equipment-rentals gross profit / average segment assets was 26.4% versus 14.7% for general rentals, while specialty's average asset share rose to 28.0%.`

## Claims Not To Make Yet

Do not say:

- specialty ROIC is proven
- specialty ROA is proven
- specialty is capital-light
- specialty utilization is known
- segment total assets equal rental fleet OEC
- equipment-rentals gross profit equals operating income
- the proxy proves growth capex returns

## What This Adds

This adds:

`segment-asset-return-proxy-visible`

It upgrades the prior trend pass from:

`segment gross-profit share trend`

to:

`segment gross-profit trend paired with filed segment asset denominators`

It still does not upgrade URI to:

`fleet-ROIC-visible`

or:

`true-utilization-visible`

## Next Concrete Work

The next URI evidence gates are:

1. Find segment OEC or rental-fleet assets rather than total segment assets.
2. Find segment operating profit or EBITDA, not only equipment-rentals gross profit.
3. Find rate/time/mix decomposition.
4. Find growth-versus-replacement capex.
5. Find specialty category mix and margin drivers.

The fifth item is now partly addressed by:

`analysis/company-first-principles/capital-flow-uri-specialty-margin-driver-boundary-pass-1.md`
