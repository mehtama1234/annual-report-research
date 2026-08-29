# Capital Flow URI Owned-Rental Segment Trend Pass 1

## Purpose

This pass answers the next narrow URI question:

`Is the owned-rental and specialty segment evidence a one-period snapshot, or does it show a trend?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-owned-rental-segment-trend-pass-1.csv`

## Source Boundary

This uses filed URI 10-K and 10-Q tables:

- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-10k-10k.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-q2-10q.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q2-10q.html`

The sources give annual FY `2023` to FY `2025` revenue type and segment tables, plus Q2/H1 `2024` to Q2/H1 `2026` segment tables.

They still do not give:

- true asset-level utilization
- rate/time/mix split
- segment OEC or average segment assets sufficient for clean ROA
- growth-versus-replacement capex
- specialty product-category margin bridge
- source-of-funds by fleet purchase

## Annual Owned-Rental Mix

| Metric | FY 2023 | FY 2024 | FY 2025 |
|---|---:|---:|---:|
| Owned equipment rentals | `9.948B USD` | `10.559B USD` | `11.048B USD` |
| Total equipment rentals revenue | `12.064B USD` | `13.029B USD` | `13.806B USD` |
| Owned equipment rentals / equipment rentals | `82.5%` | `81.0%` | `80.0%` |
| Re-rent / equipment rentals | `1.9%` | `2.0%` | `2.0%` |
| Ancillary and other rental revenue / equipment rentals | `15.6%` | `17.0%` | `18.0%` |

Owned-equipment rental revenue grew `11.1%` from FY `2023` to FY `2025`.

Total equipment-rentals revenue grew `14.4%`.

Ancillary and other rental revenue grew `31.9%`.

That means the owned-rental base stayed dominant, but ancillary and other rental revenue grew faster.

## Annual Segment Trend

| Metric | FY 2023 | FY 2024 | FY 2025 |
|---|---:|---:|---:|
| Specialty equipment rentals revenue | `3.261B USD` | `4.084B USD` | `4.641B USD` |
| Specialty share of equipment-rentals revenue | `27.0%` | `31.3%` | `33.6%` |
| Specialty equipment-rentals gross margin | `48.9%` | `48.1%` | `43.6%` |
| Specialty share of equipment-rentals gross profit | `33.1%` | `37.8%` | `38.5%` |
| Specialty share of segment capital expenditures | `21.0%` | `24.9%` | `25.4%` |

The key trend is not simply "specialty is better."

The cleaner wording is:

`Specialty is taking revenue and gross-profit share, and it has higher equipment-rentals gross margin than general rentals, but its gross margin compressed from 48.9% in FY2023 to 43.6% in FY2025.`

## H1 Segment Trend

| Metric | H1 2024 | H1 2025 | H1 2026 |
|---|---:|---:|---:|
| Specialty share of equipment-rentals revenue | `30.4%` | `33.4%` | `36.1%` |
| Specialty share of equipment-rentals gross profit | `37.9%` | `39.8%` | `41.1%` |
| Specialty equipment-rentals gross margin | `48.5%` | `44.5%` | `43.1%` |
| Specialty share of segment capital expenditures | `24.0%` | `25.8%` | `26.4%` |

The H1 trend reinforces the annual pattern:

- specialty is a rising share of equipment-rental revenue
- specialty is a rising share of equipment-rentals gross profit
- specialty still carries a higher gross margin than general rentals
- specialty gross margin is compressing
- segment capex share is rising, but still below specialty's revenue and gross-profit shares

## Safe Claim

`URI now has filed trend support that owned-equipment rentals remain the dominant equipment-rental revenue base while specialty is taking share. Owned-equipment rentals were 80.0% of FY2025 equipment-rentals revenue, down from 82.5% in FY2023, while specialty rose from 27.0% to 33.6% of annual equipment-rental revenue and from 33.1% to 38.5% of annual equipment-rentals gross profit. The same pattern appears in H1 2024-H1 2026, where specialty rose from 30.4% to 36.1% of equipment-rental revenue and from 37.9% to 41.1% of equipment-rentals gross profit.`

## Claims Not To Make Yet

Do not say:

- specialty has higher ROIC
- specialty is capital-light
- specialty margin expansion is occurring
- true utilization is known
- rate/time/mix is separately quantified
- capex is growth capex
- segment capex is a complete fleet source-and-use table

## What This Adds

This adds:

`owned-rental-segment-trend-visible`

It upgrades the prior owned-rental segment pass from:

`single filing current-period segmentation`

to:

`multi-period owned-rental and specialty segment trend`

It still does not upgrade URI to:

`fleet-ROIC-visible`

or:

`true-utilization-visible`

## Next Concrete Work

The next URI evidence gates are:

1. Find segment OEC or average assets so the specialty gross-profit trend can be paired with a real denominator.
2. Find rate/time/mix decomposition in transcripts or investor decks.
3. Find specialty category mix and margin drivers.
4. Find growth-versus-replacement capex.
5. Build a TTM version of the owned-rental and segment trend.

The first item is now partly addressed by:

`analysis/company-first-principles/capital-flow-uri-segment-asset-return-proxy-pass-1.md`
