# Capital Flow 519-Company Pilot Refresh Pass 2

## Purpose

This page executes the first pilot from the batch-refresh design.

The question is:

`Which 35 companies should be refreshed first so the 519-company universe starts moving from queue status into source-table-visible and bridge-visible evidence?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-519-company-pilot-refresh-pass-2.csv`

## Short Answer

The first `35` company pilot is selected and ready for source extraction.

It is balanced across the seven selected lanes:

| Lane | Pilot Rows | First Question |
|---|---:|---|
| Private credit direct lending | `5` | Can platform scale join to vehicles, borrowers, facility size, use, and bank-role outcomes? |
| Insurance and retirement capital | `4` | Do liability pools show asset quality and capital treatment, or only channel scale? |
| Power/grid/project finance | `5` | Does demand move into project, tariff, contract, recovery, or physical-output evidence? |
| Debt refinancing and facilities | `5` | Does the capital-stack change fund growth, repay old debt, extend maturity, or preserve liquidity? |
| Acquisition finance | `5` | Does deal financing buy assets, customers, capacity, or only ownership transfer? |
| Asset-backed and securitization | `5` | Do operating assets become collateral pools with visible credit performance? |
| Capital intensity and capex | `6` | Does capex/backlog/assets convert into output, cash, recovery, or return? |

## Pilot Selection

| Pilot ID | Lane | Company | Ticker | Score | Bridge Model | Current Status |
|---|---|---|---|---:|---|---|
| CF519P2-001 | Private credit direct lending | Kkr Co. Inc. | KKR | `123` | Source-to-vehicle-to-borrower bridge | pilot-selected |
| CF519P2-002 | Private credit direct lending | Apollo Global Management Inc. | APO | `119` | Source-to-vehicle-to-borrower bridge | pilot-selected |
| CF519P2-003 | Private credit direct lending | Ares Management Corporation | ARES | `119` | Source-to-vehicle-to-borrower bridge | pilot-selected |
| CF519P2-004 | Private credit direct lending | Blackrock Inc. | BLK | `102` | Source-to-vehicle-to-borrower bridge | pilot-selected |
| CF519P2-005 | Private credit direct lending | Blackstone Inc. | BX | `102` | Source-to-vehicle-to-borrower bridge | pilot-selected |
| CF519P2-006 | Insurance and retirement capital | Unitedhealth Group Inc. | UNH | `95` | Liability-to-asset-quality bridge | pilot-selected |
| CF519P2-007 | Insurance and retirement capital | The Cigna Group | CI | `93` | Liability-to-asset-quality bridge | pilot-selected |
| CF519P2-008 | Insurance and retirement capital | Metlife Inc. | MET | `84` | Liability-to-asset-quality bridge | pilot-selected |
| CF519P2-009 | Insurance and retirement capital | Prudential Financial Inc. | PRU | `78` | Liability-to-asset-quality bridge | pilot-selected |
| CF519P2-010 | Power/grid/project finance | Oneok Inc. | OKE | `116` | Source-use-output-return bridge | pilot-selected |
| CF519P2-011 | Power/grid/project finance | Mastec Inc. | MTZ | `113` | Backlog return/risk bridge | pilot-selected |
| CF519P2-012 | Power/grid/project finance | Plains All American Pipeline Lp | PAA | `112` | Source-use-output-return bridge | pilot-selected |
| CF519P2-013 | Power/grid/project finance | Targa Resources Corp. | TRGP | `111` | Source-use-output-return bridge | pilot-selected |
| CF519P2-014 | Power/grid/project finance | Nextera Energy Inc. | NEE | `111` | Approved-recovery bridge | pilot-selected |
| CF519P2-015 | Debt refinancing and facilities | Pbf Energy | PBF | `113` | Before-after capital-stack bridge | pilot-selected |
| CF519P2-016 | Debt refinancing and facilities | Devon Energy Corporation | DVN | `106` | Before-after capital-stack bridge | pilot-selected |
| CF519P2-017 | Debt refinancing and facilities | Matador Resources Co. | MTDR | `102` | Before-after capital-stack bridge | pilot-selected |
| CF519P2-018 | Debt refinancing and facilities | Liberty Broadband Corporation |  | `101` | Before-after capital-stack bridge | pilot-selected |
| CF519P2-019 | Debt refinancing and facilities | Wheaton Precious Metals Corp. | WPM | `99` | Before-after capital-stack bridge | pilot-selected |
| CF519P2-020 | Acquisition finance | Core Main Inc. | CNM | `94` | Deal-source-use-integration bridge | pilot-selected |
| CF519P2-021 | Acquisition finance | Verizon Communications Inc. | VZ | `90` | Deal-source-use-integration bridge | pilot-selected |
| CF519P2-022 | Acquisition finance | The Sherwin Williams Company | SHW | `86` | Deal-source-use-integration bridge | pilot-selected |
| CF519P2-023 | Acquisition finance | Lowes Companies Inc. | LOW | `84` | Deal-source-use-integration bridge | pilot-selected |
| CF519P2-024 | Acquisition finance | Roblox Corp. | RBLX | `84` | Deal-source-use-integration bridge | pilot-selected |
| CF519P2-025 | Asset-backed and securitization | Zebra Technologies Corp. | ZBRA | `93` | Operations-to-collateral bridge | pilot-selected |
| CF519P2-026 | Asset-backed and securitization | Target Corp. | TGT | `87` | Operations-to-collateral bridge | pilot-selected |
| CF519P2-027 | Asset-backed and securitization | Msc Industrial Direct Co. Inc. | MSM | `84` | Operations-to-collateral bridge | pilot-selected |
| CF519P2-028 | Asset-backed and securitization | Global Industrial Company | GIC | `82` | Operations-to-collateral bridge | pilot-selected |
| CF519P2-029 | Asset-backed and securitization | Pool Corp. | POOL | `82` | Operations-to-collateral bridge | pilot-selected |
| CF519P2-030 | Capital intensity and capex | Jacobs Solutions Inc. |  | `105` | Capital-to-output-to-cash bridge | pilot-selected |
| CF519P2-031 | Capital intensity and capex | Steel Dynamics Inc. | STLD | `101` | Capital-to-output-to-cash bridge | pilot-selected |
| CF519P2-032 | Capital intensity and capex | Eaton Corporation | ETN | `101` | Capital-to-output-to-cash bridge | pilot-selected |
| CF519P2-033 | Capital intensity and capex | Energy Transfer Lp | ET | `100` | Source-use-output-return bridge | pilot-selected |
| CF519P2-034 | Capital intensity and capex | Sterling Infrastructure Inc. | STRL | `100` | Backlog return/risk bridge | pilot-selected |
| CF519P2-035 | Capital intensity and capex | Teledyne Technologies Inc. | TDY | `100` | Capital-to-output-to-cash bridge | pilot-selected |

