"""검색엔진용 정적 레슨 페이지, 레슨 목록, 사이트맵, robots.txt 생성.

    python3 tools/build_seo.py

- 레슨마다 /{과목}/learn/{레슨ID}.html 을 만든다(설명·예제·문제 지문을 HTML에 그대로 담음).
- 실제 풀이 화면(player.html)으로 가는 버튼을 단다. player.html 은 noindex 로 두어 이 페이지가 검색 대표가 된다.
- 콘텐츠를 고친 뒤에는 이 스크립트를 다시 실행하면 된다.
"""
import datetime, glob, html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_parts import FOOT_CSS, FOOT_HTML, SITE_JS, SITE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime.date.today().isoformat()
SUBJECTS = [("socio", "사회와 역사"), ("biz", "경제와 경영"), ("lit", "언어와 문학"), ("math", "수학"),
            ("sci", "과학"), ("tech", "공학"), ("arts", "예체능")]
EXTRA = [("lingua", "외국어"), ("code", "코딩")]   # 형식이 달라 정적 레슨 페이지 없이 목록만 연결
e = html.escape

CSS = """
:root{--paper:#FAFBFD;--ink:#172033;--ink-soft:#4A5670;--grid:#DCE4F0;--blue:#1D3FA8;--blue-soft:#E7ECFA;--marker:#FFD84D;
  --font:"IBM Plex Sans KR","Apple SD Gothic Neo","Malgun Gothic",sans-serif}
*{box-sizing:border-box}
html,body{margin:0;word-break:keep-all;overflow-wrap:anywhere;background:var(--paper);color:var(--ink);font-family:var(--font)}
:focus-visible{outline:3px solid var(--blue);outline-offset:3px}
.wrap{max-width:820px;margin:0 auto;padding:0 20px}
header{border-bottom:1px solid var(--grid);background:#fff}
header .hin{max-width:1040px;margin:0 auto;padding:0 20px;display:flex;align-items:center;justify-content:space-between;height:60px}
.logo{font-weight:700;font-size:20px;color:var(--ink);text-decoration:none}
header nav a{color:var(--ink-soft);text-decoration:none;margin-left:16px;font-size:15px}
main{padding:24px 0 8px;line-height:1.8;font-size:16px}
.crumb{font-size:14px;color:var(--ink-soft);margin:0 0 10px}
.crumb a{color:var(--ink-soft)}
h1{font-size:30px;line-height:1.3;margin:0 0 6px}
h2{font-size:20px;margin:32px 0 6px}
.meta{color:var(--ink-soft);font-size:14px;margin:0 0 16px}
.cta{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0}
.btn{display:inline-flex;align-items:center;font-weight:700;padding:11px 18px;border-radius:8px;border:1px solid var(--blue);background:var(--blue);color:#fff;text-decoration:none;min-height:44px}
.btn.ghost{background:#fff;color:var(--blue)}
.ex{background:#fff;border:1px solid var(--grid);border-radius:10px;padding:14px 18px;margin:14px 0}
.ex h3{font-size:16px;margin:0 0 6px}
.q{border-left:4px solid var(--marker);background:#fff;padding:10px 14px;margin:12px 0;border-radius:0 8px 8px 0}
.q b{display:block;font-size:13px;color:var(--ink-soft);margin-bottom:2px}
.nav{display:flex;justify-content:space-between;gap:12px;margin:28px 0;font-size:15px}
.nav a{color:var(--blue)}
ul.list{padding-left:20px}ul.list li{margin:4px 0}
.hub h2{border-top:1px solid var(--grid);padding-top:20px}
.hub h3{font-size:16px;margin:16px 0 4px}
.cnt{color:var(--ink-soft);font-size:14px}
"""


def shell(path, title, desc, body, canonical):
    out = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}{canonical}">
