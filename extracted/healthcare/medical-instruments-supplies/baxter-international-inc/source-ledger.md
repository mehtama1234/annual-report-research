# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| BAX-T1 | AnnualReports verification note | 2026-08-10 | Aggregator verification note | Confirms Baxter's CLI 8 taxonomy and `2025` archive continuity | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/healthcare/medical-instruments-supplies/baxter-international-inc/annualreports-verification.md) |
| BAX-T2 | Baxter IR source-links note | 2026-08-10 | Official-source link ledger | Preserves the intended IR pages and documents the Cloudflare-blocked retrieval path | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/medical-instruments-supplies/baxter-international-inc/ir-source-links.md) |
| BAX-T3 | Baxter SEC source-links note | 2026-08-10 | SEC filing URL ledger | Preserves the exact annual and quarter filing URLs used for the CLI 8 evidence chain | `[Filed]` | [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/baxter-international-inc/sec-source-links.md) |
| BAX-T4 | Baxter 2025 annual report PDF | 2026-03-23 filed / 2026-08-10 collected | SEC ARS PDF | Official annual report artifact for fiscal `2025` | `[Filed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/baxter-international-inc/2025-annual-report.pdf) |
| BAX-T5 | Baxter 2025 Form 10-K | 2026-02-12 filed / 2026-08-10 collected | SEC filing HTML | Filed annual report for fiscal `2025` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/baxter-international-inc/2025-10k.html) |
| BAX-T6 | Baxter Q4 2025 earnings-release exhibit | 2026-02-12 filed / 2026-08-10 collected | SEC exhibit HTML | Filed release text for late-`2025` results | `[Filed]` | [2025-q4-results-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/baxter-international-inc/2025-q4-results-release.html) |
| BAX-T7 | Baxter Q4 2025 earnings 8-K | 2026-02-12 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the Q4 `2025` release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/baxter-international-inc/2025-q4-8k.html) |
| BAX-T8 | Baxter Q1 2026 earnings-release exhibit | 2026-04-30 filed / 2026-08-10 collected | SEC exhibit HTML | Filed release text for the quarter ended `2026-03-31` | `[Filed]` | [2026-q1-results-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/baxter-international-inc/2026-q1-results-release.html) |
| BAX-T9 | Baxter Q1 2026 earnings 8-K | 2026-04-30 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the Q1 `2026` release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/baxter-international-inc/2026-q1-8k.html) |
| BAX-T10 | Baxter Q1 2026 Form 10-Q | 2026-04-30 filed / 2026-08-10 collected | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/baxter-international-inc/2026-q1-10q.html) |
| BAX-T11 | Baxter Q2 2026 earnings-release exhibit | 2026-07-30 filed / 2026-08-10 collected | SEC exhibit HTML | Filed release text for the quarter ended `2026-06-30` | `[Filed]` | [2026-q2-results-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/baxter-international-inc/2026-q2-results-release.html) |
| BAX-T12 | Baxter Q2 2026 earnings 8-K | 2026-07-30 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the Q2 `2026` release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/baxter-international-inc/2026-q2-8k.html) |
| BAX-T13 | Baxter Q2 2026 Form 10-Q | 2026-07-30 filed / 2026-08-10 collected | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/baxter-international-inc/2026-q2-10q.html) |
| BAX-T14 | SEC submissions JSON | 2026-08-10 collected | SEC metadata JSON | Verifies filing dates, accession numbers, CIK, and fiscal metadata | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/baxter-international-inc/sec-submissions.json) |

## Reconciliation notes

- Baxter now has a coherent local annual-plus-quarter filing chain for the required `2025` annual package and the last three reported quarters as of `2026-08-10`.
- The official Baxter IR path remains useful as provenance, but the shell environment could not clear the Cloudflare challenge on the investor pages.
- Because of that, the quarter-release evidence used in the packet is intentionally SEC-first through the filed `99.1` exhibits and quarter filings rather than through mirrored IR release pages.

## Missing evidence

- No local Baxter earnings-call transcript artifacts are saved.
- No clean mirrored Baxter IR HTML pages are saved because the site was challenge-blocked in this shell environment.
