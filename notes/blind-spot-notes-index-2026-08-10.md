# Blind-Spot Notes Index

Date: 2026-08-10
Repo: `annual-report-research`

## Packet Inputs Used

- the blind-spot note set itself, including startup, handoff, audit, shortlist, roster, and wrap-up control files
- the surrounding `indexes/` control layer that defines ownership rules, assignment logic, and company-priority decisions
- the repo requirement that a reusable note index should help another worker recover the lane logic without reopening old thread history
- the insight-system standard that control notes should still show how they connect to lane execution, comparison work, and proof-building
- the continuation requirement that a future thread should know reading order, file purpose, and when to use each note

## Purpose

This note is the one-screen index for blind-spot-lane notes.

Use it when another thread needs the narrative operating context for the blind-spot lane rather than only the control files under `indexes/`.

## Notes in use

### 0. Quickstart

Use:

- `notes/blind-spot-quickstart-2026-08-10.md`

When to read it:

- when a new worker needs the fastest possible startup path
- when the first question is simply where to begin
- when the next worker needs the first keep-versus-leave decision in one screen
- when a worker needs the link out to the short ownership rule before claiming a company

### 1. Operating handoff

Use:

- `notes/blind-spot-handoff-2026-08-10.md`

When to read it:

- when a new worker needs the current operating boundary
- when a new worker needs the read order for the lane
- when a new worker needs the platform-versus-recurring-attention distinction in plain language

### 2. Status audit

Use:

- `notes/blind-spot-status-audit-2026-08-10.md`

When to read it:

- when a worker needs to know what is governance-complete versus research-open
- when a worker needs to know whether the blind-spot lane is operationally aligned
- when a worker needs the current "done versus still open" reading of this lane

### 3. Next actions

Use:

- `notes/blind-spot-next-actions-2026-08-10.md`

When to read it:

- when a worker is ready to move from lane setup into actual research execution
- when the next worker needs the highest-value current blind-spot moves in one place
- when the next worker needs a filter against low-payoff packet sprawl

### 4. Candidate shortlist

Use:

- `notes/blind-spot-candidate-shortlist-2026-08-10.md`

When to read it:

- when the worker wants actual company groups already supported by repo evidence
- when the worker needs to know which names fit the AnnualReports blind spot rather than normal sector backfill
- when the worker needs a concrete "what should this thread own?" answer

### 5. Take-don't-take roster

Use:

- `notes/blind-spot-take-dont-take-roster-2026-08-10.md`

When to read it:

- when another thread needs a one-screen company assignment answer
- when the question is which names this thread should explicitly take versus leave
- when the worker needs the shortest practical roster without reading the longer control files

### 6. Wrap-up checklist

Use:

- `notes/blind-spot-wrap-up-checklist-2026-08-10.md`

When to read it:

- when the question is what still remains before the framework is done
- when the question is how much substantive blind-spot research still remains
- when a worker needs a strict distinction between framework completion and research completion

### 7. Framework completion audit

Use:

- `notes/blind-spot-framework-completion-audit-2026-08-10.md`

When to read it:

- when a worker needs the evidence-based answer for whether the framework layer is actually done
- when the question is what is proven complete versus merely likely complete
- when another thread needs a durable audit record before moving from governance cleanup into research expansion

## How this fits with the control layer

Use the files under `indexes/` for:

- ownership rules
- assignment decisions
- queue selection
- lane maps
- extension shortlists
- machine-readable control paths

Those control files now also carry the explicit negative screen that thin, stale, awkward, sparse, or incomplete browse-tree page quality is not a claim reason by itself.

The mature infrastructure lanes now also have dedicated shortlist files under `indexes/` that should be read before taking another company in:

- behind-the-shelf infrastructure
- control-layer infrastructure
- hidden connectivity
- physical execution and embedded workflow

Use the files in this note for:

- handoff context
- current-state interpretation
- branch-agnostic operating orientation

Use the top-level synthesis memos under `extracted/themes/` for:

- default routing before choosing a lane
- fast classification of consumer and cultural cases
- fast classification of infrastructure and hidden-layer cases

The two current routing cores are:

- `extracted/themes/consumer-behavior-blind-spot-comparison-core-2026-08-10.md`
- `extracted/themes/infrastructure-blind-spot-comparison-core-2026-08-10.md`

## Recommended use order

1. `indexes/annualreports-noncovered-master-index-2026-08-10.md`
2. `indexes/annualreports-blind-spot-ownership-map-2026-08-10.md`
3. `indexes/annualreports-noncovered-ownership-rule-2026-08-10.md`
4. `notes/blind-spot-notes-index-2026-08-10.md`
5. `notes/blind-spot-quickstart-2026-08-10.md`
6. `extracted/themes/consumer-behavior-blind-spot-comparison-core-2026-08-10.md`
7. `extracted/themes/infrastructure-blind-spot-comparison-core-2026-08-10.md`
8. `notes/blind-spot-handoff-2026-08-10.md`
9. `notes/blind-spot-status-audit-2026-08-10.md`
10. `notes/blind-spot-next-actions-2026-08-10.md`
11. `notes/blind-spot-candidate-shortlist-2026-08-10.md`
12. `notes/blind-spot-take-dont-take-roster-2026-08-10.md`
13. `notes/blind-spot-wrap-up-checklist-2026-08-10.md`
14. `notes/blind-spot-framework-completion-audit-2026-08-10.md`

## Bottom line

If the `indexes/` files say what this lane owns, these note files explain how to operate it from the current repo state.

They should be read with the same assumption: the blind-spot lane is for system misclassification, not for rescuing weak-looking industry pages.

## Insight-System Maintenance

When you need to confirm that the blind-spot note bundle, reading order, and continuation surfaces still line up before using this index as the entrypoint, use:

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

- Does this index make the blind-spot control layer easier to navigate for a new worker without requiring old chat history?
- Can a skeptical reader tell the difference between the control files under `indexes/` and the operating-context notes listed here?
- Does the file show a usable reading order that leads from ownership rules to action, not just a loose file inventory?
- What would show that the index still leaves the next worker unsure which note to read first or why the blind-spot lane exists?
