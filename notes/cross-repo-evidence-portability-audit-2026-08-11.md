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

- distribution and middle-layer index rows still point into `annual-report-research-cli8-middle-layer`
- many packet source pointers and ledgers still point into `annual-report-research-new-lanes`
- other lanes still point into `annual-report-research-footwear-dept-audit` or `annual-report-research-energy-buildout`

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

## Bottom line

The repo is not just missing a few filings.

It still has a large canonical-reference gap.

The current state is:

- strong on interpretation
- meaningful on packet coverage
- intentionally offloaded for heavy raw storage
- still fragmented on how packets point to that evidence

That is one of the main remaining barriers to calling the original archive goal fully closed as of `2026-08-11`.
