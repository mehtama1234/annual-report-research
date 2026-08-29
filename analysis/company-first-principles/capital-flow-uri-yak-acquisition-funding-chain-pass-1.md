# Capital Flow URI Yak Acquisition Funding Chain Pass 1

## Purpose

This pass isolates the funding side of URI's Yak/Matting acquisition.

It answers:

`How was the Yak acquisition funded, and how far can we trace that capital without inventing an ABL source-and-use schedule?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-yak-acquisition-funding-chain-pass-1.csv`

## Source Boundary

This pass uses:

- `capital-flow-uri-yak-matting-acquisition-economics-pass-1.md`
- `capital-flow-uri-abl-agreement-mechanics-pass-1.md`
- `capital-flow-uri-fleet-capital-durability-pass-1.md`
- URI March `4`, `2024` Yak acquisition announcement
- URI FY `2024` acquisition footnote

This pass is:

`yak-acquisition-funding-chain-visible`

It is not:

`purchase-level-source-and-use-visible`

or:

`ABL-draw-allocation-visible`

## Funding Chain

| Step | Evidence | Boundary |
|---|---|---|
| Acquisition target | Yak Access / Yak Mat / New South Access gave URI a Matting adjacency. | Acquisition-level, not ongoing product-line ROIC. |
| Purchase value | Base purchase price was `1.100B USD`; acquisition-date fair value was `1.158B USD`. | Purchase value is not fleet OEC or replacement cost. |
| Debt instrument | FY2024 footnote says the acquisition and related fees were funded through `1.100B USD` of `6 1/8%` senior notes plus ABL drawings. | The filing does not split the exact ABL-dollar amount. |
| ABL channel | URI's ABL was an established secured funding wrapper; Q1 `2024` balance was `1.371B USD`, Q2 `2024` was `1.571B USD`, and FY `2024` was `2.253B USD`. | Balance movement does not prove acquisition-specific draw allocation. |
| Operating destination | Yak brought about `600,000` mats, `353M USD` of 2023 adjusted revenue, `171M USD` of 2023 adjusted EBITDA, and `127M USD` of acquired rental-equipment fair value. | Still not ongoing URI Matting margin, utilization, capex, or ROIC. |

## What We Can Calculate

| Metric | Calculation | Result |
|---|---|---:|
| Senior notes / base purchase price | `1.100B / 1.100B` | `100.0%` |
| Senior notes / acquisition-date fair value | `1.100B / 1.158B` | `95.0%` |
| Acquisition-date fair value less senior notes | `1.158B - 1.100B` | `58M USD` |
| Senior notes / acquired rental-equipment fair value | `1.100B / 127M` | `8.66x` |
| Q1 2024 ABL balance / stated ABL size | `1.371B / 4.250B` | `32.3%` |
| Q2 2024 ABL balance / stated ABL size | `1.571B / 4.250B` | `37.0%` |
| FY2024 ABL balance / stated ABL size | `2.253B / 4.250B` | `53.0%` |

The senior-note funding is the cleanest piece: `1.100B USD` of notes against a `1.100B USD` base purchase price and `1.158B USD` acquisition-date fair value.

The ABL piece is real but not allocated: filings say ABL drawings funded the transaction and related fees, but do not disclose the exact amount, timing, collateral base, or whether the draws were later repaid/refinanced.

## Why This Matters

This is a clean example of the capital-flow chain we are trying to build:

`capital markets debt + asset-backed revolver -> acquisition of operating fleet adjacency -> utility/midstream/power-exposed matting capacity -> Specialty segment`

That is stronger than a generic acquisition claim because we have:

- purchase value
- named funding instruments
- note principal and coupon
- ABL balance context
- target revenue and EBITDA
- target mat count
- acquired rental-equipment fair value

It is still below purchase-level source-and-use proof because the ABL draw amount is not split.

## Safe Claim

`URI's Yak acquisition funding chain is visible at instrument level: the FY2024 acquisition footnote says the acquisition and related fees were funded through 1.100B USD of 6 1/8% senior notes and drawings on URI's senior secured ABL facility. The notes alone equaled 100.0% of the 1.100B USD base purchase price and about 95.0% of the 1.158B USD acquisition-date fair value. The ABL channel is real but not allocation-visible: public filings show ABL balances during 2024, but they do not disclose the exact ABL dollars used for Yak or a purchase-level source-and-use schedule.`

## Claims Not To Make Yet

Do not say:

- the exact ABL draw for Yak is known
- Q1 or Q2 2024 ABL balance movement equals the Yak draw
- the senior notes funded only rental equipment
- acquired rental-equipment fair value equals OEC
- ABL borrowing-base availability for Yak collateral is known
- purchase-level source-and-use is fully reconciled
- ongoing Matting ROIC is proven

## Next Concrete Work

The next evidence gates are:

1. Use `capital-flow-uri-yak-senior-note-terms-pass-1.md` for note maturity, coupon, proceeds, redemption, and indenture mechanics.
2. Search for any ABL availability schedule around March `2024`.
3. Track whether later filings discuss repayment, refinancing, or integration of the Yak acquisition funding.
4. Look for rating-agency commentary on the Yak financing and leverage impact.
5. Connect Yak acquisition funding to post-acquisition Matting revenue and EBITDA if URI later discloses them.
