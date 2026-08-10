# Official IR Verification

Date baseline: 2026-08-10

## Intended investor-relations source

- Investor relations root: https://investors.nytco.com/

## Local collection result

- Direct local fetch attempts to `https://investors.nytco.com/` returned HTTP `429` in this environment.
- Because of that rate-limit response, no reliable official IR HTML capture was saved locally for the annual-report page stack or quarterly-results page stack.

## Authoritative fallback used

- SEC submissions index: https://data.sec.gov/submissions/CIK0000071691.json
- `2025` Form `10-K` filed `2026-02-27`
- Q4 `2025` results `8-K` filed `2026-02-04`
- Q1 `2026` `10-Q` and earnings `8-K` filed `2026-05-06`
- Q2 `2026` `10-Q` and earnings `8-K` filed `2026-08-05`

## Research use

- Official company IR should be treated as the intended primary company source when accessible.
- In this local archive snapshot, SEC filings and SEC-hosted Exhibit `99.1` earnings releases are the authoritative saved chain because the official IR site rate-limited collection.
