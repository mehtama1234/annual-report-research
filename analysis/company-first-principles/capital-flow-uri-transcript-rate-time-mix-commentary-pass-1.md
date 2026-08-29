# Capital Flow URI Transcript Rate/Time/Mix Commentary Pass 1

## Purpose

This pass follows the investor-deck extraction and asks:

`Do earnings-call transcripts explain what is inside URI's fleet-productivity bucket?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-transcript-rate-time-mix-commentary-pass-1.csv`

## Source Boundary

This pass uses:

- Q2 `2026` Investing.com transcript page
- Q1 `2026` Investing.com transcript page
- Q2 `2025` Investing.com transcript page
- Q4 `2025` Motley Fool transcript page, also cached locally at `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/earnings-transcripts/2025-q4-fool-transcript.html`
- URI official releases and investor decks already captured in prior passes

The Investing pages were accessible through web indexing and direct page inspection, but shell `curl` returned placeholder files. The source status is therefore:

`web-verified-transcript-commentary`

for those Investing transcript rows, not:

`locally-cached-transcript`

## What The Transcripts Add

The deck proves the bridge, but not the internal split. The transcript layer adds three things:

1. Q4 `2025` gives the clearest qualitative split: rate was positive/stable, time was slightly less positive, and mix was the large negative driver because of Matting.
2. Q2 `2025` gives a margin/cost explanation around ancillary revenue, delivery, and moving fleet across the network to support high time utilization and efficient capital utilization.
3. Q2 `2026` and Q1 `2026` support positive demand/pricing/deployment commentary but still do not quantify rate versus time utilization versus mix.

## Transcript Findings

| Period | Commentary Type | What It Adds | Evidence Level |
|---|---|---|---|
| Q4 2025 | directional rate/time/mix | rate positive/stable; time slightly softer; mix was the major negative driver; Matting was about one point of fleet productivity impact | `qualitative-rate-time-mix-commentary-visible` |
| Q2 2025 | ancillary/time-utilization cost bridge | ancillary growth was margin dilutive; delivery and fleet repositioning costs were called out; roughly `$15M` of fleet movement supported high time utilization and efficient capital utilization | `transcript-driver-commentary-visible` |
| Q1 2026 | positive productivity/pricing/deployment | fleet productivity was `2.3%`; OER growth was `6.5%`; growth came from large projects and key verticals | `aggregate-productivity-commentary-visible` |
| Q2 2026 | positive productivity/pricing/deployment | fleet productivity was `3.4%`; ancillary/re-rent grew nearly `28%`; management commentary supports strong demand, disciplined pricing, and efficient fleet deployment | `aggregate-productivity-commentary-visible` |

## What This Means

The source ladder now looks like this:

| Layer | Status |
|---|---|
| Release bridge | visible |
| Investor deck bridge | visible |
| Deck definition of rate/time/mix bucket | visible |
| Transcript qualitative split | visible for Q4 `2025` only |
| Quantified rate/time/mix split | not visible |
| Actual time utilization percentage | not visible |
| Segment ROIC or fleet ROIC | not visible |

The strongest new point is Q4 `2025`: we can now say management qualitatively attributed the low `0.5%` fleet-productivity quarter mainly to mix, specifically Matting project timing, while rate remained positive/stable and time was slightly less positive.

## Safe Claim

`URI's transcript evidence makes the rate/time/mix bucket qualitatively visible in Q4 2025 but still not quantitatively split. Management attributed Q4 2025's low 0.5% fleet productivity to a large negative mix effect from Matting project timing, with rate positive/stable and time slightly less positive. Q2 2025 commentary also links ancillary revenue, delivery costs, and fleet repositioning to margin drag and high time-utilization support. Q1 and Q2 2026 support positive aggregate productivity, disciplined pricing, strong demand, and efficient fleet deployment, but do not quantify the rate/time/mix components.`

## Claims Not To Make Yet

Do not say:

- Q2 `2026` rate contribution is quantified
- Q2 `2026` time utilization contribution is quantified
- Q2 `2026` mix contribution is quantified
- Q4 `2025` Matting explains all of 2025 fleet productivity
- ancillary/re-rent contribution equals utilization
- fleet movement cost is bad capital allocation
- transcript commentary proves fleet ROIC

## Next Concrete Work

The next URI evidence gates are:

1. Find primary audio/transcript archives or official webcast transcripts if available.
2. Extract any transcript language around Q2 `2026` ancillary/re-rent growth of nearly `28%`.
3. Use `capital-flow-uri-ancillary-matting-margin-bridge-pass-1.md` to separate Matting productivity mix from ancillary/re-rent margin mix.
4. Search for actual utilization metrics in industry datasets, rental fleet disclosures, or management comments.
5. Keep segment OEC, segment operating-profit return, and growth/replacement capex separate from the productivity bridge.
