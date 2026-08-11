# Post-Batch Integration Checklist

Date baseline: 2026-08-10

Use this checklist after a coherent lane batch is complete.
This is the standard integration pass that follows the lane-run template and batch-handoff template.

## Preconditions

Before starting integration, confirm:

- the batch has a handoff
- the batch has a commit hash
- each flagship company is either source-complete or clearly marked partial
- company packet, company profile, and source ledger status are explicit

## Company-level integration

For each flagship company:

- confirm `company-packet.md` exists or is intentionally deferred
- confirm `company-profile.md` exists or is intentionally deferred
- confirm `source-ledger.md` exists or is intentionally deferred
- confirm annual report status is explicit
- confirm annual filing status is explicit
- confirm last three reported quarters as of `2026-08-10` are explicit
- confirm thematic interpretation is present, not just document links
- confirm any offloaded `raw/**` evidence paths can be resolved through `indexes/raw-blob-offload-manifest-2026-08-10.csv` or `python3 scripts/resolve-offloaded-raw-path.py`

## Shared index integration

Update shared repo-wide indexes only after the coherent batch is ready.

Check and update as applicable:

- `indexes/companies.csv`
- `indexes/coverage-tracker.csv`
- `indexes/sectors.csv`
- lane-relevant interface indexes
- any lane-specific tracker or queue note that should reflect the finished batch

For each index update, confirm:

- the company is source-complete or clearly marked partial
- the quarter window is labeled correctly
- source taxonomy is preserved even when the business-model interpretation crosses sectors

## Synthesis integration

Update the relevant synthesis layer as applicable:

- sector brief
- industry brief
- theme memo
- lane summary
- active lane board or execution queue only if the batch changes what should be run next

Confirm that the synthesis includes:

- what changed in the annuals
- what changed across the latest quarter chain
- the strongest cross-company themes
- the main moats, pressures, and fragilities
- exact next names that would improve the lane

If the batch introduced new offloaded evidence assumptions, also confirm:

- the manifest already covers the cited raw paths, or a new offload manifest or note was added
- no live navigation layer was left pointing at a retired repo root except in explicit historical or provenance cases

## Thematic quality check

Confirm the work is not just a filing archive.

Explicitly check whether the batch surfaces:

- consumer trends
- cultural and societal shifts
- industrial and operating pressures
- bigger-picture patterns that repeat across companies
- participation, franchise, and IP monetization where relevant

If these are missing, the batch is not fully integrated.

## Handoff completion check

Confirm the end-of-run handoff includes:

- commit hash
- companies completed
- companies partial
- industry lane summary
- key themes
- strongest cross-company signals
- next recommended names
- raw evidence resolution status when heavy source files were offloaded

## Final integration note

- integration complete: yes / no
- if no, exact remaining integration tasks:
- exact next action:
