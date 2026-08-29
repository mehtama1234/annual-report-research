# Capital Flow Apollo Athene Statutory Safe Cash-Like Issuer/Borrower Map Pass 1

## Purpose

This pass maps the top Athene same-CUSIP cash-like proceeds candidates to issuer, wrapper, destination lane, and remaining borrower-cash proof needs.

The question is:

`Once Athene has named same-CUSIP cash-like proceeds, what do those instruments appear to represent, where is the money moving economically, and what is still needed to prove borrower receipt or use?`

The mapping table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-safe-cashlike-issuer-borrower-map-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-safe-cashlike-issuer-borrower-map-diagnostic-pass-1.csv`

The builder is:

`scripts/build-athene-safe-cashlike-issuer-borrower-map.py`

## Main Result

The `10` selected same-CUSIP proceeds candidates split into:

| Bucket | Rows | Athene cash-like consideration |
|---|---:|---:|
| non-Treasury operating/wrapper rows | `7` | `2.378326037B USD` |
| Treasury / sovereign reserve rows | `3` | `551.866935M USD` |
| all selected rows | `10` | `2.930192972B USD` |

This is the first Apollo/Athene pass that turns the same-CUSIP cash-like proceeds packet into an economic destination map.

## Mapped Rows

| CUSIP | Issuer / wrapper | Destination lane | Athene cash-like consideration | Mapping status |
|---|---|---|---:|---|
| `00264#-AB-3` | AP Aristotle Holdings LLC | Apollo-affiliated private credit / finance vehicle | `776.032348M USD` | issuer named; mixed row and borrower-use hold |
| `28655*-AA-7` | Eliant Invest Holding LP | Apollo-related private credit / finance vehicle | `358.251536M USD` | platform-related issuer visible; borrower-use hold |
| `00024D-AL-7` | AA Infrastructure Fund 2 LLC | infrastructure / real assets hold | `347.965250M USD` | issuer named; mixed row hold |
| `02300A-AA-8` | AMAPS 1 LLC | structured credit / asset-backed credit | `268.000000M USD` | Apollo wrapper visible; underlying collateral hold |
| `20633K-AN-8` | Concord Music Royalties LLC | music-royalty ABS finance | `229.053398M USD` | borrower wrapper and use proxy visible; receipt hold |
| `592918-AA-4` | MF1 2025-B2 LLC | real estate credit / CMBS | `209.559375M USD` | securitization vehicle visible; loan collateral hold |
| `91282C-LW-9` | U.S. Treasury | sovereign reserve / liquidity | `190.593750M USD` | mapped; operating borrower use not applicable |
| `28655*-AB-5` | Eliant Invest Holding LP | Apollo-related private credit / finance vehicle | `189.464130M USD` | platform-related issuer visible; borrower-use hold |
| `912810-TW-8` | U.S. Treasury | sovereign reserve / liquidity | `182.213263M USD` | mapped; operating borrower use not applicable |
| `91282C-MG-3` | U.S. Treasury | sovereign reserve / liquidity | `179.059922M USD` | mapped; operating borrower use not applicable |

## Source-Backed Interpretations

The map uses local Athene statutory rows as the base evidence, then adds public issuer/wrapper context where available:

1. Eliant: Apollo's SEC subsidiary exhibit lists Eliant Invest Holding LP and related Apollo Eliant entities. This supports platform-related issuer mapping, but not borrower/use proof.
2. AMAPS: Apollo describes AMAPS as a structured credit product with diversified corporate and asset-backed credit collateral, and Apollo/Athene investment disclosure identifies investment-grade ABS debt issued by AMAPS 1 LLC. This supports wrapper mapping, but not underlying collateral or borrower receipt.
3. Concord Music Royalties: Concord says it issued `1.765B USD` of senior notes, and KBRA says Series 2025 proceeds would redeem Series 2022-1 notes and support general corporate purposes. This supports borrower/wrapper and broad use proxy, but not Athene-specific cash receipt or remittance.
4. MF1 2025-B2: SEC transaction material names MF1 2025-B2 LLC in securitization servicing exhibits, and Fitch identifies MF1 2025-B2 LLC as a rated structured-finance entity. This supports securitization-vehicle mapping, but not loan-level collateral cash flow.
5. Treasury rows: local statutory descriptions are enough to classify the issuer as U.S. Treasury and the lane as sovereign reserve/liquidity rather than private borrower use.

