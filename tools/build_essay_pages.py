#!/usr/bin/env python3
"""과목별 에세이 화면(essay.html)과 코스 목록의 에세이 줄을 만듭니다.

    python3 tools/build_essay_pages.py

- tools/essay_tpl.html → <과목>/essay.html (과목 이름과 저장 키만 바꿈)
- <과목>/browse.html의 레슨 줄 아래에 에세이 줄을 넣는 코드를 한 번만 끼워 넣음
  (chapter.json의 레슨에 "essay" 항목이 있을 때만 줄이 보임)
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUBJECTS = {
    "socio": ("사회와 역사", "socio-arena"),
    "biz": ("경제와 경영", "biz-arena"),
    "lit": ("언어와 문학", "lit-arena"),
    "sci": ("과학", "sci-arena"),
    "arts": ("예체능", "arts"),
    "tech": ("공학", "tech-arena"),
    "math": ("수학", "math-arena"),
}

MARK = "/*essay-row*/"
LESSON_ROW_END = "<span class=\"meta\">${p ? `${p.first}/${p.total}` : `${l.questions}문항`}</span></a></li>`; });"
ESSAY_ROW = (MARK + " const essayRow = (l, n) => { if (!l.essay) return \"\"; const id = `${l.id}-essay`, p = progress[id];\n"
             "        return `<li><a class=\"essay ${p && p.first >= p.total ? \"done\" : \"\"}\" href=\"essay.html?c=${COURSE}&ch=${n}&l=${pad(l.no)}\">\n"
             "          <span class=\"state\" aria-hidden=\"true\"></span><span class=\"t\">에세이 · ${esc(l.title)}</span>\n"
             "          <span class=\"meta\">${p ? `${p.first}/${p.total}편` : `${l.essay.count}편`}</span></a></li>`; };\n")
PRAC_ROW_END = "<span class=\"meta\">${p ? `${p.first}/${p.total}` : `${l.questions}문항`}</span></a>${prac}</li>`; });"
ESSAY_CSS = ".items .essay{padding-left:36px;font-size:16px;color:var(--ink-soft)}.items .essay .state{width:14px;height:14px;border-radius:3px}"


def build_pages():
    with open(os.path.join(ROOT, "tools", "essay_tpl.html"), encoding="utf-8") as f:
        tpl = f.read()
    for folder, (name, store) in SUBJECTS.items():
        with open(os.path.join(ROOT, folder, "essay.html"), "w", encoding="utf-8") as f:
            f.write(tpl.replace("{{SUBJ}}", name).replace("{{STORE}}", store))


def patch_browse(folder):
    path = os.path.join(ROOT, folder, "browse.html")
    with open(path, encoding="utf-8") as f:
        s = f.read()
    if MARK in s:
        return False
    s = s.replace("const rows = ch.lessons.map(l => {", ESSAY_ROW + "      const rows = ch.lessons.flatMap(l => {", 1)
    if PRAC_ROW_END in s:  # 수학: 레슨 줄 끝에 '연습' 링크가 붙는 모양
        s = s.replace(PRAC_ROW_END, PRAC_ROW_END[:-len("`; });")] + "`, essayRow(l, n)].filter(Boolean); });", 1)
        s = s.replace("return `<li${prac ?", "return [`<li${prac ?", 1)
        s = s.replace("</style>", ESSAY_CSS + "\n</style>", 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(s)
        return True
    assert LESSON_ROW_END in s, f"{folder}/browse.html: 레슨 줄 코드를 찾지 못함"
    s = s.replace(LESSON_ROW_END,
                  "<span class=\"meta\">${p ? `${p.first}/${p.total}` : `${l.questions}문항`}</span></a></li>`, essayRow(l, n)].filter(Boolean); });", 1)
    s = s.replace("return `<li><a class=\"${p ? \"done\" : \"\"}\" href=\"player.html?c=${COURSE}&ch=${n}&l=${pad(l.no)}\">",
                  "return [`<li><a class=\"${p ? \"done\" : \"\"}\" href=\"player.html?c=${COURSE}&ch=${n}&l=${pad(l.no)}\">", 1)
    s = s.replace("</style>", ESSAY_CSS + "\n</style>", 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)
    return True


if __name__ == "__main__":
    build_pages()
    for folder in SUBJECTS:
        try:
            print(folder, "browse 수정" if patch_browse(folder) else "browse 이미 수정됨")
        except AssertionError as e:
            print("건너뜀:", e)
    print("essay.html:", ", ".join(SUBJECTS))
