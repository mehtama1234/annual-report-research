#!/usr/bin/env python3
"""Add sector pages + company-insight index to the trends site, and nav. Trend pages already built by build_site2."""
import json, os, glob, html, collections, re
A=os.path.dirname(os.path.abspath(__file__))
OUT="/home/manishmehta/ui-projects/annual-report-research/site/trends"
def e(s): return html.escape(str(s if s is not None else ""))
trends=json.load(open(os.path.join(A,"trends_final.json")))
overviews={t["slug"]: (json.load(open(os.path.join(A,"writeups",t["slug"]+".json"))) if os.path.exists(os.path.join(A,"writeups",t["slug"]+".json")) else None) for t in trends}
sectors=[]
for f in sorted(glob.glob(os.path.join(A,"sectors","*.json"))):
    try: sectors.append(json.load(open(f)))
    except: pass
sectors=[s for s in sectors if s]
# company insights
comps=[]
for f in glob.glob(os.path.join(A,"company_insights","*.jsonl")):
    for line in open(f):
        line=line.strip()
        if line:
            try: comps.append(json.loads(line))
            except: pass
# dedupe by company
seen={}; 
for c in comps:
    if c.get("company"): seen[c["company"]]=c
comps=list(seen.values())

# extra CSS
css=open(os.path.join(OUT,"trends.css")).read()
if ".topnav" not in css:
    css+="""
.topnav{display:flex;gap:20px;border-bottom:1px solid var(--line);padding:10px 0 14px;margin-bottom:20px;font:600 14px/1 -apple-system,system-ui,sans-serif}
.topnav a{color:var(--muted);text-decoration:none}.topnav a.on{color:var(--accent)}
.subtrend{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin-bottom:10px}
.subtrend h4{margin:.1em 0 .3em;font-size:1.08rem}
.standout li{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:9px 13px;margin-bottom:7px;list-style:none;font-size:.95rem}
.standout b{color:var(--gold)}
.vok{color:#2e7d32;font-weight:700;font-size:.85em;margin-left:3px}
.vwarn{color:#b26a00;font-weight:700;font-size:.85em;margin-left:3px}
.breaker{background:#fdf6f2;border:1px solid #e8d4c8;border-left:4px solid var(--accent);border-radius:10px;padding:14px 18px;margin:1.4em 0}
.breaker h2{border:0;margin:.2em 0 .5em;color:var(--accent)}
.cochips{display:flex;flex-wrap:wrap;gap:7px;margin:.4em 0 1em}
.cochip{font:600 12px/1 -apple-system,system-ui,sans-serif;background:var(--card);border:1px solid var(--line);border-radius:20px;padding:6px 11px;text-decoration:none;color:var(--ink)}
.cochip:hover{border-color:var(--accent);color:var(--accent)}
.cico a.tl{font:600 11px/1 -apple-system,system-ui,sans-serif;color:var(--accent);text-decoration:none;margin-right:8px}
#csearch{width:100%;max-width:520px;font:400 16px/1.4 -apple-system,system-ui,sans-serif;padding:11px 14px;border:1px solid var(--line);border-radius:10px;margin:6px 0 18px}
.standout a{color:var(--accent);text-decoration:none}
.cico{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:13px 15px;margin-bottom:9px}
.cico .cn{font-weight:700}.cico .ind{font:400 11px/1 -apple-system,system-ui,sans-serif;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}
.cico .hl{margin:.35em 0 .3em}.cico .sn{color:var(--accent);font:600 13px/1.4 -apple-system,system-ui,sans-serif}
.cico .wd{color:var(--muted);font-size:.92rem;margin-top:.3em}
"""
    open(os.path.join(OUT,"trends.css"),"w").write(css)

import re as _re
try: CROSS=json.load(open(os.path.join(A,"crosslinks.json")))
except Exception: CROSS={"company_trends":{},"trend_names":{},"registry":{}}
def canchor(nm): return _re.sub(r'[^a-z0-9]+','-',(nm or '').lower()).strip('-')
def trendlinks_for(nm):
    a=canchor(nm); slugs=CROSS.get("company_trends",{}).get(a,[])
    tn=CROSS.get("trend_names",{})
    return "".join(f'<a class=tl href="/site/trends/{e(sl)}.html">{e(tn.get(sl,sl))}</a>' for sl in slugs)
NAV='<div class=topnav><a href="/site/trends/index.html">Trends</a><a href="/site/trends/sectors.html">Sectors</a><a href="/site/trends/companies.html">Companies</a></div>'
def page(title, body, home=False):
    cls="wrap home" if home else "wrap"
    return f"""<!doctype html><html lang=en><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>{e(title)}</title><link rel=stylesheet href="/site/trends/trends.css"></head><body><div class="{cls}">{NAV}{body}</div></body></html>"""

