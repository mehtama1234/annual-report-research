# GoDaddy IR source links

Date checked: 2026-08-10

## Core IR pages

- Investor overview:
  - https://aboutus.godaddy.net/investor-relations/overview/default.aspx
- Investor financials:
  - https://aboutus.godaddy.net/investor-relations/financials/default.aspx
- Investor resources:
  - https://aboutus.godaddy.net/investor-relations/resources/default.aspx
- News releases:
  - https://aboutus.godaddy.net/newsroom/news-releases/default.aspx
- Legacy investor shell referenced in filings and releases:
  - https://investors.godaddy.net/

## In-scope annual and quarter chain

- Official 2025 annual report PDF:
  - https://s23.q4cdn.com/406380394/files/doc_financials/2025/ar/GoDaddy-2025-AR-FINAL.pdf
- Official investor overview page capture:
  - https://aboutus.godaddy.net/investor-relations/overview/default.aspx
- Official Q2 2026 earnings-release PDF URL verified from the investor overview page:
  - https://investors.godaddy.net/files/doc_financials/2026/q2/GDDY-Q2-2026-Earnings-Release.pdf

## Collection notes

- The official `aboutus.godaddy.net` investor overview page was directly captured from the shell on Monday, `2026-08-10`, and confirmed the live investor-navigation structure, the recent Q2 `2026` results link, and the company-stated scale markers for entrepreneurs and domain names.
- Direct shell fetches to `investors.godaddy.net` and later follow-up fetches to additional `aboutus.godaddy.net` investor pages returned `429` Cloudflare challenge responses in this environment, so the durable packet is grounded in:
  - the saved official overview HTML,
  - the saved official `2025` annual report PDF,
  - the browser-verified official Q2 `2026` earnings-release PDF URL,
  - and the full SEC annual and quarterly filing chain.
- The SEC-hosted `8-K` earnings exhibits were used as the stable local text source for `Q4 2025`, `Q1 2026`, and `Q2 2026` management commentary and operating metrics.
