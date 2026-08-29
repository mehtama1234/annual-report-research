# Capital Flow AEP/Duke Load Reconciliation Workbench

## Purpose

This page starts the first real-number reconciliation workbench for the regulated utility buildout claim.

The operating data file is:

`analysis/company-first-principles/data/capital-flow-aep-duke-load-reconciliation-workbench.csv`

This workbench sits between the company-source evidence and the outside-denominator extraction.

The question is:

`Before we ask EIA, FERC, ISO/RTO, and state dockets to validate the story, what exactly are AEP and Duke claiming about load, capital, turbines, construction, and customer offsets?`

## Why AEP And Duke First

AEP and Duke are the right first two utilities because they expose the hardest regulated-utility proof problem.

They are not only saying:

`We have a large capital plan.`

They are saying:

`Large-load demand is becoming service agreements, generation planning, turbine procurement, capital deployment, and affordability engineering.`

That is a stronger and more testable claim, but it has to be reconciled carefully.

The key risk is definition drift.

`signed load`, `expected load`, `secured ESA`, `late-stage pipeline`, `under construction`, `secured turbines`, and `capital plan` are not the same kind of number.

## Workbench Summary

| Company | Rows | Main Bridge | Why It Matters |
|---|---:|---|---|
| AEP | 10 | `56 GW` signed load in Q4 `2025` to `63 GW` signed load in Q1 `2026` to `69 GW` expected load in Q2 `2026` | Best current grid-gateway case, but only if signed and expected load definitions reconcile. |
| Duke | 8 | `4.5 GW` secured data-center ESAs in FY `2025` to `7.6 GW` secured ESAs in Q1 `2026`, plus `15.4 GW` late-stage pipeline and `5 GW` under construction | Best current service-agreement-to-capital-plan case, but secured and late-stage buckets must stay separate. |

Total rows: `18`

## Visible Workbench Row Anchors

| Row Range | Company | Main Metrics |
|---|---|---|
| ADLR-001 to ADLR-010 | AEP | signed load, expected load, load bridge, capital-plan bridge, secured turbines, under-evaluation turbines, customer offsets, DOE savings |
| ADLR-011 to ADLR-018 | Duke | secured ESAs, late-stage pipeline, under-construction load, capital plan, capacity additions, secured gas turbines, ESA bridge |

## Definition Risk

## AEP Load Bridge

Current company-source sequence:

| Period | Metric | Value | Status |
|---|---|---:|---|
| Q4 `2025` | signed incremental load by `2030` | `56 GW` | source-ledger backed, needs table/footnote extraction |
| Q1 `2026` | signed incremental load by `2030` | `63 GW` | source-ledger backed, needs definition reconciliation |
| Q2 `2026` | expected new load additions by `2030` | `69 GW` | source-ledger backed, highest-priority definition risk |

The surface read is:

`AEP's load pipeline rose from 56 GW to 63 GW to 69 GW.`

The better read is:

`AEP's disclosed load opportunity grew, but Q2 uses expected-load language while Q4 and Q1 use signed-load language. We cannot treat the full bridge as apples-to-apples until the source tables and footnotes are extracted.`

### AEP Subthemes

#### Load Growth Grid Gateway

AEP is the cleanest current example of the grid becoming the gatekeeper of industrial and AI-linked growth.

The current evidence says load demand is measured in tens of gigawatts, not in vague commentary. The next evidence test is whether the load is signed, expected, under evaluation, funded, tariff-eligible, and utility-specific.

#### Regulated Capital Plan

AEP's five-year capital plan moved from `$72B` to `$78B`.

That is a `6B USD` increase, but the workbench does not yet claim the full increase is caused by incremental load. The next step is to extract the capital-plan category bridge and identify whether the increase is transmission, distribution, generation, inflation, timing, resiliency, customer-funded work, or some mix.

#### Generation Procurement

AEP reports `13 GW` of secured gas-fired turbine capacity and another `10 GW` under evaluation.

This matters because it moves the claim from paper demand to physical equipment procurement. But the secured and under-evaluation buckets must stay separate. The next proof layer needs project names, utility mapping, delivery years, state approvals, interconnection status, and fuel/logistics feasibility.

#### Affordability And Customer Offsets

AEP reports up to `$16B` of expected customer cost offsets and about `$1.4B` of projected customer savings from DOE loans and grants.

