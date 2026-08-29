# Capital Flow Power/Grid Outside-Denominator Plan

## Purpose

This page defines the next proof layer for the power/grid capital-flow thesis.

The operating data file is:

`analysis/company-first-principles/data/capital-flow-power-grid-outside-denominator-plan.csv`

The current company-source work has reached:

`Level 3: official company-source proof`

This plan defines the bridge to:

`Level 5: outside-denominator and project-level proof`

## Why This Layer Matters

Company reports can tell us what management says it is seeing:

- contracted MW
- service agreements
- capital plans
- rate-base growth
- generation acquisitions
- BYOP projects
- capex guidance
- NGL/export volumes
- backlog
- book-to-bill
- committed and awarded projects
- EBITDA and cash-flow bridges

That is useful, but it is still company-framed evidence.

The outside-denominator layer asks a harder question:

`Do the external operating, regulatory, and financing datasets agree with the company story?`

If they do, the claim gets stronger. If they do not, the claim gets narrower or fails.

## Source Families

| Source Family | What It Tests | Claim Link |
|---|---|---|
| EIA Form EIA-861 detailed data | utility demand, customers, retail sales, sector electricity use | PGD-001 |
| FERC Form 1 | plant in service, CWIP, transmission plant, distribution plant, utility financial accounts | PGD-001 |
| FERC Form 714 | balancing-authority and planning-area load | PGD-001 |
| EIA Form EIA-860 | generator capacity, planned additions, retirements, ownership/operator data | PGD-002 |
| EIA Form EIA-923 | plant generation, fuel use, fuel receipts, utilization indicators | PGD-002 |
| ERCOT GIS | Texas generation interconnection milestones and project status | PGD-002 |
| PJM Data Miner | PJM queue, market, and generator data | PGD-002 |
| EIA natural gas/liquids datasets | basin, NGL, LPG/export, gas-market denominators | PGD-003 |
| Company filing conversion tables | backlog-to-revenue-to-margin-to-cash conversion | PGD-004 |
| ABM/CACI and peer filings | data-center and mission-critical adjacency proof | PGD-005 |
| State utility commission dockets | approved capex, riders, allowed ROE, customer contributions, rate impacts | PGD-006 |
| Financing documents | banks, bonds, private credit, project finance, tax equity, customer funding | PGD-006 |

## Claim-To-Denominator Tests

### PGD-001: Regulated Rate-Base Growth And Utility Buildout

Question:

`Are load-growth claims actually becoming regulated assets and recoverable capital?`

External checks:

- EIA Form EIA-861 for utility demand, customer counts, and sector sales.
- FERC Form 1 for plant in service, construction work in progress, transmission plant, and distribution plant.
- FERC Form 714 for peak load and planning-area load.
- State utility commission dockets for rate cases, riders, settlements, allowed ROE, customer contributions, and rate impacts.

What would strengthen the claim:

- utility-level load growth is visible outside company decks
- capital plans line up with rising plant/CWIP balances
- rate cases or riders approve recovery for specific projects
- customer contribution or special-contract language reduces cross-subsidy risk

What would weaken it:

- signed/expected/secured load definitions do not reconcile
- load growth stays in queue language without delivered-energy evidence
- state regulators reject, delay, or heavily haircut cost recovery
- affordability offsets are too small relative to capital-plan size

### PGD-002: Merchant And Contracted Power

Question:

`Are scarce generation assets and customer-backed projects real operating assets, or just announced demand?`

External checks:

- EIA Form EIA-860 for generator ownership/operator status, planned capacity additions, and retirements.
- EIA Form EIA-923 for plant-level generation, fuel use, fuel receipts, and utilization.
- ERCOT GIS for Texas generation interconnection status and projected commercial operation dates.
- PJM Data Miner for queue, generator, and market data in relevant PJM zones.
- 8-K exhibits and project documents for PPA/BYOP terms.

What would strengthen the claim:

- project MW, fuel type, location, and status reconcile across company and ISO/EIA data
- generation assets show utilization or strategic availability during scarcity periods
- contract/project documents clarify funding, risk allocation, duration, and counterparty
- acquisitions add actual dispatchable capacity rather than only financial optionality

What would weaken it:

- projects cannot be found in interconnection data
- projected commercial operation dates keep slipping
- PPA/BYOP economics remain undisclosed or unattractive
- fuel-cost or availability evidence contradicts margin claims

