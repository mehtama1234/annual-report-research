# Capital Flow URI Fleet-Type Revenue Estimate Pass 1

## Purpose

This pass turns URI's fleet-type percentage table into approximate dollar scale.

It answers:

`How many dollars of equipment-rental revenue sit behind each disclosed fleet type?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-fleet-type-revenue-estimate-pass-1.csv`

## Source Boundary

This pass uses:

- `capital-flow-uri-specialty-category-source-boundary-pass-1.md`
- `capital-flow-uri-owned-rental-segment-trend-pass-1.md`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-10k-10k.html`

This pass is:

`fleet-type-revenue-estimate-visible`

It is not:

`fleet-type source-stated revenue`

or:

`fleet-type margin/OEC visible`

The estimates multiply the disclosed fleet-type percentage by filed total equipment-rentals revenue. Because the percentage table is rounded to whole percentages, the dollar estimates are rounded approximations.

## Denominators

| Period | Total Equipment-Rentals Revenue |
|---|---:|
| FY 2024 | `13.029B USD` |
| FY 2025 | `13.806B USD` |

## Approximate Fleet-Type Revenue

| Fleet Type | FY 2025 Mix | FY 2025 Estimate | FY 2024 Mix | FY 2024 Estimate | Change |
|---|---:|---:|---:|---:|---:|
| General construction and industrial equipment | `39%` | `5.384B USD` | `40%` | `5.212B USD` | `+0.173B USD` |
| Aerial work platforms | `22%` | `3.037B USD` | `23%` | `2.997B USD` | `+0.040B USD` |
| General tools and light equipment | `9%` | `1.243B USD` | `9%` | `1.173B USD` | `+0.070B USD` |
| Power and HVAC equipment | `11%` | `1.519B USD` | `11%` | `1.433B USD` | `+0.085B USD` |
| Trench safety equipment | `5%` | `0.690B USD` | `5%` | `0.651B USD` | `+0.039B USD` |
| Fluid solutions equipment | `7%` | `0.966B USD` | `7%` | `0.912B USD` | `+0.054B USD` |
| Mobile storage equipment and modular office space | `3%` | `0.414B USD` | `3%` | `0.391B USD` | `+0.023B USD` |
| Surface protection mats | `4%` | `0.552B USD` | `2%` | `0.261B USD` | `+0.292B USD` |

## Specialty-Labeled Category Scale

The clearly Specialty-labeled categories are:

- Power/HVAC
- Trench Safety
- Fluid Solutions
- Mobile Storage/modular
- Surface Protection Mats

The rounded estimate for those categories is:

| Period | Sum |
|---|---:|
| FY 2024 | `3.648B USD` |
| FY 2025 | `4.142B USD` |
| Change | `+0.494B USD` |

This is directionally useful, but it does not exactly equal Specialty segment equipment-rentals revenue. The filed segment table reports Specialty equipment-rentals revenue of:

- FY `2024`: `4.084B USD`
- FY `2025`: `4.641B USD`

The gap likely reflects rounding, classifications, services, geography, acquisitions, and segment/category definition differences. The correct wording is therefore:

`rounded category-scale estimate`

not:

`audited category revenue by product line`

## What This Adds

This makes the category table more economically useful. Surface protection mats were only `4%` of equipment-rentals revenue in FY `2025`, but because the denominator is large, that is approximately `0.552B USD`. The increase from FY `2024` is roughly `0.292B USD`, using rounded mix percentages.

That helps explain why Matting can matter in the fleet-productivity and margin source trail without saying Matting alone explains Specialty.

## Safe Claim

`URI's 2025 10-K fleet-type percentages imply rounded FY2025 equipment-rental revenue scale of about 1.519B USD for Power/HVAC, 0.966B USD for Fluid Solutions, 0.690B USD for Trench Safety, 0.414B USD for Mobile Storage/modular, and 0.552B USD for Surface Protection Mats. These are derived estimates from rounded percentage disclosures, not source-stated product-line revenue. They make Specialty category scale visible, while category margin, OEC, capex, utilization, and ROIC remain undisclosed.`

## Claims Not To Make Yet

Do not say:

- these are audited product-line revenue numbers
- the rounded estimates reconcile exactly to segment revenue
- category margin is known
- category OEC is known
- category capex is known
- Surface Protection Mats caused the full Specialty margin decline
- category revenue growth proves category ROIC

## Next Concrete Work

The next URI evidence gates are:

1. Find a product-line source with actual category revenue, not rounded percentage estimates.
2. Find category OEC, capex, or margin.
3. Reconcile fleet-type categories to filed Specialty segment revenue.
4. Pull acquisition accounting around Yak/surface protection mats.
5. Use `capital-flow-uri-category-economics-matrix-pass-1.md` as the category-by-category stop/go table for revenue, OEC, capex, margin, utilization, productivity, and source strength.
