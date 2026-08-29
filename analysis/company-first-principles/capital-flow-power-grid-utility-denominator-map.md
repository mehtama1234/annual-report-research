# Capital Flow Power/Grid Utility Denominator Map

## Purpose

This page starts the first outside-denominator implementation pass for the regulated utility buildout claim.

The operating data file is:

`analysis/company-first-principles/data/capital-flow-power-grid-utility-denominator-map.csv`

This map is not the final extraction. It is the join-key layer.

The question is:

`Which exact utility entities, states, regulators, and external datasets do we need before we can test company capital-plan claims against real demand, plant, rate-case, and load data?`

## Why This Comes First

Parent-company claims are too broad for denominator work.

Examples:

- AEP says expected new load additions reached `69 GW` by `2030`.
- Duke says secured data-center electric service agreements reached about `7.6 GW`.
- Exelon says it has a `$41.7B` four-year capital plan and expected rate-base growth of `7.9%`.
- NextEra says FPL regulatory capital employed grew from `$72.9B` to `$79.7B`.

Those are useful company numbers, but the outside datasets are organized differently:

- EIA data is often utility/respondent, plant, generator, state, sector, or balancing-authority based.
- FERC Form 1 is utility/respondent and account-line based.
- FERC Form 714 is balancing-authority and planning-area based.
- State commission evidence is docket and utility-jurisdiction based.
- ISO/RTO evidence is zone, queue, project, generator, or interconnection-point based.

So the right next step is:

`parent company -> operating utility/entity -> state/regulator -> EIA/FERC/ISO join key -> metric extraction`

## Initial Mapping Summary

| Parent | Mapped Rows | Core Utility/Entity Coverage | Priority |
|---|---:|---|---|
| NextEra | 2 | Florida Power & Light plus NextEra Energy Resources | High for FPL; medium for development assets |
| Duke | 5 | Carolinas, Progress, Florida, Indiana, Ohio/Kentucky | High for major electric utilities |
| AEP | 7 | AEP Ohio, AEP Texas, Indiana Michigan Power, PSO, SWEPCO, Appalachian Power, transmission affiliates | High for load-gateway and transmission tests |
| Exelon | 6 | ComEd, PECO, BGE, Pepco, Delmarva, Atlantic City Electric | High for regulated wires and recovery-mechanism tests |

Total initial rows: `20`

## Visible Row Anchors

| Row Range | Parent | Anchor Entities |
|---|---|---|
| PGUM-001 to PGUM-002 | NextEra | Florida Power & Light; NextEra Energy Resources |
| PGUM-003 to PGUM-007 | Duke | Duke Energy Carolinas; Duke Energy Progress; Duke Energy Florida; Duke Energy Indiana; Duke Energy Ohio and Duke Energy Kentucky |
| PGUM-008 to PGUM-014 | AEP | AEP Ohio; AEP Texas; Indiana Michigan Power; Public Service Company of Oklahoma; Southwestern Electric Power Company; Appalachian Power; AEP Transmission |
| PGUM-015 to PGUM-020 | Exelon | ComEd; PECO; BGE; Pepco; Delmarva Power; Atlantic City Electric |

## What Is Confirmed From Current Company Packets

The current local company packets already support these parent-level claims:

- NextEra: FPL serves about `12M` people, and FPL regulatory capital employed rose from `$72.9B` to `$79.7B` in Q2 `2026`.
- Duke: electric utilities serve `8.7M` customers across North Carolina, South Carolina, Florida, Indiana, Ohio, and Kentucky; secured data-center ESAs reached about `7.6 GW`; the capital plan is `$103B`.
- AEP: the system serves `5.6M` customers in `11` states, has about `40,000` transmission line miles, more than `252,000` distribution miles, and expected new load additions of `69 GW` by `2030`.
- Exelon: the company serves almost `11M` customers through six fully regulated T&D utilities; the capital plan is `$41.7B`; expected rate-base growth is `7.9%`; close to `90%` of rate base is covered by established recovery mechanisms through `2026` to `2027`.

## What Is Deliberately Not Claimed Yet

This map does not yet claim:

- exact EIA respondent IDs
- exact FERC respondent IDs
- exact balancing-authority IDs
- exact rate-case docket numbers
- exact approved project costs
- exact customer contribution amounts
- exact delivered load growth by utility

