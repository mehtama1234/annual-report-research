# Official IR Verification

Date checked: 2026-08-09

- Investor relations root: `https://investor.atmeta.com/home/default.aspx`
- Quarterly earnings section: `https://investor.atmeta.com/financials/`
- Press release detail pages verified through live search results:
  - `https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Second-Quarter-2026-Results/default.aspx`
  - `https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-First-Quarter-2026-Results/default.aspx`
  - `https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx`

## Collection note

- Direct scripted fetches of the main Meta IR HTML pages were blocked by Cloudflare in this environment on `2026-08-09`.
- The official IR artifact chain was still recoverable through Meta-hosted CDN files referenced by the investor site:
  - `2025-annual-report.pdf`
  - `2025-q4-results-release.pdf`
  - `2025-q4-prepared-remarks.pdf`
  - `2025-q4-follow-up-call-transcript.pdf`
  - `2026-q1-results-release.pdf`
  - `2026-q1-earnings-presentation.pdf`
  - `2026-q1-prepared-remarks.pdf`
  - `2026-q1-follow-up-call-transcript.pdf`
  - `2026-q2-results-release.pdf`
  - `2026-q2-earnings-presentation.pdf`
  - `2026-q2-prepared-remarks.pdf`
  - `2026-q2-follow-up-call-transcript.pdf`

## Why this matters

- Meta now has an official annual-report artifact plus quarter-level company materials for the full target window even though the main IR HTML pages were not directly collectible in this environment.
