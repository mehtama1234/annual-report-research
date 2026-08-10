# The Kraft Heinz Company SEC Access Note

Date baseline: 2026-08-10

## Local SEC evidence saved

- [submissions-cik0001637459.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/food-major-diversified/the-kraft-heinz-company/submissions-cik0001637459.json)

The submissions index confirms:

- legal name: `Kraft Heinz Co`
- ticker: `KHC`
- exchange: `Nasdaq`
- SEC SIC description: `Canned, Frozen & Preservd Fruit, Veg & Food Specialties`
- fiscal year-end: `1226`

## Filing chain reconciled from the submissions index

- `2025-10-K` filed `2026-02-12`:
  - accession `0001637459-26-000009`
  - primary document `khc-20251227.htm`
- `Q4 2025` earnings `8-K` filed `2026-02-11`:
  - accession `0001637459-26-000006`
  - primary document `khc-20260211.htm`
- `Q1 2026` `10-Q` filed `2026-05-06`:
  - accession `0001637459-26-000022`
  - primary document `khc-20260328.htm`
- `Q1 2026` earnings `8-K` filed `2026-05-06`:
  - accession `0001637459-26-000020`
  - primary document `khc-20260506.htm`
- `Q2 2026` `10-Q` filed `2026-08-05`:
  - accession `0001637459-26-000054`
  - primary document `khc-20260627.htm`
- `Q2 2026` earnings `8-K` filed `2026-08-05`:
  - accession `0001637459-26-000052`
  - primary document `khc-20260805.htm`

## Retrieval limitation

- Repeated direct attempts from this shell environment to retrieve the SEC filing HTML and filing index JSON returned SEC anti-automation denial pages or `403` responses on `2026-08-10`, even after declaring a user agent and retrying with browser-style headers.
- Because of that, this local Kraft Heinz packet uses the saved SEC submissions index as the authoritative SEC reconciliation artifact, while the local filing content itself is represented through the official IR PDFs and transcripts rather than direct SEC filing binaries.
