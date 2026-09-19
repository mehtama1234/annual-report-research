# Apollo Q2 XBRL parent-receipt boundary

Research date: `2026-09-15`

The Apollo Q2 2026 Form 10-Q was inspected at the inline-XBRL fact and context
level after the narrative search. The accession-filtered local SEC companyfacts
cache returns `29` dividend/distribution-related facts for accession
`0001858681-26-000040`, all shareholder dividend or distribution-equivalent
outflows; it returns `0` facts whose tag or label indicates an upstream receipt,
intercompany cash receipt, affiliate transfer, or receipt. The filing contains
`ParentMember` contexts for stockholders' equity components, but no
`ParentCompanyMember` cash-receipt dimension and no separately tagged
parent-company dividend-receipt or subsidiary-distribution fact that joins
Athene to AGM.

The XBRL facts do expose AGM's own common and preferred dividend payments and
distribution-equivalent facts. Those are shareholder outflows, not upstream
Athene receipts. The filing's narrative separately states that distributions
and intercompany transfers from AAM and AHL are AGM's primary cash source, but
that route statement is not a dated, payer-specific cash-flow fact.

## Proof-grade consequence

This is a parser-level source boundary, not evidence that no transfer occurred.
It confirms that the current Apollo Q2 public filing does not provide the
missing `Athene -> AGM receiving account -> unrestricted parent cash` join.
The remaining required source is a parent-only cash-flow note, intercompany
ledger, bank receipt, or regulatory dividend record with payer, date, amount,
and recipient.

Status:

`Q2 XBRL parent-receipt fact absent; route statement visible; receipt unresolved`

## Primary source

[Apollo Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1858681/000185868126000040/apo-20260630.htm), including the inline-XBRL contexts/facts, “Liquidity and Capital Resources,” and “Dividends and Distributions.”

Structured result: [XBRL boundary CSV](data/capital-flow-apollo-q2-xbrl-parent-receipt-boundary-2026-09-15.csv).

Reproducible local check: [`check-apollo-q2-parent-receipt-boundary.py`](../../scripts/check-apollo-q2-parent-receipt-boundary.py).
