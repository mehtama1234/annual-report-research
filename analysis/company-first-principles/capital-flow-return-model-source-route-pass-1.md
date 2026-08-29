# Capital Flow Return Model Source Route Pass 1

## Purpose

This page executes repeated missing-source work-order row `CFRMSWO-012`.

It asks:

`Can current local evidence prove IRR, NPV, ROIC, reserve-life sufficiency, earned-return support, or project-return economics for the affected cash-return cases?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-return-model-source-route-pass-1.csv`

The upstream work order is:

`/cluster/capital-flow-repeated-missing-source-work-order-pass-1.md`

## Short Answer

`No full return-model upgrade yet. Wheaton Antamina, FPL Distribution Inspection, and United Rentals have bounded return proxies: Antamina has pre-tax/pre-interest cash and profit yield proxies; FPL has regulatory cost-rate, equity/debt/depreciation component, and per-project recovery math; URI has segment asset-return and fleet cash-yield proxies. Energy Transfer, Matador, and Plains remain holds because the current local evidence lacks named-project IRR, NPV, ROIC, reserve-life, project contribution, or asset-return models.`

## Row Outcomes

| Row | Case | Current Return Evidence | Return Result | Remaining Gap |
|---|---|---|---|---|
| `CFRMSR-001` | Wheaton Antamina | `4.300B USD` PMPA upfront payment; H1 `2026` Antamina revenue of `277.563M USD`; operating cash flow of `222.223M USD`; profit after depletion of `170.901M USD`; asset carrying amount of `4.708329B USD`; `10.336%` mechanical annualized OCF/upfront-payment proxy; `7.949%` mechanical annualized profit/upfront-payment proxy | Partial named asset return proxy | No delivered-ounce schedule, cash-receipt detail, tax allocation, interest allocation, debt-service waterfall, lender allocation, reserve-life support, IRR, NPV, or full PMPA valuation model |
| `CFRMSR-002` | FPL Distribution Inspection | `193199` actual projects; `61.500000M USD` actual capital cost; `15.942971M USD` final category recovery; equity component of `10.481240M USD`; debt component of `2.278910M USD`; depreciation of `3.182821M USD`; `7.0330%` weighted cost; `8.8822%` pre-tax total; per-project recovery/component math | Partial regulated earned-return component proxy | No category customer receipts, billing determinants, financing source allocation, actual earned ROE, shareholder cash return, project IRR, or asset-level return model |
| `CFRMSR-003` | United Rentals fleet | Q2 `2026` OEC of `23.8B USD`; rental revenue/OEC of `16.2%`; adjusted EBITDA/OEC of `8.6%`; H1 `2026` OCF/gross rental capex of `112.8%`; OCF/net fleet cash investment of `162.0%`; Specialty annualized equipment-rentals gross profit / average segment assets of `26.4%` versus General Rentals at `14.7%` | Partial fleet and segment return proxy | No fleet-class OEC, true utilization, growth/replacement capex, segment operating profit, asset-level ROIC, borrowing-base availability, source-to-purchase allocation, or lifecycle fleet return model |
| `CFRMSR-004` | Energy Transfer projects | Q2 `2026` adjusted EBITDA of `5.07B USD`; DCF of `2.59B USD`; growth capex of `1.10B USD`; FY `2026` growth-capex guidance of `5.6B-5.9B USD`; named Nederland, Lone Star, and y-grade capacity/demand clues; volume-growth evidence | Hold with company project-return context | No named project cost, source-to-project allocation, utilization, project revenue, project EBITDA/DCF, debt-service allocation, tariff/shipper billing, IRR, NPV, or project-return model |
| `CFRMSR-005` | Matador borrowing base | H1 `2026` source/use reconciliation; `745.343M USD` development capex; `1.228834B USD` oil-and-gas property acquisitions; named `1.160B USD` BLM Acquisition; Q2 production and revenue; borrowing-base and debt-cost context | Hold with aggregate source/use and output context | No reserve report, reserve-life sufficiency, asset-area production/cash margin, LOE, BLM contribution, source-specific asset cash, well-level economics, IRR, NPV, or reserve-backed return model |
| `CFRMSR-006` | Plains tariff route | Texas RRC tariff `TX 3.6.0`; `178.98` cents per barrel route rate; Cactus III capacity above `600000 bpd`; acquisition/control and assumed-debt context | Hold with tariff and acquisition denominator context | No committed volume, billed barrels, utilization, realized route revenue, Cactus III EBITDA/cash contribution, acquisition return, debt-service allocation, IRR, NPV, or route/asset return model |

## Decision

`return-model-source-route-hold-with-partials`

`CFRMSWO-012` is executed against the current local source set. It produces three partial return-proxy rows and three holds:

- Wheaton Antamina: partial named asset return proxy.
- FPL Distribution Inspection: partial regulated earned-return component proxy.
- United Rentals: partial fleet and segment return proxy.
- Energy Transfer: hold below named-project return model.
- Matador: hold below reserve-backed asset return model.
- Plains: hold below route/asset return model.

## Work-Order Completion

This completes the first `12` repeated missing-source work-order rows. The system now has executed source-route passes for:

- customer receipts and billing support
- source-to-use allocation
- project or asset cash contribution
- debt-service waterfalls
- borrower facility documents
- statutory investment schedules
- contract pricing and obligations
- physical output attribution
- collateral availability certificates
- working-capital collection
- transaction funds-flow
- return-model support

## Safe Claim

`The return-model source-route pass confirms that several rows have bounded return proxies, but the current local evidence does not prove full IRR, NPV, ROIC, reserve-life sufficiency, earned shareholder return, project contribution, debt-service-adjusted return, or asset-level investment return across the affected rows. The completed 12-row work order is a proof-gap execution map, not a completed cash-return thesis.`

## Next Work

1. Build a consolidated repeated-source execution status summary across `CFRMSWO-001` through `CFRMSWO-012`.
2. Rank the strongest upgrade candidates by next-source leverage: Wheaton Antamina delivery/reserve/DCF model, FPL category receipts/funding allocation, URI fleet-class ROIC/utilization, Energy Transfer project contribution, Matador reserve-backed asset cash, and Plains route revenue.
3. Convert the completed work order into a source-acquisition queue that separates local extraction from external primary-source search.
4. Keep the all-16 graph bounded until same-period source/use/output/cash/payback/return evidence is joined at row level.
