# Capital Flow AEP/Duke Regulatory Docket Queue

## Purpose

This page turns the AEP/Duke normalized bridge rows into a regulatory docket extraction queue.

The operating data file is:

`analysis/company-first-principles/data/capital-flow-aep-duke-regulatory-docket-queue.csv`

The normalized bridge table got us to:

`source fact -> status bucket -> denominator lookup target`

This queue moves the next step to:

`status bucket -> jurisdiction -> docket/source entry point -> approval/recovery/customer-protection test`

## Why This Matters

The power/grid thesis is not proven by load and capex numbers alone.

For regulated utilities, the hard proof is:

`demand -> utility obligation -> project or tariff -> regulator approval -> cost recovery -> customer protection -> plant/load evidence`

Without the docket layer, we can see management's plan but not whether regulators let the plan become recoverable capital.

## Queue Summary

| Company | Rows | Main Jurisdictions |
|---|---:|---|
| AEP | 9 | Ohio, Indiana, Oklahoma, Arkansas, Louisiana, Texas, West Virginia, Virginia |
| Duke | 7 | North Carolina, South Carolina, Indiana, FERC/Carolinas combination context |

Total rows: `16`

## Visible Docket Queue Row Anchors

| Row Range | Company | Focus |
|---|---|---|
| ADDR-001 to ADDR-009 | AEP | Ohio, Indiana, Oklahoma, Arkansas, Louisiana, Texas, West Virginia, Virginia |
| ADDR-010 to ADDR-016 | Duke | North Carolina, South Carolina, Indiana, Carolinas combination approvals, gas project dockets |

## AEP Regulatory Themes

### Ohio

Ohio is high priority because it touches three AEP proof layers:

- data-center tariff and queue treatment
- AEP Ohio distribution base case
- customer affordability and rate reduction framing

The queue points to:

- PUCO AEP Ohio distribution rate case/order source
- AEP Ohio data-center tariff page

What we need:

- case number
- final order date
- minimum charge or tariff terms
- study tranche process
- customer-class impact
- distribution investment rider treatment
- evidence that existing customers are protected

### Indiana

Indiana is high priority because I&M appears in the AEP capital bridge.

The Q1 source says the `$72B` to `$78B` capital-plan bridge includes:

`PJM and SPP transmission and I&M gas generation`

The queue points to:

- IURC docketed case for I&M's Expedited Generation Resource Plan
- I&M official announcement for additional generation under the approved EGR plan

What we need:

- IURC cause/docket number
- approved resource-plan scope
- project MW
- ratemaking relief
- accounting treatment
- recovery conditions
- connection to secured turbines

### Other AEP Jurisdictions

The AEP Q2 source table also creates queue rows for:

- PSO in Oklahoma
- SWEPCO in Arkansas, Louisiana, and Texas
- Appalachian Power in West Virginia and Virginia
- AEP Texas DOE/transmission-financing treatment

These are not final proof rows. They are source-ledger-backed lookup targets from AEP's regulatory-progress slide.

## Duke Regulatory Themes

### Carolinas Rate And Combination Work

Duke's Q1 source rows point to:

- North Carolina rate case / MYRP work
- DEC/DEP combination approvals from FERC, North Carolina, and South Carolina
- recovery-mechanism treatment for electric capex
- large-load customer protections

The queue points first to Duke's regulatory information page because it aggregates current regulatory filings by service territory.

What we need:

- NCUC docket IDs
- FERC/NC/SC order references
- approved terms
- customer-savings basis
- MYRP or rider eligibility
- customer protection language

### Anderson County CC

This is the clearest Duke project-level regulatory queue row.

The source-table pass identified:

`South Carolina Anderson County CC -> 1,365 MW -> approved -> 2030`

The queue points to:

- South Carolina PSC docket `2025-250-E`
- Duke's official approval announcement

What we need:

- certificate order
- MW and project scope
- conditions
- cost recovery status
- public testimony and objections
- construction and in-service timing

### North Carolina And Indiana Gas Projects

Duke's Q1 project table adds rows for:

- Person County CC1
- Person County CC2
- Marshall CT 1 and 2
- Cayuga CC 1 and 2
- Smith CT
- Buck CT 3 and 4

The queue keeps approved and requested projects separate. Requested projects are not proof of approved recoverable capital.

## Acceptance Rule

A docket row is not accepted as proof unless it captures:

- docket/case number
- regulator
- utility or project
- order or filing date
- status: filed, requested, settled, approved, denied, appealed, or pending
- MW or capital amount where applicable
- cost recovery or rate treatment
- customer protection or customer impact
- conditions and caveats
- source URL or local source path

## Disproof Logic

The docket layer can weaken the thesis if:

- a project is requested but not approved
- approval excludes cost recovery
- customer protection is weak or absent
- tariffs are delayed or litigated
- rate-case outcomes materially reduce recovery
- project timing slips beyond company planning assumptions
- financing savings are not allocated to customers

## Bottom Line

This is the next necessary hardening step.

The AEP/Duke evidence already shows load, capex, turbines, project tables, and customer-offset claims.

The docket queue asks:

`Which parts of those claims have legal/regulatory permission to become recoverable infrastructure?`
