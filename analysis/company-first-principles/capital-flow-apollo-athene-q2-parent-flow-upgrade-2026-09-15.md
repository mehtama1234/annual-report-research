# Apollo–Athene Q2 parent-flow upgrade

Research date: `2026-09-15`

Athene's Q2 2026 Form 10-Q provides a stronger upstream-flow observation than
the Apollo financial supplement. Athene identifies itself as a direct
subsidiary of Apollo Global Management, Inc. and its condensed statement of
stockholders' equity reports the line `Contributions from (distributions to)
parent`.

## Observed parent-flow fields

| Period | Contributions from parent | Distributions to parent | Net parent-flow direction |
| --- | ---: | ---: | ---: |
| Q2 2026 | `$58M` | `$32M` | `$26M` net contribution to Athene |
| H1 2026 | `$241M` | `$110M` | `$131M` net contribution to Athene |

The net-direction checks are arithmetic controls, not an assertion that the
distribution is an Apollo unrestricted-cash receipt: `58 - 32 = 26` for Q2
and `241 - 110 = 131` for H1. The separately reported common-stock dividends
remain distinct (`$187M` for Q2 and `$375M` for H1).

The same equity statement separately reports common-stock dividends of `$187M`
for Q2 and `$375M` for H1. Those are not substituted for the parent-flow
line: the artifact preserves both categories because a dividend to the parent,
an equity contribution from the parent, and an internal equity reclassification
are economically different paths.

## Proof-grade consequence

This upgrades the Apollo–Athene lane from a purely mechanical parent-receipt
attribution frontier to a dated Athene-to-parent flow observation. It does not
yet prove that the `$32M` or `$110M` distribution was received in Apollo's
unrestricted cash account, that it is included in Apollo's reported parent-only
cash-flow line, or that it was available to common owners after senior claims,
intercompany eliminations, tax, and corporate uses.

The correct status is therefore:

`Athene-to-parent flow observed; AGM receipt and common-owner residual unresolved`

## Primary source

[Athene Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1527469/000152746926000056/ahl-20260630.htm), including the condensed statement of stockholders' equity and the business/basis-of-presentation note identifying Athene as a direct Apollo subsidiary.

Structured result: [parent-flow CSV](data/capital-flow-apollo-athene-q2-parent-flow-upgrade-2026-09-15.csv).
