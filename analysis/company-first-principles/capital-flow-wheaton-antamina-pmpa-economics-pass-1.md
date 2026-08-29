# Capital Flow Wheaton Antamina PMPA Economics Pass 1

## Purpose

This page executes debt/refinancing upgrade queue row `CFDRBUQ-003`.

It asks:

`Can Wheaton's Antamina PMPA be upgraded from source/use/output terms to a stream-level economics proxy, or is return still unproven?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-wheaton-antamina-pmpa-economics-pass-1.csv`

The upstream page is:

`/cluster/capital-flow-wheaton-antamina-use-return-bridge-pass-1.md`

## Current Answer

`pmpa-economics-proxy-visible-return-model-incomplete`

Wheaton now has Antamina stream-level economics proxy evidence. The Q2 `2026` financial statements report Antamina silver-interest first-half revenue of `277.563M USD`, cost of sales excluding depletion of `55.340M USD`, depletion of `51.322M USD`, profit of `170.901M USD`, operating cash flow of `222.223M USD`, and assets of `4.708329B USD`.

That is a real upgrade. The earlier bridge had contract terms and company-level cash; this pass adds stream-level revenue, cash cost, depletion, profit, OCF, and asset base.

It still does not prove full return because we still lack the delivered-ounce schedule, mine-life/reserve profile, taxes, financing-cost allocation, lender allocation, and discounted PMPA cash-flow model.

## What The Pass Adds

| Test | Evidence | Answer |
|---|---:|---|
| Named upfront use | `4.300B USD` Antamina PMPA cash outflow. | Visible. |
| Output entitlement | `67.50%` attributable payable production. | Visible as a contract term. |
| Delivery cash cost | `20.00%` of silver spot price on delivery. | Visible as a contract term. |
| Stream revenue | `277.563M USD` H1 2026 Antamina revenue. | Visible. |
| Stream cash cost | `55.340M USD` cost of sales excluding depletion. | Visible. |
| Stream depletion | `51.322M USD`. | Visible. |
| Stream profit | `170.901M USD`. | Visible. |
| Stream operating cash flow | `222.223M USD`. | Visible. |
| Stream asset base | `4.708329B USD`. | Visible. |
| Return model | Delivery schedule, taxes, interest allocation, reserve life, and discounting. | Still incomplete. |

## Economics Proxy

The first useful proxy is cash margin before depletion:

`277.563M USD - 55.340M USD = 222.223M USD`

That equals reported Antamina operating cash flow in the table. Cash cost excluding depletion was about `19.93%` of revenue, consistent with the `20.00%` delivery payment formula.

The rough first-half cash-yield proxy is:

`222.223M USD / 4.300B USD = 5.17%`

Mechanically annualized, that becomes:

`10.34%`

That should be read only as a screen. It is not IRR, NPV, reserve-life proof, or debt-service-adjusted return.

## Why This Matters

Wheaton is the first debt/refinancing case where the evidence has moved beyond company-level liquidity and into a named asset's stream economics. PBF and Devon now have strong company-level cash-quality proxies; Liberty has holdco debt-retirement mechanics; Matador has borrowing-base and debt-service quality proxies. Wheaton now has the strongest stream-specific economics proxy because the financial statements expose Antamina revenue, cost, depletion, profit, OCF, and assets.

The safe conclusion is sharper:

`Antamina is no longer just a 4.300B USD use-of-cash row. It is a stream with visible first-half revenue, cost, depletion, profit, operating cash flow, and asset base.`

The unsafe conclusion remains:

`The PMPA has proven its full economic return.`

## Decision

`stream-economics-proxy-visible`

Upgrade from:

`source-use-output-cash-bridge-visible-company-level`

Hold below:

`pmpa-return-model-proven`

## Safe Claim

`Wheaton's Antamina PMPA now has stream-level economics proxy evidence. The Q2 2026 filing shows a 4.300B USD Antamina PMPA cash outflow, a 67.50% attributable-payable-production term, a 20.00% delivery payment formula, H1 2026 Antamina revenue of 277.563M USD, cost of sales excluding depletion of 55.340M USD, depletion of 51.322M USD, profit of 170.901M USD, operating cash flow of 222.223M USD, and assets of 4.708329B USD. This supports stream-level economics proxy language, not full PMPA return, IRR, NPV, reserve-life, tax, interest, debt-service, or lender-allocation proof.`

## Open Gaps

| Gap | Why It Matters | Next Source |
|---|---|---|
| Delivered ounces | Needed to turn entitlement into realized volume. | Mine-by-mine delivery schedule and Wheaton production/sales table. |
| Reserve and mine life | Needed to test life-of-mine durability. | Antamina reserve report, mine plan, or technical report. |
| Tax allocation | Needed for after-tax return. | Stream-level tax schedule. |
| Interest/debt-service allocation | Needed to test debt-funded return. | Facility draw schedule, interest allocation, and debt-service waterfall. |
| Discounted cash-flow model | Needed for IRR/NPV. | PMPA cash-flow forecast, delivery curve, price assumptions, taxes, and discount rate. |

## Hypothesis

`Antamina likely has enough stream-level cash generation to justify deeper return modeling, but the public local evidence still stops at proxy economics. The next decisive source is delivered-ounce and reserve-life support, followed by debt-service and tax allocation.`

## Next Work

1. Extract Antamina delivered ounces and realized sales volumes.
2. Pull Antamina reserve/mine-life evidence from Wheaton, BHP, Teck, Glencore, or Antamina technical filings.
3. Build a tax/depletion/interest allocation pass from the financial statements and facility note.
4. Search for PMPA agreement or amendment terms for the 2026 BHP acquisition.
5. Build a true return model only after delivery curve, tax, and debt-service allocation are source-visible.
