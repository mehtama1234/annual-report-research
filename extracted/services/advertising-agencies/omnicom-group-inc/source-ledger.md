# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| OMC-T1 | AnnualReports.com company page | 2026-08-10 collected | Aggregator page HTML | Preserves current taxonomy and confirms AnnualReports lag versus the official `2025` annual-report chain | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/annualreports/services/advertising-agencies/omnicom-group-inc/company-page.html) |
| OMC-T2 | AnnualReports.com verification note | 2026-08-10 | Aggregator verification note | Records the observed `Services / Advertising Agencies` classification and the lagging most-recent hosted package | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/annualreports/services/advertising-agencies/omnicom-group-inc/annualreports-verification.md) |
| OMC-T3 | Omnicom official IR verification note | 2026-08-10 | Official IR verification note | Preserves the official investor-relations URL chain and the observed `2025` annual-report availability | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/advertising-agencies/omnicom-group-inc/official-ir-verification.md) |
| OMC-T4 | Omnicom `2025` annual report PDF | 2026-08-10 collected | Official IR annual report PDF | Standalone annual-report artifact for the year ended `2025-12-31` | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/advertising-agencies/omnicom-group-inc/2025-annual-report.pdf) |
| OMC-T5 | Omnicom SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Verifies filer identity, fiscal year-end, and the filing sequence for the target annual year plus trailing quarters | `[Filed]` | [submissions-cik0000029989.json](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/advertising-agencies/omnicom-group-inc/submissions-cik0000029989.json) |
| OMC-T6 | Omnicom `2025` Form `10-K` | 2026-02-20 filed / 2026-08-10 collected | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/advertising-agencies/omnicom-group-inc/2025-10k.html) |
| OMC-T7 | Omnicom Q4 `2025` earnings `8-K` | 2026-02-18 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/advertising-agencies/omnicom-group-inc/2025-q4-8k.html) |
| OMC-T8 | Omnicom Q4 `2025` earnings release | 2026-02-18 filed / 2026-08-10 collected | SEC Exhibit `99.1` HTML | Full fourth-quarter and full-year `2025` results text | `[Filed]` | [2025-q4-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/advertising-agencies/omnicom-group-inc/2025-q4-earnings-release.html) |
| OMC-T9 | Omnicom Q1 `2026` `10-Q` | 2026-04-29 filed / 2026-08-10 collected | SEC filing HTML | First-quarter `2026` filing after the IPG combination | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/advertising-agencies/omnicom-group-inc/2026-q1-10q.html) |
| OMC-T10 | Omnicom Q1 `2026` earnings `8-K` | 2026-04-28 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/advertising-agencies/omnicom-group-inc/2026-q1-8k.html) |
| OMC-T11 | Omnicom Q1 `2026` earnings release | 2026-04-28 filed / 2026-08-10 collected | SEC Exhibit `99.1` HTML | Full first-quarter `2026` results text | `[Filed]` | [2026-q1-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/advertising-agencies/omnicom-group-inc/2026-q1-earnings-release.html) |
| OMC-T12 | Omnicom Q2 `2026` `10-Q` | 2026-07-29 filed / 2026-08-10 collected | SEC filing HTML | Most recent quarter in scope including first-half results | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/advertising-agencies/omnicom-group-inc/2026-q2-10q.html) |
| OMC-T13 | Omnicom Q2 `2026` earnings `8-K` | 2026-07-28 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/advertising-agencies/omnicom-group-inc/2026-q2-8k.html) |
| OMC-T14 | Omnicom Q2 `2026` earnings release | 2026-07-28 filed / 2026-08-10 collected | SEC Exhibit `99.1` HTML | Full second-quarter `2026` results text including current management framing | `[Filed]` | [2026-q2-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/advertising-agencies/omnicom-group-inc/2026-q2-earnings-release.html) |

## Reconciliation notes

- AnnualReports is still useful here for taxonomy, but it was lagging on the most recent hosted annual-report package as of `2026-08-10`.
- Official IR already exposed the `2025 Annual Report`, so the annual-report artifact comes from official IR while the core filing chain comes from SEC.
- The latest three reported quarters in scope are:
  - Q2 `2026`
  - Q1 `2026`
  - Q4 `2025`
- The quarter-level source chain is complete through SEC filing wrappers plus earnings-release exhibits for all three periods.

## Missing evidence

- No standalone earnings-call transcript artifact is saved locally yet.
- No clean official IR HTML pages are saved locally because direct shell retrieval hit Cloudflare challenge pages.