### PGD-003: Midstream Infrastructure And Fuel Logistics

Question:

`Are gas, NGL, crude, refined-products, and export systems expanding because physical volumes require them?`

External checks:

- EIA natural gas production and flow datasets.
- EIA liquids/NGL/LPG/export datasets.
- company project schedules and capex splits.
- debt maturity and liquidity tables.

What would strengthen the claim:

- company capex is tied to named projects with dates, capacity, and product lanes
- project timing matches basin/product/export volume growth
- a high share of earnings is fee-based or volume-backed
- debt and liquidity remain consistent with the growth program

What would weaken it:

- capex is mostly maintenance or acquisition integration
- volumes are flat while capex rises
- earnings are dominated by commodity or marketing uplift
- leverage or maturities force capex cuts

### PGD-004: Buildout Service Layer

Question:

`Do backlogs and awards convert into profitable construction, field services, and cash?`

External checks:

- quarterly and annual company filings
- backlog roll-forward where disclosed
- segment revenue and margin
- operating cash flow
- working capital
- project charges and claims

What would strengthen the claim:

- backlog converts into revenue at stable or improving margin
- operating cash flow tracks EBITDA over time
- awards are funded and repeatable rather than speculative
- customer concentration and labor constraints are manageable

What would weaken it:

- backlog rises but margins fall
- revenue grows while cash conversion deteriorates
- project charges become recurring
- large awards are delayed, redesigned, disputed, or repriced

### PGD-005: Digital Infrastructure Adjacency

Question:

`Is data-center infrastructure showing up beyond utilities and generators?`

External checks:

- ABM annual and quarterly reports.
- CACI annual and quarterly reports.
- Dycom and MasTec segment disclosures.
- selected facility services, cabling, security, and mission-critical infrastructure peers.

What would strengthen the claim:

- explicit data-center, mission-critical, secure-facility, or building-systems revenue/backlog
- disclosed customer verticals or named programs
- growth in services tied to physical data-center operations, not generic technology language

What would weaken it:

- companies use generic technology language with no data-center revenue or backlog
- exposure is immaterial
- margin/cash conversion is weak
- the link depends on inference rather than disclosed metrics

### PGD-006: System Claim

Question:

`Is power/grid really a broad capital-absorption lane across the economy?`

External checks:

- EIA demand, capacity, generation, fuel, and export denominators.
- FERC utility financial and load datasets.
- ISO interconnection queues and market data.
- state commission orders and rate cases.
- SEC financing documents, credit agreements, rating reports, and project-finance disclosures.

What would strengthen the claim:

- company claims line up with external demand, capacity, queue, regulatory, and financing records
- capital is visible across generation, wires, midstream, contractors, and financing stacks
- the same directional signal appears across multiple independent source families

What would weaken it:

- external datasets show the company evidence is isolated
- projects stall in queues or regulatory approvals
- financing is unavailable or too expensive
- cost allocation blocks customer-backed or regulated projects
- contractor economics deteriorate before projects convert into cash

## First Extraction Sequence

1. Build the AEP/Duke/Exelon/NextEra utility mapping table: utility legal entity, state, balancing authority, FERC respondent, EIA respondent, and rate-case docket links.
2. Pull EIA-861 and FERC Form 1 annual rows for those utilities.
3. Reconcile AEP and Duke load language: signed, expected, secured, late-stage, under evaluation, and in-service.
4. Pull ERCOT GIS rows for NRG BYOP and other Texas gas/power project references.
5. Pull EIA-860 and EIA-923 rows for Constellation, Vistra, and NRG plants where asset names can be matched.
6. Split ONEOK and Targa capex by named growth projects, maintenance, integration, and balance-sheet capacity.
7. Build the contractor backlog-to-cash conversion table for MasTec, Dycom, Primoris, and Granite.
8. Source-upgrade ABM and CACI before treating digital infrastructure adjacency as a real subtheme.

## Current Bottom Line

The company-source evidence already says power/grid is a major destination for capital.

The outside-denominator plan says how to test whether that claim survives contact with actual demand, capacity, queues, regulatory approvals, financing documents, and cash conversion.

The standard should be:

`company claim -> official company number -> outside denominator -> project/regulatory/financing proof -> bounded conclusion`
