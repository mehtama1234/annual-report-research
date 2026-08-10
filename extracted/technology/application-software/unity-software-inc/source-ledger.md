# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| UNITY-T1 | AnnualReports.com Unity verification note | 2026-08-10 | Aggregator verification note | Confirms `Technology` / `Application Software` placement and documents the stale `2024` annual anchor | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/technology/application-software/unity-software-inc/annualreports-verification.md) |
| UNITY-T2 | Unity official IR verification note | 2026-08-10 | Official IR verification note | Confirms the official IR routing stack and explains the shift to SEC exhibits for local preservation | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/technology/application-software/unity-software-inc/official-ir-verification.md) |
| UNITY-T3 | AnnualReports.com Unity company page | 2026-08-10 collected | Aggregator company page HTML | Preserves company identity, ticker, taxonomy, and archive lag | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/technology/application-software/unity-software-inc/company-page.html) |
| UNITY-T4 | SEC submissions feed for CIK `0001810806` | 2026-08-10 collected | SEC metadata JSON | Confirms ticker, fiscal year-end, identity, and current filing chronology through `Q2 2026` | `[Filed]` | [submissions-cik0001810806.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/application-software/unity-software-inc/submissions-cik0001810806.json) |
| UNITY-T5 | Unity `10-K` for year ended `2025-12-31` | 2026-02-11 filed / 2026-08-10 collected | SEC annual filing HTML | Authoritative annual filing for business model, AI strategy, segment economics, risk structure, and annual financial results | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/application-software/unity-software-inc/2025-10k.html) |
| UNITY-T6 | Unity `Q4 2025` earnings release exhibit `99.1` | 2026-02-11 filed / 2026-08-10 collected | SEC exhibit HTML | Preserves the official year-end release with management commentary, quarterly and annual metrics, and guidance | `[Filed]` | [2025-q4-ex99-1.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/application-software/unity-software-inc/2025-q4-ex99-1.html) |
| UNITY-T7 | Unity `Q4 2025` earnings `8-K` | 2026-02-11 filed / 2026-08-10 collected | SEC current report HTML | Confirms the attached press release and supplemental-material posting on the IR site | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/application-software/unity-software-inc/2025-q4-8k.html) |
| UNITY-T8 | Unity `Q1 2026` earnings release exhibit `99.1` | 2026-05-07 filed / 2026-08-10 collected | SEC exhibit HTML | Preserves the official quarter release with strategic versus non-strategic framing and impairment commentary | `[Filed]` | [2026-q1-ex99-1.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/application-software/unity-software-inc/2026-q1-ex99-1.html) |
| UNITY-T9 | Unity `Q1 2026` `10-Q` | 2026-05-07 filed / 2026-08-10 collected | SEC quarterly filing HTML | Authoritative quarter filing for impairment charges, portfolio reset mechanics, deferred revenue, and liquidity | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/application-software/unity-software-inc/2026-q1-10q.html) |
| UNITY-T10 | Unity `Q1 2026` earnings `8-K` | 2026-05-07 filed / 2026-08-10 collected | SEC current report HTML | Confirms the attached press release and supplemental-material posting on the IR site | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/application-software/unity-software-inc/2026-q1-8k.html) |
| UNITY-T11 | Unity `Q2 2026` earnings release exhibit `99.1` | 2026-08-06 filed / 2026-08-10 collected | SEC exhibit HTML | Preserves the official quarter release with strategic-revenue framing, stronger profitability, and Supersonic disposition timing | `[Filed]` | [2026-q2-ex99-1.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/application-software/unity-software-inc/2026-q2-ex99-1.html) |
| UNITY-T12 | Unity `Q2 2026` `10-Q` | 2026-08-06 filed / 2026-08-10 collected | SEC quarterly filing HTML | Authoritative quarter filing for held-for-sale treatment, non-strategic revenue, and liquidity before the 2026 notes maturity | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/application-software/unity-software-inc/2026-q2-10q.html) |
| UNITY-T13 | Unity `Q2 2026` earnings `8-K` | 2026-08-06 filed / 2026-08-10 collected | SEC current report HTML | Confirms the attached press release and supplemental-material posting on the IR site | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/application-software/unity-software-inc/2026-q2-8k.html) |

## Reconciliation notes

- The authoritative Unity coverage chain for the target window is complete through:
  - `2025` annual filing
  - `Q4 2025`
  - `Q1 2026`
  - `Q2 2026`
- AnnualReports.com is preserved for taxonomy and lag confirmation, but not treated as the current annual authority because its visible annual anchor remains `2024`.
- Unity IR is the official public routing stack, but local shell fetches returned Cloudflare challenge pages during this run. The raw quarter-release bodies are therefore preserved through the SEC `8-K` exhibit chain.
- Important chronology as of Monday, August 10, 2026:
  - `Q4 2025` results filed `2026-02-11`
  - `Q1 2026` results filed `2026-05-07`
  - `Q2 2026` results filed `2026-08-06`

## Missing evidence

- No earnings-call transcript artifact is saved locally.
- No local investor-presentation PDF is saved because direct shell access to the IR site was Cloudflare-blocked during this run.
