# Meaty End-To-End Insight Goal

Date: 2026-08-11
Repo: `annual-report-research`

## What This Repo Is Supposed To Become

Build `annual-report-research` into a source-grounded pattern library for how the economy is changing.

This repo should not stop at:

- downloading annual reports
- collecting quarterly filings
- summarizing one company at a time
- filling coverage rows

It should use company filings as raw evidence for a bigger job:

- identifying consumer trends
- identifying cultural and societal shifts
- identifying industrial and operating pressures
- identifying technical and workflow dependencies
- identifying who owns the customer relationship
- identifying who carries the burden stack
- identifying what patterns repeat across companies
- identifying what is early, real, fragile, or breaking

The finished system should let a reader move from a source document to a concrete conclusion about how demand, cost, labor, trust, regulation, infrastructure, health, media, lifestyle, and capital intensity are changing.

## The End-To-End Goal

The goal is to convert company packets into evidence-backed explanations of the world.

That means the output is not just:

- `Company X grew revenue`
- `Industry Y has tailwinds`
- `Theme Z looks interesting`

The output should instead answer:

1. `What is happening?`
2. `How do we know?`
3. `Why is it happening?`
4. `Who benefits?`
5. `Who absorbs the pressure?`
6. `What concrete facts support that claim?`
7. `What should we watch next to see if the pattern strengthens or breaks?`

The standard evidence chain is:

`source document -> exact fact -> company packet -> company strategy read -> lane comparison -> cross-company pattern -> plain-English insight -> watchlist and thesis breaker`

If a writeup does not complete that chain, it is still intermediate work.

## Core Output Types

Every serious lane should produce all of these:

### 1. Source-Complete Company Packets

Each flagship company should have:

- AnnualReports taxonomy confirmation
- annual report coverage for the target year
- annual filing coverage for the target year
- latest three reported quarters as of the run date
- exact operating facts
- company-level strategy read
- plain-English operating model
- key constraints
- burden-versus-beneficiary interpretation
- next filing watchlist

### 2. Lane-Level Explanation

Each lane should explain:

- what customer or institutional need creates demand
- how the lane makes money
- what keeps the system running
- where margin quality comes from
- which players own the relationship
- which players carry labor, property, reimbursement, inventory, debt, regulation, or execution burden
- what metrics prove the lane is healthy or under stress
- what changes in the lane say about the wider economy

### 3. Cross-Company Proof Memos

Each important pattern should be turned into a proof page with:

- a plain claim
- exact facts from multiple companies
- what each fact proves
- the causal chain
- the stronger plain-English conclusion
- disconfirming evidence or thesis breakers
- next metrics and next names to test

### 4. Curiosity And Aha Pages

The work should surface:

- surprising observations
- unresolved tensions
- weak signals that may become larger themes
- contradictions between companies
- adjacent sectors that could sharpen the claim

## What Counts As A Good Insight

A good insight is not a slogan.

It is a concrete statement that connects exact company facts to a larger pattern.

It should be possible to write every major insight in this shape:

`Because {exact fact} at {company} and {exact fact} at {company}, this suggests {plain-English conclusion}. The conclusion matters because {economic meaning}. It weakens if {specific metric or event}.`

That structure forces the work to stay grounded.

## What Kinds Of Insights The Repo Should Extract

The repo should explicitly hunt for:

- consumer demand shifts
- selective spending behavior
- loyalty, membership, and repeat-use systems
- fandom, identity, and participation economics
- occasion and lifestyle consumption
- aging-driven care needs
- care moving outside the hospital
- labor and staffing pressure
- reimbursement and payer friction
- trust, proof, safety, and verification demand
- hidden infrastructure layers behind software and AI
- AI-driven physical-capacity strain
- capital intensity and balance-sheet burden
- real estate usefulness versus impairment
- regulation and policy as part of the business model
- commodity-chain bottlenecks and passthrough
- media attention ownership versus media routing helpers
- taxonomy blind spots where the category hides the real business

## The Reader Standard

The archive should help a curious reader understand:

- what changed
- how the companies reveal it
- why the pattern repeats
- what examples make it concrete
- what the implications are for households, businesses, patients, workers, operators, and investors

The writing should stay:

- simple
- concrete
- source-backed
- non-cliche
- non-jargony

It should explain the dots, not just place them near each other.

## What To Avoid

Avoid:

- broad themes with no company facts
- company lists pretending to be synthesis
- sector labels used as explanations
- management language copied without interpretation
- one-company conclusions presented as cross-company truths
- trend claims without metrics
- shallow summary pages that do not explain the economic mechanism

## Required Closeout Standard

Every coherent batch should end with:

- commit hash
- companies completed
- companies partial
- lane summary
- company-level insights
- cross-company themes
- strongest concrete signals
- aha moments
- thesis breakers
- next watch metrics
- next recommended names
- raw blob status
- remote main status

## Reusable Master Instruction

Use this when handing a lane to another thread:

```text
Your job is not to sample one company. Your job is to open a genuinely new research frontier in annual-report-research.

Cover the assigned AnnualReports.com industries end to end using 2025 annual reports plus the latest three reported quarters as of 2026-08-10. Treat AnnualReports.com as taxonomy and archive confirmation, but use company IR and SEC as authoritative when AnnualReports lags.

Aim to complete 4-8 flagship company packets when the lane supports it. Each company must produce both a source-complete packet and a thematic interpretation. Avoid dozens of shallow starts.

The work is not just source gathering. The main output is insight extraction. Use the company packets to identify:
- consumer trends
- cultural and societal shifts
- industrial and operating pressures
- technical and workflow dependencies
- who owns the relationship
- who carries the burden
- which patterns repeat across companies
- which claims are concrete and which remain early

For every lane, produce:
- source-complete company packets
- lane summary
- cross-company themes
- concrete proof pages
- aha moments and curiosity questions
- thesis breakers
- watchlist metrics
- recommended next names

Before stopping, leave a handoff with:
- completed companies
- partial companies
- key themes
- strongest cross-company signals
- exact next targets
- raw blob status
- commit hash
```

## Relationship To The Rest Of The System

Use this document with:

- [master-insight-extraction-goal-2026-08-11.md](master-insight-extraction-goal-2026-08-11.md)
- [insight-extraction-templates-2026-08-11.md](insight-extraction-templates-2026-08-11.md)
- [lane-end-to-end-execution-runbook-2026-08-11.md](lane-end-to-end-execution-runbook-2026-08-11.md)

This page defines the ambition level. The other documents define how to execute it.
