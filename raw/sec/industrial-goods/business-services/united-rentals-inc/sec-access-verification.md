# United Rentals, Inc. SEC Access Verification

Date checked: 2026-08-10

Primary SEC reference: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=URI&owner=exclude&count=40

Saved chronology evidence:

- [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/business-services/united-rentals-inc/sec-submissions.json)

Confirmed filing chain from the saved submissions feed:

- `10-Q` filed `2025-10-22` for quarter ended `2025-09-30` with primary document `uri-20250930.htm`
- `10-K` filed `2026-01-28` for fiscal year ended `2025-12-31` with primary document `uri-20251231.htm`
- `ARS` filed `2026-03-25` for fiscal year ended `2025-12-31` with primary document `uri_ars_fye_2025.pdf`
- `10-Q` filed `2026-04-22` for quarter ended `2026-03-31` with primary document `uri-20260331.htm`
- `10-Q` filed `2026-07-22` for quarter ended `2026-06-30` with primary document `uri-20260630.htm`
- `8-K` filed `2026-07-22` tied to the latest reported quarter update with primary document `uri-20260722.htm`

Access notes:

- Direct SEC archive fetches attempted from this shell returned `403`, so standalone filing HTML was not captured successfully for United Rentals in this workspace.
- Placeholder `.download` files and matching `.error.txt` files document those failed direct-access attempts.
- The saved submissions feed is still authoritative enough to verify the annual and quarter chronology and to confirm the presence of an SEC-hosted annual report artifact (`ARS`) for fiscal `2025`.
