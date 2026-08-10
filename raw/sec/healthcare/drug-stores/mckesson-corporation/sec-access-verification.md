# McKesson Corporation SEC Access Verification

Date checked: 2026-08-10

Primary SEC reference: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=MCK&owner=exclude&count=40

Saved chronology evidence:

- [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/drug-stores/mckesson-corporation/sec-submissions.json)

Confirmed filing chain from the saved submissions feed:

- `10-Q` filed `2026-08-05` for quarter ended `2026-06-30` with primary document `mck-20260630.htm`
- `8-K` filed `2026-08-05` tied to the latest reported quarter update with primary document `mck-20260805.htm`
- `10-K` filed `2026-05-08` for fiscal year ended `2026-03-31` with primary document `mck-20260331.htm`
- `ARS` filed `2026-06-12` for fiscal year ended `2026-03-31` with primary document `mck-2026xars.pdf`
- `10-Q` filed `2026-02-04` for quarter ended `2025-12-31` with primary document `mck-20251231.htm`
- `8-K` filed `2026-02-04` tied to the fiscal third-quarter update with primary document `mck-20260204.htm`

Access notes:

- Direct SEC archive fetches attempted from this shell returned `403`, so standalone filing HTML was not captured successfully for McKesson in this workspace.
- Placeholder `.download` files and matching `.error.txt` files document those failed direct-access attempts.
- The saved submissions feed is still authoritative enough to verify the quarter chronology and align the official IR documents to the correct reporting window.
