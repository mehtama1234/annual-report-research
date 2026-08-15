#!/usr/bin/env python3
"""Build the DEEP trends site: home -> trend hub (overview + grouped angles) -> angle sub-pages."""
import json, os, glob, html
A=os.path.dirname(os.path.abspath(__file__))
OUT="/home/manishmehta/ui-projects/annual-report-research/site/trends"
os.makedirs(OUT, exist_ok=True)
def e(s): return html.escape(str(s if s is not None else ""))
trends=json.load(open(os.path.join(A,"trends_final.json")))
def load(p):
    try: return json.load(open(p))
    except Exception: return None
overviews={t["slug"]: load(os.path.join(A,"writeups",f"{t['slug']}.json")) for t in trends}
outlines={t["slug"]: load(os.path.join(A,"outlines",f"{t['slug']}.json")) for t in trends}
subs={}
for f in glob.glob(os.path.join(A,"subwriteups","*.json")):
    w=load(f)
    if not w: continue
    base=os.path.basename(f)[:-5]  # <trend_slug>__<sub_slug>  (authoritative)
    if "__" not in base: continue
    tslug,ss=base.split("__",1)
    subs.setdefault(tslug,{})[ss]=w

CSS=open(os.path.join(OUT,"trends.css")).read() if os.path.exists(os.path.join(OUT,"trends.css")) else ""
if "--ink" not in CSS:
    CSS=open(os.path.join(A,"_css_fallback.txt")).read() if os.path.exists(os.path.join(A,"_css_fallback.txt")) else CSS
# add a bit of nav css
CSS+="""
.crumb{font:600 12px/1 -apple-system,system-ui,sans-serif;color:var(--muted);margin-bottom:6px}
.crumb a{color:var(--accent);text-decoration:none}
.groupt{font:700 1.1rem/1.2 -apple-system,system-ui,sans-serif;color:var(--ink);margin:1.8em 0 .2em}
.angles{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px;margin:.6em 0 1.4em}
.acard{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px;text-decoration:none;color:var(--ink);transition:.15s}
.acard:hover{border-color:var(--accent);transform:translateY(-2px)}
.acard .at{font:600 10px/1 -apple-system,system-ui,sans-serif;letter-spacing:.09em;text-transform:uppercase;color:var(--gold)}
.acard h4{font-size:1.12rem;line-height:1.2;margin:.35em 0 .3em}
.acard p{color:var(--muted);font-size:.92rem;margin:0}
.momentum{margin:1.6em 0}
.verdict{display:flex;align-items:center;gap:10px;flex-wrap:wrap;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 16px;margin:.4em 0 1em}
.verdict .vsym{font-size:1.1rem;font-weight:700}
.verdict .vlab{font:700 13px/1 -apple-system,system-ui,sans-serif;text-transform:uppercase;letter-spacing:.06em}
.verdict .vhead{color:var(--muted);font-size:.95rem;flex:1;min-width:220px}
.verdict.acc{border-left:4px solid #2e7d32}.verdict.acc .vsym,.verdict.acc .vlab{color:#2e7d32}
.verdict.dec{border-left:4px solid #b23c3c}.verdict.dec .vsym,.verdict.dec .vlab{color:#b23c3c}
.verdict.std{border-left:4px solid var(--gold)}.verdict.std .vsym,.verdict.std .vlab{color:var(--gold)}
.verdict.mix{border-left:4px solid var(--muted)}.verdict.mix .vsym,.verdict.mix .vlab{color:var(--muted)}
.mtblwrap{overflow-x:auto;margin:.4em 0 .8em}
.mtbl{border-collapse:collapse;width:100%;font-size:.9rem}
.mtbl th{text-align:left;font:700 11px/1.3 -apple-system,system-ui,sans-serif;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);border-bottom:1px solid var(--line);padding:6px 10px}
.mtbl td{border-bottom:1px solid var(--line);padding:8px 10px;vertical-align:top}
.mtbl .dc{font-weight:700;white-space:nowrap}.mtbl .dm{color:var(--muted)}
.mtbl .dv{white-space:nowrap}.mtbl .arw{color:var(--accent)}
.mtbl .dch{font-weight:700;color:var(--ink);white-space:nowrap}.mtbl .dr{color:var(--muted)}
.mnote{font-size:.97rem}
"""
open(os.path.join(OUT,"trends.css"),"w").write(CSS)

def page(title, body, home=False):
    cls="wrap home" if home else "wrap"
    return f"""<!doctype html><html lang=en><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>{e(title)}</title><link rel=stylesheet href="/site/trends/trends.css"></head><body><div class="{cls}">{body}</div></body></html>"""

