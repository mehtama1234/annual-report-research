# Official IR Verification

Date baseline: 2026-08-10

## Investor relations endpoints used

- Annual reports page: https://investors.whirlpoolcorp.com/financial-information/annual-reports-and-proxy-statements/default.aspx
- Quarterly results page: https://investors.whirlpoolcorp.com/financial-information/quarterly-results/default.aspx
- Events and presentations page: https://investors.whirlpoolcorp.com/news-and-events/events-and-presentations/default.aspx
- Interactive annual-report host: https://ar.whirlpoolcorp.com/

## Verification notes

- The Whirlpool IR root page was Cloudflare-blocked in this local environment, but the annual-reports page, quarterly-results materials, and Q4 CDN-hosted documents were still reachable directly.
- The `2025` annual-reports page explicitly lists:
  - `2025 10-K`
  - `2025 Annual Report`
  - `2026 Proxy Statement`
- The quarter chain in scope is supported by Whirlpool IR-hosted materials for:
  - Q4 `2025`
  - Q1 `2026`
  - Q2 `2026`
- The local IR archive now includes the annual report, `10-K`, quarter earnings releases, key-stat PDFs, earnings presentations, supplemental-information packs, and available corrected transcripts for Q4 `2025`, Q1 `2026`, and Q2 `2026`.

## Collected local artifacts

- `annual-reports-page.html`
- `2025-annual-report.pdf`
- `2025-10k.pdf`
- `2025-q4-earnings-release.pdf`
- `2025-q4-key-stats.pdf`
- `2025-q4-supplemental-information.pdf`
- `2026-q1-key-stats.pdf`
- `2026-q1-earnings-presentation.pdf`
- `2026-q1-supplemental-information.pdf`
- `2026-q1-transcript.pdf`
- `2026-q2-earnings-release.pdf`
- `2026-q2-key-stats.pdf`
- `2026-q2-earnings-presentation.pdf`
- `2026-q2-supplemental-information.pdf`
- `2026-q2-transcript.pdf`

## Authority read

- Whirlpool IR is the authoritative saved content chain for the annual report and quarter materials.
- SEC filings and the SEC submissions index are the authoritative filing-date confirmation layer.
