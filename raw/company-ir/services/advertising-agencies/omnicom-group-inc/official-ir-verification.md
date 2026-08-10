# Omnicom Group Inc. Official IR Verification

Date verified: 2026-08-10

- Investor relations home: https://investor.omc.com/
- Annual reports page: https://investor.omc.com/financials/annual-reports/default.aspx
- Quarterly results page: https://investor.omc.com/financials/quarterly-results/
- Events and presentations page: https://investor.omc.com/events-and-presentations/default.aspx

Browser-verified observations:

- The annual-reports page exposes the official `2025 Annual Report` PDF.
- The events-and-presentations stack exposes second-quarter `2026`, first-quarter `2026`, and fourth-quarter `2025` earnings-call materials.
- The IR stack is the authoritative official-company chain for annual-report and quarterly-results navigation even though the collected quarter-level local artifacts in this packet are SEC-hosted filings and exhibits.

Notes:

- Direct shell fetches of the main Omnicom IR HTML pages from this environment returned Cloudflare challenge pages, so the page stack above is treated as browser-verified official evidence rather than as a clean local HTML capture.
- The direct `q4cdn` annual-report PDF asset remained fetchable and is saved locally as [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/advertising-agencies/omnicom-group-inc/2025-annual-report.pdf).