try:
    CROSS=json.load(open(os.path.join(A,"crosslinks.json")))
except Exception:
    CROSS={"trend_companies":{},"company_trends":{},"trend_names":{}}

MOM={}
for _mf in glob.glob(os.path.join(A,"momentum","*.json")):
    try: MOM[os.path.basename(_mf)[:-5]]=json.load(open(_mf))
    except Exception: pass
VERD={"accelerating":("▲","Accelerating","acc"),"steady":("▬","Holding steady","std"),
      "decelerating":("▼","Decelerating","dec"),"mixed":("◆","Mixed / diverging","mix")}
def momentum_html(slug):
    m=MOM.get(slug)
    if not isinstance(m,dict) or not m.get("deltas"): return ""
    sym,lab,cls=VERD.get(m.get("verdict","mixed"),VERD["mixed"])
    rows="".join(
        f'<tr><td class=dc>{e(d.get("company"))}</td><td class=dm>{e(d.get("metric"))}</td>'
        f'<td class=dv>{e(d.get("from"))} <span class=arw>→</span> {e(d.get("to"))}</td>'
        f'<td class=dch>{e(d.get("change"))}</td><td class=dr>{e(d.get("reads"))}</td></tr>'
        for d in m["deltas"] if isinstance(d,dict))
    return (f'<section class=momentum><h2>Direction of travel</h2>'
            f'<div class="verdict {cls}"><span class=vsym>{sym}</span><span class=vlab>{e(lab)}</span>'
            f'<span class=vhead>{e(m.get("headline"))}</span></div>'
            f'<div class=mtblwrap><table class=mtbl><thead><tr><th>Company</th><th>What moved</th>'
            f'<th>Then → now</th><th>Change</th><th>What it signals</th></tr></thead><tbody>{rows}</tbody></table></div>'
            f'<p class=mnote>{e(m.get("momentum_note"))}</p></section>')

def _mark(item):
    if isinstance(item,dict) and "verified" in item:
        return '<span class="vok" title="found in source filing">✓</span>' if item.get("verified") else '<span class="vwarn" title="not located in the packet — treat as unverified">⚠</span>'
    return ""

def render_essay(w, crumb=""):
    def _num(n):
        if isinstance(n,dict): return f'<div class="num"><b>{e(n.get("stat"))}{_mark(n)}</b><span>{e(n.get("label"))}</span></div>' if n.get("stat") else ""
        return f'<div class="num"><span>{e(n)}</span></div>' if n else ""
    nums="".join(_num(n) for n in (w.get("numbers") or []))
    _m=w.get("mechanism") or []
    if isinstance(_m,str): _m=[x for x in _m.split("\n\n") if x.strip()]
    mech="".join(f"<p>{e(p)}</p>" for p in _m)
    def _ev(x):
        if isinstance(x,dict): return f'<li><b>{e(x.get("company"))}</b> — {e(x.get("fact"))} {_mark(x)}</li>'
        return f'<li>{e(x)}</li>'
    ev="".join(_ev(x) for x in (w.get("evidence") or []))
    # thesis-breaker (hubs only)
    tb=w.get("thesis_breaker"); tb_html=""
    if isinstance(tb,dict):
        cc="".join(f'<li><b>{e(c.get("company"))}</b> — {e(c.get("fact"))}</li>' for c in (tb.get("contradicting_companies") or []) if isinstance(c,dict))
        tb_html=(f'<section class=breaker><h2>The case against this trend</h2>'
                 f'<p><b>What would falsify it:</b> {e(tb.get("what_would_falsify"))}</p>'
                 f'<p><b>Companies that don\'t fit:</b></p><ul class=ev>{cc}</ul>'
                 f'<p><b>Honest caveat:</b> {e(tb.get("honest_caveat"))}</p></section>')
    return f"""{crumb}
<h1>{e(w.get('name'))}</h1>
<p class=deck>{e(w.get('deck'))}</p>
<div class=corebet>{e(w.get('core_bet'))}</div>
<h2>What the numbers say</h2><div class=nums>{nums}</div>
<h2>The mechanism</h2>{mech}
<h2>Why now</h2><p>{e(w.get('why_now'))}</p>
<h2>Who pays · who profits</h2><div class=two><div class=box><div class=l>Who pays</div>{e(w.get('who_pays'))}</div><div class=box><div class=l>Who profits</div>{e(w.get('who_profits'))}</div></div>
<h2>The tension</h2><p>{e(w.get('tension'))}</p>
<h2>The surprising part</h2><p>{e(w.get('surprising_part'))}</p>
<h2>Why it matters</h2><p>{e(w.get('societal_stake'))}</p>
<div class=one>{e(w.get('one_sentence'))}</div>
{tb_html}
<h2>The evidence</h2><ul class=ev>{ev}</ul>
<footer>Built bottom-up from 519 company annual-report/earnings packets via open → axial → selective coding. <span class=vok>✓</span> = figure located in the source filing; <span class=vwarn>⚠</span> = not located, treat as unverified.</footer>"""

