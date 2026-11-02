"""biz-arena 레벨2·3 가이드 공용 도구 (math-arena·tech-arena 공통 단원 템플릿).

과목: overview(분야 개요), prereq(선수지식 점검 + 레벨1 연결), units(로드맵), next(다음 과목)
단원: objectives(학습 목표), checklist(핵심 개념), advice(학습 조언 1~2문단),
      resources(추천 자료), hours(예상 학습 시간), after(먼저 볼 단원), selfcheck(자가점검 문항)
자가점검 문항은 레벨1 문항 스키마를 그대로 써서 같은 채점 코드로 동작한다.
"""
import json, os

CONTENT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content")

TRACKS = [
    {"id": "economics", "title": "경제", "note": "미시·거시 원론에서 시작해 중급 이론, 계량경제, 화폐금융, 공공경제로 나아갑니다. 수학 도구는 math-arena와 함께 공부합니다.",
     "l2": [["micro-principles", "미시경제원론"], ["macro-principles", "거시경제원론"]],
     "l3": [["intermediate-micro", "중급미시경제"], ["intermediate-macro", "중급거시경제"], ["econometrics", "계량경제학 입문"],
            ["money-banking", "화폐금융론"], ["public-economics", "공공경제학"]]},
    {"id": "management", "title": "경영", "note": "경영학원론으로 기업의 기능 전체를 본 뒤 조직·전략·운영·정보시스템으로 들어갑니다.",
     "l2": [["management-principles", "경영학원론"]],
     "l3": [["org-hrm", "조직행동·인사관리"], ["strategy", "경영전략"], ["operations", "생산·운영관리"], ["mis", "경영정보시스템(MIS)"]]},
    {"id": "accounting", "title": "회계", "note": "재무회계와 원가·관리회계 입문을 거쳐 K-IFRS 중심의 중급·고급회계와 회계감사로 나아갑니다.",
     "l2": [["financial-accounting", "재무회계 입문"], ["cost-managerial", "원가·관리회계"]],
     "l3": [["intermediate-acc1", "중급회계Ⅰ"], ["intermediate-acc2", "중급회계Ⅱ"], ["advanced-accounting", "고급회계"],
            ["auditing", "회계감사"], ["public-nonprofit", "정부·비영리회계"]]},
    {"id": "tax", "title": "세무", "note": "세법 입문에서 세목별 체계를 잡고, 법인세·소득세·부가가치세법과 국세기본법·상속세 및 증여세법으로 깊어집니다.",
     "l2": [["tax-intro", "세법 입문"]],
     "l3": [["corporate-tax", "법인세법"], ["income-tax", "소득세법"], ["vat", "부가가치세법"], ["basic-inheritance", "국세기본법·상속세 및 증여세법"]]},
    {"id": "finance", "title": "재무·금융", "note": "화폐의 시간가치와 위험·수익에서 출발해 투자론, 파생상품, 금융기관, 위험관리로 이어집니다.",
     "l2": [["finance-intro", "재무관리 입문"]],
     "l3": [["investments", "투자론"], ["derivatives", "파생상품"], ["financial-institutions", "금융기관론"], ["insurance-risk", "보험·위험관리"]]},
    {"id": "marketing", "title": "마케팅·유통", "note": "마케팅원론의 STP와 4P를 바탕으로 소비자행동, 조사, 디지털마케팅, 공급망관리로 나뉩니다.",
     "l2": [["marketing-principles", "마케팅원론"]],
     "l3": [["consumer-behavior", "소비자행동론"], ["marketing-research", "마케팅조사"], ["digital-marketing", "디지털마케팅"], ["scm", "유통·공급망관리(SCM)"]]},
    {"id": "trade", "title": "무역·국제경영", "note": "무역학원론으로 이론·정책·실무의 큰 그림을 잡고, 무역실무와 관세, 국제경영으로 나아갑니다.",
     "l2": [["trade-principles", "무역학원론"]],
     "l3": [["trade-practice", "무역실무(결제·운송·보험)"], ["customs", "관세와 통관"], ["international-business", "국제경영"]]},
]
LEVELS = {"2": "대학 원론 (경상계열 1~2학년 수준)", "3": "전공 심화 (학부 전공 트랙 수준)"}
VALIDATION = {"2": "경제학원론·경영학원론·회계원리·세법개론·재무관리·마케팅원론·무역학원론 표준 교재 목차와 재경관리사·회계관리 1급·투자자산운용사 출제 범위",
              "3": "학부 전공 과목 구성과 공인회계사·세무사·관세사 1차 시험 과목 구성"}

# 자주 쓰는 공개 자료
OPENSTAX = lambda title, slug: {"kind": "book", "provider": "OpenStax (무료 공개 교재)", "title": title,
                                "url": f"https://openstax.org/details/books/{slug}", "lang": "영어"}
KHAN = lambda title, path: {"kind": "video", "provider": "Khan Academy", "title": title,
                            "url": f"https://www.khanacademy.org/economics-finance-domain/{path}", "lang": "영어(일부 한국어)"}
MIT = lambda title, slug: {"kind": "lecture", "provider": "MIT OpenCourseWare", "title": title,
                           "url": f"https://ocw.mit.edu/courses/{slug}/", "lang": "영어"}