Those fields are the next extraction targets.

The map marks these as lookup requirements instead of pretending we have already completed the external crosswalk.

## Regulated Utility Test Logic

### Demand Test

External sources:

- EIA Form EIA-861
- FERC Form 714
- ISO/RTO load data where relevant

Question:

`Do the utility/state/balancing-authority data show actual demand growth consistent with company load claims?`

Evidence needed:

- annual retail sales by sector
- customer counts
- peak load
- load duration indicators where available
- utility service-territory mapping

Failure condition:

The company reports a large load pipeline, but delivered-energy, customer, or peak-load evidence does not support the direction and no timing bridge explains the gap.

### Plant And Capital Test

External sources:

- FERC Form 1
- FERC Form 3-Q where useful
- EIA Form EIA-860 for plant/generator additions
- state commission capital-plan approvals

Question:

`Do capital plans become plant, CWIP, transmission assets, distribution assets, or approved generation additions?`

Evidence needed:

- electric plant in service
- construction work in progress
- transmission plant
- distribution plant
- generation plant
- approved capital trackers/riders
- planned generator additions and retirements

Failure condition:

The capital plan is large, but regulatory accounts, plant additions, or docket approvals do not show conversion.

### Recovery And Affordability Test

External sources:

- state utility commission dockets
- rate orders
- settlement agreements
- tariffs
- large-load customer agreements where available

Question:

`Who pays, who earns, and who is protected?`

Evidence needed:

- approved revenue requirement
- allowed ROE
- rider/recovery mechanism
- customer contribution
- special contract or tariff language
- residential/customer rate impact
- affordability offsets

Failure condition:

The utility can build, but regulators or customers do not allow attractive cost recovery.

## Company-Specific Next Steps

### NextEra

Start with FPL.

FPL is the cleanest regulated utility denominator because the current company claim is already framed around regulatory capital employed. The next extraction should map FPL to EIA-861 and FERC Form 1, then tie annual customer/sales/load data to FPL capital employed and Florida PSC recovery evidence.

NextEra Energy Resources should be tracked separately. It is not the same denominator problem. For that business, the right join key is project/plant/generator name, not utility respondent.

### Duke

Split Duke by operating utility.

The current company packet gives one parent-level growth claim, but the proof has to be by Carolinas, Progress, Florida, Indiana, and Ohio/Kentucky entities. This matters because load growth, generation approvals, riders, and commission outcomes are state-specific.

The first Duke extraction should prioritize the Carolinas and Florida because data-center and generation-build claims are most likely to require explicit state-level approval and cost-allocation evidence.

### AEP

Split AEP into utility and transmission components.

AEP is the best load-gateway case, but it is also the easiest to overstate. A parent-level `69 GW` expected load-additions number must be reconciled with utility-level demand, state-level tariff/rate-case evidence, transmission approvals, and service-agreement definitions.

The first AEP extraction should prioritize AEP Ohio, AEP Texas, Indiana Michigan Power, Public Service Company of Oklahoma, and AEP transmission affiliates.

### Exelon

Split Exelon by the six regulated utilities:

- ComEd
- PECO
- BGE
- Pepco
- Delmarva Power
- Atlantic City Electric

Exelon is the best control case. It is less dependent on a loud data-center story and more dependent on regulated wires, transmission, reliability, and recovery mechanisms. The extraction should test whether the `$41.7B` capital plan and `7.9%` rate-base growth are visible by utility and jurisdiction.

## Output Standard For The Next Pass

The next extraction file should not simply list utilities.

It should produce rows like:

`utility -> source -> table/line -> period -> metric -> value -> unit -> claim implication -> caveat`

Minimum required fields:

- parent company
- operating utility/entity
- source family
- source document or dataset
- respondent ID or docket ID
- period
- metric name
- reported value
- unit
- claim supported
- limitation
- next lookup

## Current Bottom Line

The regulated utility claim now has a denominator path.

The next question is no longer vague:

`Are utilities investing because load is real?`

It is now specific:

`For each operating utility, do EIA/FERC/load/rate-case records show demand, plant, approval, recovery, and affordability evidence that matches the parent-company capital-flow claim?`
