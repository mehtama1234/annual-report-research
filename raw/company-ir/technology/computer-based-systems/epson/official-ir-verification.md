# Epson Official IR Verification

Date verified: 2026-08-10

- Investor relations home: https://corporate.epson/en/investors/
- Annual report page: https://corporate.epson/en/investors/publications/annual-report.html
- Integrated report page: https://corporate.epson/en/investors/publications/integrated-report.html
- Financial results materials page: https://corporate.epson/en/investors/publications/financial-reports/
- 2025 annual report PDF: https://corporate.epson/en/investors/publications/pdf/ar2025.pdf
- 2025 integrated report PDF: https://corporate.epson/en/investors/publications/pdf/integrated-report/epson_ir2025_all_e.pdf
- Q1 `2026` results PDF: https://corporate.epson/en/investors/publications/financial-reports/2026/pdf/results_2026_1q_e.pdf
- FY `2025` / Q4 `2025` results PDF: https://corporate.epson/en/investors/publications/financial-reports/2025/pdf/results_2025_full_e.pdf
- Q3 `2025` / nine months ended `2025-12-31` results PDF: https://corporate.epson/en/investors/publications/financial-reports/2025/pdf/results_2025_3q_e.pdf

Direct-capture observations:

- The official investor-relations home page shows `Integrated Report 2026`, a latest-results block for the `Three Months ended June 30, 2026`, and navigation to `Annual Report` and `Financial Results Materials`.
- The annual-report page exposes `Annual Report 2026` plus an archive entry for `Annual Report 2025 (PDF, 5.8MB)`.
- The financial-results page exposes the correct latest-three-reported-period chain as of Monday, `2026-08-10`:
  - `Three Months ended June 30, 2026`
  - `Fiscal Year ended March 31, 2026`
  - `Nine Months ended December 31, 2025`

Environment note:

- Direct shell retrieval of Epson's official HTML pages and PDFs returned `403` in this environment even when using standard browser-like headers.
- The source chain remains usable because the browser-access path cleanly resolved the official URLs and exposed the content for manual verification.
- This packet therefore stores browser-captured verification and extract notes locally instead of locally downloaded official PDF binaries.

SEC applicability:

- Epson is handled here as a Japan-listed issuer using official IR materials as the authoritative chain.
- A separate SEC artifact set is not part of the core evidence chain for this packet.
