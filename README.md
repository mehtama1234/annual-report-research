# Annual Report Research Workspace

Date baseline: 2026-08-10

This workspace is for collecting, organizing, and analyzing company annual reports, quarterly earnings materials, and cross-company themes by sector and industry.

Primary collection window for this project:

- `2025` annual reports and annual filings
- `2026` quarterly earnings materials as the primary quarterly focus
- the trailing quarter from late `2025` only when needed to complete the last three reported quarters as of `2026-08-10`

It is intentionally split into three layers:

- `raw/` - source documents and source-ledger notes
- `extracted/` - normalized company packets and extracted facts
- `analysis/` - sector, industry, and theme synthesis

This keeps raw evidence separate from downstream interpretation.

## New reader? Start here

If you just want to understand what this archive found — not continue the research — use the reader layer, not the operator briefs below:

- [How to read this archive](/notes/how-to-read-this-archive-2026-08-12.md) — the front door: what this is, the one central idea, and where to look.
- [What this archive proves](/analysis/cross-sector/what-this-archive-proves-2026-08-12.md) — the main proven findings in plain English, each backed by named companies.
- [Four lane summaries](/analysis/cross-sector/four-lane-summaries-2026-08-12.md) — each of the four research lanes on one page.
- [Comparison library map](/analysis/cross-sector/comparison-library-map-2026-08-12.md) — a grouped index into the detailed company-by-company comparison pages.

Everything below this point is for an operator who is continuing the research.

Remote `main` currently carries the extracted, analysis, notes, and index layers, but not the heavy offloaded `raw/**` payload.
If a packet cites a raw evidence path that is no longer present in the checkout, resolve it through:

- [Raw blob offload readme](/notes/raw-blob-offload-readme-2026-08-10.md)
- [Raw evidence link policy](/notes/raw-evidence-link-policy-2026-08-11.md)
- [Legacy root reference audit](/notes/legacy-root-reference-audit-2026-08-11.md)
- `python3 scripts/resolve-offloaded-raw-path.py 'raw/.../file.ext'`
- `bash scripts/verify-raw-evidence-governance.sh`

## Current operating brief

Start here:

- [START-HERE.md](/START-HERE.md)

That file points to the active operator brief, lane instructions, next-step workflow, and current handoff.
Together those files define the end-to-end pursuit goal, the lane-level output standard, the `3` to `4` flagship-company batch rule, the handoff requirements, and the expanded lane coverage across recreation, healthcare frontier, connectivity / telecom / infra tech, and capital structures / property / conglomerates.

If you want the shortest continuation-mode statement of what work is still left, which lanes matter most, and what outputs now count as real progress, use:

- [Remaining meaty end-to-end operator brief](/notes/remaining-meaty-end-to-end-operator-brief-2026-08-11.md)
- [Remaining end-to-end insight goal](/notes/remaining-end-to-end-insight-goal-2026-08-11.md)
- [Remaining insight execution board](/notes/remaining-insight-execution-board-2026-08-11.md)

If you want the explicit audit trail for why those live surfaces now default to strengthening already-open lanes rather than restarting them from zero, use:

- [Continuation mode alignment audit](/notes/continuation-mode-alignment-audit-2026-08-11.md)

For the fastest lane-selection view, use:

- [Active lane board](/notes/active-lane-board-2026-08-10.md)
- [Current execution queue](/notes/current-execution-queue-2026-08-10.md)

## Why this exists

Two existing projects already cover adjacent work:

- `ibis-industries/` is the industry-synthesis layer
- `projects/Misc/ui-projects/strategy-under-a-force/` is the theme and company-dossier layer

This workspace fills the missing middle: a disciplined repository of annual reports, 10-Ks, 10-Qs, earnings releases, and call materials organized by sector, industry, and company.

For the current cross-project fit, see:

- [Annual report stack alignment](/analysis/annual-report-stack-alignment-2026-08-09.md)

## Folder layout

```text
annual-report-research/
  raw/
    annualreports/
    company-ir/
    sec/
    earnings-calls/
  extracted/
  analysis/
    sectors/
    industries/
    themes/
  indexes/
  templates/
  notes/
```

## Source policy

Use sources in this order:

1. Company investor-relations pages
2. SEC filings and exhibits
3. Earnings press releases and transcripts
4. AnnualReports.com for annual-report discovery, sector tags, industry tags, and archive convenience

