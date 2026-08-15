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
# dedupe by browser anchor so punctuation variants do not overwrite each other later
seen={};
def _early_canchor(nm): return re.sub(r'[^a-z0-9]+','-',(nm or '').lower()).strip('-')
for c in comps:
    if c.get("company"): seen[_early_canchor(c["company"])]=c
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
.tlx{font:600 11px/1 -apple-system,system-ui,sans-serif;color:var(--muted);margin-right:8px}
#csearch{width:100%;max-width:520px;font:400 16px/1.4 -apple-system,system-ui,sans-serif;padding:11px 14px;border:1px solid var(--line);border-radius:10px;margin:6px 0 18px}
.standout a{color:var(--accent);text-decoration:none}
.cico{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:13px 15px;margin-bottom:9px}
.cico .cn{font-weight:700}.cico .ind{font:400 11px/1 -apple-system,system-ui,sans-serif;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}
.cico .hl{margin:.35em 0 .3em}.cico .sn{color:var(--accent);font:600 13px/1.4 -apple-system,system-ui,sans-serif}
.cico .wd{color:var(--muted);font-size:.92rem;margin-top:.3em}
"""
    open(os.path.join(OUT,"trends.css"),"w").write(css)
if ".readmore" not in css:
    css+="""
.cico .cn a{color:var(--ink);text-decoration:none}
.cico .cn a:hover{color:var(--accent)}
.watch{border-top:1px solid var(--line);margin-top:10px;padding-top:8px;color:var(--muted);font:400 13px/1.45 -apple-system,system-ui,sans-serif}
.watch b{color:var(--gold);letter-spacing:.04em;text-transform:uppercase;font-size:11px}
.readmore{margin-top:8px;font:600 12px/1 -apple-system,system-ui,sans-serif}
.readmore a{text-decoration:none;color:var(--accent)}
.evgroup{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:0 0 12px}
.evgroup h3{font:700 1rem/1.25 -apple-system,system-ui,sans-serif;margin:0 0 8px}
.evgroup h3 a{text-decoration:none;color:var(--ink)}
.evgroup h3 a:hover{color:var(--accent)}
.evgroup .ev{margin-bottom:0}
.quiet{color:var(--muted);font:400 14px/1.5 -apple-system,system-ui,sans-serif}
.tlx{font:600 11px/1 -apple-system,system-ui,sans-serif;color:var(--muted);margin-right:8px}
"""
    open(os.path.join(OUT,"trends.css"),"w").write(css)
if ".tlx" not in css:
    css+="\n.tlx{font:600 11px/1 -apple-system,system-ui,sans-serif;color:var(--muted);margin-right:8px}\n"
    open(os.path.join(OUT,"trends.css"),"w").write(css)

import re as _re
try: CROSS=json.load(open(os.path.join(A,"crosslinks.json")))
except Exception: CROSS={"company_trends":{},"trend_names":{},"registry":{}}
def canchor(nm): return _re.sub(r'[^a-z0-9]+','-',(nm or '').lower()).strip('-')
def cpage(nm): return f'/site/trends/companies/{e(canchor(nm))}.html'
def resolve_slug(slug):
    if not slug:
        return None
    slug=slug[:-5] if slug.endswith(".json") else slug
    if os.path.exists(os.path.join(OUT,slug+".html")):
        return slug
    candidates=[]
    for f in glob.glob(os.path.join(OUT,"*.html")):
        base=os.path.splitext(os.path.basename(f))[0]
        if base.endswith("__"+slug):
            candidates.append(base)
    return candidates[0] if len(candidates)==1 else None
def trendlinks_for(nm):
    a=canchor(nm); slugs=CROSS.get("company_trends",{}).get(a,[])
    tn=CROSS.get("trend_names",{})
    parts=[]
    for sl in slugs:
        label=tn.get(sl,sl[:-5] if sl.endswith(".json") else sl)
        resolved=resolve_slug(sl)
        if resolved:
            parts.append(f'<a class=tl href="/site/trends/{e(resolved)}.html">{e(label)}</a>')
        else:
            parts.append(f'<span class=tlx>{e(label)}</span>')
    return "".join(parts)
NAV='<div class=topnav><a href="/site/trends/index.html">Trends</a><a href="/site/trends/sectors.html">Sectors</a><a href="/site/trends/companies.html">Companies</a></div>'
def page(title, body, home=False):
    cls="wrap home" if home else "wrap"
    return f"""<!doctype html><html lang=en><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>{e(title)}</title><link rel=stylesheet href="/site/trends/trends.css"></head><body><div class="{cls}">{NAV}{body}</div></body></html>"""

def source_href(slug):
    resolved=resolve_slug(slug)
    return f"/site/trends/{e(resolved)}.html" if resolved else ""

def load_company_evidence():
    out=collections.defaultdict(list)
    for f in sorted(glob.glob(os.path.join(A,"*.json"))):
        base=os.path.splitext(os.path.basename(f))[0]
        if base in {"crosslinks","trends_final","trend_packets"}:
            continue
        try:
            obj=json.load(open(f))
        except Exception:
            continue
        if not isinstance(obj,dict):
            continue
        slug=base
        title=obj.get("name") or obj.get("title") or slug.replace("-"," ").title()
        rows=[]
        for key in ("evidence","evidence_companies"):
            val=obj.get(key)
            if isinstance(val,list):
                rows.extend(x for x in val if isinstance(x,dict) and x.get("company") and x.get("fact"))
        for row in rows:
            out[canchor(row.get("company"))].append({
                "source": title,
                "slug": slug,
                "fact": row.get("fact"),
            })
    return out

company_evidence=load_company_evidence()

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
byind=collections.defaultdict(list)
for c in comps: byind[(c.get("sector") or "Other", c.get("industry") or "Other")].append(c)

company_dir=os.path.join(OUT,"companies")
os.makedirs(company_dir,exist_ok=True)

def build_company_page(c):
    nm=c.get("company") or ""
    anchor=canchor(nm)
    trendlinks=trendlinks_for(nm)
    trendrow=f'<div class=cochips>{trendlinks}</div>' if trendlinks else '<p class=quiet>No linked trend pages yet.</p>'
    evs=company_evidence.get(anchor,[])
    grouped=collections.defaultdict(list)
    seen_facts=set()
    for item in evs:
        fact=(item.get("fact") or "").strip()
        if not fact or fact in seen_facts:
            continue
        seen_facts.add(fact)
        grouped[(item.get("source"),item.get("slug"))].append(fact)
    evhtml=[]
    for (src,slug),facts in list(grouped.items())[:10]:
        lis="".join(f"<li>{e(fact)}</li>" for fact in facts[:5])
        href=source_href(slug)
        heading=f'<a href="{href}">{e(src)}</a>' if href else e(src)
        evhtml.append(f'<div class=evgroup><h3>{heading}</h3><ul class=ev>{lis}</ul></div>')
    if not evhtml:
        evhtml.append('<p class=quiet>No deeper coded trend evidence has been attached to this company yet. This page is built from the company insight record only.</p>')
    peers=[p for p in byind.get((c.get("sector") or "Other", c.get("industry") or "Other"),[]) if p.get("company")!=nm]
    peerchips="".join(f'<a class=cochip href="{cpage(p.get("company"))}">{e(p.get("company"))}</a>' for p in sorted(peers,key=lambda x:x.get("company") or "")[:18])
    peerblock=f'<h2>Same Industry Context</h2><div class=cochips>{peerchips}</div>' if peerchips else ""
    body=f"""<p class=crumb><a href="/site/trends/companies.html">← all companies</a></p>
