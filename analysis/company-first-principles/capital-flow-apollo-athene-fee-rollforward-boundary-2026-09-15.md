# Apollo–Athene fee rollforward boundary

Date: `2026-09-15`

This control isolates the difference between Athene's reported related-party
fee expense and the period-end payable. It is a settlement-boundary test, not
proof of Apollo parent cash collection.

## Management-fee rollforward

Athene reports `134M USD` of management fees payable at December 31, 2025,
`785M USD` of management fees incurred during H1 2026, and `140M USD` payable
at June 30, 2026. The mechanical equation is:

```text
opening payable                         134M USD
+ H1 fee expense                        785M USD
- ending payable                        140M USD
= implied reduction / settlement        779M USD
```

The `$779M` result is only an implied rollforward amount. It would equal cash
settlement only if the payable class had no reclassification, non-cash
settlement, foreign-exchange, consolidation, or other adjustment. The public
filing does not provide that settlement schedule or identify the Apollo
recipient account.

## Contingent-fee boundary

ACRA's contingent investment-fee payable to Apollo increased from `365M USD`
at year-end to `392M USD` at June 30. Because the period's contingent-fee
expense and settlement schedule are not separately disclosed, this balance
cannot be combined with the management-fee rollforward or converted into
parent cash.

## Proof grade and next document

```text
Athene fee expense -> payable movement -> mechanical settlement implication  qualified
mechanical implication -> Apollo recipient cash                              unresolved
fee expense / payable -> unrestricted Apollo common-owner cash                unresolved
```

The upgrade document needed next is a related-party payable rollforward or
intercompany settlement schedule that identifies cash settlement dates,
recipient legal entity, eliminations, and the receiving bank account or
parent-only cash-flow line.

Structured rows are in the [fee-rollforward CSV](data/capital-flow-apollo-athene-fee-rollforward-boundary-2026-09-15.csv).

Primary source: [Athene Q2 2026 Form 10-Q](https://ir.athene.com/sec-filings/all-sec-filings/content/0001527469-26-000056/ahl-20260630.htm).
