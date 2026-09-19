# Apollo–Athene AA MMF 1 public-source refresh

Research date: `2026-09-16`

## Question

Can public sources connect Athene's `000249-AA-0` AA MMF 1 statutory disposal
candidate to the Apollo wrapper and middle-market credit destination, while
preserving the exact legal-entity and cash-return boundaries?

## Result

`partial-upgrade` for the Apollo wrapper and strategy perimeter;
`evidence-insufficient` for exact AA MMF 1 Ltd-to-Holdco identity, settlement,
borrower cash, liability-adjusted return, or Apollo common-owner cash.

The local Athene Schedule D parser identifies `000249-AA-0`, AA MMF 1 Ltd AA
5.804% due 10/08/51, as a disposal-only `Paydown` candidate with approximately
`$222.810M` of consideration and `$13.358M` of interest/dividend fields on
September 30, 2025. No year-end holding match is present in the current parser.

Athene's 2024 and 2025 regulatory application exhibits identify AA MMF 1
Holdco LP and show its general-partner/member chain through Apollo Principal
Holdings B and related Apollo entities. Apollo's 2025 Form 10-K also lists AA
MMF 1 Holdco GP LLC among Apollo-related entities. These filings establish a
credible Apollo wrapper route, but they do not prove that AA MMF 1 Ltd (the
statutory note name) is the same legal entity as AA MMF 1 Holdco LP, nor do
they identify Athene's exact ownership lot or redemption settlement.

Public market coverage describes AA MMF 1 as an Apollo middle-market vehicle
with approximately `$1B` of issuance. This is directional strategy context,
not a substitute for the offering memorandum, collateral schedule, trustee
report, or Athene settlement ledger.

## Decision

Promote AA MMF 1 to a named Apollo-linked middle-market credit wrapper target.
Do not promote the `$222.8M` statutory consideration to a proven Athene receipt,
borrower repayment, collateral cash, liability-adjusted spread, realized
IRR/NPV, or Apollo common-owner cash.

## Next documents

Request the AA MMF 1 Ltd offering memorandum, legal-entity organizational
documents, middle-market loan/collateral schedule, trustee or administrator
reports, redemption notice, Athene trade confirmation, custodian settlement
ledger, borrower repayment records, and liability-cost allocation. Reconcile
the Ltd note, Holdco chain, principal, coupon, fees, losses, and cash receipt
before calculating return.

## Safe claim

`Athene regulatory exhibits and Apollo filings establish an Apollo-related AA
MMF 1 Holdco wrapper chain, while public coverage places AA MMF 1 in a
middle-market credit context. Athene's $222.8M AA MMF 1 Ltd disposal row is a
named cash-like candidate, not proven settlement, borrower cash, liability-
adjusted return, or Apollo common-owner cash.`

## Sources

- [Athene 2024 Form 40-APP/A exhibit](https://ir.athene.com/sec-filings/all-sec-filings/content/0001193125-24-273539/0001193125-24-273539.pdf)
- [Athene 2025 Form 40-APP/A exhibit](https://ir.athene.com/sec-filings/all-sec-filings/content/0001193125-25-073269/0001193125-25-073269.pdf)
- [Apollo 2025 Form 10-K](https://ir.apollo.com/sec-filings/content/0001858681-26-000013/apo-20251231.htm)
- [AA MMF 1 public issuance description](https://www.prospectnews.com/cgi-bin/issuerresponse.pl?first=A&issuer=82319&market=AG%7CBK%7CBT%7CCA%7CCL%7CCV%7CDD%7CEM%7CFD%7CGN%7CHY%7CIG%7CLM%7CMU%7CPP%7CPF%7CPV%7CSP%7CSS)

