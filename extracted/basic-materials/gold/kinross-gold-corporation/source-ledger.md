# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| KGC-T1 | AnnualReports verification note | 2026-08-10 | Aggregator verification note | Confirms company identity, `Basic Materials` / `Gold` taxonomy, and that AnnualReports already displayed the `2025` annual package | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/annualreports/basic-materials/gold/kinross-gold-corporation/annualreports-verification.md) |
| KGC-T2 | AnnualReports company page | 2026-08-10 | Aggregator company page | Confirms archive presence, location, industry, sector, and the `2025 Annual Report` listing | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/annualreports/basic-materials/gold/kinross-gold-corporation/company-page-annualreports.html) |
| KGC-T3 | AnnualReports `2025 Annual Report` PDF | 2026-08-10 | Aggregator PDF | Provides a locally usable annual-report artifact when the direct official IR host was blocked | `[Reported]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/annualreports/basic-materials/gold/kinross-gold-corporation/2025-annual-report.pdf) |
| KGC-T4 | Official IR verification note | 2026-08-10 | Official IR verification note | Documents that the Kinross IR pages and direct annual-report route were locally Cloudflare-blocked | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/gold/kinross-gold-corporation/official-ir-verification.md) |
| KGC-T5 | SEC submissions JSON | 2026-08-10 | SEC index JSON | Confirms legal name, ticker, fiscal year-end, CIK, and the relevant `40-F` and `6-K` filing dates | `[Filed]` | [submissions-cik0000701818.json](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/gold/kinross-gold-corporation/submissions-cik0000701818.json) |
| KGC-T6 | Kinross `2025` `40-F` | 2026-03-26 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` with business, asset, reserve, and risk detail | `[Filed]` | [2025-40f.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/gold/kinross-gold-corporation/2025-40f.html) |
| KGC-T7 | `Q4 2025` `6-K` | 2026-02-18 | SEC filing HTML | Official wrapper for the full-year `2025` results package | `[Filed]` | [2025-q4-6k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/gold/kinross-gold-corporation/2025-q4-6k.html) |
| KGC-T8 | `Q4 2025` MD&A exhibit | 2026-02-18 | SEC exhibit HTML | Provides the full-year `2025` and `Q4 2025` operating, cash-flow, capital-return, and project detail used in the packet | `[Filed]` | [2025-q4-ex99-1.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/gold/kinross-gold-corporation/2025-q4-ex99-1.html) |
| KGC-T9 | `Q4 2025` audited financial-statements exhibit | 2026-02-18 | SEC exhibit HTML | Supports the annual and year-end financial read behind the `Q4 2025` package | `[Filed]` | [2025-q4-ex99-2.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/gold/kinross-gold-corporation/2025-q4-ex99-2.html) |
| KGC-T10 | `Q1 2026` `6-K` | 2026-04-29 | SEC filing HTML | Official wrapper for the first-quarter `2026` reporting package | `[Filed]` | [2026-q1-6k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/gold/kinross-gold-corporation/2026-q1-6k.html) |
| KGC-T11 | `Q1 2026` MD&A and interim-financial exhibit | 2026-04-29 | SEC exhibit HTML | Provides first-quarter `2026` production, metal sales, costs, free cash flow, taxes, and project spending detail | `[Filed]` | [2026-q1-ex99-1.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/gold/kinross-gold-corporation/2026-q1-ex99-1.html) |
| KGC-T12 | `Q2 2026` `6-K` | 2026-07-29 | SEC filing HTML | Official wrapper for the second-quarter `2026` reporting package | `[Filed]` | [2026-q2-6k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/gold/kinross-gold-corporation/2026-q2-6k.html) |
| KGC-T13 | `Q2 2026` MD&A and interim-financial exhibit | 2026-07-29 | SEC exhibit HTML | Provides the latest in-scope quarter's production, metal sales, cash, capital returns, and project-ramp detail | `[Filed]` | [2026-q2-ex99-1.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/gold/kinross-gold-corporation/2026-q2-ex99-1.html) |
| KGC-T14 | Filing note | 2026-08-10 | Filing note | Explains why the local packet uses AnnualReports plus the SEC chain rather than direct Kinross IR downloads | `[Filed]` | [filing-note.md](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/gold/kinross-gold-corporation/filing-note.md) |

## Reconciliation notes

- The correct trailing-period set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- AnnualReports was current for this company and supplied a usable local `2025` annual-report PDF.
- The official Kinross IR routes were locally blocked by Cloudflare challenge responses, so the packet relies on the SEC `40-F` and `6-K` chain for auditable annual and quarter evidence.
- The local archive now includes:
  - the AnnualReports company-page artifact
  - the AnnualReports `2025` annual-report PDF
  - the SEC submissions index
  - the `2025` `40-F`
  - the `Q4 2025`, `Q1 2026`, and `Q2 2026` `6-K` wrappers
  - the related MD&A and financial-statement exhibits
- Kinross is a Canadian issuer, but the SEC chain remains clean enough here that no external Canadian filing system was needed for packet completion.

## Missing evidence

- No locally usable official Kinross IR annual-report or quarter-results pages because the saved files are Cloudflare challenge HTML in this environment.
- No locally saved earnings-call transcripts for the in-scope periods.
