"""레슨 추가 검사: 서술형 모범 답안이 채점 기준을 통과하는지, 빈칸 정답이 지문에 노출되는지.
사용: python3 tools/lint.py [content 경로]"""
import json, glob, re, os, sys


def norm(s):
    s = re.sub(r"\([^)]*[一-鿿][^)]*\)", "", str(s).strip())
    s = re.sub(r"[·ㆍ'\"“”‘’「」『』]", "", s).lower()
    return re.sub(r"\s+", "", s)


root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "content")
bad = 0
for p in sorted(glob.glob(os.path.join(root, "level1", "c*", "ch*", "*.json"))):
    if p.endswith("chapter.json"): continue
    d = json.load(open(p, encoding="utf-8"))
    for q in d.get("screens") or d.get("questions") or []:
        if q.get("type") != "question": continue
        where = f"{os.path.relpath(p, root)} {q['id']}"
        if q["qtype"] == "written":
            m, r = norm(q["model_answer"]), q["rubric"]
            hit = sum(any(norm(k) in m for k in g) for g in r["keyword_groups"])
            if hit < r["min_groups_matched"]: print("서술형 기준 미달", where); bad += 1
        if q["qtype"] == "fill_blank":
            shown = norm(re.sub(r"\{\{\d+\}\}", "", q["prompt"]))
            for b in q["blanks"]:
                for a in b["answers"]:
                    if len(norm(a)) >= 2 and norm(a) in shown: print("정답 노출", where, a); bad += 1
                # 한자 과목: 한 글자 음·뜻 답이 지문의 한글에 그대로 보이는지
                a0 = norm(b["answers"][0])
                if "/c3/" in p or "/c4/" in p:
                    if len(a0) == 1 and re.match(r"[가-힣]", a0) and a0 in shown: print("한 글자 정답 노출", where, a0); bad += 1
print("문제", bad)
sys.exit(1 if bad else 0)
