# Cross-Repo Evidence Portability Audit

Date baseline: `2026-08-11`
Repo: `annual-report-research`

## Purpose

This note answers a repo-level closeout question:

- are the remaining proof problems mainly a few packet-specific misses
- or does the current archive still depend heavily on evidence links that point outside the current repo in a way that bypasses the intended storage model

The answer matters because the repo now has two different external-evidence situations:

- an intentional raw-blob offload model documented in Git and backed by Google Drive manifests
- older or inherited sibling-worktree path references that are not the same thing as the offload model

## Scope

This is a markdown-link audit over the main content surfaces in the current repo:

- `extracted/`
- `analysis/`
- `notes/`
- `indexes/`
- `templates/`
- `START-HERE.md`
- `README.md`

The audit focuses on absolute local paths that point to `/home/manishmehta/ui-projects/...`.

It does not treat the documented Google Drive raw-offload model itself as a defect.

For that intended model, see:

- [raw-blob-offload-readme-2026-08-10.md](/home/manishmehta/ui-projects/annual-report-research/notes/raw-blob-offload-readme-2026-08-10.md)
- [raw-blob-offload-summary-2026-08-10.tsv](/home/manishmehta/ui-projects/annual-report-research/indexes/raw-blob-offload-summary-2026-08-10.tsv)

## Top-level content concentration

A raw path-count scan across those surfaces showed the path-heavy layer is concentrated in:

- `extracted`: about `20,996` path references
- `indexes`: about `1,414`
- `analysis`: about `475`
- `notes`: about `135`

That matters because portability problems are primarily packet and packet-adjacent, not just note-layer noise.

## External repo reference counts

When the audit excludes links that point back into the current `annual-report-research` repo, the biggest foreign roots are:

- `annual-report-research-new-lanes`: about `7,048`
- `annual-report-research-energy-buildout`: about `3,270`
- `annual-report-research-footwear-dept-audit`: about `2,044`
- `annual-report-research-cli8-middle-layer`: about `1,712`
- `annual-report-research-remaining-frontiers`: about `234`
- `annual-report-research-cli8-middle-layer-imported-2026-08-10`: about `216`
- `annual-report-research-media-frontier-push`: about `14`

The important point is not the exact last digit.

The important point is that the current repo still contains many thousands of direct links into other local worktrees.

That is a different issue from intentional Drive-backed raw offload.

## What this means

The current archive is analytically strong, but a large share of its evidence pointers still follow a pre-offload or side-worktree pathing model rather than the current canonical storage model.

In plain language:

- many company packets in `annual-report-research` still point to saved artifacts in sibling repos rather than:
  - local artifacts inside this repo
  - or the documented raw-offload manifest / resolver path
- the two recent packet-level repairs for `Sysco` and `HPE` were not isolated oddities
- they were small visible cases of a larger archive-assembly pattern

## Strongest evidence from the sample

The external-root counts were backed by direct examples in the current repo:

- some packet source pointers and ledgers still point into `annual-report-research-cli8-middle-layer` or `annual-report-research-cli8-middle-layer-imported-2026-08-10`
- many packet source pointers and ledgers still point into `annual-report-research-new-lanes`
- some handoff and frontier notes still preserve source-worktree provenance from `annual-report-research-new-lanes`, `annual-report-research-footwear-dept-audit`, or `annual-report-research-energy-buildout`

That means the repo's current state is best described as:

- integrated at the interpretation layer
- partially integrated at the packet layer
- not yet fully normalized at the evidence-location layer

## Why this matters for the original goal

The original goal was not only to produce insight.

It also implied a usable research archive with:

- source-complete packets
- authoritative filing coverage
- handoff-ready continuation quality

If the current repo still requires several sibling worktrees to open large parts of the evidence chain, then full closeout is still incomplete even when the writeups are good.

That statement does not apply to raw evidence that was intentionally offloaded and documented through the manifest system.

## What is already true

This is not a claim that the research is fake or missing.

The current evidence suggests something more specific:

- much of the research work does exist locally somewhere in the broader workspace
- the analytical layer in `annual-report-research` often reflects real packet work
- the remaining problem is that many links still point to old sibling-worktree locations instead of the current canonical pathing model

