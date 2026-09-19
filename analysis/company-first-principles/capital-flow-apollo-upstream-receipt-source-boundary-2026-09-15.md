# Apollo upstream-receipt source boundary

Research date: `2026-09-15`

The SEC companyfacts record for Apollo's Q2 2026 accession was searched for
accession-specific dividend, distribution, intercompany, affiliate, and
related cash-receipt facts. It exposes common and preferred dividend payments,
but no separately tagged upstream dividend receipt or intercompany cash receipt
that can be joined to Athene or another regulated subsidiary.

## What the search proves

- The accession-specific facts expose `$654M` of common dividends paid,
  `$729M` of common-stock repurchases paid, and `$49M` of preferred dividends
  paid in H1 2026.
- The search did not produce a separately tagged `dividends received`,
  `intercompany cash receipt`, or `Athene upstream distribution` fact for the
  accession.
- This is a source-availability boundary, not proof that no upstream transfer
  occurred. The next upgrade requires the detailed parent cash-flow note,
  subsidiary dividend schedule, intercompany elimination table, or regulatory
  dividend approval/receipt evidence.

## Primary source and reproducible test

[SEC companyfacts for Apollo](https://data.sec.gov/api/xbrl/companyfacts/CIK0001858681.json), filtered to accession `0001858681-26-000040` and facts whose labels/tags contain dividend, distribution, intercompany, affiliate, or receipt terms; corroborated against [Apollo Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1858681/000185868126000040/apo-20260630.htm).
