# Post-Batch Integration Checklist

Date baseline: 2026-08-10

Use this checklist after a coherent lane batch is complete.
This is the standard integration pass that follows the lane-run template and batch-handoff template.

## Current Archive State

As of Tuesday, August 11, 2026, many of the archive's highest-value lanes already have frameworks, proof pages, comparison memos, and watchlists.

That means integration should not assume every batch opened a lane from zero.

It should also check whether a continuation batch actually strengthened an already-open lane.

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
- confirm the packet says what its main fields are proving, not just that the fields exist
- confirm the packet names who captures cleaner economics and who absorbs the messy work
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
- which packet fields supplied the main lane conclusions
- whether the strongest claims met the right proof burden for their claim type
- the exact metric or operating fact carrying each major claim
- the exact annual or quarterly period carrying each major claim
- why those facts support the conclusion instead of merely appearing near it
- what next-filing evidence would weaken or disprove the conclusion

If the batch was a strengthening pass inside an already-open lane, also confirm:

- which missing flagship role, contradiction case, burden split, or break test it improved
- whether the live lane read is now sharper rather than merely longer
- whether the updated queue or board should change because the next best gap is now different

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
- who bears the burden stack and who captures cleaner economics
- whether consumer, cultural, industrial, technical, capital, or cross-company claims are backed by the right kind of proof
- whether the strongest conclusions can be restated as exact fact -> exact period -> plain-English meaning -> disconfirming test

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
