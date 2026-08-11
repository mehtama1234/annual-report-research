# Next Steps

Date baseline: 2026-08-10

## Packet Inputs Used

- the active lane board and start-here operating files that define current lane selection and startup flow
- the repo-wide collection window of `2025` annual reports plus the latest three reported quarters as of `2026-08-10`
- the batch-design rule that favors coherent flagship-company sets over many shallow starts
- the folder, naming, and company-level collection conventions that keep packet outputs machine-parseable and reusable
- the bridge rule for using `ibis-industries` as a force-idea input rather than as a substitute for company-source verification

## Current operating stance

The repo is no longer in a vague pilot stage.
The current rule is to pursue coherent lanes end to end starting from:

- [START-HERE.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/START-HERE.md)
- [Active lane board](/home/manishmehta/ui-projects/annual-report-research-new-lanes/notes/active-lane-board-2026-08-10.md)

Each run should aim to finish a coherent `3` to `4` company flagship batch inside a lane, not spray work across dozens of shallow starts.

## Collection window

Collection window for this phase:

- annual reports: `2025`
- quarterlies: latest three reported quarters available as of `2026-08-10`
- in many cases: `2026 Q2`, `2026 Q1`, and `2025 Q4`

## Priority lane families

Suggested lane families for current work:

1. Connectivity / telecom / technical infrastructure
2. Capital structures / property / conglomerates
3. Healthcare frontier and recurring-care systems
4. Recreation / lifestyle / participation demand

## Batch design rule

Choose `3` to `4` companies that together produce a real comparison set.

Prefer a mix such as:

1. one demand gateway, distribution owner, or network owner
2. one capital-intensive infrastructure or asset owner
3. one enabling tool, workflow, measurement, or toll-collector business
4. one contrast case with a meaningfully different monetization model or balance-sheet structure

## Collection sequence per company

1. Create raw folder path by sector / industry / company
2. Save or verify the company profile from AnnualReports.com for taxonomy and archive confirmation
3. Save the `2025` annual report
4. Save the corresponding `2025` annual filing
5. Save the last three quarterly earnings releases in scope
6. Save the last three quarterly filings in scope
7. Save latest call transcript if available
8. Fill `templates/company-packet.md`
9. Write the thematic interpretation for the company
10. Update shared indexes only at the end of the coherent batch, or leave the batch ready for integration

## Raw folder convention

```text
raw/
  annualreports/<sector>/<industry>/<company>/
  company-ir/<sector>/<industry>/<company>/
  sec/<sector>/<industry>/<company>/
  earnings-calls/<sector>/<industry>/<company>/
```

## Naming convention

- Use lowercase kebab-case for sector, industry, and company folder names.
- Prefix dated files with the reporting period when possible.
- Prefer `2026-q2-earnings-release.pdf` over generic filenames.

## Reuse from `ibis-industries`

- Use `ibis-industries` as an input layer for cross-sector force ideas, not as a direct file-source replacement.
- Prefer annual-report and earnings evidence in this repo when making company-level claims.
- Pull recurring force labels and industry context from `ibis-industries` when deciding:
  - which sectors need another company
  - which cross-sector themes deserve a memo
  - which cultural or industrial signals need stronger coverage

## End-of-run requirement

Every coherent run should end with:

- commit hash
- companies completed
- companies partial
- industry lane summary
- key themes
- strongest cross-company signals
- next recommended names

## Skeptical Reader Test

- Does this note tell a worker what to do next at the lane level, company-collection level, and closeout level?
- Can a skeptical reader see the exact collection window, batch size logic, and reuse rules that should govern the next pass?
- Does the file make it hard to drift back into vague pilot behavior or shallow multi-lane sprawl?
- What missing operating rule would leave the next worker unsure how to turn a chosen lane into a coherent batch?
