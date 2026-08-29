# Capital Flow BHP Antamina Streaming Proceeds Use Boundary Pass 1

## Purpose

This pass checks the recipient side of the Wheaton/BHP Antamina stream:

`Wheaton cash payment -> BHP receipt -> BHP liability/cash-flow classification -> BHP use-of-proceeds boundary.`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-bhp-antamina-streaming-proceeds-use-boundary-pass-1.csv`

The upstream Wheaton bridge is:

`/cluster/capital-flow-wheaton-antamina-cumulative-received-sold-cashflow-pass-1.md`

## Question

`Can the Antamina money path be extended from Wheaton's 4.300B USD payment to BHP's receipt and named use of proceeds?`

## Short Answer

`Partly. BHP's 2026 Annual Report confirms BHP received 4.300B USD from Wheaton on April 2, 2026, classifies the stream as an other financial liability under IFRS 9, reports 4.300B USD of proceeds from streaming arrangement liability in financing cash flows, and reports 41M USD of settlements of the streaming arrangement liability. It also states the stream is settled through metal credits, has no minimum or fixed delivery requirements, and depends on Antamina production-volume and silver-price assumptions. This proves BHP-side cash receipt and accounting/cash-flow classification. It does not prove BHP's named use of proceeds, debt repayment trace, capex allocation, dividend/buyback allocation, Antamina reinvestment, or delivery-settlement cash all the way through.`

## BHP-Side Bridge

| Gate | Current Evidence | Status | Boundary |
|---|---:|---|---|
| BHP receipt | Annual Report note 24 says BHP received `4.300B USD` on April 2, 2026. | `bhp-cash-receipt-visible` | Receipt is not use-of-proceeds allocation. |
| Liability accounting | The stream is an other financial liability at amortised cost under IFRS 9. | `liability-accounting-visible` | Accounting classification is not cash waterfall proof. |
| Financing source line | Cash-flow statement shows `4.300B USD` proceeds from streaming arrangement liability. | `financing-source-line-visible` | Source line does not identify destination use. |
| Settlement line | Cash-flow statement shows `41M USD` settlements of streaming arrangement liability. | `settlement-line-visible` | Does not identify ounces delivered or settlement math. |
| Delivery obligation | BHP delivers `33.75%` of Antamina silver at `90%` payable rate until `100M` ounces, then `22.5%`. | `delivery-obligation-visible` | Obligation terms are not actual delivery ledger. |
| Delivery flexibility | No minimum or fixed delivery requirements. | `delivery-flexibility-visible` | Delivery timing remains production-linked. |
| Valuation inputs | Liability valuation uses Antamina production volumes and silver prices. | `valuation-inputs-visible` | Full model, discount rate, and delivery curve are not disclosed. |
| Reserve boundary | Production estimates use development plans and risked reserves/resources that do not currently meet proved criteria. | `reserve-boundary-visible` | Does not prove reserve-backed delivery sufficiency. |
| Group capital context | BHP reports `9.8B USD` free cash flow, `10.3B USD` capex/exploration, and `8.7B USD` dividends. | `group-capital-allocation-context-visible` | Context is not allocation of Antamina proceeds. |
| Source/use verdict | BHP receipt is visible; named use remains a hold. | `bhp-receipt-visible-use-allocation-hold` | Cash-all-the-way-through remains unproven. |

## What Improved

The money path now extends one step further:

`Wheaton paid 4.300B USD -> BHP received 4.300B USD -> BHP recorded financing cash inflow and streaming liability`

That is stronger than only proving Wheaton's use of cash.

## What Still Blocks Full Proof

The public BHP source still does not answer:

1. whether the `4.300B USD` repaid debt
2. whether it funded dividends or buybacks
3. whether it funded capex or copper growth projects
4. whether it stayed in cash/liquidity
5. whether it was allocated to Antamina reinvestment
6. how the `41M USD` settlement line reconciles to metal credits delivered
7. how production forecasts, reserves, silver prices, and discount rate determine the liability
8. whether the transaction is value-accretive after delivery obligations and retained base-metals exposure

## Decision

`bhp-antamina-streaming-proceeds-receipt-visible-use-allocation-hold`

BHP-side receipt and accounting classification are visible. BHP-side named use of proceeds is not.

## Safe Claim

`The Wheaton/BHP Antamina stream now has recipient-side cash receipt evidence. BHP's 2026 Annual Report says BHP received 4.300B USD from Wheaton on April 2, 2026, records 4.300B USD as proceeds from streaming arrangement liability, classifies the stream as an IFRS 9 other financial liability at amortised cost, and reports 41M USD of streaming-liability settlements. The source still does not prove BHP's named use of proceeds, debt repayment trace, capex allocation, dividend or buyback allocation, Antamina reinvestment, delivery settlement ledger, IRR, NPV, or full cash-all-the-way-through.`

## Next Source Package

1. BHP treasury cash source/use schedule after April 2, 2026.
2. Debt repayment trace or liquidity bridge tied to stream proceeds.
3. Board/capital allocation material identifying use of Antamina proceeds.
4. Streaming liability rollforward and settlement schedule.
5. Metal-credit delivery ledger and 20% spot-price settlement support.
6. Antamina production forecast, reserve/resource model, discount rate, and liability valuation model.