Do not treat AnnualReports.com as the only source of truth for the last three quarters. Use company IR or SEC as the primary evidence for `2026` quarterlies and any required late-`2025` trailing quarter.

Just as important: the work is not only document collection.
The archive is also expected to identify recurring consumer trends, cultural and societal shifts, industrial and operating pressures, capital-allocation behavior, and cross-company patterns that repeat across the lane.
That includes participation systems, franchise or IP monetization, loyalty and habit formation, reimbursement or workflow control, infrastructure bottlenecks, and the broader social or institutional changes that keep showing up across multiple management teams.
The archive should keep distinguishing who is bearing the burden stack and who is capturing the cleaner economics.
If a batch can name the annual report and quarter chain but cannot explain the repeated behavior shift, pressure pattern, and monetization logic across several companies, that batch is still incomplete.

The packet fields should do explicit analytical work:

- annual takeaways + latest three-quarter chain
  - prove: what changed and whether the direction is strengthening, weakening, or persisting
- plain-English operating model
  - prove: what job the company really performs in the system
- strategy read
  - prove: how management is responding to the pressure or opportunity
- growth engine + economic lever
  - prove: what is really carrying the story and what actually moves the economics
- operating constraint
  - prove: where the system is strained
- exact supporting facts
  - prove: the claim directly rather than by implication
- burden-versus-beneficiary interpretation
  - prove: who gets cleaner economics and who absorbs the messy work
- thesis breaker + watchlist
  - prove: the work is falsifiable and ready for continuation

Different claim types also need different proof burdens:

- consumer claim
  - show: what behavior changed and which facts prove it
- cultural or societal claim
  - show: which real-life pressure is creating demand and why it is broader than one company
- industrial or operating claim
  - show: where the strain sits and what happens economically when that pressure changes
- technical or infrastructure claim
  - show: where software is the control layer and where physical bottlenecks still decide outcomes
- capital or balance-sheet claim
  - show: who must carry property, inventory, debt, or financing burden to keep the system working
- cross-company pattern claim
  - show: exact support from at least three companies and what evidence would weaken the broader pattern

## Minimum company packet

Each covered company should end up with:

- sector
- industry
- ticker
- exchange
- fiscal year-end
- latest annual report
- latest 10-K or 20-F
- last three quarterly earnings releases
- last three quarterly 10-Qs or equivalent
- notes on what changed
- a thematic read on the bigger pattern the company helps prove

For most calendar-year reporters, the expected quarterly window is:

- `2026 Q2`
- `2026 Q1`
- `2025 Q4`

For off-calendar fiscal reporters, use the latest three reported fiscal quarters available as of `2026-08-10`, keeping the same principle: prioritize `2026` quarters and pull in late `2025` only when required. Label them precisely.

## Operating rule

Every analysis claim should point back to a dated source in `raw/` or a row in the source ledger.

Shared repo-wide indexes should not be updated continuously during exploration.
Do that at the end of a coherent batch or leave the batch ready for later integration.

## Insight-System Maintenance

For the note-boundary and insight-system audit layer:

- run the full linked audit stack with:
  - `bash scripts/run-insight-audit-stack.sh`
- refresh the committed boundary report and rerun the linked audit stack with:
  - `bash scripts/refresh-note-layer-boundary.sh`
- run only the direct boundary audit with:
  - `bash scripts/audit-note-layer-boundary.sh`
- run only the audit-stack terminology audit with:
  - `bash scripts/audit-audit-stack-terminology.sh`
- run only the maintenance-doc audit with:
  - `bash scripts/audit-maintenance-doc-stack.sh`
- run only the reusable-note maintenance-visibility audit with:
  - `bash scripts/audit-reusable-note-maintenance-visibility.sh`
- run only the historical-note maintenance-isolation audit with:
  - `bash scripts/audit-historical-note-maintenance-isolation.sh`
- run only the continuation-link audit with:
  - `bash scripts/audit-continuation-mode-links.sh`
- run only the remaining-brief link audit with:
  - `bash scripts/audit-remaining-brief-links.sh`
- run only the remaining-stack link audit with:
  - `bash scripts/audit-remaining-stack-links.sh`
- run only the browser review-link audit with:
  - `bash scripts/audit-browser-review-links.sh`
- run only the full insight-system verifier with:
  - `bash scripts/verify-insight-system.sh`
