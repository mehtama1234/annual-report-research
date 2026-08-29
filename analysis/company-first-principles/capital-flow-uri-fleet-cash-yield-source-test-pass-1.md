# Capital Flow URI Fleet Cash-Yield Source Test Pass 1

This page executes cash-return source work-order row `CFCRSWO-004`.

The question is:

`Can United Rentals move from company-level fleet cash-yield proxy evidence to fleet-class cash-yield or ROIC proof using the current local source set?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-uri-fleet-cash-yield-source-test-pass-1.csv`

The upstream work order is:

`/cluster/capital-flow-cash-return-source-work-order-pass-1.md`

## Short Answer

`No full upgrade yet. URI has the cleanest operating-company fleet conversion bridge, but current local evidence still does not prove fleet-class cash yield or ROIC.`

The local evidence does answer the user's money-movement question at company/fleet proxy level. Capital moves into rental equipment through direct cash purchases and gross rental capex. The fleet produces owned-equipment rental revenue and rental revenue/OEC productivity. Used-equipment sales recycle cash from the asset base. Company operating cash flow covers fleet investment at the same-period proxy level. Segment gross margin and segment asset-productivity proxies separate Specialty from General Rentals. Receivables collateral supports part of the funding wrapper.

The strongest visible data points are Q2 `2026` OEC of `23.8B USD`, H1 `2026` rental-equipment purchase payments of `2.720B USD`, H1 `2026` gross rental capex of `2.931B USD`, H1 `2026` rental-equipment sale proceeds of `680M USD`, H1 `2026` net fleet cash investment of `2.040B USD`, Q2 `2026` owned-equipment rentals of `2.991B USD`, H1 `2026` owned-rental share of `78.1%`, Q2 `2026` rental revenue/OEC of `16.2%`, Q2 `2026` adjusted EBITDA/OEC of `8.6%`, H1 `2026` Specialty equipment-rentals gross margin of `43.1%` versus General Rentals at `34.8%`, H1 `2026` Specialty annualized equipment-rentals gross profit / average segment assets of `26.4%` versus General Rentals at `14.7%`, H1 `2026` OCF/gross rental capex of `112.8%`, H1 `2026` OCF/net fleet cash investment of `162.0%`, and AR collateral-pool coverage of `125.8%`.

That is still not fleet-class return proof. The current local source set lacks growth-versus-replacement capex, fleet-class OEC, true utilization, rate/time/mix decomposition, segment operating profit, legal borrowing-base availability, reserves, advance rates, source-to-purchase allocation, and ROIC.

## Source-Test Result

| Gate | Result | Meaning |
|---|---|---|
| Fleet denominator | Pass | Q2 `2026` OEC gives a large public fleet-cost denominator. |
| Cash use | Pass | H1 rental-equipment purchases and gross rental capex show cash moving into fleet. |
| Cash recycling | Pass | H1 rental-equipment sale proceeds show cash returned through fleet disposal. |
| Owned-rental output | Pass | Most equipment-rental revenue is tied to owned assets rather than re-rent. |
| Revenue productivity | Pass with boundary | Rental revenue/OEC supports an output proxy, not utilization or ROIC. |
| Profitability proxy | Pass with boundary | Adjusted EBITDA/OEC supports company-level profit proxy, not fleet operating return. |
| Segment margin | Pass with boundary | Specialty and General Rentals gross margins are visible, but not operating profit. |
| Segment asset proxy | Pass with boundary | Segment gross-profit productivity is visible, but segment assets are not fleet-class OEC. |
| Cash coverage | Pass with boundary | Company OCF covers gross and net fleet investment, but source-to-purchase allocation is not proven. |
| Collateral support | Pass with boundary | AR collateral coverage is visible, but legal borrowing-base availability is missing. |
| Fleet-class return | Hold | Current local evidence does not disclose fleet-class OEC, utilization, capex split, or ROIC. |

## Decision

`fleet-cash-yield-source-test-hold-with-strong-company-fleet-proxy`

The work-order row `CFCRSWO-004` is executed from local evidence. The result is not a full promotion. URI remains the cleanest operating-company conversion test because fleet capital, owned-rental output, equipment-sale recycling, cash coverage, segment-margin proxies, and collateral support are all visible. It does not reach fleet-class cash-yield or ROIC proof.

## Safe Claim

`United Rentals has strong company/fleet proxy evidence that capital moves into rental equipment and returns through owned-rental revenue, used-equipment sale proceeds, company operating cash coverage, segment-margin proxies, and collateral support. Current local evidence still does not prove fleet-class cash yield or ROIC because growth/replacement capex, fleet-class OEC, true utilization, rate/time/mix, segment operating profit, legal borrowing-base availability, reserves, advance rates, and source-to-purchase allocation are missing.`

## Next Source Package

1. Fleet-class OEC and average OEC schedules.
2. Growth versus replacement capex bridge.
3. Fleet-class utilization, rate, time, and mix decomposition.
4. Segment operating profit or EBITDA by owned-rental fleet class.
5. Borrowing-base certificates, reserves, advance rates, and legal availability.
6. Source-to-purchase allocation between OCF, ABL, notes, securitization, and sale proceeds.
7. ROIC or life-cycle cash-yield support by fleet category.
