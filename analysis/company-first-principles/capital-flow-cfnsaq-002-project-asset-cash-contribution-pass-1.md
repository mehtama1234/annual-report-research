# Capital Flow CFNSAQ-002 Project/Asset Cash Contribution Pass 1

## Purpose

This page executes the second row of the next-source acquisition queue.

It asks:

`Can current local sources tie company cash proxies to a named project, asset, route, train, reserve area, or backlog cohort?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-cfnsaq-002-project-asset-cash-contribution-pass-1.csv`

The queue input is:

`/cluster/capital-flow-next-source-acquisition-queue-pass-1.md`

## Short Answer

`CFNSAQ-002 is executed against the current local source set. It finds one partial contribution proxy, PBF refinery cash context, and five holds. Cheniere, Energy Transfer, Matador, MasTec, and Plains all have useful company, output, backlog, route, capacity, or collateral proxies, but none ties cash contribution to the named asset/project/route/train/cohort at proof grade.`

## Execution Result

| Row | Target Case | Current Evidence | Result | What Still Blocks Proof |
|---|---|---|---|---|
| `CFNSAQ002-001` | Cheniere LNG | FY `2025` revenue of `19.98B USD`, DCF of `5.29B USD`, `670` company cargoes; Q2 `2026` revenue of `5.73B USD`, adjusted EBITDA of `1.80B USD`, DCF of `1.17B USD`, and DOE-aligned cargo evidence | `hold-no-train-entity-cash-contribution` | Train/entity EBITDA, distribution, debt-service coverage, restricted-payment waterfall, contract revenue attribution |
| `CFNSAQ002-002` | Energy Transfer projects | Q2 `2026` adjusted EBITDA of `5.07B USD`, DCF of `2.59B USD`, growth capex of `1.10B USD`, maintenance capex of `307M USD`, and named capacity/output context | `hold-no-named-project-cash-contribution` | Project revenue, project EBITDA, DCF contribution, utilization, tariff/fee economics, debt-service allocation |
| `CFNSAQ002-003` | Matador borrowing base | Q2 `2026` borrowings of `939.000M USD`, letters of credit of `53.800M USD`, borrowing base of `3.250B USD`, elected commitments of `2.750B USD`, and aggregate operating/development context | `hold-no-asset-area-cash-contribution` | Asset-area production/cash margin, well-level contribution, acquisition contribution, reserve-supported cash return |
| `CFNSAQ002-004` | PBF refinancing | Q2 `2026` cash of `894.100M USD`, PP&E net of `5.741800B USD`, debt of `1.749100B USD`, `492.100M USD` of 2034 note net proceeds, and `801.600M USD` of 2028 notes redeemed | `partial-refinery-cash-proxy` | Refinery-level contribution, outage-normalized cash, ABL support, borrowing-base certificate, refinancing NPV |
| `CFNSAQ002-005` | MasTec backlog | Q2 `2026` backlog of `21.4B USD`, CE&I backlog of `7.8B USD`, Power Delivery backlog of `6.3B USD`, Q2 revenue of `4.374B USD`, adjusted EBITDA of `384.2M USD`, and H1 operating cash flow of `120.322M USD` | `hold-no-project-or-cohort-cash-contribution` | Segment/project cash contribution, project margin, retainage collection, backlog-cohort cash conversion |
| `CFNSAQ002-006` | Plains tariff route | Effective `2026-07-01` tariff route from Karnes County to Cactus III/Hobson, `178.98` cents per barrel base rate, negotiated-rate mechanic, and Cactus III capacity over `600000` barrels per day | `hold-no-route-cash-contribution` | Route revenue, route throughput, realized billing, Cactus III EBITDA, operating cash, maintenance capital |

## What This Answers

This pass separates company-level cash visibility from asset-level contribution proof:

- Cheniere has strong LNG output and company cash, but not train/entity contribution.
- Energy Transfer has company cash, capex, and project context, but not named-project contribution.
- Matador has borrowing-base and aggregate operating context, but not asset-area contribution.
- PBF has the strongest partial contribution proxy because refinancing, liquidity, refining assets, and operating cash context are visible together.
- MasTec has backlog/revenue/cash proxies, but not project or backlog-cohort cash contribution.
- Plains has tariff route/rate/capacity evidence, but not route revenue or cash contribution.

## Decision

`cfnsaq-002-executed-current-local-hold`

The queue row is executed against current local evidence. It does not close project/asset cash contribution proof. The next source package should move to debt-service, lender allocation, source-to-use ledgers, and transaction close support unless new project/asset contribution schedules can be acquired.

## Safe Claim

`The current local source set does not prove named project, asset, route, train, reserve-area, or backlog-cohort cash contribution for the CFNSAQ-002 target set. PBF reaches partial refinery cash proxy status; the other five rows remain holds with useful but aggregate evidence.`

## Next Work

1. Move to `CFNSAQ-003` for debt-service, lender allocation, source-to-use ledgers, and transaction close support.
2. Preserve the project/asset contribution hold unless a named contribution schedule, route revenue schedule, train/entity cash waterfall, or backlog-cohort margin/collection bridge is acquired.
