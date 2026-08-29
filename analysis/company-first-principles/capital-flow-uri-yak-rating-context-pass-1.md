# Capital Flow URI Yak Rating Context Pass 1

## Purpose

This pass adds outside credit-rating context to URI's Yak note financing.

It answers:

`How did at least one rating agency frame the Yak senior unsecured note financing, and what rating evidence is still missing?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-yak-rating-context-pass-1.csv`

## Source Boundary

This pass uses:

- S&P Global Ratings public regulatory article headline/snippet for the proposed `1.100B USD` senior unsecured notes due `2034`
- URI note pricing announcement
- URI Yak senior-note terms pass
- URI Yak acquisition funding-chain pass

The S&P public page was indexed but its body did not render through the current browser view beyond a shell. Therefore this pass uses the public search/open metadata conservatively as:

`rating-headline-visible`

It is not:

`full-rating-rationale-visible`

or:

`multi-agency-rating-visible`

## Rating Context Captured

| Source | Evidence | Boundary |
|---|---|---|
| S&P Global Ratings | Proposed `1.100B USD` senior unsecured notes due `2034` rated `BB+`. | Rating headline visible; full rationale not extracted. |
| S&P Global Ratings | Recovery rating `4`. | Recovery category visible; full recovery waterfall not extracted. |
| S&P Global Ratings | Recovery expectation described as average recovery with a `30%-50%` range and rounded estimate of `35%`. | Rounded estimate visible; not a model or liquidation schedule. |
| URI pricing release | `1.100B USD` of `6.125%` Senior Notes due `2034`, estimated `1.090B USD` net proceeds, private offering, note proceeds plus ABL borrowings to fund Yak. | Company funding/source language, not rating opinion. |
| SEC indenture | Maturity, coupon, trustee, redemption, and Yak special mandatory redemption terms. | Legal terms, not credit rating rationale. |

## What This Adds

The note is no longer just:

`company-disclosed financing`

It now has outside credit-market context:

`BB+ senior unsecured note rating + Recovery 4 + average recovery estimate`

That helps answer:

`Who is funding this and what kind of credit risk is being underwritten?`

The answer is still partial. We can say the debt was externally rated by S&P at the issue level. We cannot yet say we have the full rating rationale, initial-purchaser allocation, investor book, yield/spread, or cross-agency consensus.

## Safe Claim

`URI's Yak note financing now has rating-headline context: S&P Global Ratings rated the proposed 1.100B USD senior unsecured notes due 2034 at BB+ with a Recovery rating of 4, described as average recovery with a 30%-50% range and rounded 35% estimate. This gives outside credit-market context for the Yak funding chain, but it is not a full rating-rationale extraction, investor-allocation proof, pricing-spread proof, exact ABL draw allocation, or Matting ROIC evidence.`

## Claims Not To Make Yet

Do not say:

- all rating agencies agreed on the same rating
- the full S&P recovery waterfall is extracted
- BB+ proves the acquisition was low risk
- the rating proves Matting unit economics
- recovery rating equals expected investor return
- S&P identified the exact ABL draw amount
- investor allocation is known

## Next Concrete Work

The next evidence gates are:

1. Retrieve the full S&P article text or PDF if available.
2. Search Moody's and Fitch directly for URI/Yak note rating actions.
3. Find offering memorandum or initial purchaser details.
4. Pull note yield/spread data from a reliable bond source.
5. Compare S&P's recovery framing against URI's ABL collateral and senior-note stack without collapsing secured and unsecured recoveries.

The first initial-purchaser channel upgrade is now captured in `capital-flow-uri-yak-initial-purchaser-source-boundary-pass-1.md`.

The first instrument identifier and market-data boundary upgrade is now captured in `capital-flow-uri-yak-bond-identifier-market-data-boundary-pass-1.md`.
