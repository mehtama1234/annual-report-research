# United Rentals, Inc. Official IR Verification

Date checked: 2026-08-10

Investor relations home: https://investors.unitedrentals.com/home/default.aspx

Verified on the official IR stack:

- Annual reports navigation exposes `2025 Annual Report`.
- Press releases on the official IR site expose the in-scope trailing quarter chain as of `2026-08-10`:
  - `United Rentals Announces Record Second Quarter Results and Raises Full-Year 2026 Guidance`
    - https://investors.unitedrentals.com/press-releases/press-releases-details/2026/United-Rentals-Announces-Record-Second-Quarter-Results-and-Raises-Full-Year-2026-Guidance/default.aspx
  - `United Rentals Announces Strong First Quarter Results and Raises Full-Year 2026 Guidance`
    - https://investors.unitedrentals.com/press-releases/press-releases-details/2026/United-Rentals-Announces-Strong-First-Quarter-Results-and-Raises-Full-Year-2026-Guidance/default.aspx
  - `United Rentals Announces Fourth Quarter and Full-Year 2025 Results, Introduces 2026 Outlook for Growth, and Announces Plan to Return Approximately $2 Billion to Shareholders in 2026`
    - https://investors.unitedrentals.com/press-releases/press-releases-details/2026/United-Rentals-Announces-Fourth-Quarter-and-Full-Year1-2025-Results-Introduces-2026-Outlook-for-Growth-and-Announces-Plan-to-Return-Approximately-2-Billion-to-Shareholders-in-2/default.aspx

Capture notes:

- Direct pulls of standard IR HTML routes from the shell returned `429` on `2026-08-10`, including:
  - annual-reports landing page
  - quarterly-results landing page
  - sec-filings landing page
- A saved local IR navigation page still confirmed the financial route structure for United Rentals.
- Direct CDN downloads succeeded for:
  - [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/business-services/united-rentals-inc/2025-annual-report.pdf)
  - [2026-q2-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/business-services/united-rentals-inc/2026-q2-earnings-release.pdf)

Interpretation:

- United Rentals has a coherent official annual and trailing-quarter chain for current scope, but part of that chain had to be preserved as verified live official URLs rather than raw page captures because of shell-side rate limiting.
- The official materials are strong enough to support a full CLI 8 company packet focused on rental access, fleet productivity, specialty growth, capital discipline, and customer operating dependence.
