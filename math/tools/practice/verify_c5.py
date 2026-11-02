"""코스5: 경우의 수·확률 문항을 완전탐색으로 독립 검산"""
import json, re, sys, glob
from itertools import permutations, product, combinations
from fractions import Fraction as F
from math import comb
ok = bad = 0
def chk(c, f, q, info=""):
    global ok, bad
    if c: ok += 1
    else: bad += 1; print("BAD", f.split("level1/")[1], q["id"], q["prompt"][:90], info)
def A(q): return F(q["answer"].replace("−", "-"))
def circ(n, cond):
    """원순열: 0번을 0자리에 고정하고 나머지 배열"""
    c = 0
    for p in permutations(range(1, n)):
        seat = (0,) + p
        if cond(seat, n): c += 1
    return c
def adj(seat, n, a, b): i, j = seat.index(a), seat.index(b); return (i - j) % n in (1, n - 1)
for f in sorted(glob.glob(sys.argv[1])):
    for q in json.load(open(f))["questions"]:
        p = q["prompt"]
        try:
            if (m := re.match(r"(\d)명이 원탁에 앉는 방법은", p)): chk(circ(int(m[1]), lambda s, n: True) == A(q), f, q); continue
            if (m := re.match(r"(\d)명이 원탁에 앉을 때 A와 B가 이웃하(는|지 않는)", p)):
                n = int(m[1]); chk(circ(n, lambda s, n: adj(s, n, 0, 1) == (m[2] == "는")) == A(q), f, q); continue
            if (m := re.match(r"(\d+)명이 원탁에 같은 간격으로 앉을 때 A와 B가 서로 마주", p)):
                n = int(m[1]); chk(circ(n, lambda s, n: (s.index(0) - s.index(1)) % n == n // 2) == A(q), f, q); continue
            if (m := re.match(r"남자 (\d)명, 여자 (\d)명이 원탁에 교대로", p)):
                k = int(m[1]); chk(circ(2 * k, lambda s, n: all((s[i] < k) != (s[(i + 1) % n] < k) for i in range(n))) == A(q), f, q); continue
            if (m := re.match(r"([A-Z]+)의 \d+글자를 일렬로", p)): chk(len(set(permutations(m[1]))) == A(q), f, q); continue
            if (m := re.match(r"(\d)명을 일렬로 세울 때 A와 B 사이에 정확히 (\d)명", p)):
                n, k = int(m[1]), int(m[2]); chk(sum(1 for s in permutations(range(n)) if abs(s.index(0) - s.index(1)) == k + 1) == A(q), f, q); continue
            if (m := re.match(r"동전 (\d)개를 던질 때 적어도 한 개가 앞면", p)):
                n = int(m[1]); v = F(sum(1 for t in product([0, 1], repeat=n) if any(t)), 2 ** n); chk(v == A(q), f, q); continue
            if (m := re.match(r"주사위를 (\d)번 던질 때 (6의 눈|짝수|3의 배수의 눈)이? 적어도 한 번", p)):
                n = int(m[1]); g = {"6의 눈": lambda x: x == 6, "짝수": lambda x: x % 2 == 0, "3의 배수의 눈": lambda x: x % 3 == 0}[m[2]]
                v = F(sum(1 for t in product(range(1, 7), repeat=n) if any(g(x) for x in t)), 6 ** n); chk(v == A(q), f, q, v); continue
            if (m := re.match(r"흰 공 (\d)개, 검은 공 (\d)개 중 (\d)개를 (?:동시에 )?뽑을 때 (모두 흰 공|흰 공이 정확히 1개|적어도 한 개가 흰 공)", p)):
                w, b, k = map(int, m.groups()[:3]); balls = ["w"] * w + ["b"] * b; cs = list(combinations(range(w + b), k))
                g = {"모두 흰 공": lambda c: all(balls[i] == "w" for i in c), "흰 공이 정확히 1개": lambda c: sum(balls[i] == "w" for i in c) == 1, "적어도 한 개가 흰 공": lambda c: any(balls[i] == "w" for i in c)}[m[4]]
                chk(F(sum(1 for c in cs if g(c)), len(cs)) == A(q), f, q); continue
            if (m := re.match(r"흰 공 (\d)개, 검은 공 (\d)개에서 한 개씩 두 번 꺼낼 때\(넣지 않음\) (.+?) 확률", p)):
                w, b = int(m[1]), int(m[2]); balls = ["w"] * w + ["b"] * b; ps = list(permutations(range(w + b), 2))
                g = {"두 번 모두 흰 공일": lambda t: balls[t[0]] == balls[t[1]] == "w", "첫 번째는 흰 공, 두 번째는 검은 공일": lambda t: (balls[t[0]], balls[t[1]]) == ("w", "b"), "두 번째 공이 흰 공일": lambda t: balls[t[1]] == "w"}[m[3]]
                chk(F(sum(1 for t in ps if g(t)), len(ps)) == A(q), f, q); continue
            if (m := re.match(r"(.+?)이 나올 확률이 (\d/\d)인 시행을 (\d)번 할 때 정확히 (\d)번", p)):
                pp, n, k = F(m[2]), int(m[3]), int(m[4]); v = sum(pp ** sum(t) * (1 - pp) ** (n - sum(t)) for t in product([0, 1], repeat=n) if sum(t) == k); chk(v == A(q), f, q); continue
            if (m := re.match(r"원점에서 출발해 동전을 던져.+?(\d)번 던진 뒤 점의 위치가 (−?\d)", p)):
                n, pos = int(m[1]), int(m[2].replace("−", "-")); chk(F(sum(1 for t in product([1, -1], repeat=n) if sum(t) == pos), 2 ** n) == A(q), f, q); continue
            if (m := re.match(r"(.+?) = (\d+)를 만족하는 (음이 아닌 정수해|자연수해)", p)):
                vs = m[1].split(" + "); s_ = int(m[2]); lo = 0 if "음이" in m[3] else 1
                chk(sum(1 for t in product(range(lo, s_ + 1), repeat=len(vs)) if sum(t) == s_) == A(q), f, q); continue
            if (m := re.match(r"(\d)명의 생일 (요일|달)이 적어도 두 명 같을", p)):
                n, d = int(m[1]), 7 if m[2] == "요일" else 12; chk(F(sum(1 for t in product(range(d), repeat=n) if len(set(t)) < n), d ** n) == A(q), f, q); continue
        except Exception as e:
            print("ERR", f, q["id"], e)
print("코스5 검산", ok, "불일치", bad)
