# Capital Flow PBF Refining Liquidity Use/Return Bridge Pass 1

## Purpose

This page answers the next PBF question from the debt/refinancing use-return frontier:

`Does PBF's Q2 2026 debt/refinancing evidence connect to productive refinery use or operating return, or is it mainly a liquidity and balance-sheet bridge?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-pbf-refining-liquidity-use-return-bridge-pass-1.csv`

The upstream page is:

`/cluster/capital-flow-debt-refinancing-use-return-frontier-pass-1.md`

## Current Answer

`PBF now has a company-level refining liquidity and cash bridge. The filing explicitly ties 500.0M USD of 2034 senior notes, 492.1M USD of net proceeds, and available cash to the redemption of 801.6M USD of 2028 senior notes. It also shows first-half revolver draws of 1.100B USD, revolver repayments of 1.200B USD, zero quarter-end revolver debt, 1.2651B USD of operating cash flow, 476.5M USD of PP&E spending, 242.4M USD of turnaround spending, 887.3 thousand bpd of Q2 throughput, and 2.9263B USD of first-half gross refining margin excluding special items. That supports a refinancing/liquidity/cash bridge, not refinery-level return proof.`

## What The Bridge Adds

| Bridge Step | Evidence Now Visible | What It Means |
|---|---|---|
| Liquidity base | Cash and cash equivalents of `894.1M USD` at June `30`, `2026`. | PBF had source-visible balance-sheet liquidity after the refinancing period. |
| Named refinancing source | `500.0M USD` of `2034 7.25%` Senior Notes, with `492.1M USD` of net proceeds. | There is a named refinancing source, not just generic debt. |
| Named refinancing use | The filing says net proceeds plus available cash were used to fully redeem the `2028 6.00%` Senior Notes; the old notes fell from `801.6M USD` to zero. | PBF has explicit source/use refinancing evidence. |
| Revolver movement | First-half revolver borrowings of `1.100B USD`, repayments of `1.200B USD`, and zero quarter-end Revolving Credit Facility debt. | The balance sheet was actively managed, with a `100.0M USD` net revolver repayment. |
| Cash generation | First-half operating cash flow of `1.2651B USD`. | Same-period company cash generation is visible. |
| Productive-asset cash use | PP&E spending of `476.5M USD` and deferred turnaround spending of `242.4M USD`. | PBF used cash on refining assets and maintenance, but the filing does not allocate note proceeds to those uses. |
| Refining output | Q2 crude and feedstocks throughput of `887.3` thousand bpd and first-half throughput of `156.7M` barrels. | Same-period operating output exists at company level. |
| Refining margin context | First-half gross refining margin excluding special items of `2.9263B USD`, or `16.67 USD` per barrel. | Margin context exists, but it is not financing-return proof. |
| Covenant visibility | PBF states it was in compliance with all covenants, including financial covenants, in all debt agreements at June `30`, `2026`. | Compliance is visible, but headroom is not. |

## Decision

`refining-liquidity-cash-bridge-visible-company-level`

This is an upgrade from:

`denominator-visible-use-open`

The upgrade is narrow. PBF now has a named refinancing source/use bridge plus same-period cash, capital-use, output, and margin context. It still does not reach:

`refinery-level-return-visible`

## Why This Matters

PBF answers a different part of the debt/refinancing lane than Wheaton, Matador, or Liberty Broadband.

Wheaton is a named stream-acquisition funding case. Matador is a reserve-backed borrowing-base and operating-output case. Liberty Broadband is a holding-company collateral and transaction-liquidity case. PBF is a refining company balance-sheet case: the evidence shows notes refinancing, revolver churn, liquidity, cash generation, and operating throughput in the same period, but it does not show that the refinancing caused a refinery-level cash return.

## Open Gaps

| Gap | Why It Matters | Next Source |
|---|---|---|
| ABL mechanics | Needed to confirm borrowing-base availability, collateral, and whether there was an ABL exit or only revolver balance management. | Revolving Credit Facility agreement, amendment, borrowing-base certificate, and availability table. |
| Refinancing economics | Needed to judge whether the new `7.25%` notes improved or worsened the debt stack after fees, redemption cost, maturity extension, and coupon difference. | 2034 indenture, 2028 redemption notice, interest-expense rollforward, and pro forma debt-service schedule. |
| Covenant headroom | Needed to move from covenant-compliance language to resilience evidence. | Covenant calculation certificate and liquidity covenant schedule. |
| Refinery-level cash return | Needed to tie capex or turnaround spending to named refinery output, margin, or cash conversion. | Refinery-level throughput, capex, turnaround, margin, and cash contribution tables. |
| Insurance normalization | Needed because first-half operating cash flow includes insurance recovery effects. | Insurance recovery schedule and outage-by-refinery detail. |

## Hypothesis

`PBF is primarily a refining liquidity and balance-sheet repair bridge. The strongest safe claim is that named debt proceeds plus cash refinanced older notes while the company generated operating cash and maintained/refreshed refinery assets. The current evidence does not support a refinery-level return claim.`

## Safe Claim

`PBF's Q2 2026 filing ties a 500.0M USD 2034 senior-note issuance, 492.1M USD of net proceeds, available cash, and redemption of 801.6M USD of 2028 senior notes to a company-level liquidity bridge. It also shows 1.100B USD of first-half revolver borrowings, 1.200B USD of revolver repayments, zero quarter-end revolver debt, 894.1M USD of cash, 1.2651B USD of operating cash flow, 476.5M USD of PP&E spending, 242.4M USD of turnaround spending, 887.3 thousand bpd of Q2 throughput, and 2.9263B USD of first-half gross refining margin excluding special items. This supports company-level refining liquidity and cash-bridge language, not ABL-exit proof, covenant-headroom proof, refinancing value-creation proof, or refinery-level return proof.`

## Next Work

1. Extract the Revolving Credit Facility agreement and any Q2 2026 amendment.
2. Find borrowing-base availability, collateral, and covenant calculation detail.
3. Build a 2028-to-2034 note economics table: coupon, maturity, fees, extinguishment loss, interest expense, and annualized cash interest.
4. Pull refinery-level throughput, turnaround, capex, and margin detail if PBF discloses it outside the 10-Q.
5. Normalize operating cash flow for insurance recoveries before making any recurring cash-return claim.
