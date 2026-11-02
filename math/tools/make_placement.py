"""진입 진단 테스트 빌드.

1) content/level1/placement.json: 챕터마다 진단에 쓸 문항 풀
   - 출처: 각 챕터의 review.json (복습 세트)
   - 제외: 서술형, 앞 문항에 기대는 문항("같은 X에서…"), 그림 없이 그림을 언급하는 문항
   - 순서: '그렇다/아니다'처럼 찍기 쉬운 문항은 뒤로
2) placement.html: player.html의 공용 구간(==KIT-START== ~ ==KIT-END==)과 스타일을
   placement_tpl.html에 끼워 넣어 생성. 플레이어를 고치면 이 스크립트만 다시 실행.

사용: python3 make_placement.py [사이트 경로]
"""
import json, os, re, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SITE = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/site"
HERE = os.path.dirname(os.path.abspath(__file__))
L1 = os.path.join(SITE, "content", "level1")

CORE = ["c0", "c1", "c2", "c3", "c4"]
ELECTIVE = ["c5", "c6"]
PER_CHAPTER = 5
DEP = re.compile(r"^(같은|그 |그때|이때|위 |앞)|같은 (조건|경우|상황|분포|운동|X|함수|f|쌍곡선|타원|포물선|구|궤도|삼각형|사각뿔|원|직선|곡선|표본|시험|정사각뿔|게임)")
BINARY = re.compile(r"\(그렇다 1|\(양수 1|번호\)")


def usable(q):
    if q.get("qtype") == "written":
        return False
    p = q.get("prompt", "")
    if DEP.search(p):
        return False
    if "그림" in p and not q.get("figure") and q.get("qtype") != "diagram":
        return False
    return True


def build_pool():
    courses = json.load(open(os.path.join(L1, "courses.json"), encoding="utf-8"))["courses"]
    out = {"schema_version": "1.0", "level": 1, "core": CORE, "elective": ELECTIVE,
           "pass_rate": 0.7, "courses": []}
    total = 0
    for c in courses:
        if c["id"] not in CORE + ELECTIVE:
            continue
        cj = json.load(open(os.path.join(L1, c["id"], "course.json"), encoding="utf-8"))
        chs = []
        for chm in cj["chapters"]:
            d = os.path.join(L1, c["id"], chm["dir"])
            rv = json.load(open(os.path.join(d, "review.json"), encoding="utf-8"))
            qs = [q for q in rv["questions"] if usable(q)]
            qs.sort(key=lambda q: 1 if BINARY.search(q.get("prompt", "")) else 0)
            qs = qs[:PER_CHAPTER]
            if not qs:
                raise SystemExit(f"진단 문항 없음: {c['id']} {chm['dir']}")
            for q in qs:
                q = dict(q)
            chs.append({"no": chm["no"], "dir": chm["dir"], "id": chm["id"], "title": chm["title"],
                        "review_id": rv["review"]["id"],
                        "questions": [dict(q, stage="diagnostic") for q in qs]})
            total += len(qs)
        out["courses"].append({"id": c["id"], "title": c["title"], "description": c["description"],
                               "chapters": chs})
    path = os.path.join(L1, "placement.json")
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return path, total, sum(len(c["chapters"]) for c in out["courses"])


def build_page():
    from kit import render
    player = open(os.path.join(SITE, "player.html"), encoding="utf-8").read()
    tpl = open(os.path.join(HERE, "placement_tpl.html"), encoding="utf-8").read()
    page = render(tpl, player)
    path = os.path.join(SITE, "placement.html")
    open(path, "w", encoding="utf-8").write(page)
    return path, len(page)


if __name__ == "__main__":
    p, n, chs = build_pool()
    print(f"문항 풀: {p} ({chs}개 챕터, {n}문항)")
    p, size = build_page()
    print(f"진단 페이지: {p} ({size:,}바이트)")
