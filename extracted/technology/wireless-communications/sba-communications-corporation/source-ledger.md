# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| SBA-T1 | AnnualReports.com SBA verification note | 2026-08-10 | Aggregator verification note | Confirms company identity, lagging archive status, and the AnnualReports industry label | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/technology/wireless-communications/sba-communications-corporation/annualreports-verification.md) |
| SBA-T2 | AnnualReports.com company page snapshot | 2026-08-10 collected | Aggregator HTML snapshot | Preserves company metadata and the visible `2024` annual-package lag | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/technology/wireless-communications/sba-communications-corporation/company-page.html) |
| SBA-T3 | SBA investor-relations source-links note | 2026-08-10 | Official IR source note | Logs the official annual and quarter URLs used to verify the packet when AnnualReports lagged | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/technology/wireless-communications/sba-communications-corporation/ir-source-links.md) |
| SBA-T4 | SEC filing-chain note | 2026-08-10 | SEC source note | Records the exact annual-plus-quarter SEC chain used in the packet | `[Filed]` | [sec-filing-chain.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/wireless-communications/sba-communications-corporation/sec-filing-chain.md) |
| SBA-T5 | SEC submissions index | 2026-08-10 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and the exact annual-plus-quarter filing sequence | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/wireless-communications/sba-communications-corporation/sec-submissions.json) |
| SBA-T6 | FY2025 Form `10-K` | 2026-02-27 filed / 2026-08-10 collected | SEC filing HTML | Annual filing for the fiscal year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/wireless-communications/sba-communications-corporation/2025-10k.html) |
| SBA-T7 | Q4 2025 earnings `8-K` wrapper | 2026-02-26 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the Q4 `2025` results release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/wireless-communications/sba-communications-corporation/2025-q4-8k.html) |
| SBA-T8 | Q4 2025 earnings Exhibit `99.1` | 2026-02-26 filed / 2026-08-10 collected | SEC exhibit HTML | Preserves the Q4 `2025` headline results, 2026 outlook, and management commentary | `[Filed]` | [2025-q4-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/wireless-communications/sba-communications-corporation/2025-q4-ex99.html) |
| SBA-T9 | Q1 2026 Form `10-Q` | 2026-05-05 filed / 2026-08-10 collected | SEC filing HTML | Quarter filing for the period ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/wireless-communications/sba-communications-corporation/2026-q1-10q.html) |
| SBA-T10 | Q1 2026 earnings `8-K` wrapper | 2026-04-29 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the first-quarter release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/wireless-communications/sba-communications-corporation/2026-q1-8k.html) |
| SBA-T11 | Q1 2026 earnings Exhibit `99.1` | 2026-04-29 filed / 2026-08-10 collected | SEC exhibit HTML | Preserves first-quarter metrics, capital-allocation data, and management commentary | `[Filed]` | [2026-q1-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/wireless-communications/sba-communications-corporation/2026-q1-ex99.html) |
| SBA-T12 | Q2 2026 Form `10-Q` | 2026-08-06 filed / 2026-08-10 collected | SEC filing HTML | Latest reported quarter filing for the period ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/wireless-communications/sba-communications-corporation/2026-q2-10q.html) |
| SBA-T13 | Q2 2026 earnings `8-K` wrapper | 2026-08-03 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the latest reported quarter release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/wireless-communications/sba-communications-corporation/2026-q2-8k.html) |
| SBA-T14 | Q2 2026 earnings Exhibit `99.1` | 2026-08-03 filed / 2026-08-10 collected | SEC exhibit HTML | Preserves the latest quarter metrics, outlook, and management commentary | `[Filed]` | [2026-q2-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/wireless-communications/sba-communications-corporation/2026-q2-ex99.html) |

## Reconciliation notes

- AnnualReports still lagged at `2024`, so it is only the taxonomy and archive-status check for this company.
- The official investor-relations SEC-filings page verified that `2025` annual-report materials were available at company IR even though scripted local capture was blocked.
- The SEC annual filing is the controlling annual anchor for the year ended `2025-12-31`.
- The latest three reported quarters as of `2026-08-10` are Q2 `2026`, Q1 `2026`, and Q4 `2025`.
- The three-quarter window is fully supported locally through the SEC `10-Q` / `8-K` / exhibit chain.

## Missing evidence

- No standalone official IR annual-report PDF is preserved locally.
- No locally saved official IR HTML pages or transcripts are preserved because scripted retrieval of the IR site intermittently hit anti-bot protection.