## What This Tells Us In Simple Terms

The selected Athene cash-like proceeds are not all the same kind of money movement.

They point to at least five different lanes:

1. Apollo-related private credit or finance vehicles: AP Aristotle and Eliant
2. Apollo structured credit: AMAPS
3. royalty-backed finance: Concord Music Royalties
4. real estate credit / CMBS-style finance: MF1 2025-B2
5. sovereign reserve/liquidity assets: U.S. Treasury securities

That means Apollo/Athene insurance capital is showing up in named instruments that look like private credit, structured credit, royalties, real estate credit, and liquidity management.

But the borrower question is still mostly open. The map tells us where to look; it does not yet prove that cash reached a specific borrower, was used for a specific purpose, and returned through a waterfall to Athene.

## What This Proves

This pass proves:

1. the top same-CUSIP cash-like proceeds candidates can be organized by issuer/wrapper lane
2. `2.378326037B USD` of the selected cash-like proceeds sit in non-Treasury operating or securitization wrapper rows
3. AP Aristotle, Eliant, AMAPS, Concord, MF1, AA Infrastructure, and Treasury rows require different proof routes
4. AMAPS and Concord have stronger public wrapper/use context than a local statutory row alone
5. Treasury rows should be excluded from private borrower/use proof chases

## What It Does Not Prove

This pass does not prove:

1. borrower receipt
2. borrower use of proceeds
3. exact source-of-funds allocation from Athene liabilities into each asset
4. lot-level continuity
5. remittance or debt waterfall
6. liability-cost spread
7. IRR, NPV, ROIC, cash-on-cash return, or platform profit

## Required Documents To Finish Named Cash Proof

The next proof layer needs:

1. offering memoranda or note purchase agreements
2. collateral schedules or loan tapes
3. trustee/remittance reports
4. redemption, paydown, or repayment notices
5. Athene trade/allocation support
6. liability-cost or credited-rate schedule
7. issuer financials or borrower cash-flow support
8. return model or realized spread bridge

## Safe Claim

`The Athene same-CUSIP cash-like proceeds packet now maps 2.930192972B USD of selected cash-like consideration across Apollo-related private credit/finance vehicles, AMAPS structured credit, Concord music-royalty ABS, MF1 real estate credit, AA Infrastructure, and U.S. Treasury liquidity rows. The map identifies where the money appears to be routed economically and which documents would be needed next, but it does not prove borrower receipt, source/use, liability spread, or final asset-level return.`

## Decision

`apollo-athene-cashlike-proceeds-issuer-map-ready-for-borrower-source-acquisition`

The next move is source acquisition for the highest-leverage non-Treasury rows: Concord for public use-of-proceeds and remittance evidence, AMAPS for Apollo wrapper/collateral evidence, and Eliant/AP Aristotle for Apollo-related private issuer documents.

## Source Links

- Apollo AMAPS overview: `https://www.apollo.com/insights-news/insights/2026/05/introducing-amaps`
- Apollo/Athene investment disclosure: `https://www.sec.gov/Archives/edgar/data/1527469/000152746926000013/R12.htm`
- Apollo SEC subsidiary exhibit: `https://www.sec.gov/Archives/edgar/data/1411494/000141149422000014/exhibit211q42021.htm`
- Concord note issuance release: `https://concord.com/news/concord-closes-1-765-billion-abs-to-fuel-continued-growth/`
- KBRA Concord publication: `https://www.kbra.com/publications/ZLhcMNKm`
- MF1 SEC transaction exhibit: `https://www.sec.gov/Archives/edgar/data/2134864/000153949726001596/exh4_2-mf1psa.htm`
- Fitch MF1 entity page: `https://www.fitchratings.com/entity/mf1-2025-b2-llc-97720910`
