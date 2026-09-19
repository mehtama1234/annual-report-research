# Capital Flow Ares Borrower Holder Expansion Pass 1

## Purpose

This pass normalizes the borrower-level holder work across the Ares selected-borrower lane.

The operating table is:

`analysis/company-first-principles/data/capital-flow-ares-borrower-holder-expansion-pass-1.csv`

It does not replace the individual borrower crosswalks. It turns them into one row-level proof table that preserves holder vehicle, vehicle taxonomy, capital-channel group, period, instrument, funded value, unfunded commitment, transaction context, and claim boundary.

## Source Set

The normalized source set covers:

- AeriTek
- Atwell
- Frontline Road Safety
- MAI Capital
- Precinmac
- Relation Insurance
- Sunvair
- Valcourt
- Jiffy Lube / Premium Velocity Auto

## Normalized Result

The pass emits `95` normalized rows across `16` holder/source channel groups: `74` funded-holder rows, `8` pure unfunded-commitment rows, plus holder-locator and transaction-gap rows.

The row-level table preserves every extracted row, including historical, comparative, mixed-quarter, and locator rows. Its row-level sums are useful for audit coverage, not for promoted exposure totals:

| Metric | Amount | Boundary |
|---|---:|---|
| Row-level fair-value audit sum | `4683.4920M USD` | Mixed periods and comparative rows; do not promote as same-date exposure. |
| Row-level unfunded-commitment audit sum | `462.3293M USD` | Mixed periods and commitment rows; do not add to drawn exposure. |
| Unique borrower transaction / bank denominator context | `1500.0000M USD` | Atwell prior bank facility plus Jiffy sale value; not facility-size proof for the other borrowers. |

For promoted borrower-level totals, use the master rollup rather than the row-level audit sum:

| Master-Rollup Metric | Amount | Boundary |
|---|---:|---|
| Latest visible funded fair value across holder-dollar cases | `1157.8648M USD` | Deduped by borrower case at the current best visible period. |
| Mixed-quarter visible funded fair value, including selected extra rows | `1234.5575M USD` | Useful for reach, not same-date exposure. |
| Visible unfunded commitments across cases | `153.5020M USD` | Commitments are not drawn debt. |
| Hard transaction / bank denominator values captured | `1500.0000M USD` | Atwell prior bank facility plus Jiffy transaction value. |

The same-period borrower summary is:

`analysis/company-first-principles/data/capital-flow-ares-borrower-same-period-exposure-summary-pass-1.csv`

It selects one actual reporting period per borrower before summing fair value or commitments.

## Holder-Source Taxonomy

The taxonomy layer classifies each reporting entity or transaction source before any source-of-capital claim is promoted.

| Capital Channel Group | Normalized Rows | Boundary |
|---|---:|---|
| derived summary | `1` | Computed gap/status row; not a holder vehicle. |
| direct lending program / private credit vehicle | `7` | Program-level holder visibility; ownership and capital source still need vehicle notes. |
| financing arranger role only | `3` | Arranger/bookrunner context; not funded allocation. |
| financing-source context | `1` | Legal-advisor financing context; not full lender group. |
| middle-market lending fund | `1` | Middle-market fund holder visibility, often historical. |
| multi-vehicle summary | `7` | Derived summary row; use underlying rows for holder proof. |
| non-traded BDC / private credit fund | `17` | Private or non-listed credit vehicle visibility; investor channel still needs vehicle documents. |
| private credit / filing-source route evidence | `2` | Route evidence with unit/context limits. |
| private credit fund | `4` | Private credit fund holder visibility; investor source still unproven. |
| public BDC | `29` | SEC-reporting BDC holder rows; does not identify ultimate shareholder source. |
| registered credit fund | `7` | Registered fund holder visibility; not whole facility proof. |
| search status | `1` | Search-result status row; not exposure proof. |
| sponsor transaction context | `2` | Sponsor transaction source; not lender allocation. |
| transaction context | `3` | Transaction source context; not holder evidence or facility-size proof. |
| transaction value context | `2` | Transaction value source; not debt facility size unless source says so. |
| unclassified | `8` | Classification needs follow-up documentation. |

## Same-Period Borrower Summary

This table is the conservative current-period control. It deliberately excludes derived `latest visible 2026` rows and older periods when a newer actual reporting period exists.

