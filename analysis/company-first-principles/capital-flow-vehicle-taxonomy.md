# Capital Flow Vehicle Taxonomy

## Purpose

The borrower exposure table says where the credit is landing.

The holder source-of-funds map says which filing vehicles or transaction sources appear.

This taxonomy adds the missing control layer: what kind of vehicle is each holder or source?

Machine-readable table:

`analysis/company-first-principles/data/capital-flow-vehicle-taxonomy.csv`

## Simple Answer

We should not treat every private-credit row as the same kind of money.

The current evidence set has:

- `5` public BDCs
- `4` non-traded BDC / private-credit-fund labels
- `1` direct-lending program / private-credit vehicle
- `2` registered credit fund labels
- `1` private credit fund
- `1` middle-market lending fund
- `1` prior bank facility denominator
- `1` arranger-only source

The taxonomy makes the research safer. It lets us say “this borrower appears in a public BDC schedule” or “this borrower appears in an Ares-linked direct-lending program schedule” without jumping to “insurance money funded this loan” unless the source document proves that connection.

## Vehicle Classification Table

| Reporting Entity | Manager / Platform | Vehicle Taxonomy | Channel Group | Confidence | Borrower Cases |
|---|---|---|---|---|---|
| Ares Capital Corporation | Ares | Business development company | Public BDC | high | Valcourt; Sunvair; AeriTek; MAI Capital |
| FS KKR Capital Corp. | KKR / FS | Business development company | Public BDC | high | Frontline Road Safety; Atwell |
| Goldman Sachs BDC Inc. | Goldman Sachs | Business development company | Public BDC | high | Frontline Road Safety; Relation Insurance |
| Blue Owl Capital Corporation | Blue Owl | Business development company | Public BDC | high | Precinmac |
| Kayne Anderson BDC Inc. | Kayne Anderson | Business development company | Public BDC | high | AeriTek |
| KKR FS Income Trust Select | KKR / FS | Non-traded BDC or private credit fund | Non-traded BDC / private credit fund | medium | Frontline Road Safety; Atwell |
| Ares Strategic Income Fund | Ares | Non-traded BDC or private credit fund | Non-traded BDC / private credit fund | medium | Frontline Road Safety; Sunvair; AeriTek; MAI Capital |
| Goldman Sachs Private Credit Corp. | Goldman Sachs | Non-traded BDC or private credit fund | Non-traded BDC / private credit fund | medium | Frontline Road Safety; Relation Insurance |
| Senior Direct Lending Program LLC | Ares-linked SDLP | Direct-lending program / joint venture-style credit vehicle | Direct lending program / private credit vehicle | medium | Valcourt; Precinmac |
| CION Ares Diversified Credit Fund | CION / Ares | Registered credit fund | Registered credit fund | medium | Sunvair |
| New Mountain Private Credit Fund | New Mountain | Private credit fund | Private credit fund | medium | MAI Capital |
| New Mountain Guardian IV BDC LLC | New Mountain | Non-traded BDC or private credit fund | Non-traded BDC / private credit fund | medium | MAI Capital |
| Cliffwater Corporate Lending Fund | Cliffwater | Registered credit fund / private credit fund | Registered credit fund | medium | Valcourt |
| Phillip Street Middle Market Lending Fund LLC | Goldman Sachs / Phillip Street | Middle-market lending fund | Middle-market lending fund | medium | Relation Insurance |
| Bank of America-led facility | Bank lender group | Bank-administered credit facility | Bank credit facility | medium | Atwell |
| Ares Management Corporation | Ares | Arranger / asset manager | Financing arranger role only | high | Jiffy Lube / Premium Velocity Auto; Frontline Road Safety; Relation Insurance |

## What The Taxonomy Changes

Before this pass, the research could say:

Private credit is funding these operating companies.

After this pass, the better claim is:

Named operating-company borrowers appear in disclosed credit holdings across public BDCs, non-traded/private-credit vehicles, direct-lending program vehicles, and other credit funds. Transaction releases also show private-credit arranger roles where holder-dollar filings have not yet been captured.

That is stronger because it is more exact.

## What Each Channel Proves

| Channel | What It Proves | What It Does Not Prove |
|---|---|---|
| Public BDC | A public SEC-reporting credit vehicle held borrower debt or commitments. | It does not identify every lender or ultimate shareholder source. |
| Non-traded BDC / private credit fund | A private or non-listed credit vehicle held borrower debt or commitments. | It does not by itself prove insurance funding, pension funding, or full facility size. |
| Direct-lending program / private credit vehicle | A named direct-lending program held borrower exposure. | It does not prove ownership, source of capital, or syndicate composition without vehicle notes. |
| Registered credit fund | A registered fund reported borrower exposure. | It does not prove the whole debt package or capital-provider origin. |
| Middle-market lending fund | A middle-market lending vehicle reported borrower exposure. | It may be historical and may not represent current financing. |
| Bank credit facility | A bank-administered facility existed as a denominator. | It does not prove later repayment or displacement. |
| Arranger-only source | A private-credit platform arranged or led financing. | It does not prove funded exposure, allocation, or final lender group. |

## Why This Matters

The deeper research question is not only “what is private credit buying?”

It is:

Who is routing capital into these operating companies, through which vehicles, and with what claim strength?

This taxonomy prevents three common overclaims:

- equating an arranger role with actual funded exposure
- equating a BDC holder row with insurance-funded credit
- equating one holder slice with total borrower debt

## Next Documents To Pull

The next evidence layer is vehicle-level documentation:

| Vehicle Group | Needed Documents | Purpose |
|---|---|---|
| Public BDCs | 10-K/10-Q capital structure notes, debt-funding notes, shareholder mix, adviser agreement | Determine whether BDC assets are funded by public equity, notes, credit facilities, SPVs, or adviser-linked structures. |
| Non-traded BDCs / private-credit funds | Prospectus, registration statement, annual report, distribution-channel disclosure | Identify investor source and whether retail/wealth/insurance channels are involved. |
| Direct-lending program vehicles | Formation notes, ownership split, member capital, related-party disclosures | Determine whether the vehicle is a joint venture, managed program, insurance-linked account, or other structure. |
| Insurance-linked platforms | Statutory statements, Schedule D/BA, rating reports, affiliated-investment notes | Prove whether insurer liabilities are actually backing a given credit channel. |
| Transaction arranger cases | Credit agreements, lender allocation schedules, rating reports | Convert arranger-role evidence into facility-size and holder-allocation evidence. |

## Current Bottom Line

The source-of-funds question is now split into two layers:

1. Visible holder channel: we can already classify the filing vehicle or transaction source.
2. Ultimate capital source: this still needs vehicle-level annual reports, prospectuses, statutory filings, and rating reports.

That is the right direction. It keeps the borrower-dollar claims hard while giving us a clear path toward the deeper “who is funding it?” question.
