# Source Ledger

Date baseline: 2026-08-08

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
| UNH-T1 | AnnualReports.com UnitedHealth company page | 2026-08-08 | Aggregator page | Confirms Healthcare / Managed Health Care classification and shows AnnualReports currently lagging at `2024` for the hosted annual package | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/healthcare/managed-health-care/unitedhealth-group-inc/company-page-annualreports.html) |
| UNH-T2 | SEC submissions JSON for UnitedHealth | 2026-08-08 | SEC index JSON | Confirms CIK, fiscal year-end, and the filing chain for the annual and trailing three quarters | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/managed-health-care/unitedhealth-group-inc/sec-submissions.json) |
| UNH-T3 | UnitedHealth 2025 annual report on Form 10-K PDF | 2026-03-02 | Annual report PDF | Core annual narrative and financial package for the year ended `2025-12-31` | `[Disclosed]` | [2025-annual-report-10k.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/healthcare/managed-health-care/unitedhealth-group-inc/2025-annual-report-10k.pdf) |
| UNH-T4 | UnitedHealth 2025 Form 10-K | 2026-03-02 | SEC filing HTML | Standalone annual filing covering business structure, risks, and 2025 financial framing | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/managed-health-care/unitedhealth-group-inc/2025-10k.html) |
| UNH-T5 | Q4 2025 earnings release | 2026-01-27 | IR earnings release PDF | Exact Q4 and full-year 2025 metrics plus initial 2026 guidance | `[Disclosed]` | [2025-q4-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/healthcare/managed-health-care/unitedhealth-group-inc/2025-q4-earnings-release.pdf) |
| UNH-T6 | Q4 2025 8-K | 2026-01-27 | SEC filing PDF | Wrapper filing for fourth-quarter 2025 earnings release | `[Filed]` | [2025-q4-8k.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/managed-health-care/unitedhealth-group-inc/2025-q4-8k.pdf) |
| UNH-T7 | Q1 2026 earnings release | 2026-04-21 | IR earnings release PDF | Exact Q1 2026 metrics, raised guidance floor, and management-reset actions | `[Disclosed]` | [2026-q1-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/healthcare/managed-health-care/unitedhealth-group-inc/2026-q1-earnings-release.pdf) |
| UNH-T8 | Q1 2026 8-K | 2026-04-21 | SEC filing PDF | Wrapper filing for first-quarter 2026 earnings release | `[Filed]` | [2026-q1-8k.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/managed-health-care/unitedhealth-group-inc/2026-q1-8k.pdf) |
| UNH-T9 | Q1 2026 Form 10-Q | 2026-05-05 | SEC filing PDF | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/managed-health-care/unitedhealth-group-inc/2026-q1-10q.pdf) |
| UNH-T10 | Q1 2026 earnings-call prepared remarks | 2026-04-21 | IR prepared-remarks PDF | Adds management tone and commentary on governance, AI, Alegeus, and U.S. healthcare refocus | `[Disclosed]` | [2026-q1-earnings-call-remarks.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/earnings-calls/healthcare/managed-health-care/unitedhealth-group-inc/2026-q1-earnings-call-remarks.pdf) |
| UNH-T11 | Q2 2026 earnings release | 2026-07-16 | IR earnings release PDF | Exact Q2 2026 metrics, raised 2026 guidance, and reform commitments across affordability, prior authorization, and pharmacy pricing | `[Disclosed]` | [2026-q2-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/healthcare/managed-health-care/unitedhealth-group-inc/2026-q2-earnings-release.pdf) |
| UNH-T12 | Q2 2026 8-K | 2026-07-16 | SEC filing PDF | Wrapper filing for second-quarter 2026 earnings release | `[Filed]` | [2026-q2-8k.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/managed-health-care/unitedhealth-group-inc/2026-q2-8k.pdf) |
| UNH-T13 | Q2 2026 earnings-call prepared remarks | 2026-07-16 | IR prepared-remarks PDF | Adds management commentary on Medicare, Medicaid, commercial cost pressure, Optum momentum, and AI-enabled system simplification | `[Disclosed]` | [2026-q2-earnings-call-remarks.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/earnings-calls/healthcare/managed-health-care/unitedhealth-group-inc/2026-q2-earnings-call-remarks.pdf) |

## Reconciliation notes

- AnnualReports is useful here for classification and company metadata only. As of `2026-08-08`, it still lagged at `2024`, so the authoritative `2025` annual evidence chain comes from UnitedHealth IR and SEC materials.
- The correct trailing-quarter set as of `2026-08-08` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- The Q2 2026 source chain is intentionally recorded as earnings release + `8-K` + prepared remarks. No Q2 2026 `10-Q` was posted on the IR page as of `2026-08-08`, and none was collected into this workspace.
- For Q4 2025, the annual filing package serves as the main filed artifact alongside the earnings release and `8-K`.

## Missing evidence

- No posted Q2 2026 `10-Q` was collected as of `2026-08-08`.
- No full Q4 2025 earnings-call transcript was collected in the current workspace.
