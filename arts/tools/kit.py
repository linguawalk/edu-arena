"""예체능 레슨 JSON 작성 도구.

화면(screen)과 문항을 짧게 쓰고, 레슨·복습·챕터 파일을 같은 형식으로 저장합니다.
다른 과목(math, lit 등)의 레슨 파일과 같은 스키마를 씁니다.
"""
import json
import math
import os

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content", "level1")


# ---------- 화면 ----------
def explain(id, stage, title, body, figure=None):
    s = {"type": "explain", "id": id, "stage": stage, "title": title, "body": body}
    if figure: s["figure"] = figure
    return s


def example(id, stage, problem, steps, answer, title="예제"):
    return {"type": "example", "id": id, "stage": stage, "title": title, "problem": problem, "steps": steps, "answer": answer}


def blank(id, stage, prompt, answers, explanation, hint=None, figure=None):
    """answers: 빈칸마다 허용 답 목록. 빈칸이 하나면 ["답", "다른 표기"]처럼 줘도 됩니다."""
    if answers and isinstance(answers[0], str): answers = [answers]
    q = {"type": "question", "id": id, "stage": stage, "qtype": "fill_blank", "prompt": prompt,
         "blanks": [{"id": k + 1, "answers": a} for k, a in enumerate(answers)], "hint": hint, "explanation": explanation}
    if figure: q["figure"] = figure
    assert prompt.count("{{") == len(answers), (id, prompt)
    return q


def numeric(id, stage, prompt, answer, explanation, hint=None, fmt="integer", tol=0, figure=None):
    q = {"type": "question", "id": id, "stage": stage, "qtype": "numeric", "prompt": prompt, "answer": str(answer),
         "answer_format": fmt, "tolerance": tol, "hint": hint, "explanation": explanation}
    if figure: q["figure"] = figure
    return q


def ordering(id, stage, prompt, correct, explanation, hint=None, shuffle=None):
    """correct: 올바른 순서의 문장 목록. shuffle: 화면에 보일 순서(인덱스)."""
    ids = "abcdefgh"
    items = [{"id": ids[k], "text": t} for k, t in enumerate(correct)]
    order = shuffle or list(range(len(correct)))[::-1]
    assert sorted(order) == list(range(len(correct))) and order != list(range(len(correct))), id
    return {"type": "question", "id": id, "stage": stage, "qtype": "ordering", "prompt": prompt,
            "items": [items[k] for k in order], "answer_order": [ids[k] for k in range(len(correct))],
            "hint": hint, "explanation": explanation}


def written(id, stage, prompt, groups, model, hint=None, need=None):
    return {"type": "question", "id": id, "stage": stage, "qtype": "written", "prompt": prompt, "hint": hint,
            "rubric": {"visibility": "hidden", "keyword_groups": groups, "min_groups_matched": need or max(2, len(groups) - 1)},
            "model_answer": model}


# ---------- 그림 (geo 위젯, 정적) ----------
def fig(alt, elements, maxh=220):
    return {"widget": "geo", "static": True, "config": {"alt": alt, "maxh": maxh, "elements": elements}}


def seg(a, b, hl=False, dash=False):
    e = {"t": "seg", "a": list(a), "b": list(b)}
    if hl: e["hl"] = True
    if dash: e["dash"] = True
    return e


def text(p, s, hl=False):
    e = {"t": "text", "p": list(p), "s": s}
    if hl: e["hl"] = True
    return e


def rect(x, y, w, h, hl=False):
    e = {"t": "poly", "pts": [[x, y], [x + w, y], [x + w, y + h], [x, y + h]]}
    if hl: e["hl"] = True
    return e


def pt(p, label=None, pos=None):
    e = {"t": "pt", "p": list(p)}
    if label: e["label"] = label
    if pos: e["pos"] = pos
    return e


def wave(x0, x1, y, amp, cycles, hl=False, n=None):
    """y를 중심으로 진폭 amp, cycles번 진동하는 사인파를 선분으로 그립니다."""
    n = n or int(24 * cycles)
    pts = [(x0 + (x1 - x0) * k / n, y + amp * math.sin(2 * math.pi * cycles * k / n)) for k in range(n + 1)]
    return [seg([round(a[0], 3), round(a[1], 3)], [round(b[0], 3), round(b[1], 3)], hl=hl) for a, b in zip(pts, pts[1:])]


# ---------- 파일 저장 ----------
def _meta(course, chapter):
    return {"course": {"id": course["id"], "title": course["title"]},
            "chapter": {"id": f'{course["id"]}-ch{chapter["no"]:02d}', "no": chapter["no"], "title": chapter["title"]}}


def _check(screens):
    seen = set()
    for s in screens:
        assert s["id"] not in seen, f"중복 id {s['id']}"
        seen.add(s["id"])
        if s["type"] == "question":
            assert s.get("explanation") or s["qtype"] == "written", f"해설 없음 {s['id']}"


