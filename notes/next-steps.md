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

- [START-HERE.md](/START-HERE.md)
- [Active lane board](/notes/active-lane-board-2026-08-10.md)

As of Tuesday, August 11, 2026, many of the archive's highest-value lanes already have frameworks, proof pages, comparison memos, and watchlists.

That means a new run should usually begin by deciding whether it is:

1. opening a truly new lane
2. strengthening an already-open lane

Each run should aim to finish a coherent `3` to `4` company flagship batch inside a lane when a real new batch is needed, not spray work across dozens of shallow starts.

For an already-open lane, the default next move is usually not to restart the lane from zero.

It is usually to:

- fill a missing flagship role
- add the strongest contradiction or weak-link case
- sharpen the burden-versus-beneficiary split
- improve the next-filing break test

If you need to verify which live instruction, queue, template, and review surfaces already reflect that continuation-phase state, use:

- [Continuation mode alignment audit](/notes/continuation-mode-alignment-audit-2026-08-11.md)

If you want the shortest continuation-mode statement of what is still left, which lanes matter most, and what now counts as real progress, use:

- [Remaining meaty end-to-end operator brief](/notes/remaining-meaty-end-to-end-operator-brief-2026-08-11.md)

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

If the lane already exists in working form, the batch should instead be chosen to improve the live read:

1. one missing role that completes the lane map
2. one contradiction or weak-link case
3. one company that sharpens the burden-versus-beneficiary split
4. one company that improves the best disconfirming next-filing test

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

Before writing the interpretation, decide what the packet fields are supposed to prove:

- annual takeaways + quarter chain
  - prove: what changed and whether the direction is strengthening, weakening, or persisting
- operating model + strategy read
  - prove: what job the company really performs and how management is responding
- exact supporting facts
  - prove: the claim directly rather than by implication
- burden-versus-beneficiary read
  - prove: who captures cleaner economics and who absorbs the messy work
- watchlist
  - prove: the next read is falsifiable rather than rhetorical

Also decide which kind of claim the company should strengthen:

- consumer
- cultural or societal
- industrial or operating
- technical or infrastructure
- capital or balance-sheet
- cross-company comparison

Also decide before the packet is treated as directionally useful:

- the best alternative explanation still in play
- the next-filing disconfirming test
- the exact fact-period chain that would make the company useful in a lane comparison

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

## Insight-System Maintenance

When you need to confirm that the note layer, remaining-work bundle, and browser review surfaces still line up before starting the next run, use:

- `bash scripts/run-insight-audit-stack.sh`
- `bash scripts/refresh-note-layer-boundary.sh`
- `bash scripts/audit-audit-stack-terminology.sh`
- `bash scripts/audit-maintenance-doc-stack.sh`
- `bash scripts/audit-continuation-mode-links.sh`
- `bash scripts/audit-remaining-brief-links.sh`
- `bash scripts/audit-remaining-stack-links.sh`
- `bash scripts/audit-browser-review-links.sh`
- `bash scripts/verify-insight-system.sh`

## Skeptical Reader Test

- Does this note tell a worker what to do next at the lane level, company-collection level, and closeout level?
- Can a skeptical reader see the exact collection window, batch size logic, and reuse rules that should govern the next pass?
- Does the file make it hard to drift back into vague pilot behavior or shallow multi-lane sprawl?
- What missing operating rule would leave the next worker unsure how to turn a chosen lane into a coherent batch?
