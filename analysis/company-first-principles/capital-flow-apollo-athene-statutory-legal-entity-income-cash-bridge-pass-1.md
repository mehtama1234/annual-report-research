# Capital Flow Apollo Athene Statutory Legal-Entity Income Cash Bridge Pass 1

## Purpose

This pass moves Apollo/Athene from near-reconciled Schedule D holdings toward the next cash question:

`Does the Athene legal entity show asset income, cash conversion, investment turnover, liability funding scale, and credit/reserve pressure?`

The generated companion table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-legal-entity-income-cash-bridge-pass-1.csv`

The bridge script is:

`scripts/build-athene-legal-entity-income-bridge.py`

## Current Schedule D correction — 2026-09-18

The historical pass-1 table below retains its original pre-correction parser
base for reproducibility. The current rerun now emits `158.852395199B USD`
of combined Section 1 plus Section 2 book/adjusted carrying value against the
page-451 statutory verification total of `158.852395201B USD`, a `$2` aggregate
difference. The issuer-credit and ABS components each differ by `$1`.

This improves the asset denominator from a broad near-reconciliation to an
effectively exact aggregate tie, but it does not change the bridge's cash
boundary: income, proceeds, impairments, liability cost, borrower receipt, and
return remain unjoined at holding level. See the [current Schedule D correction
pass](capital-flow-apollo-athene-statutory-schedule-d-reconciliation-correction-pass-2-2026-09-18.md)
and the [sparse-row worklist](capital-flow-apollo-athene-statutory-sparse-row-classification-pass-1.md).

The upstream Schedule D residual diagnostic is:

`/cluster/capital-flow-apollo-athene-statutory-schedule-d-residual-gap-diagnostic-pass-1.md`

The 2026-09-18 interest-column repair is now a separate controlled input to
this bridge. The full-range parser anchors the two interest fields to the
acquisition-date columns rather than to trailing numeric tokens, preventing
payment-at-maturity from being mislabeled as received interest. The corrected
population reports `$6.230478121B` of Schedule D received interest; AP Grange
`G2964#-AA-7` reports `$7.219623M` of interest income and `$230.263772M`
received, while Treasury Strip `912803-DM-2` preserves blank interest fields.
See the [interest-column repair pass](capital-flow-apollo-athene-statutory-schedule-d-interest-column-repair-pass-1.md).

## Short Answer

`Yes, at legal-entity bridge level. Athene Annuity and Life Company shows a near-reconciled Schedule D bond base, statutory net investment income, cash-flow support for investment income, collected-versus-earned income proximity, bond and mortgage-loan proceeds, liability-base scale, AVR reserve pressure, IMR mechanics, and current-year OTTI. This is a real upgrade from "where are assets?" to "did the legal entity generate cash/income from the asset base?" It is still not full named cash proof because the income, proceeds, impairments, and liability cost are not yet joined to individual holdings, borrowers, or return models.`

## Bridge Results