<meta property="og:type" content="article">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{SITE}{canonical}">
<meta property="og:site_name" content="edu-arena">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<style>{CSS}{FOOT_CSS}</style>
</head>
<body>
<header><div class="hin"><a class="logo" href="/">edu-arena</a><nav data-auth><a href="/#subjects">과목</a><a href="/lessons.html">레슨 목록</a></nav></div></header>
<main class="wrap">
{body}
</main>
{FOOT_HTML}
{SITE_JS}
</body>
</html>
"""
    full = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(out)


def paras(text):
    if text is None:
        return ""
    if isinstance(text, list):
        return "".join(paras(t) for t in text)
    return "".join(f"<p>{e(t)}</p>" for t in str(text).split("\n") if t.strip())


def blanks(prompt):
    return re.sub(r"\{\{\s*\w+\s*\}\}", "＿＿＿", prompt or "")


def describe(lesson):
    for s in lesson["screens"]:
        if s["type"] == "explain" and s.get("body"):
            t = " ".join(s["body"] if isinstance(s["body"], list) else [s["body"]])
            t = re.sub(r"\s+", " ", t).strip()
            return t[:150] + ("…" if len(t) > 150 else "")
    return lesson["lesson"]["title"]


def lesson_body(lesson):
    out, qn = [], 0
    for s in lesson["screens"]:
        t = s["type"]
        if t == "explain":
            out.append(f'<h2>{e(s.get("title") or "")}</h2>{paras(s.get("body"))}')
        elif t == "example":
            steps = "".join(f"<li>{e(x)}</li>" for x in (s.get("steps") or []))
            ans = f'<p><strong>답:</strong> {e(str(s["answer"]))}</p>' if s.get("answer") not in (None, "") else ""
            out.append(f'<div class="ex"><h3>{e(s.get("title") or "예제")}</h3>{paras(s.get("problem"))}'
                       f'{"<ol>" + steps + "</ol>" if steps else ""}{ans}</div>')
        elif t == "question":
            qn += 1
            out.append(f'<div class="q"><b>문제 {qn}</b>{paras(blanks(s.get("prompt")))}</div>')
    return "\n".join(out), qn


def collect():
    """과목별 (레슨 목록, 묶음 정보)"""
    data = {}
    for subj, sname in SUBJECTS:
        items, groups = [], []
        cj = json.load(open(os.path.join(ROOT, subj, "content/level1/courses.json"), encoding="utf-8"))
        for c in cj["courses"]:
            cdir = os.path.join(ROOT, subj, "content/level1", c["id"])
            chs = []
            for chf in sorted(glob.glob(os.path.join(cdir, "ch*/chapter.json"))):
                ch = json.load(open(chf, encoding="utf-8"))
                chno = os.path.basename(os.path.dirname(chf))[2:]
                ls = []
                for l in ch["lessons"]:
                    lf = os.path.join(os.path.dirname(chf), l["file"])
                    if not os.path.exists(lf):
                        continue
                    lno = f'{int(l["no"]):02d}'
                    q = f'c={c["id"]}&ch={chno}&l={lno}'
                    it = dict(subj=subj, sname=sname, id=l["id"], title=l["title"], file=lf,
                              crumbs=[(f"/{subj}/browse.html", sname), (f"/{subj}/browse.html?c={c['id']}", c["title"])],
                              chapter=f'{ch["chapter"]["no"]}. {ch["chapter"]["title"]}',
                              play=f"/{subj}/player.html?{q}", practice=f"/{subj}/player.html?{q}&practice=1",
                              essay=f"/{subj}/essay.html?{q}" if l.get("essay") else None, group=c["title"], level="레벨1")
                    items.append(it); ls.append(it)
                chs.append((ch["chapter"]["title"], ls))
            groups.append((c["title"], c.get("description", ""), chs))
        # 심화(올림피아드)
        for sjf in sorted(glob.glob(os.path.join(ROOT, subj, "olympiad/content/*/subject.json"))):
            sj = json.load(open(sjf, encoding="utf-8"))
            key = os.path.basename(os.path.dirname(sjf))
            for st in sj["stages"]:
                for tr in st["tracks"]:
                    tdir = os.path.join(os.path.dirname(sjf), f's{st["no"]}', tr["id"])
                    if not os.path.isdir(tdir):
                        continue
                    chs = []
                    for chf in sorted(glob.glob(os.path.join(tdir, "ch*/chapter.json"))):
                        ch = json.load(open(chf, encoding="utf-8"))
                        chno = os.path.basename(os.path.dirname(chf))[2:]
                        ls = []
                        for l in ch["lessons"]:
                            lf = os.path.join(os.path.dirname(chf), l["file"])
                            if not os.path.exists(lf):
                                continue
                            q = f'subj={key}&s={st["no"]}&t={tr["id"]}&ch={chno}&l={int(l["no"]):02d}'
                            gname = f'{sj["subject"]["title"]} {st["title"]} · {tr["title"]}'
                            it = dict(subj=subj, sname=sname, id=l["id"], title=l["title"], file=lf,
                                      crumbs=[(f"/{subj}/browse.html", sname), (f"/{subj}/olympiad/browse.html", "심화"),
                                              (f"/{subj}/olympiad/browse.html", gname)],
                                      chapter=f'{ch["chapter"]["no"]}. {ch["chapter"]["title"]}',
                                      play=f"/{subj}/olympiad/player.html?{q}", practice=None, essay=None,
                                      group=gname, level="심화")
                            items.append(it); ls.append(it)
                        chs.append((ch["chapter"]["title"], ls))
                    if chs:
                        groups.append((gname, tr.get("description", ""), chs))
        data[subj] = (items, groups)
    return data


def build_lessons(data):
    total = 0
    for subj, (items, groups) in data.items():
        old = glob.glob(os.path.join(ROOT, subj, "learn", "*.html"))
        for f in old:
            os.remove(f)
        for i, it in enumerate(items):
            lesson = json.load(open(it["file"], encoding="utf-8"))
            body, qn = lesson_body(lesson)
            mins = lesson["lesson"].get("minutes", 15)
            crumbs = " › ".join([f'<a href="/">edu-arena</a>'] + [f'<a href="{u}">{e(t)}</a>' for u, t in it["crumbs"]])
            btns = [f'<a class="btn" href="{it["play"]}">이 레슨 풀어 보기</a>']
            if it["practice"]:
                btns.append(f'<a class="btn ghost" href="{it["practice"]}">연습 문제</a>')
            if it["essay"]:
                btns.append(f'<a class="btn ghost" href="{it["essay"]}">에세이 과제</a>')
            cta = '<div class="cta">' + "".join(btns) + "</div>"
            prev = items[i - 1] if i > 0 and items[i - 1]["group"] == it["group"] else None
            nxt = items[i + 1] if i + 1 < len(items) and items[i + 1]["group"] == it["group"] else None
            nav = ('<div class="nav"><span>' + (f'<a href="/{subj}/learn/{prev["id"]}.html">← {e(prev["title"])}</a>' if prev else "") +
                   '</span><span>' + (f'<a href="/{subj}/learn/{nxt["id"]}.html">{e(nxt["title"])} →</a>' if nxt else "") + "</span></div>")
            page = (f'<p class="crumb">{crumbs}</p><h1>{e(it["title"])}</h1>'
                    f'<p class="meta">{e(it["group"])} · {e(it["chapter"])} · {it["level"]} · 약 {mins}분 · 문제 {qn}개</p>'
                    f'{cta}{body}<p class="meta">문제의 정답과 해설, 힌트는 레슨을 풀면서 확인할 수 있습니다.</p>{cta}{nav}')
            title = f'{it["title"]} - {it["group"]} | {it["sname"]} | edu-arena'
            shell(f"/{subj}/learn/{it['id']}.html", title, describe(lesson), page, f"/{subj}/learn/{it['id']}.html")
            total += 1
        # 과목 레슨 목록
        parts = [f'<p class="crumb"><a href="/">edu-arena</a> › <a href="/{subj}/browse.html">{e(items[0]["sname"])}</a></p>',
                 f'<h1>{e(items[0]["sname"])} 전체 레슨</h1><p class="meta">레슨 {len(items)}개 · 제목을 누르면 레슨 내용을 볼 수 있습니다.</p>',
                 '<div class="hub">']
        for gname, gdesc, chs in groups:
            n = sum(len(ls) for _, ls in chs)
            parts.append(f'<h2>{e(gname)} <span class="cnt">레슨 {n}개</span></h2>' + (f'<p class="cnt">{e(gdesc)}</p>' if gdesc else ""))
            for ctitle, ls in chs:
                parts.append(f'<h3>{e(ctitle)}</h3><ul class="list">' +
                             "".join(f'<li><a href="/{subj}/learn/{x["id"]}.html">{e(x["title"])}</a></li>' for x in ls) + "</ul>")
        parts.append("</div>")
        sname = items[0]["sname"]
        shell(f"/{subj}/learn/index.html", f"{sname} 전체 레슨 목록 | edu-arena",
              f"edu-arena {sname} 과목의 레슨 {len(items)}개 전체 목록입니다. 고교 교과부터 올림피아드 심화까지 레슨 내용을 바로 볼 수 있습니다.",
              "\n".join(parts), f"/{subj}/learn/")
    return total


def build_root_index(data):
    rows = []
    for subj, sname in SUBJECTS:
        items = data[subj][0]
        rows.append(f'<li><a href="/{subj}/learn/"><strong>{e(sname)}</strong></a> <span class="cnt">레슨 {len(items)}개</span></li>')
    for subj, sname in EXTRA:
        rows.append(f'<li><a href="/{subj}/browse.html"><strong>{e(sname)}</strong></a> <span class="cnt">과정 목록</span></li>')
    body = ('<p class="crumb"><a href="/">edu-arena</a></p><h1>전체 레슨 목록</h1>'
            '<p class="meta">과목을 고르면 그 과목의 모든 레슨 제목과 내용을 볼 수 있습니다.</p>'
            f'<ul class="list">{"".join(rows)}</ul>')
    shell("/lessons.html", "전체 레슨 목록 | edu-arena",
          "edu-arena의 모든 과목 레슨 목록. 사회와 역사, 경제와 경영, 언어와 문학, 수학, 과학, 공학, 예체능, 외국어, 코딩.",
          body, "/lessons.html")


def build_sitemaps(data):
    def urlset(urls):
        return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
                "".join(f"  <url><loc>{SITE}{html.escape(u)}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) +
                "</urlset>\n")
    pages = ["/", "/lessons.html", "/about.html", "/contact.html", "/privacy.html", "/terms.html"]
    for subj, _ in SUBJECTS + EXTRA:
        for name in ["browse.html", "guide.html", "placement.html", "essay.html", "olympiad/browse.html"]:
            if os.path.exists(os.path.join(ROOT, subj, name)) and not (name == "essay.html"):
                pages.append(f"/{subj}/{name}")
        if subj in dict(SUBJECTS):
            pages.append(f"/{subj}/learn/")
    files = ["sitemap-pages.xml"]
    with open(os.path.join(ROOT, "sitemap-pages.xml"), "w", encoding="utf-8") as f:
        f.write(urlset(pages))
    for subj, (items, _) in data.items():
        name = f"sitemap-{subj}.xml"
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
            f.write(urlset([f"/{subj}/learn/{x['id']}.html" for x in items]))
        files.append(name)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
                "".join(f"  <sitemap><loc>{SITE}/{n}</loc><lastmod>{TODAY}</lastmod></sitemap>\n" for n in files) +
                "</sitemapindex>\n")
    tools_dirs = sorted({os.path.relpath(os.path.dirname(p), ROOT) for p in glob.glob(os.path.join(ROOT, "*/tools/*"))} | {"tools"})
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\nDisallow: /legacy/\n" +
                "".join(f"Disallow: /{d}/\n" for d in tools_dirs) +
                f"\nSitemap: {SITE}/sitemap.xml\n")
    return len(pages), files


if __name__ == "__main__":
    data = collect()
    n = build_lessons(data)
    build_root_index(data)
    p, files = build_sitemaps(data)
    print(f"정적 레슨 {n}개, 일반 페이지 {p}개, 사이트맵 {len(files)}개")
