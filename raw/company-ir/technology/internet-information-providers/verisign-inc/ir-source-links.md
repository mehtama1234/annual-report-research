# VeriSign IR source links

Date checked: 2026-08-10

## Core IR pages

- Investor home: https://investor.verisign.com/
- Events archive: https://investor.verisign.com/events.cfm

## In-scope annual and quarter chain

- Investor home page capture:
  - https://investor.verisign.com/
- Q1 2026 earnings release page:
  - https://investor.verisign.com/news-releases/news-release-details/verisign-reports-first-quarter-2026-results
- Q2 2026 earnings release page:
  - https://investor.verisign.com/news-releases/news-release-details/verisign-reports-second-quarter-2026-results
- Q2 2026 `.web` delegation release page:
  - https://investor.verisign.com/news-releases/news-release-details/verisign-announces-delegation-web

## Collection notes

- The investor pages responded successfully over `HTTP/1.1` on Monday, `2026-08-10`, after earlier plain `curl` attempts had failed under `HTTP/2`.
- The official investor pages cleanly exposed the live `Q1 2026` and `Q2 2026` earnings-release chain and linked back to the events archive used for webcast access.
- The company-hosted pages were used as the official IR verification layer, while the detailed numeric archive remains SEC-first through the `2025` `10-K`, the `2026` `10-Q` filings, and the related quarter `8-K` earnings exhibits.