<p class=kick>{e(c.get("sector"))} · {e(c.get("industry"))}</p>
<h1>{e(nm)}</h1>
<p class=deck>{e(c.get("headline"))}</p>
<div class=two>
  <div class=box><div class=l>Standout figure</div>{e(c.get("standout_number"))}</div>
  <div class=box><div class=l>Watch next</div>{e(c.get("watch"))}</div>
</div>
<h2>Why It Is Distinctive</h2>
<p>{e(c.get("whats_different"))}</p>
<h2>Trend Links</h2>
{trendrow}
<h2>Evidence Trail</h2>
{''.join(evhtml)}
{peerblock}
"""
    open(os.path.join(company_dir,f"{anchor}.html"),"w").write(page(nm,body))

for c in comps:
    build_company_page(c)

blocks=[]
for sec in sorted(bysec):
    def _cico(c):
        tl=trendlinks_for(c.get("company"))
        tlrow=f'<div style="margin-top:6px">{tl}</div>' if tl else ""
        return (f'<div class=cico id="{e(canchor(c.get("company")))}" data-name="{e((c.get("company") or "").lower())} {e((c.get("industry") or "").lower())}">'
                f'<span class=ind>{e(c.get("industry"))}</span><div class=cn><a href="{cpage(c.get("company"))}">{e(c.get("company"))}</a></div>'
                f'<div class=hl>{e(c.get("headline"))}</div><div class=sn>{e(c.get("standout_number"))}</div>'
                f'<div class=wd>{e(c.get("whats_different"))}</div>'
                f'<div class=watch><b>Watch:</b> {e(c.get("watch"))}</div>'
                f'{tlrow}<div class=readmore><a href="{cpage(c.get("company"))}">Open company page</a></div></div>')
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
open(os.path.join(OUT,"companies.html"),"w").write(page("Company insights","<p class=kick>Per-company</p><h1>What's distinctive about each of "+str(len(comps))+" companies</h1><p class=lede>Company-level reads from the latest filing packet: the distinctive operating fact, standout number, what to watch next, linked trend context, and a deeper evidence trail where the company appears in coded writeups.</p>"+SEARCH+"".join(blocks),home=True))
print(f"built {sec_built} sector pages + sectors index + companies index ({len(comps)} companies) + company detail pages")
