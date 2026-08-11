# Source Ledger

Date baseline: 2026-08-10

Use evidence tags:

- `[Disclosed]` company filing, press release, or official investor-relations material
- `[Filed]` SEC filing or exhibit
- `[Reported]` credible press or transcript provider
- `[Estimated]` derived or analyst estimate
- `[Speculative]` weak or unverified
- `[verify]` found but not yet confirmed directly

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| PNC-T1 | AnnualReports verification note for PNC | 2026-08-10 | Aggregator verification note | Records that AnnualReports still lagged at `2024` and classified PNC under `Money Center Banks` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/financial/regional-mid-atlantic-banks/pnc-financial-services-group-inc/annualreports-verification.md) |
| PNC-T2 | PNC financial-results page snapshot | 2026-08-10 | Official IR page snapshot | Confirms the official investor hub for annual and quarterly materials | `[Disclosed]` | [financial-results-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/regional-mid-atlantic-banks/pnc-financial-services-group-inc/financial-results-page.html) |
| PNC-T3 | PNC annual-reports page snapshot | 2026-08-10 | Official IR page snapshot | Confirms the investor annual-reports access page | `[Disclosed]` | [annual-reports-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/regional-mid-atlantic-banks/pnc-financial-services-group-inc/annual-reports-page.html) |
| PNC-T4 | PNC 2025 annual report PDF | 2026-08-10 local capture | Official IR annual report PDF | Preserves the company-posted `2025` annual report | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/regional-mid-atlantic-banks/pnc-financial-services-group-inc/2025-annual-report.pdf) |
| PNC-T5 | PNC 2025 Form 10-K | 2026-02-14 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-mid-atlantic-banks/pnc-financial-services-group-inc/2025-10k.html) |
| PNC-T6 | PNC Q4 2025 earnings release PDF | 2026-01-15 | Official IR release PDF | Company-posted fourth-quarter and full-year `2025` results | `[Disclosed]` | [2025-q4-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/regional-mid-atlantic-banks/pnc-financial-services-group-inc/2025-q4-earnings-release.pdf) |
| PNC-T7 | PNC Q4 2025 filed release exhibit | 2026-01-15 | SEC exhibit HTML | Preserves the quarter release through the filed exhibit chain | `[Filed]` | [2025-q4-8k-exhibit.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-mid-atlantic-banks/pnc-financial-services-group-inc/2025-q4-8k-exhibit.html) |
| PNC-T8 | PNC Q1 2026 earnings release PDF | 2026-04-15 | Official IR release PDF | Company-posted first-quarter `2026` results | `[Disclosed]` | [2026-q1-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/regional-mid-atlantic-banks/pnc-financial-services-group-inc/2026-q1-earnings-release.pdf) |
| PNC-T9 | PNC Q1 2026 Form 10-Q | 2026-05-05 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-mid-atlantic-banks/pnc-financial-services-group-inc/2026-q1-10q.html) |
| PNC-T10 | PNC Q2 2026 earnings release PDF | 2026-07-16 | Official IR release PDF | Company-posted second-quarter `2026` results | `[Disclosed]` | [2026-q2-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/regional-mid-atlantic-banks/pnc-financial-services-group-inc/2026-q2-earnings-release.pdf) |
| PNC-T11 | PNC Q2 2026 Form 10-Q | 2026-08-05 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-mid-atlantic-banks/pnc-financial-services-group-inc/2026-q2-10q.html) |
| PNC-T12 | PNC SEC submissions JSON | 2026-08-10 | SEC index JSON | Confirms issuer identity and the annual / trailing-three-quarter filing sequence | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-mid-atlantic-banks/pnc-financial-services-group-inc/sec-submissions.json) |

## Reconciliation notes

- AnnualReports lagged the required annual package as of Monday, `2026-08-10`, so official PNC IR and SEC materials are the authoritative chain.
- The correct trailing-quarter set as of Monday, `2026-08-10`, is `2Q26`, `1Q26`, and `4Q25`.
- PNC is a taxonomy-drift comparison case inside CLI 6: AnnualReports places it in `Money Center Banks`, while this archive uses it as a large-bank contrast alongside regional and broker names.

## Missing evidence

- No local PNC earnings-call transcript or prepared-remarks capture was preserved for `4Q25`, `1Q26`, or `2Q26`.