def save_chapter(course, chapter, lessons, review, domain):
    """lessons: [(제목, screens)], review: [문항(source_lesson 포함)]"""
    base = os.path.join(ROOT, course["id"], f'ch{chapter["no"]:02d}')
    os.makedirs(base, exist_ok=True)
    meta = _meta(course, chapter)
    ch_id = meta["chapter"]["id"]
    entries = []
    for k, (title, screens) in enumerate(lessons, 1):
        _check(screens)
        lid = f"{ch_id}-l{k:02d}"
        nq = sum(s["type"] == "question" for s in screens)
        doc = {"schema_version": "1.0", "site": "edu-arena", "level": 1, **meta,
               "lesson": {"id": lid, "no": k, "title": title, "minutes": 15},
               "tags": {"domain": domain, "region": "KR", "curriculum": "2022-high"}, "screens": screens}
        json.dump(doc, open(os.path.join(base, f"l{k:02d}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        entries.append({"no": k, "id": lid, "title": title, "file": f"l{k:02d}.json", "questions": nq, "screens": len(screens)})
    _check(review)
    for q in review: q["stage"] = "review"
    rdoc = {"schema_version": "1.0", "site": "edu-arena", "level": 1, **meta,
            "review": {"id": f"{ch_id}-review", "title": f'{chapter["title"]} 복습', "minutes": 10}, "questions": review}
    json.dump(rdoc, open(os.path.join(base, "review.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    cdoc = {"schema_version": "1.0", "course": course["id"], "chapter": meta["chapter"], "lessons": entries,
            "review": {"id": f"{ch_id}-review", "file": "review.json", "questions": len(review)}}
    json.dump(cdoc, open(os.path.join(base, "chapter.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f'{ch_id}: 레슨 {len(entries)}개, 문항 {sum(e["questions"] for e in entries)} + 복습 {len(review)}')
    return entries, len(review)


def save_course(course_id):
    """plan.json의 목차와 만들어진 챕터를 합쳐 course.json을 씁니다. 아직 없는 챕터는 '준비 중'."""
    plan = json.load(open(os.path.join(os.path.dirname(ROOT), "plan.json"), encoding="utf-8"))[course_id]
    courses = json.load(open(os.path.join(ROOT, "courses.json"), encoding="utf-8"))["courses"]
    info = next(c for c in courses if c["id"] == course_id)
    chs, L, LQ, RQ = [], 0, 0, 0
    for no, ch in enumerate(plan["chapters"], 1):
        d = f"ch{no:02d}"
        path = os.path.join(ROOT, course_id, d, "chapter.json")
        entry = {"no": no, "id": f"{course_id}-{d}", "title": ch["title"], "dir": d}
        if os.path.exists(path):
            c = json.load(open(path, encoding="utf-8"))
            lq = sum(l["questions"] for l in c["lessons"])
            entry.update(lessons=len(c["lessons"]), lesson_questions=lq, review_questions=c["review"]["questions"])
            L += len(c["lessons"]); LQ += lq; RQ += c["review"]["questions"]
        else:
            entry.update(available=False, titles=ch["lessons"])
        chs.append(entry)
    doc = {"schema_version": "1.0", "level": 1,
           "course": {"id": course_id, "title": info["title"], "description": info["description"]},
           "totals": {"chapters": len(chs), "lessons": L, "lesson_questions": LQ, "review_questions": RQ, "questions": LQ + RQ},
           "chapters": chs}
    json.dump(doc, open(os.path.join(ROOT, course_id, "course.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"{course_id}/course.json: 레슨 {L}개, {LQ + RQ}문항")


# ---------- 오선 악보 (staff 위젯, player.html의 staffFig) ----------
def staff(alt, notes, clef="treble", key=0, time=None, noclef=False, minw=0):
    cfg = {"alt": alt, "clef": clef, "notes": notes}
    if key: cfg["key"] = key
    if time: cfg["time"] = time
    if noclef: cfg["noclef"] = True
    if minw: cfg["minw"] = minw
    return {"widget": "staff", "static": True, "config": cfg}


def N(p, d="q", label=None, hl=False, acc=None, dot=False, above=None, w=None):
    """p: 'C4', 'F#4'처럼 쓰거나 화음은 ['C4','E4','G4']. acc: '#','b','n' (화음이면 목록)."""
    n = {"p": p, "d": d}
    if label: n["label"] = label
    if hl: n["hl"] = True
    if acc: n["acc"] = acc
    if dot: n["dot"] = True
    if above: n["above"] = above
    if w: n["w"] = w
    return n


def REST(kind, label=None, hl=False):
    n = {"rest": kind}
    if label: n["label"] = label
    if hl: n["hl"] = True
    return n


BAR = {"bar": True}
END = {"bar": "end"}


# ---------- 연표 (음악사) ----------
def timeline(alt, spans, marks=(), unit=50, maxh=150):
    """spans: [(이름, 시작해, 끝해, 강조)], marks: [(해, 글)]. unit: 1칸 = 몇 년"""
    y0 = min(s[1] for s in spans)
    X = lambda y: (y - y0) / unit
    els = []
    for name, a, b, h in spans:
        els += [rect(X(a), 0, X(b) - X(a) - 0.05, 1.3, hl=h), text([(X(a) + X(b)) / 2, 0.65], name, hl=h),
                text([X(a), -0.55], str(a))]
    end = max(s[2] for s in spans)
    els.append(text([X(end), -0.55], str(end)))
    for k, (y, lab) in enumerate(marks):
        lift = 2.0 + (k % 2) * 0.9
        els += [seg([X(y), 1.3], [X(y), lift - 0.35], dash=True), text([X(y), lift], lab, hl=True)]
    return fig(alt, els, maxh=maxh)


# ---------- 색 채운 도형 (미술) ----------
def swatch(x, y, w, h, color):
    return {"t": "poly", "pts": [[x, y], [x + w, y], [x + w, y + h], [x, y + h]], "color": color}


def disc(c, r, color=None, hl=False):
    e = {"t": "circle", "c": list(c), "r": r}
    if color: e["color"] = color
    if hl: e["hl"] = True
    return e


def poly(pts, color=None, hl=False, open_=False):
    e = {"t": "poly", "pts": [list(p) for p in pts]}
    if color: e["color"] = color
    if hl: e["hl"] = True
    if open_: e["fill"] = False
    return e
