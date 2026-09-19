# Apollo–Athene Q2 parent-cash perimeter reconciliation

Research date: `2026-09-16`

## Purpose

Reconcile the distinct Q2 2026 cash and financing surfaces used in Q-07 so
that Athene distributions, AHL-to-AGM note balances, consolidated cash, and
HoldCo cash are not silently added or treated as unrestricted common-owner
cash.

## Non-additive perimeter table

| Surface | Period / date | Reported amount | Legal/accounting scope | Safe use |
| --- | --- | ---: | --- | --- |
| Athene distributions to parent | Q2 2026 | `$32M` | AHL legal-entity equity flow | Source-side upstream-flow observation |
| Athene distributions to parent | H1 2026 | `$110M` | AHL legal-entity equity flow | Period-total upstream-flow observation |
| AHL note receivable from AGM | June 30, 2026 | `$279M` | AHL creditor / AGM borrower balance | Direct financing-route balance |
| AHL-to-AGM note capacity | June 30, 2026 | `$500M` | Revolving facility ceiling | Facility-perimeter context |
| Apollo consolidated unrestricted cash | June 30, 2026 | `$25.4B` | Consolidated AGM perimeter | Broad liquidity context only |
| Apollo HoldCo & Asset Management cash | June 30, 2026 | `$3.412B` | Parent-summary presentation | HoldCo-denominator context |
| Apollo Asset Management segment cash | June 30, 2026 | `$3.415B` | GAAP segment presentation | Cross-check with parent summary; `$3M` presentation difference remains |
| Apollo common dividends | H1 2026 | `$654M` | Parent-level cash use | Use-side comparison only |
| Apollo common repurchases | H1 2026 | `$729M` | Parent-level cash use | Use-side comparison only |
| Apollo preferred dividends | H1 2026 | `$49M` | Parent-level senior-equity cash use | Use-side comparison only |

## Mechanical perspective, not attribution

For orientation only, the `$110M` H1 Athene distribution equals approximately
`3.22%` of the `$3.412B` HoldCo-summary cash surface and `0.43%` of the `$25.4B`
consolidated unrestricted-cash surface. These are denominator ratios, not
proof that Athene funded either cash pool. The `$279M` note receivable is a
period-end balance, not a cash receipt, and the `$52M` increase from December
31, 2025 is not promoted to principal draw because accrued interest,
repayments, and intra-period activity are not disclosed.

The `$3.412B` and `$3.415B` values are separate presentation surfaces, not
additional cash to add to `$25.4B`. The `$110M` distribution is a source-side
AHL equity-flow line; the parent receipt account, intercompany elimination,
restricted/regulated availability, taxes, preferred claims, debt, dividends,
repurchases, and residual common-owner cash are not joined.

Apollo's FY2025 filing supplies the legal-availability control: AGM's primary
funding source is described as distributions and other intercompany transfers
from operating subsidiaries, with subsidiary distributions conditioned on
applicable law, surplus and minimum-solvency requirements, and prior AHL
preferred-stock distributions. This constrains the availability analysis but
does not establish that a particular Q2 Athene distribution reached AGM cash.

## Proof-grade result

`Q-07 denominator perimeter reconciled; Athene source-side flow and direct
financing route observed; parent receipt, unrestricted availability, and
common-owner residual unresolved.`

## Next proof objects

Obtain the AGM parent-only cash-flow ledger, AHL/AGM intercompany elimination,
note draw and repayment ledger, bank confirmations, legal-dividend support,
regulated surplus/capital constraints, and the common-owner cash waterfall.
Then calculate a residual only after separating consolidated, HoldCo, regulated,
VIE, and parent-only scopes.

## Sources

- [Athene Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1527469/000152746926000056/ahl-20260630.htm)
- [Apollo Q2 2026 Form 10-Q](https://ir.apollo.com/sec-filings/content/0001858681-26-000040/apo-20260630.htm)
- [Apollo FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1858681/000185868126000013/apo-20251231.htm)
- [Q2 upstream source-to-destination bridge](capital-flow-apollo-athene-q2-upstream-source-destination-bridge-2026-09-15.md)
- [Q2 parent-receipt refresh](capital-flow-apollo-athene-q2-parent-receipt-refresh-2026-09-16.md)
- [Intercompany note longitudinal refresh](capital-flow-apollo-athene-intercompany-note-longitudinal-refresh-2026-09-16.md)
