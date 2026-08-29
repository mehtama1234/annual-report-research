# Capital Flow URI Yak Public Holder Crosswalk Pass 2

## Purpose

This pass expands the later public-holder crosswalk for URI's Yak senior notes using only rows that were re-opened and source-visible in this pass.

It answers:

`Can the identified Yak note be followed into additional public holder rows beyond the first ETF/fund crosswalk?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-yak-public-holder-crosswalk-pass-2.csv`

## Source Boundary

This pass searches for the `6.125%` United Rentals North America note due March `15`, `2034`, with ISIN `US911365BR47` where visible.

This pass is:

`expanded-later-public-holder-crosswalk-visible`

It is not:

`full-holder-base-visible`

or:

`initial-purchaser-allocation-visible`

or:

`original-order-book-visible`

## Additional Holder Rows Captured

| Holder / source | Date / filing period | Identifier | Visible amount | Boundary |
|---|---:|---|---:|---|
| Federated Hermes Institutional High Yield Bond Fund SEC EDGAR portfolio | January `31`, `2025` | Security description; 144A note | `5.650M` face; `5.666272M USD` value | Later public portfolio row, not issuance allocation. |
| Loomis Sayles/Natixis annual report portfolio section A | Annual report source section | Security description | `27.620M` face; `28.771009M USD` value | Later public portfolio row; section-level scope only. |
| Loomis Sayles/Natixis annual report portfolio section B | Annual report source section | Security description | `1.785M` face; `1.859386M USD` value | Later public portfolio row; not deduped against other sections. |
| Loomis Sayles/Natixis annual report portfolio section C | Annual report source section | Security description | `6.985M` face; `7.276086M USD` value | Later public portfolio row; not deduped against other sections. |
| Loomis Sayles Global Allocation Fund Q1 holdings | First fiscal quarter holdings source | Security description | `1.090M` face; `1.135424M USD` value | Later public portfolio row; may overlap manager family exposure. |
| Invesco Global High Yield Corporate Bond ESG Climate Transition UCITS ETF composition page | Current public composition page | ISIN `US911365BR47` | `0.13%` portfolio weight | Later ETF composition row; no face or value visible. |

## Captured Row Sums

Do not treat this as a deduped holder base.

Rows with visible face amount:

`5.650M + 27.620M + 1.785M + 6.985M + 1.090M = 43.130M USD face`

Rows with visible market / portfolio value:

`5.666272M + 28.771009M + 1.859386M + 7.276086M + 1.135424M = 44.708177M USD`

The Invesco row adds a visible `0.13%` portfolio weight but no visible face or market value in the opened composition page.

These are captured row sums across mixed dates, fund families, source sections, and valuation contexts. They are useful for finding where the bond later sat, but they are not unique holders, not a single-date ownership table, and not evidence of the March `2024` order book.

## What This Adds

The holder map now has a stronger public-market trail:

`CUSIP / ISIN / coupon / maturity -> public fund schedules -> larger visible later-holder rows`

In simple terms: after URI issued the Yak acquisition notes, public fund schedules show pieces of that same bond sitting inside high-yield and allocation portfolios. That helps answer "who funded or held it later," but it still does not answer "who bought the deal at issuance."

## Safe Claim

`URI's Yak senior notes are now expanded-later-public-holder-crosswalk-visible: additional public portfolio schedules show the 6.125% United Rentals North America note due March 15 2034 in Federated Hermes, Loomis Sayles/Natixis, Loomis Sayles Global Allocation, and Invesco composition sources. The verified rows in this pass sum to 43.130M USD face and 44.708177M USD of visible later market/portfolio value where those fields are disclosed, plus one Invesco row with 0.13% portfolio weight. These are mixed-date captured row sums, not a full holder base, not deduped manager exposure, not original buyer allocation, and not original pricing evidence.`

## Claims Not To Make Yet

Do not say:

- these rows are all unique holders
- these rows are the full holder base
- these funds were initial purchasers
- later portfolio weight explains the original March `2024` syndicate allocation
- holder rows prove the exact ABL draw for Yak
- public fund marks prove original issue yield or spread

## Next Concrete Work

The next evidence gates are:

1. Build a dated N-PORT/statutory holder extractor keyed on CUSIP `911365BR4` and ISIN `US911365BR47`.
2. Add manager-family and fund-section dedupe fields before producing any unique-holder total.
3. Separate same-date holdings snapshots from mixed-date discovery rows.
4. Continue searching for original pricing terms: issue price, yield, benchmark spread, purchase agreement, offering memorandum, TRACE, or institutional deal database.
5. Keep the first-pass and expanded-pass totals separate until dedupe rules exist.

The first local holder-schedule extractor pass is now captured in `capital-flow-uri-yak-holder-schedule-extractor-pass-1.md`.
