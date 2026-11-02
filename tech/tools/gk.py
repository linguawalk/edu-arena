"""tech-arena 레벨2·3 가이드 공용 도구 (math-arena·sci-arena와 같은 공통 단원 템플릿).

과목: overview(분야 개요), prereq(선수지식 점검 + 레벨1·타 Arena 연결), units(로드맵), next(다음 과목)
단원: objectives(학습 목표), checklist(핵심 개념), advice(학습 조언 1~2문단),
      resources(추천 자료), hours(예상 학습 시간), after(먼저 볼 단원), selfcheck(자가점검 문항)
자가점검 문항은 레벨1 문항 스키마를 그대로 써서 같은 채점 코드로 동작한다.
트랙 항목 [id, 제목, 다른 트랙 id]는 다른 트랙의 과목을 공유한다(예: 토목의 정역학 → 기계 트랙).
"""
import json, os

CONTENT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content")

TRACKS = [
    {"id": "electrical", "title": "전기", "note": "회로이론과 전기자기학에서 시작해 전기기기·전력·설비로, 레벨3에서 전력계통·제어·전력전자로 나아갑니다.",
     "l2": [["circuit-theory", "회로이론"], ["electromagnetics", "전기자기학"], ["electric-machines", "전기기기"], ["power-basics", "전력공학 기초"], ["electrical-installation", "전기설비"]],
     "l3": [["power-systems", "전력계통"], ["control", "제어공학"], ["power-electronics", "전력전자"]]},
    {"id": "electronics", "title": "전자", "note": "반도체 소자로 만드는 아날로그·디지털 회로. 회로이론(전기 트랙)을 먼저 공부하세요.",
     "l2": [["circuit-theory", "회로이론", "electrical"], ["electronic-circuits", "전자회로"], ["digital-circuits", "디지털회로"], ["electromagnetics", "전기자기학", "electrical"]],
     "l3": [["integrated-circuits", "집적회로"], ["embedded", "임베디드 시스템"]]},
    {"id": "ict", "title": "정보통신", "note": "신호를 멀리 보내는 기술. 레벨1 전기전자의 통신 단원과 컴퓨터의 네트워크 단원이 만나는 곳입니다.",
     "l2": [["comm-theory", "통신이론 기초"], ["wireless", "무선통신"], ["optical-comm", "광통신"], ["comm-networks", "통신망"]],
     "l3": [["digital-comm", "디지털통신"], ["mobile-comm", "이동통신"], ["satellite-comm", "위성통신"], ["network-design", "통신망 설계"]]},
    {"id": "computer", "title": "컴퓨터", "note": "하드웨어·운영체제·네트워크·데이터베이스·소프트웨어의 원리와 설계. 코드 작성과 자료구조·알고리즘 실습은 code-arena가 맡습니다.",
     "l2": [["computer-architecture", "컴퓨터 구조"], ["operating-systems", "운영체제"], ["networks", "컴퓨터 네트워크"],
            ["databases", "데이터베이스 시스템"], ["software-engineering", "소프트웨어공학"], ["digital-circuits", "디지털회로", "electronics"],
            ["dsa", "자료구조·알고리즘", None, "https://code-arena.org/browse.html?type=module&key=dsa", "code-arena"]],
     "l3": [["system-programming", "시스템 프로그래밍"], ["distributed-systems", "분산시스템·클라우드"], ["security", "정보보안"],
            ["compilers", "컴파일러와 언어 원리"]]},
    {"id": "mechanical", "title": "기계", "note": "힘과 변형, 열과 에너지, 기계 설계. 정역학·재료역학은 토목·건축과 공유합니다.",
     "l2": [["statics", "정역학"], ["mechanics-of-materials", "재료역학"], ["thermodynamics", "열역학 기초"], ["machine-elements", "기계요소"], ["drafting-cad", "제도·CAD"]],
     "l3": [["fluid-mechanics", "유체역학"], ["heat-transfer", "열전달"], ["dynamics-vibration", "동역학·진동"], ["machine-design", "기계설계"]]},
    {"id": "chemical", "title": "화공", "note": "물질과 에너지의 수지에서 시작해 반응·이동·분리·제어로. 레벨1 화학공학에서 이어집니다.",
     "l2": [["stoichiometry", "화공양론"], ["chem-thermo", "화공열역학 기초"], ["unit-operations", "단위조작 기초"]],
     "l3": [["reaction-engineering", "반응공학"], ["transport", "이동현상"], ["separation", "분리공정"], ["process-control", "공정제어"]]},
    {"id": "civil", "title": "토목", "note": "구조물과 땅과 물. 레벨1 기계와 sci-arena 물리가 선수이며 역학 과목은 기계 트랙과 공유합니다.",
     "l2": [["statics", "정역학", "mechanical"], ["mechanics-of-materials", "재료역학", "mechanical"], ["surveying", "측량"], ["soil-mechanics", "토질역학 기초"], ["hydraulics", "수리학 기초"]],
     "l3": [["structural-analysis", "구조해석"], ["rc-steel", "철근콘크리트·강구조"], ["foundation", "기초공학"], ["hydrology", "수문학"]]},
    {"id": "architecture", "title": "건축", "note": "공간을 계획하고, 세우고, 쾌적하게 만드는 일. 구조는 기계 트랙의 역학 과목에서 출발합니다.",
     "l2": [["statics", "정역학", "mechanical"], ["arch-planning", "건축계획"], ["arch-structure", "건축구조 기초"], ["construction", "시공"], ["building-services", "건축환경·설비"]],
     "l3": [["structural-design", "구조설계"], ["urban-design", "도시설계"], ["green-building", "친환경·에너지 건축"]]},
    {"id": "materials", "title": "재료", "note": "원자 배열이 성질을 결정합니다. 반도체·이차전지 등 융합 과정의 공통 선수입니다.",
     "l2": [["materials-intro", "재료공학 입문"]],
     "l3": [["material-properties", "재료물성"], ["metal-ceramic-polymer", "금속·세라믹·고분자"], ["materials-analysis", "재료분석"]]},
    {"id": "industrial", "title": "산업", "note": "시스템을 더 효율적으로. math-arena 확률·통계가 선수입니다.",
     "l2": [["ie-intro", "산업공학 입문"]],
     "l3": [["operations-research", "경영과학(OR)"], ["quality-engineering", "품질공학"], ["ergonomics", "인간공학"]]},
    {"id": "convergence", "title": "융합", "note": "12대 국가전략기술을 뼈대로 한 7개 군 22과정. 레벨1에서 바로 이어지는 3과정은 레벨2 입문 브리지가 있습니다.",
     "l2": [["semiconductor-intro", "반도체 입문 (브리지)"], ["ai-chip-intro", "AI 반도체 입문 (브리지)"], ["next-comm-intro", "차세대 통신 입문 (브리지)"]],
     "l3": [["semiconductor", "반도체 소자·공정"], ["ai-chip", "AI 반도체"], ["display", "디스플레이"], ["quantum-tech", "양자기술 입문"],
            ["battery", "이차전지"], ["hydrogen", "수소에너지"], ["nuclear", "차세대 원자력"], ["renewable-grid", "신재생·스마트그리드"], ["carbon-neutral", "탄소중립 공학"],
            ["ev-autonomous", "전기차·자율주행"], ["drone-uam", "드론·UAM"], ["aerospace", "우주항공"], ["smart-ocean", "스마트 해양·조선"],
            ["ai-engineering", "AI 공학"], ["next-comm", "차세대 통신"], ["cybersecurity", "사이버보안 공학"],
            ["robotics", "로보틱스·휴머노이드"], ["smart-factory", "스마트팩토리·디지털트윈"], ["additive-mfg", "적층제조(3D프린팅)"],
            ["bioprocess", "바이오공정·합성생물학"], ["biomedical", "의공학·웨어러블"], ["smart-city", "스마트시티·스마트건설"]]},
]
LEVELS = {"2": "응용 (전문대졸·산업기사 수준)", "3": "심화 (대졸·기사 수준)"}
VALIDATION = {"2": "분야별 산업기사 필기 과목 구성과 전문대·대학 저학년 표준 교재의 목차",
              "3": "분야별 기사 필기 과목 구성(전기기사, 일반기계기사, 화공기사, 토목기사, 건축기사, 정보처리기사, 정보통신기사 등)과 학부 전공 교재의 목차. 시험 대비가 아니라 누락 방지용입니다"}

