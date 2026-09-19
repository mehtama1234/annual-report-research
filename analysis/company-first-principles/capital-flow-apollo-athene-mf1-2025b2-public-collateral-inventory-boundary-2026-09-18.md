# MF1 2025-B2 public collateral inventory boundary

Research date: `2026-09-18`

## Result

`mf1-2025b2-named-collateral-objects-public; underlying-tape-and-cash-open`

The SEC-filed agreed-upon-procedures report for MF1 2025-B2 states that the
company-provided `MF1 2025-B2 Data Tape CSR.xlsx` contains information on `23`
collateral interests and `74` related mortgaged properties as of April 9,
2025. Its instructions attachment names the 23 collateral-interest/property
objects used for selected comparison or recomputation procedures:

- Citizen Bayonne
- 1909 Rittenhouse
- Oaklyn
- Woodside Central
- Metro Edgewater
- Reserve
- The Villas at Tuttle Royale
- Swells Cottages
- The Arc at Westchester Place
- Broadstone Axis
- Avilla Traditions
- Avilla Springs
- Avilla Lakeridge
- Creekside
- Mossdale Landing
- Central Florida Portfolio
- Granby Oaks
- Concourse Westchester
- 1110 S Hobart Blvd
- Wyvernwood
- ARIUM Greenview
- ARIUM Crowntree Lakes
- Jones Estates MHC Portfolio - Pool B

This is a material upgrade over a count-only collateral reference. It gives
the acquisition route a concrete property/loan inventory and connects the
public CTSLink metadata names `Woodside Central` and `Broadstone Axis` to the
same MF1 2025-B2 collateral universe as named report targets.

## Critical series boundary

The locally captured SEC transaction exhibit is not a 2025-B2 collateral
schedule. It is headed `MF1 2026-FL21 - Servicing Agreement`; its Exhibit A
lists a different 2026-FL21 portfolio, including The Lightwell, The Legacy
Portfolio, The Westline, Crossings at Raritan Station, and other assets, with
separate closing and delayed collateral interests. No public crosswalk has
been found that maps those 2026-FL21 assets to MF1 2025-B2 or to Athene CUSIP
`592918-AA-4`.

Accordingly, that agreement can support generic servicing and remittance
mechanics only. It cannot be used as the MF1 2025-B2 asset schedule, borrower
ledger, or Athene cash evidence.

Independent North Carolina public-holder records add security-level
corroboration and a short continuity screen:

| As-of date | Public description | Par | Reported market value |
|---|---|---:|---:|
| 2025-09-30 | MF1 2025-B2 LLC B2 A 144A | `$4,000,000` | `$4,010,826` |
| 2025-11-30 | MF1 2025-B2 LLC B2 A 144A | `$4,000,000` | `$4,010,575` |
| 2025-12-31 | MF1 2025-B2 LLC B2 A 144A | `$4,000,000` | `$4,010,842` |
| 2026-01-31 | MF1 2025-B2 LLC B2 A 144A | `$4,000,000` | `$4,010,750` |

The repeated class description, `04/21/2025` deal date, `05/18/2040`
maturity, and unchanged `$4.0M` par strengthen the public instrument-identity
and continuity screen. They do not identify Athene as holder, prove a CUSIP-
level remittance, show collateral-to-bond allocation, or establish that the
position was held continuously by one investor.

## What the public exhibit actually proves

The report is an agreed-upon-procedures description, not a published loan
tape or servicing report. Its compared-attribute tables identify fields such
as property address, city, state, county, property type, units, occupancy,
loan balance, debt yield, DSCR, ownership interest, loan purpose, and payment
dates, along with the source documents used to test them. The instructions
also mark selected values as `Provided by the Company`, including several
DSCR, margin, occupancy, appraisal, property-manager, and affiliated-sponsor
attributes.

The exhibit therefore proves:

1. a dated 23-collateral-interest / 74-property data-file population;
2. the names of the 23 collateral-interest/property objects used in the
   procedures; and
3. the intended attribute and source-document schema for diligence.

It does not publish the underlying `Data Tape CSR.xlsx`, a full borrower or
property-address inventory, current balances, period collections, servicing
status, account deposits, trustee remittances, noteholder allocations, or
Athene ownership/receipt. The named objects are not, by themselves, evidence
of a cash realization or return.

## Join boundary

The statutory candidate remains Athene CUSIP `592918-AA-4`, labeled MF1
2025-B2 LLC in the corrected Schedule D packet. The public collateral names
now provide a candidate asset-side crosswalk, but no public source yet joins
that CUSIP to an individual named object, borrower legal entity, custodian
record, or same-period cash report.

```text
Athene CUSIP 592918-AA-4
  -> MF1 2025-B2 LLC statutory row
  -> 23 named collateral-interest/property objects / 74 properties
  -> gated data tape and current CTSLink collateral/servicing reports
  -> unresolved borrower collections, trustee remittance, Athene allocation,
     liability-cost-adjusted return, and Apollo common-owner cash
```

## Next source object

The next useful acquisition is the authorized investor copy of the data tape
or CREFC Loan Set Up/Loan Periodic files, followed by the same-period
Distribution Date Statement and Bond Level file. Promotion requires a
property or borrower identifier, loan balance/status, gross collections,
collection-account deposit, trustee remittance, security-level allocation,
and Athene receipt or custody evidence. Until that join exists, Q-12 remains
`evidence-insufficient`.

## Sources

- [MF1 2025-B2 data-file agreed-upon-procedures exhibit](../../raw/primary-sources/capital-flow/mf1/2025-05/mf1-2025-b2-data-file-procedures-ex99-1.htm).
- [MF1 2026-FL21 servicing agreement captured in the transaction-exhibit route](../../raw/primary-sources/capital-flow/mf1/2026-03/mf1-2025-b2-transaction-exhibit.htm) (mechanics only; series mismatch noted above).
- [MF1CAP 2025B2 CTSLink series page](https://www.ctslink.com/a/seriesdocs.html?seriesId=2025B2&shelfId=MF1CAP).
- [MF1CAP 2025B2 additional documents](https://www.ctslink.com/a/seriesdocs.html?seriesId=2025B2&shelfId=MF1CAP&tab=ADDDOC).
- [North Carolina public market holdings record, January 31, 2026](https://www.nctreasurer.gov/documents/files/ncia/ncrs-public-markets-holdings-direct-ownership-01-31-26/download?attachment=).
- [North Carolina public market holdings record, September 30, 2025](https://www.ncinvest.gov/media/239/download?attachment=).
- [North Carolina public market holdings record, November 30, 2025](https://www.nctreasurer.gov/documents/files/ncia/ncrs-public-markets-holdings-direct-ownership-11-30-25/open).
- [North Carolina public market holdings record, December 31, 2025](https://www.nctreasurer.gov/documents/files/ncia/ncrspublicmarketsholdingsdirectownership123125/open).
