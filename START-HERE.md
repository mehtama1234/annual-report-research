# Start Here

Date baseline: 2026-08-10
Repo: `annual-report-research`

If you are starting work in this repo, read these files in this order:

1. [Insight extraction hub](/home/manishmehta/ui-projects/annual-report-research/notes/insight-extraction-hub-2026-08-11.md)
2. [End-to-end insight operator and review brief](/home/manishmehta/ui-projects/annual-report-research/notes/end-to-end-insight-operator-and-review-brief-2026-08-11.md)
3. [Remaining end-to-end insight goal](/home/manishmehta/ui-projects/annual-report-research/notes/remaining-end-to-end-insight-goal-2026-08-11.md)
4. [Remaining insight execution board](/home/manishmehta/ui-projects/annual-report-research/notes/remaining-insight-execution-board-2026-08-11.md)
5. [Insight-driven next lane queue](/home/manishmehta/ui-projects/annual-report-research/notes/insight-driven-next-lane-queue-2026-08-11.md)
6. [Lane end-to-end execution runbook](/home/manishmehta/ui-projects/annual-report-research/notes/lane-end-to-end-execution-runbook-2026-08-11.md)
7. [Insight extraction templates](/home/manishmehta/ui-projects/annual-report-research/notes/insight-extraction-templates-2026-08-11.md)
8. [Insight completion rubric](/home/manishmehta/ui-projects/annual-report-research/notes/insight-completion-rubric-2026-08-11.md)
9. [Insight artifact manifest](/home/manishmehta/ui-projects/annual-report-research/notes/insight-artifact-manifest-2026-08-11.md)
10. [Next steps](/home/manishmehta/ui-projects/annual-report-research/notes/next-steps.md)
11. [Master operator brief](/home/manishmehta/ui-projects/annual-report-research/notes/master-operator-brief-2026-08-10.md)
12. [End-to-end pursuit goal](/home/manishmehta/ui-projects/annual-report-research/notes/end-to-end-pursuit-goal-2026-08-10.md)
13. [CLI lane instructions](/home/manishmehta/ui-projects/annual-report-research/indexes/cli-lane-instructions-2026-08-10.md)
14. [Lane run template](/home/manishmehta/ui-projects/annual-report-research/templates/lane-run-template.md)
15. [Batch log template](/home/manishmehta/ui-projects/annual-report-research/templates/batch-log-template.md)
16. [Theme memo template](/home/manishmehta/ui-projects/annual-report-research/templates/theme-memo.md)
17. [Batch handoff template](/home/manishmehta/ui-projects/annual-report-research/templates/batch-handoff-template.md)
18. [Status rubric](/home/manishmehta/ui-projects/annual-report-research/templates/status-rubric.md)
19. [Post-batch integration checklist](/home/manishmehta/ui-projects/annual-report-research/templates/post-batch-integration-checklist.md)
20. [Current handoff](/home/manishmehta/ui-projects/annual-report-research/notes/handoff-2026-08-10.md)
21. [Active lane board](/home/manishmehta/ui-projects/annual-report-research/notes/active-lane-board-2026-08-10.md)
22. [Current execution queue](/home/manishmehta/ui-projects/annual-report-research/notes/current-execution-queue-2026-08-10.md)

## Current Archive State

As of Tuesday, August 11, 2026, the archive is no longer mainly missing its first interpretation layer.

Many of the highest-value lanes already have:

- frameworks
- proof pages
- comparison memos
- next-filing watchlists

That means a new run should usually start with the continuation-mode notes above rather than with older kickoff briefs alone.

The default next move is often not to open a lane from zero.

It is often to:

- fill a missing flagship role
- add the strongest contradiction or weak-link case
- sharpen the burden-versus-beneficiary split
- improve the next-filing break test

## Insight-System Maintenance

Use these when you need to refresh or verify the note-boundary and insight-system audit layer:

- one-command refresh plus verification:
  - `bash scripts/refresh-note-layer-boundary.sh`
- direct boundary audit only:
  - `bash scripts/audit-note-layer-boundary.sh`
- maintenance-doc audit:
  - `bash scripts/audit-maintenance-doc-stack.sh`
- continuation-link audit:
  - `bash scripts/audit-continuation-mode-links.sh`
- browser review-link audit:
  - `bash scripts/audit-browser-review-links.sh`
- full broader insight-system verifier:
  - `bash scripts/verify-insight-system.sh`

Current boundary artifacts:

- [Note layer boundary audit report](/home/manishmehta/ui-projects/annual-report-research/notes/note-layer-boundary-audit-2026-08-11.md)
- [Note layer boundary audit JSON](/home/manishmehta/ui-projects/annual-report-research/notes/note-layer-boundary-audit-2026-08-11.json)
- [Insight artifact manifest](/home/manishmehta/ui-projects/annual-report-research/notes/insight-artifact-manifest-2026-08-11.md)
- [Continuation mode alignment audit](/home/manishmehta/ui-projects/annual-report-research/notes/continuation-mode-alignment-audit-2026-08-11.md)

