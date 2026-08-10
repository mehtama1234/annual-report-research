# W.W. Grainger, Inc. SEC Access Verification

Date checked: 2026-08-10

Primary SEC reference: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=GWW&owner=exclude&count=40

Saved chronology evidence:

- [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/industrial-equipment-components/ww-grainger-inc/sec-submissions.json)

Confirmed filing chain from the saved submissions feed:

- `10-K` filed `2026-02-19` for fiscal year ended `2025-12-31` with primary document `gww-20251231.htm`
- `ARS` filed `2026-03-10` for fiscal year ended `2025-12-31` with primary document `tm2529296d2_ars.pdf`
- `10-Q` filed `2026-05-07` for quarter ended `2026-03-31` with primary document `gww-20260331.htm`
- `10-Q` filed `2026-08-04` for quarter ended `2026-06-30` with primary document `gww-20260630.htm`
- `8-K` filed `2026-08-04` tied to the latest reported quarter update with primary document `gww-20260804.htm`
- `8-K` filed `2026-02-03` tied to the fourth-quarter and full-year 2025 update with primary document `gww-20260203.htm`

Access notes:

- Direct SEC archive fetches attempted from this shell returned `403`, so standalone filing HTML was not captured successfully for Grainger in this workspace.
- Placeholder `.download` files and matching `.error.txt` files document those failed direct-access attempts.
- The saved submissions feed is still authoritative enough to verify the annual and quarter chronology and to confirm the presence of an SEC-hosted annual report artifact (`ARS`) for fiscal `2025`.
