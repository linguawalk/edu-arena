"""경우의 수·집합·행렬·복소수 문항을 완전탐색/sympy로 독립 검산"""
import json, re, sys, glob
from itertools import permutations, product
from math import comb, perm, factorial
import sympy as sp
from verify import tosym, x
def num(s): return int(s.replace("−", "-"))
def mat(t): return [[num(v) for v in row.split()] for row in t.strip("[]").split(";")]
ok = bad = 0
def chk(cond, f, q, info=""):
    global ok, bad
    if cond: ok += 1
    else: bad += 1; print("BAD", f, q["id"], q["prompt"][:90], info)
for f in sorted(glob.glob(sys.argv[1])):
    for q in json.load(open(f))["questions"]:
        p = q["prompt"]; a = q.get("answer")
        try:
            if (mt := re.match(r"(\d+)C(\d+)의 값은", p)): chk(comb(int(mt[1]), int(mt[2])) == int(a), f, q); continue
            if (mt := re.match(r"(\d+)P(\d+)의 값은", p)): chk(perm(int(mt[1]), int(mt[2])) == int(a), f, q); continue
            if (mt := re.match(r"(\d+)!의 값은", p)): chk(factorial(int(mt[1])) == int(a), f, q); continue
            if (mt := re.match(r"([A-Z]+)의 \d+글자를 일렬로 늘어놓는 방법은", p)): chk(len(set(permutations(mt[1]))) == int(a), f, q); continue
            if (mt := re.match(r"([A-Z]+)의 글자를 일렬로 늘어놓을 때 ([A-Z])[이가] ([A-Z])보다 앞", p)):
                w = mt[1]; chk(sum(1 for t in permutations(w) if t.index(mt[2]) < t.index(mt[3])) == int(a), f, q); continue
            if (mt := re.match(r"가로로 (\d+)칸, 세로로 (\d+)칸", p)):
                A, B = int(mt[1]), int(mt[2]); chk(len(set(permutations("R" * A + "U" * B))) == int(a), f, q); continue
            if (mt := re.match(r"x \+ y \+ z = (\d+)를 만족하는 (음이 아닌 정수해|자연수해)", p)):
                k = int(mt[1]); lo = 0 if "음이" in mt[2] else 1
                chk(sum(1 for u in range(lo, k + 1) for v in range(lo, k + 1) if k - u - v >= lo) == int(a), f, q); continue
            if (mt := re.match(r"(\d+)의 약수는 몇 개", p)): n = int(mt[1]); chk(sum(n % d == 0 for d in range(1, n + 1)) == int(a), f, q); continue
            if (mt := re.match(r"1부터 (\d+)까지 자연수 중 (\d+)의 배수 또는 (\d+)의 배수", p)):
                N, P_, Q = map(int, mt.groups()); chk(sum(1 for z in range(1, N + 1) if z % P_ == 0 or z % Q == 0) == int(a), f, q); continue
            if (mt := re.match(r"1부터 (\d+)까지 자연수 중 (\d+)의 배수도 (\d+)의 배수도 아닌", p)):
                N, P_, Q = map(int, mt.groups()); chk(sum(1 for z in range(1, N + 1) if z % P_ and z % Q) == int(a), f, q); continue
            if (mt := re.match(r"1부터 (\d+)까지 자연수 중 (\d+), (\d+), (\d+) 중 적어도", p)):
                N, *ps = map(int, mt.groups()); chk(sum(1 for z in range(1, N + 1) if any(z % t == 0 for t in ps)) == int(a), f, q); continue
            if (mt := re.match(r"A, B를 포함한 (\d+)명을 일렬로 세울 때 A와 B가 (이웃하는|이웃하지 않는)", p)):
                n = int(mt[1]); c = sum(1 for t in permutations(range(n)) if (abs(t.index(0) - t.index(1)) == 1) == (mt[2] == "이웃하는"))
                chk(c == int(a), f, q); continue
            if (mt := re.match(r"남자 (\d+)명, 여자 (\d+)명을 일렬로 세울 때 여자끼리 이웃하지 않는", p)):
                b, g = int(mt[1]), int(mt[2]); n = b + g
                c = sum(1 for t in permutations(range(n)) if all(not (t[i] >= b and t[i + 1] >= b) for i in range(n - 1)))
                chk(c == int(a), f, q); continue
            if (mt := re.match(r"(\d+)명이 원탁에 앉을 때 특정한 2명이 이웃", p)):
                n = int(mt[1]); c = sum(1 for t in permutations(range(1, n)) if abs(((0,) + t).index(1) - 0) in (1, n - 1)) if n <= 8 else None
                chk(c == int(a), f, q); continue
            if (mt := re.match(r"(.+?)일 때 x \+ y의 값은\? \(x, y는 실수\)", p)): ok += 0
            if (mt := re.match(r"A = (\[[^\]]+\])일 때 ad − bc의 값은", p)):
                A = mat(mt[1]); chk(A[0][0] * A[1][1] - A[0][1] * A[1][0] == int(a), f, q); continue
            if q["qtype"] == "fill_blank" and (mt := re.match(r"(\[[^\]]+\])(\[[^\]]+\]) = (\[.+\])$", p)):
                A, B = mat(mt[1]), mat(mt[2]); C = (sp.Matrix(A) * sp.Matrix(B)).tolist()
                tgt = mt[3].replace("{{1}}", q["blanks"][0]["answers"][0]); chk(C == mat(tgt), f, q); continue
            if q["qtype"] == "fill_blank" and (mt := re.match(r"\((.+?)\)(?: ([+−÷]) |)\((.+?)\) = \{\{1\}\} \+ \{\{2\}\}i$", p)):
                I = sp.I
                def cz(t): return tosym(t.replace("i", "*I").replace(" *I", " 1*I").replace("−*I", "−1*I").replace("+ *I", "+ 1*I")) if False else sp.sympify(re.sub(r"(\d)i", r"\1*I", t.replace("−", "-")).replace("- i", "- I").replace("+ i", "+ I").replace("i", "I"))
                L_, op, R_ = cz(mt[1]), mt[2] or "×", cz(mt[3])
                v = sp.expand({"+": L_ + R_, "−": L_ - R_, "÷": L_ / R_, "×": L_ * R_}[op]); v = sp.nsimplify(sp.simplify(v))
                want = sp.Rational(q["blanks"][0]["answers"][0]) + sp.Rational(q["blanks"][1]["answers"][0]) * I
                chk(sp.simplify(v - want) == 0, f, q, v); continue
            if (mt := re.match(r"\|x([^|]*)\| ([<≤]) (\d+)[을를] 만족하는 정수 x는 몇 개", p)):
                e = tosym("x" + mt[1]); k = int(mt[3]); s_ = mt[2]
                c = sum(1 for z in range(-60, 61) if (abs(e.subs(x, z)) < k if s_ == "<" else abs(e.subs(x, z)) <= k))
                chk(c == int(a), f, q); continue
        except Exception as e:
            print("ERR", f, q["id"], e)
print("완전탐색 검산", ok, "불일치", bad)