That is a canonical-reference problem, not necessarily a research-coverage problem.

## What is not a problem

The presence of heavy raw evidence outside Git is not, by itself, a repo defect here.

The offload readme makes the intended model explicit:

- heavy `raw/**` payload was moved out of remote `main`
- Google Drive holds the bulk payload
- Git keeps manifests, summaries, and resolver scripts

So the correct question is not:

- "does every packet point to a file physically inside this repo"

The correct question is:

- "does every packet point either to the current repo or to the documented canonical offload system, instead of to an arbitrary sibling worktree"

## Highest-priority canonical-reference problems

### 1. `annual-report-research-new-lanes`

This is the single largest foreign worktree root in the current repo by a wide margin.

Implication:

- many packets and ledgers still treat `new-lanes` as the live evidence warehouse behind the current main repo instead of using a normalized canonical reference model

### 2. `annual-report-research-energy-buildout`

This is the second-largest foreign root and shows that substantial later work was integrated by direct sibling-reference rather than normalized into current canonical pointers.

### 3. `annual-report-research-footwear-dept-audit`

This remains a major upstream evidence root even for companies that have nothing to do with the original name of that worktree.

Implication:

- the folder name is historical noise, but the dependency is real

### 4. `annual-report-research-cli8-middle-layer`

This root is especially visible in distribution, wholesale, and middle-layer indexes and packet references.

Implication:

- the archive still relies on a specialist side-worktree for a meaningful share of channel-control and distribution evidence

Update as of `2026-08-11`:

- the top-level CLI 8 synthesis and index pages inside `annual-report-research` now point to the current repo for their live packet navigation
- the remaining CLI 8 dependency is therefore more concentrated in packet-level raw provenance and inherited source-ledger links, not in the main reader-facing synthesis surface

## Practical consequence for completion status

The remaining closeout problem should now be described in three separate layers:

### Layer 1: packet truthfulness

This layer improved materially.

- `Sysco` no longer overclaims a local `Q4 FY26` filed-wrapper chain
- `HPE` no longer pretends to have a clean locally inspectable raw chain

### Layer 2: repo portability

The offload model itself is intentional and documented.

What is still incomplete is not raw-offload existence, but canonical path normalization.

### Layer 3: canonical evidence references

This layer is still materially incomplete.

- thousands of links still point to sibling worktrees
- many of those links do not yet route through the documented offload-manifest model
- that means the archive is not yet cleanly normalized even if the heavy raw storage decision was correct

## What This Means After The Recent Lane-Narrowing Work

Since this note was first drafted, the repo has materially improved its lane-closure picture through:

- the CLI 5 control-layer expansion and healthcare-information bridge
- the CLI 4 adjacent burden bridge
- the CLI 6 balance-sheet and property clarification pass
- the recreation owner and repeat-relationship bridge

That matters because the reference problem now stands out more clearly.

The repo is no longer mainly held back by missing high-level interpretations in those lanes.

It is increasingly held back by the fact that many packets still point to evidence through sibling-worktree paths rather than a canonical reference model.

In plain language:

- lane structure is getting ahead of evidence portability
- proof-language is getting more honest
- the remaining archive-quality gap is becoming more operational and less conceptual

## Best next move

The highest-value next cleanup is not another isolated packet wording fix.

It is a canonical-reference triage pass.

The shortest high-yield sequence is:

1. choose the largest foreign root first:
   `annual-report-research-new-lanes`
2. identify which current-repo packets most often depend on it
3. decide lane by lane whether to:
   - repoint links to the documented offload-manifest / resolver model when the evidence was intentionally offloaded
   - repoint links to the correct current canonical local root when the evidence still exists locally in a non-offloaded form
   - or explicitly mark the packet as inherited and not yet canonically normalized
4. repeat for:
   - `annual-report-research-energy-buildout`
   - `annual-report-research-footwear-dept-audit`
   - `annual-report-research-cli8-middle-layer`

## Concrete Progress From This Pass

This pass did not solve the whole portability problem.

It did complete one useful normalization step:

- the CLI 8 synthesis page now links to current-repo packet locations
- the CLI 8 middle-layer index now links to the current-repo synthesis, slate, quarter snapshot, CSV index, and packet locations
- the CLI 8 handoff note now points its deliverable links at the current repo rather than the sibling worktree

