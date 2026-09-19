# Industrial contractor project-cash proof chase pass 1

Research date: `2026-09-18`

## Purpose

This chase tests whether power/grid and data-center demand reaches contractor cash through Sterling Infrastructure and MasTec. It keeps backlog, funded awards, mobilization, progress billing, contract assets, receivables, retainage, cost-to-complete, collection, fleet capex, debt, acquisitions, and diluted common residual separate.

## Required chain

`customer need -> funded award/contract -> mobilization -> labor/material/equipment -> progress measurement and billing -> collection after retainage/claims -> project cash after working capital -> debt, capex, acquisition, and common residual`

## Gate register

| Gate | Required object | Current evidence | Status | Stop rule |
| --- | --- | --- | --- | --- |
| CONTRACTOR-001 | Named utility, data-center, or infrastructure customer/cohort | Sector synthesis identifies Sterling site/infrastructure and MasTec communications/energy exposure | cohort-visible | Do not treat company backlog as a named funded customer. |
| CONTRACTOR-002 | Signed/funded scope and mobilization | Backlog and project narratives are visible; executed scope is not joined in current bridge | hold-contract | Backlog is not a funded award or cash right. |
| CONTRACTOR-003 | Revenue and progress-billing determinant | Reported revenue and contract-account disclosures | hold-billing | Revenue recognition does not prove billed or collected cash. |
| CONTRACTOR-004 | Contract assets, receivables, retainage, and aging | Working-capital and contract-balance diagnostics | hold-collection | Do not net contract assets or receivables into cash without aging and remittance. |
| CONTRACTOR-005 | Cost-to-complete, rework, claims, and margin | Contractor QoE framework and reported margin | hold-cost | Do not promote backlog margin without cost-to-complete and claims evidence. |
| CONTRACTOR-006 | Project cohort cash conversion | Aggregate OCF and capex are visible; project/cohort cash is not allocated | hold-cohort | Aggregate OCF is not project-level collection or return. |
| CONTRACTOR-007 | Fleet/property capex, debt, leases, and acquisition allocation | Sterling and MasTec capex, acquisitions, debt, and dilution diagnostics | hold-residual | Do not treat OCF-less-PP&E as owner cash. |
| CONTRACTOR-008 | Common-owner residual after all burdens | No named project cash waterfall currently closes | hold-owner-cash | Keep the industrial-contractor lane qualified and unranked. |

## Current conclusion

`industrial-contractor-project-cash-hold-backlog-and-aggregate-cash-visible`

Sterling and MasTec strengthen the power/grid proof lane by showing where buildout work may be executed, but the current evidence remains below named project collection and owner-cash proof.

## Sources

- [Industrial contractor project-cash synthesis](annual-report-industrial-contractors-project-cash-first-principles-synthesis-pass-1-2026-09-17.md)
- [Power-grid customer-cash work order](annual-report-power-grid-customer-cash-proof-work-order-pass-1.md)
- [Power-grid answer synthesis](capital-flow-power-grid-pilot-answer-synthesis-pass-2.md)
