"""레슨별 에세이(논술) 작성 도구. 과목 폴더의 build_essay_*.py에서 씁니다.

    from essay_kit import *
    write_essays("sci", "c0", 1, 1, [essay(...), essay(...), essay(...)])

- <과목>/content/level1/<코스>/chNN/eNN.json 을 쓰고
- 같은 폴더 chapter.json의 해당 레슨에 "essay": {"file", "count"}를 기록합니다.
- 예시 답안이 스스로 만든 자동 점검(분량·문단·필수 내용)을 모두 통과하는지 검사합니다.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 자기 평가 기준(공통). 과목에 따라 essay(self_=...)로 바꿀 수 있습니다.
SELF_DEFAULT = [
    ("주장", "논제에 대한 내 답이 첫 문단에 분명하게 드러나는가"),
    ("근거", "레슨에서 배운 개념과 제시문을 정확하게 써서 주장을 뒷받침했는가"),
    ("구성", "문단마다 하는 일이 분명하고 순서가 자연스러운가"),
    ("표현", "개념어를 정확히 쓰고 문장이 짧고 분명한가"),
]


def src(label, text=(), title=None, table=None):
    d = {"label": label, "text": list(text)}
    if title: d["title"] = title
    if table: d["table"] = table
    return d


# 활용하면 모양이 바뀌는 짧은 어간: 학생 답안의 '큽니다·큰'도 잡도록 자동으로 넓힘
STEM_FORMS = {"크": ["큽", "큰", "커"], "늘": ["늡", "는다"], "바뀌": ["바뀝", "바뀐", "바꿔"], "되": ["됩", "된", "돼"],
              "내보내": ["내보냅", "내보낸"], "변하": ["변합", "변한", "변해"], "하": ["합", "한", "해"]}


def _widen(g):
    out = list(g)
    for w in g:
        for f in STEM_FORMS.get(w, []):
            if f not in out: out.append(f)
    return out


def chk(label, *groups, need=None):
    """groups: 각각 '이 가운데 한 단어라도 있으면 통과'인 단어 묶음."""
    d = {"label": label, "groups": [_widen(list(g)) for g in groups]}
    if need is not None: d["need"] = need
    return d


def essay(prompt, conditions, checks, outline, answer, sources=(), length=(300, 600), paragraphs=3, self_=None):
    return {"prompt": prompt, "conditions": list(conditions), "sources": list(sources),
            "length": {"min": length[0], "max": length[1]}, "paragraphs": paragraphs,
            "checks": checks, "self": [{"label": a, "desc": b} for a, b in (self_ or SELF_DEFAULT)],
            "model": {"outline": list(outline), "answer": list(answer)}}


def _auto(e, text):
    t = re.sub(r"\s+", " ", text)
    fails = []
    n = len(text.strip())
    if not (e["length"]["min"] <= n <= e["length"]["max"]): fails.append(f"분량 {n}자")
    paras = [p for p in text.split("\n") if len(p.strip()) >= 20]
    if e["paragraphs"] and len(paras) < e["paragraphs"]: fails.append(f"문단 {len(paras)}개")
    for c in e["checks"]:
        hit = sum(1 for g in c["groups"] if any(w in t for w in g))
        if hit < c.get("need", len(c["groups"])): fails.append("점검: " + c["label"])
    return fails


def write_essays(subject, course, ch, lesson, essays):
    base = os.path.join(ROOT, subject, "content", "level1", course, f"ch{ch:02d}")
    with open(os.path.join(base, "chapter.json"), encoding="utf-8") as f:
        chap = json.load(f)
    les = next(l for l in chap["lessons"] if l["no"] == lesson)
    with open(os.path.join(ROOT, subject, "content", "level1", course, "course.json"), encoding="utf-8") as f:
        ctitle = json.load(f)["course"]["title"]
    assert len(essays) == 3, f"{les['id']}: 에세이는 3편"
    lid = les["id"]
    out = {"schema_version": "1.0", "type": "essay_set", "id": f"{lid}-essay", "lesson": lid,
           "course_title": ctitle, "chapter_title": chap["chapter"]["title"], "title": les["title"], "essays": []}
    for k, e in enumerate(essays, 1):
        e = dict(e, id=f"{lid}-e{k}")
        assert len(e["prompt"]) >= 20 and e["conditions"] and len(e["checks"]) >= 2, f"{e['id']}: 논제·조건·점검 부족"
        assert len(e["self"]) >= 3 and len(e["model"]["outline"]) >= 2, f"{e['id']}: 자기평가·개요 부족"
        fails = _auto(e, "\n".join(e["model"]["answer"]))
        assert not fails, f"{e['id']}: 예시 답안이 자동 점검을 통과하지 못함 → {fails}"
        out["essays"].append(e)
    fname = f"e{lesson:02d}.json"
    with open(os.path.join(base, fname), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    les["essay"] = {"file": fname, "count": len(essays)}
    with open(os.path.join(base, "chapter.json"), "w", encoding="utf-8") as f:
        json.dump(chap, f, ensure_ascii=False, indent=2)
    return f"{lid}: 에세이 {len(essays)}편"
