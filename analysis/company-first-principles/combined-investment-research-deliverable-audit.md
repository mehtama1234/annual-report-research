# Combined investment research deliverable audit

Research date: `2026-09-16`

The end-to-end goal names a set of mature-system deliverables in addition to
the 13 definition-of-done requirements. This audit checks that each deliverable
has an authoritative artifact, a stated boundary, and a reproducible
verification route. A `checked` or `usable` deliverable means the artifact and
control exist; it does not mean every underlying investment conclusion is
proven.

The structured audit is the [deliverable-audit CSV](data/combined-investment-research-deliverable-audit.csv).

## Current conclusion

The deliverable architecture is present and checked across 98 rows. The [active-pilot packet coverage matrix](combined-investment-research-active-pilot-packet-coverage-2026-09-15.md)
now makes the annual, quarter, results, IR, call, ledger, dossier, and legal-entity
coverage boundaries explicit for the selected pilots. The [owner-cash and denominator index](combined-investment-research-owner-cash-denominator-index.md)
now provides one traversal point for the three pilot denominator layers. The force,
valuation, macro, owner-cash, and capital-flow layers remain qualified or
partial where the underlying source or denominator is incomplete. The audit
therefore distinguishes system existence from proof grade: a named-cash table,
for example, can exist while its rows remain qualified or unresolved.

For the retail denominator specifically, the [owner-cash input schema](capital-flow-retail-owner-cash-input-schema-2026-09-16.md)
is now the authoritative CA-06 field specification: it records the observed,
partial, and missing inputs needed before normalized owner cash can be promoted.

The Lyn Alden/macro row now also routes to the [through-cycle causal-test
protocol](combined-investment-research-through-cycle-causal-test-protocol-2026-09-16.md),
which defines the promotion gate for repeated observations and confound
controls rather than treating regime consistency as causal proof.

The reviewer layer now also has a machine-readable five-theme status map,
checked by the pilot verifier, so the representative writeup, connected pilot
route, current grade, and decisive open question cannot drift apart in the
reader-facing guide.

The capital-flow and named-cash rows now point to the ARI closing-payment
mechanics, AUM outflow classification, and bounded post-close proof search. This makes the distinction
between a contractually specified settlement object and an observed cash
receipt visible from the deliverable index itself; the public-search result is
`searched-negative`, not a claim that private closing records do not exist.

The audit also requires the reusable verification controls to exist: the pilot,
deliverable, reader-route, internal-link, and browser-review checks. The pilot
verifier now additionally enforces the next-evidence queue's result class for
each open test and resolves every declared queue source artifact. Their
presence makes the verification route reproducible; passing them still does
not upgrade an incomplete investment claim.

The [current dated browser-review record](combined-investment-research-reader-browser-review-2026-09-17.md)
preserves the successful Chromium runtime scope and its boundary: it verifies
reader navigation and confidence presentation, including the three new Q-10
diagnostic links, not the truth of the underlying investment claims.

The new [next-cycle candidate expansion](combined-investment-research-next-cycle-candidate-expansion-2026-09-16.md)
is included as D-18. It is a qualified sequencing deliverable: it makes the
post-pilot move-on path reproducible, but it does not promote any candidate or
close the unresolved owner-cash denominator.

The insurance statutory named-asset lane is included as D-19. Its Apollo/Athene
and KKR/Global Atlantic/Accordia routes are independently checked as
legal-entity and row-level cash-back proxies; borrower cash, liability-adjusted
spread, remittance, waterfall, and final return remain outside the promoted
proof grade.

The asset-backed collateral lane is included as D-20. Its URI work separates
facility availability, AR collateral-pool coverage, fleet assets, and ABL
formula definitions from the missing populated certificate, eligible-collateral
schedule, reserves, legal availability, and lifecycle return.

The expansion-lane QoE and financial-shenanigans overlay is included as D-21.
It extends the diagnostic method beyond the original pilots while preserving
the no-fraud-score and no-owner-cash-promotion boundaries.

The official FPL Distribution Inspection PSC source refresh is included as
D-22. It records the first next-cycle public-source execution result and
preserves the distinction between rate-class recovery authority and observed
category customer cash or source-of-funds allocation.

The MF1 public SEC wrapper and collateral route refresh is included as D-23.
It strengthens the Apollo-affiliated structured-credit source route while
preserving the missing Athene ownership, remittance, liability-cost, and
common-owner-return gates.

The latest insurance refreshes deepen, but do not replace, D-19. The [insurance
named-asset proof ladder](combined-investment-research-insurance-named-asset-proof-ladder-2026-09-17.md)
puts AP Aristotle, AMAPS, Concord, Bear Financing, Intel, and Orange on one
comparable evidence surface. The [private-credit borrower proof ladder](combined-investment-research-private-credit-borrower-proof-ladder-2026-09-17.md)
then connects statutory ownership, borrower/use evidence, and facility-purpose
evidence across Bear Financing, Concord, and Ares/Frontline. These artifacts
improve cross-route comparability and QoE/financial-integrity controls, but do
not close Q-12's settlement, remittance, liability-cost, borrower-cash, or
common-owner-return requirements.

## Review rule

For each row, verify the authoritative artifact, read the boundary, and run the
listed check. Do not promote a deliverable merely because its file exists or a
pilot arithmetic test passes. The linked [completion audit](combined-investment-research-completion-audit.md)
remains the controlling requirement-by-requirement status, while this file
prevents the broader deliverable list from disappearing behind the pilot
ledger.