WEB = lambda provider, title, url, lang="한국어": {"kind": "web", "provider": provider, "title": title, "url": url, "lang": lang}


def R(base, part):
    d = dict(base); d["part"] = part; return d


def book(provider, title):
    return {"kind": "book", "provider": provider, "title": title}


def num(i, prompt, answer, expl, hint=None, fmt="integer", tol=0):
    q = {"type": "question", "id": f"q{i}", "qtype": "numeric", "prompt": prompt, "answer": str(answer),
         "answer_format": fmt, "tolerance": tol, "explanation": expl}
    if hint: q["hint"] = hint
    return q


def fill(i, prompt, blanks, expl, hint=None, groups=None):
    q = {"type": "question", "id": f"q{i}", "qtype": "fill_blank", "prompt": prompt,
         "blanks": [{"id": k + 1, "answers": a if isinstance(a, list) else [a]} for k, a in enumerate(blanks)],
         "explanation": expl}
    if hint: q["hint"] = hint
    if groups: q["unordered_groups"] = groups
    return q


def written(i, prompt, groups, need, model):
    return {"type": "question", "id": f"q{i}", "qtype": "written", "prompt": prompt,
            "rubric": {"visibility": "hidden", "keyword_groups": groups, "min_groups_matched": need},
            "model_answer": model}


def unit(no, title, hours, after, objectives, checklist, advice, resources, selfcheck):
    return {"no": no, "title": title, "hours": hours, "after": after, "objectives": objectives,
            "checklist": checklist, "advice": advice, "resources": resources, "selfcheck": selfcheck}


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
        assert 3 <= len(u["selfcheck"]) <= 6, f"{where}: 자가점검 3~6문항"
        for q in u["selfcheck"]:
            if q["qtype"] == "written":
                m = q["model_answer"]
                hit = sum(any(k in m for k in g) for g in q["rubric"]["keyword_groups"])
                assert hit >= q["rubric"]["min_groups_matched"], f"{where}: 모범 답안이 채점 기준 미달"
            else:
                assert len(q.get("explanation", "")) >= 10, f"{where}: 풀이"
            if q["qtype"] == "fill_blank":
                n = q["prompt"].count("{{")
                assert n == len(q["blanks"]), f"{where}: 빈칸 수"
    p = subject["prereq"]
    assert p["links"] and len(p["questions"]) >= 3, f"{subject['id']}: 선수 점검"


def write_subject(subject, units):
    check(subject, units)
    lv, tr, sid = subject["level"], subject["track"], subject["id"]
    base = os.path.join(CONTENT, f"level{lv}", tr, sid)
    os.makedirs(base, exist_ok=True)
    subj = dict(subject, schema_version="1.0", type="guide_subject")
    for k, q in enumerate(subj["prereq"]["questions"]):
        q["id"] = f"p{k + 1}"; q["stage"] = "prereq"
    subj["units"] = [{"no": u["no"], "title": u["title"], "hours": u["hours"], "after": u["after"],
                      "file": f"u{u['no']:02d}.json"} for u in units]
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
    print(f"{subject['title']}: {len(units)}단원, 약 {subj['total_hours']}시간, 자가점검 {n}문항, 선수 점검 {len(p_(subject))}문항")
    return subj


def p_(subject):
    return subject["prereq"]["questions"]


def write_tracks():
    out = {"schema_version": "1.0", "levels": LEVELS, "validation": VALIDATION, "tracks": []}
    for t in TRACKS:
        subs = []
        for lv, key in ((2, "l2"), (3, "l3")):
            for sid, title in t[key]:
                ok = os.path.exists(os.path.join(CONTENT, f"level{lv}", t["id"], sid, "subject.json"))
                subs.append({"level": lv, "id": sid, "title": title, "available": ok})
        out["tracks"].append({"id": t["id"], "title": t["title"], "note": t["note"], "subjects": subs})
    json.dump(out, open(os.path.join(CONTENT, "guides.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def L2LINK(track, sid, u):
    """레벨2 가이드 단원 링크 (제목은 이미 만든 subject.json에서 읽음)"""
    d = json.load(open(os.path.join(CONTENT, "level2", track, sid, "subject.json"), encoding="utf-8"))
    ut = next(x["title"] for x in d["units"] if x["no"] == u)
    return {"title": f"레벨2 {d['title']} · {u}단원 {ut}", "href": f"guide.html?lv=2&t={track}&s={sid}&u={u}"}


def L1LINK(c, ch):
    """레벨1 코스 챕터 링크 (코스·챕터 제목은 courses.json, course.json에서 읽음)"""
    cs = json.load(open(os.path.join(CONTENT, "level1", "courses.json"), encoding="utf-8"))["courses"]
    ct = next(x["title"] for x in cs if x["id"] == c)
    d = json.load(open(os.path.join(CONTENT, "level1", c, "course.json"), encoding="utf-8"))
    t = next(x["title"] for x in d["chapters"] if x["no"] == ch)
    return {"title": f"레벨1 {ct} · 챕터 {ch} {t}", "href": f"browse.html?c={c}#ch{ch:02d}"}
