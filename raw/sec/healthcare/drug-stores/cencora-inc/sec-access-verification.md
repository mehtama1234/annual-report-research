# Cencora SEC Access Verification

Date checked: 2026-08-10

Primary SEC reference: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=COR&owner=exclude&count=40

Saved chronology evidence:

- [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/drug-stores/cencora-inc/sec-submissions.json)

Confirmed filing chain from the saved submissions feed:

- `10-Q` filed `2026-08-05` for quarter ended `2026-06-30` with primary document `cor-20260630.htm`
- `8-K` filed `2026-08-05` tied to the latest reported quarter update with primary document `abc-20260805.htm`
- `10-Q` filed `2026-05-06` for quarter ended `2026-03-31` with primary document `cor-20260331.htm`
- `8-K` filed `2026-05-06` tied to the fiscal second-quarter update with primary document `abc-20260506.htm`
- `10-Q` filed `2026-02-04` for quarter ended `2025-12-31` with primary document `cor-20251231.htm`
- `8-K` filed `2026-02-10` tied to the fiscal first-quarter update with primary document `cor-20260210.htm`
- `ARS` filed `2026-01-22` for fiscal year ended `2025-09-30` with primary document `tm2533035d4_ars.pdf`
- `10-K` filed `2025-11-25` for fiscal year ended `2025-09-30` with primary document `cor-20250930.htm`

Access notes:

- Direct SEC archive fetches attempted from this shell returned access failures, so standalone filing HTML was not captured successfully for Cencora in this workspace.
- Placeholder `.download` files and matching `.error.txt` files document those failed direct-access attempts.
- The saved submissions feed is still authoritative enough to verify the annual and quarter chronology and align the official IR evidence to the correct reporting window.
