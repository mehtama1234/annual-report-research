# MF1 2025-B2 remittance-access boundary

Research date: `2026-09-17`

The public MF1 2025-B2 series page identifies current CREFC loan-periodic and
restricted-servicer-report routes, but the listed documents require sign-in.
The public SEC exhibits therefore establish the servicing and collateral
perimeter, while the actual remittance and loan-level cash reports remain
access-controlled in the checked public route. The page itself is preserved
locally so the report names, login boundary, and access state can be rechecked
without relying on a search snippet.

## Current CTSLink report inventory — 2026-09-18

The public series page currently lists the following report routes:

| Report | Current public cycle | Access state | Cash-proof use if obtained |
| --- | --- | --- | --- |
| Distribution Date Statement | `09/18/2026` | Sign-in/certification required | Trustee/payment-date distribution and noteholder allocation. |
| CREFC Bond Level File | `09/18/2026` | Sign-in/certification required | Bond-level principal, interest, and balance fields. |
| CREFC Collateral Summary File | `09/18/2026` | Sign-in/certification required | Pool and collateral-level composition. |
| CREFC Loan Periodic Update | `09/18/2026` | Sign-in/certification required | Loan-level balance, payment, and status fields. |
| CREFC Restricted Servicer Report | `09/18/2026` | Sign-in/certification required | Servicing, delinquency, collection, and remittance support. |

The page now shows the September 18 cycle as current and October 19 as the next
cycle. The public page explicitly says that one or more reports are restricted
to investors and other specified parties and
directs users to complete an investor, borrower/affiliate, NRSRO, or market-data
provider certification.

| Route | Result | Safe interpretation |
| --- | --- | --- |
| CTSLink MF1CAP / 2025B2 series page | `located-access-controlled` | A current report route exists for loan-periodic and servicer reporting; report contents are not public in the checked session |
| SEC data-procedures exhibit | `public-source-confirmed` | The exhibit names “MF1 2025-B2 Data Tape CSR.xlsx” and identifies `23` collateral interests and `74` related mortgaged properties, but does not attach or link the workbook; compared/recomputed attributes are public, values are not |
| SEC servicing agreement | `public-source-confirmed` | Collection accounts, servicing duties, record keeping, and default-collateral mechanics are specified |

This boundary does not prove that a report is unavailable to authorized
noteholders. It identifies two distinct next acquisition paths—the named
“MF1 2025-B2 Data Tape CSR.xlsx” and the gated CREFC/remittance reports—and
prevents either a filing description or a gated report route from being treated
as observed borrower cash or trustee remittance.

The current public page therefore upgrades the route from a generic
access-controlled reference to a dated report inventory, but it does not change
Q-12's `evidence-insufficient` result class.

The [September 18 metadata refresh](capital-flow-apollo-athene-mf1-2025b2-ctslink-metadata-refresh-2026-09-18.md)
adds the deal-document and additional-report inventory now visible on the
public page, including Q1/Q2 2026 quarterly reports, CREFC CMDR files, and
named asset-status reports for Broadstone Axis and Woodside Central. These are
acquisition targets, not observed report contents or cash evidence.

Structured control: [MF1 remittance-access CSV](data/capital-flow-apollo-athene-mf1-remittance-access-boundary-2026-09-16.csv).

Primary route: [CTSLink MF1CAP 2025B2 series documents](https://www.ctslink.com/a/seriesdocs.html?seriesId=2025B2&shelfId=MF1CAP).

## Live CTSLink recheck — 2026-09-18

The public CTSLink page now shows the September 18 cycle as current and the
October 19 cycle as next. The Distribution Date, Bond Level, Collateral
Summary, Loan Periodic, and Restricted Servicer routes remain
sign-in/certification gated. This confirms publication metadata but adds no
report content, borrower collection, trustee remittance, Athene receipt, or
return evidence.