ANGLE_LABEL={"origin":"Origin","sub-pattern":"Sub-pattern","company-deepdive":"Company deep-dive","who-profits":"Who profits","who-pays":"Who pays","tension":"The tension"}
built_sub=0; built_hub=0; cards=[]
for t in trends:
    slug=t["slug"]; ov=overviews.get(slug); ol=outlines.get(slug); tsub=subs.get(slug,{})
    if not ov: continue
    # sub pages
    angle_nav=""
    if ol and ol.get("groups"):
        for g in ol["groups"]:
            acards=[]
            for ang in g.get("angles",[]):
                ss=ang.get("sub_slug"); w=tsub.get(ss)
                if not w: continue
                fn=f"{slug}__{ss}.html"
                crumb=f'<p class=crumb><a href="/site/trends/index.html">Trends</a> · <a href="/site/trends/{slug}.html">{e(ov.get("name"))}</a></p>'
                open(os.path.join(OUT,fn),"w").write(page(w.get("name"), render_essay(w,crumb))); built_sub+=1
                acards.append(f'<a class=acard href="/site/trends/{fn}"><span class=at>{e(ANGLE_LABEL.get(ang.get("angle_type"),"Angle"))}</span><h4>{e(w.get("name"))}</h4><p>{e(w.get("deck") or ang.get("focus"))}</p></a>')
            if acards:
                angle_nav+=f'<div class=groupt>{e(g.get("group_title"))}</div><div class=angles>{"".join(acards)}</div>'
    # hub page = overview essay + angle nav
    crumb=f'<p class=crumb><a href="/site/trends/index.html">← all trends</a></p>'
    body=render_essay(ov, crumb)
    # momentum / direction-of-travel (hubs only), placed right after the numbers section
    mh=momentum_html(slug)
    if mh:
        body=body.replace("<h2>The mechanism</h2>", mh+"<h2>The mechanism</h2>",1)
    # cross-link: companies cited in this trend -> company cards
    colinks=CROSS.get("trend_companies",{}).get(slug,[])
    if colinks:
        chips="".join(f'<a class=cochip href="/site/trends/companies.html#{e(c["anchor"])}">{e(c["company"])}</a>' for c in colinks)
        body=body.replace("<h2>The evidence</h2>", f'<h2>Companies in this trend ({len(colinks)})</h2><div class=cochips>{chips}</div><h2>The evidence</h2>',1)
    if angle_nav:
        body=body.replace("<footer>", f'<h2>Go deeper — {sum(len(g.get("angles",[])) for g in ol["groups"]) } angles</h2>{angle_nav}<footer>',1)
    open(os.path.join(OUT,f"{slug}.html"),"w").write(page(ov.get("name"), body)); built_hub+=1
    na=sum(1 for g in (ol.get("groups",[]) if ol else []) for _ in g.get("angles",[])) if ol else 0
    cards.append(f'<a class=tcard href="/site/trends/{slug}.html"><p class=kick>{e(" · ".join(t.get("axis_mix",[])[:2]))}{" · "+str(len(tsub))+" pages" if tsub else ""}</p><h3>{e(ov.get("name"))}</h3><p>{e(ov.get("deck") or ov.get("one_sentence"))}</p></a>')

total_sub=sum(len(v) for v in subs.values())
home=f"""<p class=kick>Bottom-up trend analysis</p>
<h1>What 519 companies are actually telling us</h1>
<p class=lede>Trends surfaced bottom-up from 519 company annual reports and the latest earnings — open-coded, clustered, and written up in depth. {built_hub} distinct dynamics, {total_sub} deep-dive pages, every figure traced to a filing.</p>
<div class=grid>{''.join(cards)}</div>
<footer>Method: open coding (2,157 codes from every packet) → axial coding (4-lens clustering) → selective coding (20 trends) → multi-page write-up. {built_hub} trends · {total_sub} sub-pages.</footer>"""
open(os.path.join(OUT,"index.html"),"w").write(page("Trends — What 519 companies are telling us", home, home=True))
print(f"built {built_hub} hubs + {built_sub} sub-pages")