| Bridge | Numerator | Denominator | Ratio | Status |
|---|---:|---:|---:|---|
| Near-reconciled Schedule D parser book to statutory bond reference | `158.852395199B USD` | `158.852395201B USD` | `~100.0000%` | aggregate tie within `$2` |
| Net investment income to core invested asset base | `12.732699320B USD` | `270.261704399B USD` | `4.7112%` | legal-entity income visible |
| Cash-flow net investment income to summary net investment income | `12.281980822B USD` | `12.732699320B USD` | `96.4601%` | cash-income proxy visible |
| Gross collected investment income to gross earned investment income | `13.601183683B USD` | `14.010808604B USD` | `97.0764%` | collected-versus-earned visible |
| Collected bond income to statutory Schedule D bond base | `7.859004314B USD` | `158.852395201B USD` | `4.9474%` | bond-income category visible |
| Reconciled page-18 collected bond income to statutory Schedule D bond base | `8.127852536B USD` | `158.852395201B USD` | `5.1166%` | near-reconciled within `$2` after Part 4/5 and footnote bridge |
| Net investment income less contract/deposit interest adjustments to net investment income | `6.842002522B USD` | `12.732699320B USD` | `53.7357%` | bounded same-period liability-burden screen |
| Individual-annuity liability-interest burden to summary liability-interest line | `5.882288174B USD` | `5.890696798B USD` | `99.8573%` | line-of-business allocation visible |
| Group-annuity liability-interest burden to summary liability-interest line | `8.408625M USD` | `5.890696798B USD` | `0.1427%` | line-of-business allocation visible |
| Gross derivative assets to core invested asset base | `2.482135218B USD` | `270.261704399B USD` | `0.9184%` | hedge scale visible; not hedge cost |
| Schedule DB termination considerations to Part A ending book value | `2.009384164B USD` | `3.513012150B USD` | `57.2%` | derivative turnover/cash control; not free cash |
| Collected mortgage-loan income to first-lien mortgage loans | `4.557162846B USD` | `84.664838463B USD` | `5.3826%` | mortgage-income category visible |
| Bond sale/maturity/repayment proceeds to Schedule D bond base | `54.035221430B USD` | `158.852395201B USD` | `34.0160%` | bond proceeds visible |
| Mortgage-loan sale/maturity/repayment proceeds to mortgage-loan base | `12.676073505B USD` | `84.664838463B USD` | `14.9721%` | mortgage proceeds visible |
| Core invested asset base to life reserve plus deposit liability base | `270.261704399B USD` | `174.875533582B USD` | `154.5452%` | asset-liability scale visible |
| Asset valuation reserve to core invested asset base | `6.291800508B USD` | `270.261704399B USD` | `2.3280%` | statutory risk reserve visible |
| Interest maintenance reserve to bond proceeds | `219.835675M USD` | `54.035221430B USD` | `0.4068%` | realized-gain/loss smoothing visible |
| Current-year OTTI to Schedule D bond base | `110.227270M USD` | `158.852395201B USD` | `0.0694%` | impairment scale visible |

## What This Tells Us

This is the clearest Apollo/Athene money-flow statement so far:

`policyholder/reserve/deposit-type liability channel -> Athene legal entity -> bonds, mortgage loans, Schedule BA assets, and liquid assets -> statutory investment income and investment cash flow -> proceeds, reserves, IMR/AVR, and impairment pressure`

In simpler words:

Athene is not just holding a large asset book. The statutory statement shows the legal entity earned investment income, collected most of the income it earned, generated investment-income cash flow, and received large proceeds from bond and mortgage-loan turnover.

## Cash-conversion quality boundary

The cash conversion ratios are useful return-quality controls before any
liability-adjusted yield is attempted:

| Test | Calculation | Result | Safe interpretation |
| --- | --- | ---: | --- |
| Statutory cash-flow investment income | `$12.281980822B / $12.732699320B` | `96.4601%` | Most reported net investment income is represented in the statutory cash-flow line; the remaining gap is not automatically a loss |
| Collected gross investment income | `$13.601183683B / $14.010808604B` | `97.0764%` | Collected and earned gross income are close, but timing and classification remain possible explanations |
| Core assets against life-reserve and deposit liabilities | `$270.261704399B / $174.875533582B` | `154.5452%` | Asset and liability scale can be compared; this is not surplus available to Apollo |

The first two gaps are approximately `$450.718M` and `$409.625M`, respectively.
They should remain labeled as cash-conversion or collection differences, not
be deducted as recurring credit losses or treated as distributable cash. The
remaining return problem is the liability-block cost, credited-rate schedule,
capital requirement, impairment allocation, and legal-entity-to-Apollo route.

## Schedule BA disposal-to-legal-entity cash boundary

The corrected Schedule BA verification gives a controlled Part 3 disposal
consideration total of `$4,417,190,618`, within `$2` of the source control
`$4,417,190,620`. The legal-entity cash bridge separately shows aggregate bond
sale/maturity/repayment proceeds of `$54,035,221,430` and mortgage-loan
sale/maturity/repayment proceeds of `$12,676,073,505`.

These figures are not additive proof of a BA cash waterfall. The statutory cash
flow presentation does not allocate aggregate proceeds to the 168 BA event rows,
and the BA verification total does not identify the settlement account,
counterparty receipt, liability release, taxes/fees, or Apollo distribution.
The 57 BA rows whose coordinate disposal-nature column is exactly `Sale`
total `$1,847,866,086`, but that is a prioritized statutory event population,
not a legal-entity cash total. The BA-to-Schedule-D crosswalk finds only three
same-CUSIP matches, including two `Security Withdraw` transfer holds and one
different-date/different-perimeter collision.

