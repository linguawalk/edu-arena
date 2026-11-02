"""빌드 기준보다 짧은 풀이를 찾아 출력한다. 사용: python3 tools/short_expl.py tools/lessons/파일.py"""
import importlib.util, sys
spec = importlib.util.spec_from_file_location("m", sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
GR = {"numeric", "fill_blank", "ordering", "diagram"}
def bad(q):
    ex = q.get("explanation") or ""
    return q.get("qtype") in GR and (len(ex.replace("\n", "")) < 60 or len([l for l in ex.split("\n") if l.strip()]) < 3)
for k, L in enumerate(m.LESSONS, 1):
    for i, s in enumerate(L["screens"], 1):
        if s["type"] == "question" and bad(s): print(f"L{k} #{i}: {s['explanation']!r}")
for i, (_, q) in enumerate(m.REVIEW["questions"], 1):
    if bad(q): print(f"R #{i}: {q['explanation']!r}")
