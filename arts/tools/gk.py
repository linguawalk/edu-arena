"""edu-arena 예체능 레벨2·3 가이드 공용 도구 (lit·tech·math·sci와 같은 공통 단원 템플릿).

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
FACTS = {}  # 예체능은 아직 별도 facts 파일이 없다. 바뀔 수 있는 값은 단원 review로 표시한다.

CONTENT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content")

TRACKS = [
    {"id": "harmony", "title": "화성학", "note": "레벨1 '음악 이론과 감상'의 조성과 화음 기초에서 이어집니다. 성부 진행과 화음 연결에서 시작해 실용화성, 대위법과 20세기 화성으로 나아갑니다.",
     "l2": [["harmony-basics", "화성 기초 (성부 진행, 7화음, 전조)"], ["applied-harmony", "실용화성 (코드 심볼, 텐션, 대리코드)"]],
     "l3": [["counterpoint", "대위법"], ["chromatic-harmony", "반음계적 화성"], ["20c-harmony", "20세기 화성"]]},
    {"id": "composition", "title": "작곡·편곡", "note": "가락을 만들고 악기에 나누어 맡기는 방법. 화성학 트랙과 함께 공부하세요.",
     "l2": [["melody-writing", "가락 만들기와 편곡 기초"]],
     "l3": [["orchestration", "관현악법"]]},
    {"id": "music-tech", "title": "음악 기술", "note": "소리가 녹음되고 다듬어지는 과정. 레벨1 '소리의 성질'에서 이어집니다.",
     "l2": [["acoustics-daw", "음향의 원리와 DAW·녹음 기초"]],
     "l3": [["mixing-mastering", "믹싱과 마스터링"]]},
    {"id": "musicology", "title": "음악학", "note": "음악을 역사와 이론, 문화의 눈으로 연구합니다. 레벨1 '음악사'에서 이어집니다.",
     "l2": [["music-history-adv", "음악사 심화"]],
     "l3": [["music-aesthetics", "음악미학"], ["ethnomusicology", "민족음악학"]]},
    {"id": "art-history", "title": "미술사 심화", "note": "레벨1 '미술사'에서 이어집니다. 서양과 동양 미술을 시대·지역별로 깊게 읽고, 미술사를 연구하는 방법을 배웁니다.",
     "l2": [["western-eastern-art", "서양·동양 미술사"]],
     "l3": [["art-history-methods", "미술사 방법론"]]},
    {"id": "aesthetics", "title": "미학·비평", "note": "아름다움과 예술이란 무엇인지 묻고, 작품을 근거를 들어 평가하는 법을 배웁니다.",
     "l2": [["aesthetics-intro", "미학 입문"]],
     "l3": [["contemporary-theory", "현대 미술 이론과 비평"]]},
    {"id": "design", "title": "디자인", "note": "레벨1 '미술의 요소와 감상'의 조형 원리를 실제 시각 디자인에 적용합니다.",
     "l2": [["visual-design", "시각 디자인 원리와 타이포그래피"]],
     "l3": [["design-theory", "디자인 이론과 역사"]]},
    {"id": "photo-film", "title": "사진·영상", "note": "빛과 구도로 장면을 만들고, 장면을 이어 이야기를 만드는 방법.",
     "l2": [["photography", "사진의 원리와 구도"]],
     "l3": [["film-language", "영상 언어와 편집"]]},
    {"id": "performing-arts", "title": "공연예술", "note": "무용과 연극을 작품과 역사, 표현 방법으로 이해합니다.",
     "l2": [["dance-theatre-intro", "무용·연극 개론"]],
     "l3": [["performance-history", "공연예술사와 작품 분석"]]},
    {"id": "sport-science", "title": "스포츠 과학", "note": "몸이 운동에 어떻게 반응하고 움직이는지 과학으로 설명합니다. 레벨1 '스포츠와 건강'에서 이어집니다.",
     "l2": [["exercise-physiology", "운동생리학"], ["biomechanics", "운동역학"]],
     "l3": [["training-methods", "트레이닝 방법론"], ["sports-medicine", "스포츠 의과학"]]},
    {"id": "sport-humanities", "title": "스포츠 인문사회", "note": "스포츠를 하는 사람의 마음과, 스포츠가 사회와 맺는 관계를 다룹니다.",
     "l2": [["sport-psychology", "스포츠심리학"], ["sport-sociology", "스포츠사회학"]],
     "l3": [["sport-ethics", "스포츠윤리"], ["pe-history", "한국체육사"]]},
    {"id": "sport-education", "title": "스포츠 교육·경영", "note": "운동을 가르치고, 스포츠 조직과 산업을 운영하는 방법.",
     "l2": [["sport-pedagogy", "스포츠교육학과 생활체육 지도"]],
     "l3": [["sport-management", "스포츠 경영과 산업"]]},
]
LEVELS = {"2": "응용 (전문대졸·대학 1~2학년 수준)", "3": "심화 (대졸·학부 전공 수준)"}
VALIDATION = {"2": "음악·미술은 대학 교양·전공 기초 과목과 표준 교재의 목차, 체육은 생활스포츠지도사 2급 필기 과목 구성", "3": "음악·미술은 학부 전공 과목과 전공 교재의 목차, 체육은 생활스포츠지도사·전문스포츠지도사 필기 과목과 학부 전공 교재의 목차. 시험 대비가 아니라 누락 방지용입니다"}

# ---------------------------------------------------------------- 자주 쓰는 자료와 링크
WEB = lambda provider, title, url, lang="한국어": {"kind": "web", "provider": provider, "title": title, "url": url, "lang": lang}
KMOOC = {"kind": "lecture", "provider": "K-MOOC", "title": "K-MOOC 강좌 검색 (과목명으로 검색)", "url": "https://www.kmooc.kr/", "lang": "한국어"}
KOCW = {"kind": "lecture", "provider": "KOCW (대학 공개 강의)", "title": "KOCW 강의 검색 (과목명으로 검색)", "url": "http://www.kocw.net/", "lang": "한국어"}
OMT = {"kind": "book", "provider": "Open Music Theory (무료 공개 교재)", "title": "Open Music Theory, 2판", "url": "https://viva.pressbooks.pub/openmusictheory/", "lang": "영어"}
MTNET = {"kind": "web", "provider": "musictheory.net (무료)", "title": "음악 이론 레슨과 연습 도구(음정·화음·조표 연습)", "url": "https://www.musictheory.net/", "lang": "영어·한국어 일부"}
IMSLP = {"kind": "web", "provider": "IMSLP (페트루치 악보 도서관)", "title": "저작권 만료 악보 검색", "url": "https://imslp.org/", "lang": "영어"}
YALE_MUSIC = {"kind": "lecture", "provider": "Open Yale Courses", "title": "MUSI 112 Listening to Music (Craig Wright)", "url": "https://oyc.yale.edu/music/musi-112", "lang": "영어"}
SMARTHISTORY = {"kind": "web", "provider": "Smarthistory (무료)", "title": "미술사 영상과 해설", "url": "https://smarthistory.org/", "lang": "영어"}
KHAN_ART = {"kind": "video", "provider": "Khan Academy", "title": "Arts and humanities: Art history", "url": "https://www.khanacademy.org/humanities/art-history", "lang": "영어"}
SEP = lambda title, slug: {"kind": "web", "provider": "Stanford Encyclopedia of Philosophy", "title": title, "url": f"https://plato.stanford.edu/entries/{slug}/", "lang": "영어"}
L1 = lambda c, n, title: {"title": f"레벨1 · {title}", "href": f"browse.html?c={c}#ch{n:02d}"}
L1R = lambda c, n, title: {"kind": "web", "provider": "edu-arena 예체능 레벨1", "title": f"챕터 {n} {title}", "url": f"browse.html?c={c}#ch{n:02d}", "part": "레벨1 복습"}
G2R = lambda t, s, u, title: {"kind": "web", "provider": "예체능 레벨2", "title": title, "url": f"guide.html?lv=2&t={t}&s={s}" + (f"&u={u}" if u else ""), "part": "함께 볼 단원"}
G3R = lambda t, s, u, title: {"kind": "web", "provider": "예체능 레벨3", "title": title, "url": f"guide.html?lv=3&t={t}&s={s}" + (f"&u={u}" if u else ""), "part": "함께 볼 단원"}
G2 = lambda t, s, title: {"title": f"레벨2 · {title}", "href": f"guide.html?lv=2&t={t}&s={s}"}
G3 = lambda t, s, title: {"title": f"레벨3 · {title}", "href": f"guide.html?lv=3&t={t}&s={s}"}


def book(provider, title):
    return {"kind": "book", "provider": provider, "title": title}


def R(base, part):
    d = dict(base); d["part"] = part; return d


L2NOTE = "레벨 2 (응용, 전문대졸·대학 1~2학년 수준). 목차 검증 기준: {}."
L3NOTE = "레벨 3 (심화, 대졸·학부 전공 수준). 목차 검증 기준: {}. 레벨3은 단원당 학습 조언 1문단, 자가점검 3문항의 가벼운 형식이며 전공서와 작품(악보·작품·현장)을 직접 다루는 것을 전제로 합니다."


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
