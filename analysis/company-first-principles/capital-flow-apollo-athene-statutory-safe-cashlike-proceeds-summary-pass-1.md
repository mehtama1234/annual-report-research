# Capital Flow Apollo Athene Statutory Safe Cash-Like Proceeds Summary Pass 1

## Purpose

This pass turns the corrected Athene Schedule D disposal/proceeds parser into a full-universe cash-like proceeds summary.

The question is:

`Of the named disposal/proceeds rows, how much looks like cash coming back, how much must be held as noncash/transfer activity, and which named CUSIPs are the highest-dollar next proof targets?`

The summary data is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-safe-cashlike-proceeds-summary-pass-1.csv`

The diagnostic data is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-safe-cashlike-proceeds-summary-diagnostic-pass-1.csv`

The builder is:

`scripts/build-athene-safe-cashlike-proceeds-summary.py`

## Main Finding

The corrected disposal parser has `7,655` rows and `72.807523483B USD` of parser consideration.

After disposition classification:

| Bucket | Rows | Consideration | Share |
|---|---:|---:|---:|
| cash-like candidate | `7,396` | `57.909402803B USD` | `79.5377%` |
| noncash-or-transfer hold | `259` | `14.898120680B USD` | `20.4623%` |

This is the first full-universe answer to the cash-back side of the Apollo/Athene statutory prototype. Most of the Schedule D disposal consideration is now in a cash-like candidate bucket, but more than `14.8B USD` is explicitly blocked from cash-return treatment because the disposition language points to exchanges, security withdrawals, transfers, or unresolved classification.

## Economic Class Split

| Economic class | Cash-likeness | Rows | Consideration | Share |
|---|---|---:|---:|---:|
| market-sale-or-counterparty-cash-candidate | cash-like-candidate | `3,258` | `39.699B USD` | `54.53%` |
| principal-paydown-cash-candidate | cash-like-candidate | `3,636` | `15.022B USD` | `20.63%` |
| tax-free-exchange-hold | noncash-or-transfer-hold | `186` | `12.231B USD` | `16.80%` |
| redemption-or-call-cash-candidate | cash-like-candidate | `389` | `2.096B USD` | `2.88%` |
| security-withdrawal-hold | noncash-or-transfer-hold | `45` | `1.341B USD` | `1.84%` |
| maturity-proceeds-cash-candidate | cash-like-candidate | `113` | `1.092B USD` | `1.50%` |
| direct-or-private-transfer-hold | noncash-or-transfer-hold | `21` | `0.742B USD` | `1.02%` |
| unclassified-hold | noncash-or-transfer-hold | `7` | `0.584B USD` | `0.80%` |

## Named CUSIP Proceeds Targets

The top `50` cash-like CUSIPs account for `10.876822674B USD`, or `14.9391%` of total parser consideration.

The same-CUSIP cash-like matched universe excluding placeholder identifiers has `19.636559453B USD` of consideration. Those rows are the best candidates for row-level proof because they can connect disposal/proceeds rows back to year-end Schedule D holding rows.

Top named cash-like CUSIP candidates:

