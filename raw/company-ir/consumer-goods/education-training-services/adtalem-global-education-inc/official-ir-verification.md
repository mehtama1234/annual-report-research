# Official IR Verification

Date collected: 2026-08-10

## IR pages used

- Investor home: https://investors.adtalem.com/
- Current investor home redirect: https://investors.covista.com/overview/default.aspx
- Quarterly results page: https://investors.covista.com/financials/quarterly-results/default.aspx
- Financial news page: https://investors.covista.com/press-releases/default.aspx
- Q4 FY2026 press-release PDF: https://s21.q4cdn.com/400572492/files/doc_earnings/2026/q4/earnings-result/PR-4Q26.pdf

## Quarter chain confirmed as of 2026-08-10

- Q4 and full-year FY2026 results released `2026-08-06`
- Q3 FY2026 results released `2026-05-07`
- Q2 FY2026 results released `2026-01-28`

## Notes

- The investor-relations site is now branded `Covista` after the `2026-02-05` name change.
- Direct local `curl` collection of the main IR pages hit Cloudflare protection in this environment, so the saved `ir-home.html` artifact is only a challenge page.
- Web access still confirmed the live investor homepage and its quarter-results links, including the current Q4 FY2026 press-release PDF.
- Because the IR site blocked most local HTML collection, the authoritative locally saved quarter narratives in this pass come from the SEC `8-K` exhibit press releases.

## Local evidence

- [ir-home.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/consumer-goods/education-training-services/adtalem-global-education-inc/ir-home.html)
- [2026-fq4-press-release.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/consumer-goods/education-training-services/adtalem-global-education-inc/2026-fq4-press-release.pdf)
