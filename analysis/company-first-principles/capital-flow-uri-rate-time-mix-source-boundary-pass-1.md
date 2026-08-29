# Capital Flow URI Rate/Time/Mix Source Boundary Pass 1

## Purpose

This pass answers the narrow URI question:

`Can we split fleet productivity into rental rate, time utilization, and mix from the current source set?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-rate-time-mix-source-boundary-pass-1.csv`

## Source Boundary

This pass uses local filed/release sources plus official URI investor-relations pages:

- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-q2-ex99-earnings-release.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q2-ex99-earnings-release.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q2-10q.html`
- URI Q2 `2025`, Q4/FY `2025`, Q1 `2026`, and Q2 `2026` official releases
- URI events and presentations page
- URI Q2 `2026` call/webcast announcement

This pass is:

`rate-time-mix-source-boundary-visible`

It is not:

`rate/time/mix split quantified`

The releases define fleet productivity as an aggregate impact from rental rates, time utilization, and mix on owned equipment rental revenue. The public releases also expose a bridge from rental revenue growth to average OEC, assumed inflation, fleet productivity, and ancillary/re-rent contribution. They still do not split the fleet-productivity bucket into actual rental rate, time utilization, and mix components.

## What Is Visible

| Period | Average OEC | Assumed Inflation | Fleet Productivity | Ancillary/Re-rent Contribution | Total Rental Revenue Change |
|---|---:|---:|---:|---:|---:|
| Q2 2025 | `3.6%` | `-1.5%` | `3.3%` | `0.8%` | `6.2%` |
| H1 2025 | `3.5%` | `-1.5%` | `3.2%` | `1.6%` | `6.8%` |
| Q4 2025 | `4.5%` | `-1.5%` | `0.5%` | `1.1%` | `4.6%` |
| FY 2025 | `3.9%` | `-1.5%` | `2.2%` | `1.4%` | `6.0%` |
| Q1 2026 | `5.7%` | `-1.5%` | `2.3%` | `2.2%` inferred | `8.7%` |
| Q2 2026 | `7.1%` | `-1.5%` | `3.4%` | `3.7%` inferred | `12.7%` |
| H1 2026 | `6.4%` | `-1.5%` | `2.9%` | `3.0%` inferred | `10.8%` |

The inferred rows use the same public-release bridge:

`rental revenue growth = average OEC growth + assumed inflation + fleet productivity + ancillary/re-rent contribution`

So:

`ancillary/re-rent contribution = rental revenue growth - average OEC growth - assumed inflation - fleet productivity`

Because assumed inflation is shown as a negative `-1.5%` drag, subtracting it adds back `1.5%`.

## What This Adds

This turns URI's fleet productivity evidence from:

`productivity number observed`

to:

`source-visible fleet-productivity bridge`

It still does not become:

`rate/time/mix split known`

or:

`true utilization known`

## Why The Missing Split Matters

URI is a fleet-access capital absorber. To know whether the fleet capex is producing better economics, we need to know whether growth is coming from:

- more fleet deployed into the market
- higher rental rates
- better time utilization
- mix shift toward higher-value fleet or specialty categories
- ancillary/re-rent growth
- acquisition effects

The current source set can separate average OEC, inflation, aggregate productivity, and ancillary/re-rent. It cannot yet separate the internal rate/time/mix components inside aggregate fleet productivity.

## Safe Claim

`URI now has a source-visible fleet-productivity methodology bridge: rental revenue change can be decomposed into average OEC growth, assumed inflation drag, aggregate fleet productivity, and ancillary/re-rent contribution. However, the public filings and locally cached source set still do not split fleet productivity into rental rate, time utilization, and mix. Official IR pages point to investor presentations and archived calls as the next source family.`

## Claims Not To Make Yet

Do not say:

- rental rate contribution is known
- time utilization contribution is known
- fleet mix contribution is known
- true utilization is known
- investor-deck rate/time/mix detail has been extracted
- transcript management commentary has been reviewed
- the fleet return proxy is full fleet ROIC

## Next Concrete Work

The next URI evidence gates are:

1. Use `capital-flow-uri-investor-deck-fleet-productivity-pass-1.md` as the deck-extracted aggregate bridge.
2. Pull transcript commentary around rate, time utilization, fleet mix, specialty mix, and Yak.
3. Match any transcript rate/time/mix commentary back to the filed owned-rental and segment economics tables.
4. Keep actual utilization, segment OEC, operating-profit return, and growth/replacement capex as separate proof gates.
