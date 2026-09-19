# Apollo–Athene Q2 AMAPS 1 current-exposure boundary — 2026-09-16

Athene's Q2 2026 Form 10-Q provides a current-period update to the AMAPS 1
wrapper route. The filing lists investment-grade ABS debt issued by AMAPS 1,
LLC at `$2.544B` on June 30, 2026, compared with `$2.550B` at December 31,
2025. The mechanical change is `-$6M`. The structured comparison is in the
[AMAPS exposure CSV](data/capital-flow-apollo-athene-q2-amaps-current-exposure-boundary-2026-09-16.csv).

| Evidence item | Q2 2026 observation | Safe use | Boundary |
| --- | --- | --- | --- |
| Named wrapper | AMAPS 1 LLC | Confirms the current Athene investment-concentration route | Does not identify the underlying obligors, collateral, or borrower use |
| June 30 exposure | `$2.544B` investment-grade ABS debt | Current-period wrapper exposure denominator | Concentration is not a cash receipt, realized return, or Apollo fee cash flow |
| December 31 comparison | `$2.550B` | Provides a period-over-period exposure comparison | The `$6M` change is not a trade, repayment, or settlement ledger |
| Related-party caveat | Filing footnote says amounts may include only a portion of total investments associated with a related party | Preserves the filing's scope limitation | Does not establish Athene ownership percentage, Apollo funding, or liability-cost allocation |

## Concentration orientation

For scale context only, the `$2.544B` AMAPS 1 exposure is approximately
`0.810%` of Athene's Q2 `$314.090B` net invested assets and approximately
`5.782%` of the filing's `$44.0B` look-through related-party investment
population. These are mechanical denominator ratios, not ownership, funding,
income, liability-cost, or return allocations. The related-party denominator
also includes multiple affiliated-platform and managed-asset categories, so it
must not be read as a directly comparable portfolio bucket.

This is a current wrapper-exposure boundary, not full named-cash proof. The
public filing still does not join AMAPS 1 to an offering memorandum collateral
tape, named borrower receipts, trustee remittance, Athene liability cost,
settled lot, or Apollo common-owner cash.

## Route

```text
Apollo structured-credit platform
  -> AMAPS 1 LLC
  -> Athene investment-grade ABS exposure
  -> underlying collateral and borrower cash: unresolved
  -> trustee remittance / liability spread: unresolved
  -> Apollo common-owner cash: unresolved
```

Status: `current-wrapper-exposure-confirmed; collateral-remittance-return-held`

Primary source: [Athene Q2 2026 Form 10-Q](https://ir.athene.com/sec-filings/all-sec-filings/content/0001527469-26-000056/ahl-20260630.htm), concentration table and related-party footnote.

Local source artifact: [preserved Q2 2026 filing](../../raw/primary-sources/capital-flow/apollo/q2-2026/athene-q2-2026-10q.html).
