# Brown-Forman SEC Access Note

Date verified: 2026-08-10

## What worked

- The official SEC submissions index was retrievable with a custom user agent:
  - [submissions-cik0000014693.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/beverages-wineries-distillers/brown-forman/submissions-cik0000014693.json)
- That JSON verified:
  - legal name: `BROWN FORMAN CORP`
  - tickers: `BF-A`, `BF-B`
  - fiscal year-end: `0430`
  - headquarters: Louisville, Kentucky

## Relevant accession chain

- `2025-06-13` `10-K` accession `0000014693-25-000062` primary document `bfb-20250430.htm`
- `2025-06-05` `8-K` accession `0000014693-25-000055` primary document `bfb-20250605.htm`
- `2025-12-04` `10-Q` accession `0000014693-25-000112` primary document `bfb-20251031.htm`
- `2025-12-04` `8-K` accession `0000014693-25-000107` primary document `bfb-20251204.htm`
- `2026-03-04` `10-Q` accession `0000014693-26-000010` primary document `bfb-20260131.htm`
- `2026-03-04` `8-K` accession `0000014693-26-000005` primary document `bfb-20260304.htm`
- `2026-06-12` `10-K` accession `0000014693-26-000024` primary document `bfb-20260430.htm`
- `2026-06-04` `8-K` accession `0000014693-26-000018` primary document `bfb-20260604.htm`

## What did not work cleanly

- The saved local SEC archive files [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/beverages-wineries-distillers/brown-forman/2025-10k.html), [2025-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/beverages-wineries-distillers/brown-forman/2025-q2-10q.html), [2026-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/beverages-wineries-distillers/brown-forman/2026-q3-10q.html), and [2026-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/consumer-goods/beverages-wineries-distillers/brown-forman/2026-10k.html) are SEC automated-access block pages rather than real filing content.
- The supposed annual-report file [2025-annual-report-sec-ars.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/consumer-goods/beverages-wineries-distillers/brown-forman/2025-annual-report-sec-ars.pdf) is also HTML block content, not a usable PDF.
- Any locally saved exhibit HTML files under this Brown-Forman SEC folder should be treated as suspect unless separately validated, because the same retrieval path produced automated-access block pages for the core filing artifacts.

## Practical conclusion

- Use the submissions JSON as the authoritative filing map.
- Use the AnnualReports archived `2025` annual report and the verified official IR quarter pages for the actual packet analysis.
- Treat the direct SEC artifact collection for Brown-Forman as incomplete in this environment.