| Borrower | Selected Period | Same-Period Rows | Fair Value | Unfunded Commitment | Excluded Periods | Boundary |
|---|---|---:|---:|---:|---|---|
| AeriTek | Q2 2026 | `2` | `59.6000M USD` | `0.0000M USD` | FY2025; FY2025 comparative; Q1 2026; Q3 2025 | Not full facility size or total debt. |
| Atwell | Q2 2026 | `4` | `7.1860M USD` | `0.8880M USD` |  | Not full facility size or total debt. |
| Frontline Road Safety | Q2 2026 | `16` | `622.8244M USD` | `130.7960M USD` | Q1 2026 | Not full facility size or total debt. |
| MAI Capital | Q2 2026 | `1` | `8.0000M USD` | `0.0000M USD` | 2025; FY2025 comparative; Q1 2026; Q3 2024 | Not full facility size or total debt. |
| Precinmac | FY2024 | `4` | `274.8560M USD` | `8.3720M USD` |  | Not full facility size or total debt. |
| Relation Insurance | Q2 2026 | `7` | `4.5480M USD` | `1.1960M USD` | FY2024; Q1 2026 | Not full facility size or total debt. |
| Sunvair | Q2 2026 | `2` | `68.1000M USD` | `0.0000M USD` | Q1 2025; Q1 2026; Q2 2024 | Not full facility size or total debt. |
| Valcourt | Q2 2026 | `1` | `117.6000M USD` | `0.0000M USD` | FY2023; FY2023 comparative; FY2024; FY2024 comparative; Q1 2026; Q4 2025; Q4 2025 comparative | Not full facility size or total debt. |
| Jiffy Lube / Premium Velocity Auto | no holder-dollar period captured | `0` |  |  |  | Not full facility size or total debt. |

## Borrower Summary

| Borrower | Sector Lane | Rows | Funded Rows | Commitment Rows | Fair Value Sum | Unfunded Sum | Transaction / Bank Denominator | Main Boundary |
|---|---|---:|---:|---:|---:|---:|---:|---|
| AeriTek | commercial refrigeration and foodservice equipment | `9` | `9` | `0` | `176.3085M USD` |  |  | `facility-size-missing` |
| Atwell | critical infrastructure and engineering services | `5` | `5` | `3` | `16.1440M USD` | `1.7760M USD` | `200.0000M USD` | `prior-bank-denominator-visible; current-facility-size-missing` |
| Frontline Road Safety | roadway safety and infrastructure services | `22` | `17` | `6` | `898.1921M USD` | `238.7840M USD` |  | `facility-size-missing` |
| MAI Capital | wealth-management advisory consolidation | `11` | `8` | `4` | `113.5596M USD` | `26.2522M USD` |  | `facility-size-missing` |
| Precinmac | precision manufacturing, aerospace, defense, semiconductor, and power | `5` | `5` | `3` | `549.7400M USD` | `16.7440M USD` |  | `facility-size-missing` |
| Relation Insurance | insurance brokerage consolidation | `14` | `8` | `4` | `36.9690M USD` | `159.8200M USD` |  | `facility-size-missing` |
| Sunvair | aerospace MRO services | `10` | `10` | `0` | `279.7418M USD` |  |  | `facility-size-missing` |
| Valcourt | building maintenance and facility services | `12` | `12` | `2` | `2612.8370M USD` | `18.9531M USD` |  | `facility-size-missing` |
| Jiffy Lube / Premium Velocity Auto | automotive services franchising | `7` | `0` | `0` |  |  | `1300.0000M USD` | `facility-size-missing` |

## What This Adds

This is the missing sector-level proof layer between individual borrower pages and the master rollup.

The new table lets the research ask, row by row:

- which credit vehicle holds the borrower exposure
- whether the row is funded value, unfunded commitment, locator evidence, or transaction context
- what borrower sector the exposure belongs to
- whether transaction-role evidence is linked or still separate
- whether facility size and bank replacement are proven or still missing

## Safe Claim

`The Ares borrower-destination lane now has a normalized holder-expansion table across nine borrower cases. The table preserves row-level holder vehicles, holder-source taxonomy, filing periods, instruments, funded fair values, unfunded commitments, transaction context, and proof boundaries. It supports borrower-destination claims across services, infrastructure-adjacent services, aerospace/industrial supply chains, insurance brokerage, wealth management, and automotive services, but it does not prove total facility size, Ares' exact funded amount, full lender groups, use of proceeds, ultimate capital source, or bank replacement.`

## Claims Not To Make Yet

Do not say:

- the row-level fair-value sum is total private-credit exposure
- visible BDC fair value equals total borrower debt
- unfunded commitments are already drawn debt
- every holder row maps to the named Ares selected-borrower transaction
- private credit replaced banks in these cases unless borrower-specific payoff, termination, amendment, or lender replacement evidence exists

## Next Concrete Work

1. Search facility-size and bank-replacement documents for Frontline, Relation, Precinmac, and Valcourt first.
2. Pull vehicle-level annual reports, prospectuses, and funding notes for public BDC and non-traded/private-credit vehicles.
3. Add Q3 2026 schedule refresh checks for Jiffy/PVA and the borrowers with Q2-only evidence.
4. Add a transaction-to-holder confidence upgrade only when a credit agreement, rating report, amendment, or lender allocation source links the rows.
