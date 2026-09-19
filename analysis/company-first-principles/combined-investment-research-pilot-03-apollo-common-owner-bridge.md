# Pilot 03 Apollo Common-Owner Bridge

Date: 2026-09-15

This bridge separates what Apollo reports from what a common owner can safely
call cash. The structured table is [the bridge CSV](data/combined-investment-research-pilot-03-apollo-common-owner-bridge.csv).

## Reported Q2 bridge

```text
Fee-related earnings                         785M USD
+ spread-related earnings                   877M USD
+ principal-investing income                 16M USD
= fee + spread + principal                1,678M USD
- HoldCo interest and financing costs        53M USD
- taxes and related payables                311M USD
= adjusted net income                    1,314M USD
```

The arithmetic reconciles exactly to Apollo's Q2 2026 adjusted net income.
GAAP net income attributable to common stockholders was `1.336B USD`, only
`22M USD` above ANI in this quarter. That narrow difference does not prove
higher-quality cash; it only identifies the reported-period reconciliation.

## Capital return and dilution are separate tests

Apollo disclosed `324M USD` of common dividends declared and `102M USD` of
share repurchases in Q2, or `426M USD` of reported capital returned. It also
recorded `246M USD` of equity-based compensation in Q2 and `478M USD` in the
first half. Dividends and buybacks are uses of capital, while equity
compensation is a claim on per-share economics; none is a substitute for a
source-backed cash-generation bridge.

## Why consolidated OCF is not the final denominator

The Q2 2026 10-Q reports `4.501B USD` of six-month consolidated operating cash
flow. The same filing includes Athene's policyholder liabilities, investment
transactions, reinsurance, regulated cash, and consolidated entities. That
number therefore cannot be inserted into the fee-platform SOTP as unrestricted
common-owner cash.

The remaining bridge is:

```text
ANI / GAAP common earnings
  -> cash actually collected by fee entities
  -> cash retained for Athene policyholder and regulatory obligations
  -> NCI and preferred claims
  -> HoldCo debt, tax, compensation, and repurchases
  -> cash transferred to common owners
```

Current status: `reported earnings bridge complete; unrestricted common-owner
cash bridge unresolved`.

The [ANI-to-cash residual frontier](capital-flow-apollo-common-owner-ani-residual-frontier-2026-09-15.md)
now quantifies that gap. Against selected H1 parent uses of `$1.432B`, the
mechanical residual ranges from `($1.432B)` at 0% ANI cash conversion to
`$1.090B` at 100% conversion, with `($171M)` at 50%. These are explicit
assumptions, not observed cash and not a common-owner valuation conclusion.

Athene's entity-level cash flow now sharpens the boundary. In the first half
of 2026 Athene reported `42M USD` of capital contributions from its parent,
`271M USD` of NCI contributions, `759M USD` of VIE-NCI contributions, and
`301M USD` of distributions to NCI. It also reported `41.617B USD` of policy
deposits and `14.741B USD` of withdrawals. These figures prove the existence
of cash movement between parent, insurance, VIE, and policyholder channels;
they do not prove that the consolidated cash is distributable to Apollo common
owners.

The Q2 2026 balance-sheet segment presentation also reports `3.415B USD` of
asset-management cash plus `19M USD` restricted, and `21.957B USD` of
retirement-services cash plus `1.583B USD` restricted. These are now explicit
cash-pool boundary inputs, not an owner-cash numerator: the asset-management
pool still has HoldCo claims, while the retirement-services pool remains
subject to insurance, policyholder, VIE, and regulatory constraints.

The parent-level H1 cash-use layer is now also explicit: Apollo paid `654M USD`
of common dividends, `729M USD` for common-stock repurchases, and `49M USD` of
preferred dividends. These are cash claims against the residual, not proof that
the segment cash pools or Athene fees were freely available to fund them.

Athene also reports `375M USD` of common stock dividends and `71M USD` of
preferred stock dividends in the six-month financing flows. Its `27.801B USD`
net financing cash flow is dominated by policy deposits and withdrawals, and
its `23.711B USD` ending cash includes restricted cash and consolidated VIE
cash. These are liability-backed and entity-level figures, not a parent-owner
cash balance.

## Upstream cash-access upgrade

The latest filing work adds two distinct Athene-to-AGM paths without collapsing
them into one receipt claim:

```text
Athene H1 distributions to parent: 110M USD
  -> direct parent-flow line observed
  -> AGM receiving account / parent-only cash-flow join: unresolved

AHL unsecured note receivable from AGM: 279M USD at 2026-06-30
  -> direct financing route; 500M USD capacity; reciprocal AHL payable: zero
  -> draw date, use of proceeds, repayment, and dividend linkage: unresolved
```

Apollo's Q2 filing says distributions and intercompany transfers from AAM and
AHL are AGM's primary cash source and reports `25.4B USD` of consolidated
unrestricted cash. It also reports `1.175B USD` due from and `1.617B USD` due
to non-guarantor subsidiaries. These are route and perimeter evidence, not
proof that the `110M USD` Athene distribution or the note balance entered a
parent-only unrestricted account. Apollo's inline-XBRL contexts do not add a
separately tagged parent-receipt fact.

The owner-cash conclusion therefore remains:

`Athene-to-AGM cash-access routes observed; AGM receipt, elimination, senior claims, and common-owner residual unresolved.`

See the [Athene parent-flow upgrade](capital-flow-apollo-athene-q2-parent-flow-upgrade-2026-09-15.md),
[intercompany-note route](capital-flow-apollo-athene-intercompany-note-route-upgrade-2026-09-15.md),
[HoldCo liquidity boundary](capital-flow-apollo-q2-holdco-liquidity-intercompany-boundary-2026-09-15.md),
and [Q2 XBRL boundary](capital-flow-apollo-q2-xbrl-parent-receipt-boundary-2026-09-15.md).

The buyer-side ARI perimeter remains qualified. Athene's commercial-mortgage
portfolio increased from `$39.071B` to `$48.291B` fair value between year-end
and Q2, while Athene separately disclosed the approximately `$8.7B` ARI
purchase. The `$9.220B` aggregate change is not treated as an ARI-specific
receipt, repayment, or return; loan-level attribution and borrower cash remain
open in the [ARI buyer-side portfolio boundary](capital-flow-apollo-athene-ari-buyer-portfolio-expansion-boundary-2026-09-15.md).
