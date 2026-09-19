# UPS parcel-network and logistics valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves UPS from a freight-services packet into a company-specific valuation object. It separates parcel density, package mix, labor, aircraft and vehicle assets, automation, customer concentration, Amazon volume reduction, international and supply-chain services, transformation charges, capex, debt, and diluted common residual. It does not treat package volume, adjusted operating profit, guidance, operating cash flow, or buybacks as normalized owner cash.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| UPS | Physical parcel-network cash after pickup and delivery density, package mix, pricing, labor, aircraft and vehicle fleet, hubs, automation, tracking technology, customer concentration, transformation, capex, leases, debt, and dilution | Fleet and hub maintenance, automation, aircraft and vehicle replacement, labor and bargaining, network redesign, technology, working capital, leases, pensions, capex, SBC, and repurchases | E-commerce or B2B slowdown, Amazon glide-down execution, labor disruption, fuel and aircraft costs, network under-density, customer concentration, transformation cash, lease or debt refinancing, or dilution | Adjusted margins and guidance improve while package density, labor productivity, customer mix, GAAP transformation cash, required capex, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2025 revenue was about `$88.7B`, operating profit about `$7.9B`, adjusted operating profit about `$8.7B`, diluted EPS `$6.56`, and adjusted diluted EPS `$7.16`.
- UPS delivered about `5.2B` packages in 2025 and served about `1.6M` shipping customers; those volumes require density, labor, fleet, and network-cost reconciliation rather than simple revenue extrapolation.
- Q2 2026 revenue was about `$22.8B`, GAAP operating profit about `$930M`, adjusted operating profit about `$2.1B`, and adjusted diluted EPS `$1.76`; transformation charges make GAAP-to-adjusted cash persistence a live question.
- UPS raised 2026 revenue guidance to about `$91.2B` and adjusted operating profit guidance to about `$8.65B`, with capital expenditure guidance of about `$3.0B`.
- The Amazon glide-down and network reconfiguration are central return tests: lower-quality volume may improve mix, but lost density, severance, automation, and restructuring cash must remain visible.

## QoE and financial-shenanigans prompts

1. Reconcile packages, revenue per package, surcharge and fuel effects, service mix, residential/business density, and customer concentration against route and hub cost.
2. Keep labor reductions, bargaining, severance, transformation, network redesign, and automation spending in a cash-paid persistence test; “adjusted” does not make them nonrecurring.
3. Test Amazon volume reduction for both margin improvement and stranded network cost, including aircraft, vehicles, facilities, labor, and technology utilization.
4. Separate maintenance capex from growth and transformation capex, then include leases, pensions, working capital, and fleet replacement in the common-owner bridge.
5. Reconcile adjusted operating profit, GAAP operating profit, operating cash flow, dividends, repurchases, debt, and diluted shares before treating guidance as owner cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what revenue per package, density, labor productivity, mix, reinvestment rate, fleet life, and cost of capital the valuation requires. The Lyn Alden-style stress test asks whether the physical network can remain liquid through a volume shock, labor disruption, fuel or aircraft-cost spike, customer concentration reset, and transformation period without converting adjusted earnings into a misleading owner-cash claim.

## Promotion boundary

`ups-parcel-network-qualified; density-and-transformation-open; no-ranking`

Promotion requires same-entity joins from packages and customers to collections, route and hub utilization, labor settlement, fleet and hub capex, transformation cash, lease and pension obligations, debt, claims, and diluted common residual. Package volume, adjusted operating profit, guidance, operating cash flow, and buybacks remain diagnostic inputs.

## Sources

- [UPS company packet](../../extracted/services/air-delivery-freight-services/united-parcel-service-inc/company-packet.md)
- [UPS source ledger](../../extracted/services/air-delivery-freight-services/united-parcel-service-inc/source-ledger.md)

