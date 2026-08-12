# Source Ledger

Date baseline: 2026-08-10

Use evidence tags:

- `[Disclosed]` company filing, press release, or official investor-relations material
- `[Filed]` SEC filing or mirrored filing page
- `[Reported]` credible press or transcript provider
- `[Estimated]` derived or analyst estimate
- `[Speculative]` weak or unverified
- `[verify]` found but not yet confirmed directly

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| CLH-T1 | AnnualReports.com Clean Harbors company page | 2026-08-10 | Aggregator page | Confirms `Industrial Goods / Waste Management` classification and shows that AnnualReports already exposes the `2025` annual report and Form `10-K` | `[Reported]` | [company-page-annualreports.html](/raw/annualreports/industrial-goods/waste-management/clean-harbors-inc/company-page-annualreports.html) |
| CLH-T2 | Clean Harbors annual-reports page | 2026-08-10 | Official IR page | Confirms the official `2025 Annual Report` PDF is live on IR | `[Disclosed]` | [annual-reports.html](/raw/company-ir/industrial-goods/waste-management/clean-harbors-inc/annual-reports.html) |
| CLH-T3 | Clean Harbors 2025 annual report PDF | 2026-08-10 | Annual report PDF | Core annual narrative package for the year ended `2025-12-31` | `[Disclosed]` | [2025-annual-report.pdf](/raw/company-ir/industrial-goods/waste-management/clean-harbors-inc/2025-annual-report.pdf) |
| CLH-T4 | SEC submissions JSON for Clean Harbors | 2026-08-10 | SEC index JSON | Confirms CIK, fiscal year-end, and accession chain for the annual and trailing-quarter filings | `[Filed]` | [sec-submissions.json](/raw/sec/industrial-goods/waste-management/clean-harbors-inc/sec-submissions.json) |
| CLH-T5 | Clean Harbors 2025 10-K filing page | 2026-02-18 | IR filing-detail page | Confirms annual filing date, document date, and filing type | `[Filed]` | [2025-10k-ir-filing-page.html](/raw/company-ir/industrial-goods/waste-management/clean-harbors-inc/2025-10k-ir-filing-page.html) |
| CLH-T6 | Clean Harbors mirrored 2025 10-K HTML | 2026-02-18 | Mirrored filing HTML | Local mirror of the filed annual report content | `[Filed]` | [2025-10k.html](/raw/company-ir/industrial-goods/waste-management/clean-harbors-inc/2025-10k.html) |
| CLH-T7 | Q4 2025 and full-year 2025 earnings release | 2026-02-18 | Official IR release | Exact Q4 and full-year `2025` metrics plus `2026` starting guidance and operating commentary | `[Disclosed]` | [2025-q4-earnings-release.html](/raw/company-ir/industrial-goods/waste-management/clean-harbors-inc/2025-q4-earnings-release.html) |
| CLH-T8 | Clean Harbors Q1 2026 10-Q filing page | 2026-05-06 | IR filing-detail page | Confirms Q1 `2026` filing date and document date | `[Filed]` | [2026-q1-10q-ir-filing-page.html](/raw/company-ir/industrial-goods/waste-management/clean-harbors-inc/2026-q1-10q-ir-filing-page.html) |
| CLH-T9 | Clean Harbors mirrored Q1 2026 10-Q HTML | 2026-05-06 | Mirrored filing HTML | Local mirror of the filed Q1 `2026` report | `[Filed]` | [2026-q1-10q.html](/raw/company-ir/industrial-goods/waste-management/clean-harbors-inc/2026-q1-10q.html) |
| CLH-T10 | Q1 2026 earnings release | 2026-05-06 | Official IR release | Exact Q1 `2026` metrics, raised guidance, and operating commentary around PFAS, disposal demand, and Safety-Kleen spread management | `[Disclosed]` | [2026-q1-earnings-release.html](/raw/company-ir/industrial-goods/waste-management/clean-harbors-inc/2026-q1-earnings-release.html) |
| CLH-T11 | Clean Harbors Q2 2026 10-Q filing page | 2026-07-29 | IR filing-detail page | Confirms Q2 `2026` filing date and document date | `[Filed]` | [2026-q2-10q-ir-filing-page.html](/raw/company-ir/industrial-goods/waste-management/clean-harbors-inc/2026-q2-10q-ir-filing-page.html) |
| CLH-T12 | Clean Harbors mirrored Q2 2026 10-Q HTML | 2026-07-29 | Mirrored filing HTML | Local mirror of the filed Q2 `2026` report | `[Filed]` | [2026-q2-10q.html](/raw/company-ir/industrial-goods/waste-management/clean-harbors-inc/2026-q2-10q.html) |
| CLH-T13 | Q2 2026 earnings release | 2026-07-29 | Official IR release | Exact Q2 `2026` metrics, raised guidance, ten-year disposal contract, and planned `ES&H` acquisition | `[Disclosed]` | [2026-q2-earnings-release.html](/raw/company-ir/industrial-goods/waste-management/clean-harbors-inc/2026-q2-earnings-release.html) |
| CLH-T14 | Clean Harbors quarterly-results page | 2026-08-10 | Official IR page | Confirms the trailing-quarter set as of `2026-08-10` and the linked filing chain | `[Disclosed]` | [quarterly-results.html](/raw/company-ir/industrial-goods/waste-management/clean-harbors-inc/quarterly-results.html) |
| CLH-T15 | Clean Harbors events and presentations page | 2026-08-10 | Official IR page | Confirms recent earnings-call events and investor-review support pages | `[Disclosed]` | [events-and-presentations.html](/raw/company-ir/industrial-goods/waste-management/clean-harbors-inc/events-and-presentations.html) |

## Reconciliation notes

- The correct trailing-quarter set as of Monday, `2026-08-10`, is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- AnnualReports is current enough here to confirm the `2025` annual package, unlike some other companies where the AnnualReports page still lags one year behind.
- Direct SEC archive HTML requests were rate-limited from this shell during collection. The archive therefore uses the downloaded SEC submissions JSON plus the Clean Harbors IR filing-detail pages and the IR-hosted mirrored filing HTML pages as the local filing chain.
- This is sufficient for packetization because the mirrored filing pages preserve the filed `10-K` and `10-Q` content while the accession references remain documented in the IR filing-detail pages and submissions JSON.

## Missing evidence

- No standalone official earnings-call transcript artifacts were collected for Q4 `2025`, Q1 `2026`, or Q2 `2026`.
