# Capital Flow Plains Tariff Volume Cash Pass 1

This page executes end-to-end graph upgrade queue row `CFE2EGUQ-016`.

The question is:

`Can Plains Cactus III tariff-route evidence be upgraded to committed volume, billing, realized revenue, and segment cash proof?`

The evidence table is:

`analysis/company-first-principles/data/capital-flow-plains-tariff-volume-cash-pass-1.csv`

## Short Answer

`Plains has tariff route/rate commercial evidence for a specific movement path, but committed-volume, billing, realized-revenue, and segment-cash proof remain missing.`

The local evidence answers the money-movement question through commercial route/rate mechanics. A Texas RRC tariff identifies Plains Eagle Ford Energy LLC tariff `TX 3.6.0`, effective `2026-07-01`, for the Karnes County to Cactus III Crude Pipeline Hobson Terminal route. The base tariff rate is `178.98` cents per barrel. The tariff also contains negotiated-rate and FERC-index escalation mechanics.

The same Plains commercial-durability pass ties the route to Cactus III acquisition/control evidence: Cactus III capacity above `600,000` barrels per day, a `55%` EPIC/Cactus III interest bought for about `1.568B USD` inclusive of `613M USD` debt assumed, the remaining `45%` bought from an Ares portfolio company for about `1.327B USD` inclusive of `501M USD` debt assumed, `2.016B USD` purchase-accounting consideration, `2.737B USD` of property and equipment acquired, and Plains operator-of-record status.

That is enough to show a real asset route and tariff economics. It is not enough to show who shipped barrels, how many barrels were committed or billed, what revenue Plains realized from the route, or what segment cash/EBITDA came back from the asset.

## Money Movement

| Question | Current Answer | Boundary |
|---|---:|---|
| Tariff authority | Texas RRC tariff `TX 3.6.0` | Regulator-hosted route/rate evidence, not billing evidence. |
| Effective date | `2026-07-01` | Current tariff date, not volume shipped. |
| Origin | Karnes County | Physical starting point visible. |
| Destination | Cactus III Crude Pipeline Hobson Terminal | Movement path visible. |
| Base rate | `178.98` cents per barrel | Published tariff, not realized average rate. |
| Term agreement mechanic | Negotiated rates may be available for term shippers | Contract mechanic visible, not executed shipper proof. |
| Escalation mechanic | Annual July 1 FERC-index escalation language | Rate durability mechanic, not cash-return proof. |
| Asset capacity | More than `600,000` barrels per day | Output denominator visible, not utilization. |
| Acquisition stack | `55%` and `45%` stake transactions with assumed debt | Ownership/control bridge, not project financing trace. |
| Operator control | Plains owns `100%` and is operator of record | Asset control visible, not return proof. |

## Queue Result

`executed-local-boundary-pass-1`

The row can be upgraded from route-visible-not-local to executed-local boundary status because local evidence now ties Plains to an official tariff route/rate and SEC-filed Cactus III acquisition/control facts. It does not pass the full target because committed-volume, billing, realized-revenue, contract-duration, and segment-cash evidence remain incomplete.

With this row, all `16` seeded end-to-end graph upgrade rows now have local boundary artifacts. That does not mean the system has asset-level cash-return proof across all rows; it means every seeded flow now has a money-movement answer and a missing-proof boundary.

## What This Proves

The current Plains answer is:

`tariff authority -> Plains Eagle Ford Energy route -> Karnes County origin -> Cactus III/Hobson destination -> 178.98 cents-per-barrel base-rate economics -> possible shipper billing path`

That is not the same as:

`named shipper contract -> committed barrels -> actual billed volume -> realized route revenue -> segment cash contribution -> asset return`

## Missing Proof

| Missing proof | Why it matters | Next source |
|---|---|---|
| Shipper identity | Needed to know who pays Plains for the movement. | Executed transportation agreements, public customer filings, open-season result, or contract summary. |
| Committed volume | Needed to distinguish durable contracted cash from spot tariff availability. | Committed-volume schedule, MVC disclosure, shipper contract, or open-season award. |
| Billing volume | Needed to know how much throughput moved under the tariff. | Tariff billing records, throughput by route, RRC/FERC volume support, or customer statements. |
| Realized revenue | Needed to connect tariff economics to cash collected. | Route revenue, realized average rate, invoice data, or segment revenue bridge. |
| Contract duration | Needed to test commercial durability. | Term agreement, renewal clause, maturity table, or tariff-rate contract exhibit. |
| Segment cash contribution | Needed to test return on the asset base. | Cactus III EBITDA, operating cash flow, maintenance capital, debt-service, and project contribution schedules. |

## Safe Claim

`Plains has tariff route/rate commercial evidence for a specific movement path: Texas RRC tariff TX 3.6.0, effective 2026-07-01, shows a Karnes County to Cactus III/Hobson route with a 178.98 cents-per-barrel base rate and negotiated-rate mechanics. Local SEC evidence also supports Cactus III acquisition/control context. The evidence supports tariff-route/rate and acquisition-stack money-movement language, not committed-volume, billing, realized-revenue, segment-cash, or asset-return proof.`

## Next Work

1. Find Cactus III committed shipper contracts or open-season result evidence.
2. Extract route-level throughput and billing volume if public.
3. Tie tariff rates to realized route revenue or segment revenue.
4. Extract Cactus III EBITDA/cash contribution and debt-service support.
5. Separate committed, negotiated, and uncommitted tariff economics.
