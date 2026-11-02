#!/usr/bin/env python3
"""edu-arena 메인(전체 코스 목록) 생성기.

각 과목의 content/level1/courses.json을 읽어 index.html을 다시 만듭니다.
코스를 추가하거나 이름을 바꾼 뒤 저장소 루트에서 실행하세요:

    python3 tools/build_home.py
"""
import html
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 과목 정의: (폴더, 이름, 묶음, 짧은 설명, [(링크 이름, 주소)])
SUBJECTS = [
    ("socio", "사회와 역사", "hum", "한국사·세계사, 사회와 문화, 지리, 정치와 법, 윤리",
     [("레벨2·3 가이드", "guide.html"), ("심화 · 인문·사회 경시", "olympiad/browse.html")]),
    ("biz", "경제와 경영", "hum", "고교 경제부터 회계, 세무, 마케팅, 무역까지",
     [("레벨2·3 가이드", "guide.html"), ("심화 · 경제 올림피아드", "olympiad/browse.html")]),
    ("lit", "국어와 문학", "hum", "국어, 한자, 영어, 국문학, 세계문학",
     [("레벨2·3 가이드", "guide.html"), ("심화 · 언어학 올림피아드", "olympiad/browse.html")]),
    ("math", "수학", "stem", "중학 핵심부터 고등 수학까지",
     [("진입 진단", "placement.html"), ("레벨2·3 가이드", "guide.html"), ("심화 · 수학 올림피아드", "olympiad/browse.html")]),
    ("sci", "과학", "stem", "물리, 화학, 생명과학, 지구과학",
     [("진입 진단", "placement.html"), ("레벨2·3 가이드", "guide.html"), ("심화 · 과학 올림피아드", "olympiad/browse.html")]),
    ("tech", "공학", "stem", "과학 원리를 회로·기계·공정·컴퓨터에 쓰는 법",
     [("레벨2·3 가이드", "guide.html")]),
    ("code", "코딩", "stem", "컴퓨팅 사고부터 언어별 과정, 실습, 자격증까지",
     [("전체 코스", "courses.html"), ("심화 · 정보 올림피아드", "olympiad/browse.html")]),
]

# 코딩은 courses.json 대신 트랙 단위로 보여 줍니다.
CODE_COURSES = [
    ("기초", "컴퓨터적 사고와 C 온보딩", "browse.html?type=foundation&stage=stage0_computer_thinking"),
    ("시스템·저수준", "C → C++ → Rust", "courses.html#track-a"),
    ("객체지향·엔터프라이즈", "VB → C# → Java", "courses.html#track-b"),
    ("스크립트·실무", "Python → JavaScript → PHP", "courses.html#track-c"),
    ("레거시·역사", "BASIC · Pascal · FORTRAN · COBOL", "courses.html#track-d"),
    ("개념 모듈", "자료구조·알고리즘, 통계, DB 이론, Linux, Excel/Access", "courses.html#modules"),
    ("실습", "직접 코드를 써서 실행 결과로 채점", "courses.html#practice"),
    ("자격증", "Oracle·Microsoft·AWS·Google·Cisco·LPI", "courses.html#certs"),
]

GROUPS = [("hum", "인문사회"), ("stem", "수학·과학")]

e = html.escape


def load_courses(folder):
    if folder == "code":
        return [{"title": t, "description": d, "href": f"code/{h}", "available": True} for t, d, h in CODE_COURSES]
    path = os.path.join(ROOT, folder, "content", "level1", "courses.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return [{"title": c["title"], "description": c.get("description", ""),
             "href": f"{folder}/browse.html?c={c['id']}", "available": c.get("available", True)}
            for c in data["courses"]]


def card(c, group):
    if c["available"]:
        return (f'<a class="course {group}" href="{e(c["href"])}"><h4>{e(c["title"])}</h4>'
                f'<p>{e(c["description"])}</p></a>')
    return (f'<div class="course {group} off"><h4>{e(c["title"])}</h4>'
            f'<p>{e(c["description"])}</p><span class="soon">준비 중</span></div>')


def build():
    with open(os.path.join(ROOT, "tools", "home_hero.html"), encoding="utf-8") as f:
        hero = f.read()

    total = 0
    chips = ['<a class="chip" href="./" data-s="all" aria-current="true">전체</a>']
    blocks = []
    for gid, gname in GROUPS:
        subs = [s for s in SUBJECTS if s[2] == gid]
        parts = [f'<div class="gtitle">{gname}</div>']
        for folder, name, group, desc, links in subs:
            courses = load_courses(folder)
            total += len(courses)
            chips.append(f'<a class="chip {group}" href="?s={folder}" data-s="{folder}">{e(name)}</a>')
            link_html = "".join(f'<a href="{folder}/{h}">{e(t)}</a>' for t, h in links)
            parts.append(
                f'<section class="subject" id="{folder}" data-s="{folder}" aria-labelledby="h-{folder}">'
                f'<div class="shead"><h3 id="h-{folder}">{e(name)}</h3><span class="cnt">{len(courses)}개 코스</span>'
                f'<p>{e(desc)}</p><nav class="slinks" aria-label="{e(name)} 바로가기">{link_html}</nav></div>'
                f'<div class="courses">{"".join(card(c, group) for c in courses)}</div></section>')
        blocks.append("\n".join(parts))

    page = TEMPLATE.replace("{{HERO}}", hero) \
        .replace("{{CHIPS}}", "".join(chips)) \
        .replace("{{BLOCKS}}", "\n".join(blocks)) \
        .replace("{{TOTAL}}", str(total))
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)
    print(f"index.html: {len(SUBJECTS)}과목, {total}개 코스")


TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>edu-arena · 풀면서 배우는 모든 과목</title>
<meta name="description" content="읽기 전에 먼저 풀어 보는 15분 레슨. 사회와 역사, 경제와 경영, 국어와 문학, 수학, 과학, 공학, 코딩까지 {{TOTAL}}개 코스를 한곳에서. 과목별 올림피아드 심화 과정 포함.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{--paper:#FAFBFD;--ink:#172033;--ink-soft:#4A5670;--grid:#DCE4F0;--grid-strong:#B9C7DD;--blue:#1D3FA8;--blue-soft:#E7ECFA;--marker:#FFD84D;
  --hum:#7A4B1E;--hum-soft:#F6ECE1;--stem:#1D3FA8;--stem-soft:#E7ECFA;
  --font:"IBM Plex Sans KR","Apple SD Gothic Neo","Malgun Gothic",sans-serif}
*{box-sizing:border-box}
html{scroll-padding-top:72px}
html,body{margin:0;word-break:keep-all;overflow-wrap:anywhere;background:var(--paper);color:var(--ink);font-family:var(--font)}
body{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
:focus-visible{outline:3px solid var(--blue);outline-offset:3px}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px}
header .wrap{display:flex;align-items:center;justify-content:space-between;height:64px}
.logo{font-weight:700;font-size:18px;text-decoration:none;color:inherit}
.logo span{background:linear-gradient(transparent 58%,var(--marker) 58%)}
header nav a{font-size:16px;color:var(--ink-soft);text-decoration:none;padding:8px 10px;border-radius:8px}
header nav a:hover{background:var(--blue-soft);color:var(--blue)}
.hero{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center;padding:56px 0 64px}
.plot{background:#fff;border:1px solid var(--grid);border-radius:14px;padding:14px;margin:0}
.plot svg{display:block;width:100%;height:auto}
.plot figcaption{font-size:15px;color:var(--ink-soft);padding:10px 6px 2px;line-height:1.5}
.step{opacity:0;animation:pop .35s ease-out forwards}.s1{animation-delay:.2s}.s2{animation-delay:.5s}.s3{animation-delay:.8s}.s4{animation-delay:1.1s}
#route{stroke-dasharray:520;stroke-dashoffset:520;animation:draw 1.4s 1.3s ease-out forwards}#me{opacity:0;animation:pop .3s 2.6s ease-out forwards}
@keyframes pop{to{opacity:1}}@keyframes draw{to{stroke-dashoffset:0}}
@media (prefers-reduced-motion:reduce){.step,#me{animation:none;opacity:1}#route{animation:none;stroke-dashoffset:0}}
h1{font-size:clamp(36px,5.5vw,60px);line-height:1.15;letter-spacing:-.035em;margin:0 0 20px;font-weight:700}
.lede{font-size:19px;line-height:1.75;color:var(--ink-soft);margin:0}
.catalog{border-top:2px solid var(--ink);padding:26px 0 24px}
.catalog>h2{font-size:24px;margin:0 0 6px;letter-spacing:-.02em}
.catalog>p{margin:0 0 18px;color:var(--ink-soft);font-size:16px}
.chips{position:sticky;top:0;z-index:5;background:var(--paper);display:flex;gap:8px;overflow-x:auto;padding:10px 0 12px;margin:0 0 6px;border-bottom:1px solid var(--grid);scrollbar-width:none}
.chips::-webkit-scrollbar{display:none}
.chip{flex:none;font-size:15px;text-decoration:none;color:var(--ink);padding:8px 14px;border-radius:999px;border:1px solid var(--grid-strong);background:#fff;white-space:nowrap}
.chip:hover{border-color:var(--blue)}
.chip[aria-current]{background:var(--ink);border-color:var(--ink);color:#fff;font-weight:700}
.gtitle{font-size:13px;font-weight:700;letter-spacing:.06em;color:var(--ink-soft);margin:26px 0 0}
.subject{padding:18px 0 22px;border-bottom:1px solid var(--grid)}
.shead{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 12px;margin-bottom:14px}
.shead h3{font-size:22px;margin:0;letter-spacing:-.02em}
.shead .cnt{font-size:14px;color:var(--ink-soft)}
.shead p{flex-basis:100%;margin:2px 0 0;font-size:15px;color:var(--ink-soft)}
.slinks{flex-basis:100%;display:flex;flex-wrap:wrap;gap:6px 16px;margin-top:6px}
.slinks a{font-size:15px;font-weight:700;color:var(--blue);text-decoration:none}
.slinks a:hover{text-decoration:underline}
.slinks a::after{content:" →"}
.courses{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px}
.course{display:flex;flex-direction:column;gap:6px;text-decoration:none;color:inherit;background:#fff;border:1px solid var(--grid);border-left:4px solid var(--c);border-radius:10px;padding:14px 16px;transition:border-color .15s,box-shadow .15s}
a.course:hover{border-color:var(--c);box-shadow:0 2px 10px rgba(23,32,51,.06)}
.course h4{font-size:17px;margin:0;letter-spacing:-.01em}
.course p{margin:0;font-size:14px;line-height:1.6;color:var(--ink-soft);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.course.off{opacity:.55}
.course .soon{font-size:13px;color:var(--ink-soft)}
.hum{--c:var(--hum)}
.stem{--c:var(--stem)}
.levels{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;border-top:2px solid var(--ink);padding:26px 0 40px;margin-top:24px}
.levels h2{font-size:18px;margin:0 0 6px}
.levels p{margin:0;font-size:15px;line-height:1.7;color:var(--ink-soft)}
.family{border-top:1px solid var(--grid);padding:24px 0 56px;display:flex;flex-wrap:wrap;gap:10px 22px;align-items:center;font-size:15px;color:var(--ink-soft)}
.family strong{color:var(--ink)}
.family a{color:var(--blue);font-weight:700;text-decoration:none}
.family a:hover{text-decoration:underline}
[hidden]{display:none!important}
@media (max-width:820px){.hero{grid-template-columns:1fr;padding-top:28px}.levels{grid-template-columns:1fr;gap:18px}}
@media (max-width:520px){.courses{grid-template-columns:1fr}}
</style>
</head>
<body>
<header><div class="wrap"><a class="logo" href="./"><span>edu-arena</span></a><nav><a href="#courses">코스</a><a href="#levels">레벨</a></nav></div></header>
<main class="wrap">
{{HERO}}

  <section class="catalog" id="courses" aria-labelledby="courses-h">
    <h2 id="courses-h">전체 코스</h2>
    <p>{{TOTAL}}개 코스를 과목별로 모았습니다. 코스를 고르면 바로 첫 챕터부터 시작할 수 있습니다.</p>
    <nav class="chips" aria-label="과목 선택">{{CHIPS}}</nav>
{{BLOCKS}}
  </section>

  <section class="levels" id="levels" aria-label="레벨 구성">
    <div><h2>레벨1 · 고교 수준</h2><p>위의 코스들입니다. 설명과 문제가 번갈아 나오는 레슨으로 배우고, 기초가 불안하면 진입 진단으로 시작 위치를 찾으세요.</p></div>
    <div><h2>레벨2 · 전문대 수준</h2><p>응용과 해외 비교를 다루는 독학 가이드로 스스로 공부합니다. 과목마다 "레벨2·3 가이드"에서 시작하세요.</p></div>
    <div><h2>레벨3 · 대학 수준</h2><p>전공 수준의 심화 주제를 트랙별 독학 가이드로 안내합니다. 과목마다 올림피아드·경시를 준비하는 심화 과정도 있습니다.</p></div>
  </section>

  <section class="family" aria-label="Arena 패밀리">
    <strong>Arena 패밀리</strong>
    <a href="https://lingua-arena.org/">lingua-arena</a><span>외국어</span>
    <a href="https://mind-arena.org/">mind-arena</a><span>퍼즐과 보드게임</span>
  </section>
</main>
<script>
(function () {
  var chips = document.querySelectorAll(".chip"), subs = document.querySelectorAll(".subject"), titles = document.querySelectorAll(".gtitle");
  function show(s, push) {
    if (!document.getElementById(s)) s = "all";
    chips.forEach(function (c) { if (c.dataset.s === s) c.setAttribute("aria-current", "true"); else c.removeAttribute("aria-current"); });
    subs.forEach(function (x) { x.hidden = s !== "all" && x.dataset.s !== s; });
    titles.forEach(function (t) { t.hidden = s !== "all"; });
    if (push) history.replaceState(null, "", s === "all" ? location.pathname : "?s=" + s);
  }
  chips.forEach(function (c) {
    c.addEventListener("click", function (ev) {
      ev.preventDefault(); show(c.dataset.s, true);
      document.getElementById("courses").scrollIntoView({ behavior: "smooth" });
    });
  });
  var q = new URLSearchParams(location.search).get("s");
  if (q) { show(q, false); document.getElementById("courses").scrollIntoView(); }
})();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    build()
