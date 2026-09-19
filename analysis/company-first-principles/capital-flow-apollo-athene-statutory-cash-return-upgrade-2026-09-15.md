# Apollo–Athene 2025 Statutory Cash-Return Upgrade

Research date: `2026-09-15`

This upgrade executes queue item `Q-08` using the locally archived 2025
statutory statement for Athene Annuity and Life Company. The source is an
entity-level statutory statement, not a consolidated Apollo report or an
Apollo-parent bank ledger.

Source artifact:

`raw/primary-sources/capital-flow/apollo/athene/statutory/2025/athene-annuity-and-life-company-2025-statutory-statement.pdf`

The extraction table is:

`data/capital-flow-apollo-athene-statutory-cash-return-upgrade-2026-09-15.csv`

## What the statutory statement proves

Athene's 2025 statement gives a legal-entity balance-sheet, income, and cash
denominator. At December 31, 2025 it reports `$158.852B` of bonds,
`$86.639B` of mortgage loans, `$110.616B` of life-contract reserves, and
`$64.260B` of deposit-type contract liabilities. The entity therefore has a
large invested-asset base funded alongside explicit policyholder and
deposit-type obligations.

The 2025 statutory income statement reports `$12.733B` of net investment
income. The statutory cash-flow statement reports `$12.282B` of net investment
income cash, `$8.857B` of premiums collected net of reinsurance, `$20.790B` of
net cash from operations, `$71.384B` of investment proceeds, `$131.823B` of
long-term investments acquired, and negative `$60.428B` of net cash from
investments. It also reports `$27.901B` of net deposits on deposit-type
contracts and `$39.232B` of net cash from financing and miscellaneous sources.

These figures establish that statutory investment income has a cash-flow
counterpart and that Athene's cash movement is dominated by both investment
turnover and policyholder financing flows. They do not establish that the
cash was distributed to Apollo, that it was free of policyholder claims, or
that it came from Apollo-linked assets.

## Reconciliation screen

The mechanical statutory conversion screen is:

```text
net investment income cash / reported net investment income
= 12.281980822B / 12.732699320B
= 96.46%
```

This is a cash-flow-to-statutory-income conversion screen, not distributable
cash and not a realized return on equity. The remaining difference can reflect
statutory timing, non-cash investment income, accruals, and other statement
classification effects; the filing alone does not allocate it to loss or
leakage.

The broader entity cash bridge is:

```text
premiums collected + net investment-income cash + miscellaneous income
  - benefits/loss payments - separate-account transfers
  - commissions/expenses - taxes
= statutory net cash from operations
```

For 2025 that produces `$20.790B` of net operating cash. Separately, the
entity acquired `$131.823B` of long-term investments and received `$71.384B`
of investment proceeds, producing negative `$60.428B` of net investment cash.
This prevents net investment income from being presented as the same thing as
free cash available to a parent.

## Proof-grade result

| Gate | Result | Boundary |
| --- | --- | --- |
| Athene legal-entity perimeter | Proven for the 2025 statement | This is Athene Annuity and Life Company, not all Athene entities or Apollo HoldCo |
| Invested-asset and liability denominator | Proven | Asset categories and policyholder/deposit liabilities are visible; asset-level allocation to Apollo strategies is not |
| Statutory investment-income cash bridge | Qualified and quantified | Cash investment income is visible, but not by issuer, borrower, affiliate, or Apollo-linked asset |
| Operating cash bridge | Qualified and quantified | Net operating cash includes policyholder, reinsurance, benefit, expense, tax, and separate-account flows |
| Investment turnover | Qualified and quantified | Proceeds and acquisitions are visible; realized gains, impairments, and return by asset class require schedules |
| Parent receipt | Not proven | No Apollo HoldCo receipt or unrestricted parent cash allocation appears in this statement |
| Common-owner residual | Not proven | Policyholder claims, regulated capital, NCI, preferred claims, taxes, and other obligations remain ahead of common residual |

## Updated safe claim

`Athene's 2025 statutory statement proves an entity-level invested-asset,
policyholder-liability, statutory-income, and cash-flow channel. It reports
$12.733B of net investment income, $12.282B of cash net investment income,
$20.790B of net operating cash, $71.384B of investment proceeds, and $131.823B
of long-term investments acquired. The 96.46% cash-to-statutory-income screen
supports a qualified cash-conversion observation. It does not prove the asset-
level source of income, borrower repayment, Apollo fee collection, parent
receipt, or Apollo common-owner cash.`

## Next gate

The next required source is still Schedule D/BA detail and statutory investment
income/realized-gain/impairment schedules. Those schedules must match named
holdings or asset classes to income, credit cost, liability funding cost, and
cash realization before the pilot can claim a legal-entity risk-adjusted
return.

