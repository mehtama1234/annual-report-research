# Official IR Verification

Date checked: 2026-08-09

Company checked: CF Industries Holdings, Inc.

Verified official source URLs:

- reports page: https://www.cfindustries.com/reports
- 2025 annual report PDF: https://www.cfindustries.com/globalassets/cf-industries/media/documents/reports/annual-reports/cf-industries-2025-annual-report.pdf
- Q4 2025 results release page: https://www.cfindustries.com/newsroom/2026/fy-2025-earnings
- Q1 2026 results release page: https://www.cfindustries.com/newsroom/2026/2026-q1-earnings
- Q2 2026 results release page: https://www.cfindustries.com/newsroom/2026/1h-2026-earnings
- Q4 2025 earnings presentation PDF: https://s203.q4cdn.com/145805377/files/doc_financials/2025/q4/4Q25-Earnings-Deck-vfinal140.pdf
- Q1 2026 earnings presentation PDF: https://s203.q4cdn.com/145805377/files/doc_financials/2026/q1/1Q26-Earnings-Deck-vfinal244.pdf
- Q2 2026 earnings presentation PDF: https://s203.q4cdn.com/145805377/files/doc_financials/2026/q2/2Q26-Earnings-Deck-vfinal213.pdf

Verified results:

- The official public reports page exposes the `2025` annual report.
- The official newsroom pages expose the in-scope trailing-quarter earnings releases:
  - `Q4 2025`
  - `Q1 2026`
  - `Q2 2026`
- The official presentation PDFs for all three in-scope quarters are saved locally.

Environment note:

- The `investor.cfindustries.com` event pages were browser-visible during collection but returned Cloudflare challenge pages to raw shell fetches from this environment.
- Because of that, the local archive for CF relies on:
  - the public `cfindustries.com` reports page
  - public `cfindustries.com` newsroom pages
  - public q4cdn presentation PDFs
  - SEC-hosted filing and exhibit artifacts

This is sufficient to support the company packet and quarter-by-quarter evidence chain.
