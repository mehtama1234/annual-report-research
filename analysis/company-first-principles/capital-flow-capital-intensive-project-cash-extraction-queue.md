# Capital Flow Capital-Intensive Project/Cash Extraction Queue

## Purpose

This page turns the first-pass buildout ledger into the next extraction queue.

The operating table is:

`analysis/company-first-principles/data/capital-flow-capital-intensive-project-cash-extraction-queue.csv`

The prior ledger showed that capital-intensive buildout is real at packet level. This queue asks the harder question:

`Which project, asset, backlog, capacity, fleet, throughput, working-capital, debt, or rate-recovery number would prove that the capital is actually turning into productive operating capacity?`

## Why This Queue Matters

The first buildout pass gave us enough evidence to say:

`Capital is visibly being absorbed by operating companies.`

It did not give us enough evidence to say:

`The absorbed capital is all growth, fully funded, high-return, and converting into cash.`

This queue is the bridge between those two statements.

## Queue Summary

| Queue | Linked Rows | Priority | Extraction Target |
|---|---|---|---|
| CIPC-001 | Energy Transfer; Cheniere | High | growth/maintenance capex, project schedules, contracted volumes, in-service milestones, debt/project finance, DCF |
| CIPC-002 | Nucor; Steel Dynamics | High | capex by project, tons, utilization, fabrication backlog, pricing/spreads, operating cash flow |
| CIPC-003 | United Rentals | High | gross/net rental capex, OEC, utilization, fleet productivity, free cash flow, debt/leverage |
| CIPC-004 | Sterling Infrastructure | High | signed backlog, combined backlog, future-phase work, mission-critical mix, working capital, acquisition contribution |
| CIPC-005 | AECOM; Jacobs; KBR | High | backlog quality, funded status, contract type, DSO, contract assets/liabilities, operating cash flow, debt |
| CIPC-006 | Eaton; Teledyne | High | orders, backlog, capacity investments, acquisitions, end-market tags, cash conversion, debt/leverage |
| CIPC-007 | Knife River | Medium | public-funded backlog, aggregate reserves, growth initiatives, acquisitions, greenfields, leverage |
| CIPC-008 | Verizon | High | network capex, operating cash flow, free cash flow, debt burden, subscriber/broadband adds, integration funding |
| CIPC-009 | ONE Gas | High | capex purpose, system integrity, rate base, allowed return, recovery mechanisms, debt/equity funding |
| CIPC-010 | Reliance Steel & Aluminum | Medium | tons sold, processing share, inventory, receivables, capex, cash flow, revolver/debt use |
| CIPC-011 | Cross-buildout derived claims | Medium | rewrite each claim from extracted numbers and status buckets |

Total rows: `11`

## Subtheme Workplan

### 1. Energy Infrastructure

Companies:

- Energy Transfer
- Cheniere
- ONE Gas

What to prove:

`Energy-security and reliability capital is becoming physical infrastructure: pipelines, export docks, storage, fractionation, LNG trains, gas-network replacement, customer extensions, and regulated rate-base assets.`

Numbers to pull:

- growth capex versus maintenance capex
- project name and capacity added
- bpd, mtpa, cargoes, miles, train completion, storage, or compression metrics
- contracted-volume terms
- project cost and expected in-service date
- debt, project finance, DCF, leverage, distribution coverage, rate base, allowed return, and rider recovery

Disproof tests:

- capex is mostly replacement or compliance
- project is delayed, suspended, not approved, or not contracted
- reported EBITDA/DCF is not tied to incremental in-service assets
- regulatory recovery is missing or contested

### 2. Materials And Fabrication

Companies:

- Steel Dynamics
- Nucor
- Knife River
- Reliance Steel & Aluminum

What to prove:

`Infrastructure, data centers, manufacturing, public works, aerospace, defense, and reindustrialization demand are turning into steel, fabrication, aggregates, reserves, processing capacity, inventory, and delivered tons.`

