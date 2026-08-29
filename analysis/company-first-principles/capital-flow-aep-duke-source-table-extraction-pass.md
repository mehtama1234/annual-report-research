# Capital Flow AEP/Duke Source-Table Extraction Pass

## Purpose

This page is the first actual source-table extraction pass for AEP and Duke.

The operating data file is:

`analysis/company-first-principles/data/capital-flow-aep-duke-source-table-extraction-pass.csv`

It upgrades the prior queue from:

`document to open`

to:

`source URL -> page/slide/section -> line references -> metric -> definition bucket -> caveat -> next step`

## Important Source Availability Note

The original local source ledgers point to PDF and HTML files under an older absolute path:

`/home/manishmehta/ui-projects/annual-report-research-new-lanes/...`

That path is not available in this workspace. The repo's current `raw/` tree also does not contain the AEP/Duke PDF source files.

So this pass uses web-accessible official source documents and records the source URLs directly. It does not pretend the old local PDF artifacts were inspected here.

Tooling note: `pdftotext` and Python PDF libraries were not available in this environment. The extraction therefore uses the web-rendered PDF text available from official source URLs.

## Extraction Summary

| Company | Extracted Rows | Official Source Coverage |
|---|---:|---|
| AEP | 11 | Q2 `2026` release, Q2 `2026` presentation, Q1 `2026` presentation, Q4 `2025` presentation |
| Duke | 7 | Q1 `2026` release and Q1 `2026` presentation |

Total rows: `18`

## Visible Extraction Row Anchors

| Row Range | Company | Source Coverage |
|---|---|---|
| ADSE-001 to ADSE-011 | AEP | Q2 `2026` release/presentation, Q1 `2026` presentation, Q4 `2025` presentation |
| ADSE-012 to ADSE-018 | Duke | Q1 `2026` release and Q1 `2026` presentation |

The Duke project-level gas generation row, `ADSE-018`, captures the source table total of `7,501 MW`.

## What Improved

### AEP

The AEP load bridge is now much sharper.

Q4 `2025`:

- `56 GW` incremental contracted load by `2030`
- backed by ESAs and LOAs
- about `180 GW` active projects in the interconnection queue
- state/RTO splits are visible in the source table
- `$72B` capital-plan baseline is visible

Q1 `2026`:

- `63 GW` incremental contracted load by `2030`
- RTO split: ERCOT, PJM, SPP
- state split: Texas, Ohio, Oklahoma, Indiana, Louisiana, Virginia
- LOA/ESA conversion language is visible
- `$78B` updated capital plan and `$72B` to `$78B` bridge are visible
- category mix is visible: distribution, transmission, generation, other

Q2 `2026`:

- `69 GW` incremental contracted load by `2030`
- up from `63 GW`
- load growth tied to fully executed LOAs in ERCOT
- `13 GW` secured turbine capacity through `2031`
- `$16B` expected residential customer cost offsets from take-or-pay ESAs
- about `$5B` DOE loans and almost `$400M` DOE grants
- estimated `$1.4B` customer savings from loans and grants
- large-load tariffs approved in five of eight states where filings were submitted

The important change is that AEP's Q2 language is not merely "expected load." The Q2 presentation labels the headline as incremental contracted load, but the footnote still matters because forecasted demand depends on existing and future customer financial agreements subject to terms and conditions.

### Duke

Duke's Q1 ladder is now clearer:

- `7.6 GW` total data centers secured under ESAs
- about `2.7 GW` additional ESAs signed since Q4
- about `5 GW` already under construction
- `15.4 GW` high-confidence late-stage pipeline
- large-load customer provisions include fair-share cost language
- `14 GW` capacity additions by `2031`
- `20` gas turbines secured through GE Vernova
- EPC contracts signed for first `5 GW` of projects
- `$103B` capital plan for `2026` through `2030`
- more than `7.5 GW` new gas generation project table is visible

The important change is that Duke's Q1 presentation gives a status ladder:

`late-stage pipeline -> signed ESA -> under construction -> generation project table -> recovery mechanism`

Those buckets must stay separate.

## What We Can Say Now

The safe statement is:

`AEP and Duke have official-source table evidence that large-load growth is moving into contracted load, ESAs, capital plans, turbine procurement, project tables, recovery mechanisms, customer offsets, and regulatory workstreams.`

The unsafe statement is:

`Every disclosed GW is already approved, funded, connected, in service, and profitable.`

## Remaining Gaps

### AEP

Still needed:

- local source file acquisition
- exact slide-image table capture
- Q2 state/RTO/customer split for `69 GW`
- project/utility mapping for `13 GW` turbines
- docket-level proof for large-load tariffs
- DOE award notices and project allocations
- 10-Q filing-section extraction

### Duke

Still needed:

- local source file acquisition
- Q4 `2025` official presentation extraction for the `4.5 GW` baseline
- project/customer/service-territory split for `7.6 GW` ESAs
- docket-level proof for recovery mechanisms and customer protection
- EIA-860 matching for the new gas generation project table
- Q1/Q2 10-Q filing-section extraction

## Next Normalized Tables

This pass creates enough source evidence to build three normalized tables next:

1. AEP load bridge:
   `period -> RTO -> state -> customer type -> LOA/ESA status -> GW -> source line`

2. Duke large-load status ladder:
   `pipeline -> signed ESA -> under construction -> project -> in service`

3. Generation project crosswalk:
   `company -> state -> plant/project -> technology -> MW -> approval status -> COD -> source line -> EIA/state docket lookup`

## Bottom Line

This is the first real extraction pass behind the power/grid thesis.

The evidence now supports a more grounded claim:

`The power/grid capital-flow story is visible in official AEP and Duke source tables, but the quality of the claim depends on preserving definition buckets and then matching those buckets to state, EIA, FERC, and ISO/RTO records.`
