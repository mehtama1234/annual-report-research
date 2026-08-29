# Capital Flow CFNSAQ-005 Return Model Support Pass 1

## Purpose

This page executes the fifth row of the next-source acquisition queue.

It asks:

`Can current local sources support a real return model: IRR, NPV, ROIC, reserve life, earned return, or cash yield tied to the funded asset or project?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-cfnsaq-005-return-model-support-pass-1.csv`

The queue input is:

`/cluster/capital-flow-next-source-acquisition-queue-pass-1.md`

## Short Answer

`CFNSAQ-005 is executed against the current local source set. It finds three partial return proxies: Wheaton Antamina, FPL Distribution Inspection, and United Rentals fleet. Energy Transfer, Matador, and Plains remain holds. No row reaches full IRR, NPV, ROIC, reserve-life, earned-return, or financed asset-return proof.`

## Execution Result

| Row | Target Case | Current Evidence | Result | What Still Blocks Proof |
|---|---|---|---|---|
| `CFNSAQ005-001` | Wheaton Antamina | `4.300B USD` PMPA payment; H1 `2026` Antamina revenue of `277.563M USD`; cash cost of `55.340M USD`; profit after depletion of `170.901M USD`; `33.750%` acquired silver production interest; `67.500%` payable production; `20.000%` delivery cash-cost formula | `partial-named-asset-return-proxy` | Delivered-ounce schedule, cash-receipt detail, tax allocation, interest allocation, debt-service waterfall, lender allocation, reserve-life support, PMPA IRR/NPV |
| `CFNSAQ005-002` | FPL Distribution Inspection | `193199` actual projects; `61.500000M USD` actual capital cost; `15.942971M USD` final category recovery; `38.320627M USD` final expenditures; `22.263219M USD` plant additions; equity/debt/depreciation recovery components | `partial-regulated-earned-return-component-proxy` | Category customer receipts, billing determinants, financing-source allocation, actual earned ROE, shareholder cash return, project IRR |
| `CFNSAQ005-003` | United Rentals fleet | Q2 `2026` OEC of `23.8B USD`; rental revenue/OEC of `16.2%`; adjusted EBITDA/OEC of `8.6%`; H1 `2026` OCF/gross rental capex coverage of `112.8%`; OCF/net fleet cash investment coverage of `162.0%` | `partial-fleet-and-segment-return-proxy` | Fleet-class OEC, true utilization, growth/replacement capex split, segment operating profit, asset-level ROIC, borrowing-cost allocation |
| `CFNSAQ005-004` | Energy Transfer projects | Q2 `2026` adjusted EBITDA of `5.07B USD`; DCF of `2.59B USD`; growth capex of `1.10B USD`; FY `2026` growth-capex guidance of `5.6B-5.9B USD` | `hold-no-named-project-return-model` | Named project cost, source-to-project allocation, utilization, project revenue, project EBITDA/DCF, debt-service allocation, shipper billing |
| `CFNSAQ005-005` | Matador borrowing base | H1 `2026` source/use reconciliation; development capex of `745.343M USD`; oil-and-gas property acquisitions of `1.228834B USD`; borrowing-base and aggregate production/cash context | `hold-no-reserve-backed-asset-return-model` | Reserve report, reserve-life sufficiency, asset-area production/cash margin, LOE, BLM contribution, borrowing-cost allocation |
| `CFNSAQ005-006` | Plains tariff route | Texas RRC tariff `TX 3.6.0`; `178.98` cents per barrel route rate; Cactus III capacity above `600000` bpd; acquisition/control context | `hold-no-route-asset-return-model` | Committed volume, billed barrels, utilization, realized route revenue, Cactus III EBITDA/cash contribution, acquisition debt-service allocation |

## What This Answers

This pass is the final return layer:

- Wheaton is strongest because named asset cash use and stream economics are visible.
- FPL is strong in regulated-return component math, but it still lacks category receipts and actual earned cash return.
- United Rentals has the cleanest fleet productivity/cash coverage proxy, but not fleet-class ROIC.
- Energy Transfer, Matador, and Plains remain below project, reserve-backed, or route-level return proof.

## Decision

`cfnsaq-005-executed-current-local-mixed-partial-hold`

The five-row next-source acquisition queue has now been executed against the current local source set. The result is a bounded proof map, not full investment-return proof.

## Safe Claim

`The current local source set supports partial return proxies for Wheaton Antamina, FPL Distribution Inspection, and United Rentals fleet. Energy Transfer, Matador, and Plains remain return-model holds. No CFNSAQ-005 row proves full IRR, NPV, ROIC, reserve-life sufficiency, earned shareholder return, or financed asset-level cash return.`

## Next Work

1. Build a consolidated next-source execution synthesis across `CFNSAQ-001` through `CFNSAQ-005`.
2. Use that synthesis to answer the user-facing question in one table: who invests, through what instrument, into what, what cash comes back, and what remains unproven.
