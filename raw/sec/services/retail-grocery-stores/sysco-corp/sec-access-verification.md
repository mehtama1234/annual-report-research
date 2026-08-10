# Sysco Corporation SEC Access Verification

Date checked: 2026-08-10

Primary SEC reference: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=SYY&owner=exclude&count=40

Saved chronology evidence:

- [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/retail-grocery-stores/sysco-corp/sec-submissions.json)

Confirmed filing chain from the saved submissions feed:

- `10-K` filed `2025-08-22` for fiscal year ended `2025-06-28` with primary document `syy-20250628.htm`
- `10-Q` filed `2025-10-29` for quarter ended `2025-09-27` with primary document `syy-20250927.htm`
- `10-Q` filed `2026-01-28` for quarter ended `2025-12-27` with primary document `syy-20251227.htm`
- `10-Q` filed `2026-04-29` for quarter ended `2026-03-28` with primary document `syy-20260328.htm`
- `8-K` filed `2026-08-04` tied to the latest reported quarter update with primary document `syy-20260804.htm`

Access notes:

- Direct SEC archive fetches attempted from this shell returned `403`, so standalone filing HTML was not captured successfully for Sysco in this workspace.
- Placeholder `.download` files and matching `.error.txt` files document those failed direct-access attempts.
- The saved SEC submissions JSON is still authoritative enough to verify the filing chronology and align the official IR materials to the correct annual and quarter window.
