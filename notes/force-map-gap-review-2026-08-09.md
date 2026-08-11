# Force Map Gap Review

Date: 2026-08-09

## Packet Inputs Used

- the `ibis-industries/forces/` slug set used as the external force reference
- `indexes/force-map.csv` inside `annual-report-research` as the bridge record being audited
- the current company-anchor choices already mapped to specific force slugs
- the distinction between slug-level coverage completion and deeper confidence or breadth inside each mapped force
- the archive rule that future collection should improve force depth where useful instead of manufacturing new gaps after slug coverage is complete

## What this checks

This note compares:

- `ibis-industries/forces/` force slugs
- `indexes/force-map.csv` coverage inside `annual-report-research`

## Current result

Mapped force slugs: `20`

Unmapped force slugs: `0`

## Why these remain open

The current annual-report archive is strong in:

- large-cap technology
- financials
- healthcare
- industrial infrastructure
- operational services
- defensive consumer goods

It is weaker in:

- additional direct agriculture, food-processing, and homebuilding labor-bottleneck operators
- broader immigration-sensitive coverage outside the current BrightView anchor

Recently closed:

- `the-labor-squeeze` is now mapped through Comfort Systems USA, with ABM, HCA, and Cintas as supporting evidence.
- `the-graying-market` is now mapped through Brookdale Senior Living, with UnitedHealth, HCA, and Abbott as supporting evidence.
- `the-immigration-squeeze` is now mapped through BrightView Holdings, with adjacent labor-heavy operators such as ABM, Waste Management, and UPS serving as weaker secondary context rather than primary anchors.

So the force-map bridge is now fully covered at the slug level.

## What remains to improve

The remaining work is no longer to close a missing slug. It is to widen confidence and breadth:

- add more direct immigration-sensitive operators beyond BrightView
- add more direct age-linked operators beyond Brookdale
- deepen transcript and IR coverage where the filing chain is strong but management-tone coverage is still thin

## Recommendation

Keep the force-map itself high-confidence and complete.

Use future collection passes to improve depth around already mapped forces rather than to patch missing slugs.

## Insight-System Maintenance

When you need to confirm that this force-map gap review, the bridge-layer notes, and the broader continuation surfaces still line up before relying on this audit, use:

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

- Does this note identify the exact two source sets being compared when it claims the force-map bridge is complete at the slug level?
- Can a skeptical reader see the difference between “no missing slugs” and “plenty of room to deepen the evidence around mapped slugs”?
- Does the recommendation follow from the audited result rather than from a generic desire to keep collecting?
- What contradiction in `indexes/force-map.csv` or the force-slug list would weaken the claim of full slug-level coverage?
