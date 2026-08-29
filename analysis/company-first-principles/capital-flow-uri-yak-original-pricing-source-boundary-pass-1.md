# Capital Flow URI Yak Original Pricing Source Boundary Pass 1

## Purpose

This pass tests whether URI's Yak senior notes have public original-pricing evidence: issue price, original yield, and spread.

It answers:

`Can we say what the notes originally priced at beyond coupon and principal?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-yak-original-pricing-source-boundary-pass-1.csv`

## Source Boundary

This pass uses:

- URI March `7`, `2024` pricing announcement
- SEC Exhibit `4.1` indenture
- SEC Q3 `2024` 10-Q debt note
- Cbonds public bond page
- Public.com current bond page
- BusinessWire / MonitorDaily republications of URI's pricing announcement
- the prior URI Yak note-term, identifier, and holder-crosswalk passes

This pass is:

`original-pricing-source-boundary-visible`

It is not:

`original-issue-yield-visible`

or:

`original-spread-visible`

or:

`institutional-pricing-tape-visible`

## Evidence Captured

| Source | Evidence | Boundary |
|---|---|---|
| URI pricing announcement | `1.100B USD` principal, `6.125%` coupon, `2034` maturity, estimated `1.090B USD` net proceeds. | Coupon/proceeds visible, not issue price/yield/spread. |
| SEC indenture | Coupon, maturity, CUSIPs, ISINs, redemption terms. | Legal terms visible, not underwriting economics. |
| SEC Q3 `2024` 10-Q | Carrying amount of the `6 1/8%` Senior Notes due `2034`. | Balance-sheet carrying value, not original price/yield/spread. |
| Cbonds public page | Placement/outstanding amount, identifiers, ticker, and gated price/yield fields. | Public reference visible; original price/yield not visible in free view. |
| Public.com current page | Current price/yield snapshot. | Current retail quote, not March `2024` original pricing. |
| BusinessWire / MonitorDaily | Republished the URI pricing announcement. | Confirms announcement distribution, not additional pricing economics. |

## What This Adds

This pass narrows the exact missing source:

`offering memorandum / pricing supplement / purchase agreement / TRACE or institutional bond database`

Without one of those, the safe claim remains:

`coupon and proceeds visible, original price/yield/spread not visible`

The key discipline is not to treat current `5.71%` yield, current price `101.97`, or fund holding marks as the original March `2024` deal yield.

## Safe Claim

`URI's Yak senior notes are original-pricing-source-boundary-visible: public company, SEC, and bond-reference sources show principal, coupon, maturity, identifiers, estimated net proceeds, later holder rows, and a current retail quote snapshot, but this search pass did not locate original issue price, original issue yield, spread to benchmark, TRACE issuance tape, offering memorandum, purchase agreement, or pricing supplement. Do not promote current yield or fund marks into original deal pricing.`

## Claims Not To Make Yet

Do not say:

- the original issue yield is known
- the original spread to Treasury or benchmark is known
- current yield equals original yield
- carrying value equals offering price
- estimated net proceeds alone gives underwriting discount
- Cbonds free-view fields prove original yield
- holder marks prove deal pricing

## Next Concrete Work

The next evidence gates are:

1. Search paid or archived bond databases for `US911365BR47`, `USU91139AK85`, `911365BR4`, and `U91139AK8`.
2. Search for offering memorandum / purchase agreement / pricing supplement text.
3. Search TRACE issuance/trade history around March `7` to March `11`, `2024`.
4. Search legal-adviser and initial-purchaser deal databases for pricing grids.
5. Keep original yield/spread separate from current market yield and later fund marks.
