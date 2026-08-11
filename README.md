# Annual Report Research Workspace

Date baseline: 2026-08-10

This workspace is for collecting, organizing, and analyzing company annual reports, quarterly earnings materials, and cross-company themes by sector and industry.

Primary collection window for this project:

- `2025` annual reports and annual filings
- `2026` quarterly earnings materials as the primary quarterly focus
- the trailing quarter from late `2025` only when needed to complete the last three reported quarters as of `2026-08-10`

It is intentionally split into three layers:

- `raw/` - source documents and source-ledger notes
- `extracted/` - normalized company packets and extracted facts
- `analysis/` - sector, industry, and theme synthesis

This keeps raw evidence separate from downstream interpretation.

## Current operating brief

Start here:

- [START-HERE.md](/home/manishmehta/ui-projects/annual-report-research/START-HERE.md)

That file points to the active operator brief, lane instructions, next-step workflow, and current handoff.
Together those files define the end-to-end pursuit goal, the lane-level output standard, the `3` to `4` flagship-company batch rule, the handoff requirements, and the expanded lane coverage across recreation, healthcare frontier, connectivity / telecom / infra tech, and capital structures / property / conglomerates.

For the fastest lane-selection view, use:

- [Active lane board](/home/manishmehta/ui-projects/annual-report-research/notes/active-lane-board-2026-08-10.md)
- [Current execution queue](/home/manishmehta/ui-projects/annual-report-research/notes/current-execution-queue-2026-08-10.md)

## Why this exists

Two existing projects already cover adjacent work:

- `ibis-industries/` is the industry-synthesis layer
- `projects/Misc/ui-projects/strategy-under-a-force/` is the theme and company-dossier layer

This workspace fills the missing middle: a disciplined repository of annual reports, 10-Ks, 10-Qs, earnings releases, and call materials organized by sector, industry, and company.

For the current cross-project fit, see:

- [Annual report stack alignment](/home/manishmehta/ui-projects/annual-report-research/analysis/annual-report-stack-alignment-2026-08-09.md)

## Folder layout

```text
annual-report-research/
  raw/
    annualreports/
    company-ir/
    sec/
    earnings-calls/
  extracted/
  analysis/
    sectors/
    industries/
    themes/
  indexes/
  templates/
  notes/
```

## Source policy

Use sources in this order:

1. Company investor-relations pages
2. SEC filings and exhibits
3. Earnings press releases and transcripts
4. AnnualReports.com for annual-report discovery, sector tags, industry tags, and archive convenience

Do not treat AnnualReports.com as the only source of truth for the last three quarters. Use company IR or SEC as the primary evidence for `2026` quarterlies and any required late-`2025` trailing quarter.

Just as important: the work is not only document collection.
The archive is also expected to identify recurring consumer trends, cultural and societal shifts, industrial and operating pressures, capital-allocation behavior, and cross-company patterns that repeat across the lane.
That includes participation systems, franchise or IP monetization, loyalty and habit formation, reimbursement or workflow control, infrastructure bottlenecks, and the broader social or institutional changes that keep showing up across multiple management teams.
The archive should keep distinguishing who is bearing the burden stack and who is capturing the cleaner economics.
If a batch can name the annual report and quarter chain but cannot explain the repeated behavior shift, pressure pattern, and monetization logic across several companies, that batch is still incomplete.

## Minimum company packet

Each covered company should end up with:

- sector
- industry
- ticker
- exchange
- fiscal year-end
- latest annual report
- latest 10-K or 20-F
- last three quarterly earnings releases
- last three quarterly 10-Qs or equivalent
- notes on what changed
- a thematic read on the bigger pattern the company helps prove

For most calendar-year reporters, the expected quarterly window is:

- `2026 Q2`
- `2026 Q1`
- `2025 Q4`

For off-calendar fiscal reporters, use the latest three reported fiscal quarters available as of `2026-08-10`, keeping the same principle: prioritize `2026` quarters and pull in late `2025` only when required. Label them precisely.

## Operating rule

Every analysis claim should point back to a dated source in `raw/` or a row in the source ledger.

Shared repo-wide indexes should not be updated continuously during exploration.
Do that at the end of a coherent batch or leave the batch ready for later integration.

## Insight-System Maintenance

For the note-boundary and insight-system audit layer:

- refresh the committed boundary report and rerun both checks with:
  - `bash scripts/refresh-note-layer-boundary.sh`
- run only the direct boundary audit with:
  - `bash scripts/audit-note-layer-boundary.sh`
- run only the broader insight-system verifier with:
  - `bash scripts/verify-insight-system.sh`
