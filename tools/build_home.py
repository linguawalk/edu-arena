#!/usr/bin/env python3
"""edu-arena 메인(전체 코스 목록) 생성기.

각 과목의 content/level1/courses.json을 읽어 index.html을 다시 만듭니다.
코스를 추가하거나 이름을 바꾼 뒤 저장소 루트에서 실행하세요:

    python3 tools/build_home.py
"""
import html
import json
import os
import sys as _sys
_sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_parts import FOOT_CSS, FOOT_HTML

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 과목 정의: (폴더, 이름, 묶음, 짧은 설명, [(링크 이름, 주소)])
SUBJECTS = [
    ("socio", "사회와 역사", "hum", "한국사·세계사, 사회와 문화, 지리, 정치와 법, 윤리",
     [("레벨2·3 가이드", "guide.html"), ("심화 · 인문·사회 경시", "olympiad/browse.html")]),
    ("biz", "경제와 경영", "hum", "고교 경제부터 회계, 세무, 마케팅, 무역까지",
     [("레벨2·3 가이드", "guide.html"), ("심화 · 경제 올림피아드", "olympiad/browse.html")]),
    ("lit", "언어와 문학", "hum", "국어, 한자, 영어, 국문학, 세계문학",
     [("레벨2·3 가이드", "guide.html"), ("심화 · 언어학 올림피아드", "olympiad/browse.html")]),
    ("lingua", "외국어", "hum", "영어, 일본어, 중국어, 프랑스어, 독일어, 스페인어 · CEFR A1–C2",
     [("배치고사", "placement.html")]),
    ("math", "수학", "stem", "중학 핵심부터 고등 수학까지",
     [("진입 진단", "placement.html"), ("레벨2·3 가이드", "guide.html"), ("심화 · 수학 올림피아드", "olympiad/browse.html")]),
    ("sci", "과학", "stem", "물리, 화학, 생명과학, 지구과학",
     [("진입 진단", "placement.html"), ("레벨2·3 가이드", "guide.html"), ("심화 · 과학 올림피아드", "olympiad/browse.html")]),
    ("tech", "공학", "stem", "과학 원리를 회로·기계·공정·컴퓨터에 쓰는 법",
     [("레벨2·3 가이드", "guide.html")]),
    ("code", "코딩", "stem", "컴퓨팅 사고부터 언어별 과정, 실습, 자격증까지",
     [("전체 코스", "courses.html"), ("심화 · 정보 올림피아드", "olympiad/browse.html")]),
    ("arts", "예체능", "arts", "음악 이론과 감상, 음악사, 미술, 미술사, 스포츠와 건강",
     [("레벨2·3 가이드", "guide.html")]),
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

# 외국어도 courses.json 대신 언어 단위로 보여 줍니다.
LINGUA_COURSES = [
    ("영어", "English", "en"), ("일본어", "日本語", "ja"), ("중국어", "中文", "zh"), ("프랑스어", "Français", "fr"),
    ("독일어", "Deutsch", "de"), ("스페인어", "Español", "es"),
]

# 카드에 보이는 영어 표기 (폴더 이름은 그대로)
TAGS = {"socio": "social studies", "biz": "biz", "lit": "literature", "math": "mathematics",
        "sci": "science", "tech": "engineering", "code": "code", "arts": "arts & PE", "lingua": "languages"}

GROUPS = [("hum", "인문사회"), ("stem", "수학·과학"), ("arts", "예체능")]

e = html.escape


def load_courses(folder):
    if folder == "code":
        return [{"title": t, "description": d, "href": f"code/{h}", "available": True} for t, d, h in CODE_COURSES]
    if folder == "lingua":
        return [{"title": t, "description": d, "href": f"lingua/browse.html?lang={k}", "available": True} for t, d, k in LINGUA_COURSES]
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
    blocks = []
    for gid, gname in GROUPS:
        cards = []
        for folder, name, group, desc, links in [x for x in SUBJECTS if x[2] == gid]:
            n = len(load_courses(folder))
            total += n
            cards.append(
                f'<a class="card {group}" href="{folder}/browse.html"><span class="tag">{TAGS[folder]}</span>'
                f'<h3>{e(name)}</h3><p>{e(desc)}</p><span class="go">{n}개 코스 →</span></a>')
        blocks.append(f'<section class="group" aria-labelledby="g-{gid}"><div class="group-head">'
                      f'<h2 id="g-{gid}">{gname}</h2></div><div class="grid">{"".join(cards)}</div></section>')

    page = TEMPLATE.replace("{{HERO}}", hero).replace("{{BLOCKS}}", "\n".join(blocks)).replace("{{TOTAL}}", str(total)).replace("{{FOOT_CSS}}", FOOT_CSS).replace("{{FOOT_HTML}}", FOOT_HTML)
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)
    print(f"index.html: {len(SUBJECTS)}과목, {total}개 코스")


TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>edu-arena · 풀면서 배우는 모든 과목</title>
<link rel="canonical" href="https://edu-arena.org/">
<meta name="description" content="읽기 전에 먼저 풀어 보는 15분 레슨. 사회와 역사, 경제와 경영, 언어와 문학, 외국어, 수학, 과학, 공학, 코딩, 예체능까지 {{TOTAL}}개 코스를 한곳에서. 과목별 올림피아드 심화 과정 포함.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{--paper:#FAFBFD;--ink:#172033;--ink-soft:#4A5670;--grid:#DCE4F0;--grid-strong:#B9C7DD;--blue:#1D3FA8;--blue-soft:#E7ECFA;--marker:#FFD84D;
  --hum:#7A4B1E;--hum-soft:#F6ECE1;--stem:#1D3FA8;--stem-soft:#E7ECFA;--arts:#1E6B5C;--arts-soft:#E2F2EE;
  --font:"IBM Plex Sans KR","Apple SD Gothic Neo","Malgun Gothic",sans-serif}
*{box-sizing:border-box}
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
.group{border-top:2px solid var(--ink);padding:26px 0 40px}
.group-head{margin-bottom:18px}
.group-head h2{font-size:22px;margin:0}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:14px}
.card{display:flex;flex-direction:column;gap:8px;text-decoration:none;color:inherit;background:#fff;border:1px solid var(--grid);border-radius:14px;padding:20px 20px 18px;transition:border-color .15s,transform .15s}
.card:hover{border-color:var(--c);transform:translateY(-2px)}
.card .tag{align-self:flex-start;font-size:13px;font-weight:700;color:var(--c);background:var(--cs);border-radius:6px;padding:4px 8px}
.card h3{font-size:20px;margin:2px 0 0;letter-spacing:-.02em}
.card p{margin:0;font-size:15px;line-height:1.65;color:var(--ink-soft)}
.card .go{margin-top:auto;padding-top:6px;font-size:15px;font-weight:700;color:var(--c)}
.hum{--c:var(--hum);--cs:var(--hum-soft)}
.stem{--c:var(--stem);--cs:var(--stem-soft)}
.arts{--c:var(--arts);--cs:var(--arts-soft)}
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
<header><div class="wrap"><a class="logo" href="./"><span>edu-arena</span></a><nav data-auth><a href="#subjects">과목</a><a href="#levels">레벨</a><a href="lessons.html">레슨 목록</a></nav></div></header>
<main class="wrap">
{{HERO}}

  <div id="subjects"></div>
{{BLOCKS}}

  <section class="levels" id="levels" aria-label="레벨 구성">
    <div><h2>레벨1 · 고교 수준</h2><p>설명과 문제가 번갈아 나오는 레슨으로 배웁니다. 기초가 불안하면 진입 진단으로 시작 위치를 찾으세요.</p></div>
    <div><h2>레벨2 · 전문대 수준</h2><p>응용과 해외 비교를 다루는 독학 가이드로 스스로 공부합니다. 과목마다 "레벨2·3 가이드"에서 시작하세요.</p></div>
    <div><h2>레벨3 · 대학 수준</h2><p>전공 수준의 심화 주제를 트랙별 독학 가이드로 안내합니다. 과목마다 올림피아드·경시를 준비하는 심화 과정도 있습니다.</p></div>
  </section>

  <section class="family" aria-label="Arena 패밀리">
    <strong>Arena 패밀리</strong>
    <a href="https://mind-arena.org/">mind-arena</a><span>퍼즐과 보드게임</span>
  </section>
</main>
<style>{{FOOT_CSS}}</style>
{{FOOT_HTML}}
<script src="/assets/site.js" defer></script>
</body>
</html>
"""

if __name__ == "__main__":
    build()
