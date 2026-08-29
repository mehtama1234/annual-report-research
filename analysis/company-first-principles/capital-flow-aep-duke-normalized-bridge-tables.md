# Capital Flow AEP/Duke Normalized Bridge Tables

## Purpose

This page normalizes the first AEP/Duke source-table extraction pass into denominator-ready rows.

The operating data file is:

`analysis/company-first-principles/data/capital-flow-aep-duke-normalized-bridge-tables.csv`

The prior extraction pass captured source-table facts. This artifact changes the shape:

`source fact -> normalized row type -> status bucket -> denominator lookup target -> caveat`

## Why This Matters

The next layer is EIA, FERC, state commission, and ISO/RTO validation.

Those datasets will not understand a prose claim like:

`AEP and Duke are benefiting from power demand.`

They need rows that say:

- which period
- which company
- what metric stage
- what value
- what status bucket
- what geography or operating entity
- which outside denominator should validate it
- what caveat prevents overstatement

## Normalized Row Families

| Row Type | Rows | Purpose |
|---|---:|---|
| AEP load bridge | 4 | Normalize Q4 `56 GW`, Q1 `63 GW`, Q2 `69 GW`, and the Q2 bridge. |
| AEP capital bridge | 2 | Normalize `$72B` to `$78B` and category-mix evidence. |
| AEP equipment, affordability, and regulatory rows | 4 | Keep turbines, offsets, DOE savings, and docket cues separate. |
| Duke status ladder | 5 | Separate late-stage pipeline, secured ESAs, and under-construction load. |
| Duke capital, equipment, project, and recovery rows | 5 | Normalize `$103B`, `14 GW`, `20` turbines, `7,501 MW`, and recovery mechanisms. |

Total rows: `20`

## Visible Normalized Row Anchors

| Row Range | Family |
|---|---|
| ADNB-001 to ADNB-004 | AEP load bridge |
| ADNB-005 to ADNB-006 | AEP capital bridge |
| ADNB-007 to ADNB-010 | AEP equipment, affordability, and regulatory rows |
| ADNB-011 to ADNB-015 | Duke status ladder |
| ADNB-016 to ADNB-020 | Duke capital, project, equipment, and recovery rows |

## AEP Normalized Bridge

The AEP bridge now has a clean sequence:

| Period | Metric | Value | Bucket | Core Caveat |
|---|---|---:|---|---|
| Q4 `2025` | incremental contracted load by `2030` | `56 GW` | contracted load | ESAs and LOAs must be separated; active projects are not contracted load. |
| Q1 `2026` | incremental contracted load by `2030` | `63 GW` | contracted load | RTO/state/customer split is visible but needs exact table capture. |
| Q2 `2026` | incremental contracted load by `2030` | `69 GW` | contracted load with conditions | Footnote says demand is supported by existing and future customer financial agreements subject to terms and conditions. |
| Q2 `2026` | bridge from Q1 | `6 GW` | incremental bridge | Do not confuse this with the `7 GW` contracted-load-additions-in-2026 row. |

The important normalized conclusion:

`AEP has a consistent company-source load-growth sequence, but the external test must preserve LOA, ESA, RTO, state, customer-type, and condition language.`

## AEP Capital And Affordability

AEP has two capital-plan rows:

- `$72B` Q4 `2025` capital plan baseline
- `$78B` Q1 `2026` updated capital plan

The Q1 source gives the bridge:

`PJM and SPP transmission and I&M gas generation -> +$6B`

The normalized table also keeps these rows separate:

- `13 GW` secured turbine capacity through `2031`
- `$16B` expected residential customer cost offsets
- `$1.4B` projected DOE loan/grant customer savings
- regulatory-progress docket cues

The important normalized conclusion:

`AEP's capital-flow claim is not only demand. It is demand plus transmission, generation, financing, customer offsets, and regulatory approval workstreams.`

## Duke Status Ladder

Duke has to be read as a ladder, not as one additive number.

| Stage | Value | Bucket | Meaning |
|---|---:|---|---|
| High-confidence late-stage pipeline | `15.4 GW` | pipeline | Broad opportunity set, not additive to secured ESAs. |
| Secured data-center ESAs | `7.6 GW` | signed/secured ESA | Stronger evidence grade. |
| Under construction | `5 GW` | under construction | Stronger than pipeline, but still not necessarily delivered load. |

The key rule:

`15.4 GW + 7.6 GW + 5 GW` is wrong.

The correct interpretation is:

`15.4 GW pipeline contains a 7.6 GW signed ESA subset, and that signed ESA subset contains about 5 GW under construction.`

## Duke Capital And Project Crosswalk

Duke has five normalized capital/project rows:

- `$103B` capital plan for `2026` through `2030`
- `14 GW` capacity additions by `2031`
- `20` secured gas turbines
- `7,501 MW` new gas generation project table
- electric capex recovery-mechanism framework

The `7,501 MW` row is especially important because it is closest to project-level proof. It points to named state/project rows:

- North Carolina Person County CC1
- North Carolina Marshall CT 1 and 2
- North Carolina Person County CC2
- Indiana Cayuga CC 1 and 2
- North Carolina Smith CT
- North Carolina Buck CT 3 and 4
- South Carolina Anderson County CC

The next evidence step is to turn that source table into one row per project with state docket and EIA-860 lookup fields.

## Denominator Lookup Targets

The normalized table points to these outside checks:

- EIA-861 and FERC Form 714 for load and customer demand.
- FERC Form 1 for plant, CWIP, transmission, and distribution accounts.
- EIA-860 for planned generator rows.
- State commission dockets for large-load tariffs, generation approvals, cost recovery, and customer protections.
- DOE award notices and project-finance documents for federal loan/grant savings.

## Current Claim Upgrade

Before this table, the claim was:

`AEP and Duke have official source-table evidence.`

After this table, the claim is:

`AEP and Duke have official source-table evidence that can now be tested row-by-row against external denominators, because each fact has a status bucket, caveat, and lookup target.`

## Bottom Line

This is the practical bridge into outside validation.

We are no longer stuck at:

`AEP has 69 GW and Duke has 7.6 GW.`

We now have:

`AEP load bridge, AEP capital bridge, AEP affordability stack, Duke status ladder, Duke project table, and Duke recovery-mechanism rows, each with the next denominator source attached.`
