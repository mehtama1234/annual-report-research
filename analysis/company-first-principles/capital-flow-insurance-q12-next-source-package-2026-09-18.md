# Insurance statutory named-asset Q-12 next-source package

Research date: `2026-09-18`

## Purpose

Q-12 already has a platform-selection and named-asset proof ladder. It does
not yet have a single execution packet for moving from statutory rows and
interest-received proxies to settlement, liability cost, remittance, and
return. This package supplies that next layer for Apollo/Athene and
KKR/Global Atlantic/Accordia.

The machine-readable companion is the [Q-12 source-package CSV](data/capital-flow-insurance-q12-next-source-package-2026-09-18.csv).

The current-period Accordia legal-entity control is preserved in the [Q2 2026 statutory cash-flow refresh](capital-flow-kkr-global-atlantic-accordia-q2-2026-statutory-cash-flow-refresh-2026-09-18.md)
and its [structured companion](data/capital-flow-kkr-global-atlantic-accordia-q2-2026-statutory-cash-flow-refresh-2026-09-18.csv).

## Q2 2026 AAIA named-asset scan

The official [Athene statutory-filings page](https://ir.athene.com/financial-information/statutory-filings)
provides the Q2 2026 AAIA statement. Its Schedule D Part 3/4 pages add
current-period named-asset controls to the Apollo/Athene side of Q-12:

| Named route | Current statutory observation | Safe status |
| --- | --- | --- |
| AMAPS 1 `02300A-AA-8` | Part 3 PDF page `2470`: acquired `06/23/2026` from `ALRe Corporate AAM`; `$120.700M` actual cost/par; `$2.661M` paid accrued interest/dividends. | Same-CUSIP acquisition/affiliated-counterparty candidate; no settlement or collateral receipt. |
| MF1 2025-B2 A `592918-AA-4` | Part 3 PDF page `2468`: acquired `06/23/2026` from `AARE Surplus AAM`; `$58.538417M` actual cost; `$58.547M` par; `$42.814K` accrued interest. Part 4 PDF page `2577` separately shows `06/12/2026` consideration of `$58.537820M` to `AARE Surplus AAM`, `$58.400633M` book at disposal, and `$137.187K` gain. | Two current same-CUSIP rows create a continuity/transfer question; they are not merged into a cash return without lot-level settlement. |
| Atlas A `04940#-AA-9` | Part 4 PDF page `2594`: `04/23/2026` redemption at `100%`; `$891.351351M` consideration, par, actual cost, and book at disposal; `$17.510770M` bond interest received during year. | Strong current statutory redemption candidate; purchaser/payment agent and bank remittance remain unidentified. |
| Atlas B `04940#-AB-7` | Part 4 PDF page `2594`: same `04/23/2026` redemption window; `$78.648649M` consideration, par, actual cost, and book at disposal; `$1.967474M` bond interest received during year. | Companion-class redemption candidate; same settlement boundary. |

These rows expand the named-asset evidence surface, especially the Atlas
redemption candidate and the MF1 same-CUSIP continuity question. They do not
replace the required custody, trustee, servicing, liability-cost, or remittance
records. The direct statement is the [Q2 2026 AAIA statutory PDF](https://d1io3yog0oux5.cloudfront.net/_f301a7da18a01c1717e3734d3a0fe50c/athene/db/2370/22562/pdf/2Q+2026+AAIA+Statement.pdf).

### Atlas settlement search recheck

A bounded public-source recheck searched the two exact statutory identifiers
(`04940#-AA-9` and `04940#-AB-7`), the combined `$970.000M` amount, and the
`04/23/2026` date across SEC-indexed and general public results. It did not
locate an issuer notice, trustee report, paying-agent statement, counterparty
confirmation, bank/remittance record, or holder-side settlement record that
matches both Atlas classes and the Athene disposal row. Results using only
“Atlas” were materially ambiguous, including unrelated Atlas repurchase,
securitization, and corporate-finance records.

Therefore the current promotion boundary is unchanged: the paired `$970.000M`
statutory redemption is a high-quality dated disposition candidate, not yet
confirmed cash received by Athene or cash available to common owners. The
`$17.510770M` and `$1.967474M` fields remain annual bond-interest-received
columns, not incremental Q2 settlement evidence.

## Priority order

1. **Accordia top-40 selection.** Start with rows that combine interest
   received, private/ABS markers, issuer traceability, and disposal evidence.
2. **Apollo/Athene custody and remittance.** Target Concord, AMAPS, MF1, and AP
   Grange for lot-level settlement or trustee records.
3. **Servicing waterfall.** Obtain MF1 or equivalent borrower collections,
   fees, advances, losses, and distributions.
4. **Funding burden.** Join insurance liability cost, credited rates,
   reinsurance/funds-held, FHLB, and pledged-asset claims.
5. **Return model.** Reconcile named asset cash, senior claims, tax, fees,
   residual entity cash, and owner allocation.

## Promotion rule

Q-12 can move beyond `evidence-insufficient` only when the source set joins:

`legal entity -> named asset/CUSIP -> income/proceeds -> borrower or trustee cash -> liability cost -> remittance/waterfall -> return`

Statutory interest received, consideration, public CUSIP identity, or platform
AUM remains a cash-back proxy until that chain is joined.

## Stop rule

Do not broaden the platform search or convert statutory columns into settled
cash. Reopen only for a named-asset custody/trustee/servicing record, legal-
entity cash schedule, liability-cost allocation, or equivalent waterfall.

## Accordia Q2 controlled-source request

The public Global Atlantic portal currently exposes Accordia's Q2 2026
verification statement and its aggregate cash-flow pages, but not a separate
current-period Schedule D/BA or Part 4 CUSIP package. The next controlled
request should ask for the following exact objects:

1. Accordia Q2 2026 Schedule D Part 1 pages containing `458140-BM-1`,
   `202795-JY-7`, and `685218-AB-5`;
2. the corresponding Q2 Part 4/5 disposal or maturity pages and page-level
   column headers;
3. lot continuity from the year-end owned rows to any Q2 disposal event;
4. broker, custodian, or settlement confirmation for the disposal dates;
5. Accordia investment-income allocation for those CUSIPs; and
6. liability, reinsurance, and funds-held allocation needed to calculate an
   after-cost legal-entity return.

The Q2 statement's `$764.721M` aggregate investment proceeds and `$259.286M`
ending cash are not substitutes for these objects. The request status is
`current-entity-cash-visible; current-named-cusip-pages-and-settlement-requested`.

The portal's separate [ALIRT Q2 2026 Exhibit](https://www.globalatlantic.com/content/dam/global-atlantic/investors/financial-statements/annual-and-quarterly-statements/alirt-q2-2026-exhibit.pdf)
was also checked. It provides a notional FLIC/Global Atlantic Re and GAAL
capital, income, and invested-asset attribution, but expressly is not prepared
under a statutory or GAAP accounting basis and does not identify Accordia
CUSIPs or settlement. Keep it as a reinsurance/funds-held boundary, not as the
missing liability-cost or remittance source.

## New AMAPS source lead

Apollo's [August 24, 2026 Form 8-K](https://www.sec.gov/Archives/edgar/data/1858681/000185868126000048/apo-20260824.htm)
identifies an `Apollo Multi-Asset Prime Securities (AMAPS) Overview
Presentation` posted on its investor-relations site. The presentation could
improve the affiliated-asset wrapper and capital-
solution map relevant to Athene named holdings. The linked investor-relations
PDF was identified, but both the retrieval tool and direct official-URL
header requests for the Apollo and Athene issuer-linked CDN paths returned
HTTP `403` from CloudFront/S3; no slide content is promoted here. A controlled
download or authorized copy is needed before using it for portfolio identity,
funding, settlement, or return.
The 8-K itself is only a posting notice, not a cash-flow record.

## Decision

`return-unproven; source-package-ready`
