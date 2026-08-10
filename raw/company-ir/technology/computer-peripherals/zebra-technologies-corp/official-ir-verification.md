# Zebra Technologies Corp. Official IR Verification

Date verified: 2026-08-10

- Investor relations home: https://investors.zebra.com/overview/default.aspx
- Annual reports page: https://investors.zebra.com/financials/annual-reports/default.aspx
- Financial summary page: https://investors.zebra.com/financials/financial-summary/default.aspx
- SEC filings page: https://investors.zebra.com/financials/sec-filings/default.aspx
- Events page: https://investors.zebra.com/news-and-events/events/

Direct-capture observations:

- The official investor-relations overview page identifies Zebra as a provider of connected frontline, asset-visibility, and automation solutions and shows the latest news item `Zebra Technologies Announces Second Quarter 2026 Results` dated `2026-08-04`.
- The annual-reports page exposes a `2025 Annual Report` PDF entry.
- The financial-summary page exposes the correct latest-three-reported-period chain as of Monday, `2026-08-10`:
  - `Q2 2026`
  - `Q1 2026`
  - `Q4 2025`
- The events page shows the `2Q 2026 Zebra Technologies Earnings Release Conference Call` dated `August 4, 2026` and confirms the company had not yet reported `Q3 2026` as of `2026-08-10`.

Environment note:

- Direct shell retrieval of Zebra's official investor-relations HTML pages returned `429` rate limiting in this environment.
- The source chain remains usable because browser-access verification cleanly resolved the official URLs and exposed the page-level annual-report and quarter sequence.
- This packet therefore stores URL-verification notes plus SEC-hosted annual and quarter artifacts locally rather than locally downloaded official IR HTML pages.

SEC applicability:

- Zebra is a U.S. SEC filer, so the authoritative annual and quarter artifact chain for this packet is preserved locally through the filed `ARS`, `10-K`, `10-Q`, and related `8-K` wrappers.
