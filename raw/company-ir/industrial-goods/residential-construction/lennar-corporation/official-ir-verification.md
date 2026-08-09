# Official investor-relations verification for Lennar Corporation

Verified on: 2026-08-09

Primary investor-relations pages:

- Overview: https://investors.lennar.com/
- Annual reports and proxy statements: https://investors.lennar.com/financials/annual-reports-and-proxy-statements
- Earnings: https://investors.lennar.com/earnings
- Press releases 2026: https://investors.lennar.com/press-releases/2026

Key direct file and release URLs collected:

- Annual report PDF:
  - https://investors.lennar.com/~/media/Files/L/Lennar-IR-V3/documents/annual-reports/annual-report-2025.pdf
- Q4 2025:
  - Earnings release page: https://investors.lennar.com/press-releases/2025/12-16-2025-213022894
  - Earnings call transcript PDF: https://investors.lennar.com/~/media/Files/L/Lennar-IR-V3/reports-and-presentations/len-q4-25-earnings-call-transcript.pdf
  - Form `10-K` PDF: https://investors.lennar.com/~/media/Files/L/Lennar-IR-V3/documents/earnings-releases/len-4q25-10-k.pdf
- Q1 2026:
  - Earnings release page: https://investors.lennar.com/press-releases/2026/03-12-2026-203055658
  - Earnings call transcript PDF: https://investors.lennar.com/~/media/Files/L/Lennar-IR-V3/reports-and-presentations/q1-2026-len-earnings-call-transcript.pdf
  - Form `10-Q` PDF: https://investors.lennar.com/~/media/Files/L/Lennar-IR-V3/documents/earnings-releases/len-1q26-10-q.pdf
- Q2 2026:
  - Earnings release page: https://investors.lennar.com/press-releases/2026/06-11-2026-214520364
  - Earnings call transcript PDF: https://investors.lennar.com/~/media/Files/L/Lennar-IR-V3/reports-and-presentations/q2-26-len-earnings-call-transcript.pdf
  - Form `10-Q` PDF: https://investors.lennar.com/~/media/Files/L/Lennar-IR-V3/documents/earnings-releases/len-2q26-10-q.pdf

Verification notes:

- The AnnualReports page lagged at `2024`, but Lennar's official annual-reports page exposed the `2025` annual report PDF on `2026-08-09`.
- The official earnings page exposed the in-scope `Q4 2025`, `Q1 2026`, and `Q2 2026` package, including earnings releases, transcript PDFs, and `10-K` / `10-Q` PDFs.
- The official `Q1 2026` release page needed a corrected direct press-release URL. The initially captured page path resolved to a Lennar error page and was replaced with the valid release URL above.
- SEC submissions JSON was collected successfully and confirms the filing sequence, filer identity, and fiscal year-end.
- Direct SEC archive HTML fetches in this environment returned SEC bot-protection pages rather than valid filing bodies, so the IR-hosted `10-K` and `10-Q` PDFs are the usable local filing artifacts for this packet.
