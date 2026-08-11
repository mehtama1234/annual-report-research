#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

required_files=(
  "notes/insight-extraction-hub-2026-08-11.md"
  "notes/master-insight-extraction-goal-2026-08-11.md"
  "notes/insight-extraction-templates-2026-08-11.md"
  "notes/insight-artifact-manifest-2026-08-11.md"
  "notes/insight-driven-next-lane-queue-2026-08-11.md"
  "analysis/cross-sector/company-level-strategy-insight-guide-2026-08-10.md"
  "analysis/cross-sector/industry-level-strategy-guide-2026-08-10.md"
  "analysis/cross-sector/concrete-insights-and-curiosity-map-2026-08-10.md"
  "analysis/cross-sector/metric-glossary-and-watchlist-2026-08-10.md"
  "analysis/cross-sector/thesis-breaker-index-2026-08-10.md"
  "analysis/cross-sector/aha-moments-and-curiosity-questions-2026-08-10.md"
  "analysis/cross-sector/ai-physical-capacity-proof-2026-08-10.md"
  "analysis/cross-sector/hidden-operating-infrastructure-proof-2026-08-10.md"
  "analysis/cross-sector/selective-consumer-proof-2026-08-10.md"
  "analysis/cross-sector/fandom-identity-participation-proof-2026-08-10.md"
  "analysis/cross-sector/recreation-lifestyle-occasion-demand-comparison-2026-08-11.md"
  "analysis/cross-sector/healthcare-outside-hospital-proof-2026-08-10.md"
  "analysis/cross-sector/healthcare-burden-vs-workflow-comparison-2026-08-11.md"
  "analysis/cross-sector/trust-as-paid-product-proof-2026-08-10.md"
  "analysis/cross-sector/relationship-owner-vs-burden-carrier-proof-2026-08-10.md"
  "analysis/cross-sector/commodity-chain-proof-2026-08-10.md"
  "analysis/cross-sector/taxonomy-blind-spots-proof-2026-08-10.md"
  "site/index.html"
  "site/concrete-insights.html"
)

required_patterns=(
  "notes/insight-extraction-hub-2026-08-11.md:Workflow For A New Company"
  "notes/insight-extraction-hub-2026-08-11.md:Workflow For A New Lane"
  "notes/insight-extraction-hub-2026-08-11.md:Workflow For A New Theme"
  "notes/master-insight-extraction-goal-2026-08-11.md:No broad claim without concrete filing evidence"
  "notes/insight-extraction-templates-2026-08-11.md:Company Packet Template"
  "notes/insight-extraction-templates-2026-08-11.md:Run Closeout Template"
  "notes/insight-artifact-manifest-2026-08-11.md:Required Insight System Layers"
  "notes/insight-artifact-manifest-2026-08-11.md:Proof Memo Inventory"
  "notes/insight-driven-next-lane-queue-2026-08-11.md:Best Immediate Next Move"
  "analysis/cross-sector/healthcare-burden-vs-workflow-comparison-2026-08-11.md:Burden Versus Cleaner Workflow Map"
  "analysis/cross-sector/recreation-lifestyle-occasion-demand-comparison-2026-08-11.md:Occasion Versus Routine Demand Map"
  "analysis/cross-sector/recreation-lifestyle-occasion-demand-comparison-2026-08-11.md:Brand Relationship Versus Inventory And Support Burden"
  "analysis/cross-sector/recreation-lifestyle-occasion-demand-comparison-2026-08-11.md:Queue Status"
  "analysis/cross-sector/healthcare-outside-hospital-proof-2026-08-10.md:healthcare-burden-vs-workflow-comparison-2026-08-11.md"
  "site/concrete-insights.html:Recreation lifestyle and occasion demand comparison"
  "site/concrete-insights.html:Healthcare burden versus workflow comparison"
  "site/index.html:Insight extraction hub"
  "site/index.html:Insight-driven next lane queue"
  "site/concrete-insights.html:Insight extraction hub"
  "site/concrete-insights.html:Insight-driven next lane queue"
)

for path in "${required_files[@]}"; do
  if [[ ! -s "$path" ]]; then
    printf 'missing or empty required file: %s\n' "$path" >&2
    exit 1
  fi
done

for item in "${required_patterns[@]}"; do
  path="${item%%:*}"
  pattern="${item#*:}"
  if ! rg -q --fixed-strings "$pattern" "$path"; then
    printf 'missing required pattern in %s: %s\n' "$path" "$pattern" >&2
    exit 1
  fi
done

printf 'insight-system-ok\n'
