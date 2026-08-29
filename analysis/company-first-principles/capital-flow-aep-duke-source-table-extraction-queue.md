# Capital Flow AEP/Duke Source-Table Extraction Queue

## Purpose

This page converts the AEP/Duke load reconciliation workbench into a document-level extraction queue.

The operating data file is:

`analysis/company-first-principles/data/capital-flow-aep-duke-source-table-extraction-queue.csv`

The prior workbench said what has to be reconciled:

- AEP `56 GW`, `63 GW`, and `69 GW` load bridge
- AEP `$72B` to `$78B` capital-plan bridge
- AEP `13 GW` secured turbines and `10 GW` under evaluation
- AEP `$16B` customer offsets and `$1.4B` DOE-related savings
- Duke `4.5 GW` to `7.6 GW` secured ESA bridge
- Duke `15.4 GW` late-stage pipeline and `5 GW` under-construction load
- Duke `$103B` capital plan
- Duke `14 GW` capacity target and `20` secured gas turbines

This queue says exactly which official documents to open and what table, slide, filing section, label, footnote, and caveat to extract.

## Why This Queue Matters

The next step is not yet EIA or FERC.

First we need clean company-source table extraction.

The standard is:

`source ID -> page/slide/section -> exact label -> value -> unit -> period -> definition bucket -> caveat`

Without that standard, we would risk comparing outside data to a poorly defined company number.

## Queue Summary

| Company | Queue Rows | Highest-Priority Pulls |
|---|---:|---|
| AEP | 7 | Q2 `69 GW` expected-load table; Q4/Q1 `56 GW` and `63 GW` signed-load tables; capital-plan bridge; turbine disclosure; customer-offset stack |
| Duke | 6 | Q1 `7.6 GW` secured ESA table; `15.4 GW` pipeline; `5 GW` under construction; FY `2025` `4.5 GW` baseline; `$103B` capital-plan split; capacity/turbine table |
| AEP and Duke QA | 1 | final consistency check across all extracted values |

Total rows: `14`

## AEP Extraction Targets

### ADST-001: Q2 Expected Load

Target:

`69 GW expected new load additions by 2030`

Source package:

- `AEP-T19`: Q2 `2026` earnings release
- `AEP-T20`: Q2 `2026` earnings presentation
- `AEP-T21`: Q2 `2026` supplemental schedules
- `AEP-T23`: Q2 `2026` Form `10-Q`
- `AEP-T24`: Q2 `2026` Form `8-K`

Main risk:

Q2 uses expected-load language. It may not be comparable to Q4/Q1 signed-load language.

Acceptance rule:

Record the exact table/slide, metric label, footnote, definition, state/customer split if shown, and any attrition or cancellation language.

### ADST-002: Q4/Q1 Signed Load

Targets:

- Q4 `2025`: `56 GW` signed incremental load by `2030`
- Q1 `2026`: `63 GW` signed incremental load by `2030`

Source package:

- `AEP-T9` to `AEP-T11`
- `AEP-T13` to `AEP-T15`

Main risk:

The Q4-to-Q1 bridge is only valid if the signed-load definition is stable.

Acceptance rule:

Transcribe the Q4 and Q1 metric labels and footnotes side by side.

### ADST-003: Capital-Plan Bridge

Targets:

- Q4 `2025`: `$72B` five-year capital plan
- Q1 `2026`: `$78B` five-year capital plan

Main risk:

The `$6B` increase may reflect growth investment, inflation, timing, reclassification, or category mix.

Acceptance rule:

Capture plan period, category split, change from prior plan, and any footnote explaining the increase.

### ADST-004: Turbine Procurement

Targets:

- `13 GW` secured gas-fired turbine capacity
- `10 GW` under evaluation

Main risk:

Secured turbines are not approved generation projects, and under-evaluation turbines are lower-confidence.

Acceptance rule:

Keep secured and under-evaluation buckets separate and capture any project, utility, delivery, vendor, or approval language.

### ADST-005: Customer Offsets

Targets:

- up to `$16B` expected customer cost offsets
- `$1.4B` projected customer savings from DOE loans and grants

Main risk:

Offsets may be conditional, estimated, not approved, or not available to all customer classes.

Acceptance rule:

Separate customer contributions, DOE loans/grants, securitization, tax/policy support, and other categories.

## Duke Extraction Targets

### ADST-007: Q1 ESA And Pipeline Table

Targets:

- `7.6 GW` secured data-center ESAs
- `15.4 GW` late-stage data-center pipeline
- `5 GW` under construction

Source package:

- `DUK-T13`: Q1 `2026` earnings release
- `DUK-T14`: Q1 `2026` earnings presentation
- `DUK-T16`: Q1 `2026` Form `10-Q`
- `DUK-T17`: Q1 `2026` Form `8-K`

Main risk:

Secured ESAs, late-stage pipeline, and under-construction load are different evidence grades.

Acceptance rule:

Keep each status bucket separate and preserve the exact source wording.

### ADST-008: FY 2025 Baseline ESA

Target:

`4.5 GW secured data-center ESAs`

Source package:

- `DUK-T4`: `2025` annual report
- `DUK-T8`: Q4 `2025` earnings release
- `DUK-T9`: Q4 `2025` earnings presentation
- `DUK-T11`: Q4 `2025` Form `8-K`

Main risk:

The FY `2025` baseline must be comparable to the Q1 `2026` secured ESA update.

Acceptance rule:

Capture the exact baseline definition and any customer or service-territory language.

### ADST-009: Capital-Plan Split

Target:

`$103B` capital plan for `2026` through `2030`

Main risk:

The headline number does not prove load-driven growth unless category and recovery detail are extracted.

Acceptance rule:

Capture category split and utility/state allocation where disclosed. If not disclosed, mark the gap explicitly.

### ADST-010: Capacity And Turbines

Targets:

- `14 GW` targeted capacity additions by `2031`
- `20` secured gas turbines

Main risk:

Targeted capacity and secured turbines are not the same as approved, in-service generation.

Acceptance rule:

Capture technology mix, COD timing, project/utility/state mapping, and approval status if disclosed.

## Filing Support Rows

Two rows force investor-deck claims back into filings:

- `ADST-012`: Duke Q1/Q2 `10-Q` regulatory and recovery language
- `ADST-013`: AEP Q1/Q2 `10-Q` load, capital, recovery, and affordability language

These matter because decks often carry the headline claim, but filings carry more caveats.

## QA Rule

The final QA row, `ADST-014`, exists to prevent a common error:

`Different evidence grades get merged into one clean-looking number.`

The extraction pass must assign every value a definition bucket:

- signed
- expected
- secured ESA
- late-stage pipeline
- under construction
- secured turbine
- under evaluation
- capital plan
- approved capex
- customer offset
- projected savings

## Bottom Line

The next proof step is now concrete.

We are no longer saying:

`Go read AEP and Duke filings.`

We are saying:

`Open these source IDs, extract these exact tables and footnotes, preserve these definition buckets, and only then compare the company claims to EIA, FERC, state dockets, and ISO/RTO data.`
