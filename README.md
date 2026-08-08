# Annual Report Research Workspace

Date baseline: 2026-08-08

This workspace is for collecting, organizing, and analyzing company annual reports, quarterly earnings materials, and cross-company themes by sector and industry.

Primary collection window for this project:

- `2025` annual reports and annual filings
- `2026` quarterly earnings materials as the primary quarterly focus
- the trailing quarter from late `2025` only when needed to complete the last three reported quarters as of `2026-08-08`

It is intentionally split into three layers:

- `raw/` - source documents and source-ledger notes
- `extracted/` - normalized company packets and extracted facts
- `analysis/` - sector, industry, and theme synthesis

This keeps raw evidence separate from downstream interpretation.

## Why this exists

Two existing projects already cover adjacent work:

- `ibis-industries/` is the industry-synthesis layer
- `projects/Misc/ui-projects/strategy-under-a-force/` is the theme and company-dossier layer

This workspace fills the missing middle: a disciplined repository of annual reports, 10-Ks, 10-Qs, earnings releases, and call materials organized by sector, industry, and company.

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

For most calendar-year reporters, the expected quarterly window is:

- `2026 Q2`
- `2026 Q1`
- `2025 Q4`

For off-calendar fiscal reporters, use the latest three reported fiscal quarters available as of `2026-08-08`, keeping the same principle: prioritize `2026` quarters and pull in late `2025` only when required. Label them precisely.

## Operating rule

Every analysis claim should point back to a dated source in `raw/` or a row in the source ledger.
