# Comcast Corporation Official IR Verification

Date: 2026-08-10

Official IR surfaces verified:

- financials hub: `https://www.cmcsa.com/financials`
- earnings index: `https://www.cmcsa.com/financials/earnings`
- Q4 2025 release page: `https://www.cmcsa.com/news-releases/news-release-details/comcast-reports-4th-quarter-2025-results`
- Q1 2026 release page: `https://www.cmcsa.com/news-releases/news-release-details/comcast-reports-1st-quarter-2026-results`
- Q2 2026 release page: `https://www.cmcsa.com/news-releases/news-release-details/comcast-reports-2nd-quarter-2026-results`

Annual-report IR surfaces verified:

- The financials hub shows a `2025 Annual Review` module with links for:
  - `Letter to Shareholders`
  - `Year in Review`
  - `Annual Report on Form 10-K`

Collection note:

- Direct shell fetches of Comcast IR navigation pages were unreliable in this environment and repeatedly stalled before returning usable HTML.
- Because of that, the saved evidence chain for Comcast leans on:
  - AnnualReports for archive confirmation and annual-report PDF preservation
  - SEC submissions JSON for filing sequence confirmation
  - SEC `10-K`, `10-Q`, and `8-K` filings for filed evidence
  - SEC-hosted `99.1` earnings-release exhibits for the full quarter narrative that mirrors the official IR releases

Working conclusion:

- Comcast has a clean official IR chain for the target annual and quarter window.
- The archive has enough authoritative support to packetize Comcast even without saved local IR HTML pages.
