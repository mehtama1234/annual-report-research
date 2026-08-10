# Generac IR source links

Date checked: 2026-08-10

## Core IR pages

- Investor home: https://investors.generac.com/
- SEC filings page: https://investors.generac.com/financial-information/sec-filings
- Annual reports page: https://investors.generac.com/financial-information/annual-reports-and-proxy
- News releases page: https://investors.generac.com/news-events/press-releases

## In-scope annual and quarter chain

- 2025 annual reports page:
  - https://investors.generac.com/financial-information/annual-reports-and-proxy
- 2025 annual report PDF:
  - https://investors.generac.com/static-files/3cea6a42-660e-4a8c-8704-c0fd04e55551
- 2025 10-K filing detail page:
  - https://investors.generac.com/financial-information/sec-filings?items_per_page=10&page=0
  - local filing-page capture confirms filing date `2026-02-18`, document date `2025-12-31`, and PDF path `/static-files/8ae3e2f2-e3b7-48ee-bd54-c2220a70fb4b`

- Q4 2025 earnings-release filing detail page:
  - https://investors.generac.com/financial-information/sec-filings?items_per_page=10&page=0
  - local filing-page capture confirms filing date `2026-02-11`, form `8-K`, and PDF path `/static-files/5003d7c1-1816-48f5-a532-a2c2d30ad1a2`
- Q4 2025 earnings release PDF:
  - https://investors.generac.com/static-files/5003d7c1-1816-48f5-a532-a2c2d30ad1a2

- Q1 2026 10-Q filing detail page:
  - https://investors.generac.com/financial-information/sec-filings?items_per_page=10&page=0
  - local filing-page capture confirms filing date `2026-05-05`, document date `2026-03-31`, and PDF path `/static-files/661c9b8e-14b7-4972-9a65-58f8008d591a`
- Q1 2026 earnings-release filing detail page:
  - https://investors.generac.com/financial-information/sec-filings?items_per_page=10&page=0
  - local filing-page capture confirms filing date `2026-04-29`, form `8-K`, and PDF path `/static-files/7f41e312-11fc-4d0a-82b6-b208e761cdcc`
- Q1 2026 earnings release PDF:
  - https://investors.generac.com/static-files/7f41e312-11fc-4d0a-82b6-b208e761cdcc

- Q2 2026 10-Q filing detail page:
  - https://investors.generac.com/financial-information/sec-filings?items_per_page=10&page=0
  - local filing-page capture confirms filing date `2026-08-04`, document date `2026-06-30`, and PDF path `/static-files/7ed2aadf-bbfb-418c-b2ae-be7af848bf79`
- Q2 2026 earnings-release filing detail page:
  - https://investors.generac.com/financial-information/sec-filings?items_per_page=10&page=0
  - local filing-page capture confirms filing date `2026-07-29`, form `8-K`, and PDF path `/static-files/c851dd53-ca1c-4197-a350-255d0f9c451e`
- Q2 2026 earnings release PDF:
  - https://investors.generac.com/static-files/c851dd53-ca1c-4197-a350-255d0f9c451e

## Collection notes

- The company-hosted annual-reports page exposes the official `2025 Annual Report` PDF directly.
- The company-hosted SEC-filings pages were reliable for the annual plus trailing-three-quarter chain and were used to confirm form type, filing date, document date, and downloadable PDF paths.
- Direct SEC HTML fetches were not retained because the raw requests returned the SEC automated-tool block page during collection. The saved evidence set therefore uses company-hosted filing detail pages, locally saved filing PDFs, and the SEC submissions JSON as the authoritative chain.
