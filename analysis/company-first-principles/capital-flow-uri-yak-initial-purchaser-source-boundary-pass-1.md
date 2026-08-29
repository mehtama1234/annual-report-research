# Capital Flow URI Yak Initial-Purchaser Source Boundary Pass 1

## Purpose

This pass tests the next buyer-side evidence gate for URI's Yak note financing.

It answers:

`Can we move from "the notes were privately offered" to "the initial-purchaser channel is visible," and what is still missing before we can name who funded the debt?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-yak-initial-purchaser-source-boundary-pass-1.csv`

## Source Boundary

This pass uses:

- Cravath's March `25`, `2024` transaction page for the `1.100B USD` high-yield senior notes offering
- URI's March `7`, `2024` proposed private offering announcement
- URI's March `7`, `2024` pricing announcement
- SEC Exhibit `4.1` indenture dated March `11`, `2024`
- the prior URI Yak senior-note and rating-context passes

This pass is:

`initial-purchaser-role-visible`

It is not:

`initial-purchaser-names-visible`

or:

`note-investor-allocation-visible`

## Evidence Captured

| Source | Evidence | Boundary |
|---|---|---|
| Cravath | Cravath represented the initial purchasers in connection with the `1.100B USD` high-yield senior notes offering. | Initial-purchaser role visible; names not disclosed on the page. |
| Cravath | Transaction closed on March `11`, `2024`. | Closing date visible from counsel source. |
| URI proposed offering release | The notes were offered privately; initial purchasers would offer only to Rule `144A` QIBs or non-U.S. buyers under Regulation `S`. | Distribution channel visible; initial-purchaser names not disclosed. |
| URI pricing release | Estimated net proceeds were about `1.090B USD` after initial purchasers' discounts, commissions, and estimated fees/expenses. | Fee/discount existence visible; amount allocated to purchasers versus expenses not split. |
| SEC indenture | The notes were legal-term visible, but the indenture does not name initial purchasers. | Legal instrument evidence, not buyer-list evidence. |

## What This Adds

The Yak note chain now has a buyer-side channel boundary:

`Rule 144A / Reg S private high-yield notes -> initial purchasers represented by Cravath -> institutional distribution channel -> Yak acquisition funding`

This answers part of:

`Who funded it?`

The correct answer is still partial. We can say the notes moved through an initial-purchaser private-offering channel and that Cravath represented those initial purchasers. We still cannot name the individual banks, institutional buyers, allocations, order book, spread, yield, or secondary-market holders from this pass.

## Safe Claim

`URI's Yak note financing is now initial-purchaser-role-visible: the 1.100B USD high-yield senior notes offering closed on March 11 2024, Cravath represented the initial purchasers, URI described the distribution as a Rule 144A / Regulation S private offering, and estimated net proceeds were reduced by initial purchasers' discounts, commissions, and estimated fees/expenses. This proves the private-placement channel existed, but not the names of the initial purchasers, investor allocation, book composition, pricing spread, exact ABL draw allocation, or ongoing Matting ROIC.`

## Claims Not To Make Yet

Do not say:

- the initial purchaser banks are identified
- Cravath's client list equals the final investor base
- Rule `144A` buyers are the same thing as ultimate noteholders
- initial purchasers' discounts and commissions are separately quantified
- the offering memorandum is public
- the notes' buyer base proves Matting unit economics
- this solves the exact Yak ABL draw amount

## Next Concrete Work

The next evidence gates are:

1. Find the offering memorandum, purchase agreement, or transaction database entry that names initial purchasers.
2. Pull CUSIP/ISIN-level bond identifiers and pricing/yield/spread from a reliable bond source.
3. Search EDGAR exhibits for any purchase agreement or registration-rights agreement tied to the March `2024` private notes.
4. Search rating reports for arranger or initial-purchaser references.
5. Track later holder evidence only if a source names actual institutional noteholders.

The first instrument identifier and market-data boundary upgrade is now captured in `capital-flow-uri-yak-bond-identifier-market-data-boundary-pass-1.md`.
