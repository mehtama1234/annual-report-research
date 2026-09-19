# Apollo Q2 2026 Share-Claim and Dilution Boundary Upgrade

Research date: `2026-09-15`

This pass extracts the share-claim denominator from Apollo's Q2 2026 financial
supplement. It upgrades the common-owner bridge and valuation workbench by
making the reported common-share base, mandatory-convertible preferred claim,
and RSU-related share claims visible in one period-specific source route.

It does not prove that Athene distributions reached Apollo HoldCo, and it does
not convert adjusted shares into a cash return. The figures are a claim and
denominator boundary for per-share valuation and residual-cash analysis.

## Source and extraction

Primary source:

`raw/primary-sources/capital-flow/apollo/q2-2026/apollo-q2-2026-financial-supplement.xlsx`

Worksheet: `Reconciliation_Sharecount`, column `2Q'26`.

| Claim or denominator | Q2 2026 shares | What it controls |
| --- | ---: | --- |
| GAAP common stock outstanding | `575,971,752` | Basic common-share denominator |
| Underlying shares assumed issuable on mandatory-convertible preferred conversion | `14,587,841` | Preferred-to-common dilution claim |
| Vested RSUs | `17,073,031` | Earned equity-compensation share claim |
| Unvested RSUs eligible for dividend equivalents | `15,921,831` | Additional adjusted-income/share claim |
| Adjusted net-income shares outstanding | `623,554,455` | Apollo's disclosed adjusted per-share denominator |

The supplement's adjusted denominator reconciles mechanically:

`575,971,752 + 14,587,841 + 17,073,031 + 15,921,831 = 623,554,455`.

That is `47,582,703` shares above GAAP common shares, or approximately `8.26%`
of the GAAP common-share base. This is a denominator screen, not a claim that
all instruments have identical voting, dividend, or cash-settlement terms.

## Investment-research implication

Apollo's fee, spread, principal, insurance, preferred, NCI, and parent-cash
layers should not be divided by GAAP common shares alone when the question is
the per-share burden carried by adjusted earnings or a residual common-owner
claim. The preferred conversion assumption and RSU claims must remain visible
beside the common-owner bridge.

The exact remaining gap is unchanged: the source does not identify the cash
receipt from Athene to AGM, the portion available after regulated capital and
other claims, or the amount ultimately attributable to common owners. It also
does not provide a full economic dilution model for future issuance,
repurchase, or conversion timing.

## Safe grade

`dilution-denominator-confirmed` — the Q2 2026 adjusted-share bridge is
source-backed and arithmetically reconciled. It strengthens the price-implied
expectation and common-owner residual screens without promoting consolidated
or adjusted earnings into distributable HoldCo cash.
