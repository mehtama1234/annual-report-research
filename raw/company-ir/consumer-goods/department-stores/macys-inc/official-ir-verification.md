# Macy's, Inc. Official IR Verification

Date checked: 2026-08-10

Official investor-relations pages verified:

- Investor landing page: https://www.macysinc.com/investors/
- Annual reports page: https://www.macysinc.com/investors/financials/annual-reports-and-proxy-statements/default.aspx
- Quarterly results page: https://www.macysinc.com/investors/financials/quarterly-results/default.aspx
- Presentations page: https://www.macysinc.com/investors/events-presentations-and-investor-updates/Presentations/default.aspx

Verified annual-report chain:

- The official annual-reports page exposed `2025 Annual Report`.
- The local official annual-report artifact was collected directly from the `q4cdn` PDF URL:
  - https://s202.q4cdn.com/285121676/files/doc_financials/2025/ar/Macy-s-Inc-2025-Annual-Report.pdf

Verified quarter window in scope as of `2026-08-10`:

- `Q1 2026`
  - quarterly-results coverage exposed `Q1 2026`
  - official newsroom release URL verified:
    - https://www.macysinc.com/newsroom/news/news-details/2026/Macys-Inc--Reports-Strong-First-Quarter-2026-Results-and-Raises-Full-Year-Outlook/default.aspx
  - official release PDF collected locally:
    - https://s202.q4cdn.com/285121676/files/doc_financials/2026/q1/Macy-s-Inc-_1Q2026_Designed-Release.pdf
  - official presentation PDF collected locally:
    - https://s202.q4cdn.com/285121676/files/doc_financials/2026/q1/v2/1Q26-Presentation.pdf
- `Q4 2025`
  - quarterly-results coverage exposed `Q4 2025`
  - official newsroom release URL verified:
    - https://www.macysinc.com/newsroom/news/news-details/2026/Macys-Inc--and-Macys-Return-to-Annual-Comparable-Sales-Growth-Fourth-Quarter-and-Fiscal-Year-2025-Results-Exceed-Guidance/default.aspx
  - official presentation PDF collected locally:
    - https://s202.q4cdn.com/285121676/files/doc_financials/2025/q4/4Q25-Presentation-03-18-26.pdf
- `Q3 2025`
  - quarterly-results coverage exposed `Q3 2025`
  - official newsroom release URL verified:
    - https://www.macysinc.com/newsroom/news/news-details/2025/CORRECTING-and-REPLACING-Macys-Inc--Reports-Third-Quarter-2025-Results/default.aspx
  - official release PDF collected locally:
    - https://s202.q4cdn.com/285121676/files/doc_financials/2025/q3/3Q25-Earnings-Release-12-03-25.pdf
  - official presentation PDF collected locally:
    - https://s202.q4cdn.com/285121676/files/doc_financials/2025/q3/3Q25-Presentation-12-03-25.pdf

Collection issue:

- The live Macy's IR and newsroom pages are Cloudflare-protected in this shell environment.
- Direct shell fetches of the main IR HTML pages returned `Just a moment...` challenge pages or `429` responses.
- Because of that, the archive preserves the directly downloadable `q4cdn` annual-report, release, and presentation files plus the SEC filing chain, while this note records the verified official URLs and quarter sequence.

Timing correction:

- As of Monday, August 10, 2026, `Q2 2026` had not yet been reported in the verified Macy's official IR and SEC chain used for this packet.
- The correct latest-three-quarter window is therefore `Q1 2026`, `Q4 2025`, and `Q3 2025`.