This is central because the growth claim does not survive if existing customers are forced to carry unattractive cost shifts. The next extraction must split the offset stack into customer contributions, DOE loans/grants, securitization, tax or policy support, and other mechanisms.

## Duke Load Bridge

Current company-source sequence:

| Period | Metric | Value | Status |
|---|---|---:|---|
| FY `2025` | secured data-center ESAs | `4.5 GW` | source-ledger backed, needs baseline table extraction |
| Q1 `2026` | secured data-center ESAs | `7.6 GW` | source-ledger backed, highest-priority extraction |
| Q1 `2026` | late-stage data-center pipeline | `15.4 GW` | lower-confidence pipeline bucket |
| Q1 `2026` | data-center load under construction | `5 GW` | stronger than pipeline, needs project crosswalk |

The surface read is:

`Duke has 7.6 GW of secured data-center ESAs and a 15.4 GW late-stage pipeline.`

The better read is:

`Duke has a secured ESA base that appears to rise by about 3.1 GW from the FY 2025 baseline to Q1 2026, but secured ESAs, late-stage pipeline, and under-construction load are different evidence grades.`

### Duke Subthemes

#### Regulated Load Conversion

Duke is the cleanest service-agreement case.

The key number is not just `7.6 GW`. The key is the status ladder:

`late-stage pipeline -> secured ESA -> under construction -> utility infrastructure spend -> rate recovery -> delivered load`

The next source pass should extract each status bucket separately.

#### Regulated Capital Plan

Duke has a `$103B` capital plan for `2026` through `2030`.

That number cannot be used safely without a category split. The next extraction needs generation, transmission, distribution, grid modernization, nuclear, renewables, storage, gas, and other categories where disclosed.

#### Generation Procurement

Duke reports about `14 GW` of targeted capacity additions by `2031` and `20` secured gas turbines.

This is physical capacity evidence. But the next test is project-level: which states, which utilities, which COD years, what technology mix, what approvals, what interconnection, and what cost recovery?

## Reconciliation Rules

The workbench uses five rules:

1. Do not add signed load and expected load unless definitions match.
2. Do not treat late-stage pipeline as secured load.
3. Do not treat secured turbines as approved plants.
4. Do not treat capital plans as earned returns until rate recovery is shown.
5. Do not treat customer offsets as real until the mechanism is identified.

## Outside-Denominator Links

This workbench feeds directly into the denominator map:

- AEP Ohio, AEP Texas, Indiana Michigan Power, PSO, SWEPCO, Appalachian Power, and AEP Transmission rows in the utility denominator map.
- Duke Energy Carolinas, Duke Energy Progress, Duke Energy Florida, Duke Energy Indiana, and Duke Energy Ohio/Kentucky rows in the utility denominator map.

The external sources needed next are:

- EIA Form EIA-861 for demand/customer/sales evidence
- FERC Form 714 for load evidence
- FERC Form 1 for plant, CWIP, transmission, and distribution accounts
- EIA Form EIA-860 for planned generation additions
- state utility commission dockets for approvals, tariffs, cost recovery, and customer protections

## What This Lets Us Say Now

Simple version:

AEP and Duke are showing real numbers behind the power buildout story, but the numbers are at different levels of certainty.

The safer claim is:

`AEP and Duke have official-source-backed evidence that large-load demand is being translated into utility planning, service agreements, capital plans, turbine procurement, and affordability mechanisms.`

The unsafe claim is:

`All disclosed load is guaranteed, approved, in service, and profitable.`

## Next Extraction Order

1. AEP Q2 `2026` source table for `69 GW` expected new load additions.
2. AEP Q1 `2026` and Q4 `2025` source tables for `63 GW` and `56 GW` signed incremental load.
3. Duke Q1 `2026` source table for `7.6 GW` secured ESAs, `15.4 GW` late-stage pipeline, and `5 GW` under construction.
4. Duke FY `2025`/Q4 source table for `4.5 GW` secured ESAs.
5. AEP and Duke capital-plan category splits.
6. AEP and Duke turbine/capacity-addition project mapping.
7. State docket and rate-case lookup by utility entity.

## Bottom Line

This is the first bridge from broad theme to real proof.

The broad theme is:

`Capital is flowing into power/grid bottlenecks.`

The precise test is:

`Do AEP and Duke load claims survive definition reconciliation, utility-level mapping, regulatory approval checks, and outside demand/plant/load denominators?`
