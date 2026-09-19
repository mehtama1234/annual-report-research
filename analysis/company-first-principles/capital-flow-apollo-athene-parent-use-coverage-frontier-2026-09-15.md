# Apollo–Athene parent-use coverage frontier — 2026-09-15

This memo adds a bounded attribution test to Q-07. Athene reports `$110M` of
H1 2026 distributions to its parent. Apollo separately reports H1 common
dividends, common-stock repurchases, and preferred dividends. The calculation
asks how much of those parent-level uses could be covered by the Athene flow
under an explicit attribution assumption.

## Source inputs

| Input | H1 2026 | Interpretation |
| --- | ---: | --- |
| Athene distributions to parent | `$110M` | Legal-entity upstream-flow observation; AGM receipt not joined |
| Apollo common dividends | `$654M` | Parent-level cash use |
| Apollo common-stock repurchases | `$729M` | Parent-level cash use |
| Apollo preferred dividends | `$49M` | Senior equity cash use |
| Total listed parent uses | `$1.432B` | Sum of the three reported uses; not all parent cash uses |

## Attribution frontier

| Assumed Athene share of listed parent uses | Attributed Athene flow | Coverage of listed parent uses |
| ---: | ---: | ---: |
| 0% | `$0M` | `0.00%` |
| 25% | `$27.5M` | `1.92%` |
| 50% | `$55.0M` | `3.84%` |
| 75% | `$82.5M` | `5.76%` |
| 100% | `$110.0M` | `7.68%` |

```text
attributed Athene flow = $110M × attribution assumption
coverage = attributed Athene flow ÷ ($654M + $729M + $49M)
```

The 100% row is an upper-bound attribution screen, not an observed receipt.
Even under that assumption, the identified Athene flow would cover only 7.68%
of these three listed Apollo parent uses. The calculation does not imply that
Athene funded none, some, or all of the uses; it only prevents the `$110M`
observation from being silently treated as the source of the full parent cash
return.

## Proof-grade boundary

This frontier does not prove an AGM bank receipt, parent-only cash-flow
inclusion, payment date, receiving account, intercompany elimination, source
priority, unrestricted availability, or common-owner cash generation.

Status: `source-bounded parent-use coverage frontier; receipt and common-owner residual unresolved`.

## Primary sources

- [Athene Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1527469/000152746926000056/ahl-20260630.htm)
- [Apollo Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1858681/000185868126000040/apo-20260630.htm)
- [Apollo Q2 upstream source-to-destination bridge](capital-flow-apollo-athene-q2-upstream-source-destination-bridge-2026-09-15.md)

Structured result: [parent-use coverage CSV](data/capital-flow-apollo-athene-parent-use-coverage-frontier-2026-09-15.csv).

