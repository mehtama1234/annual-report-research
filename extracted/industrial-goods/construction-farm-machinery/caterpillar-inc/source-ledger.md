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
| CAT-T1 | AnnualReports.com Caterpillar company page | 2026-08-08 | Aggregator page | Confirms Industrial Goods / Construction & Farm Machinery classification and directly shows the `2025` annual package | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/industrial-goods/construction-farm-machinery/caterpillar-inc/company-page-annualreports.html) |
| CAT-T2 | SEC submissions JSON for Caterpillar | 2026-08-08 | SEC index JSON | Confirms CIK, fiscal year-end, and the filing chain for the annual and trailing three quarters | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/construction-farm-machinery/caterpillar-inc/sec-submissions.json) |
| CAT-T3 | Caterpillar 2025 annual report to shareholders | 2026-04-30 | Annual report PDF | Core annual narrative and annual financial package for the year ended `2025-12-31` | `[Filed]` | [2025-annual-report-sec-ars.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/construction-farm-machinery/caterpillar-inc/2025-annual-report-sec-ars.pdf) |
| CAT-T4 | Caterpillar 2025 Form 10-K | 2026-02-13 | SEC filing HTML | Standalone annual filing covering business mix, backlog, risks, and resource-allocation framing | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/construction-farm-machinery/caterpillar-inc/2025-10k.html) |
| CAT-T5 | Q4 2025 8-K | 2026-01-29 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year 2025 earnings release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/construction-farm-machinery/caterpillar-inc/2025-q4-8k.html) |
| CAT-T6 | Q4 2025 earnings release exhibit | 2026-01-29 | SEC exhibit HTML | Exact Q4 and full-year 2025 metrics, tariff headwinds, and entering-2026 framing | `[Filed]` | [2025-q4-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/construction-farm-machinery/caterpillar-inc/2025-q4-earnings-release-sec-ex99.html) |
| CAT-T7 | Q4 2025 earnings-call transcript | 2026-01-29 | Transcript PDF | Adds management tone on backlog, tariffs, Power & Energy, and 2026 volume expectations | `[Reported]` | [2025-q4-earnings-call-transcript.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/earnings-calls/industrial-goods/construction-farm-machinery/caterpillar-inc/2025-q4-earnings-call-transcript.pdf) |
| CAT-T8 | Q1 2026 earnings release | 2026-04-30 | IR earnings release PDF | Exact Q1 2026 metrics, cash deployment, and segment bridge | `[Disclosed]` | [2026-q1-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/construction-farm-machinery/caterpillar-inc/2026-q1-earnings-release.pdf) |
| CAT-T9 | Q1 2026 8-K | 2026-04-30 | SEC filing HTML | Wrapper filing for first-quarter 2026 earnings release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/construction-farm-machinery/caterpillar-inc/2026-q1-8k.html) |
| CAT-T10 | Q1 2026 Form 10-Q | 2026-05-06 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31`, including tariff and end-market outlook detail | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/construction-farm-machinery/caterpillar-inc/2026-q1-10q.html) |
| CAT-T11 | Q1 2026 earnings-call transcript | 2026-04-30 | Transcript PDF | Adds management commentary on record backlog, all-time record orders, and data-center-linked demand | `[Reported]` | [2026-q1-earnings-call-transcript.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/earnings-calls/industrial-goods/construction-farm-machinery/caterpillar-inc/2026-q1-earnings-call-transcript.pdf) |
| CAT-T12 | Q2 2026 earnings release | 2026-08-04 | IR earnings release PDF | Exact Q2 2026 metrics, first `$20+ billion` revenue quarter, and stronger segment mix | `[Disclosed]` | [2026-q2-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/construction-farm-machinery/caterpillar-inc/2026-q2-earnings-release.pdf) |
| CAT-T13 | Q2 2026 8-K | 2026-08-04 | SEC filing HTML | Wrapper filing for second-quarter 2026 earnings release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/construction-farm-machinery/caterpillar-inc/2026-q2-8k.html) |
| CAT-T14 | Q2 2026 Form 10-Q | 2026-08-05 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30`, including tariff recovery and end-market outlook updates | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/construction-farm-machinery/caterpillar-inc/2026-q2-10q.html) |

## Reconciliation notes

- The annual chain is unusually clean because AnnualReports already hosts the `2025` package and SEC also hosts both the annual report PDF and the `10-K`.
- The correct trailing-quarter set as of `2026-08-08` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- For the late-2025 quarter, the filed `8-K` exhibit is the cleanest saved release artifact; a separate corporate IR HTML release page was not needed once the SEC exhibit was captured.
- Q4 2025 and Q1 2026 transcripts were collected, but no Q2 2026 transcript artifact was surfaced on the Caterpillar event page during this pass.

## Missing evidence

- No official Q2 2026 earnings-call transcript was collected in the current workspace.
