# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| AV-T1 | AnnualReports company page | 2026-08-10 | Aggregator page | Confirms `Healthcare / Medical Appliances & Equipment` taxonomy and the direct-plus-distributor company description | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/healthcare/medical-appliances-equipment/avanos-medical-inc/company-page.html) |
| AV-T2 | AnnualReports verification note | 2026-08-10 | Verification note | Normalizes the taxonomy and current-annual observation into repo format | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/healthcare/medical-appliances-equipment/avanos-medical-inc/annualreports-verification.md) |
| AV-T3 | SEC source-links note | 2026-08-10 | SEC filing URL ledger | Preserves the exact annual and quarter filing URLs used for the packet | `[Filed]` | [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-appliances-equipment/avanos-medical-inc/sec-source-links.md) |
| AV-T4 | SEC submissions JSON | 2026-08-10 collected | SEC metadata JSON | Verifies filing dates, accession numbers, and that `Q1 2026` is still the latest reported quarter as of `2026-08-10` | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-appliances-equipment/avanos-medical-inc/sec-submissions.json) |
| AV-T5 | Avanos `2025` annual report PDF | 2026-03-12 filed / 2026-08-10 collected | SEC ARS PDF | Official annual report artifact for fiscal `2025` | `[Filed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-appliances-equipment/avanos-medical-inc/2025-annual-report.pdf) |
| AV-T6 | Avanos `2025` Form `10-K` | 2026-02-24 filed / 2026-08-10 collected | SEC filing HTML | Filed annual report for fiscal `2025` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-appliances-equipment/avanos-medical-inc/2025-10k.html) |
| AV-T7 | Avanos Q1 `2026` earnings-release exhibit | 2026-05-05 filed / 2026-08-10 collected | SEC exhibit HTML | Gives the latest reported quarter headline numbers, segment mix, and pending take-private framing | `[Filed]` | [2026-q1-results-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-appliances-equipment/avanos-medical-inc/2026-q1-results-release.html) |
| AV-T8 | Avanos Q1 `2026` earnings `8-K` | 2026-05-05 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the latest reported quarter release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-appliances-equipment/avanos-medical-inc/2026-q1-8k.html) |
| AV-T9 | Avanos Q1 `2026` Form `10-Q` | 2026-05-05 filed / 2026-08-10 collected | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-appliances-equipment/avanos-medical-inc/2026-q1-10q.html) |
| AV-T10 | Avanos Q4 `2025` earnings-release exhibit | 2026-02-24 filed / 2026-08-10 collected | SEC exhibit HTML | Gives the full-year `2025` headline numbers, margin reset, and savings program framing | `[Filed]` | [2025-q4-results-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-appliances-equipment/avanos-medical-inc/2025-q4-results-release.html) |
| AV-T11 | Avanos Q4 `2025` earnings `8-K` | 2026-02-24 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the year-end release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-appliances-equipment/avanos-medical-inc/2025-q4-8k.html) |
| AV-T12 | Avanos Q3 `2025` earnings-release exhibit | 2025-11-05 filed / 2026-08-10 collected | SEC exhibit HTML | Gives the pre-year-end growth and Nexus acquisition framing that sets up the `2025` to `2026` arc | `[Filed]` | [2025-q3-results-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-appliances-equipment/avanos-medical-inc/2025-q3-results-release.html) |
| AV-T13 | Avanos Q3 `2025` earnings `8-K` | 2025-11-05 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the `Q3 2025` release | `[Filed]` | [2025-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-appliances-equipment/avanos-medical-inc/2025-q3-8k.html) |
| AV-T14 | Avanos Q3 `2025` Form `10-Q` | 2025-11-05 filed / 2026-08-10 collected | SEC filing HTML | Preserves the pre-year-end quarterly filing chain locally | `[Filed]` | [2025-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-appliances-equipment/avanos-medical-inc/2025-q3-10q.html) |

## Reconciliation notes

- Avanos has a coherent annual-plus-quarter filing chain for the required `2025` annual package and the latest three reported quarters as of Monday, `2026-08-10`.
- The as-of date matters here because `Q2 2026` had not yet been reported by Monday, `2026-08-10`; the required latest-three-quarter chain is therefore `Q1 2026`, `Q4 2025`, and `Q3 2025`.
- The SEC recent-filings trail does include later `2026` `8-K`s, but the saved submissions metadata shows those do not replace the reported-quarter chain for this packet.

## Missing evidence

- No local earnings-call transcript artifacts are saved.
- No separately mirrored official IR HTML stack is saved locally.
