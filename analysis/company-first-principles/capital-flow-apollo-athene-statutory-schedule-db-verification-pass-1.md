# Apollo/Athene statutory Schedule DB verification and derivative cash pass 1

Research date: `2026-09-18`

## Located source range

Schedule DB is located at statutory pages `464–491` of the 2025 Athene
statement:

- page 464: Part A verification for options, caps, floors, collars, swaps, and
  forwards, plus Part B verification for futures;
- pages 465–489: Part C replication/synthetic-asset transactions;
- page 490: Part C Section 2 quarterly/year-to-date roll-forward; and
- page 491: Schedule DB verification of book value, fair value, and potential
  exposure.

## Quantified Part A/B flows

Part A reports `$2.009384164B` of consideration received or paid on
terminations, a `$(491.016129M)` total gain/loss on termination recognized,
`$3.283681900B` of unrealized valuation change, `$(2.168460812B)` of
amortization, and `$(1.515225396B)` of foreign-exchange change. Its displayed
ending book/adjusted carrying value is `$3.513012150B`.

Part B reports `$108.756075M` of cumulative cash change for futures and an
ending statement value of `$188.060515M`.

These are the first direct derivative cash/turnover controls in the Athene
packet. They materially improve the spread work because they show that hedge
cash, termination gains/losses, and valuation movements are distinct layers.

## Part C named-component ledger

Pages 465–489 were extracted into a conservative `735`-row component ledger.
Each row preserves the derivative identifier and instrument type alongside the
cash-instrument CUSIP and description. The ledger includes a direct identity
join for `592918-AE-6 / MF1 2025-B2 B` under derivative identifier
`04687#AB4`, with the source-visible book and fair-value candidates retained.

The extraction intentionally classifies numeric fields as resolved component
columns, sparse, or ambiguous because the PDF text layer merges dotted column
leaders and adjacent values. `233` rows have one candidate in each component
book/fair column, `474` remain sparse, and `28` remain ambiguous. A missing
derivative notional is not treated as a defect when the source presents it on a
parent derivative row. The extractor excludes the Part C total row, does not
impute values, and does not promote candidate columns into cash. The [Part C
ledger](data/capital-flow-apollo-athene-statutory-schedule-db-part-c-ledger-pass-1.csv)
is therefore a row-identity and review queue, not a settlement ledger.

The Part C rows now have an exact-CUSIP crosswalk to Schedule D: `728` of `735`
Part C rows match, producing `743` crosswalk rows across `586` unique CUSIPs.
The matched set includes MF1 2025-B2, AMAPS 1, Atlas secured advance funding,
Varde, and Ares routes. See the [Schedule DB–Schedule D crosswalk pass](capital-flow-apollo-athene-statutory-schedule-db-part-c-schedule-d-crosswalk-pass-1.md).

## Verification controls

The filing's page-491 verification reports:

| Control | Reported result | Interpretation |
|---|---:|---|
| Book/adjusted carrying value | `$1` difference | Schedule DB Part A/B versus Part D control closes within one dollar |
| Fair value | `$1` difference | Open-derivative fair-value control closes within one dollar |
| Potential exposure | `0` difference | Potential-exposure control closes exactly at displayed precision |

The structured values are in the [derivative hedge boundary CSV](data/capital-flow-apollo-athene-statutory-derivative-hedge-boundary-pass-1.csv).

## Boundary

The Schedule DB flows remain statutory derivative controls. They do not yet
prove net hedge return, product-level liability allocation, policyholder
credited rates, collateral/margin economics, borrower receipts, parent receipt,
or Apollo common-owner cash. Consideration received on termination must not be
promoted to free cash without matching the contract, counterparty, collateral,
hedged item, and liability purpose.

## Decision

`schedule-db-derivative-cash-and-verification-controls-visible; net-hedge-return-and-owner-cash-open`

The next promotion-quality object is a normalized Part A/B/C contract ledger
matched to Schedule DB verification, derivative cash-flow classifications,
counterparties, and product/liability hedge coverage.
