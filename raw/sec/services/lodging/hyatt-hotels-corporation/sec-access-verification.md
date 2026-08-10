# Hyatt Hotels Corporation SEC Access Verification

Date checked: 2026-08-10

Primary SEC reference: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=H&owner=exclude&count=40

Saved chronology evidence:

- [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/lodging/hyatt-hotels-corporation/sec-submissions.json)

Confirmed filing chain from the saved submissions feed:

- `10-K` filed `2026-02-13` for fiscal year ended `2025-12-31` with primary document `h-20251231.htm`
- `ARS` filed `2026-04-02` for fiscal year ended `2025-12-31` with primary document `tm266889d4_ars.pdf`
- `10-Q` filed `2026-04-30` for quarter ended `2026-03-31` with primary document `h-20260331.htm`
- `8-K` filed `2026-04-30` tied to the first-quarter update with primary document `h-20260430.htm`
- `10-Q` filed `2026-07-30` for quarter ended `2026-06-30` with primary document `h-20260630.htm`
- `8-K` filed `2026-07-30` tied to the second-quarter update with primary document `h-20260730.htm`
- `8-K` filed `2026-02-12` tied to the fourth-quarter and full-year 2025 update with primary document `h-20260212.htm`

Access notes:

- Direct SEC archive fetches attempted from this shell returned `403`, so standalone filing HTML was not captured successfully for Hyatt in this workspace.
- Placeholder `.download` files and matching `.error.txt` files document those failed direct-access attempts.
- The saved submissions feed is still authoritative enough to verify the annual and quarter chronology and to confirm the presence of an SEC-hosted annual report artifact (`ARS`) for fiscal `2025`.