The subsequent [Schedule BA exact-lot page review](capital-flow-apollo-athene-statutory-schedule-ba-exact-lot-page-review-pass-1.md)
classifies the four strongest same-identifier screens without changing this
cash boundary: two rows have a visible `Sale` marker, while two have blank
disposal-nature fields and approximately twice the Part 2 cost relative to the
Part 1/Part 3 book. The review confirms source-column continuity and lot-count
warnings, but does not allocate any row to the aggregate legal-entity proceeds
or to an Athene-to-Apollo receipt.

Income has a parallel boundary: Schedule BA Part 1 row income reconciles to
positive `$237,086,006`, while page 18 reports Other invested assets income of
`$(185,080,219)` collected and `$(132,204,517)` earned. See the [BA income-category boundary](capital-flow-apollo-athene-statutory-ba-income-category-boundary-pass-1.md); neither figure is promoted to named-asset cash until the perimeter is reconciled.

The [income-category reconciliation pass](capital-flow-apollo-athene-statutory-ba-income-category-reconciliation-pass-1.md)
now makes the mismatch arithmetic explicit: the naive Part 1-to-page-18
differences are `$422.166225M` against the collected category and
`$369.290523M` against the earned category. These are diagnostic perimeter
residuals, not losses or missing receipts. The `$156.037953M` Part 3 event-income
population is held separately because it may overlap the Part 1 population.

The page-18 / Schedule D perimeter bridge provides a second control. Page-18
bond categories report `$8.127852536B` collected and `$8.279777653B` earned,
while the corrected Schedule D row fields report `$1.504450447B` of interest
income due and accrued and `$6.230478121B` of interest received. The source
footnote identifies `$400.899897M` of discount accrual, `$223.877582M` of
premium amortization, and `$487.050806M` paid for accrued interest on
purchases. These distinctions explain why the `$1.897374415B` collected-versus-
received difference—and the `$392.923968M` collected-versus-both-fields
comparison—remain definition/perimeter diagnostics rather than reconciled cash
shortfalls. See the [page-18 / Schedule D perimeter bridge pass 2](capital-flow-apollo-athene-statutory-page18-schedule-d-perimeter-bridge-pass-2.md).
The corrected Schedule D row population also ties the filing's issuer-credit
and asset-backed-security subtotal rows exactly for both interest fields. The
combined source-controlled totals are `$1.504450447B` of interest income due
and accrued and `$6.230478121B` of interest received. See the [Schedule D
interest subtotal control](capital-flow-apollo-athene-statutory-schedule-d-interest-subtotal-control-pass-1.md).
The source-defined population boundary is also explicit: page 18 is full-year
income, Part 1 is year-end owned assets, and Parts 4–5 are disposed or
acquired-then-disposed assets. The [income population boundary pass](capital-flow-apollo-athene-statutory-income-population-boundary-pass-1.md)
routes that distinction into the next reconciliation without assigning the
residual to disposals.

The liability side now has a same-period statutory burden control: Summary of
Operations line 17 reports `$5.890696798B` of interest and adjustments on
contract or deposit-type contract funds. Subtracting that line from net
investment income gives a mechanical `$6.842002522B` residual, or `53.7357%`
of net investment income. See the [liability-interest burden bridge](capital-flow-apollo-athene-statutory-liability-interest-burden-bridge-pass-1.md).

The filing now supports a limited allocation of that burden by business line:
the individual-annuity schedule reports `$5.882288174B` and the group-annuity
schedule reports `$8.408625M`. Their sum is `$5.890696799B`, one dollar above
the summary line. This is a line-of-business control, not product-level
credited-rate or normalized cost-of-funds proof. Exhibit 7 separately reports
`$2.649832829B` of investment earnings credited to deposit-type contract
accounts and a `$64.259784362B` net after-reinsurance ending balance; neither
figure is substituted for line 17 without an accounting bridge. See the
[line-of-business liability allocation pass](capital-flow-apollo-athene-statutory-liability-interest-by-line-of-business-pass-1.md).

The same statutory notes also identify the hedge mechanism that sits between
asset income and policyholder crediting: options, futures, variance swaps,
swaptions for minimum crediting-rate exposure, and interest-rate swaps for
asset/liability mismatches. Gross derivative assets are `$2.482135218B`, of
which `$2.479627050B` is admitted. This is a quantified hedge-scale control,
not a hedge-cost or cash-settlement bridge. See the [derivative hedge boundary
pass](capital-flow-apollo-athene-statutory-derivative-hedge-boundary-pass-1.md).

