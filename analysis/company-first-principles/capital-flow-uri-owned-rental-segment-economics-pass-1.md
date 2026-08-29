# Capital Flow URI Owned-Rental Segment Economics Pass 1

## Purpose

This pass answers the next narrow URI question:

`Can we move beyond total rental revenue and separate owned-equipment rental revenue, re-rent/ancillary revenue, and segment economics?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-owned-rental-segment-economics-pass-1.csv`

## Source Boundary

This uses the filed Q2 `2026` 10-Q:

`raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q2-10q.html`

It adds filed visibility into:

- owned-equipment rental revenue
- re-rent revenue
- delivery and pick-up revenue
- other ancillary rental revenue
- general-rentals versus specialty equipment-rental revenue
- segment equipment-rentals gross profit and gross margin
- segment capital expenditures
- management's stated capital-allocation logic

It still does not provide:

- asset-level ROIC
- true time utilization by asset class
- rate/time/mix split
- owned-equipment rental revenue by segment
- growth-versus-replacement capex
- segment OEC or average assets sufficient for clean segment ROA

## Revenue Type Split

| Metric | Q2 2026 | H1 2026 |
|---|---:|---:|
| Owned equipment rentals | `2.991B USD` | `5.676B USD` |
| Re-rent revenue | `88M USD` | `166M USD` |
| Total ancillary and other rental revenues | `770M USD` | `1.426B USD` |
| Total equipment rentals revenue | `3.849B USD` | `7.268B USD` |
| Owned equipment rentals / equipment rentals | `77.7%` | `78.1%` |
| Re-rent / equipment rentals | `2.3%` | `2.3%` |
| Ancillary and other rental revenues / equipment rentals | `20.0%` | `19.6%` |
| Owned equipment rentals / total revenue | `67.8%` | `67.6%` |

## Segment Economics

| Metric | General Rentals | Specialty | Total |
|---|---:|---:|---:|
| Q2 equipment rentals revenue | `2.418B USD` | `1.431B USD` | `3.849B USD` |
| Q2 equipment-rentals gross profit | `865M USD` | `636M USD` | `1.501B USD` |
| Q2 equipment-rentals gross margin | `35.8%` | `44.4%` | `39.0%` |
| H1 equipment rentals revenue | `4.647B USD` | `2.621B USD` | `7.268B USD` |
| H1 equipment-rentals gross profit | `1.618B USD` | `1.129B USD` | `2.747B USD` |
| H1 equipment-rentals gross margin | `34.8%` | `43.1%` | `37.8%` |
| H1 capital expenditures | `2.279B USD` | `817M USD` | `3.096B USD` |

## Derived Checks

| Check | Result |
|---|---:|
| Specialty share of Q2 equipment rentals revenue | `37.2%` |
| Specialty share of Q2 equipment-rentals gross profit | `42.4%` |
| Specialty share of H1 equipment rentals revenue | `36.1%` |
| Specialty share of H1 equipment-rentals gross profit | `41.1%` |
| Specialty share of H1 segment capex | `26.4%` |
| General rentals H1 capex / H1 equipment rentals revenue | `49.0%` |
| Specialty H1 capex / H1 equipment rentals revenue | `31.2%` |

## Management Allocation Clue

The filed segment note says equipment-rentals gross profit is the primary measure used by the CODM to assess segment performance and allocate resources.

It also says the most significant allocation decisions relate to purchases of rental equipment, and that the CODM considers monthly budget-to-actual variances for equipment-rentals gross profit when allocating capital.

This matters because it links the capital-flow question to the company's own operating logic:

`rental-equipment capital allocation -> segment equipment-rentals gross profit -> return-on-assets comparison -> resource allocation`

But the public filing still stops short of giving the clean denominator we want.

## Safe Claim

`URI now has filed support separating owned-equipment rental revenue from re-rent and ancillary revenue: owned-equipment rentals were 2.991B USD in Q2 2026 and 5.676B USD in H1 2026, equal to 77.7% and 78.1% of equipment-rentals revenue, respectively. The 10-Q also separates general-rentals and specialty segment economics: specialty was 36.1% of H1 equipment-rental revenue but 41.1% of H1 equipment-rentals gross profit, with a 43.1% H1 equipment-rentals gross margin versus 34.8% for general rentals.`

## Claims Not To Make Yet

Do not say:

- specialty has higher ROIC
- owned-fleet utilization is known
- rental rate, time utilization, and mix are separately quantified
- segment capex is growth capex
- segment capital expenditures reconcile exactly to gross rental capex
- specialty is capital-light
- the filing gives source-of-funds by fleet purchase

## What This Adds

This adds:

`owned-rental-segment-economics-visible`

It upgrades the prior proxy from:

`total rental revenue / OEC`

to:

`owned-equipment rental revenue and segment gross-profit/capex context`

It still does not upgrade URI to:

`fleet-ROIC-visible`

or:

`true-utilization-visible`

## Next Concrete Work

The next URI evidence gates are:

1. Find a rate/time/mix split in management commentary, investor decks, or transcripts.
2. Find segment OEC or average segment assets that can support a cleaner segment return proxy.
3. Find growth-versus-replacement capex split.
4. Build a multi-year segment economics table from 10-Q/10-K segment disclosures.
5. Check whether specialty category mix explains the higher gross margin.

The fourth item is now partly addressed by:

`analysis/company-first-principles/capital-flow-uri-owned-rental-segment-trend-pass-1.md`
