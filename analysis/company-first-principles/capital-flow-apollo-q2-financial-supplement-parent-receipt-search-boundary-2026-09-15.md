# Apollo Q2 financial-supplement parent-receipt search boundary

Research date: `2026-09-15`

The Apollo Q2 2026 financial supplement workbook was searched across all eight
worksheets for `dividend`, `cash`, `subsidiary`, `distribution`,
`intercompany`, and `parent`. It exposes preferred-stock dividends, unvested
RSUs eligible for dividend equivalents, and consolidated cash and cash
equivalents including restricted cash. It does not expose a separately tagged
Athene-to-AGM receipt, subsidiary-distribution line, receiving account, or
intercompany settlement.

This is a source-availability boundary, not evidence that no transfer occurred.
It narrows the public supplement route and leaves the parent-receipt attribution
frontier unchanged. The next required evidence remains a parent cash-flow note,
intercompany ledger, bank receipt, subsidiary dividend schedule, or regulatory
approval/receipt that identifies payer, date, amount, and recipient.

## Reproducible source

- Local source: `raw/primary-sources/capital-flow/apollo/q2-2026/apollo-q2-2026-financial-supplement.xlsx`
- Reproducible checker: [`check-apollo-q2-financial-supplement-boundary.py`](../../scripts/check-apollo-q2-financial-supplement-boundary.py)
- Sheets searched: Cover, Summary, Total Segment Earnings, GAAP Income Statement,
  RS Flows and IA, Reconciliation_ANI, Reconciliation_Sharecount, and
  Reconciliation_NIA and Alts.
- Structured result: [search-boundary CSV](data/capital-flow-apollo-q2-financial-supplement-parent-receipt-search-boundary-2026-09-15.csv)
