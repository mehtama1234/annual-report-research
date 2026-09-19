# AEP large-load customer-obligation proof chase pass 1

Research date: `2026-09-18`

## Purpose

This chase advances the power-grid customer-cash lane from AEP's tariff and customer-security mechanics toward executed customer obligations, project allocation, and billed or collected cash. It is a proof-control artifact, not a claim that AEP's disclosed load is energized or profitable.

## Required chain

`large-load request -> LOA/ESA/application -> collateral/deposit/minimum billing/reimbursement -> approved interconnection or project -> utility investment -> billed/collected cash -> debt service and owner residual`

## Gate register

| Gate | Required object | Current evidence | Status | Stop rule |
| --- | --- | --- | --- | --- |
| AEP-LL-001 | Q2 2026 state/RTO/customer-type table and footnotes supporting `69 GW` | Company Q2 load disclosure and condition language | hold-definition | Do not combine Q4/Q1 contracted load with Q2 expected load until definitions reconcile. |
| AEP-LL-002 | AEP Ohio data-center tariff sheets and final PUCO order | Effective tariff, `25,000 kW` threshold, study fee, LOA/ESA, and reimbursement mechanics | tariff-visible | Tariff mechanics do not prove a signed customer or collected fee. |
| AEP-LL-003 | Executed or redacted LOA/ESA/application | Filing identifies large-load security and agreement conditions, but no executed customer contract is in the packet | hold-execution | Do not promote prospective or Batch Zero load to customer cash. |
| AEP-LL-004 | Financial-security terms and release/forfeiture mechanics | Approximately `$2B` of cash collateral, guarantees, and letters of credit for prospective Batch Zero load | security-visible | Security is not unrestricted cash, revenue, or construction funding without legal terms. |
| AEP-LL-005 | Interconnection, transmission-upgrade, and cost-responsibility order | ERCOT/PUCT process and cost-responsibility references | hold-approval | Do not treat load request or tariff eligibility as approved plant or rate base. |
| AEP-LL-006 | Project allocation and utility spend | AEP capital plan, secured turbines, and named generation path | hold-allocation | Do not assign aggregate capex or turbines to a customer without project mapping. |
| AEP-LL-007 | Billing determinant, minimum-demand, reimbursement, or customer contribution | Tariff provides threshold and cancellation/delay reimbursement mechanics | hold-billing | Do not call a study fee or potential reimbursement collected customer cash. |
| AEP-LL-008 | Period-matched billed/collected cash and residual bridge | Aggregate utility operating cash and capital structure only | hold-receipt | Do not promote aggregate utility OCF, collateral, or customer-offset estimates into project return. |

## Current conclusion

`aep-large-load-customer-obligation-hold-with-security-and-tariff-visible`

AEP has moved beyond generic data-center demand narrative: customer-security, tariff, and cost-responsibility mechanics are visible. The hard proof remains missing at the executed-agreement, project-allocation, billing-determinant, and receipt levels.

## Sources

- [AEP/Duke large-load security bridge](capital-flow-aep-duke-large-load-customer-security-quality-bridge-2026-09-16.md)
- [AEP/Duke approved-recovery bridge](capital-flow-aep-duke-approved-recovery-bridge-pass-1.md)
- [Power-grid customer-cash work order](annual-report-power-grid-customer-cash-proof-work-order-pass-1.md)
- [Power-grid answer synthesis](capital-flow-power-grid-pilot-answer-synthesis-pass-2.md)
