# Apollo–Athene statutory same-CUSIP bridge upgrade

Research date: `2026-09-15`

## Purpose

This pass promotes the strongest locally reproducible part of the Athene
statutory lane: a same-CUSIP bridge from a year-end legal-entity holding to a
dated Schedule D disposal or proceeds row, with the source page and numeric
fields preserved. It does not promote the bridge to borrower cash or final
investment return.

The underlying source is the locally acquired Athene Annuity and Life Company
2025 statutory statement:

`raw/primary-sources/capital-flow/apollo/athene/statutory/2025/athene-annuity-and-life-company-2025-statutory-statement.pdf`

## Evidence bridge

| Route | Holding evidence | Disposal / proceeds evidence | Conservative conclusion |
| --- | --- | --- | --- |
| AMAPS 1 LLC Tranche A Note, CUSIP `02300A-AA-8` | Schedule D Part 1 Section 2, PDF page `6023`: book/adjusted carrying value `$1.9175B`, interest income `$48.871M`, maturity `07/31/2070` | Schedule D Part 4, PDF page `6276`: dated `10/24/2025`, counterparty `Apollo Capital Markets Partner`, consideration `$268.000M`, interest/dividends `$3.987M` | Same legal-entity CUSIP is visible in both the year-end holding and a dated cash-like disposal/proceeds row |
| Concord Music Royalties LLC TUNES 2025-3A A, CUSIP `20633K-AN-8` | Schedule D Part 1 Section 2, PDF page `6025`: book/adjusted carrying value `$215.168M`, interest income `$3.313M`, maturity `07/20/2075` | Schedule D Part 5, PDF page `6334`: dated `07/01/2025`, counterparties `Santander US Capital Markets L` and `AARE Surplus AAM`, consideration `$229.053M`, book value at disposal `$224.990M`, interest/dividends `$4.733M` | Same legal-entity CUSIP is visible in both the year-end holding and an acquisition/disposal schedule row with a populated consideration field |

## What is now proven

1. The Athene statutory source can be cited at page level for two named
   issuer/CUSIP routes.
2. Each route has a year-end holding row and a separate dated Schedule D
   disposal/proceeds row.
3. The AMAPS route has a visible named Apollo-related counterparty label on
   the disposal row.
4. The Concord route has a visible named market/intermediary and affiliate
   counterparty context on the acquisition/disposal row.
5. The holding-side book value and interest fields are separated from the
   disposal-side consideration fields; they are not silently treated as one
   cash number.

## What remains deliberately unproven

The bridge does not prove:

- lot-level continuity between the holding and disposal rows;
- that the statutory consideration equals a settled cash receipt rather than
  another disposition or accounting event;
- the underlying borrower or collateral cash use;
- Athene's allocation across subsidiaries or custodians;
- liability funding cost, capital charge, impairment allocation, or net spread;
- Apollo parent collection or unrestricted HoldCo cash; or
- IRR, NPV, ROIC, payback, or common-owner residual.

The correct proof grade is therefore `same-cusip-statutory-bridge-visible`,
not `full named-cash proof`.

## Reproducibility

The structured rows are recorded in
`data/capital-flow-apollo-athene-statutory-same-cusip-bridge-upgrade-2026-09-15.csv`
and promoted into the canonical Apollo ledger as `APO-071` and `APO-072`.
The source rows can be rechecked against the full-range parser and the
page-specific raw-text inspection packets already in this repository.

## Next upgrade

Obtain the AMAPS or Concord offering/trustee/custodian records and Athene
allocation ledger. The decisive test is to match the statutory consideration
to a dated settlement, then join collateral remittance, liability cost, and
realized return.
