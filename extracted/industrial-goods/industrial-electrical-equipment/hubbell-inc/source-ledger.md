# Source Ledger

Date baseline: 2026-08-09

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
| HUBB-T1 | AnnualReports taxonomy verification note | 2026-08-09 | Aggregator note | Captures the AnnualReports featured-listing taxonomy evidence and the classification mismatch issue | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/industrial-goods/industrial-electrical-equipment/hubbell-inc/annualreports-verification.md) |
| HUBB-T2 | Hubbell IR source links | 2026-08-09 | Official IR link note | Captures the annual report page, direct PDF URL, press release URLs, and fetch limitations in this environment | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/industrial-electrical-equipment/hubbell-inc/ir-source-links.md) |
| HUBB-T3 | 2025 annual report direct PDF URL, browser-verified | 2026-08-09 | Annual report PDF URL | Direct annual report source verified through the official hosted PDF even though no valid local binary copy was saved in this pass | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/industrial-electrical-equipment/hubbell-inc/ir-source-links.md) |
| HUBB-T4 | Hubbell 2025 Form 10-K | 2026-02-12 | SEC filing HTML | Formal annual business description, end-market framing, and annual financial detail | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/industrial-electrical-equipment/hubbell-inc/2025-10k.html) |
| HUBB-T5 | Q4 2025 8-K | 2026-02-03 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year 2025 results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/industrial-electrical-equipment/hubbell-inc/2025-q4-8k.html) |
| HUBB-T6 | Q4 2025 earnings release exhibit | 2026-02-03 | SEC exhibit HTML | Exact Q4 and full-year 2025 metrics, guidance, and end-market commentary | `[Filed]` | [2025-q4-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/industrial-electrical-equipment/hubbell-inc/2025-q4-earnings-release-sec-ex99.html) |
| HUBB-T7 | Q1 2026 8-K | 2026-04-30 | SEC filing HTML | Wrapper filing for first-quarter 2026 results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/industrial-electrical-equipment/hubbell-inc/2026-q1-8k.html) |
| HUBB-T8 | Q1 2026 earnings release exhibit | 2026-04-30 | SEC exhibit HTML | Exact Q1 2026 metrics, raised guidance, and transmission/substation plus data-center demand language | `[Filed]` | [2026-q1-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/industrial-electrical-equipment/hubbell-inc/2026-q1-earnings-release-sec-ex99.html) |
| HUBB-T9 | Q1 2026 Form 10-Q | 2026-05-01 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/industrial-electrical-equipment/hubbell-inc/2026-q1-10q.html) |
| HUBB-T10 | Q2 2026 8-K | 2026-07-28 | SEC filing HTML | Wrapper filing for second-quarter 2026 results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/industrial-electrical-equipment/hubbell-inc/2026-q2-8k.html) |
| HUBB-T11 | Q2 2026 earnings release exhibit | 2026-07-28 | SEC exhibit HTML | Exact Q2 2026 metrics, raised adjusted EPS guidance, and explicit grid-modernization and data-center demand language | `[Filed]` | [2026-q2-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/industrial-electrical-equipment/hubbell-inc/2026-q2-earnings-release-sec-ex99.html) |
| HUBB-T12 | Q2 2026 Form 10-Q | 2026-07-29 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/industrial-electrical-equipment/hubbell-inc/2026-q2-10q.html) |
| HUBB-T13 | SEC submissions JSON | 2026-08-09 | SEC metadata | Confirms CIK `0000048898`, fiscal year-end `1231`, and the in-scope filing chain | `[Filed]` | [submissions-cik0000048898.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/industrial-electrical-equipment/hubbell-inc/submissions-cik0000048898.json) |

## Reconciliation notes

- The correct trailing-quarter set as of `2026-08-09` is `Q2 2026`, `Q1 2026`, and `Q4 2025` because Hubbell reports on a December fiscal year.
- AnnualReports evidence found in this pass showed a legacy classification of `Consumer Goods / Electronic Equipment`, but Hubbell's current operating profile and peer set align more clearly with industrial electrical and utility infrastructure.
- The local SEC evidence chain is complete for the `2025` annual filing and the `Q4 2025` through `Q2 2026` quarter chain.
- The official annual report PDF URL was verified through the browser tool and the IR site, but no valid local binary copy was saved during this pass because the hosted download path repeatedly timed out in the shell environment.

## Missing evidence

- No official earnings-call transcript artifact was collected for Q4 2025, Q1 2026, or Q2 2026.
- No local binary copy of the official `2025` annual report PDF is saved in this pass despite the source URL being verified.
