#!/usr/bin/env python3
"""Local HTML viewer for extracted annual-report company Markdown files."""

from __future__ import annotations

import html
import os
import re
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
EXTRACTED = ROOT / "extracted"
FIRST_PRINCIPLES = ROOT / "analysis" / "company-first-principles"
PORT = int(os.environ.get("COMPANY_REPORT_PORT", "8765"))
HOST = os.environ.get("COMPANY_REPORT_HOST", "0.0.0.0")


def company_dirs() -> list[Path]:
    dirs = []
    for packet in EXTRACTED.glob("*/*/*/company-packet.md"):
        dirs.append(packet.parent)
    return sorted(dirs, key=lambda p: str(p.relative_to(EXTRACTED)).lower())


def title_from_slug(slug: str) -> str:
    fixes = {"inc": "Inc.", "corp": "Corp.", "co": "Co.", "plc": "PLC", "ltd": "Ltd.", "nv": "N.V.", "sa": "S.A."}
    words = []
    for part in slug.replace("_", "-").split("-"):
        words.append(fixes.get(part, part.capitalize()))
    return " ".join(words)


def nav_html(active: str | None = None) -> str:
    rows = []
    for directory in company_dirs():
        rel = directory.relative_to(EXTRACTED)
        sector, industry, company = rel.parts
        analysis = FIRST_PRINCIPLES / rel / "company-analysis.md"
        href = (
            f"/analysis/{quote(str(rel))}/company-analysis.md"
            if analysis.exists()
            else f"/company/{quote(str(rel))}/company-packet.md"
        )
        active_class = " active" if str(rel) == active else ""
        rows.append(
            f'<a class="company-link{active_class}" href="{href}" '
            f'data-search="{html.escape(str(rel).lower())}">'
            f'<strong>{html.escape(title_from_slug(company))}</strong>'
            f'<span>{html.escape(sector.replace("-", " ").title())} / '
            f'{html.escape(industry.replace("-", " ").title())}</span></a>'
        )
    return "\n".join(rows)


def inline_md(text: str) -> str:
    value = html.escape(text)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', value)
    return value


def render_table(lines: list[str]) -> str:
    parsed = [[inline_md(cell.strip()) for cell in line.strip().strip("|").split("|")] for line in lines]
    if not parsed:
        return ""
    head, *body = parsed
    out = ["<table><thead><tr>"]
    out.extend(f"<th>{cell}</th>" for cell in head)
    out.append("</tr></thead><tbody>")
    for row in body[1:] if body and all(set(cell.replace("-", "").strip()) <= {":", ""} for cell in body[0]) else body:
        out.append("<tr>")
        out.extend(f"<td>{cell}</td>" for cell in row)
        out.append("</tr>")
    out.append("</tbody></table>")
    return "".join(out)


def render_markdown(markdown: str) -> str:
    out: list[str] = []
    lines = markdown.splitlines()
    i = 0
    in_list = False
    in_code = False
    code_lines: list[str] = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            if in_code:
                out.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
                code_lines = []
                in_code = False
            else:
                in_code = True
            i += 1
            continue

        if in_code:
            code_lines.append(line)
            i += 1
            continue

        if not stripped:
            if in_list:
                out.append("</ul>")
                in_list = False
            i += 1
            continue

        if "|" in stripped and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", lines[i + 1]):
            table_lines = [line, lines[i + 1]]
            i += 2
            while i < len(lines) and "|" in lines[i].strip() and lines[i].strip():
                table_lines.append(lines[i])
                i += 1
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(render_table(table_lines))
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            if in_list:
                out.append("</ul>")
                in_list = False
            level = min(len(heading.group(1)), 4)
            out.append(f"<h{level}>{inline_md(heading.group(2))}</h{level}>")
            i += 1
            continue

        bullet = re.match(r"^[-*]\s+(.+)$", stripped)
        if bullet:
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline_md(bullet.group(1))}</li>")
            i += 1
            continue

        if in_list:
            out.append("</ul>")
            in_list = False
        out.append(f"<p>{inline_md(stripped)}</p>")
        i += 1

    if in_list:
        out.append("</ul>")
    if in_code:
        out.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
    return "\n".join(out)


