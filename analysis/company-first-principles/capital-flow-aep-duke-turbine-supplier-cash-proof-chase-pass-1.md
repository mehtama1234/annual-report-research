# AEP/Duke turbine-supplier cash proof chase pass 1

Research date: `2026-09-18`

## Purpose

This chase tests whether AEP and Duke's secured-turbine disclosures reach supplier-side cash through vendor identity, order/contract terms, deposits, delivery, revenue recognition, margin, and collection. Secured capacity remains separate from approved plants and in-service generation.

## Required chain

`utility load need -> turbine reservation/order -> supplier contract/backlog -> deposit or payment term -> delivery and acceptance -> supplier revenue/margin -> collection -> utility plant approval and cash return`

## Gate register

| Gate | Required object | Current evidence | Status | Stop rule |
| --- | --- | --- | --- | --- |
| TURBINE-001 | AEP/Duke secured versus under-evaluation capacity | AEP `13 GW` secured and `10 GW` under evaluation; Duke `20` secured turbines | bucket-visible | Do not combine secured and under-evaluation capacity. |
| TURBINE-002 | Vendor identity and utility/project mapping | Company disclosures describe secured procurement but current bridge lacks full vendor/project crosswalk | hold-vendor | Do not infer supplier revenue or backlog from utility capacity. |
| TURBINE-003 | Order, reservation, EPC, or purchase agreement | Procurement narrative and project tables | hold-contract | Procurement intent is not a binding supplier cash claim without terms. |
| TURBINE-004 | Deposit, milestone, or payment terms | No supplier-side deposit or milestone ledger currently joined | hold-payment | Do not treat secured equipment as supplier cash or utility capex paid. |
| TURBINE-005 | Delivery, acceptance, and in-service timing | Delivery years and project timelines remain incomplete; Anderson target is summer 2027 construction and early 2031 service | hold-delivery | Do not treat reservation as delivered equipment or operating plant. |
| TURBINE-006 | Supplier revenue, margin, and collection | No named supplier-period revenue or receivable collection bridge | hold-supplier-cash | Do not promote supplier backlog, utility OCF, or turbine count into cash. |
| TURBINE-007 | Utility approval, recovery, and plant funding | AEP/Duke tariffs, dockets, and Anderson approval visible | approval-path-visible | Approval does not prove paid capex, rate-base transfer, or return. |
| TURBINE-008 | Cross-entity owner residual | No supplier/utility project waterfall closes | hold-owner-cash | Keep turbine lane diagnostic and unranked. |

## Current conclusion

`aep-duke-turbine-procurement-hold-capacity-visible`

The current evidence proves physical procurement intent and regulatory pathways, not supplier-side deposits, delivery cash, or utility project return.

## Sources

- [AEP/Duke load reconciliation workbench](capital-flow-aep-duke-load-reconciliation-workbench.md)
- [AEP/Duke approved-recovery bridge](capital-flow-aep-duke-approved-recovery-bridge-pass-1.md)
- [Duke Anderson approval-to-cash boundary](capital-flow-duke-anderson-county-generation-approval-recovery-boundary-2026-09-16.md)
- [Power-grid customer-cash work order](annual-report-power-grid-customer-cash-proof-work-order-pass-1.md)