It also completed one note-layer normalization step:

- handoff headers that previously named only the source side-worktree now distinguish:
  - `Source repo`
  - `Current integrated repo`
- this keeps historical provenance while reducing the chance that a reader mistakes the side-worktree for the current canonical archive
- after that note-layer cleanup, the remaining non-raw sibling-root footprint is materially smaller and more concentrated in packet and ledger surfaces rather than batch-header metadata

It also completed one packet-navigation cleanup step:

- a focused CLI 8 subset of current company packets now points its local `company-profile.md` and `source-ledger.md` links at `annual-report-research`
- that repair covered `Ferguson`, `Arrow`, `Avnet`, `Applied Industrial`, `MSC`, `Fastenal`, `Core & Main`, `Watsco`, and `DNOW`
- this did not change raw evidence provenance, but it did remove another layer of unnecessary side-worktree navigation for readers inside the current repo

It also completed one source-ledger prose cleanup step:

- a fifteen-company imported CLI 8 subset no longer names the imported sibling worktree in reconciliation-note prose
- those ledgers now describe the situation more directly: the raw proof still lives in an imported raw workspace rather than the current repo raw tree
- this keeps the packet honest about raw-location limits without treating the old imported repo name as part of the live reader surface

It also completed one handoff-header provenance cleanup step:

- the bulk handoff notes no longer name old side-worktree repo roots directly in their headers
- those notes now preserve provenance through:
  - `Source snapshot`
  - branch
  - commit hash
- this keeps the integration trail readable without leaving dozens of one-off source-repo names as part of the current archive surface

It also completed a small final-leftover cleanup step:

- the stale energy-buildout location note now points readers at the current integrated note files in `annual-report-research`
- the `SBA Communications` source ledger no longer names legacy side-worktree roots in reconciliation prose
- the `IBIS` alignment note now refers to the archive as the annual-report evidence layer rather than naming the older side-worktree directly
- the remaining non-raw sibling-root residue is now concentrated in deliberate historical documentation rather than active packet or handoff surfaces

What did not change:

- packet-level raw citations that still point into `annual-report-research-cli8-middle-layer/raw/...`
- other inherited packet and ledger references tied to `annual-report-research-new-lanes`, `annual-report-research-energy-buildout`, and `annual-report-research-footwear-dept-audit`

So the practical outcome is narrower and more honest:

- reader-facing CLI 8 navigation is cleaner
- handoff-note provenance is clearer
- a first packet-level local-document subset is cleaner
- a first imported-source-ledger subset is cleaner
- the bulk handoff-header residue is now cleaner
- several narrow leftover notes are cleaner
- packet-level provenance cleanup is still a remaining archive task

## What Remains After These Passes

After the latest cleanup passes, the remaining non-raw sibling-root references are concentrated in three intentional files:

- `notes/cross-repo-evidence-portability-audit-2026-08-11.md`
- `notes/new-lanes-raw-blob-offload-2026-08-10.md`
- `notes/legacy-root-reference-audit-2026-08-11.md`

That remaining residue is different from the earlier portability problem.

It is now mostly:

- audit language that names the roots being measured
- historical offload documentation that records the original worktree and raw-tree names

In plain language:

- the broad cleanup debt is no longer spread across live packet navigation and handoff surfaces
- the remaining old-root names are now mostly part of explicit historical recordkeeping

## Highest-Value Endgame Interpretation

At this stage of the wrap-up, the canonical-reference gap should be treated as one of the main blockers to a fully clean closeout.

Not because:

- the research is missing

But because:

- the archive is increasingly good enough that portability and auditability are now the weaker layer

That means a final closeout that ignores canonical path normalization would risk leaving:

- strong synthesis
- mostly real packets
- but an unnecessarily confusing evidence surface for the next worker

## Bottom line

The repo is not just missing a few filings.

It still has a large canonical-reference gap.

The current state is:

- strong on interpretation
- meaningful on packet coverage
- intentionally offloaded for heavy raw storage
- still fragmented on how packets point to that evidence

That is one of the main remaining barriers to calling the original archive goal fully closed as of `2026-08-11`.