Schedule DB now adds direct derivative turnover controls: Part A reports
`$2.009384164B` of termination consideration against a displayed ending
book/adjusted carrying value of `$3.513012150B`, a `$(491.016129M)` termination
gain/loss, and `$3.283681900B` of unrealized valuation change. Part B reports
`$108.756075M` of cumulative futures cash change. The page-491 Schedule DB
verification closes book value and fair value within `$1` and potential
exposure at the displayed control. These are derivative cash/valuation layers,
not normalized hedge return, policyholder-cost allocation, or owner cash. See
the [Schedule DB verification pass](capital-flow-apollo-athene-statutory-schedule-db-verification-pass-1.md).

The next reconciliation closes the page-18 collected-bond bridge to within
`$2`: Part 1 received interest of `$6.230478121B` plus Part 4/5 bond
interest/dividends of `$2.207402908B`, less the page-18 net footnote adjustment
of `$310.028491M`, reconstructs `$8.127852538B` against the reported
`$8.127852536B`. See the [page-18/Schedule D income reconciliation pass 3](capital-flow-apollo-athene-statutory-page18-schedule-d-income-reconciliation-pass-3.md).

## What It Proves

This pass proves:

1. the near-reconciled Schedule D base can be used as a legal-entity asset denominator with a hold flag
2. statutory net investment income is visible against the core invested asset base
3. cash-flow net investment income supports the income line at `96.4601%`
4. collected gross investment income is close to earned gross investment income at `97.0764%`
5. bond income and mortgage-loan income are visible by statutory category
6. bond and mortgage-loan sale/maturity/repayment proceeds are visible
7. liability scale is visible through life reserves and deposit-type contracts
8. risk and realized-gain/loss reserve mechanics are visible through AVR and IMR
9. current-year OTTI is visible as a credit-cost pressure measure
10. the liability-interest burden is allocable to individual and group annuity business lines within a one-dollar source-control tolerance
11. statutory notes identify liability-linked hedge mechanisms and quantify gross derivative scale
12. Schedule DB exposes derivative termination consideration, futures cash change, gain/loss, valuation, and verification controls

## What It Still Does Not Prove

It does not yet prove:

1. income by CUSIP or issuer
2. cash received from any specific borrower
3. disposal proceeds by holding
4. realized gain/loss by holding
5. impairment by holding
6. liability cost or credited rate by product block
7. legal-entity spread after policyholder funding cost
8. asset-level IRR, NPV, ROIC, payback, or cash yield
9. product/block-level credited rates, reserve duration, surrender behavior, or a full Exhibit 7-to-line-17 accounting bridge
10. derivative premium, hedge settlement, hedge effectiveness, product attribution, or liability-adjusted return
11. derivative termination consideration as free cash or Apollo common-owner cash

## Decision

`apollo-athene-statutory-legal-entity-income-cash-bridge-visible-holding-join-next`

Apollo/Athene now has legal-entity asset base, income, cash-flow, proceeds, liability-scale, reserve-pressure, and impairment-scale evidence. The page-18 collected-bond category also reconciles to Schedule D Parts 1, 4, and 5 plus the statutory footnote within `$2`. The next gate is joining the reconciled legal-entity cash line to liability-cost schedules and named settlement/borrower evidence.

## Safe Claim

`Athene Annuity and Life Company shows a statutory legal-entity bridge from assets to income and cash-flow: 12.732699320B USD of net investment income, 12.281980822B USD of cash-flow net investment income, 13.601183683B USD of collected gross investment income, 8.127852536B USD of page-18 collected bond income reconciled to Schedule D Parts 1/4/5 within $2, 54.035221430B USD of bond sale/maturity/repayment proceeds, and a 158.852395199B USD parsed Schedule D bond base that ties the statutory reference within $2. This supports legal-entity income/cash conversion language, not holding-level borrower cash or asset-return proof.`

## Next Work

1. Resolve the highest-priority BA Sale rows against custodian, trustee, counterparty, settlement, or liability-release evidence.
2. Obtain liability-cost or credited-rate schedules for reserves and deposit-type contracts.
3. Resolve the highest-priority named settlement, trustee, or borrower-remittance rows without double counting the reconciled statutory income.
4. Reconcile Schedule BA income and disposal populations to legal-entity cash-flow categories without double counting.
5. Build the first legal-entity spread bridge after liability-cost extraction.
