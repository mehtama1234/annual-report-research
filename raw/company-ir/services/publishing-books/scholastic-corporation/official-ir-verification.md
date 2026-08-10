# Official IR Verification

Date baseline: 2026-08-10

## Investor-relations sources

- IR root: https://investor.scholastic.com/
- Annual reports page: https://investor.scholastic.com/financial-information/annual-reports
- Quarterly results page: https://investor.scholastic.com/financial-information/quarterly-results
- Events and presentations page: https://investor.scholastic.com/news-events/events-and-presentations

## Local collection result

- The annual-reports page was captured successfully and locally confirms:
  - `2025 Annual Report` at `/static-files/79cb81e9-a5b8-41de-8c79-554c1b0bcaab`
  - `2026 Annual Report` at `/static-files/790c46e3-2d5e-4ea5-ad3e-ca1edb8a2933`
- The quarterly-results page was captured successfully and locally confirms the in-scope quarter chain:
  - FY2026 Q4 release path `/news-releases/news-release-details/scholastic-reports-fourth-quarter-and-fiscal-2026-results`
  - FY2026 Q4 presentation `/static-files/e2531bb5-6d43-4433-90ea-bbdba24b7b0e`
  - FY2026 Q3 release path `/news-releases/news-release-details/scholastic-reports-fiscal-2026-third-quarter-results`
  - FY2026 Q3 presentation `/static-files/4b410c75-45cb-4fd8-ae31-32a673142628`
  - FY2026 Q2 release path `/news-releases/news-release-details/scholastic-reports-fiscal-2026-second-quarter-results`
  - FY2026 Q2 presentation `/static-files/367352fa-76a9-40b7-968d-a679c2f3ca00`
- The events-and-presentations and investor-home pages were captured successfully and locally confirm the reporting dates:
  - FY2026 Q2 results on `2025-12-18`
  - FY2026 Q3 results on `2026-03-19`
  - FY2026 Q4 / FY2026 results on `2026-07-23`

## Saved official artifacts

- `investor-home.html`
- `events-and-presentations.html`
- `annual-reports.html`
- `quarterly-results.html`

## Research use

- Treat the captured IR pages as authoritative confirmation that the company-hosted annual-report and quarter-result chain exists for the required evidence window.
- Use SEC as the authoritative saved chain for the `2025` Form `10-K`, the in-scope FY2026 quarter wrappers, the linked Exhibit `99.1` earnings releases, and the FY2026 `10-K` filed after the latest quarter.
