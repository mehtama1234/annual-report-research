# KKR / Global Atlantic / Accordia Q2 2026 statutory cash-flow refresh

Research date: `2026-09-18`

## Purpose

The public Global Atlantic statutory portal now provides Accordia Life and
Annuity Company's quarterly statement for the quarter ended June 30, 2026.
This refresh adds a current-period legal-entity cash and liability surface to
Q-12. It does not allocate those totals to the three named Accordia CUSIPs in
the disposal packet.

The structured companion is the [Accordia Q2 cash-flow CSV](data/capital-flow-kkr-global-atlantic-accordia-q2-2026-statutory-cash-flow-refresh-2026-09-18.csv).

## Current-period observations

| Field | June 30, 2026 / H1 2026 | Use | Boundary |
|---|---:|---|---|
| Net admitted assets | `$12.146052B` | Legal-entity balance-sheet perimeter | Not unrestricted parent cash |
| Bonds, admitted | `$7.371492B` | Named-asset population scale | Q2 verification PDF does not provide the selected CUSIP rows |
| Cash, cash equivalents and short-term investments | `$259.286M` | Legal-entity ending cash | Includes cash equivalents and is not an upstream KKR receipt |
| Funds held under coinsurance | `$4.240949B` | Liability/funding perimeter | Not freely distributable cash |
| Total liabilities | `$11.411695B` | Senior-claim context | Does not allocate liability cost to a named bond |
| Surplus | `$734.357M` | Statutory capital context | Not common-owner residual |
| Net investment income, summary operations | `$291.515M` | Current-period earnings context | Not named-asset cash or platform profit |
| Net investment income, cash flow | `$288.780M` | Collected-income cash-flow context | Not named-asset attribution |
| Federal and foreign income taxes paid/(recovered) | `$(31.085M)` | Current-period tax cash control | Aggregate legal-entity tax line; not asset allocation |
| Net cash from operations | `$75.718M` | Current-period operating-cash control | Not KKR cash and not named-asset return |
| Investment proceeds | `$764.721M` | Proceeds source/use surface | Not joined to the Intel/Commonwealth Edison/Orange rows |
| Investments acquired | `$906.633M` | Reinvestment burden | Not allocated to named assets or funding source |
| Net cash from investments | `$(163.923M)` | Investment cash-burn control | Not a return calculation |
| Net cash from financing and miscellaneous sources | `$111.230M` | Funding/liability flow context | Does not identify KKR remittance or owner cash |
| Net change in cash | `$23.025M` | Period cash reconciliation | Does not prove availability or distribution |
| Ending cash, cash equivalents and short-term investments | `$259.286M` | Reconciled ending legal-entity cash | Not unrestricted or upstream cash |

## Interpretation

The current public chain is now stronger at the legal-entity level:

```text
Accordia assets and liabilities
  -> current-period investment income and proceeds
  -> investment purchases and financing flows
  -> statutory operating cash and ending cash
```

The chain still stops before the named-asset return question:

```text
Intel / Commonwealth Edison / Orange CUSIP
  -> statutory disposal consideration
  -> broker or custodian settlement
  -> Accordia cash account
  -> liability-cost / reinsurance allocation
  -> Global Atlantic / KKR residual
```

The Q2 statement therefore improves the denominator and burden perimeter, but
the aggregate `$764.721M` proceeds and `$259.286M` ending cash must not be
assigned to the three disposal rows or treated as KKR owner cash.

## Portal-linked reinsurance boundary

The same official Global Atlantic portal links an `ALIRT Q2 2026 Exhibit`, but
that one-page exhibit is not an Accordia Schedule D or a named-asset settlement
record. It presents an unaudited, notional attribution for Global Atlantic Re
and Global Atlantic Assurance to Forethought Life Insurance Company (FLIC):
`$3.779481B` of attributed capital and surplus, `$78.315M` of attributed
after-tax operating income, and `$62.764M` of attributed net income for H1
2026. It also shows a notional FLIC invested-asset allocation of `$808.825M`
of bonds and `$30.381M` of gross bond/mortgage/cash investment income before
`$2.218M` of expense.

