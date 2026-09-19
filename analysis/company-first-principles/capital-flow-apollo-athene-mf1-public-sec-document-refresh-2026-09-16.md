# Apollo/Athene MF1 Public SEC Document Refresh

Research date: `2026-09-16`

## Purpose

This refresh tests the MF1 2025-B2 candidate in Q-12's Apollo/Athene
statutory named-asset queue:

`named statutory candidate -> public wrapper/collateral document -> servicing/remittance route -> Athene ownership -> liability-adjusted return`

## Public evidence

The SEC-filed agreed-upon-procedures report for MF1 REIT III identifies:

- MF1 2025-B2 LLC as the offering vehicle;
- 23 collateral interests and 74 related mortgaged properties in the data file
  as of the April 9, 2025 cut-off date;
- J.P. Morgan Securities, Morgan Stanley, Goldman Sachs, Atlas SP Securities
  (a division of Apollo Global Securities), and Atlas SP Partners as specified
  parties; and
- an electronic collateral data file reviewed for specified attributes.

This is a meaningful public wrapper and collateral route. It provides a
document-backed way to inspect asset composition and transaction participants,
and it is materially stronger than a platform-AUM reference.

## What remains unproven

The report does not establish that Athene owned the selected `592918-AA-4`
position, that Athene received a particular remittance, that a borrower paid
cash into the deal during the relevant period, or that any proceeds reached
Apollo common owners. It also does not by itself provide a complete trustee
waterfall, liability-cost allocation, lot continuity, or realized return.

| Gate | Result |
| --- | --- |
| Public named wrapper | `pass` |
| Collateral-count and property-count route | `pass` |
| Apollo-affiliated transaction participant | `pass — Atlas SP Securities / Apollo Global Securities named` |
| Athene legal-entity ownership of candidate CUSIP | `hold` |
| Trustee remittance or borrower receipt | `hold` |
| Liability-adjusted spread or return | `hold` |
| Apollo common-owner cash | `hold` |

## Decision

`evidence-insufficient — MF1 wrapper/collateral route strengthened; Athene lot, receipt, waterfall, and return remain unjoined`

The correct next documents are the MF1 offering memorandum, pooling and
servicing agreement, trustee remittance reports, collateral tape, and Athene
custodian or statutory lot records that connect the named CUSIP to the legal
entity. This observation does not change Q-12's result class.

## Official source

- SEC-filed MF1 2025-B2 data-file procedures report:
  https://www.sec.gov/Archives/edgar/data/1991416/000153949725001106/n4961_x1exh99-1.htm

Key source location checked: SEC filing lines 17–26.