## Raw Evidence Maintenance

Remote `main` does not carry the heavy offloaded `raw/**` payload.
If a packet, profile, or source ledger points at raw evidence that is not present in the checkout:

- resolve the offloaded raw path with:
  - `python3 scripts/resolve-offloaded-raw-path.py 'raw/.../file.ext'`
- audit the remaining retired-root footprint with:
  - `bash scripts/audit-legacy-root-references.sh`
- run the full raw-evidence governance check with:
  - `bash scripts/verify-raw-evidence-governance.sh`

Supporting references:

- [Raw evidence link policy](/home/manishmehta/ui-projects/annual-report-research/notes/raw-evidence-link-policy-2026-08-11.md)
- [Raw blob offload readme](/home/manishmehta/ui-projects/annual-report-research/notes/raw-blob-offload-readme-2026-08-10.md)
- [Legacy root reference audit](/home/manishmehta/ui-projects/annual-report-research/notes/legacy-root-reference-audit-2026-08-11.md)

## Current integrated checkpoints

Use these before opening a new batch if you want the current state rather than only the kickoff briefs:

- [Concrete insights and curiosity map](/home/manishmehta/ui-projects/annual-report-research/analysis/cross-sector/concrete-insights-and-curiosity-map-2026-08-10.md)
- [CLI 4 recurring-care framework](/home/manishmehta/ui-projects/annual-report-research/analysis/themes/cli-4-recurring-care-and-workflow-control-framework-2026-08-10.md)
- [CLI 5 control-point framework](/home/manishmehta/ui-projects/annual-report-research/analysis/themes/cli-5-control-point-and-chokepoint-framework-2026-08-10.md)
- [CLI 6 trust-intermediation framework](/home/manishmehta/ui-projects/annual-report-research/analysis/themes/cli-6-trust-intermediation-framework-2026-08-10.md)
- [CLI 4 / 5 / 6 recurring-interface framework](/home/manishmehta/ui-projects/annual-report-research/analysis/themes/cli-4-5-6-recurring-interface-control-framework-2026-08-10.md)
- [CLI 4 / 5 / 6 multi-lane handoff](/home/manishmehta/ui-projects/annual-report-research/notes/cli-4-5-6-multi-lane-handoff-2026-08-10.md)

## Direct kickoff briefs

Use these when you already know which lane you are opening:

- [Recreation / participation kickoff brief](/home/manishmehta/ui-projects/annual-report-research/notes/recreation-participation-kickoff-2026-08-10.md)
- [CLI 4 kickoff brief](/home/manishmehta/ui-projects/annual-report-research/notes/cli-4-kickoff-2026-08-10.md)
- [CLI 5 kickoff brief](/home/manishmehta/ui-projects/annual-report-research/notes/cli-5-kickoff-2026-08-10.md)
- [CLI 6 kickoff brief](/home/manishmehta/ui-projects/annual-report-research/notes/cli-6-kickoff-2026-08-10.md)

## Working goal

Build this repo into a source-grounded, multi-lane research archive that combines:

- `2025` annual reports and annual filings
- the latest three reported quarters as of `2026-08-10`
- company-level thematic interpretation
- lane-level summaries
- recurring cross-company pattern recognition

That pattern work is a core deliverable.
Every coherent batch should identify the consumer, cultural, societal, industrial, technical, operating, and capital-allocation signals that repeat across multiple companies.
That includes participation, franchise, IP, loyalty, workflow, reimbursement, trust, destination, and asset-utilization monetization patterns when they are actually doing the economic work.

## Main lane families

- recreation, lifestyle, and participation demand
- healthcare frontier and recurring-care systems
- connectivity, telecom, and technical infrastructure
- capital structures, property vehicles, and conglomerates

## Standard run shape

Each run should usually:

- pick one coherent lane
- complete `4` to `8` flagship companies when the lane supports it, or at minimum leave one finished coherent comparison set with exact staged next names
- use the lane-run template to keep the batch structure, evidence state, and handoff fields consistent
- use the batch-log template while the batch is actively in progress
- use the theme-memo template when a cross-company signal is strong enough to matter beyond one packet
- use the batch-handoff template for the end-of-run closeout format
- use the post-batch integration checklist before considering the batch fully integrated
- produce both filing coverage and thematic interpretation for each company
- keep moving if one company or source chain gets messy by advancing the next best in-scope name and leaving a clean partial trail
- keep committing alongside substantial progress so another thread can resume from real repo state
- avoid continuous shared-index updates during exploration
- end with a handoff containing the commit hash, completed companies, partial companies, lane summary, key themes, strongest signals, and next recommended names

The run is not done when the files are collected.
It is done when another operator can see what changed, why it matters, what pressures recur across the lane, and which names should be added next.
That includes the consumer, cultural, societal, industrial, and monetization patterns the covered companies are collectively revealing.

The packet fields should also do explicit analytical work:

- annual takeaways + latest three quarters
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

## Source rule

Use `AnnualReports.com` for taxonomy and archive confirmation.
Use company IR and SEC as authoritative when AnnualReports lags.
