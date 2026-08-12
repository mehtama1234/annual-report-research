# Overall Writing Pass Handoff

Date: `2026-08-12`
Repo: `annual-report-research`
Branch intended for writing pass: `main`
Current `main` commit at handoff: `391d10fd`

## What this handoff is for

- This handoff is for another CLI to take a writing pass across `annual-report-research`.
- The core research buildout and proof-tightening pass are now in a good enough state to support synthesis work.
- This is not a request to open new lanes, rebuild evidence chains, or do another broad company-collection phase.
- This is a request to improve the readability, usefulness, and coherence of the repo's written layer.

## Current repo state

- The proof-tightening queue for the recent closeout pass is complete.
- The current checkpoint note says:
  - `Qualified companies`
  - `None in the current proof-tightening queue.`
- Recent `main` commits that matter for closeout state:
  - `391d10fd` `Promote Tenet packet to proven status`
  - `d6ac3690` `Promote Cigna packet to proven status`
  - `c896fa59` `Promote Prudential packet to proven status`
  - `7f271b9f` `Promote AGNC packet to proven status`
  - `e9b095ee` `Promote HPE packet to proven status`

## What is already strong

- The archive now has broad lane coverage across:
  - recreation / lifestyle / participation
  - healthcare frontier and recurring-care systems
  - connectivity / telecom / infrastructure tech
  - capital structures / property / conglomerates
- Many company packets are already strong enough for use.
- There is a large cross-sector insight layer in [analysis/cross-sector](/analysis/cross-sector).
- There are lane-specific writing surfaces in:
  - [analysis/sectors](/analysis/sectors)
  - [analysis/themes](/analysis/themes)
- There are many operator and insight briefs in [notes](/notes).

## Best source material for the writing pass

Start here:

- [notes/main-wrap-up-checkpoint-handoff-2026-08-11.md](/notes/main-wrap-up-checkpoint-handoff-2026-08-11.md)
- [notes/end-to-end-insight-operator-and-review-brief-2026-08-11.md](/notes/end-to-end-insight-operator-and-review-brief-2026-08-11.md)
- [notes/master-insight-extraction-goal-2026-08-11.md](/notes/master-insight-extraction-goal-2026-08-11.md)
- [notes/insight-artifact-manifest-2026-08-11.md](/notes/insight-artifact-manifest-2026-08-11.md)
- [analysis/cross-sector/concrete-insights-and-curiosity-map-2026-08-10.md](/analysis/cross-sector/concrete-insights-and-curiosity-map-2026-08-10.md)
- [analysis/cross-sector/aha-moments-and-curiosity-questions-2026-08-10.md](/analysis/cross-sector/aha-moments-and-curiosity-questions-2026-08-10.md)
- [analysis/cross-sector/company-level-strategy-insight-guide-2026-08-10.md](/analysis/cross-sector/company-level-strategy-insight-guide-2026-08-10.md)
- [analysis/cross-sector/industry-level-strategy-guide-2026-08-10.md](/analysis/cross-sector/industry-level-strategy-guide-2026-08-10.md)

Then use the comparison library selectively:

- [analysis/cross-sector](/analysis/cross-sector)

High-value theme pages:

- [analysis/themes/cli-4-healthcare-proof-page-2026-08-11.md](/analysis/themes/cli-4-healthcare-proof-page-2026-08-11.md)
- [analysis/themes/cli-5-connectivity-proof-page-2026-08-11.md](/analysis/themes/cli-5-connectivity-proof-page-2026-08-11.md)
- related `cli-4`, `cli-5`, and `cli-6` lane-run notes in [analysis/sectors](/analysis/sectors)

## What the writing pass should actually do

- Turn the repo from "large collection of strong research artifacts" into "clear readable archive a new reader can navigate."
- Prioritize synthesis and explanation over additional collection.
- Improve pages that are directionally right but too abstract, too repetitive, or too dependent on repo context.
- Make the best insight pages easier to understand without losing specificity.
- Surface concrete examples from actual company packets when making big claims.
- Reduce jargon, cliché, and over-compressed shorthand.
- Connect macro claims back to the exact kinds of company evidence that support them.

## High-value deliverables

- A clearer top-level synthesis page for what the archive now proves.
- Cleaner lane summaries for the four major fronts.
- Stronger cross-company theme pages that use concrete examples instead of generic statements.
- Better "how to read this archive" guidance for a new reader.
- Tighter curiosity / aha pages that show why the findings matter.

## Recommended writing targets

Prioritize these kinds of files:

- checkpoint and wrap-up notes that summarize the archive state
- cross-sector pages that carry the biggest conclusions
- proof pages that need clearer examples
- insight pages that are conceptually strong but still read like operator notes

Good candidate work:

- tighten duplicated claims across similar cross-sector comparison pages
- merge near-overlapping pages where the distinction is too subtle to justify separate files
- add short concrete example blocks when a page makes a broad claim
- improve introductions and endings so each page states what it proves and why it matters
- standardize voice across the best synthesis pages

## What the writing pass should avoid

- Do not reopen broad evidence collection unless a writing change absolutely requires it.
- Do not start another raw download sweep.
- Do not churn repo-wide indexes unless the writing pass truly requires it.
- Do not weaken concrete statements into generic business-school prose.
- Do not turn everything into abstract thematic language detached from companies.
- Do not rewrite dozens of company packets just to smooth style. Use them as evidence first.

## Evidence standard for writing claims

- Every stronger claim should still be traceable back to actual company analysis.
- When writing "big picture" pages, prefer specific company examples over generic sector talk.
- Good pattern:
  - claim
  - why it matters
  - two to four concrete company examples
  - implication or tension
- Avoid unsupported phrases like:
  - "the future is"
  - "across the board"
  - "clear winner"
  - "paradigm shift"
unless the page actually proves them.

## Tone target

- Simple, concrete, direct.
- No cliché.
- No inflated theory language.
- No fake certainty.
- Write like an investigator explaining what repeated company evidence actually shows.

## Suggested operating sequence

1. Read the checkpoint note and insight-operator brief.
2. Pick the small set of synthesis pages that matter most.
3. Improve them one by one with concrete examples and cleaner structure.
4. Only then decide whether any new summary page is needed.
5. Leave a concise handoff listing:
   - pages materially improved
   - pages still weak
   - duplicated pages worth merging later
   - strongest new synthesis surfaces
   - commit hash

## Suggested definition of success

- A new reader can understand the archive's main findings without reading thread history.
- The strongest pages explain claims in plain English and back them with named company examples.
- Lane summaries feel connected to the actual research, not like abstract theme dumps.
- The repo feels more coherent and less like a pile of separate notes.

## Concrete starting prompt for another CLI

Use the current `main` state of `annual-report-research` as authoritative.
Take a writing-only pass on the repo's synthesis layer.
Do not expand research breadth.
Prioritize clarity, concrete examples, and cross-page coherence.
Use actual company packets and existing comparison pages as evidence.
Leave the repo easier for a serious outside reader to understand.
