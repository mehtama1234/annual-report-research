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
| MMC-T1 | AnnualReports verification note for Marsh & McLennan | 2026-08-10 | Aggregator verification note | Confirms `Insurance Brokers` taxonomy and records that AnnualReports lagged at `2024` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/financial/insurance-brokers/marsh-mclennan-companies-inc/annualreports-verification.md) |
| MMC-T2 | Marsh IR source-links note | 2026-08-10 | Official-link verification note | Records the investor overview, annual reports page, quarterly earnings page, and in-scope release URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/insurance-brokers/marsh-mclennan-companies-inc/ir-source-links.md) |
| MMC-T3 | Marsh investor-overview page snapshot | 2026-08-10 | Official IR page snapshot | Confirms the current investor hub used for annual and quarterly materials | `[Disclosed]` | [investor-overview.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/insurance-brokers/marsh-mclennan-companies-inc/investor-overview.html) |
| MMC-T4 | Marsh annual-reports page snapshot | 2026-08-10 | Official IR page snapshot | Confirms the annual-reports hub and the company-posted `2025` annual report link | `[Disclosed]` | [annual-reports-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/insurance-brokers/marsh-mclennan-companies-inc/annual-reports-page.html) |
| MMC-T5 | Marsh quarterly-earnings page snapshot | 2026-08-10 | Official IR page snapshot | Confirms the quarterly-results hub used to verify the current quarter chain | `[Disclosed]` | [quarterly-earnings-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/insurance-brokers/marsh-mclennan-companies-inc/quarterly-earnings-page.html) |
| MMC-T6 | Marsh 2025 annual report PDF | 2026-08-10 local capture | Official IR annual report PDF | Preserves the company-posted `2025` annual report | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/insurance-brokers/marsh-mclennan-companies-inc/2025-annual-report.pdf) |
| MMC-T7 | Marsh SEC submissions JSON | 2026-08-10 | SEC index JSON | Confirms issuer identity and the annual / trailing-three-quarter filing sequence | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/insurance-brokers/marsh-mclennan-companies-inc/sec-submissions.json) |
| MMC-T8 | Marsh 2025 Form 10-K | 2026-02-13 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/insurance-brokers/marsh-mclennan-companies-inc/2025-10k.html) |
| MMC-T9 | Marsh Q4 2025 earnings 8-K | 2026-01-28 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` results, including the filed release exhibit chain | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/insurance-brokers/marsh-mclennan-companies-inc/2025-q4-8k.html) |
| MMC-T10 | Marsh Q1 2026 Form 10-Q | 2026-04-17 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/insurance-brokers/marsh-mclennan-companies-inc/2026-q1-10q.html) |
| MMC-T11 | Marsh Q1 2026 earnings 8-K | 2026-04-16 | SEC filing HTML | Wrapper filing for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/insurance-brokers/marsh-mclennan-companies-inc/2026-q1-8k.html) |
| MMC-T12 | Marsh Q2 2026 Form 10-Q | 2026-07-18 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/insurance-brokers/marsh-mclennan-companies-inc/2026-q2-10q.html) |
| MMC-T13 | Marsh Q2 2026 earnings 8-K | 2026-07-17 | SEC filing HTML | Wrapper filing for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/insurance-brokers/marsh-mclennan-companies-inc/2026-q2-8k.html) |

## Reconciliation notes

- AnnualReports is used here for taxonomy confirmation only. As of Monday, `2026-08-10`, it still lagged at `2024`.
- The authoritative `2025` annual-plus-three-quarter chain is therefore company IR plus SEC.
- The correct trailing-quarter set as of Monday, `2026-08-10`, is `2Q26`, `1Q26`, and `4Q25`.
- Local evidence is mixed but strong: the workspace includes the company-posted `2025` annual report PDF, official IR hub pages, and the full SEC annual and quarter chain.

## Missing evidence

- No local company-posted Marsh binary capture was preserved for the `1Q26` or `2Q26` quarterly release pages in this workspace.
- No local prepared remarks or full earnings-call transcript capture was collected for `4Q25`, `1Q26`, or `2Q26`.