## What This Pass Actually Does

This pass does not pretend to have extracted new source tables for all `35` companies.

It does three concrete things:

1. selects the first balanced pilot from the `71` row lane queue
2. assigns every pilot company a bridge model and first source task
3. defines the proof fields, expected upgrade, disproof test, and safe boundary before extraction begins

That matters because the system can now run company refreshes without changing the evidence standard company by company.

## Pilot Extraction Rules

Every pilot row needs:

- source URL or local path
- exact source family
- metric name
- period
- value
- unit
- lane-specific proof field
- caveat
- disproof signal
- next source
- refreshed proof level
- safe claim
- do-not-claim boundary

## Lane Patterns Reused

The pilot applies the completed bridge patterns:

| Pattern | Source Case | Pilot Use |
|---|---|---|
| Fleet/asset productivity | URI | asset productivity, cash conversion, collateral, and capex split |
| Backlog return/risk | Sterling | contractor backlog, RPO, signed/unsigned split, retainage, margin, cash |
| Approved recovery | AEP/Duke | utility load, tariff, docket, project approval, rate recovery |
| Source/use/output/return | Cheniere | energy projects, physical output, contract support, debt service |
| Bank-role resolution | Atwell | repay, amend, replace, coexist, or unresolved |
| Liability-to-asset quality | insurance bridge | invested assets, statutory quality, ratings/NAIC, impairments, borrower links |

## Decision

`pilot-selected - the first 35-company refresh batch is ready for source extraction.`

## First Mini-Batch Execution

The first power/grid/project-finance mini-batch has started:

`/cluster/capital-flow-power-grid-pilot-source-table-extraction-pass-1.md`

That pass extracts `25` source-backed rows across ONEOK, MasTec, Plains All American, Targa, and NextEra. It moves those five companies from `pilot-selected` to first-pass source-table/proxy evidence while preserving project-level return gaps.

The follow-through proof queue is:

`/cluster/capital-flow-power-grid-pilot-return-proof-upgrade-queue-pass-1.md`

It adds `20` pass/fail extraction tasks for project economics, backlog quality, contract support, recovery mechanisms, funding attribution, and durability risk.

The priority-1 source availability audit is:

`/cluster/capital-flow-power-grid-pilot-priority1-source-availability-pass-1.md`

That audit keeps the pilot honest: packets and source ledgers are present, but the raw source artifacts needed for promotion are not mounted in this workspace.

The official source discovery pass is:

`/cluster/capital-flow-power-grid-pilot-official-source-discovery-pass-1.md`

It identifies official online routes for the missing source packages and queues the directly usable URLs in the acquisition manifest.

The source acquisition result is:

`/cluster/capital-flow-power-grid-pilot-source-acquisition-results-pass-1.md`

It confirms that `10` official Q2 2026 source artifacts were fetched locally and are ready for parsing into priority-1 extraction rows.

The priority-1 metric extraction result is:

`/cluster/capital-flow-power-grid-pilot-priority1-metric-extraction-pass-1.md`

It parses the acquired package into `30` metric rows and keeps project-return promotion bounded.

The second-pass gap closure is:

`/cluster/capital-flow-power-grid-pilot-gap-closure-and-metric-pass-2.md`

It adds `12` additional ONEOK and MasTec metric rows after resolving direct financial-table, presentation, and 10-Q sources.

The current proof-status dashboard is:

`/cluster/capital-flow-power-grid-pilot-proof-status-dashboard-pass-1.md`

The cash-realization batch design is:

`/cluster/capital-flow-519-company-cash-realization-batch-pass-1.md`

## Safe Claim

`The 519-company system now has an executable pilot: 35 companies selected from the 71-row lane queue, with lane-specific bridge models, first source tasks, proof fields, disproof tests, and safe boundaries assigned. This is an execution plan and control table, not evidence that those 35 companies are already source-table-visible or representative.`

## Claims Not To Make Yet

Do not say:

- the `35` pilot rows are already source-proven
- the pilot proves the full `519` company universe
- a selected company passes its bridge model before source extraction
- high score equals proof grade
- all lanes should use the same extraction fields

## Next Proof

Continue from the return-proof upgrade queue, then apply the same extraction pattern to the next pilot lane.