| Rank | CUSIP | Issuer / description | Class | Match status | Consideration |
|---:|---|---|---|---|---:|
| 1 | `00264#-AB-3` | AP Aristotle Holdings LLC Aristotle Sen 5.25% | principal-paydown-cash-candidate | holding-and-disposal-same-cusip-visible | `776.0M USD` |
| 2 | `20633K-AA-6` | Concord Music Royalties LLC TUNES 2022-1A A2 | market-sale-or-counterparty-cash-candidate | disposal-only-cusip-visible | `624.9M USD` |
| 3 | `69346Y-AP-8` | PK Airfinance 2020 B1-F | principal-paydown-cash-candidate | disposal-only-cusip-visible | `497.7M USD` |
| 4 | `00196#-AA-8` | AOP Finance Partners LP | principal-paydown-cash-candidate | disposal-only-cusip-visible | `451.9M USD` |
| 5 | `69346Y-AQ-6` | PK Airfinance 2020 B2-F | market-sale-or-counterparty-cash-candidate | disposal-only-cusip-visible | `434.2M USD` |
| 6 | `G7741@-AB-6` | SoftBank Vision Fund II | principal-paydown-cash-candidate | disposal-only-cusip-visible | `372.9M USD` |
| 7 | `28655*-AA-7` | Eliant Invest Holding LP | market-sale-or-counterparty-cash-candidate | holding-and-disposal-same-cusip-visible | `358.3M USD` |
| 8 | `00024D-AL-7` | AA Infrastructure Fund 2 LLC | market-sale-or-counterparty-cash-candidate | holding-and-disposal-same-cusip-visible | `348.0M USD` |
| 9 | `91836A-AA-4` | VMC Finance 2023-PV1 LLC | principal-paydown-cash-candidate | disposal-only-cusip-visible | `295.3M USD` |
| 10 | `02300A-AA-8` | AMAPS 1 LLC Tranche A Note | market-sale-or-counterparty-cash-candidate | holding-and-disposal-same-cusip-visible | `268.0M USD` |

## What This Tells Us In Simple Terms

Apollo/Athene is not just sitting on an abstract pool of insurance assets. One Athene legal entity shows a large statutory asset book, and its Schedule D disposal schedule contains tens of billions of named asset proceeds.

The safer read is:

1. about `57.9B USD` of parsed disposal consideration is worth pursuing as cash-like proceeds
2. about `14.9B USD` must be held back because the row language looks noncash, transfer-like, or unresolved
3. the highest-dollar named candidates are not vague sectors; they are actual CUSIPs tied to entities like AP Aristotle, Concord Music Royalties, PK Airfinance, AOP Finance Partners, SoftBank Vision Fund II, Eliant, AA Infrastructure Fund, VMC Finance, and AMAPS
4. same-CUSIP rows are strongest because we can bridge from year-end holding rows to disposal/proceeds rows
5. disposal-only rows may still be legitimate cash return, but they need a different proof route because the asset may have been fully sold, matured, paid down, or absent from year-end holdings

## What This Proves

This pass proves:

1. the full corrected disposal/proceeds parser can be split into cash-like and noncash/transfer buckets
2. cash-like consideration is large enough to support named proceeds proof work, not just entity-level cash-flow discussion
3. the top named CUSIP worklist can be ranked by dollars
4. same-CUSIP matched cash-like proceeds can be isolated for row-level proof
5. noncash/transfer rows remain explicitly blocked from cash-return claims

## What It Does Not Prove

This pass does not prove:

1. borrower receipt or use of proceeds
2. source-of-funds from Apollo/Athene liabilities into each asset
3. lot-level continuity between specific purchases, holdings, and disposals
4. liability-cost spread or net investment spread by asset
5. final realized gain/loss for the full disposal schedule
6. IRR, NPV, ROIC, cash-on-cash return, or platform profit

## Safe Claim

`The Athene statutory disposal/proceeds workbench now separates 72.807523483B USD of parsed Schedule D consideration into 57.909402803B USD of cash-like candidates and 14.898120680B USD of noncash/transfer holds. This creates a named CUSIP proof queue for Apollo/Athene cash-back work, led by AP Aristotle, Concord Music Royalties, PK Airfinance, AOP Finance Partners, SoftBank Vision Fund II, Eliant, AA Infrastructure Fund, VMC Finance, and AMAPS. It supports named cash-like proceeds targeting, not final borrower-receipt, liability-spread, or asset-return proof.`

## Decision

`apollo-athene-safe-cashlike-proceeds-summary-ready-for-next-row-proof-packet`

The next move is a row-level packet for the highest-dollar same-CUSIP cash-like candidates and a separate disposal-only resolution pass for the highest-dollar disposal-only candidates.
