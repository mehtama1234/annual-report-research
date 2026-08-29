# Capital Flow URI Yak Public Holder Crosswalk Pass 1

## Purpose

This pass builds the first later-holder crosswalk for URI's Yak senior notes.

It answers:

`After identifying the Yak note by CUSIP and ISIN, can we find public fund or ETF holdings that show who later held pieces of the bond?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-yak-public-holder-crosswalk-pass-1.csv`

## Source Boundary

This pass uses public ETF/fund/portfolio holdings pages and files that mention CUSIP `911365BR4` or ISIN `US911365BR47`.

This pass is:

`later-public-holder-crosswalk-visible`

It is not:

`initial-purchaser-names-visible`

or:

`full-holder-base-visible`

or:

`note-investor-allocation-visible`

## Holder Rows Captured

| Holder / source | Date | Identifier | Visible amount | Boundary |
|---|---:|---|---:|---|
| Schwab High Yield Bond ETF (`SCYB`) | August `21`, `2026` | CUSIP `911365BR4` | `2.225M` face; about `2.3M USD` market value | Later ETF holding, not initial purchaser. |
| Pacer Trendpilot US Bond ETF (`PTBD`) | August `24`, `2026` | CUSIP `911365BR4` | `0.070M` face; `0.071168M USD` market value | Later ETF holding, not full holder base. |
| Columbia Threadneedle ETF holdings export | August `21`, `2026` | CUSIP `911365BR4`; ISIN `US911365BR47` | `0.600M` face; `0.610542M USD` market value | Later fund holding, not buyer allocation. |
| Fidelity Strategic Advisers Income Opportunities portfolio listing | March `2026` source snapshot | CUSIP `911365BR4`; ISIN `US911365BR47` | `0.727331M USD` market value | Later fund holding; face not captured in this pass. |
| Federated Core Trust High Yield Bond Portfolio via Fintel | Reporting period March `31`, `2026` | ISIN `US911365BR47` | about `1.12M USD` value; `0.1076%` portfolio weight | Later portfolio disclosure, not initial-purchaser evidence. |

## Aggregates

Do not add unlike units.

Visible face amount from sources that disclosed face/quantity:

`2.225M + 0.070M + 0.600M = 2.895M USD face`

Visible market value / portfolio value snapshots from the five captured later-holder rows:

`2.300000M + 0.071168M + 0.610542M + 0.727331M + 1.120000M = 4.829041M USD`

These are lower-bound public holder traces, not a full holder base. Dates, source formats, valuation methods, and portfolio scopes differ.

## What This Adds

The Yak note chain now has a later-holder evidence path:

`CUSIP / ISIN -> ETF/fund holdings rows -> visible later holders`

This helps answer:

`Who is funding or holding this after issuance?`

The answer is still partial. We can identify several later public funds/ETFs with reported positions in the same bond. We still cannot say those vehicles were original buyers, initial purchasers, anchor investors, or representative of the full institutional holder base.

## Safe Claim

`URI's Yak senior notes are now later-public-holder-crosswalk-visible: public ETF/fund holdings sources show later positions in CUSIP 911365BR4 / ISIN US911365BR47 across Schwab SCYB, Pacer PTBD, a Columbia Threadneedle ETF holdings export, a Fidelity Strategic Advisers portfolio listing, and Federated Core Trust High Yield Bond Portfolio via Fintel. The three sources with visible face/quantity show 2.895M USD face, and the five captured market-value rows show about 4.829M USD of later public holder traces. This does not identify original initial purchasers, the full holder base, allocation, original issue spread/yield, exact Yak ABL draw allocation, or Matting ROIC.`

## Claims Not To Make Yet

Do not say:

- these funds were initial purchasers
- the five rows are the full holder base
- market value equals face amount
- current fund holdings explain the March `2024` order book
- ETF holder rows prove use of proceeds beyond URI's filings
- the holder crosswalk solves the exact ABL draw
- holder evidence proves Matting category economics

## Next Concrete Work

The next evidence gates are:

1. Search more ETF, mutual-fund, insurance statutory, and N-PORT holdings files for CUSIP `911365BR4` and ISIN `US911365BR47`.
2. Separate holdings by date before aggregating.
3. Keep face, market value, portfolio weight, and fair value in separate columns.
4. Find original issue price, yield, and spread from an offering memorandum, TRACE source, or institutional database.
5. Find purchase agreement or offering memorandum evidence naming the initial purchaser firms.

The expanded later-holder crosswalk is now captured in `capital-flow-uri-yak-public-holder-crosswalk-pass-2.md`.

The first original-pricing source-boundary pass is now captured in `capital-flow-uri-yak-original-pricing-source-boundary-pass-1.md`.
