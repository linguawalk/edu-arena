"""lit-arena 레벨2·3 가이드 공용 도구 (tech-arena·math-arena·sci-arena와 같은 공통 단원 템플릿).

과목: overview(분야 개요), prereq(선수지식 점검 + 레벨1 연결), units(로드맵), next(다음 과목)
단원: objectives(학습 목표), checklist(핵심 개념), advice(학습 조언 1~2문단),
      resources(추천 자료), hours(예상 학습 시간), after(먼저 볼 단원), selfcheck(자가점검 문항)
자가점검 문항은 레벨1 문항 스키마를 그대로 써서 같은 채점 코드로 동작한다.
트랙 항목 [id, 제목, 다른 트랙 id]는 다른 트랙의 과목을 공유한다(예: 세계문학 트랙의 문학개론 → 국문학 트랙).

바뀔 수 있는 값(어문 규범 개정, 교육용 한자 목록, 문학상 수상 현황 등)은 tools/facts.py에 두고 F(키)·V(키)로 쓴다.
그런 값이나 제도를 다루는 단원에는 review(근거, 확인 시점, 다음 점검, 무엇을 볼지, 쓰는 facts 키)를 붙인다.
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from facts import FACTS, F, V  # noqa: F401  (가이드 스크립트에서 함께 쓴다)

CONTENT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content")

TRACKS = [
    {"id": "korean-language", "title": "국어학", "note": "모국어인 국어를 '쓰는 사람'에서 '설명하는 사람'으로. 레벨1 국어Ⅰ의 문법 지식을 학문 체계로 넓힙니다.",
     "l2": [["korean-linguistics-intro", "국어학개론"], ["korean-grammar", "국어 문법론(형태·통사)"], ["korean-norms", "국어 어문 규범"]],
     "l3": [["korean-phonology", "국어 음운론"], ["korean-semantics-pragmatics", "국어 의미론·화용론"], ["korean-language-history", "국어사"]]},
    {"id": "hanja-hanmun", "title": "한자·한문", "note": "한자는 국어 어휘의 뿌리이자 고전 문해력의 열쇠입니다. 문자학과 한문 문법에서 한국 한문학으로 이어집니다.",
     "l2": [["hanja-studies", "한자학 개론(문자학)"], ["hanmun-grammar", "한문 문법과 강독"]],
     "l3": [["korean-hanmun-literature", "한국 한문학사"], ["classics-reading", "경서·사서 강독"]]},
    {"id": "english-studies", "title": "영어학", "note": "외국어 회화가 아니라 세계 공용어로서의 영어를 다룹니다. 영어의 구조와 역사, 학술 영어, 국제 소통의 언어로서의 영어를 공부합니다.",
     "l2": [["english-linguistics-intro", "영어학개론"], ["academic-english", "학술 영어 읽기·쓰기"]],
     "l3": [["english-syntax", "영어 통사론"], ["world-englishes", "세계 영어와 사회언어학"], ["history-of-english", "영어사"]]},
    {"id": "korean-literature", "title": "국문학", "note": "레벨1 국문학Ⅰ·Ⅱ의 작품 감상 위에 갈래론과 문학사를 쌓습니다. 문학개론은 세계문학 트랙과 공유합니다.",
     "l2": [["literature-intro", "문학개론"], ["korean-classical-lit-history", "한국 고전문학사"], ["korean-modern-lit-history", "한국 현대문학사"]],
     "l3": [["classical-poetry", "고전 시가론"], ["classical-prose", "고전 산문론"], ["modern-poetry", "현대시론"], ["modern-fiction", "현대소설론"]]},
    {"id": "world-literature", "title": "세계문학", "note": "한국어 번역으로 읽는 세계의 정전과 문학사. 원어로 읽는 지역 문학은 lingua-arena의 언어 트랙이 맡습니다.",
     "l2": [["literature-intro", "문학개론", "korean-literature"], ["western-lit-history", "서양 문학사"], ["east-asian-lit-history", "동아시아 문학사"]],
     "l3": [["comparative-literature", "비교문학"], ["english-lit", "영미문학"], ["literary-theory", "문학 비평 이론"], ["translation-studies", "번역학"]]},
]
LEVELS = {"2": "전문대 수준 (학문 입문·개론)", "3": "대학 수준 (전공 심화)"}
VALIDATION = {"2": "국어국문학과·영어영문학과·한문학과 개론 교재의 목차와 관련 시험(국어능력인증시험, KBS한국어능력시험, 한자능력검정시험 2급, 대학 편입 영어 등)의 출제 범위",
              "3": "학부 전공 교재의 목차와 관련 시험(한자능력검정시험 1급, 중등교사 임용 국어·영어·한문 등)의 과목 구성. 시험 대비가 아니라 누락 방지용입니다"}

# ---------------------------------------------------------------- 자주 쓰는 자료와 링크
OPENSTAX = lambda title, slug: {"kind": "book", "provider": "OpenStax (무료 공개 교재)", "title": title,
                                "url": f"https://openstax.org/details/books/{slug}", "lang": "영어"}
SEP = lambda title, slug: {"kind": "web", "provider": "Stanford Encyclopedia of Philosophy", "title": title,
                           "url": f"https://plato.stanford.edu/entries/{slug}/", "lang": "영어"}
WEB = lambda provider, title, url, lang="한국어": {"kind": "web", "provider": provider, "title": title, "url": url, "lang": lang}
KMOOC = {"kind": "lecture", "provider": "K-MOOC", "title": "K-MOOC 강좌 검색 (과목명으로 검색)", "url": "https://www.kmooc.kr/", "lang": "한국어"}
KOCW = {"kind": "lecture", "provider": "KOCW (대학 공개 강의)", "title": "KOCW 강의 검색 (과목명으로 검색)", "url": "http://www.kocw.net/", "lang": "한국어"}
LAW = {"kind": "web", "provider": "국가법령정보센터", "title": "법령 원문 검색", "url": "https://www.law.go.kr/", "lang": "한국어"}
KORNORM = {"kind": "web", "provider": "국립국어원", "title": "한국어 어문 규범 (맞춤법·표준어·표기법)", "url": "https://korean.go.kr/kornorms/", "lang": "한국어"}
STDICT = {"kind": "web", "provider": "국립국어원", "title": "표준국어대사전", "url": "https://stdict.korean.go.kr/", "lang": "한국어"}
ITKC = {"kind": "web", "provider": "한국고전번역원", "title": "한국고전종합DB (원문·번역)", "url": "https://db.itkc.or.kr/", "lang": "한국어"}
GUTENBERG = {"kind": "web", "provider": "Project Gutenberg", "title": "저작권 만료 원전 (영어 등)", "url": "https://www.gutenberg.org/", "lang": "영어"}
L1 = lambda c, n, title: {"title": f"레벨1 · {title}", "href": f"browse.html?c={c}#ch{n:02d}"}
L1R = lambda c, n, title: {"kind": "web", "provider": "lit-arena 레벨1", "title": f"챕터 {n} {title}", "url": f"browse.html?c={c}#ch{n:02d}", "part": "레벨1 복습"}
LINGUA = lambda path, title: {"title": f"lingua-arena · {title}", "href": f"https://lingua-arena.org/{path}"}
SCI = lambda c, title: {"title": f"sci-arena 레벨1 · {title}", "href": f"https://sci-arena.org/browse.html?c={c}"}
MATH = lambda c, title: {"title": f"math-arena 레벨1 · {title}", "href": f"https://math-arena.org/browse.html?c={c}"}
G2R = lambda t, s, u, title: {"kind": "web", "provider": "lit-arena 레벨2", "title": title, "url": f"guide.html?lv=2&t={t}&s={s}" + (f"&u={u}" if u else ""), "part": "함께 볼 단원"}
G3R = lambda t, s, u, title: {"kind": "web", "provider": "lit-arena 레벨3", "title": title, "url": f"guide.html?lv=3&t={t}&s={s}" + (f"&u={u}" if u else ""), "part": "함께 볼 단원"}
G2 = lambda t, s, title: {"title": f"레벨2 · {title}", "href": f"guide.html?lv=2&t={t}&s={s}"}
G3 = lambda t, s, title: {"title": f"레벨3 · {title}", "href": f"guide.html?lv=3&t={t}&s={s}"}


def book(provider, title):
    return {"kind": "book", "provider": provider, "title": title}


def R(base, part):
    d = dict(base); d["part"] = part; return d


L2NOTE = "레벨 2 (전문대 수준, 학문 입문·개론). 목차 검증 기준: {}."
L3NOTE = "레벨 3 (대학 수준, 전공 심화). 목차 검증 기준: {}. 레벨3은 단원당 학습 조언 1문단, 자가점검 3문항의 가벼운 형식이며 원전과 전공서를 직접 읽는 것을 전제로 합니다."


# ---------------------------------------------------------------- 점검 정보(review)
# 법령·제도·통계처럼 바뀔 수 있는 내용이 있는 단원(또는 과목)에 붙인다.
#   basis: 근거, checked: 마지막 확인 "YYYY-MM", next: 다음 점검 "YYYY-MM", watch: 무엇이 바뀌면 고칠지,
#   facts: 이 단원이 쓰는 tools/facts.py 키 목록(값을 고치고 다시 빌드하면 함께 바뀐다)
def review(basis, checked, next_, watch, facts=()):
    return {"basis": basis, "checked": checked, "next": next_, "watch": watch, "facts": list(facts)}


def _check_review(r, where):
    for k in ("basis", "checked", "next", "watch"):
        assert r.get(k), f"{where}: review.{k}"
    assert re.fullmatch(r"\d{4}-\d{2}", r["checked"]) and re.fullmatch(r"\d{4}-\d{2}", r["next"]), f"{where}: review 날짜 형식 YYYY-MM"
    assert r["next"] > r["checked"], f"{where}: 다음 점검은 확인일 뒤"
    for k in r.get("facts", []): assert k in FACTS, f"{where}: facts 키 {k} 없음"


# ---------------------------------------------------------------- 문항
def num(i, prompt, answer, expl, hint=None, fmt="integer", tol=0):
    q = {"type": "question", "id": f"q{i}", "qtype": "numeric", "prompt": prompt, "answer": str(answer),
         "answer_format": fmt, "tolerance": tol, "explanation": expl}
    if hint: q["hint"] = hint
    return q


def fill(i, prompt, blanks, expl, hint=None):
    q = {"type": "question", "id": f"q{i}", "qtype": "fill_blank", "prompt": prompt,
         "blanks": [{"id": k + 1, "answers": a if isinstance(a, list) else [a]} for k, a in enumerate(blanks)],
         "explanation": expl}
    if hint: q["hint"] = hint
    return q


def order(i, prompt, correct, disp, expl, hint=None):
    """correct: 정답 순서의 항목, disp: 화면 표시 순서(correct의 인덱스, 정답 순서와 달라야 함)."""
    ids = "abcdefgh"
    q = {"type": "question", "id": f"q{i}", "qtype": "ordering", "prompt": prompt,
         "items": [{"id": ids[k], "text": correct[j]} for k, j in enumerate(disp)],
         "answer_order": [ids[disp.index(j)] for j in range(len(correct))], "explanation": expl}
    if hint: q["hint"] = hint
    return q


def written(i, prompt, groups, need, model):
    return {"type": "question", "id": f"q{i}", "qtype": "written", "prompt": prompt,
            "rubric": {"visibility": "hidden", "keyword_groups": groups, "min_groups_matched": need},
            "model_answer": model}


def unit(no, title, hours, after, objectives, checklist, advice, resources, selfcheck, review=None):
    u = {"no": no, "title": title, "hours": hours, "after": after, "objectives": objectives,
         "checklist": checklist, "advice": advice, "resources": resources, "selfcheck": selfcheck}
    if review: u["review"] = review
    return u


# ---------------------------------------------------------------- 검사와 저장
def _norm(s):
    return re.sub(r"\s+", "", str(s)).lower()


_EXPOSED = []


def _check_q(q, where):
    if q["qtype"] == "written":
        m = q["model_answer"]
        hit = sum(any(k in m for k in g) for g in q["rubric"]["keyword_groups"])
        assert hit >= q["rubric"]["min_groups_matched"], f"{where}: 모범 답안이 채점 기준 미달"
        return
    assert len(q.get("explanation", "")) >= 10, f"{where}: 풀이"
    if q["qtype"] == "fill_blank":
        n = q["prompt"].count("{{")
        assert n == len(q["blanks"]), f"{where}: 빈칸 수"
        shown = _norm(re.sub(r"\{\{\d+\}\}", "", q["prompt"]))
        for b in q["blanks"]:
            for a in b["answers"]:
                if len(_norm(a)) >= 2 and _norm(a) in shown: _EXPOSED.append(f"{where}: 지문에 정답 노출({a})")
    if q["qtype"] == "ordering":
        assert len(q["items"]) >= 3, f"{where}: 순서 항목 3개 이상"
        assert q["answer_order"] != [it["id"] for it in q["items"]], f"{where}: 표시 순서가 정답 순서와 같음"


def check(subject, units):
    """최소 품질 검사"""
    nos = [u["no"] for u in units]
    assert nos == list(range(1, len(units) + 1)), "단원 번호"
    for u in units:
        where = f"{subject['id']} u{u['no']}"
        assert all(a < u["no"] for a in u["after"]), f"{where}: 선수 단원은 앞 단원이어야 함"
        assert len(u["objectives"]) >= 2 and len(u["checklist"]) >= 4, f"{where}: 목표·체크리스트"
        assert len(u["advice"]) >= 1 and all(len(a) >= 80 for a in u["advice"]), f"{where}: 조언 분량"
        assert u["resources"], f"{where}: 자료"
        for r in u["resources"]:
            assert r.get("kind") in ("lecture", "video", "book", "web") and r.get("provider") and r.get("title"), f"{where}: 자료 형식 {r}"
        assert 3 <= len(u["selfcheck"]) <= 6, f"{where}: 자가점검 3~6문항"
        if u.get("review"): _check_review(u["review"], where)
        for q in u["selfcheck"]: _check_q(q, where)
    if subject.get("review"): _check_review(subject["review"], subject["id"])
    p = subject["prereq"]
    assert p["links"] and len(p["questions"]) >= 3, f"{subject['id']}: 선수 점검"
    for q in p["questions"]: _check_q(q, f"{subject['id']} 선수")
    assert len(subject["overview"]) == 3, f"{subject['id']}: 개요 3문단"
    assert not _EXPOSED, "\n".join(_EXPOSED)


def write_subject(subject, units):
    check(subject, units)
    lv, tr, sid = subject["level"], subject["track"], subject["id"]
    base = os.path.join(CONTENT, f"level{lv}", tr, sid)
    os.makedirs(base, exist_ok=True)
    subj = dict(subject, schema_version="1.0", type="guide_subject")
    for k, q in enumerate(subj["prereq"]["questions"]):
        q["id"] = f"p{k + 1}"; q["stage"] = "prereq"
    subj["units"] = [dict({"no": u["no"], "title": u["title"], "hours": u["hours"], "after": u["after"],
                      "file": f"u{u['no']:02d}.json"}, **({"review": True} if u.get("review") else {})) for u in units]
    subj["total_hours"] = sum(u["hours"] for u in units)
    json.dump(subj, open(os.path.join(base, "subject.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for u in units:
        d = dict(u, schema_version="1.0", type="guide_unit", level=lv, track=tr, subject=sid,
                 id=f"l{lv}-{tr}-{sid}-u{u['no']:02d}")
        for k, q in enumerate(d["selfcheck"]):
            q["id"] = f"q{k + 1}"; q["stage"] = "selfcheck"
        json.dump(d, open(os.path.join(base, f"u{u['no']:02d}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    write_tracks()
    n = sum(len(u["selfcheck"]) for u in units)
    print(f"{subject['title']}: {len(units)}단원, 약 {subj['total_hours']}시간, 자가점검 {n}문항, 선수 점검 {len(subject['prereq']['questions'])}문항")
    return subj


def write_tracks():
    out = {"schema_version": "1.0", "levels": LEVELS, "validation": VALIDATION, "tracks": []}
    for t in TRACKS:
        subs = []
        for lv, key in ((2, "l2"), (3, "l3")):
            for e in t[key]:
                sid, title = e[0], e[1]
                home = e[2] if len(e) > 2 and e[2] else t["id"]
                ok = os.path.exists(os.path.join(CONTENT, f"level{lv}", home, sid, "subject.json"))
                d = {"level": lv, "id": sid, "title": title, "available": ok}
                if home != t["id"]: d["t"] = home
                subs.append(d)
        out["tracks"].append({"id": t["id"], "title": t["title"], "note": t["note"], "subjects": subs})
    json.dump(out, open(os.path.join(CONTENT, "guides.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    write_tracks(); print("guides.json 갱신")