Numbers to pull:

- capex by project
- tons shipped or tons sold
- fabrication backlog
- utilization
- aggregate reserves and public-funded backlog
- growth initiatives, acquisition spend, and greenfield spend
- inventory, receivables, revolver use, pricing, spread, and operating cash flow

Disproof tests:

- volume is cyclical restocking rather than project demand
- price/spread drove results more than throughput
- capex is replacement or environmental compliance rather than capacity growth
- public funding exists but project conversion is delayed by weather, timing, energy costs, or contracting mix

### 3. Engineering, Program Delivery, And Specialty Construction

Companies:

- Jacobs
- AECOM
- KBR
- Sterling Infrastructure

What to prove:

`Capital plans need human and organizational execution capacity: design, permitting, engineering, program management, mission support, site work, utilities, electrical integration, and project controls.`

Numbers to pull:

- signed backlog
- funded backlog
- combined backlog
- award options
- future-phase opportunities
- book-to-burn or book-to-bill
- contract type and cancellability
- contract assets and liabilities
- DSO
- working-capital bridge
- operating cash flow and free cash flow
- acquisition contribution

Disproof tests:

- backlog is unfunded, cancellable, pass-through-heavy, or not margin-accretive
- revenue grows but cash conversion fails
- acquisitions explain growth more than organic demand
- customer capital plans are not tied to signed awards

### 4. Electrical And Instrumentation Equipment

Companies:

- Eaton
- Teledyne

What to prove:

`Digital, electrification, aerospace, defense, sensing, resilience, and industrial demand require physical equipment, instrumentation, thermal management, power distribution, and mission systems.`

Numbers to pull:

- orders
- backlog
- book-to-bill where available
- capacity investment
- acquisition amount and funding
- segment revenue
- margin
- cash flow
- debt and leverage
- end-market tags

Disproof tests:

- AI/data-center language is only a small part of the demand base
- acquisitions, not organic capacity, drive growth
- backlog does not convert to revenue or cash
- capacity investment creates margin pressure or execution risk

### 5. Fleet Access And Telecom Network Capex

Companies:

- United Rentals
- Verizon

What to prove:

`Some real-economy buildout is funded indirectly: customers avoid owning equipment by renting fleet access, while telecom absorbs digital demand through continuous network capex and debt capacity.`

Numbers to pull:

- gross rental capex
- net rental capex
- original equipment cost
- fleet age and utilization
- fleet productivity
- proceeds from equipment sales
- specialty and re-rent mix
- network capex by category
- operating cash flow and free cash flow
- debt, maturity, leverage, and liquidity
- subscriber and broadband net additions

Disproof tests:

- fleet productivity does not cover reinvestment requirements
- capex only maintains current capacity
- network traffic grows but returns accrue elsewhere
- debt burden limits flexibility

## Output Standard

Every extraction row should preserve:

`source ID -> filing/page/slide/section -> exact label -> value -> unit -> period -> definition bucket -> caveat -> safe claim`

The required status buckets are:

| Status | Meaning |
|---|---|
| `capex-visible` | Capex amount is visible, but purpose and conversion are not fully clear. |
| `growth-maintenance-split` | Growth and maintenance/replacement are separated. |
| `project-scheduled` | Project, expected timing, and capacity addition are named. |
| `contracted-or-regulated` | Contract, tariff, rate case, recovery mechanism, or committed customer status is visible. |
| `cash-converting` | Operating cash flow, free cash flow, DSO, inventory, fleet metrics, or working-capital bridge supports conversion. |
| `project-and-cash-grade` | Project/capacity evidence and cash/funding evidence line up for the same period or asset. |

## Bottom Line

The next move is not broader coverage. It is sharper proof.

For each buildout company, we need to answer:

`What exact physical asset, backlog, fleet, material volume, project, network, or regulated system absorbed the capital, and what cash/funding evidence shows that the absorption is economically real?`
