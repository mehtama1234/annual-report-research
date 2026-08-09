# Spotify Technology S.A. Official IR Verification

Date checked: 2026-08-09

Investor relations home: https://investors.spotify.com/overview/default.aspx

Verified on the live IR stack:

- Financials exposes:
  - `Q2 2026 Update`
  - `Q1 2026 Update`
  - `Q4 2025 Update`
  - annual reporting navigation that is more current than AnnualReports.com
- Search and page snippets from the live investor site indicate:
  - the latest reported quarter is `Q2 2026`
  - shareholder-update materials are available for `Q2 2026`, `Q1 2026`, and `Q4 2025`
  - annual-report navigation includes the `2025` reporting year

Capture notes:

- Direct fetches of ordinary investor-site HTML pages returned `429` rate limiting in the shell environment on `2026-08-09`.
- Direct CDN fetches of the official shareholder-update PDFs succeeded for:
  - `Q4 2025`
  - `Q1 2026`
  - `Q2 2026`
- The `2025` annual-report PDF filename on Spotify's CDN could not be resolved directly during this collection pass, so the annual evidence chain relies on the official-site verification note plus the filed `2025` `20-F`.

Interpretation:

- Spotify has a current and internally consistent official IR chain for the `2025` annual reporting year and the last three reported quarters in scope as of `2026-08-09`.
- The official IR stack is more current than AnnualReports.com for Spotify and is enough to verify the quarter-update cadence even where shell access to the site itself is rate-limited.
