# Source Ledger

Date baseline: 2026-08-10

Use evidence tags:

- `[Disclosed]` company filing, press release, or official investor-relations material
- `[Filed]` SEC filing or filing-equivalent reference
- `[Reported]` credible press or transcript provider
- `[Estimated]` derived or analyst estimate
- `[Speculative]` weak or unverified
- `[verify]` found but not yet confirmed directly

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| BHP-T1 | AnnualReports company page | 2026-08-10 collected | AnnualReports page | Confirms taxonomy inside `Industrial Metals & Minerals` and shows a current `2025` annual-report entry on AnnualReports | `[verify]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/annualreports/basic-materials/industrial-metals-minerals/bhp-group-plc/company-page-annualreports.html) |
| BHP-T2 | BHP official IR source index | 2026-08-10 compiled | Local source-index note | Preserves the official annual-report page, financial-results hub, financial-calendar page, half-year results release, and operational-review document URLs used for this packet | `[Disclosed]` | [official-source-index.md](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/industrial-metals-minerals/bhp-group-plc/official-source-index.md) |
| BHP-T3 | BHP official filing-chain note | 2026-08-10 compiled | Local filing-chain note | Preserves the `Form 20-F` URL and explains why the official BHP-hosted filing chain was more usable than a domestic-issuer SEC pattern in this case | `[Filed]` | [official-source-index.md](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/industrial-metals-minerals/bhp-group-plc/official-source-index.md) |

## Reconciliation notes

- The user requirement is `2025` annual reports plus the latest three reported quarters as of `Monday, August 10, 2026`.
- BHP is a foreign issuer with a `June 30` fiscal year-end and a non-standard current-period reporting cadence.
- The most honest mapping for this company is:
  - latest period: `FY26` year-end operational review for the year ended `2026-06-30`, released `2026-07-16`
  - period minus 1: `FY26` nine months operational review for the period ended `2026-03-31`, released `2026-04-22`
  - period minus 2: `FY26` half-year results for the half year ended `2025-12-31`, released `2026-02-17`
- The annual anchor is `FY2025`, not calendar `2025`, because BHP reports on a fiscal-year basis ending `June 30`.
- The official BHP-hosted annual-report and results URLs were verified, but direct file downloads repeatedly hung and produced zero-byte files in this environment. The packet therefore preserves the authoritative URL chain locally through source-index notes instead of pretending the binary files were collected successfully.

## Missing evidence

- No local BHP PDF binaries were retained because the official BHP-hosted document endpoints repeatedly stalled in this environment on `2026-08-10`.
- No earnings-call transcript was required for this packet because the annual-report, half-year-results, operational-review, and financial-calendar evidence was sufficient to anchor the periods and thematic interpretation.
