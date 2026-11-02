"""빌더의 레슨별 화면·문항·예제 수를 빌드 없이 확인한다. 사용: python3 tools/count.py tools/build_c1_ch04.py"""
import sys, os, re
sys.path.insert(0, os.path.dirname(__file__))
src = open(sys.argv[1], encoding="utf-8").read()
src = re.sub(r"\nrun\(", "\n_run_ = (", src)
ns = {}; exec(compile(src, sys.argv[1], "exec"), ns)
for k in sorted(x for x in ns if re.fullmatch(r"L\d", x)):
    sc = ns[k]["screens"]; q = sum(s["type"] == "question" for s in sc); e = sum(s["type"] == "example" for s in sc)
    ok = 20 <= len(sc) <= 24 and 15 <= q <= 17 and e == 3
    print(k, "화면", len(sc), "문항", q, "예제", e, "설명", sum(s["type"] == "explain" for s in sc), "" if ok else "  <-- 확인")
print("복습", len(ns["REVIEW"]))
allq = [s for k in ns if re.fullmatch(r"L\d", k) for s in ns[k]["screens"] if s["type"] == "question"] + ns["REVIEW"]
for q in allq:
    if q["qtype"] != "written" and len(q.get("explanation") or "") < 20: print("  풀이 짧음:", q["id"], q["explanation"])
    if q["qtype"] == "fill_blank" and q["prompt"].count("{{") != len(q["blanks"]): print("  빈칸 수:", q["id"])
    if q["qtype"] == "journal":
        a = q["answer"]
        if sum(n for _, n in a["debit"]) != sum(n for _, n in a["credit"]): print("  대차 불일치:", q["id"])
        if {x for x, _ in a["debit"] + a["credit"]} - set(q["accounts"]): print("  선택지 계정 누락:", q["id"])