def page_shell(title: str, content: str, active: str | None = None) -> bytes:
    body = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    :root {{ color-scheme: light; --ink: #181818; --muted: #666; --line: #ddd; --bg: #f5f5f2; --panel: #fff; --accent: #0b5cad; }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color: var(--ink); background: var(--bg); }}
    .layout {{ display: grid; grid-template-columns: 360px minmax(0, 1fr); min-height: 100vh; }}
    aside {{ position: sticky; top: 0; height: 100vh; overflow: auto; border-right: 1px solid var(--line); background: #ededeb; padding: 16px; }}
    main {{ min-width: 0; padding: 34px 44px 64px; }}
    .brand {{ display: flex; justify-content: space-between; gap: 12px; align-items: baseline; margin-bottom: 14px; }}
    .brand h1 {{ margin: 0; font-size: 18px; line-height: 1.2; }}
    .count {{ color: var(--muted); font-size: 13px; white-space: nowrap; }}
    input {{ width: 100%; height: 38px; border: 1px solid #c9c9c4; background: #fff; border-radius: 6px; padding: 0 10px; font: inherit; margin-bottom: 12px; }}
    .company-link {{ display: block; text-decoration: none; color: var(--ink); border: 1px solid transparent; border-radius: 6px; padding: 9px 10px; margin-bottom: 4px; }}
    .company-link:hover, .company-link.active {{ background: #fff; border-color: #d4d4cf; }}
    .company-link strong {{ display: block; font-size: 14px; line-height: 1.25; }}
    .company-link span {{ display: block; color: var(--muted); font-size: 12px; line-height: 1.3; margin-top: 3px; }}
    .doc {{ max-width: 1120px; background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 30px 36px; box-shadow: 0 1px 2px rgba(0,0,0,.04); }}
    .tabs {{ display: flex; gap: 8px; flex-wrap: wrap; margin: 0 0 18px; }}
    .tabs a {{ color: var(--accent); border: 1px solid #c8d7e8; border-radius: 6px; padding: 7px 10px; text-decoration: none; font-size: 14px; }}
    h1, h2, h3, h4 {{ line-height: 1.2; margin: 1.1em 0 .45em; }}
    h1:first-child {{ margin-top: 0; }}
    p, li {{ line-height: 1.58; }}
    code {{ background: #f0f0ed; border: 1px solid #deded8; border-radius: 4px; padding: 1px 4px; }}
    pre {{ overflow: auto; background: #202124; color: #f6f6f3; border-radius: 8px; padding: 14px; }}
    table {{ width: 100%; border-collapse: collapse; margin: 18px 0; font-size: 14px; }}
    th, td {{ border: 1px solid var(--line); padding: 8px 10px; vertical-align: top; }}
    th {{ background: #f0f0ed; text-align: left; }}
    a {{ color: var(--accent); }}
    @media (max-width: 900px) {{
      .layout {{ grid-template-columns: 1fr; }}
      aside {{ position: relative; height: 44vh; }}
      main {{ padding: 18px; }}
      .doc {{ padding: 22px; }}
    }}
  </style>
</head>
<body>
  <div class="layout">
    <aside>
      <div class="brand"><h1>Company Reports</h1><span class="count">{len(company_dirs())} packets</span></div>
      <input id="search" placeholder="Search company, sector, industry" autofocus>
      <nav id="company-list">{nav_html(active)}</nav>
    </aside>
    <main>{content}</main>
  </div>
  <script>
    const search = document.getElementById('search');
    const links = [...document.querySelectorAll('.company-link')];
    search.addEventListener('input', () => {{
      const q = search.value.toLowerCase().trim();
      for (const link of links) link.style.display = link.dataset.search.includes(q) ? '' : 'none';
    }});
  </script>
</body>
</html>"""
    return body.encode("utf-8")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path in {"/", "/companies"}:
            content = """<section class="doc"><h1>Individual Company Reports</h1>
<p>Use the search box to open any company packet. Entries with a first-principles note open to the <code>Analysis</code> tab first.</p>
<h2>Cluster Syntheses</h2>
<ul>
  <li><a href="/cluster/value-retail-cluster-synthesis.md">Value Retail Cluster Synthesis</a></li>
  <li><a href="/cluster/internet-software-control-cluster-synthesis.md">Internet Software And Control-Layer Cluster Synthesis</a></li>
  <li><a href="/cluster/built-environment-upkeep-cluster-synthesis.md">Built Environment Upkeep Cluster Synthesis</a></li>
  <li><a href="/cluster/industrial-access-mro-distribution-cluster-synthesis.md">Industrial Access And MRO Distribution Cluster Synthesis</a></li>
  <li><a href="/cluster/power-scarcity-grid-reliability-cluster-synthesis.md">Power Scarcity And Grid Reliability Cluster Synthesis</a></li>
  <li><a href="/cluster/healthcare-access-care-delivery-cluster-synthesis.md">Healthcare Access And Care Delivery Cluster Synthesis</a></li>
  <li><a href="/cluster/capital-allocation-private-markets-cluster-synthesis.md">Capital Allocation And Private Markets Cluster Synthesis</a></li>
  <li><a href="/cluster/where-dollar-pool-is-flowing-capital-platforms.md">Where The Dollar Pool Is Flowing Across Capital Platforms</a></li>
  <li><a href="/cluster/capital-flow-real-economy-funding-map.md">Capital Flow Real-Economy Funding Map</a></li>
  <li><a href="/cluster/capital-flow-destination-matrix.md">Capital Flow Destination Matrix</a></li>
  <li><a href="/cluster/capital-flow-to-real-economy-end-to-end-thesis.md">Capital Flow To Real-Economy End-To-End Thesis</a></li>
  <li><a href="/cluster/capital-flow-end-to-end-goal-and-answer-mechanism.md">Capital Flow End-To-End Goal And Answer Mechanism</a></li>
  <li><a href="/cluster/capital-flow-big-money-named-cash-end-to-end-goal-pass-1.md">Capital Flow Big-Money Named-Cash End-To-End Goal Pass 1</a></li>
  <li><a href="/cluster/capital-flow-meaty-end-to-end-goal-and-proof-workplan-pass-1.md">Capital Flow Meaty End-To-End Goal And Proof Workplan Pass 1</a></li>
  <li><a href="/cluster/capital-flow-big-picture-meaty-end-to-end-goal-pass-1.md">Capital Flow Big Picture Meaty End-To-End Goal Pass 1</a></li>
  <li><a href="/cluster/capital-flow-detailed-theme-and-subtheme-synthesis-pass-1.md">Capital Flow Detailed Theme And Subtheme Synthesis Pass 1</a></li>
  <li><a href="/cluster/capital-flow-long-form-theme-subtheme-report-pass-1.md">Capital Flow Long-Form Theme Subtheme Report Pass 1</a></li>
  <li><a href="/cluster/capital-flow-theme-package-with-exhibits-pass-1.md">Capital Flow Theme Package With Exhibits Pass 1</a></li>
  <li><a href="/cluster/capital-flow-annual-report-theme-opportunity-map-pass-1.md">Capital Flow Annual Report Theme Opportunity Map Pass 1</a></li>
  <li><a href="/cluster/capital-flow-annual-report-next-dig-queue-pass-1.md">Capital Flow Annual Report Next-Dig Queue Pass 1</a></li>
  <li><a href="/cluster/annual-report-broader-theme-expansion-map-pass-1.md">Annual Report Broader Theme Expansion Map Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-writing-architecture-pass-1.md">Annual Report Theme Writing Architecture Pass 1</a></li>
  <li><a href="/cluster/annual-report-long-form-draft-pass-1.md">Annual Report Long-Form Draft Pass 1</a></li>
  <li><a href="/cluster/annual-report-draft-review-chapter-selection-pass-1.md">Annual Report Draft Review And Chapter Selection Pass 1</a></li>
  <li><a href="/cluster/annual-report-power-scarcity-chapter-polish-pass-1.md">Annual Report Power Scarcity Chapter Polish Pass 1</a></li>
  <li><a href="/cluster/annual-report-capital-platforms-chapter-polish-pass-1.md">Annual Report Capital Platforms Chapter Polish Pass 1</a></li>
  <li><a href="/cluster/annual-report-industrial-uptime-chapter-polish-pass-1.md">Annual Report Industrial Uptime Chapter Polish Pass 1</a></li>
  <li><a href="/cluster/annual-report-healthcare-access-chapter-polish-pass-1.md">Annual Report Healthcare Access Chapter Polish Pass 1</a></li>
  <li><a href="/cluster/annual-report-built-environment-chapter-polish-pass-1.md">Annual Report Built Environment Chapter Polish Pass 1</a></li>
  <li><a href="/cluster/annual-report-digital-control-chapter-polish-pass-1.md">Annual Report Digital Control Chapter Polish Pass 1</a></li>
  <li><a href="/cluster/annual-report-value-retail-chapter-polish-pass-1.md">Annual Report Value Retail Chapter Polish Pass 1</a></li>
  <li><a href="/cluster/annual-report-final-theme-synthesis-package-pass-1.md">Annual Report Final Theme Synthesis Package Pass 1</a></li>
  <li><a href="/cluster/annual-report-reader-facing-essay-pass-1.md">Annual Report Reader-Facing Essay Pass 1</a></li>
  <li><a href="/cluster/annual-report-reader-exhibit-package-pass-1.md">Annual Report Reader Exhibit Package Pass 1</a></li>
  <li><a href="/cluster/annual-report-publication-readiness-review-pass-1.md">Annual Report Publication Readiness Review Pass 1</a></li>
  <li><a href="/cluster/annual-report-final-article-source-note-package-pass-1.md">Annual Report Final Article Source-Note Package Pass 1</a></li>
  <li><a href="/cluster/annual-report-final-publication-draft-pass-1.md">Annual Report Final Publication Draft Pass 1</a></li>
  <li><a href="/cluster/annual-report-public-citation-polish-pass-1.md">Annual Report Public Citation Polish Pass 1</a></li>
  <li><a href="/cluster/annual-report-public-citation-acquisition-queue-pass-1.md">Annual Report Public Citation Acquisition Queue Pass 1</a></li>
  <li><a href="/cluster/annual-report-paragraph-overclaim-review-pass-1.md">Annual Report Paragraph Overclaim Review Pass 1</a></li>
  <li><a href="/cluster/annual-report-reader-review-packet-pass-1.md">Annual Report Reader Review Packet Pass 1</a></li>
  <li><a href="/cluster/annual-report-public-citation-source-list-pass-1.md">Annual Report Public Citation Source List Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-expansion-next-dig-review-pass-1.md">Annual Report Theme Expansion Next-Dig Review Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-selection-work-order-pass-1.md">Annual Report Theme Selection Work Order Pass 1</a></li>
  <li><a href="/cluster/annual-report-power-grid-customer-cash-proof-work-order-pass-1.md">Annual Report Power/Grid Customer-Cash Proof Work Order Pass 1</a></li>
  <li><a href="/cluster/annual-report-complete-wrapup-synthesis-pass-1.md">Annual Report Complete Wrap-Up Synthesis Pass 1</a></li>
  <li><a href="/cluster/annual-report-extra-themes-first-principles-writeup-pass-1.md">Annual Report Extra Themes First-Principles Writeup Pass 1</a></li>
  <li><a href="/cluster/annual-report-all-sector-theme-coverage-review-pass-1.md">Annual Report All-Sector Theme Coverage Review Pass 1</a></li>
  <li><a href="/cluster/annual-report-all-sector-theme-expansion-pass-1.md">Annual Report All-Sector Theme Expansion Pass 1</a></li>
  <li><a href="/cluster/annual-report-undercovered-industry-deep-dive-work-order-pass-1.md">Annual Report Undercovered Industry Deep-Dive Work Order Pass 1</a></li>
  <li><a href="/cluster/annual-report-broad-theme-end-to-end-goal-pass-1.md">Annual Report Broad Theme End-To-End Goal Pass 1</a></li>
  <li><a href="/cluster/annual-report-integrated-meaty-end-to-end-goal-pass-1.md">Annual Report Integrated Meaty End-To-End Goal Pass 1</a></li>
  <li><a href="/cluster/annual-report-final-project-front-door-pass-1.md">Annual Report Final Project Front Door Pass 1</a></li>
  <li><a href="/cluster/annual-report-linked-reading-hub-pass-1.md">Annual Report Linked Reading Hub Pass 1</a></li>
  <li><a href="/cluster/annual-report-html-trend-crosswalk-pass-1.md">Annual Report HTML Trend Crosswalk Pass 1</a></li>
  <li><a href="/cluster/annual-report-html-integration-workbench-pass-1.md">Annual Report HTML Integration Workbench Pass 1</a></li>
  <li><a href="/cluster/annual-report-final-completion-audit-pass-1.md">Annual Report Final Completion Audit Pass 1</a></li>
  <li><a href="/cluster/annual-report-15-theme-first-principles-deep-dive-pass-1.md">Annual Report 15-Theme First-Principles Deep Dive Pass 1</a></li>
  <li><a href="/cluster/annual-report-what-else-theme-map-pass-1.md">Annual Report What Else Theme Map Pass 1</a></li>
  <li><a href="/cluster/annual-report-big-findings-takeaways-pass-1.md">Annual Report Big Findings And Takeaways Pass 1</a></li>
  <li><a href="/cluster/annual-report-15-theme-expanded-atlas-completion-pass-1.md">Annual Report 15-Theme Expanded Atlas Completion Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-pages-index-pass-1.md">Annual Report Theme Pages Index Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-services-cultural-consumption-html-expanded-pass-1.md">Annual Report Services Cultural Consumption HTML Expanded Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-consumer-goods-household-identity-html-expanded-pass-1.md">Annual Report Consumer Goods Household Identity HTML Expanded Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-broad-technology-html-expanded-pass-1.md">Annual Report Broad Technology HTML Expanded Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-real-estate-html-expanded-pass-1.md">Annual Report Real Estate HTML Expanded Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-healthcare-tools-html-expanded-pass-1.md">Annual Report Healthcare Tools HTML Expanded Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-industrial-uptime-html-expanded-pass-1.md">Annual Report Industrial Uptime HTML Expanded Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-basic-materials-html-expanded-pass-1.md">Annual Report Basic Materials HTML Expanded Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-ordinary-finance-html-expanded-pass-1.md">Annual Report Ordinary Finance HTML Expanded Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-capital-platforms-html-expanded-pass-1.md">Annual Report Capital Platforms HTML Expanded Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-power-scarcity-html-expanded-pass-1.md">Annual Report Power Scarcity HTML Expanded Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-healthcare-access-html-expanded-pass-1.md">Annual Report Healthcare Access HTML Expanded Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-value-retail-html-expanded-pass-1.md">Annual Report Value Retail HTML Expanded Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-energy-affordability-route-html-expanded-pass-1.md">Annual Report Energy Affordability Route HTML Expanded Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-built-environment-upkeep-html-expanded-pass-1.md">Annual Report Built Environment Upkeep HTML Expanded Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-digital-control-html-expanded-pass-1.md">Annual Report Digital Control HTML Expanded Pass 1</a></li>
  <li><a href="/cluster/annual-report-company-to-theme-matrix-pass-1.md">Annual Report Company-To-Theme Matrix Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-evidence-depth-scorecard-pass-1.md">Annual Report Theme Evidence Depth Scorecard Pass 1</a></li>
  <li><a href="/cluster/annual-report-theme-extraction-workbench-pass-1.md">Annual Report Theme Extraction Workbench Pass 1</a></li>
  <li><a href="/cluster/annual-report-blackrock-capital-platform-extraction-pass-1.md">Annual Report BlackRock Capital Platform Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-costco-value-retail-extraction-pass-1.md">Annual Report Costco Value Retail Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-walmart-value-retail-extraction-pass-1.md">Annual Report Walmart Value Retail Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-target-discretionary-stress-extraction-pass-1.md">Annual Report Target Discretionary Stress Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-dollar-general-value-retail-extraction-pass-1.md">Annual Report Dollar General Value Retail Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-burlington-off-price-value-extraction-pass-1.md">Annual Report Burlington Off Price Value Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-unitedhealth-healthcare-access-extraction-pass-1.md">Annual Report UnitedHealth Healthcare Access Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-cigna-healthcare-routing-extraction-pass-1.md">Annual Report Cigna Healthcare Routing Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-davita-care-site-extraction-pass-1.md">Annual Report DaVita Care Site Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-addus-home-care-extraction-pass-1.md">Annual Report Addus Home Care Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-option-care-infusion-extraction-pass-1.md">Annual Report Option Care Infusion Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-healthcare-access-cash-quality-bridge-pass-1.md">Annual Report Healthcare Access Cash Quality Bridge Pass 1</a></li>
  <li><a href="/cluster/annual-report-cloudflare-digital-control-extraction-pass-1.md">Annual Report Cloudflare Digital Control Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-akamai-digital-control-extraction-pass-1.md">Annual Report Akamai Digital Control Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-zscaler-digital-control-extraction-pass-1.md">Annual Report Zscaler Digital Control Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-fortinet-digital-control-extraction-pass-1.md">Annual Report Fortinet Digital Control Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-roblox-digital-control-extraction-pass-1.md">Annual Report Roblox Digital Control Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-digital-control-cash-quality-bridge-pass-1.md">Annual Report Digital Control Cash Quality Bridge Pass 1</a></li>
  <li><a href="/cluster/annual-report-home-depot-built-environment-extraction-pass-1.md">Annual Report Home Depot Built Environment Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-core-main-built-environment-extraction-pass-1.md">Annual Report Core & Main Built Environment Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-builders-firstsource-built-environment-extraction-pass-1.md">Annual Report Builders FirstSource Built Environment Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-lowes-built-environment-extraction-pass-1.md">Annual Report Lowe's Built Environment Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-sherwin-williams-built-environment-extraction-pass-1.md">Annual Report Sherwin-Williams Built Environment Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-built-environment-cash-quality-bridge-pass-1.md">Annual Report Built Environment Cash Quality Bridge Pass 1</a></li>
  <li><a href="/cluster/annual-report-jpmorgan-ordinary-finance-extraction-pass-1.md">Annual Report JPMorgan Ordinary Finance Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-amex-ordinary-finance-extraction-pass-1.md">Annual Report American Express Ordinary Finance Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-capital-one-ordinary-finance-extraction-pass-1.md">Annual Report Capital One Ordinary Finance Extraction Pass 1</a></li>
  <li><a href="/cluster/annual-report-undercovered-industry-theme-synthesis-pass-1.md">Annual Report Undercovered Industry Theme Synthesis Pass 1</a></li>
  <li><a href="/cluster/annual-report-final-integrated-theme-map-pass-1.md">Annual Report Final Integrated Theme Map Pass 1</a></li>
  <li><a href="/cluster/annual-report-integrated-final-publication-draft-pass-1.md">Annual Report Integrated Final Publication Draft Pass 1</a></li>
  <li><a href="/cluster/annual-report-integrated-final-reader-edit-pass-1.md">Annual Report Integrated Final Reader Edit Pass 1</a></li>
  <li><a href="/cluster/annual-report-integrated-priority1-citation-attachment-pass-1.md">Annual Report Integrated Priority-1 Citation Attachment Pass 1</a></li>
  <li><a href="/cluster/annual-report-integrated-priority2-citation-attachment-pass-1.md">Annual Report Integrated Priority-2 Citation Attachment Pass 1</a></li>
  <li><a href="/cluster/annual-report-integrated-priority3-citation-attachment-pass-1.md">Annual Report Integrated Priority-3 Citation Attachment Pass 1</a></li>
  <li><a href="/cluster/annual-report-integrated-final-citation-readiness-audit-pass-1.md">Annual Report Integrated Final Citation Readiness Audit Pass 1</a></li>
  <li><a href="/cluster/annual-report-integrated-sentence-metric-audit-pass-1.md">Annual Report Integrated Sentence Metric Audit Pass 1</a></li>
  <li><a href="/cluster/annual-report-integrated-final-public-formatting-pass-1.md">Annual Report Integrated Final Public Formatting Pass 1</a></li>
  <li><a href="/cluster/annual-report-integrated-release-link-check-pass-1.md">Annual Report Integrated Release Link Check Pass 1</a></li>
  <li><a href="/cluster/annual-report-integrated-draft-citation-overclaim-gate-pass-1.md">Annual Report Integrated Draft Citation Overclaim Gate Pass 1</a></li>
  <li><a href="/cluster/annual-report-integrated-15-theme-public-citation-queue-pass-1.md">Annual Report Integrated 15-Theme Public Citation Queue Pass 1</a></li>
  <li><a href="/cluster/annual-report-integrated-article-source-note-appendix-pass-1.md">Annual Report Integrated Article Source Note Appendix Pass 1</a></li>
  <li><a href="/cluster/annual-report-integrated-article-final-handoff-checklist-pass-1.md">Annual Report Integrated Article Final Handoff Checklist Pass 1</a></li>
  <li><a href="/cluster/capital-flow-insurance-statutory-named-asset-income-next-dig-pass-1.md">Capital Flow Insurance Statutory Named-Asset Income Next Dig Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-kkr-statutory-named-asset-selection-pass-1.md">Capital Flow Apollo KKR Statutory Named Asset Selection Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-row-level-proof-packet-pass-1.md">Capital Flow Apollo Athene Row-Level Proof Packet Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-aristotle-mixed-row-resolution-pass-1.md">Capital Flow Apollo Athene Aristotle Mixed Row Resolution Pass 1</a></li>
  <li><a href="/cluster/capital-flow-power-grid-data-center-customer-cash-map-pass-1.md">Capital Flow Power Grid Data Center Customer Cash Map Pass 1</a></li>
  <li><a href="/cluster/capital-flow-power-grid-customer-contract-receipt-workbench-pass-1.md">Capital Flow Power Grid Customer Contract Receipt Workbench Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-sppcrc-docket-billing-workpaper-map-pass-1.md">Capital Flow FPL SPPCRC Docket Billing Workpaper Map Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-sppcrc-form-4p-5p-billing-base-extraction-pass-1.md">Capital Flow FPL SPPCRC Form 4P 5P Billing Base Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-sppcrc-amended-form-4p-5p-comparison-pass-1.md">Capital Flow FPL SPPCRC Amended Form 4P 5P Comparison Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-sppcrc-2027-factor-to-category-reconciliation-pass-1.md">Capital Flow FPL SPPCRC 2027 Factor To Category Reconciliation Pass 1</a></li>
  <li><a href="/cluster/capital-flow-big-money-player-map-pass-1.md">Capital Flow Big-Money Player Map Pass 1</a></li>
  <li><a href="/cluster/capital-flow-big-money-destination-lane-map-pass-1.md">Capital Flow Big-Money Destination Lane Map Pass 1</a></li>
  <li><a href="/cluster/capital-flow-platform-proof-chase-matrix-pass-1.md">Capital Flow Platform Proof Chase Matrix Pass 1</a></li>
  <li><a href="/cluster/capital-flow-big-money-current-state-execution-brief-pass-1.md">Capital Flow Big-Money Current-State Execution Brief Pass 1</a></li>
  <li><a href="/cluster/capital-flow-big-money-platform-source-acquisition-queue-pass-1.md">Capital Flow Big-Money Platform Source Acquisition Queue Pass 1</a></li>
  <li><a href="/cluster/capital-flow-ares-frontline-public-source-acquisition-attempt-pass-1.md">Capital Flow Ares Frontline Public Source Acquisition Attempt Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-source-acquisition-pass-1.md">Capital Flow Apollo Athene Statutory Source Acquisition Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-schedule-locator-pass-1.md">Capital Flow Apollo Athene Statutory Schedule Locator Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-compact-extraction-pass-1.md">Capital Flow Apollo Athene Statutory Compact Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-detail-sample-extraction-pass-1.md">Capital Flow Apollo Athene Statutory Detail Sample Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-parser-prototype-pass-1.md">Capital Flow Apollo Athene Statutory Parser Prototype Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-schedule-d-normalized-sample-pass-1.md">Capital Flow Apollo Athene Statutory Schedule D Normalized Sample Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-schedule-d-full-range-parser-pass-1.md">Capital Flow Apollo Athene Statutory Schedule D Full-Range Parser Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-schedule-d-reconciliation-diagnostic-pass-1.md">Capital Flow Apollo Athene Statutory Schedule D Reconciliation Diagnostic Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-schedule-d-page-diagnostic-pass-1.md">Capital Flow Apollo Athene Statutory Schedule D Page Diagnostic Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-schedule-d-high-priority-page-inspection-pass-1.md">Capital Flow Apollo Athene Statutory Schedule D High-Priority Page Inspection Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-schedule-d-blank-column-parser-correction-pass-1.md">Capital Flow Apollo Athene Statutory Schedule D Blank-Column Parser Correction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-schedule-d-row-start-cusip-marker-correction-pass-1.md">Capital Flow Apollo Athene Statutory Schedule D Row-Start CUSIP Marker Correction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-schedule-d-residual-gap-diagnostic-pass-1.md">Capital Flow Apollo Athene Statutory Schedule D Residual Gap Diagnostic Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-legal-entity-income-cash-bridge-pass-1.md">Capital Flow Apollo Athene Statutory Legal-Entity Income Cash Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-schedule-d-disposal-proceeds-parser-pass-1.md">Capital Flow Apollo Athene Statutory Schedule D Disposal Proceeds Parser Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-cusip-cashback-match-pass-1.md">Capital Flow Apollo Athene Statutory CUSIP Cash-Back Match Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-cusip-cashback-high-dollar-inspection-pass-1.md">Capital Flow Apollo Athene Statutory CUSIP Cash-Back High-Dollar Inspection Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-cusip-row-proof-packet-pass-1.md">Capital Flow Apollo Athene Statutory CUSIP Row Proof Packet Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-cusip-raw-text-inspection-pass-1.md">Capital Flow Apollo Athene Statutory CUSIP Raw Text Inspection Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-cusip-column-interpretation-pass-1.md">Capital Flow Apollo Athene Statutory CUSIP Column Interpretation Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-disposal-parser-safe-gainloss-correction-pass-1.md">Capital Flow Apollo Athene Statutory Disposal Parser Safe Gain/Loss Correction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-safe-cashlike-proceeds-summary-pass-1.md">Capital Flow Apollo Athene Statutory Safe Cash-Like Proceeds Summary Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-safe-cashlike-same-cusip-row-proof-packet-pass-1.md">Capital Flow Apollo Athene Statutory Safe Cash-Like Same-CUSIP Row Proof Packet Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-safe-cashlike-same-cusip-raw-text-inspection-pass-1.md">Capital Flow Apollo Athene Statutory Safe Cash-Like Same-CUSIP Raw Text Inspection Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-safe-cashlike-column-review-pass-1.md">Capital Flow Apollo Athene Statutory Safe Cash-Like Column Review Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-safe-cashlike-issuer-borrower-map-pass-1.md">Capital Flow Apollo Athene Statutory Safe Cash-Like Issuer/Borrower Map Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-concord-named-cash-source-acquisition-pass-1.md">Capital Flow Apollo Athene Concord Named-Cash Source Acquisition Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-concord-controlled-document-request-packet-pass-1.md">Capital Flow Apollo Athene Concord Controlled-Document Request Packet Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-concord-public-document-acquisition-attempt-pass-1.md">Capital Flow Apollo Athene Concord Public Document Acquisition Attempt Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-amaps-named-cash-source-acquisition-pass-1.md">Capital Flow Apollo Athene AMAPS Named-Cash Source Acquisition Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-amaps-controlled-document-request-packet-pass-1.md">Capital Flow Apollo Athene AMAPS Controlled-Document Request Packet Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-amaps-public-document-acquisition-attempt-pass-1.md">Capital Flow Apollo Athene AMAPS Public Document Acquisition Attempt Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-named-issuer-prototype-synthesis-pass-1.md">Capital Flow Apollo Athene Named-Issuer Prototype Synthesis Pass 1</a></li>
  <li><a href="/cluster/capital-flow-meta-question-answer-matrix.md">Capital Flow Meta-Question Answer Matrix</a></li>
  <li><a href="/cluster/capital-flow-meta-question-status-dashboard-pass-1.md">Capital Flow Meta-Question Status Dashboard Pass 1</a></li>
  <li><a href="/cluster/capital-flow-current-answer-brief-pass-1.md">Capital Flow Current Answer Brief Pass 1</a></li>
  <li><a href="/cluster/capital-flow-research-sprint-answer-synthesis-pass-1.md">Capital Flow Research Sprint Answer Synthesis Pass 1</a></li>
  <li><a href="/cluster/capital-flow-end-to-end-graph-pass-1.md">Capital Flow End-To-End Graph Pass 1</a></li>
  <li><a href="/cluster/capital-flow-end-to-end-graph-upgrade-queue-pass-1.md">Capital Flow End-To-End Graph Upgrade Queue Pass 1</a></li>
  <li><a href="/cluster/capital-flow-evidence-backed-insights-pass-1.md">Capital Flow Evidence-Backed Insights Pass 1</a></li>
  <li><a href="/cluster/capital-flow-cash-realization-proof-ladder-pass-1.md">Capital Flow Cash-Realization Proof Ladder Pass 1</a></li>
  <li><a href="/cluster/capital-flow-cash-realization-source-targets-pass-1.md">Capital Flow Cash-Realization Source Targets Pass 1</a></li>
  <li><a href="/cluster/capital-flow-cash-realization-source-acquisition-queue-pass-1.md">Capital Flow Cash-Realization Source Acquisition Queue Pass 1</a></li>
  <li><a href="/cluster/capital-flow-publication-claim-cash-realization-audit-pass-1.md">Capital Flow Publication Claim Cash-Realization Audit Pass 1</a></li>
  <li><a href="/cluster/capital-flow-519-company-cash-realization-batch-pass-1.md">Capital Flow 519-Company Cash-Realization Batch Pass 1</a></li>
  <li><a href="/cluster/capital-flow-519-company-cash-realization-source-table-pass-1.md">Capital Flow 519-Company Cash-Realization Source Table Pass 1</a></li>
  <li><a href="/cluster/capital-flow-519-company-money-movement-map-pass-1.md">Capital Flow 519-Company Money Movement Map Pass 1</a></li>
  <li><a href="/cluster/capital-flow-executed-money-movement-synthesis-pass-1.md">Capital Flow Executed Money Movement Synthesis Pass 1</a></li>
  <li><a href="/cluster/capital-flow-cash-return-source-work-order-pass-1.md">Capital Flow Cash Return Source Work Order Pass 1</a></li>
  <li><a href="/cluster/capital-flow-debt-service-waterfall-source-route-pass-1.md">Capital Flow Debt-Service Waterfall Source Route Pass 1</a></li>
  <li><a href="/cluster/capital-flow-borrower-facility-document-source-route-pass-1.md">Capital Flow Borrower Facility Document Source Route Pass 1</a></li>
  <li><a href="/cluster/capital-flow-insurance-statutory-asset-income-source-route-pass-1.md">Capital Flow Insurance Statutory Asset-Income Source Route Pass 1</a></li>
  <li><a href="/cluster/capital-flow-contract-pricing-obligation-source-route-pass-1.md">Capital Flow Contract Pricing Obligation Source Route Pass 1</a></li>
  <li><a href="/cluster/capital-flow-output-utilization-attribution-source-route-pass-1.md">Capital Flow Output Utilization Attribution Source Route Pass 1</a></li>
  <li><a href="/cluster/capital-flow-collateral-availability-certificate-source-route-pass-1.md">Capital Flow Collateral Availability Certificate Source Route Pass 1</a></li>
  <li><a href="/cluster/capital-flow-working-capital-collection-source-route-pass-1.md">Capital Flow Working Capital Collection Source Route Pass 1</a></li>
  <li><a href="/cluster/capital-flow-transaction-funds-flow-source-route-pass-1.md">Capital Flow Transaction Funds-Flow Source Route Pass 1</a></li>
  <li><a href="/cluster/capital-flow-return-model-source-route-pass-1.md">Capital Flow Return Model Source Route Pass 1</a></li>
  <li><a href="/cluster/capital-flow-source-route-execution-status-pass-1.md">Capital Flow Source Route Execution Status Pass 1</a></li>
  <li><a href="/cluster/capital-flow-next-source-acquisition-queue-pass-1.md">Capital Flow Next Source Acquisition Queue Pass 1</a></li>
  <li><a href="/cluster/capital-flow-cfnsaq-001-customer-receipts-acquisition-pass-1.md">Capital Flow CFNSAQ-001 Customer Receipts Acquisition Pass 1</a></li>
  <li><a href="/cluster/capital-flow-cfnsaq-002-project-asset-cash-contribution-pass-1.md">Capital Flow CFNSAQ-002 Project/Asset Cash Contribution Pass 1</a></li>
  <li><a href="/cluster/capital-flow-cfnsaq-003-debt-service-lender-allocation-pass-1.md">Capital Flow CFNSAQ-003 Debt-Service/Lender Allocation Pass 1</a></li>
  <li><a href="/cluster/capital-flow-cfnsaq-004-statutory-facility-collateral-pass-1.md">Capital Flow CFNSAQ-004 Statutory/Facility/Collateral Pass 1</a></li>
  <li><a href="/cluster/capital-flow-cfnsaq-005-return-model-support-pass-1.md">Capital Flow CFNSAQ-005 Return Model Support Pass 1</a></li>
  <li><a href="/cluster/capital-flow-cfnsaq-execution-synthesis-pass-1.md">Capital Flow CFNSAQ Execution Synthesis Pass 1</a></li>
  <li><a href="/cluster/capital-flow-cfnsaq-publication-safe-answer-brief-pass-1.md">Capital Flow CFNSAQ Publication-Safe Answer Brief Pass 1</a></li>
  <li><a href="/cluster/capital-flow-named-cash-proof-source-locator-pass-1.md">Capital Flow Named Cash Proof Source Locator Pass 1</a></li>
  <li><a href="/cluster/capital-flow-named-cash-proof-requirements-matrix-pass-1.md">Capital Flow Named Cash Proof Requirements Matrix Pass 1</a></li>
  <li><a href="/cluster/capital-flow-named-cash-proof-decisive-source-request-packet-pass-1.md">Capital Flow Named Cash Proof Decisive Source Request Packet Pass 1</a></li>
  <li><a href="/cluster/capital-flow-named-cash-proof-wrapup-insights-pass-1.md">Capital Flow Named Cash Proof Wrap-Up Insights Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-billing-determinant-category-receipt-proof-chase-pass-1.md">Capital Flow FPL Billing Determinant Category Receipt Proof Chase Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-borrowing-base-collateral-availability-proof-chase-pass-1.md">Capital Flow URI Borrowing-Base Collateral Availability Proof Chase Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-collateral-fleet-return-bridge-pass-1.md">Capital Flow URI Collateral Fleet Return Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-wheaton-antamina-debt-waterfall-return-proof-chase-pass-1.md">Capital Flow Wheaton Antamina Debt-Waterfall Return Proof Chase Pass 1</a></li>
  <li><a href="/cluster/capital-flow-energy-midstream-project-cash-contribution-proof-chase-pass-1.md">Capital Flow Energy Midstream Project Cash Contribution Proof Chase Pass 1</a></li>
  <li><a href="/cluster/capital-flow-insurance-legal-entity-statutory-proof-chase-pass-1.md">Capital Flow Insurance Legal-Entity Statutory Proof Chase Pass 1</a></li>
  <li><a href="/cluster/capital-flow-ares-frontline-borrower-facility-use-proceeds-proof-chase-pass-1.md">Capital Flow Ares Frontline Borrower Facility Use-Proceeds Proof Chase Pass 1</a></li>
  <li><a href="/cluster/capital-flow-ares-frontline-facility-cash-waterfall-bridge-pass-1.md">Capital Flow Ares Frontline Facility Cash Waterfall Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-return-model-named-cash-proof-chase-pass-1.md">Capital Flow Return Model Named Cash Proof Chase Pass 1</a></li>
  <li><a href="/cluster/capital-flow-transaction-funds-flow-named-cash-proof-chase-pass-1.md">Capital Flow Transaction Funds-Flow Named Cash Proof Chase Pass 1</a></li>
  <li><a href="/cluster/capital-flow-named-cash-proof-execution-status-matrix-pass-1.md">Capital Flow Named Cash Proof Execution Status Matrix Pass 1</a></li>
  <li><a href="/cluster/capital-flow-top-three-named-cash-source-acquisition-packet-pass-1.md">Capital Flow Top Three Named Cash Source Acquisition Packet Pass 1</a></li>
  <li><a href="/cluster/capital-flow-pbf-proof-package-acquisition-pass-1.md">Capital Flow PBF Proof Package Acquisition Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-proof-package-acquisition-pass-1.md">Capital Flow FPL Proof Package Acquisition Pass 1</a></li>
  <li><a href="/cluster/capital-flow-519-company-denominator-control-pass-1.md">Capital Flow 519-Company Denominator Control Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-statutory-cash-return-pass-1.md">Capital Flow Apollo/Athene Statutory Cash Return Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-borrower-allocation-pass-1.md">Capital Flow KKR Global Atlantic Borrower Allocation Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-statutory-template-pass-1.md">Capital Flow KKR Global Atlantic Statutory Template Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-statutory-source-acquisition-pass-1.md">Capital Flow KKR Global Atlantic Statutory Source Acquisition Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-statutory-schedule-locator-pass-1.md">Capital Flow KKR Global Atlantic Statutory Schedule Locator Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-accordia-compact-extraction-pass-1.md">Capital Flow KKR Global Atlantic Accordia Compact Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-accordia-schedule-d-parser-pass-1.md">Capital Flow KKR Global Atlantic Accordia Schedule D Parser Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-accordia-schedule-d-column-reconciliation-pass-1.md">Capital Flow KKR Global Atlantic Accordia Schedule D Column Reconciliation Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-accordia-schedule-d-held-row-column-geometry-pass-1.md">Capital Flow KKR Global Atlantic Accordia Schedule D Held-Row Column Geometry Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-accordia-schedule-d-coordinate-owned-bond-reconciliation-pass-1.md">Capital Flow KKR Global Atlantic Accordia Schedule D Coordinate Owned-Bond Reconciliation Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-accordia-owned-bond-income-bridge-pass-1.md">Capital Flow KKR Global Atlantic Accordia Owned-Bond Income Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-accordia-owned-bond-income-proceeds-cusip-match-pass-1.md">Capital Flow KKR Global Atlantic Accordia Owned-Bond Income Proceeds CUSIP Match Pass 1</a></li>
  <li><a href="/cluster/capital-flow-blackstone-credit-borrower-use-cash-pass-1.md">Capital Flow Blackstone Credit Borrower Use Cash Pass 1</a></li>
  <li><a href="/cluster/capital-flow-plains-tariff-volume-cash-pass-1.md">Capital Flow Plains Tariff Volume Cash Pass 1</a></li>
  <li><a href="/cluster/capital-flow-debt-refinancing-sec-source-denominator-pass-1.md">Capital Flow Debt Refinancing SEC Source/Denominator Pass 1</a></li>
  <li><a href="/cluster/capital-flow-wheaton-6k-ifrs-debt-cash-extraction-pass-1.md">Capital Flow Wheaton 6-K IFRS Debt/Cash Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-debt-refinancing-use-return-frontier-pass-1.md">Capital Flow Debt Refinancing Use/Return Frontier Pass 1</a></li>
  <li><a href="/cluster/capital-flow-wheaton-antamina-use-return-bridge-pass-1.md">Capital Flow Wheaton Antamina Use/Return Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-wheaton-antamina-pmpa-economics-pass-1.md">Capital Flow Wheaton Antamina PMPA Economics Pass 1</a></li>
  <li><a href="/cluster/capital-flow-wheaton-antamina-net-cash-return-pass-1.md">Capital Flow Wheaton Antamina Net Cash Return Pass 1</a></li>
  <li><a href="/cluster/capital-flow-wheaton-antamina-cash-return-proof-stack-pass-1.md">Capital Flow Wheaton Antamina Cash-Return Proof Stack Pass 1</a></li>
  <li><a href="/cluster/capital-flow-wheaton-antamina-full-return-source-test-pass-1.md">Capital Flow Wheaton Antamina Full Return Source Test Pass 1</a></li>
  <li><a href="/cluster/capital-flow-wheaton-antamina-production-receipt-bridge-pass-1.md">Capital Flow Wheaton Antamina Production Receipt Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-wheaton-antamina-cumulative-received-sold-cashflow-pass-1.md">Capital Flow Wheaton Antamina Cumulative Received/Sold Cashflow Pass 1</a></li>
  <li><a href="/cluster/capital-flow-bhp-antamina-streaming-proceeds-use-boundary-pass-1.md">Capital Flow BHP Antamina Streaming Proceeds/Use Boundary Pass 1</a></li>
  <li><a href="/cluster/capital-flow-antamina-proof-package-acquisition-pass-1.md">Capital Flow Antamina Proof Package Acquisition Pass 1</a></li>
  <li><a href="/cluster/capital-flow-matador-borrowing-base-use-return-bridge-pass-1.md">Capital Flow Matador Borrowing-Base Use/Return Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-liberty-broadband-holdco-restructuring-bridge-pass-1.md">Capital Flow Liberty Broadband Holdco Restructuring Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-pbf-refining-liquidity-use-return-bridge-pass-1.md">Capital Flow PBF Refining Liquidity Use/Return Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-devon-merger-period-allocation-bridge-pass-1.md">Capital Flow Devon Merger-Period Allocation Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-debt-refinancing-bridge-upgrade-queue-pass-1.md">Capital Flow Debt Refinancing Bridge Upgrade Queue Pass 1</a></li>
  <li><a href="/cluster/capital-flow-matador-source-specific-use-allocation-pass-1.md">Capital Flow Matador Source-Specific Use Allocation Pass 1</a></li>
  <li><a href="/cluster/capital-flow-matador-source-specific-asset-cash-pass-1.md">Capital Flow Matador Source-Specific Asset-Cash Pass 1</a></li>
  <li><a href="/cluster/capital-flow-matador-blm-borrowing-base-asset-cash-bridge-pass-1.md">Capital Flow Matador BLM Borrowing-Base Asset Cash Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-matador-named-cash-proof-source-availability-pass-1.md">Capital Flow Matador Named Cash Proof Source Availability Pass 1</a></li>
  <li><a href="/cluster/capital-flow-devon-treasury-funds-flow-pass-1.md">Capital Flow Devon Treasury Funds-Flow Pass 1</a></li>
  <li><a href="/cluster/capital-flow-devon-source-priority-stress-fcf-pass-1.md">Capital Flow Devon Source-Priority Stress FCF Pass 1</a></li>
  <li><a href="/cluster/capital-flow-pbf-note-refinancing-economics-pass-1.md">Capital Flow PBF Note Refinancing Economics Pass 1</a></li>
  <li><a href="/cluster/capital-flow-pbf-insurance-normalized-cash-flow-pass-1.md">Capital Flow PBF Insurance-Normalized Cash Flow Pass 1</a></li>
  <li><a href="/cluster/capital-flow-pbf-pro-forma-debt-service-refinery-cash-pass-1.md">Capital Flow PBF Pro Forma Debt-Service And Refinery-Cash Pass 1</a></li>
  <li><a href="/cluster/capital-flow-pbf-redemption-settlement-bridge-pass-1.md">Capital Flow PBF Redemption Settlement Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-devon-debt-payout-sustainability-pass-1.md">Capital Flow Devon Debt/Payout Sustainability Pass 1</a></li>
  <li><a href="/cluster/capital-flow-liberty-debenture-settlement-economics-pass-1.md">Capital Flow Liberty Debenture Settlement Economics Pass 1</a></li>
  <li><a href="/cluster/capital-flow-liberty-ltv-merger-shareholder-realization-pass-1.md">Capital Flow Liberty LTV Merger Shareholder Realization Pass 1</a></li>
  <li><a href="/cluster/capital-flow-matador-debt-service-quality-pass-1.md">Capital Flow Matador Debt-Service Quality Pass 1</a></li>
  <li><a href="/cluster/capital-flow-debt-refinancing-source-use-cash-allocation-pass-1.md">Capital Flow Debt Refinancing Source/Use/Cash Allocation Pass 1</a></li>
  <li><a href="/cluster/capital-flow-operating-return-frontier-pass-1.md">Capital Flow Operating Return Frontier Pass 1</a></li>
  <li><a href="/cluster/capital-flow-operating-return-scorecard-pass-1.md">Capital Flow Operating Return Scorecard Pass 1</a></li>
  <li><a href="/cluster/capital-flow-cash-return-source-test-status-pass-1.md">Capital Flow Cash Return Source Test Status Pass 1</a></li>
  <li><a href="/cluster/capital-flow-money-movement-proof-graph-pass-1.md">Capital Flow Money Movement Proof Graph Pass 1</a></li>
  <li><a href="/cluster/capital-flow-all-16-money-movement-proof-graph-pass-1.md">Capital Flow All-16 Money Movement Proof Graph Pass 1</a></li>
  <li><a href="/cluster/capital-flow-repeated-missing-source-index-pass-1.md">Capital Flow Repeated Missing Source Index Pass 1</a></li>
  <li><a href="/cluster/capital-flow-repeated-missing-source-work-order-pass-1.md">Capital Flow Repeated Missing Source Work Order Pass 1</a></li>
  <li><a href="/cluster/capital-flow-customer-receipts-billing-source-route-pass-1.md">Capital Flow Customer Receipts Billing Source Route Pass 1</a></li>
  <li><a href="/cluster/capital-flow-source-to-use-allocation-work-order-pass-1.md">Capital Flow Source-To-Use Allocation Work Order Pass 1</a></li>
  <li><a href="/cluster/capital-flow-project-asset-cash-contribution-source-route-pass-1.md">Capital Flow Project Asset Cash Contribution Source Route Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-fleet-return-bridge-pass-1.md">Capital Flow URI Fleet Return Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-fleet-cash-yield-source-target-pass-1.md">Capital Flow URI Fleet Cash-Yield Source Target Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-fleet-cash-yield-source-test-pass-1.md">Capital Flow URI Fleet Cash-Yield Source Test Pass 1</a></li>
  <li><a href="/cluster/capital-flow-sterling-backlog-return-risk-pass-1.md">Capital Flow Sterling Backlog Return/Risk Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-mastec-project-cash-collection-pass-1.md">Capital Flow MasTec Project Cash Collection Pass 1</a></li>
  <li><a href="/cluster/capital-flow-sterling-project-cash-collection-source-target-pass-1.md">Capital Flow Sterling Project Cash Collection Source Target Pass 1</a></li>
  <li><a href="/cluster/capital-flow-sterling-project-cash-collection-source-test-pass-1.md">Capital Flow Sterling Project Cash Collection Source Test Pass 1</a></li>
  <li><a href="/cluster/capital-flow-detailed-answers-open-questions-pass-1.md">Capital Flow Detailed Answers And Open Questions Pass 1</a></li>
  <li><a href="/cluster/capital-flow-answer-resolution-queue-pass-1.md">Capital Flow Answer Resolution Queue Pass 1</a></li>
  <li><a href="/cluster/capital-flow-publication-ready-claim-register-pass-1.md">Capital Flow Publication-Ready Claim Register Pass 1</a></li>
  <li><a href="/cluster/capital-flow-bank-role-after-private-credit-pass-1.md">Capital Flow Bank Role After Private Credit Pass 1</a></li>
  <li><a href="/cluster/capital-flow-auctane-post-close-bank-role-pass-1.md">Capital Flow Auctane Post-Close Bank Role Pass 1</a></li>
  <li><a href="/cluster/capital-flow-medallia-lender-allocation-repayment-pass-1.md">Capital Flow Medallia Lender Allocation Repayment Pass 1</a></li>
  <li><a href="/cluster/capital-flow-guidehouse-bank-competition-proof-pass-1.md">Capital Flow Guidehouse Bank Competition Proof Pass 1</a></li>
  <li><a href="/cluster/capital-flow-frontline-facility-use-bridge-pass-1.md">Capital Flow Frontline Facility Use Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-relation-holder-to-facility-bridge-pass-1.md">Capital Flow Relation Holder To Facility Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-valcourt-acquisition-use-timeline-pass-1.md">Capital Flow Valcourt Acquisition Use Timeline Pass 1</a></li>
  <li><a href="/cluster/capital-flow-mai-acquisition-financing-map-pass-1.md">Capital Flow MAI Acquisition Financing Map Pass 1</a></li>
  <li><a href="/cluster/capital-flow-vehicle-capital-stack-decomposition-pass-1.md">Capital Flow Vehicle Capital Stack Decomposition Pass 1</a></li>
  <li><a href="/cluster/capital-flow-non-traded-private-credit-funding-stack-pass-1.md">Capital Flow Non-Traded Private-Credit Funding Stack Pass 1</a></li>
  <li><a href="/cluster/capital-flow-capital-source-to-vehicle-bridge-pass-1.md">Capital Flow Capital Source To Vehicle Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-use-of-proceeds-classification-pass-1.md">Capital Flow Use-Of-Proceeds Classification Pass 1</a></li>
  <li><a href="/cluster/bidirectional-claims-to-evidence-method.md">Bidirectional Claims-To-Evidence Method</a></li>
  <li><a href="/cluster/capital-flow-claims-evidence-backlog.md">Capital Flow Claims Evidence Backlog</a></li>
  <li><a href="/cluster/capital-flow-evidence-ledger-index.md">Capital Flow Evidence Ledger Index</a></li>
  <li><a href="/cluster/capital-flow-primary-source-verification-pass-1.md">Capital Flow Primary-Source Verification Pass 1</a></li>
  <li><a href="/cluster/capital-flow-real-number-acquisition-system.md">Capital Flow Real-Number Acquisition System</a></li>
  <li><a href="/cluster/capital-flow-real-number-extraction-roadmap.md">Capital Flow Real-Number Extraction Roadmap</a></li>
  <li><a href="/cluster/capital-flow-big-picture-remaining-work-map.md">Capital Flow Big-Picture Remaining Work Map</a></li>
  <li><a href="/cluster/capital-flow-promoted-claims-and-overclaims-pass-1.md">Capital Flow Promoted Claims And Overclaims Pass 1</a></li>
  <li><a href="/cluster/capital-flow-next-work-program.md">Capital Flow Next Work Program</a></li>
  <li><a href="/cluster/capital-flow-all-company-triage.md">Capital Flow All-Company Triage</a></li>
  <li><a href="/cluster/capital-flow-lane-candidate-queues.md">Capital Flow Lane Candidate Queues</a></li>
  <li><a href="/cluster/capital-flow-all-company-scale-up-operating-model.md">Capital Flow All-Company Scale-Up Operating Model</a></li>
  <li><a href="/cluster/capital-flow-all-company-extraction-template-pass-1.md">Capital Flow All-Company Extraction Template Pass 1</a></li>
  <li><a href="/cluster/capital-flow-519-company-batch-evidence-refresh-pass-1.md">Capital Flow 519-Company Batch Evidence Refresh Pass 1</a></li>
  <li><a href="/cluster/capital-flow-519-company-pilot-refresh-pass-2.md">Capital Flow 519-Company Pilot Refresh Pass 2</a></li>
  <li><a href="/cluster/capital-flow-power-grid-pilot-source-table-extraction-pass-1.md">Capital Flow Power/Grid Pilot Source-Table Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-power-grid-pilot-return-proof-upgrade-queue-pass-1.md">Capital Flow Power/Grid Pilot Return-Proof Upgrade Queue Pass 1</a></li>
  <li><a href="/cluster/capital-flow-power-grid-pilot-priority1-source-availability-pass-1.md">Capital Flow Power/Grid Pilot Priority-1 Source Availability Pass 1</a></li>
  <li><a href="/cluster/capital-flow-power-grid-pilot-official-source-discovery-pass-1.md">Capital Flow Power/Grid Pilot Official Source Discovery Pass 1</a></li>
  <li><a href="/cluster/capital-flow-power-grid-pilot-source-acquisition-results-pass-1.md">Capital Flow Power/Grid Pilot Source Acquisition Results Pass 1</a></li>
  <li><a href="/cluster/capital-flow-power-grid-pilot-priority1-metric-extraction-pass-1.md">Capital Flow Power/Grid Pilot Priority-1 Metric Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-power-grid-pilot-gap-closure-and-metric-pass-2.md">Capital Flow Power/Grid Pilot Gap Closure And Metric Pass 2</a></li>
  <li><a href="/cluster/capital-flow-power-grid-pilot-proof-status-dashboard-pass-1.md">Capital Flow Power/Grid Pilot Proof Status Dashboard Pass 1</a></li>
  <li><a href="/cluster/capital-flow-power-grid-pilot-followup-source-route-map-pass-1.md">Capital Flow Power/Grid Pilot Follow-Up Source Route Map Pass 1</a></li>
  <li><a href="/cluster/capital-flow-power-grid-followup-metric-extraction-pass-1.md">Capital Flow Power/Grid Follow-Up Metric Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-plains-commercial-durability-extraction-pass-1.md">Capital Flow Plains Commercial Durability Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-power-grid-pilot-answer-synthesis-pass-2.md">Capital Flow Power/Grid Pilot Answer Synthesis Pass 2</a></li>
  <li><a href="/cluster/capital-flow-power-grid-project-return-workbench-pass-1.md">Capital Flow Power/Grid Project-Return Workbench Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-sppcrc-category-recovery-extraction-pass-1.md">Capital Flow FPL SPPCRC Category Recovery Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-sppcrc-factor-trueup-wacc-extraction-pass-1.md">Capital Flow FPL SPPCRC Factor/True-Up/WACC Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-sppcrc-final-trueup-extraction-pass-1.md">Capital Flow FPL SPPCRC Final True-Up Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-sppcrc-factor-order-extraction-pass-1.md">Capital Flow FPL SPPCRC Final Factor Order Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-sppcrc-project-detail-extraction-pass-1.md">Capital Flow FPL SPPCRC Project Detail Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-sppcrc-earnings-cash-bridge-pass-1.md">Capital Flow FPL SPPCRC Earnings/Cash Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-sppcrc-category-attribution-bridge-pass-1.md">Capital Flow FPL SPPCRC Category Attribution Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-distribution-inspection-attribution-pass-1.md">Capital Flow FPL Distribution Inspection Attribution Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-distribution-inspection-component-extraction-pass-1.md">Capital Flow FPL Distribution Inspection Component Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-distribution-inspection-receipts-financing-boundary-pass-1.md">Capital Flow FPL Distribution Inspection Receipts/Financing Boundary Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-distribution-inspection-customer-receipt-source-pursuit-pass-1.md">Capital Flow FPL Distribution Inspection Customer Receipt/Source Pursuit Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-distribution-inspection-customer-receipt-source-acquisition-pass-1.md">Capital Flow FPL Distribution Inspection Customer Receipt/Source Acquisition Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-distribution-inspection-customer-receipt-source-test-pass-1.md">Capital Flow FPL Distribution Inspection Customer Receipt Source Test Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-category-receipt-workpaper-bridge-pass-1.md">Capital Flow FPL Category Receipt Workpaper Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-2026-docket-billing-receipt-source-availability-pass-1.md">Capital Flow FPL 2026 Docket Billing Receipt Source Availability Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-2026-discovery-audit-receipt-proof-route-pass-1.md">Capital Flow FPL 2026 Discovery Audit Receipt Proof Route Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-psc-api-document-access-boundary-pass-1.md">Capital Flow FPL PSC API Document Access Boundary Pass 1</a></li>
  <li><a href="/cluster/capital-flow-fpl-sppcrc-remaining-source-status-pass-1.md">Capital Flow FPL SPPCRC Remaining Source Status Pass 1</a></li>
  <li><a href="/cluster/capital-flow-cross-theme-claim-status-dashboard.md">Capital Flow Cross-Theme Claim Status Dashboard</a></li>
  <li><a href="/cluster/capital-flow-funding-type-hypothesis-map-pass-1.md">Capital Flow Funding-Type Hypothesis Map Pass 1</a></li>
  <li><a href="/cluster/capital-flow-refinancing-event-ledger-pass-1.md">Capital Flow Refinancing Event Ledger Pass 1</a></li>
  <li><a href="/cluster/capital-flow-acquisition-finance-ledger-pass-1.md">Capital Flow Acquisition Finance Ledger Pass 1</a></li>
  <li><a href="/cluster/capital-flow-asset-backed-finance-ledger-pass-1.md">Capital Flow Asset-Backed Finance Ledger Pass 1</a></li>
  <li><a href="/cluster/capital-flow-capital-intensive-buildout-ledger-pass-1.md">Capital Flow Capital-Intensive Buildout Ledger Pass 1</a></li>
  <li><a href="/cluster/capital-flow-capital-intensive-project-cash-extraction-queue.md">Capital Flow Capital-Intensive Project/Cash Extraction Queue</a></li>
  <li><a href="/cluster/capital-flow-capital-intensive-project-cash-extraction-pass-1.md">Capital Flow Capital-Intensive Project/Cash Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-capital-intensive-priority-source-manifest.md">Capital Flow Capital-Intensive Priority Source Manifest</a></li>
  <li><a href="/cluster/capital-flow-capital-intensive-priority-source-table-extraction-pass-1.md">Capital Flow Capital-Intensive Priority Source-Table Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-capital-intensive-energy-source-table-extraction-pass-1.md">Capital Flow Capital-Intensive Energy Source-Table Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-capital-intensive-energy-annual-baseline-source-table-pass-1.md">Capital Flow Capital-Intensive Energy Annual Baseline Source-Table Pass 1</a></li>
  <li><a href="/cluster/capital-flow-capital-intensive-industrial-annual-baseline-source-table-pass-1.md">Capital Flow Capital-Intensive Industrial Annual Baseline Source-Table Pass 1</a></li>
  <li><a href="/cluster/capital-flow-capital-intensive-project-denominator-workbench-pass-1.md">Capital Flow Capital-Intensive Project Denominator Workbench Pass 1</a></li>
  <li><a href="/cluster/capital-flow-capital-intensive-energy-project-denominator-pass-1.md">Capital Flow Capital-Intensive Energy Project Denominator Pass 1</a></li>
  <li><a href="/cluster/capital-flow-energy-project-source-use-return-pass-1.md">Capital Flow Energy Project Source-Use-Return Pass 1</a></li>
  <li><a href="/cluster/capital-flow-energy-transfer-project-cash-realization-pass-1.md">Capital Flow Energy Transfer Project Cash-Realization Pass 1</a></li>
  <li><a href="/cluster/capital-flow-energy-transfer-named-project-cash-source-test-pass-1.md">Capital Flow Energy Transfer Named Project Cash Source Test Pass 1</a></li>
  <li><a href="/cluster/capital-flow-energy-transfer-nederland-contract-cash-bridge-pass-1.md">Capital Flow Energy Transfer Nederland Contract Cash Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-capital-intensive-industrial-denominator-pass-1.md">Capital Flow Capital-Intensive Industrial Denominator Pass 1</a></li>
  <li><a href="/cluster/capital-flow-capital-intensive-industrial-conversion-pass-1.md">Capital Flow Capital-Intensive Industrial Conversion Pass 1</a></li>
  <li><a href="/cluster/capital-flow-capital-intensive-project-funding-map-pass-1.md">Capital Flow Capital-Intensive Project Funding Map Pass 1</a></li>
  <li><a href="/cluster/capital-flow-capital-intensive-credit-agreement-and-project-finance-pass-1.md">Capital Flow Capital-Intensive Credit Agreement And Project Finance Pass 1</a></li>
  <li><a href="/cluster/capital-flow-capital-intensive-credit-document-source-locator-pass-1.md">Capital Flow Capital-Intensive Credit Document Source Locator Pass 1</a></li>
  <li><a href="/cluster/capital-flow-capital-intensive-filed-credit-term-summary-pass-1.md">Capital Flow Capital-Intensive Filed Credit Term Summary Pass 1</a></li>
  <li><a href="/cluster/capital-flow-cheniere-train-source-use-return-bridge-pass-1.md">Capital Flow Cheniere Train Source-Use-Return Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-cheniere-project-cash-waterfall-source-target-pass-1.md">Capital Flow Cheniere Project Cash-Waterfall Source Target Pass 1</a></li>
  <li><a href="/cluster/capital-flow-cheniere-train-cash-waterfall-source-test-pass-1.md">Capital Flow Cheniere Train Cash Waterfall Source Test Pass 1</a></li>
  <li><a href="/cluster/capital-flow-cheniere-entity-dscr-waterfall-bridge-pass-1.md">Capital Flow Cheniere Entity DSCR Waterfall Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-operating-conversion-scorecard-pass-1.md">Capital Flow Operating Conversion Scorecard Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-borrowing-base-fleet-collateral-pass-1.md">Capital Flow URI Borrowing-Base Fleet-Collateral Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-fleet-capital-durability-pass-1.md">Capital Flow URI Fleet-Capital Durability Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-receivables-purchase-agreement-mechanics-pass-1.md">Capital Flow URI Receivables Purchase Agreement Mechanics Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-abl-agreement-mechanics-pass-1.md">Capital Flow URI ABL Agreement Mechanics Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-abl-borrowing-base-definitions-pass-1.md">Capital Flow URI ABL Borrowing-Base Definitions Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-abl-borrowing-base-certificate-source-boundary-pass-1.md">Capital Flow URI ABL Borrowing-Base Certificate Source Boundary Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-abl-public-disclosure-proxy-bridge-pass-1.md">Capital Flow URI ABL Public-Disclosure Proxy Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-fleet-return-utilization-proxy-pass-1.md">Capital Flow URI Fleet Return And Utilization Proxy Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-owned-rental-segment-economics-pass-1.md">Capital Flow URI Owned-Rental Segment Economics Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-owned-rental-segment-trend-pass-1.md">Capital Flow URI Owned-Rental Segment Trend Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-segment-asset-return-proxy-pass-1.md">Capital Flow URI Segment Asset-Return Proxy Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-specialty-margin-driver-boundary-pass-1.md">Capital Flow URI Specialty Margin Driver Boundary Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-rate-time-mix-source-boundary-pass-1.md">Capital Flow URI Rate/Time/Mix Source Boundary Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-investor-deck-fleet-productivity-pass-1.md">Capital Flow URI Investor Deck Fleet Productivity Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-transcript-rate-time-mix-commentary-pass-1.md">Capital Flow URI Transcript Rate/Time/Mix Commentary Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-ancillary-matting-margin-bridge-pass-1.md">Capital Flow URI Ancillary/Matting Margin Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-specialty-category-source-boundary-pass-1.md">Capital Flow URI Specialty Category Source Boundary Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-fleet-type-revenue-estimate-pass-1.md">Capital Flow URI Fleet-Type Revenue Estimate Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-category-economics-matrix-pass-1.md">Capital Flow URI Category Economics Matrix Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-yak-matting-acquisition-economics-pass-1.md">Capital Flow URI Yak/Matting Acquisition Economics Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-yak-acquisition-funding-chain-pass-1.md">Capital Flow URI Yak Acquisition Funding Chain Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-yak-senior-note-terms-pass-1.md">Capital Flow URI Yak Senior-Note Terms Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-yak-rating-context-pass-1.md">Capital Flow URI Yak Rating Context Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-yak-initial-purchaser-source-boundary-pass-1.md">Capital Flow URI Yak Initial-Purchaser Source Boundary Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-yak-bond-identifier-market-data-boundary-pass-1.md">Capital Flow URI Yak Bond Identifier And Market-Data Boundary Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-yak-public-holder-crosswalk-pass-1.md">Capital Flow URI Yak Public Holder Crosswalk Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-yak-public-holder-crosswalk-pass-2.md">Capital Flow URI Yak Public Holder Crosswalk Pass 2</a></li>
  <li><a href="/cluster/capital-flow-uri-yak-holder-schedule-extractor-pass-1.md">Capital Flow URI Yak Holder Schedule Extractor Pass 1</a></li>
  <li><a href="/cluster/capital-flow-uri-yak-original-pricing-source-boundary-pass-1.md">Capital Flow URI Yak Original Pricing Source Boundary Pass 1</a></li>
  <li><a href="/cluster/capital-flow-sterling-agreement-term-extraction-pass-1.md">Capital Flow Sterling Agreement-Term Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-sterling-backlog-customer-funding-pass-1.md">Capital Flow Sterling Backlog Customer-Funding Pass 1</a></li>
  <li><a href="/cluster/capital-flow-sterling-funded-backlog-covenant-cushion-pass-1.md">Capital Flow Sterling Funded Backlog And Covenant Cushion Pass 1</a></li>
  <li><a href="/cluster/capital-flow-sterling-eight-quarter-contract-capital-conversion-pass-1.md">Capital Flow Sterling Eight-Quarter Contract-Capital Conversion Pass 1</a></li>
  <li><a href="/cluster/capital-flow-sterling-acquired-versus-organic-backlog-pass-1.md">Capital Flow Sterling Acquired Versus Organic Backlog Pass 1</a></li>
  <li><a href="/cluster/capital-flow-sterling-lc-surety-usage-boundary-pass-1.md">Capital Flow Sterling L/C And Surety Usage Boundary Pass 1</a></li>
  <li><a href="/cluster/capital-flow-sterling-backlog-credit-platform-conversion-pass-1.md">Capital Flow Sterling Backlog Credit-Platform Conversion Pass 1</a></li>
  <li><a href="/cluster/capital-flow-sterling-project-cash-collection-source-target-pass-1.md">Capital Flow Sterling Project Cash Collection Source Target Pass 1</a></li>
  <li><a href="/cluster/capital-flow-theme-subtheme-map.md">Capital Flow Theme And Subtheme Map</a></li>
  <li><a href="/cluster/capital-flow-theme-evidence-program.md">Capital Flow Theme Evidence Program</a></li>
  <li><a href="/cluster/capital-flow-power-grid-first-extraction-pass.md">Capital Flow Power/Grid First Extraction Pass</a></li>
  <li><a href="/cluster/capital-flow-power-grid-source-upgrade.md">Capital Flow Power/Grid Source Upgrade</a></li>
  <li><a href="/cluster/capital-flow-power-grid-claim-dashboard.md">Capital Flow Power/Grid Claim Dashboard</a></li>
  <li><a href="/cluster/capital-flow-power-grid-outside-denominator-plan.md">Capital Flow Power/Grid Outside Denominator Plan</a></li>
  <li><a href="/cluster/capital-flow-power-grid-utility-denominator-map.md">Capital Flow Power/Grid Utility Denominator Map</a></li>
  <li><a href="/cluster/capital-flow-aep-duke-load-reconciliation-workbench.md">Capital Flow AEP/Duke Load Reconciliation Workbench</a></li>
  <li><a href="/cluster/capital-flow-aep-duke-source-table-extraction-queue.md">Capital Flow AEP/Duke Source-Table Extraction Queue</a></li>
  <li><a href="/cluster/capital-flow-aep-duke-source-table-extraction-pass.md">Capital Flow AEP/Duke Source-Table Extraction Pass</a></li>
  <li><a href="/cluster/capital-flow-aep-duke-normalized-bridge-tables.md">Capital Flow AEP/Duke Normalized Bridge Tables</a></li>
  <li><a href="/cluster/capital-flow-aep-duke-regulatory-docket-queue.md">Capital Flow AEP/Duke Regulatory Docket Queue</a></li>
  <li><a href="/cluster/capital-flow-aep-duke-regulatory-docket-extraction-pass.md">Capital Flow AEP/Duke Regulatory Docket Extraction Pass</a></li>
  <li><a href="/cluster/capital-flow-aep-duke-approved-recovery-bridge-pass-1.md">Capital Flow AEP/Duke Approved-Recovery Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-liability-to-credit-pass.md">Capital Flow Apollo/Athene Liability-To-Credit Pass</a></li>
  <li><a href="/cluster/capital-flow-apollo-athene-fy2025-asset-quality-pass.md">Capital Flow Apollo/Athene FY2025 Asset-Quality Pass</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-insurance-pass.md">Capital Flow KKR/Global Atlantic Insurance Pass</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-q2-2026-10q-pass.md">Capital Flow KKR/Global Atlantic Q2 2026 10-Q Pass</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-statutory-template-pass-1.md">Capital Flow KKR Global Atlantic Statutory Template Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-statutory-source-acquisition-pass-1.md">Capital Flow KKR Global Atlantic Statutory Source Acquisition Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-statutory-schedule-locator-pass-1.md">Capital Flow KKR Global Atlantic Statutory Schedule Locator Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-accordia-compact-extraction-pass-1.md">Capital Flow KKR Global Atlantic Accordia Compact Extraction Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-accordia-schedule-d-parser-pass-1.md">Capital Flow KKR Global Atlantic Accordia Schedule D Parser Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-accordia-schedule-d-column-reconciliation-pass-1.md">Capital Flow KKR Global Atlantic Accordia Schedule D Column Reconciliation Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-accordia-schedule-d-held-row-column-geometry-pass-1.md">Capital Flow KKR Global Atlantic Accordia Schedule D Held-Row Column Geometry Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-accordia-schedule-d-coordinate-owned-bond-reconciliation-pass-1.md">Capital Flow KKR Global Atlantic Accordia Schedule D Coordinate Owned-Bond Reconciliation Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-accordia-owned-bond-income-bridge-pass-1.md">Capital Flow KKR Global Atlantic Accordia Owned-Bond Income Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-kkr-global-atlantic-accordia-owned-bond-income-proceeds-cusip-match-pass-1.md">Capital Flow KKR Global Atlantic Accordia Owned-Bond Income Proceeds CUSIP Match Pass 1</a></li>
  <li><a href="/cluster/capital-flow-brookfield-wealth-solutions-insurance-pass.md">Capital Flow Brookfield Wealth Solutions Insurance Pass</a></li>
  <li><a href="/cluster/capital-flow-brookfield-wealth-solutions-fy2025-20f-pass.md">Capital Flow Brookfield Wealth Solutions FY2025 20-F Pass</a></li>
  <li><a href="/cluster/capital-flow-blackstone-credit-insurance-pass.md">Capital Flow Blackstone Credit & Insurance Pass</a></li>
  <li><a href="/cluster/capital-flow-insurance-statutory-asset-quality-bridge-pass-1.md">Capital Flow Insurance Statutory Asset-Quality Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-ares-q2-2026-platform-credit-pass.md">Capital Flow Ares Q2 2026 Platform Credit Pass</a></li>
  <li><a href="/cluster/capital-flow-arcc-source-of-capital-pass.md">Capital Flow ARCC Source-Of-Capital Pass</a></li>
  <li><a href="/cluster/capital-flow-sdlp-source-of-capital-pass.md">Capital Flow SDLP Source-Of-Capital Pass</a></li>
  <li><a href="/cluster/capital-flow-asif-source-of-capital-pass.md">Capital Flow ASIF Source-Of-Capital Pass</a></li>
  <li><a href="/cluster/capital-flow-fsk-source-of-capital-pass.md">Capital Flow FSK Source-Of-Capital Pass</a></li>
  <li><a href="/cluster/capital-flow-kfits-source-of-capital-pass.md">Capital Flow K-FITS Source-Of-Capital Pass</a></li>
  <li><a href="/cluster/capital-flow-gsbd-source-of-capital-pass.md">Capital Flow GSBD Source-Of-Capital Pass</a></li>
  <li><a href="/cluster/capital-flow-gspcc-source-of-capital-pass.md">Capital Flow GSPCC Source-Of-Capital Pass</a></li>
  <li><a href="/cluster/capital-flow-obdc-source-of-capital-pass.md">Capital Flow OBDC Source-Of-Capital Pass</a></li>
  <li><a href="/cluster/capital-flow-ares-selected-direct-lending-destination-map.md">Capital Flow Ares Selected Direct-Lending Destination Map</a></li>
  <li><a href="/cluster/capital-flow-ares-borrower-follow-through-pass.md">Capital Flow Ares Borrower Follow-Through Pass</a></li>
  <li><a href="/cluster/capital-flow-atwell-bank-replacement-test.md">Capital Flow Atwell Bank-Replacement Test</a></li>
  <li><a href="/cluster/capital-flow-atwell-bank-replacement-pursuit.md">Capital Flow Atwell Bank-Replacement Pursuit</a></li>
  <li><a href="/cluster/capital-flow-atwell-bank-role-resolution-bridge-pass-1.md">Capital Flow Atwell Bank-Role Resolution Bridge Pass 1</a></li>
  <li><a href="/cluster/capital-flow-atwell-kfits-holding-extraction.md">Capital Flow Atwell K-FITS Holding Extraction</a></li>
  <li><a href="/cluster/capital-flow-atwell-sec-holder-crosswalk.md">Capital Flow Atwell SEC Holder Crosswalk</a></li>
  <li><a href="/cluster/capital-flow-aeritek-sec-holder-crosswalk.md">Capital Flow AeriTek SEC Holder Crosswalk</a></li>
  <li><a href="/cluster/capital-flow-frontline-sec-holder-crosswalk.md">Capital Flow Frontline SEC Holder Crosswalk</a></li>
  <li><a href="/cluster/capital-flow-jiffy-transaction-gap-pass.md">Capital Flow Jiffy Transaction Gap Pass</a></li>
  <li><a href="/cluster/capital-flow-master-borrower-exposure-rollup.md">Capital Flow Master Borrower Exposure Rollup</a></li>
  <li><a href="/cluster/capital-flow-ares-borrower-holder-expansion-pass-1.md">Capital Flow Ares Borrower Holder Expansion Pass 1</a></li>
  <li><a href="/cluster/capital-flow-ares-borrower-facility-use-cash-proof-stack-pass-1.md">Capital Flow Ares Borrower Facility/Use/Cash Proof Stack Pass 1</a></li>
  <li><a href="/cluster/capital-flow-holder-source-of-funds-map.md">Capital Flow Holder Source-Of-Funds Map</a></li>
  <li><a href="/cluster/capital-flow-vehicle-taxonomy.md">Capital Flow Vehicle Taxonomy</a></li>
  <li><a href="/cluster/capital-flow-ultimate-source-proof-plan.md">Capital Flow Ultimate Source Proof Plan</a></li>
  <li><a href="/cluster/capital-flow-mai-sec-holder-crosswalk.md">Capital Flow MAI SEC Holder Crosswalk</a></li>
  <li><a href="/cluster/capital-flow-precinmac-sec-holder-crosswalk.md">Capital Flow Precinmac SEC Holder Crosswalk</a></li>
  <li><a href="/cluster/capital-flow-relation-sec-holder-crosswalk.md">Capital Flow Relation SEC Holder Crosswalk</a></li>
  <li><a href="/cluster/capital-flow-sunvair-sec-holder-crosswalk.md">Capital Flow Sunvair SEC Holder Crosswalk</a></li>
  <li><a href="/cluster/capital-flow-valcourt-sec-holder-crosswalk.md">Capital Flow Valcourt SEC Holder Crosswalk</a></li>
  <li><a href="/cluster/capital-flow-insurance-credit-channel-comparison.md">Capital Flow Insurance-Credit Channel Comparison</a></li>
  <li><a href="/cluster/capital-flow-derived-claim-metrics-pass.md">Capital Flow Derived Claim Metrics Pass</a></li>
  <li><a href="/cluster/capital-flow-next-evidence-coverage-pass.md">Capital Flow Next Evidence Coverage Pass</a></li>
  <li><a href="/cluster/capital-flow-bank-denominator-comparison.md">Capital Flow Bank Denominator Comparison</a></li>
  <li><a href="/cluster/capital-flow-bdc-borrower-evidence.md">Capital Flow BDC Borrower Evidence</a></li>
  <li><a href="/cluster/capital-flow-bdc-industry-lane-evidence.md">Capital Flow BDC Industry Lane Evidence</a></li>
  <li><a href="/cluster/capital-flow-borrower-matching-workbench.md">Capital Flow Borrower Matching Workbench</a></li>
  <li><a href="/cluster/capital-flow-borrower-source-of-funds-pass.md">Capital Flow Borrower Source-Of-Funds Pass</a></li>
  <li><a href="/cluster/capital-flow-borrower-credit-document-pursuit-log.md">Capital Flow Borrower Credit Document Pursuit Log</a></li>
  <li><a href="/cluster/capital-flow-arcc-schedule-parser-pass.md">Capital Flow ARCC Schedule Parser Pass</a></li>
  <li><a href="/cluster/capital-flow-obdc-schedule-parser-pass.md">Capital Flow OBDC Schedule Parser Pass</a></li>
  <li><a href="/cluster/capital-flow-bxsl-industry-percentage-pass.md">Capital Flow BXSL Industry Percentage Pass</a></li>
  <li><a href="/cluster/capital-flow-cross-bdc-industry-lane-comparison.md">Capital Flow Cross-BDC Industry Lane Comparison</a></li>
  <li><a href="/cluster/capital-flow-bank-credit-trend-test.md">Capital Flow Bank Credit Trend Test</a></li>
</ul></section>"""
            self.send_html(page_shell("Company Reports", content))
            return

        if parsed.path.startswith("/company/"):
            rel = unquote(parsed.path.removeprefix("/company/"))
            target = (EXTRACTED / rel).resolve()
            if not target.is_file() or EXTRACTED.resolve() not in target.parents:
                self.send_error(404)
                return
            company_dir = target.parent
            active = str(company_dir.relative_to(EXTRACTED))
            tabs = []
            analysis = FIRST_PRINCIPLES / company_dir.relative_to(EXTRACTED) / "company-analysis.md"
            if analysis.exists():
                href = f"/analysis/{quote(str(analysis.relative_to(FIRST_PRINCIPLES)))}"
                tabs.append(f'<a href="{href}">Analysis</a>')
            for name, label in [("company-packet.md", "Packet"), ("company-profile.md", "Profile"), ("source-ledger.md", "Source Ledger")]:
                candidate = company_dir / name
                if candidate.exists():
                    href = f"/company/{quote(str(candidate.relative_to(EXTRACTED)))}"
                    tabs.append(f'<a href="{href}">{label}</a>')
            text = target.read_text(encoding="utf-8", errors="replace")
            content = f'<article class="doc"><div class="tabs">{"".join(tabs)}</div>{render_markdown(text)}</article>'
            self.send_html(page_shell(target.name, content, active))
            return

        if parsed.path.startswith("/analysis/"):
            rel = unquote(parsed.path.removeprefix("/analysis/"))
            target = (FIRST_PRINCIPLES / rel).resolve()
            if not target.is_file() or FIRST_PRINCIPLES.resolve() not in target.parents:
                self.send_error(404)
                return
            company_rel = target.parent.relative_to(FIRST_PRINCIPLES)
            company_dir = EXTRACTED / company_rel
            if not company_dir.exists():
                self.send_error(404)
                return
            active = str(company_rel)
            tabs = [f'<a href="/analysis/{quote(str(target.relative_to(FIRST_PRINCIPLES)))}">Analysis</a>']
            for name, label in [("company-packet.md", "Packet"), ("company-profile.md", "Profile"), ("source-ledger.md", "Source Ledger")]:
                candidate = company_dir / name
                if candidate.exists():
                    href = f"/company/{quote(str(candidate.relative_to(EXTRACTED)))}"
                    tabs.append(f'<a href="{href}">{label}</a>')
            text = target.read_text(encoding="utf-8", errors="replace")
            content = f'<article class="doc"><div class="tabs">{"".join(tabs)}</div>{render_markdown(text)}</article>'
            self.send_html(page_shell(target.name, content, active))
            return

        if parsed.path.startswith("/cluster/"):
            rel = unquote(parsed.path.removeprefix("/cluster/"))
            target = (FIRST_PRINCIPLES / rel).resolve()
            if not target.is_file() or FIRST_PRINCIPLES.resolve() not in target.parents:
                self.send_error(404)
                return
            text = target.read_text(encoding="utf-8", errors="replace")
            content = f'<article class="doc">{render_markdown(text)}</article>'
            self.send_html(page_shell(target.name, content))
            return

        if parsed.path == "/raw":
            params = parse_qs(parsed.query)
            rel = params.get("path", [""])[0]
            target = (ROOT / rel).resolve()
            if not target.is_file() or ROOT.resolve() not in target.parents:
                self.send_error(404)
                return
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(target.read_bytes())
            return

        self.send_error(404)

    def log_message(self, fmt: str, *args: object) -> None:
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def send_html(self, payload: bytes) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


def main() -> None:
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"Serving {len(company_dirs())} company reports at http://{HOST}:{PORT}/", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
