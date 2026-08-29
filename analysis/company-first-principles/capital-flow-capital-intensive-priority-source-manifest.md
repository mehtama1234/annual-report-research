# Capital Flow Capital-Intensive Priority Source Manifest

## Purpose

This page is the handoff between the packet-backed project/cash extraction pass and true source-table extraction.

The operating table is:

`analysis/company-first-principles/data/capital-flow-capital-intensive-priority-source-manifest.csv`

The prior pass identified four best next rows:

1. Energy Transfer
2. Cheniere
3. United Rentals
4. Sterling Infrastructure

This manifest answers:

`Which exact source IDs must be restored or opened first, and what should each source prove?`

## Current Workspace Finding

The source ledgers are present.

The raw files referenced by those ledgers are not present in this checkout under the paths tested.

That means the current state supports:

- source-ID planning
- source-family mapping
- evidence-role assignment
- rehydration prioritization

It does not yet support:

- source-page table extraction
- page/slide citation
- exact original label transcription
- primary-source promotion to `project-and-cash-grade`

## Manifest Summary

| Manifest ID | Company | Source Set | Availability | What It Should Prove |
|---|---|---|---|---|
| CIPSM-001 | Energy Transfer | Q2 `2026` source chain | `source-table-extracted` | growth/maintenance capex, DCF, throughput, Nederland/Lone Star/y-grade capacity, latest growth-capex guide |
| CIPSM-002 | Energy Transfer | FY/Q4 `2025` source chain | `source-table-extracted` | baseline annual EBITDA/DCF, Q4 capex split, Lake Charles LNG suspension, initial 2026 growth-capex guide |
| CIPSM-003 | Cheniere | Q2 `2026` source chain | `source-table-extracted` | revenue, adjusted EBITDA, DCF, capital deployment, cargoes, Stage 3 Train 6, Train 7 timing |
| CIPSM-004 | Cheniere | FY/Q4 `2025` source chain | `source-table-extracted` | Sabine Pass/Corpus Christi capacity, FY cargoes, Stage 3 completions, DCF, capital allocation |
| CIPSM-005 | United Rentals | Q2 `2026` source chain | `partially-rehydrated-sec` | gross rental capex, fleet productivity, leverage, liquidity, specialty mix, raised guidance |
| CIPSM-006 | United Rentals | FY/Q4 `2025` source chain | `source-table-extracted` | annual operating cash flow, free cash flow, gross rental capex, rental mix, fleet metrics |
| CIPSM-007 | Sterling Infrastructure | Q2 `2026` source chain | `partially-rehydrated-sec` | signed backlog, combined backlog, future-phase work, mission-critical mix, segment shift, guidance |
| CIPSM-008 | Sterling Infrastructure | FY/Q4 `2025` source chain | `source-table-extracted` | annual backlog, E-Infrastructure growth, mission-critical mix, CEC contribution, annual EBITDA |

Total manifest rows: `8`

## Priority Pull Logic

### 1. Energy Transfer

Why first:

Energy Transfer is the cleanest row for separating growth capex from maintenance capex.

The source-table pull should extract:

- growth capex
- maintenance capex
- adjusted EBITDA
- distributable cash flow
- NGL export volumes
- NGL transportation volumes
- fractionation volumes
- Nederland export-expansion capacity
- Lone Star Express capacity
- y-grade contracted volumes
- debt, maturities, liquidity, and funding language

Promotion test:

`Promote only when project capacity, capex type, contract term, and cash/funding metric are tied to source tables.`

### 2. Cheniere

Why second:

Cheniere is the cleanest row for physical capacity conversion: LNG trains, cargoes, mtpa, DCF, and capital deployment.

The source-table pull should extract:

- Sabine Pass capacity
- Corpus Christi capacity
- Stage 3 train status
- cargoes exported
- adjusted EBITDA
- distributable cash flow
- capital deployment
- SPA/contract maturity
- debt and project-finance schedule
- regulatory approvals and in-service timing

Promotion test:

`Promote only when train completion, cargo throughput, contract term, and debt/cash-flow evidence line up.`

### 3. United Rentals

Why third:

United Rentals is the cleanest row for fleet access as capital absorption.

The source-table pull should extract:

- gross rental capex
- net rental capex
- OEC
- fleet age
- utilization
- fleet productivity
- rental revenue
- specialty mix
- proceeds from used-equipment sales
- operating cash flow
- free cash flow
- leverage, liquidity, and debt maturity

Promotion test:

`Promote only when fleet investment, utilization/productivity, free cash flow, and leverage are tied to the same reporting period.`

### 4. Sterling Infrastructure

Why fourth:

Sterling is the best row for capital reaching field execution through backlog and mission-critical project mix.

The source-table pull should extract:

- signed backlog
- combined backlog
- unsigned awards
- future-phase opportunities
- mission-critical percentage of E-Infrastructure backlog
- segment revenue and operating income
- guidance
- organic versus acquired growth
- contract assets/liabilities
- working-capital conversion

Promotion test:

`Promote only when signed/funded backlog, project/customer mix, acquisition contribution, and cash conversion are separated.`

## Why This Matters

This is the control layer that prevents overclaiming.

The packet evidence says:

`These four companies are high-signal.`

The manifest says:

`Here are the exact source chains that would prove whether the signal is project/cash-grade.`

The current file availability now says:

`The first source-table extraction has proceeded for all eight priority source families: Energy Transfer Q2 2026, Energy Transfer FY/Q4 2025, Cheniere Q2 2026, Cheniere FY/Q4 2025, United Rentals Q2 2026, United Rentals FY/Q4 2025, Sterling Q2 2026, and Sterling FY/Q4 2025. The remaining gap is no longer source-family availability; it is project-level documents, contract/customer detail, source-page/slide citation, and outside denominators.`

## Next Pass

The next source artifact should be:

`capital-flow-capital-intensive-energy-project-denominator-pass-1.md`

It should add project-level cost schedules, contract/customer evidence where public, and outside denominator checks for U.S. LNG, NGL exports, Gulf Coast fractionation, and Permian takeaway.
