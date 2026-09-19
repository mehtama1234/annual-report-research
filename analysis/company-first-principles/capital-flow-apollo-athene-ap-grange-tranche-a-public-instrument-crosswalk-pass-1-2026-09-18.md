# Apollo/Athene AP Grange Tranche A public-instrument crosswalk pass 1

Research date: `2026-09-18`

## New crosswalk

The Athene Schedule D population contains a separate AP Grange Tranche A row,
distinct from the Schedule BA Tranche B row discussed in the [call-to-statutory
bridge](capital-flow-apollo-athene-ap-grange-call-statutory-bridge-pass-1-2026-09-18.md):

| Field | Athene Schedule D 2025 row |
| --- | ---: |
| Statutory identifier | `G2964#-AA-7` |
| Description | AP Grange Holdings LLC, AP Grange Sr Secured Tranche A |
| Coupon / maturity | `6.500%`, `03/20/2045` |
| NAIC designation | `2.A` |
| Actual cost | `$3,636.208008B` |
| Par value | `$3,635.055108B` |
| Fair value | `$3,859.188407B` |
| Book / adjusted carrying value | `$3,637.502713B` |
| Investment income | `$343.374413M` |
| Interest received during year | `$265.774068M` |
| Acquisition date | `12/22/2025` |

The raw statutory row preserves the same coupon and maturity and identifies
the position as affiliated (`2.A`).

A public N-2/A independently lists AP Grange Holdings LLC 6.50% convertible
bonds maturing 03/20/2045, acquired 04/14/2025. The filing shows a `$2.250M`
principal position and `$2.278125M` amortized cost for one listed position,
plus a separate `$250K` 5.00% position. See the [public N-2/A instrument
schedule](https://www.sec.gov/Archives/edgar/data/2067955/000119312525335256/d902005dn2a.htm),
pages 149–150 in the filing's pagination.

A later SSGA N-PORT filing provides the public identifier for the same
issuer/coupon/maturity family: CUSIP `00187RAA3`, ISIN `US00187RAA32`, issuer
country Cayman Islands, fixed coupon `6.500%`, and maturity `2045-03-20`. The
filing reports principal balance `$1.025M` and value `$1.081964M` for the March
31, 2026 report. See the [SSGA N-PORT record](https://www.sec.gov/Archives/edgar/data/1516212/000141036825041167/xslFormNPORT-P_X01/primary_doc.xml).

The decisive tuple join comes from an Apollo-provided transaction summary
distributed through SSGA's public fund-document library. Its AP Grange Senior
Notes table lists `US00187RAA32` as the identifier and `G2964#AA7` as the CUSIP,
alongside the same Cayman issuer, 6.50% coupon, June 2024 issue date, and
03/20/2045 maturity. See the [Apollo AP Grange transaction summary](https://www.ssga.com/library-content/products/fund-docs/etfs/us/ps/doc-ap-grange-prsd.pdf).

## What the crosswalk supports

The public record supports the instrument identity behind Athene's row when
the full issuer/coupon/maturity/identifier tuple is used:
Apollo's transaction summary maps public CUSIP `G2964#AA7` to ISIN
`US00187RAA32`, while Athene's statutory marker is the same identifier with a
statutory hyphen (`G2964#-AA-7`). The issuer, coupon, issue date, and maturity
also agree. This closes the identifier crosswalk, but not the cash-settlement
bridge:

`AP Grange 6.50% / 03-20-2045 instrument family -> Athene Schedule D Tranche A
holding -> Q2 2026 AP Grange call/gain disclosure`

It also separates the relevant Tranche A route from the smaller Schedule BA
Tranche B row (`G2964#-AB-5`).

`00187RAA3` / `US00187RAA32` is a confirmed public identifier for the 6.50%
instrument family, and `G2964#AA7` is the public-form match for Athene's
`G2964#-AA-7` when coupon and maturity are included. The statutory prefix is
not treated as a unique security key by itself: other statutory extracts show
visually similar `G2964*-AA-7` rows with different issuer labels or coupons.
The SSGA holder records remain holder-level corroboration only; they do not
establish Athene's lot balance or settlement.

## Additional credit-quality control

A Kentucky Employers' Mutual Insurance Authority quarterly statement also
identifies `G2964#AA7` as an AP Grange security and says its terms permit the
lender to defer accrued and unpaid interest and principal amounts otherwise
due on a quarterly payment date. KEMI reports that it nonadmitted amounts over
90 days due. This is independent-holder evidence, not an Athene delinquency
record, but it is an important cash-versus-accrual control for interpreting
Athene's `$343.374M` investment-income figure against `$265.774M` of interest
received. See the [KEMI quarterly statement](https://apps.legislature.ky.gov/AgencyReports/IJC/AR/KEMI/C2025/Quarterly%20Statement%2006-30-25.pdf).

A Moody's life-insurance portfolio table separately labels `G2964#AA7` AP
Grange senior debt and `G2964#AB5` AP Grange subordinated debt. That supports
keeping the Schedule D Tranche A and Schedule BA Tranche B routes separate,
but does not establish valuation or repayment. See the [Moody's portfolio
table](https://d1e00ek4ebabms.cloudfront.net/production/uploaded-files/Sector_In-Depth-Life-Insurance-US-Life-17Jun2025-PBC_1442118-13e5e8a3-b692-4b9c-88d2-d9ed4ece1b4e.pdf).

## What it does not support

The public N-2/A position is held by another investment fund and is not an
Athene trade confirmation. Matching coupon and maturity do not prove CUSIP,
lot identity, ownership, settlement, or call proceeds. The public position's
04/14/2025 acquisition date also differs from Athene's 12/22/2025 acquisition
date.

The SSGA N-PORT position is holder-level evidence. Its March 31, 2026
position does not show a call notice, paying-agent payment, Athene allocation,
or any relationship to Athene's `$3.638B` position. It corroborates the public
identifier and instrument terms, not Athene cash.

Athene's Schedule D Part 4 rows for `G2964#-AA-7` show two earlier 2025
disposals—`$2.249993M` to Apollo Global Securities, LLC and `$33.489724M` to
AARe–Sony Life [Block] Trust—but those occurred before the year-end holding's
12/22/2025 acquisition date. They are continuity clues, not proof of the
Q2-2026 call settlement or a same-lot cash return.

The `$673M` Q2 AP Grange gain remains an issuer-level observation. No public
call notice, affected-CUSIP schedule, paying-agent statement, or Athene cash
ledger has been found that allocates it to `G2964#-AA-7`.

## Decision

`ap-grange-tranche-a-identifier-and-instrument-terms-confirmed; athene-lot-call-settlement-hold`

Structured result: [AP Grange Tranche A cash/accrual crosswalk CSV](data/capital-flow-apollo-athene-ap-grange-tranche-a-cash-accrual-crosswalk-2026-09-18.csv).

The next source should identify the exact call notice, payment date, paying
agent, and Athene allocation, then reconcile the `$3.638B` year-end Tranche A
position, the earlier Part 4 dispositions, and the `$673M` gain to dated
settlement proceeds. Do not add the public N-2/A or SSGA positions to Athene
holdings or cash.
