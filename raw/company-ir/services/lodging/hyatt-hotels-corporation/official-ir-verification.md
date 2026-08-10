# Hyatt Hotels Corporation Official IR Verification

Date checked: 2026-08-10

Investor relations home: https://investors.hyatt.com/overview/default.aspx

Verified on the official IR stack:

- Annual Reports page exposes `2025 Annual Report`.
- Quarterly and event pages expose the trailing quarter chain in scope as of `2026-08-10`:
  - `Q2 2026`
  - `Q1 2026`
  - `Q4 2025`
- Recent investor-home content confirms the latest reported quarter is `Q2 2026`.

Saved official artifacts collected locally:

- [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/lodging/hyatt-hotels-corporation/2025-annual-report.pdf)
- [2026-q2-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/lodging/hyatt-hotels-corporation/2026-q2-earnings-release.pdf)
- [2026-q1-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/lodging/hyatt-hotels-corporation/2026-q1-earnings-release.pdf)
- [2025-q4-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/lodging/hyatt-hotels-corporation/2025-q4-earnings-release.pdf)

Verified live official IR URLs:

- Annual Reports:
  - https://investors.hyatt.com/financials/annual-reports/default.aspx
- Q2 2026 earnings call / materials:
  - https://investors.hyatt.com/events-and-presentations/event-details/2026/Hyatt-Second-Quarter-2026-Earnings-Call/default.aspx
- Q1 2026 earnings call / materials:
  - https://investors.hyatt.com/events-and-presentations/event-details/2026/Hyatt-First-Quarter-2026-Earnings-Call/default.aspx
- Q4 2025 earnings call / materials:
  - https://investors.hyatt.com/events-and-presentations/event-details/2026/Hyatt-Fourth-Quarter-2025-Earnings-Call/default.aspx

Capture notes:

- Earlier shell-side direct pulls of standard IR HTML routes returned rate-limited responses, leaving `.error.txt` files in this folder.
- Direct CDN downloads of the annual-report and quarter-release PDFs succeeded.

Interpretation:

- Hyatt has a coherent official annual and trailing-quarter chain for CLI 8 scope.
- The annual and quarter materials are strong enough to support the service-layer physical interface case this frontier needed: fee growth, room growth, loyalty, owner relationships, and asset-light brand expansion.
