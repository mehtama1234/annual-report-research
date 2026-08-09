# Costco Wholesale Corporation Official IR Verification

Date checked: 2026-08-09

Investor relations home:

- https://investor.costco.com/overview/default.aspx

Verified from Costco live investor pages and current search index coverage:

- Annual Reports and Proxy Statements page exposes:
  - `2025 Annual Report`
- Investor news / events coverage exposes:
  - `Q1 2026` operating results dated `2025-12-11`
  - `Q2 2026` operating results dated `2026-03-05`
  - `Q3 2026` operating results dated `2026-05-28`

Official URLs verified:

- Annual reports page:
  - https://investor.costco.com/financials/annual-reports-and-proxy-statements/default.aspx
- SEC filings page:
  - https://investor.costco.com/financials/sec-filings/default.aspx
- Events and presentations page:
  - https://investor.costco.com/events-and-presentations/default.aspx
- Q1 2026 release page:
  - https://investor.costco.com/news/news-details/2025/Costco-Wholesale-Corporation-Reports-First-Quarter-Fiscal-Year-2026-Operating-Results/default.aspx
- Q2 2026 release page:
  - https://investor.costco.com/news/news-details/2026/Costco-Wholesale-Corporation-Reports-Second-Quarter-and-Year-to-Date-Operating-Results-for-Fiscal-2026-and-February-Sales-Results/default.aspx
- Q3 2026 release page:
  - https://investor.costco.com/news/news-details/2026/Costco-Wholesale-Corporation-Reports-Third-Quarter-and-Year-To-Date-Operating-Results-For-Fiscal-2026/default.aspx

Collection note:

- Direct scripted fetches of the live Costco investor-relations HTML pages from this environment returned Cloudflare challenge pages rather than the underlying content.
- The `2025` annual report PDF was still collected locally from Costco's cloudfront-backed investor-relations asset host.
- The quarter press-release artifacts in this packet were collected through the matching SEC-hosted Exhibit `99.1` filings, which preserve the company-issued release text even when the live investor-relations HTML is challenge-gated.

Interpretation:

- Costco has a current and internally consistent official IR chain for the fiscal `2025` annual package and the last three reported quarters in scope as of `2026-08-09`.
- The live IR site is current, but not fully script-friendly from this environment, so the archive relies on a mix of official PDF capture and SEC-hosted company exhibits.
