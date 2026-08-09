# Walt Disney Co. Official IR Verification

Date checked: 2026-08-09

Investor relations home: https://investors.thewaltdisneycompany.com/overview/default.aspx

Verified on the live IR stack:

- Annual Reports exposes:
  - `2025` annual report PDF
- Quarterly Results exposes:
  - latest quarter results for `Q3 2026`
  - shareholder letter
  - webcast
  - financial reconciliations
  - financial tables
- Events and Presentations exposes:
  - `Q2 2026` earnings webcast page with shareholder letter, `10-Q` report, financial reconciliations, transcript, and earnings recap links
  - `Q3 2026` earnings webcast page with shareholder letter and webcast links
- SEC Filings exposes:
  - `2026`
  - `2025`
  - current filing history consistent with the local SEC submissions index

Capture notes:

- The official `2025` annual report PDF was captured successfully.
- The `2026 Q1` executive commentary PDF was captured successfully.
- Multiple direct Disney investor-site requests returned rate limiting or challenge behavior in the shell environment, so not every IR artifact was directly retrievable from the same path.
- The locally saved files named `2026-q2-executive-commentary.pdf`, `2026-q2-shareholder-letter.pdf`, `2026-q3-executive-commentary.pdf`, and `2026-q3-shareholder-letter.pdf` were invalid HTML placeholders rather than PDFs and are excluded from the packet evidence chain.

Interpretation:

- Disney has a current and internally consistent official IR chain for the `2025` annual package and the last three reported quarters in scope as of `2026-08-09`.
- The official IR stack is more current than AnnualReports.com for Disney and is required to bridge the archive from the lagging aggregator view to the actual `2025` and `2026` reporting set.
