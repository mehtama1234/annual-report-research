# Capital Flow PBF Insurance-Normalized Cash Flow Pass 1

## Purpose

This page executes debt/refinancing upgrade queue row `CFDRBUQ-015`.

It asks:

`Can PBF's first-half 2026 cash flow be normalized enough to compare with debt service and capital uses, or is recurring refinery return still unproven?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-pbf-insurance-normalized-cash-flow-pass-1.csv`

The upstream bridge is:

`/cluster/capital-flow-pbf-refining-liquidity-use-return-bridge-pass-1.md`

## Current Answer

`insurance-normalized-company-cash-proxy-visible-recurring-refinery-return-unproven`

PBF's Q2 `2026` filing supports a bounded company-level cash-flow quality answer. Reported first-half operating cash flow was `1.2651B USD`, but the same filing says net income included a `356.5M USD` gain on insurance recoveries, with `111.3M USD` of insurance proceeds related to operating activities and `245.2M USD` classified in investing activities. Removing only the operating-section insurance proceeds leaves a conservative company-level operating cash proxy of `1.1538B USD`.

That is enough to compare against visible debt service and capital-use burdens. It is not enough to claim recurring refinery-level return.

## What The Pass Adds

| Question | Evidence | Answer |
|---|---:|---|
| Was reported company cash generation visible? | `1.2651B USD` first-half operating cash flow. | Yes. |
| Was insurance material? | `356.5M USD` gain/proceeds total; `111.3M USD` operating; `245.2M USD` investing. | Yes, it must be bounded. |
| Does a simple operating-insurance adjustment still leave positive cash? | `1.1538B USD` OCF less operating insurance proceeds. | Yes, at company level. |
| Did reported cash cover PP&E? | `788.6M USD` OCF less `476.5M USD` PP&E spending. | Yes, before broader normalizations. |
| Did insurance-adjusted cash cover PP&E? | `677.3M USD` OCF less operating insurance proceeds and PP&E spending. | Yes, as a proxy. |
| Did cash cover PP&E plus turnaround spending? | `175.98%` reported OCF coverage; `160.50%` insurance-adjusted OCF coverage. | Yes, but this is a burden proxy, not management FCF. |
| Was debt-service comparison possible? | `90.9M USD` cash interest paid; about `12.7x` insurance-adjusted OCF coverage. | Yes, same-period proxy. |
| Is refinery-level recurring return proven? | No refinery-level cash contribution, capex return, or outage-normalized margin allocation. | No. |

## Normalization Logic

The cleanest local adjustment is intentionally narrow:

`reported OCF - operating-section insurance proceeds`

That gives:

`1.2651B USD - 111.3M USD = 1.1538B USD`

This is not a full adjusted free-cash-flow measure. It does not normalize working-capital timing, LCM inventory effects, taxes, business-interruption economics, refinery-level outage impact, or future insurance recoveries. It is only a conservative first control that prevents reported OCF from being treated as recurring refinery cash without qualification.

## Why This Matters

The earlier PBF bridge showed a named refinancing and company-level liquidity repair. The note-economics pass then showed measured 2028-to-2034 mechanics. This pass answers the next harder cash-quality question.

The evidence says PBF was not merely surviving on a one-time insurance check. Even after removing the `111.3M USD` operating insurance proceeds, first-half company cash flow remained large relative to PP&E, turnaround spending, and cash interest.

But the evidence also says insurance and outage effects are too important to ignore. Total visible insurance proceeds were about `28.18%` of reported OCF, and the filing still flags Martinez and Chalmette refinery fire risks. That blocks any clean recurring refinery-return claim.

## Decision

`company-level-cash-quality-proxy-visible`

Upgrade from:

`partial-local`

Hold below:

`recurring-refinery-return-visible`

## Safe Claim

`PBF's Q2 2026 filing supports insurance-bounded company-level cash-flow quality evidence. Reported first-half operating cash flow was 1.2651B USD; after removing 111.3M USD of operating-section insurance proceeds, a conservative company-level operating-cash proxy is 1.1538B USD. That proxy covered 476.5M USD of PP&E spending, 242.4M USD of deferred turnaround spending, and 90.9M USD of cash interest in the period. The evidence supports company-level cash-quality and debt-service comparison, not recurring refinery-level return, ABL-exit proof, or refinancing value creation.`

## Open Gaps

| Gap | Why It Matters | Next Source |
|---|---|---|
| Insurance recovery category detail | Needed to separate business interruption, property damage, operating expenses, and investing recovery. | Insurance recovery note, claim settlement schedule, and receivable rollforward. |
| Outage-by-refinery detail | Needed to normalize Martinez and Chalmette impacts. | Refinery incident disclosures, downtime schedule, throughput by refinery, and repair timetable. |
| Adjusted OCF reconciliation | Needed before writing recurring cash-flow quality as a management measure. | Company supplement, MD&A bridge, and non-GAAP reconciliation. |
| Refinery-level cash contribution | Needed to move from company-level cash quality to refinery-level return. | Refinery throughput, capex, turnaround, operating expense, margin, and cash contribution table. |
| Pro forma debt service | Needed to compare normalized cash flow to the post-refinancing stack. | Interest schedule, 2034 note cash coupon, redeemed 2028 coupon, ABL pricing, and amortized fees. |

## Hypothesis

`PBF's 2026 refinancing should be read as balance-sheet repair plus company-level cash recovery, not proven refinery-level value creation. The next proof layer is refinery-specific outage normalization and pro forma debt-service scheduling.`

## Next Work

1. Pull insurance recovery and receivable detail by category.
2. Find Martinez and Chalmette outage duration and throughput impact.
3. Build a pro forma cash-interest schedule after the 2028-to-2034 refinancing.
4. Search for refinery-level margin, capex, and cash contribution outside the 10-Q.
5. Keep ABL-exit and refinancing-value claims blocked until borrowing-base availability and pro forma economics are visible.
