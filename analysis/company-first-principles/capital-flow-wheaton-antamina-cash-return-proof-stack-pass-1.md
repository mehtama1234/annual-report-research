# Capital Flow Wheaton Antamina Cash-Return Proof Stack Pass 1

## Purpose

This page executes end-to-end graph upgrade queue row `CFE2EGUQ-001`.

It asks:

`Can Wheaton Antamina be upgraded from named source/use/cash-return proxy to full asset-level return proof?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-wheaton-antamina-cash-return-proof-stack-pass-1.csv`

The upstream graph queue is:

`/cluster/capital-flow-end-to-end-graph-upgrade-queue-pass-1.md`

The upstream Antamina economics pages are:

`/cluster/capital-flow-wheaton-antamina-pmpa-economics-pass-1.md`

`/cluster/capital-flow-wheaton-antamina-net-cash-return-pass-1.md`

## Current Answer

`No full return proof yet, but the proof stack is now explicit. Wheaton Antamina passes the named use, financing-context, acquired-interest, production-entitlement, delivery-cost-formula, duration-language, stream-revenue, stream-cash-cost, depletion, stream-cash/profit, asset-denominator, and return-proxy gates. It holds on Antamina-specific tax, interest, debt-service, lender allocation, delivered-ounce schedule, reserve-life sufficiency, IRR, and NPV. The correct current grade remains named-source-use-cash-return-proxy-visible.`

## Gate Read

| Gate | Status | Evidence | Boundary |
|---|---|---|---|
| Named cash use | `source-proven` | `4.300B USD` Antamina PMPA cash payment. | Expected return and exact funding allocation remain open. |
| Financing context | `source-proven-company-level` | `2.700B USD` bank debt drawn, `728M USD` repaid, `1.500B USD` term loan, `1.972B USD` gross bank debt. | Lender-level allocation and repayment waterfall remain open. |
| Acquired interest | `source-proven` | BHP's `33.750%` portion of Antamina silver production. | Delivery timing and total realized ounces remain open. |
| Production entitlement | `source-proven-contract-term` | `67.500%` attributable payable production. | Realized payable production remains open. |
| Delivery cash-cost formula | `source-proven-contract-term` | `20.000%` of price received on delivery. | Delivered ounces, realized price, tax, and financing allocation remain open. |
| Duration language | `source-proven-contract-term` | Life-of-mine agreement term. | Reserve life and delivery curve remain open. |
| Stream revenue | `source-proven-stream-level` | H1 `2026` Antamina revenue of `277.563M USD`. | Delivery and realized-price bridge remain open. |
| Stream cash cost | `source-proven-stream-level` | H1 `2026` cost excluding depletion of `55.340M USD`. | Per-ounce reconciliation remains open. |
| Depletion | `source-proven-stream-level` | H1 `2026` depletion of `51.322M USD`. | Reserve base and depletion methodology remain open. |
| Stream cash/profit | `source-proven-stream-level` | H1 `2026` profit of `170.901M USD` and OCF of `222.223M USD`. | Tax, interest, debt service, and future periods remain open. |
| Asset denominator | `source-proven-stream-level` | Antamina asset carrying amount of `4.708329B USD`. | Fair value and reserve valuation remain open. |
| Tax and interest | `company-level-context-only` | Company finance costs of `32.502M USD` and tax expense of `210.876M USD`. | Antamina-specific allocation remains open. |
| Debt principal scale | `derived-proxy-only` | Term loan equals `34.884%` of PMPA payment; gross bank debt equals `45.860%`; annualized Antamina OCF equals `29.630%` of term-loan principal. | Debt-service coverage is not proven. |
| Return proxy | `derived-proxy-only` | H1 OCF/upfront payment `5.168%`; annualized OCF/upfront payment `10.336%`; simple payback proxy `9.675` years. | IRR, NPV, tax, financing, reserve life, and delivery curve remain open. |

## Decision

`named-source-use-cash-return-proxy-visible-full-return-unproven`

This is the strongest end-to-end row in the graph right now because it has:

- named capital source context
- named use of funds
- named asset/stream
- contract output entitlement
- delivery cost formula
- stream-level revenue
- stream-level cash cost
- stream-level depletion
- stream-level profit and operating cash flow
- asset denominator
- bounded return proxies

It still does not have:

- delivered ounces
- realized price bridge
- Antamina-specific tax
- Antamina-specific interest
- cash debt-service waterfall
- lender allocation
- reserve-life sufficiency
- IRR or NPV

## Safe Claim

`Wheaton Antamina is the current strongest end-to-end cash-return proxy in the graph. The local Q2 2026 evidence ties a 4.300B USD Antamina PMPA payment to company-level financing context, a 33.750% BHP silver-production interest, a 67.500% attributable-payable-production term, a 20.000% delivery cash-cost formula, H1 2026 Antamina revenue of 277.563M USD, cost excluding depletion of 55.340M USD, depletion of 51.322M USD, profit of 170.901M USD, operating cash flow of 222.223M USD, and a 10.336% mechanical annualized OCF/upfront-payment proxy. This is not full PMPA return, IRR, NPV, after-tax return, debt-service coverage, or lender-allocation proof.`

## Next Work

1. Locate Antamina delivered-ounce and realized-price detail.
2. Pull reserve-life and mine-plan support from Wheaton, BHP, Teck, Glencore, or Antamina technical materials.
3. Build an Antamina-specific tax allocation only if source support exists.
4. Build a debt-service waterfall only after term-loan/revolver repayment and interest schedules are source-visible.
5. Build IRR/NPV only after delivery curve, reserve life, tax, financing, and price assumptions are evidence-backed.
