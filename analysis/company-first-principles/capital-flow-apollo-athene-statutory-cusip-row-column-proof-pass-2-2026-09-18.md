# Apollo/Athene Schedule D CUSIP row-column proof pass 2

Date: `2026-09-18`

## Purpose

This pass tightens the first row-level proof packet by comparing the raw PDF
row text with the schedule-specific numeric layout for three of the five
highest-dollar same-CUSIP candidates:

- `00264#-AB-3` — AP Aristotle Holdings LLC;
- `28655*-AA-7` — Eliant Invest Holding LP; and
- `02300A-AA-8` — AMAPS 1 LLC Tranche A Note.

The raw-row source is the [CUSIP raw-text inspection
CSV](data/capital-flow-apollo-athene-statutory-cusip-raw-text-inspection-pass-1.csv).
The interpreted output is the [schedule-column interpretation
CSV](data/capital-flow-apollo-athene-statutory-cusip-column-interpretation-pass-1.csv).

## Result

Schedule-positioned consideration is supported for all six inspected disposal
rows. One row is explicitly excluded from cash-like treatment because its
source label is `Tax Free Exchange`.

| CUSIP | Named asset | Gross consideration | Held out as noncash exchange | Consideration retained as cash-like candidate | Proof boundary |
| --- | --- | ---: | ---: | ---: | --- |
| `00264#-AB-3` | AP Aristotle Holdings LLC | `$782.620834M` | `$6.588486M` | `$776.032348M` | Paydown/various labels support a cash-like candidate; borrower receipt, fees, tax, and return remain open. |
| `28655*-AA-7` | Eliant Invest Holding LP | `$358.251536M` | `$0` | `$358.251536M` | Various/redemption labels support a cash-like candidate; the visible `$(18)` token is not a full return reconciliation. |
| `02300A-AA-8` | AMAPS 1 LLC Tranche A Note | `$268.000000M` | `$0` | `$268.000000M` | `Apollo Capital Markets Partner` identifies a disposition counterparty/role, not borrower cash or Apollo distribution. |

The three rows therefore provide `$1.402032348B` of consideration that is
safe to carry forward as a **cash-like statutory candidate** after excluding
the `$6.588486M` tax-free exchange. This is not a collected-cash total.

## Row-level observations

`00264#-AB-3` has two cash-like-looking Part 4 rows—`Paydown` of
`$250.704550M` and `Various` of `$525.327798M`—plus a Part 5 `Tax Free
Exchange` of `$6.588486M`. The gross CUSIP total must not be used without that
split.

`28655*-AA-7` has a Part 4 `Various` row of `$356.444966M` with a visible
`$(18)` gain/loss token and a Part 5 `Redemption` row of `$1.806570M`. The
consideration fields are supported, but the gain/loss and interest columns are
not promoted beyond the source-supported tokens.

`02300A-AA-8` has one Part 4 row of `$268.000000M` whose disposition text is
`Apollo Capital Markets Partner`. The row is useful for tracing the Apollo
capital-markets role, but it does not identify the settlement account,
borrower use, legal-entity recipient, or parent-level cash availability.

## Current local-source boundary

A targeted search of the local Apollo primary-source corpus found no exact
public-source hit for the three CUSIPs, AP Aristotle, Eliant Invest Holding,
or AMAPS 1 LLC outside the statutory extraction and analysis artifacts. The
local Apollo AMAPS article is useful wrapper context—it describes AMAPS as a
structured-credit product with diversified, higher-credit-quality collateral—
but it does not identify the `02300A-AA-8` tranche, its holder, settlement, or
cash waterfall. The route therefore remains source-acquisition-ready rather
than settlement-proven.

## What this upgrades

The prior proof packet could safely say that these rows were prioritized
candidates. This pass upgrades the narrower statement that the selected
consideration values are supported by the raw row and schedule-specific
numeric layout, and that the explicit exchange row should be held out.

It does **not** upgrade any of the following:

- statutory consideration into bank-settled cash;
- a CUSIP into same-lot continuity with the year-end holding;
- a paydown into borrower receipt or debt-service waterfall;
- an Apollo Capital Markets Partner label into Apollo parent cash;
- parser-positioned gain/loss or interest fields into a realized return;
- gross or cash-like consideration into Athene liability spread or Apollo
  owner cash.

## Next proof object

The next useful source is transaction-level evidence for these rows: a
custodian/settlement record, counterparty remittance, borrower payoff or
liability-release schedule, and legal-entity cash reconciliation. If that
source is unavailable, the correct status remains
`cash-like-statutory-candidate; settlement-and-return-unproven`.

This pass should be read with the [CUSIP row proof packet](capital-flow-apollo-athene-statutory-cusip-row-proof-packet-pass-1.md),
the [CUSIP cashback inspection](capital-flow-apollo-athene-statutory-cusip-cashback-high-dollar-inspection-pass-1.md),
and the [legal-entity income/cash bridge](capital-flow-apollo-athene-statutory-legal-entity-income-cash-bridge-pass-1.md).
