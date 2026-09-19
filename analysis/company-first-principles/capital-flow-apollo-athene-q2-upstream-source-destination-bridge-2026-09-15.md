# Apollo–Athene Q2 upstream source-to-destination bridge

Research date: `2026-09-15`

This bridge consolidates the current Q2 legal-entity evidence for the
Athene-to-Apollo upstream cash route. It is designed to prevent a common
modeling error: adding a subsidiary distribution, an intercompany note balance,
and consolidated intercompany revenue as though they were the same cash event.

## Source-to-destination ledger

| Source / route | Period or date | Amount | Destination visible in source | What is proven | What is not proven |
| --- | --- | ---: | --- | --- | --- |
| Athene equity statement: distributions to parent | Q2 2026 | `$32M` | Parent, legal-entity level | A dated upstream parent-flow line is reported by Athene | AGM bank receipt, unrestricted parent account, elimination, and common-owner residual |
| Athene equity statement: distributions to parent | H1 2026 | `$110M` | Parent, legal-entity level | The H1 upstream-flow total is reported by Athene | Payment dates, payer account, AGM parent-only cash-flow inclusion, and common-owner availability |
| Athene equity statement: contributions from parent | H1 2026 | `$241M` | Athene | A separate downstream parent-to-Athene equity-flow line is reported | Whether any contribution was funded by or netted against a distribution in the same bank account |
| AHL unsecured revolving note receivable from AGM | June 30, 2026 | `$279M` balance; `$500M` capacity | AGM borrower / AHL creditor | A direct financing route and legal direction are disclosed | Draw dates, repayments, use of proceeds, and whether the `$52M` period-end change was cash principal |
| Apollo HoldCo liquidity route | June 30, 2026 | `$25.4B` consolidated unrestricted cash | Consolidated AGM reporting perimeter | Apollo states subsidiary distributions and intercompany transfers are a primary HoldCo cash source | Parent-only cash, Athene-specific portion, restrictions, and common-owner residual |
| Apollo obligor-group intercompany perimeter | H1 2026 / June 30, 2026 | `$785M` intercompany revenue; `$300M` expense; `$17M` interest income; `$1.175B` due from and `$1.617B` due to non-guarantor subsidiaries | Obligor-group reporting perimeter | Current-period balances and flows establish an elimination boundary | Athene-specific attribution to the `$110M` distribution or the note route |

## Non-additivity rule

The `$110M` Athene distribution, `$279M` AHL note receivable balance, `$52M`
period-end note-balance change, `$785M` intercompany revenue, and `$25.4B`
consolidated cash figure must not be summed into parent cash. They represent
different legal-entity statements, measurement bases, and periods. In
particular:

1. The `$52M` note balance change is not promoted to a draw because the filing
   does not disclose intra-period principal activity separately from accrued
   interest or repayments.
2. The `$785M` intercompany-revenue figure is a consolidated obligor-group
   reporting amount, not a cash receipt from Athene.
3. The `$25.4B` cash balance is consolidated and cannot be used as AGM-only
   cash available to common owners.
4. The `$110M` distribution is an Athene legal-entity observation. A receipt
   date, AGM account, intercompany elimination, tax, debt, preferred claim,
   dividend, repurchase, and dilution bridge is required before it becomes
   common-owner cash.

## Proof-grade result

`Athene-to-parent flow observed; legal source and route visible; AGM receipt,
unrestricted HoldCo availability, and common-owner residual unresolved.`

The existing `0–100%` attribution frontier remains a sensitivity tool only.
This bridge improves the accounting perimeter and prevents double counting; it
does not upgrade Q-07 to full receipt proof.

## Primary sources

- [Athene Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1527469/000152746926000056/ahl-20260630.htm)
- [Apollo Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1858681/000185868126000040/apo-20260630.htm)
- [Athene Q2 parent-flow upgrade](capital-flow-apollo-athene-q2-parent-flow-upgrade-2026-09-15.md)
- [Athene-to-AGM intercompany note route](capital-flow-apollo-athene-intercompany-note-route-upgrade-2026-09-15.md)
- [Apollo Q2 HoldCo liquidity boundary](capital-flow-apollo-q2-holdco-liquidity-intercompany-boundary-2026-09-15.md)

Structured ledger: [Q2 upstream source-destination CSV](data/capital-flow-apollo-athene-q2-upstream-source-destination-bridge-2026-09-15.csv).