# 자주 쓰는 공개 자료
OCW = lambda code, title, slug: {"kind": "lecture", "provider": "MIT OpenCourseWare", "title": f"{code} {title}",
                                 "url": f"https://ocw.mit.edu/courses/{slug}/", "lang": "영어"}
OPENSTAX = lambda title, slug: {"kind": "book", "provider": "OpenStax (무료 공개 교재)", "title": title,
                                "url": f"https://openstax.org/details/books/{slug}", "lang": "영어"}
KHAN = lambda title, path: {"kind": "video", "provider": "Khan Academy", "title": title,
                            "url": f"https://www.khanacademy.org/science/{path}", "lang": "영어(일부 한국어)"}
L1 = lambda c, n, title: {"title": f"레벨1 · {title}", "href": f"browse.html?c={c}#ch{n:02d}"}
L1R = lambda c, n, title: {"kind": "web", "provider": "tech-arena 레벨1", "title": f"챕터 {n} {title}", "url": f"browse.html?c={c}#ch{n:02d}"}
SCI = lambda c, title: {"title": f"sci-arena 레벨1 · {title}", "href": f"https://sci-arena.org/browse.html?c={c}"}
MATHG = lambda lv, t, s, title: {"title": f"math-arena 레벨{lv} · {title}", "href": f"https://math-arena.org/guide.html?lv={lv}&t={t}&s={s}"}


