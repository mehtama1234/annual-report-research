# Capital Flow URI Investor Deck Fleet Productivity Pass 1

## Purpose

This pass follows the source-boundary page and answers:

`Do URI's investor decks give us the missing rate/time/mix split?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-investor-deck-fleet-productivity-pass-1.csv`

## Cached Sources

The following official URI investor presentations are now cached locally:

- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/investor-presentations/2025-q2-investor-presentation.pdf`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/investor-presentations/2025-q4-investor-presentation.pdf`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/investor-presentations/2026-q1-investor-presentation.pdf`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/investor-presentations/2026-q2-investor-presentation.pdf`

The Q2 `2026` deck is the most complete current deck because its fleet-productivity table carries the quarterly history through Q2 `2026`.

This pass is:

`investor-deck-aggregate-productivity-bridge-visible`

It is not:

`rate/time/mix split quantified`

## Deck Definition

The investor decks define fleet productivity as a combined metric. They say it captures the combined effect of:

- rental rates
- time utilization
- mix

The decks also define mix to include customer mix, fleet mix, geographic mix, and business mix, including Specialty.

That is useful because it tells us exactly what is inside the bucket. It is still not enough to decompose the bucket.

## Deck-Extracted Bridge

| Period | Average OEC | Assumed Inflation | Fleet Productivity | Owned Equipment Rental Revenue Change | Ancillary/Re-rent | Rental Revenue Change |
|---|---:|---:|---:|---:|---:|---:|
| Q1 2023 | `25.6%` | `-1.5%` | `2.0%` | `26.1%` | `-0.1%` | `26.0%` |
| Q2 2023 | `25.5%` | `-1.5%` | `-2.0%` | `22.0%` | `-0.9%` | `21.1%` |
| Q3 2023 | `22.2%` | `-1.5%` | `-2.2%` | `18.5%` | `-0.5%` | `18.0%` |
| Q4 2023 | `15.1%` | `-1.5%` | `0.3%` | `13.9%` | `-0.4%` | `13.5%` |
| Q1 2024 | `3.6%` | `-1.5%` | `4.0%` | `6.1%` | `0.8%` | `6.9%` |
| Q2 2024 | `2.7%` | `-1.5%` | `4.6%` | `5.8%` | `2.0%` | `7.8%` |
| Q3 2024 | `3.8%` | `-1.5%` | `3.5%` | `5.8%` | `1.6%` | `7.4%` |
| Q4 2024 | `4.1%` | `-1.5%` | `4.3%` | `6.9%` | `2.8%` | `9.7%` |
| Q1 2025 | `3.3%` | `-1.5%` | `3.1%` | `4.9%` | `2.5%` | `7.4%` |
| Q2 2025 | `3.6%` | `-1.5%` | `3.3%` | `5.4%` | `0.8%` | `6.2%` |
| Q3 2025 | `4.2%` | `-1.5%` | `2.0%` | `4.7%` | `1.1%` | `5.8%` |
| Q4 2025 | `4.5%` | `-1.5%` | `0.5%` | `3.5%` | `1.1%` | `4.6%` |
| Q1 2026 | `5.7%` | `-1.5%` | `2.3%` | `6.5%` | `2.2%` | `8.7%` |
| Q2 2026 | `7.1%` | `-1.5%` | `3.4%` | `9.0%` | `3.7%` | `12.7%` |

## What We Learn

The deck evidence is stronger than the release-only pass in three ways:

1. The deck confirms the same bridge formula in one table.
2. The deck adds the owned-equipment rental revenue bridge line.
3. The deck makes the source boundary explicit: fleet productivity is one bucket made from rate, time utilization, and mix.

The important pattern is that URI's revenue acceleration in Q2 `2026` was not only fleet-size growth. Q2 `2026` had:

- `7.1%` average OEC growth
- `3.4%` aggregate fleet productivity
- `3.7%` ancillary/re-rent contribution
- `12.7%` reported rental revenue growth

That is a stronger operating-conversion trail for fleet capital. It still is not asset-level ROIC or true utilization.

## Safe Claim

`URI's investor decks make the aggregate fleet-productivity bridge deck-visible. The Q2 2026 deck shows quarterly bridge history from Q1 2023 through Q2 2026 and defines fleet productivity as the combined impact of rental rates, time utilization, and mix on owned equipment rental revenue. Q2 2026 rental revenue growth of 12.7% bridged to 7.1% average OEC growth, -1.5% assumed inflation, 3.4% fleet productivity, 9.0% owned-equipment rental revenue growth, and 3.7% ancillary/re-rent contribution. The deck still does not split fleet productivity into its rate, time-utilization, and mix components.`

## Claims Not To Make Yet

Do not say:

- rental-rate contribution is quantified
- time-utilization contribution is quantified
- fleet/customer/geographic/business mix contribution is quantified
- Specialty mix contribution inside fleet productivity is quantified
- fleet productivity equals utilization
- the deck proves segment ROIC
- ancillary/re-rent contribution is owned-equipment utilization

## Next Concrete Work

The next URI evidence gates are:

1. Use `capital-flow-uri-transcript-rate-time-mix-commentary-pass-1.md` for the first transcript commentary layer.
2. Find official transcript/audio archives that can replace third-party transcript pages.
3. Test whether management gives a quantitative reason for Q2 `2026` ancillary/re-rent contribution increasing to `3.7%`.
4. Keep segment OEC, operating-profit return, growth/replacement capex, and actual utilization as separate gates.
