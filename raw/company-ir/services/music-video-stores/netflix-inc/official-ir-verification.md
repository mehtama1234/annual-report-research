# Official IR Verification

Date checked: 2026-08-09

- Investor relations root: `https://ir.netflix.net/ir-overview/profile/default.aspx`
- Quarterly earnings section: `https://ir.netflix.net/financials/quarterly-earnings/default.aspx`
- Official annual report PDF verified:
  - `https://s22.q4cdn.com/959853165/files/doc_financials/2025/ar/99482238-46b2-4d0d-b292-40e6781bdf03.pdf`
- Official quarterly materials verified:
  - `https://s22.q4cdn.com/959853165/files/doc_financials/2025/q4/FINAL-Q4-25-Shareholder-Letter.pdf`
  - `https://s22.q4cdn.com/959853165/files/doc_financials/2025/q4/Netflix-Inc-_Earnings-Call_2026-01-20_English-1.pdf`
  - `https://s22.q4cdn.com/959853165/files/doc_financials/2026/q1/FINAL-Q1-26-Shareholder-Letter.pdf`
  - `https://s22.q4cdn.com/959853165/files/doc_financials/2026/q1/Netflix-Inc-_Earnings-Call_2026-04-16T00_00_00_English-1.pdf`
  - `https://s22.q4cdn.com/959853165/files/doc_financials/2026/q2/FINAL-Q2-26-Shareholder-Letter.pdf`
  - `https://s22.q4cdn.com/959853165/files/doc_financials/2026/q2/Netflix-Inc-_Earnings-Call_2026-07-16T00_00_00_English-1.pdf`

## Collection note

- Direct scripted fetches of the main Netflix IR HTML pages were blocked by Cloudflare in this environment on `2026-08-09`.
- The official IR artifact chain was still recoverable through Netflix-hosted static files referenced by the investor site, and those files are saved locally for the annual report plus the `Q4 2025` through `Q2 2026` quarter window.

## Why this matters

- Netflix now has an official annual-report artifact plus quarter-level company materials for the full target window even though the main IR HTML pages were not directly collectible from the shell.
