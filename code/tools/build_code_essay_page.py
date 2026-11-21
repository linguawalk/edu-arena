#!/usr/bin/env python3
"""tech/essay.html을 바탕으로 코딩 에세이 화면(code/essay.html)을 만든다.  python3 code/tools/build_code_essay_page.py"""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
s = open(os.path.join(ROOT, "tech", "essay.html"), encoding="utf-8").read()
def rep(old, new):
    global s
    assert old in s, old[:70]
    s = s.replace(old, new)
rep("<title>에세이 · 공학 · edu-arena</title>", "<title>에세이 · 코딩 · edu-arena</title>")
rep("이 파일은 tools/essay_tpl.html에서 만듭니다. 직접 고치지 말고 python3 tools/build_essay_pages.py를 실행하세요.",
    "이 파일은 tech/essay.html에서 python3 code/tools/build_code_essay_page.py로 만듭니다. 직접 고치지 마세요.")
rep('const STORE = "tech-arena";', 'const STORE = "code-arena";')
rep('const COURSE = P.get("c") || "c0", CH = (P.get("ch") || "01").padStart(2, "0"), LES = (P.get("l") || "01").padStart(2, "0");',
    'const SET = (P.get("set") || "").replace(/[^a-z0-9-]/g, "");')
rep('document.getElementById("backCourse").href = `browse.html?c=${COURSE}#ch${CH}`;', 'document.getElementById("backCourse").href = "browse.html?type=essay";')
rep('<a class="ea-subj" href="browse.html">공학</a>', '<a class="ea-subj" href="browse.html">코딩</a>')
rep('id="backCourse">레벨1 코스</a>', 'id="backCourse">에세이 목록</a>')
rep('<a href="browse.html?c=${COURSE}#ch${CH}">${esc(DATA.course_title)}</a> · ${esc(DATA.chapter_title)}', '<a href="browse.html?type=essay">${esc(DATA.course_title)} 에세이</a> · ${esc(DATA.chapter_title)}')
rep("에세이 ${idx + 1} · 공학 · edu-arena", "에세이 ${idx + 1} · 코딩 · edu-arena")
rep('<a class="btn" href="browse.html?c=${COURSE}#ch${CH}">코스 목록으로</a>', '<a class="btn" href="browse.html?type=essay">에세이 목록으로</a>')
rep("레슨 내용을 바탕으로 짧은 논술을 씁니다.", "코딩 개념을 바탕으로 짧은 논술을 씁니다.")
rep("fetch(`content/level1/${COURSE}/ch${CH}/e${LES}.json`).then(r => { if (!r.ok) throw new Error(\"e\" + LES + \".json\"); return r.json(); })",
    "fetch(`essay/${SET}.json`).then(r => { if (!r.ok) throw new Error(SET + \".json\"); return r.json(); })")
open(os.path.join(ROOT, "code", "essay.html"), "w", encoding="utf-8").write(s)
print("code/essay.html", len(s))
