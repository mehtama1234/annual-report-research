# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| S-L1 | AnnualReports.com company page | 2026-08-10 collected | Aggregator page HTML | Confirms exact taxonomy placement as `Services / Education & Training Services` and shows that AnnualReports still lags at `2024` | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/annualreports/services/education-training-services/stride-inc/company-page.html) |
| S-L2 | AnnualReports.com verification note | 2026-08-10 | Aggregator verification note | Records exact-category fit and current-hosted annual-report lag | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/annualreports/services/education-training-services/stride-inc/annualreports-verification.md) |
| S-L3 | Stride official IR verification note | 2026-08-10 | Official IR verification note | Preserves the official annual-report and quarter timing chain for `Q4 2026`, `Q3 2026`, and `Q2 2026` despite local Cloudflare friction | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/education-training-services/stride-inc/official-ir-verification.md) |
| S-L4 | SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Verifies filer identity, ticker, fiscal year-end, and the in-scope filing sequence | `[Filed]` | [submissions-cik0001157408.json](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/education-training-services/stride-inc/submissions-cik0001157408.json) |
| S-L5 | Form `10-K` for fiscal year ended `2025-06-30` | 2025-08-06 filed / 2026-08-10 collected | SEC filing HTML | Core annual filing for the required `2025` annual-report window | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/education-training-services/stride-inc/2025-10k.html) |
| S-L6 | `2025` annual report PDF on form `ARS` | 2025-10-24 filed / 2026-08-10 collected | SEC annual report PDF | Standalone annual-report artifact for the `2025` annual window | `[Filed]` | [2025-annual-report-ars.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/education-training-services/stride-inc/2025-annual-report-ars.pdf) |
| S-L7 | `Q2 2026` earnings `8-K` | 2026-01-27 filed | SEC filing HTML | Filing wrapper for second-quarter fiscal `2026` results | `[Filed]` | not separately saved; filing date preserved in [submissions-cik0001157408.json](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/education-training-services/stride-inc/submissions-cik0001157408.json) |
| S-L8 | `Q2 2026` `10-Q` | 2026-01-28 filed / 2026-08-10 collected | SEC filing HTML | Strong filing evidence for second-quarter fiscal `2026` operating and financial condition | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/education-training-services/stride-inc/2026-q2-10q.html) |
| S-L9 | `Q3 2026` earnings exhibit `99.1` | 2026-04-28 filed / 2026-08-10 collected | SEC exhibit HTML | Most compact saved operating summary for third-quarter fiscal `2026` | `[Filed]` | [2026-q3-8k-ex99-1.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/education-training-services/stride-inc/2026-q3-8k-ex99-1.html) |
| S-L10 | `Q3 2026` `10-Q` | 2026-04-29 filed / 2026-08-10 collected | SEC filing HTML | Strong filing evidence for third-quarter fiscal `2026` operating and financial condition | `[Filed]` | [2026-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/education-training-services/stride-inc/2026-q3-10q.html) |
| S-L11 | `Q4 2026` earnings `8-K` | 2026-08-04 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year fiscal `2026` results | `[Filed]` | [2026-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/education-training-services/stride-inc/2026-q4-8k.html) |
| S-L12 | `Q4 2026` earnings exhibit `99.1` | 2026-08-04 filed / 2026-08-10 collected | SEC exhibit HTML | Most compact saved operating summary for fourth-quarter and full-year fiscal `2026` | `[Filed]` | [2026-q4-8k-ex99-1.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/education-training-services/stride-inc/2026-q4-8k-ex99-1.html) |

## Reconciliation notes

- AnnualReports is used here for taxonomy and archive-lag confirmation.
- Official IR is used to verify that the company itself preserved the `2025 Annual Report` and the in-scope quarter chronology, even though direct local HTML capture was challenge-blocked.
- SEC is the strongest locally saved source for the authoritative annual and quarter filing chain.
- The latest three reported periods in scope are:
  - `Q4 2026`
  - `Q3 2026`
  - `Q2 2026`

## Missing evidence

- No standalone earnings-call transcript artifact was collected in this pass.
- The company-hosted annual-report PDF URL was confirmed through official IR, but the locally saved standalone annual-report artifact comes from the SEC `ARS` filing because that was the cleaner retrievable PDF in this environment.