# sector pages
sec_built=0
for s in sectors:
    sl=s.get("slug"); 
    nums="".join(f'<div class="num"><b>{e(n.get("stat"))}</b><span>{e(n.get("label"))}</span></div>' for n in (s.get("numbers") or []) if isinstance(n,dict) and n.get("stat"))
    subs="".join(f'<div class=subtrend><h4>{e(st.get("name"))}</h4><p>{e(st.get("what"))}</p><p class=quiet>{e(", ".join(st.get("companies",[])[:8]))}</p></div>' for st in (s.get("sub_trends") or []) if isinstance(st,dict))
    stand="".join(f'<li><b><a href="/site/trends/companies.html#{e(canchor(x.get("company")))}">{e(x.get("company"))}</a></b> — {e(x.get("why_notable"))}</li>' for x in (s.get("standout_companies") or []) if isinstance(x,dict))
    summ="".join(f"<p>{e(p)}</p>" for p in (s.get("summary","").split("\n\n") if isinstance(s.get("summary"),str) else s.get("summary") or []))
    body=f"""<p class=crumb><a href="/site/trends/sectors.html">← all sectors</a></p>
<p class=kick>Sector synthesis</p><h1>{e(s.get("sector"))}</h1><p class=deck>{e(s.get("deck"))}</p>
<h2>The state of the sector</h2>{summ}
<h2>What the numbers say</h2><div class=nums>{nums}</div>
<h2>Sub-trends inside the sector</h2>{subs}
<h2>Standout companies</h2><ul class=standout>{stand}</ul>
<h2>The tension</h2><p>{e(s.get("tension"))}</p>
<h2>Who wins · who loses</h2><p>{e(s.get("who_wins_who_loses"))}</p>
<h2>Outlook</h2><p>{e(s.get("outlook"))}</p>
<div class=one>{e(s.get("one_sentence"))}</div>"""
    open(os.path.join(OUT,f"sector-{sl}.html"),"w").write(page(s.get("sector"),body)); sec_built+=1
# sectors index
scards="".join(f'<a class=tcard href="/site/trends/sector-{e(s.get("slug"))}.html"><p class=kick>Sector</p><h3>{e(s.get("sector"))}</h3><p>{e(s.get("deck"))}</p></a>' for s in sectors)
open(os.path.join(OUT,"sectors.html"),"w").write(page("Sectors","<p class=kick>Sector-wise synthesis</p><h1>What's happening inside each sector</h1><p class=lede>Bottom-up synthesis of each sector's own dynamics, standout companies, and fault lines — from the coded filings.</p><div class=grid>"+scards+"</div>",home=True))

# companies index grouped by sector
bysec=collections.defaultdict(list)
for c in comps: bysec[(c.get("sector") or "Other")].append(c)
blocks=[]
for sec in sorted(bysec):
    def _cico(c):
        tl=trendlinks_for(c.get("company"))
        tlrow=f'<div style="margin-top:6px">{tl}</div>' if tl else ""
        return (f'<div class=cico id="{e(canchor(c.get("company")))}" data-name="{e((c.get("company") or "").lower())} {e((c.get("industry") or "").lower())}">'
                f'<span class=ind>{e(c.get("industry"))}</span><div class=cn>{e(c.get("company"))}</div>'
                f'<div class=hl>{e(c.get("headline"))}</div><div class=sn>{e(c.get("standout_number"))}</div>'
                f'<div class=wd>{e(c.get("whats_different"))}</div>{tlrow}</div>')
    cards="".join(_cico(c) for c in sorted(bysec[sec],key=lambda x:x.get("company") or ""))
    blocks.append(f'<details><summary style="cursor:pointer;font:700 1.15rem/1.3 -apple-system,system-ui,sans-serif;margin:14px 0 6px">{e(sec)} <span style="opacity:.6;font-weight:400">({len(bysec[sec])})</span></summary>{cards}</details>')
SEARCH=('<input id=csearch type=search placeholder="Search '+str(len(comps))+' companies or industries…" autocomplete=off>'
        '<script>(function(){var b=document.getElementById("csearch");var cards=[].slice.call(document.querySelectorAll(".cico"));'
        'var groups=[].slice.call(document.querySelectorAll("details"));'
        'b.addEventListener("input",function(){var q=b.value.trim().toLowerCase();'
        'if(!q){cards.forEach(function(c){c.style.display=""});groups.forEach(function(g){g.style.display="";g.open=false});return;}'
        'groups.forEach(function(g){g.open=true;var any=false;'
        '[].slice.call(g.querySelectorAll(".cico")).forEach(function(c){var m=(c.getAttribute("data-name")||"").indexOf(q)>-1||c.textContent.toLowerCase().indexOf(q)>-1;c.style.display=m?"":"none";if(m)any=true;});'
        'g.style.display=any?"":"none";});});})();</script>')
open(os.path.join(OUT,"companies.html"),"w").write(page("Company insights","<p class=kick>Per-company</p><h1>What's distinctive about each of "+str(len(comps))+" companies</h1><p class=lede>The one notable, unusual, or surprising thing about each company from its latest filing — grouped by sector. Each links to the trends it appears in.</p>"+SEARCH+"".join(blocks),home=True))
print(f"built {sec_built} sector pages + sectors index + companies index ({len(comps)} companies)")
