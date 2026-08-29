# Capital Flow URI Fleet Cash-Yield Source Target Pass 1

## Purpose

This pass executes `CFE2EGUQ-006`:

`Can United Rentals' fleet capital, owned-rental output, margin proxies, equipment-sale proceeds, cash conversion, and collateral support be upgraded into fleet-class cash-yield proof?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-uri-fleet-cash-yield-source-target-pass-1.csv`

The upstream queue is:

`/cluster/capital-flow-end-to-end-graph-upgrade-queue-pass-1.md`

## Short Answer

Not fully.

United Rentals has the strongest current operating-conversion evidence in the queue, but it still stops at fleet cash-yield proxy status.

The strongest current money-movement answer is:

`Capital goes into URI's rental fleet through cash fleet purchases and gross rental capex. The fleet produces owned-equipment rental revenue, rental revenue/OEC productivity, segment gross-margin evidence, used-equipment sale proceeds, company operating cash coverage, and collateralized funding support. The evidence still does not prove cash yield by fleet class because growth/replacement capex, fleet-class OEC, true utilization, segment operating profit, borrowing-base availability, reserves, advance rates, source-to-purchase allocation, and ROIC remain missing.`

## Money Movement Answer

| Link | Current Answer | Status |
|---|---|---|
| Source of money | Company operating cash flow, debt stack, ABL availability, AR securitization support, and equipment-sale proceeds are visible in the broader URI evidence set. | company funding/cash proxy visible |
| Use of money | H1 `2026` payments for rental equipment were `2.720B USD`; gross rental capex was `2.931B USD`; net cash rental-equipment investment after sale proceeds was `2.040B USD`. | fleet cash use visible |
| Into what | Q2 `2026` OEC was `23.8B USD`, giving a public fleet-cost denominator. | fleet denominator visible |
| Output | Q2 owned-equipment rentals were `2.991B USD`; H1 owned-equipment rentals were `78.1%` of equipment-rentals revenue. | owned-fleet output visible |
| Cash/recycling | H1 rental-equipment sale proceeds were `680M USD`; H1 OCF covered `112.8%` of gross rental capex and `162.0%` of net fleet cash investment. | company cash coverage visible |
| Margin/return proxy | Specialty H1 equipment-rentals gross margin was `43.1%` versus `34.8%` for General Rentals; Specialty annualized gross profit / average segment assets was `26.4%` versus `14.7%` for General Rentals. | return-quality proxy visible |
| Funding wrapper | AR collateral-pool coverage was `125.8%` of AR securitization borrowings. | collateral support visible |
| Missing proof | Growth versus replacement capex, fleet-class OEC, true utilization, rate/time/mix split, segment operating profit, legal borrowing-base availability, reserves, advance rates, and purchase-level source allocation. | hold |

## Evidence Stack

| Gate | Evidence | Result |
|---|---|---|
| Fleet denominator | Q2 `2026` OEC of `23.8B USD`. | Gives a denominator for fleet output proxies. |
| Fleet cash use | H1 `2026` rental-equipment purchase payments of `2.720B USD` and gross rental capex of `2.931B USD`. | Shows cash moving into rental equipment. |
| Fleet recycling | H1 `2026` rental-equipment sale proceeds of `680M USD`. | Shows cash coming back through equipment disposals. |
| Owned-rental output | Q2 `2026` owned-equipment rentals of `2.991B USD` and H1 owned-rental share of `78.1%`. | Shows most equipment-rental output comes from owned assets. |
| Productivity | Q2 rental revenue/OEC of `16.2%` and adjusted EBITDA/OEC of `8.6%`. | Supports output and company-profit proxy, not ROIC. |
| Segment economics | H1 Specialty gross margin of `43.1%` versus General Rentals at `34.8%`. | Shows segment margin difference, not fleet-class return. |
| Segment asset proxy | H1 Specialty annualized equipment-rentals gross profit / average segment assets of `26.4%` versus General Rentals at `14.7%`. | Supports bounded segment asset-productivity proxy. |
| Cash coverage | H1 OCF/gross rental capex of `112.8%` and OCF/net fleet cash investment of `162.0%`. | Shows same-period company cash coverage. |
| Collateral support | AR collateral-pool coverage of `125.8%` of AR securitization borrowings. | Supports funding-wrapper durability, not legal borrowing-base availability. |

## Decision

`CFE2EGUQ-006` should move from `partial-local` to:

`executed-local-boundary-pass-1`

Pass result:

`United Rentals reaches strong fleet cash-yield proxy status with OEC, rental-equipment purchase cash, gross rental capex, equipment-sale proceeds, owned-rental output, revenue/OEC productivity, segment margin, segment asset-productivity proxy, company cash coverage, and collateral support.`

Hold result:

`Full fleet-class cash yield remains unproven because the local evidence does not expose growth-versus-replacement capex, fleet-class OEC, fleet-class utilization, segment operating profit, legal borrowing-base availability, reserves, advance rates, source-to-purchase allocation, or ROIC.`

## Safe Claim

`United Rentals has strong evidence that capital is moving into rental fleet and that the fleet model is producing owned-rental output, equipment-sale recycling, company cash coverage, segment-margin proxies, and collateral support. It should not be described as fleet-class cash-yield or ROIC proof until fleet-class OEC, utilization, growth/replacement capex, segment operating profit, legal borrowing-base availability, and source-to-purchase allocation are visible.`

