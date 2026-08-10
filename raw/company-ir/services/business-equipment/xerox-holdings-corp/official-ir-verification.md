# Official IR Verification

Date baseline: 2026-08-10

## Investor relations endpoints collected

- IR root: https://investors.xerox.com/
- Annual reports page: https://investors.xerox.com/investor-materials/annual-reports
- SEC filings page: https://investors.xerox.com/investor-materials/sec-filings
- Earnings summary page: https://investors.xerox.com/earnings-summary

## Collected local artifacts

- `annual-reports-page-correct.html`
- `sec-filings-page-correct.html`
- `earnings-summary-page.html`
- `2025-annual-report.pdf`
- `2025-10k.pdf`
- `1q2026-10q.pdf`
- `2q2026-10q.pdf`
- `4q2025-earnings-release.pdf`
- `1q2026-earnings-release.pdf`
- `2q2026-earnings-release.pdf`
- `4q2025-transcript.pdf`

## Verification notes

- The first Xerox IR paths collected earlier in the session were incorrect and returned `404` pages; those were superseded by the corrected paths above.
- The corrected annual-reports page exposes the `2025` annual report PDF directly.
- The earnings-summary page exposes the required quarter chain for Q4 `2025`, Q1 `2026`, and Q2 `2026`, including earnings releases, transcripts, and IR-hosted `10-K` / `10-Q` PDFs.
- The SEC submissions JSON confirms the filing-date chain, but direct SEC filing HTML pulls were rate-limited in this environment with the message `Your Request Originates from an Undeclared Automated Tool`.
- For this local archive snapshot, Xerox IR serves as the authoritative saved content chain, and the SEC submissions JSON serves as the authoritative filing-sequence confirmation layer.