The exhibit expressly says the analysis is for a rating-agency evaluation and
is not prepared under statutory, GAAP, or another comprehensive accounting
basis. It is therefore useful as a reinsurance/funds-held attribution
boundary, but it cannot allocate Accordia's selected CUSIPs, prove a cash
transfer, or replace the controlled liability-cost and remittance request.

## Derived current-period diagnostics

These ratios are legal-entity diagnostics for H1 2026, not named-asset returns:

| Diagnostic | Calculation | Result | Read-through |
|---|---:|---:|---|
| Cash investment income / summary investment income | `$288.780M / $291.515M` | `99.06%` | Reported investment income was closely matched by the cash-flow investment-income line |
| Operating cash / summary investment income | `$75.718M / $291.515M` | `25.97%` | Only a minority of summary investment income remained in aggregate operating cash after the statement's operating adjustments |
| Investment proceeds / investments acquired | `$764.721M / $906.633M` | `84.35%` | Current-period acquisitions exceeded reported investment proceeds |
| Net investment cash burn / summary investment income | `$163.923M / $291.515M` | `56.23%` | The aggregate investment portfolio absorbed cash equal to more than half of summary investment income |

The diagnostics make the cash-quality and reinvestment burden visible, but do
not identify which CUSIP generated proceeds, which liability or reinsurance
claim consumed cash, or whether any residual reached KKR/common owners.

## September 18, 2026 Schedule D activity cross-check

The same Q2 statutory verification package adds a book-activity control even
though it does not expose the full named Schedule D rows. Schedule D
verification reports `$1.055732B` of bonds and stocks acquired,
`$922.749M` of consideration for bonds and stocks disposed, `$25.769M` of
current-year other-than-temporary impairment, `$1.027822M` of investment
income recognized from prepayment penalties and/or acceleration fees, and
`$8.215277B` of ending bonds-and-stocks book/adjusted carrying value.

These are statutory book-activity and income controls, not a replacement for
the cash-flow statement's `$764.721M` investment proceeds or for a named-CUSIP
settlement. The difference in scope is important: book-value acquisitions and
disposals, cash-flow proceeds, and selected named-asset rows cannot be joined
without lot-level custody or broker records. The new control therefore
strengthens the legal-entity activity perimeter while preserving the named
asset boundary:

`current Schedule D book activity visible; named CUSIP settlement,
liability-cost allocation, and KKR residual still unproven.`

## Promotion boundary

This is a `current-legal-entity-cash-and-liability-control`, not a named-cash
or return promotion. Q-12 still requires a same-CUSIP settlement record,
liability-cost allocation, reinsurance/funds-held waterfall, and platform or
common-owner residual before an asset-level return can be claimed.

## Portal source-availability boundary

The Global Atlantic financial-statements portal was checked for a separate
Q2 2026 Accordia Schedule D or Schedule BA/CUSIP package. The public Q2 link
resolves to the 52-page verification statement used here; searches within that
document do not locate the three packet CUSIPs (`458140-BM-1`,
`202795-JY-7`, or `685218-AB-5`). The result is
`public-current-cash-statement-available; current-named-cusip-schedule-not-located`.
It does not imply that the schedule is nonexistent or unavailable through a
regulator or controlled data channel.

An additional official-portal URL probe for alternate `accordia-q2-2026`
quarterly-statement filenames did not locate an accessible fuller public
Schedule D/BA document. Keep the portal-linked verification PDF as the public
source anchor and route future CUSIP work through a controlled statutory,
regulatory, custodian, or broker source.

Status: `current-entity-cash-surface-upgraded; named-asset-settlement-unproven`

## Primary source

[Accordia Life and Annuity Company Q2 2026 statutory quarterly statement](https://www.globalatlantic.com/content/dam/global-atlantic/investors/financial-statements/annual-and-quarterly-statements/accordia-q2-2026-quarterly-statement-verifications.pdf), pages 2–5 and 14; Schedule D verification on PDF page 45 / printed page `SI01`.

[Global Atlantic ALIRT Q2 2026 Exhibit](https://www.globalatlantic.com/content/dam/global-atlantic/investors/financial-statements/annual-and-quarterly-statements/alirt-q2-2026-exhibit.pdf), page 1; portal-linked reinsurance attribution boundary only.