# ---------------------------------------------------------------- 점검 정보(review)와 규정값(standards)
# 법령·기준·시험 제도·시장 수치처럼 바뀔 수 있는 내용이 있는 단원(또는 과목)에 review를 붙인다.
#   basis: 근거(예: "한국전기설비규정(KEC)"), checked: 마지막 확인 "YYYY-MM", next: 다음 점검 "YYYY-MM",
#   watch: 무엇이 바뀌면 고쳐야 하는지, standards: 이 단원이 쓰는 규정값 키 목록
# 규정값은 content/standards.json 한곳에 두고 std(키)로 불러 문항·해설에 쓴다. 값을 고치고 다시 빌드하면 함께 바뀐다.
STANDARDS_PATH = os.path.join(CONTENT, "standards.json")


def _load_std():
    try: return json.load(open(STANDARDS_PATH, encoding="utf-8"))["items"]
    except FileNotFoundError: return {}


def std(key):
    """규정값 한 항목: value, unit, text, basis, clause, checked, next"""
    items = _load_std()
    assert key in items, f"standards.json에 {key} 없음"
    return items[key]


def review(basis, checked, next_, watch, standards=()):
    return {"basis": basis, "checked": checked, "next": next_, "watch": watch, "standards": list(standards)}


def _check_review(r, where):
    import re
    for k in ("basis", "checked", "next", "watch"):
        assert r.get(k), f"{where}: review.{k}"
    assert re.fullmatch(r"\d{4}-\d{2}", r["checked"]) and re.fullmatch(r"\d{4}-\d{2}", r["next"]), f"{where}: review 날짜 형식 YYYY-MM"
    assert r["next"] > r["checked"], f"{where}: 다음 점검은 확인일 뒤"
    items = _load_std()
    for k in r.get("standards", []): assert k in items, f"{where}: 규정값 {k} 없음"


def R(base, part):
    d = dict(base); d["part"] = part; return d


def book(provider, title):
    return {"kind": "book", "provider": provider, "title": title}


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


def written(i, prompt, groups, need, model):
    return {"type": "question", "id": f"q{i}", "qtype": "written", "prompt": prompt,
            "rubric": {"visibility": "hidden", "keyword_groups": groups, "min_groups_matched": need},
            "model_answer": model}


def unit(no, title, hours, after, objectives, checklist, advice, resources, selfcheck, review=None):
    u = {"no": no, "title": title, "hours": hours, "after": after, "objectives": objectives,
         "checklist": checklist, "advice": advice, "resources": resources, "selfcheck": selfcheck}
    if review: u["review"] = review
    return u


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
        if u.get("review"): _check_review(u["review"], where)
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
    if subject.get("review"): _check_review(subject["review"], subject["id"])
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
    print(f"{subject['title']}: {len(units)}단원, 약 {subj['total_hours']}시간, 자가점검 {n}문항, 선수 점검 {len(p_(subject))}문항")
    return subj


def p_(subject):
    return subject["prereq"]["questions"]


def write_tracks():
    out = {"schema_version": "1.0", "levels": LEVELS, "validation": VALIDATION, "tracks": []}
    for t in TRACKS:
        subs = []
        for lv, key in ((2, "l2"), (3, "l3")):
            for e in t[key]:
                sid, title = e[0], e[1]
                if len(e) > 3 and e[3]:  # 다른 사이트의 과목으로 연결
                    subs.append({"level": lv, "id": sid, "title": title, "available": True, "url": e[3], "site": e[4]})
                    continue
                home = e[2] if len(e) > 2 and e[2] else t["id"]
                ok = os.path.exists(os.path.join(CONTENT, f"level{lv}", home, sid, "subject.json"))
                d = {"level": lv, "id": sid, "title": title, "available": ok}
                if home != t["id"]: d["t"] = home
                subs.append(d)
        out["tracks"].append({"id": t["id"], "title": t["title"], "note": t["note"], "subjects": subs})
    json.dump(out, open(os.path.join(CONTENT, "guides.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
