# Apollo–Athene related-party fee and asset-transfer upgrade

Date: `2026-09-15`

This upgrade adds two primary-source boundaries to Pilot 03. Athene's fee
expense can now be compared with a period-end payable, and a named asset
transfer from Apollo's origination platform into Athene is visible. Neither
fact proves Apollo parent cash collection, final asset return, or unrestricted
common-owner cash.

## Fee boundary

Athene's Q2 2026 Form 10-Q reports `785M USD` of management fees incurred to
Apollo in the first half, inclusive of base, sub-allocation, and performance
fees. It reports `140M USD` of management fees payable at June 30, 2026,
versus `134M USD` at December 31, 2025. The payable is an entity-level balance
and is not a receipt ledger. The difference between incurred fees and the
period-end payable cannot be treated as cash collected without the opening
payable, settlements, intercompany eliminations, and Apollo recipient-entity
cash flow.

Athene separately reports `392M USD` of related-party payables for contingent
investment fees payable by ACRA to Apollo at June 30, 2026, versus `365M USD`
at December 31, 2025. This is a distinct contingent-fee liability and should
not be added to the `140M USD` management-fee payable without an accounting
rollforward.

## Named asset-transfer boundary

Apollo's Q2 2026 Form 10-Q reports that Athene completed the purchase of a
commercial mortgage loan portfolio, including accrued interest, for `8.7B USD`
from ARI on April 24, 2026. This is a named related-party origination-to-
insurance-balance-sheet transfer. It establishes asset movement and potential
origination monetization, not borrower repayment, credit performance, fee cash,
or Apollo common-owner return.

## Current proof grade

```text
Athene fee expense -> fee payable boundary -> parent receipt ledger          hold
ARI originated portfolio -> Athene acquisition -> borrower cash/credit return hold
Athene related-party exposure -> Apollo common-owner cash                    unresolved
```

Primary sources: [Athene Q2 2026 Form 10-Q](https://ir.athene.com/sec-filings/all-sec-filings/content/0001527469-26-000056/ahl-20260630.htm) and [Apollo Q2 2026 Form 10-Q](https://ir.apollo.com/sec-filings/content/0001858681-26-000040/apo-20260630.htm).
