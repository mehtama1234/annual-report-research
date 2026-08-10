# Levi Strauss & Co. Official IR Verification

Date checked: 2026-08-10

Official investor-relations pages verified:

- Investor landing page: https://investors.levistrauss.com/home/default.aspx
- Annual reports page: https://investors.levistrauss.com/financials/annual-reports/default.aspx
- Quarterly results page: https://investors.levistrauss.com/financials/quarterly-results/default.aspx
- Financial news page: https://investors.levistrauss.com/news/financial-news/default.aspx

Verified annual-report chain:

- The official annual-reports page exposed `2025 Annual Report`.
- The local official annual-report artifact was collected directly from the `q4cdn` PDF URL:
  - https://s23.q4cdn.com/172692177/files/doc_financials/2025/ar/449421_LEVI-STRAUSS_AR_PROOF_RC.pdf

Verified quarter window in scope as of `2026-08-10`:

- `Q2 2026`
  - quarterly-results coverage exposed `Q2 2026`
  - official financial-news release URL verified:
    - https://investors.levistrauss.com/news/financial-news/news-details/2026/Levi-Strauss--Co--Reports-Second-Quarter-Results/default.aspx
  - official release PDF collected locally:
    - https://s23.q4cdn.com/172692177/files/doc_financials/2026/q2/FINAL-Exhibit-99-1-2Q-2026-Press-Release_FINAL.pdf
- `Q1 2026`
  - quarterly-results coverage exposed `Q1 2026`
  - official financial-news release URL verified:
    - https://investors.levistrauss.com/news/financial-news/news-details/2026/Levi-Strauss--Co--Reports-First-Quarter-Results/default.aspx
  - official release PDF collected locally:
    - https://s23.q4cdn.com/172692177/files/doc_financials/2026/q1/Exhibit-99-1-1Q-2026-Press-Release_FINAL.pdf
- `Q4 2025`
  - quarterly-results coverage exposed `Q4 2025`
  - official financial-news release URL verified:
    - https://investors.levistrauss.com/news/financial-news/news-details/2026/Levi-Strauss--Co--Reports-Fourth-Quarter-Results/default.aspx
  - official release PDF collected locally:
    - https://s23.q4cdn.com/172692177/files/doc_financials/2025/q4/Exhibit-99-1-4Q-2025-Press-Release-wdesk.pdf

Collection issue:

- The live Levi Strauss investor-relations HTML pages returned `403` and `429` responses in this shell environment during direct fetch attempts.
- Because of that, the archive preserves the directly downloadable `q4cdn` annual-report and quarter-release PDFs plus the SEC filing chain, while this note records the verified official URLs and quarter sequence.

Timing confirmation:

- As of Monday, August 10, 2026, the correct latest-three-quarter window for Levi Strauss is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- `Q3 2025` is outside the latest-three-quarter window and is not part of this packet.
