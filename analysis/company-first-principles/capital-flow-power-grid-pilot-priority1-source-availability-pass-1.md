# Capital Flow Power/Grid Pilot Priority-1 Source Availability Pass 1

## Purpose

This page audits whether the priority-1 return-proof tasks for the first five-company pilot can be executed from the current workspace.

The question is:

`Do we have the source files needed to upgrade ONEOK, MasTec, Plains, Targa, and NextEra from proxy-grade evidence into project-return, backlog-quality, contract-durability, or recovery-grade evidence?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-power-grid-pilot-priority1-source-availability-pass-1.csv`

## Short Answer

The priority-1 proof program is now source-targeted but not fully source-file-ready in this workspace.

The current workspace has:

- company packets for all five companies
- source ledgers for all five companies
- a NextEra company-analysis page
- first-pass source-table/proxy rows
- a 20-task return-proof upgrade queue

The current workspace does not have the referenced raw `10-Q`, earnings-release, presentation, supplement, XLSX, tariff, or docket files under the local `raw/` tree. The source ledgers point to those artifacts, but the paths are either from another build root or are relative paths whose raw tree is not mounted here.

## Priority-1 Availability

| Company | Priority-1 Questions | Workspace Result | Next Action |
|---|---|---|---|
| ONEOK | named project capex; segment/project throughput | source pointers exist, raw target files absent | restore or fetch Q2 2026 10-Q, earnings tables, and presentation |
| MasTec | segment backlog/funded status; segment margin | source pointers exist, raw target files absent | restore or fetch Q2 2026 release, presentation, and 10-Q |
| Plains | Cactus III economics; shipper/tariff support | Cactus III source pointers exist; tariff source still needs search | fetch/remount Q2 2026 materials and search FERC/tariff records |
| Targa | named growth-project capex; utilization/volume tables | source pointers exist, raw target files absent | restore or fetch Q2 2026 supplement, release exhibit, and 10-Q |
| NextEra | FPL recovery mechanism; Energy Resources contract/in-service detail | earnings source pointers exist; regulatory source still needs search | restore Q2 2026 supplement and search FPL docket/rider/order records |

## What This Means

This pass prevents a false promotion.

The five-company pilot can currently support source-table and proxy-grade claims, but the stronger claims require source files that are not actually available in the current local tree. The next step is therefore not to infer project economics from packet summaries; it is to acquire or remount the target source files and then extract the exact tables.

The follow-through official source discovery pass is:

`/cluster/capital-flow-power-grid-pilot-official-source-discovery-pass-1.md`

It identifies `14` official online routes for the missing Q2 2026 source packages and adds `10` queued source rows to the global source-acquisition manifest.

The source acquisition result is now:

`/cluster/capital-flow-power-grid-pilot-source-acquisition-results-pass-1.md`

It confirms that those `10` directly fetchable source rows were acquired locally and are ready for parsing.

## Extraction Gate

To promote a priority-1 task, the next pass must extract at least one of:

- named project capex plus in-service timing
- segment volume/capacity denominator
- segment backlog plus margin or funded/contract status
- shipper, tariff, PPA, ESA, rider, or commission-order terms
- project, segment, or recovery-mechanism contribution to EBITDA, EPS, cash flow, or allowed return

If the source only gives aggregate capex, aggregate backlog, aggregate GW, aggregate volume, or consolidated EBITDA, the task remains proxy-grade.

## Decision

`priority1-source-availability-audited - the first five-company return-proof queue now has an explicit source-readiness map and acquisition/remount plan.`

## Safe Claim

`The first power/grid/project-finance pilot has enough local packet and ledger evidence to define priority-1 return-proof tasks, but the raw source artifacts needed for project-return, backlog-quality, tariff/contract durability, and recovery-grade upgrades are not mounted in the current workspace.`

## Claims Not To Make Yet

Do not say:

- the priority-1 upgrade extraction has succeeded
- raw Q2 2026 filings and supplements are available in this repo
- source-ledger pointers are the same as extracted source tables
- ONEOK, MasTec, Plains, Targa, or NextEra have been promoted to project-return grade
