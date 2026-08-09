# T. Rowe Price IR Source Links

Date verified: 2026-08-08

## Primary IR pages

- Investor relations home: https://investors.troweprice.com/
- Annual reports page: https://investors.troweprice.com/financials/annual-reports-proxy-statements
- Quarterly results page: https://investors.troweprice.com/financials/quarterly-results
- Q1 2026 earnings event page: https://investors.troweprice.com/events/event-details/q1-2026-trow-earnings
- Q4 2025 earnings event page: https://investors.troweprice.com/events/event-details/q4-2025-trow-earnings

## Verified direct asset URLs

- 2025 annual report PDF: https://investors.troweprice.com/static-files/7c2a040a-0872-4017-b25a-52c92b489983
- 2026 Q2 earnings release PDF: https://www.troweprice.com/content/dam/public/enterprise/press/2026/earnings-press-release-q2-2026.pdf
- 2026 Q2 earnings supplement PDF: https://investors.troweprice.com/static-files/91b69c99-d092-4187-94df-34c8fa7e6e38
- 2026 Q2 earnings transcript PDF: https://investors.troweprice.com/static-files/4732e9b0-5fef-4155-94e9-025779db4a11
- 2026 Q1 earnings release PDF: https://investors.troweprice.com/static-files/56801ab1-300c-40aa-963d-c5d290896598
- 2026 Q1 earnings supplement PDF: https://investors.troweprice.com/static-files/14a8ac90-6835-4eea-8970-b02b189fbc3c
- 2026 Q1 earnings transcript PDF: https://investors.troweprice.com/static-files/3ce1b3ea-9061-4520-a769-2f23055e2c60
- 2025 Q4 earnings release PDF: https://investors.troweprice.com/static-files/a772cd0c-8940-4b3b-a819-62813d689a4c
- 2025 Q4 earnings supplement PDF: https://investors.troweprice.com/static-files/4680d6d5-12bd-4d11-bd8b-b83a676b6b62
- 2025 Q4 earnings transcript PDF: https://investors.troweprice.com/static-files/758b6cfe-5a97-439d-9ac8-12adbce9b430

## Local collection status

- `2026-q2-earnings-release.pdf` downloaded successfully.
- The SEC filing chain for `2025` annual, `4Q25`, `1Q26`, and `2Q26` is saved locally under `raw/sec/...`.
- Several `investors.troweprice.com/static-files/...` assets were verified through browser search and page inspection but stalled or failed through local machine fetches during this pass, so they are logged here even where the binary artifact is not yet saved locally.
- The `2025` annual report PDF URL is verified above.
- Browser-side verification on `2026-08-09` confirms the file resolves as a `2025 Annual Report` PDF with `116` pages, and the IR page advertises the file size as `4.7 MB`.
- Repeated shell fetch attempts from this machine using `requests`, `curl`, `wget`, `http.client`, and Node `http2` either stalled after connect or failed with transport-level errors, so no valid local `2025-annual-report.pdf` artifact is saved yet.
- A local Playwright / Chromium browser pass on `2026-08-09` also failed from this machine: the annual-reports page and the direct `static-files` annual-report URL both returned `403 Access Denied` HTML from the edge rather than the PDF binary.
