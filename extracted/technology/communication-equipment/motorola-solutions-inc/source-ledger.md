# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| MSI-T1 | AnnualReports.com Motorola verification note | 2026-08-10 | Aggregator verification note | Confirms company identity, lagging archive status, and AnnualReports industry label | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/technology/communication-equipment/motorola-solutions-inc/annualreports-verification.md) |
| MSI-T2 | AnnualReports.com company page snapshot | 2026-08-10 collected | Aggregator HTML snapshot | Preserves company metadata and the visible `2024` annual-package lag | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/technology/communication-equipment/motorola-solutions-inc/company-page.html) |
| MSI-T3 | Motorola Solutions IR source-links note | 2026-08-10 | Official IR source note | Preserves the exact annual and quarter URLs verified from official IR despite redirect-loop collection issues | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/technology/communication-equipment/motorola-solutions-inc/ir-source-links.md) |
| MSI-T4 | SEC filing-chain note | 2026-08-10 | SEC source note | Records the exact annual-plus-quarter SEC chain used in the packet | `[Filed]` | [sec-filing-chain.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/communication-equipment/motorola-solutions-inc/sec-filing-chain.md) |
| MSI-T5 | SEC submissions index | 2026-08-10 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and the exact annual-plus-quarter sequence | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/communication-equipment/motorola-solutions-inc/sec-submissions.json) |
| MSI-T6 | FY2025 Form `10-K` | 2026-02-12 filed / 2026-08-10 collected | SEC filing HTML | Annual filing for the fiscal year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/communication-equipment/motorola-solutions-inc/2025-10k.html) |
| MSI-T7 | Q4 2025 earnings `8-K` wrapper | 2026-02-11 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the Q4 `2025` and full-year `2025` results release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/communication-equipment/motorola-solutions-inc/2025-q4-8k.html) |
| MSI-T8 | Q4 2025 earnings Exhibit `99.1` | 2026-02-11 filed / 2026-08-10 collected | SEC exhibit HTML | Preserves the Q4 `2025` and full-year `2025` metrics, backlog, and management commentary | `[Filed]` | [2025-q4-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/communication-equipment/motorola-solutions-inc/2025-q4-ex99.html) |
| MSI-T9 | Q1 2026 Form `10-Q` | 2026-05-07 filed / 2026-08-10 collected | SEC filing HTML | Quarter filing for the period ended `2026-04-04` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/communication-equipment/motorola-solutions-inc/2026-q1-10q.html) |
| MSI-T10 | Q1 2026 earnings `8-K` wrapper | 2026-05-07 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the first-quarter `2026` release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/communication-equipment/motorola-solutions-inc/2026-q1-8k.html) |
| MSI-T11 | Q1 2026 earnings Exhibit `99.1` | 2026-05-07 filed / 2026-08-10 collected | SEC exhibit HTML | Preserves first-quarter metrics, backlog, acquisition activity, and management commentary | `[Filed]` | [2026-q1-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/communication-equipment/motorola-solutions-inc/2026-q1-ex99.html) |
| MSI-T12 | Q2 2026 Form `10-Q` | 2026-08-05 filed / 2026-08-10 collected | SEC filing HTML | Latest reported quarter filing for the period ended `2026-07-04` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/communication-equipment/motorola-solutions-inc/2026-q2-10q.html) |
| MSI-T13 | Q2 2026 earnings `8-K` wrapper | 2026-08-05 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the latest reported quarter release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/communication-equipment/motorola-solutions-inc/2026-q2-8k.html) |
| MSI-T14 | Q2 2026 earnings Exhibit `99.1` | 2026-08-05 filed / 2026-08-10 collected | SEC exhibit HTML | Preserves the latest quarter metrics, updated guidance, acquisition signal, and management commentary | `[Filed]` | [2026-q2-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/communication-equipment/motorola-solutions-inc/2026-q2-ex99.html) |

## Reconciliation notes

- AnnualReports still lagged at `2024`, so it is only the taxonomy and archive-status check for this company.
- Official Motorola IR URLs were externally verified on 2026-08-10, but direct shell fetches of several official HTML and PDF endpoints redirected repeatedly.
- The SEC annual filing and quarter earnings exhibits are therefore the controlling local evidence set.
- The latest three reported quarters as of `2026-08-10` are Q2 `2026`, Q1 `2026`, and Q4 `2025`.

## Missing evidence

- No official Motorola IR PDFs or transcript files are preserved locally because of redirect-loop collection failures in this shell environment.
- The exact official URLs are preserved in [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/technology/communication-equipment/motorola-solutions-inc/ir-source-links.md).
