"""코스 5 · 확률과 통계 — 연습 문제 은행 (답은 가능한 한 완전탐색으로 계산)"""
from core import *
from math import comb, perm, factorial
from itertools import product, permutations, combinations
from collections import Counter

def nz(r, a, b):
    while True:
        v = r.randint(a, b)
        if v: return v
def nf(v, prompt, expl, hint):
    v = F(v)
    return num(prompt, v, expl, hint, fmt="fraction" if v.denominator > 1 else "integer")
def dec(v, prompt, expl, hint, tol=0):
    q = num(prompt, f"{float(v):.8f}".rstrip("0").rstrip("."), expl, hint, fmt="decimal")
    if tol: q["tolerance"] = tol
    return q
def C(n, k): return f"{n}C{k}"
Z = {0.5: .1915, 1: .3413, 1.5: .4332, 2: .4772, 2.5: .4938, 3: .4987}
def zt(*zs): return "(표: " + ", ".join(f"P(0 ≤ Z ≤ {z:g}) = {Z[z]:.4f}" for z in zs) + ")"

# ================= ch01 순열 =================
def a1_circ(r):
    n = r.randint(4, 8); t = r.choice(["basic", "adj", "nonadj", "alt"])
    if t == "basic": return nf(factorial(n - 1), f"{n}명이 원탁에 앉는 방법은?", f"원순열: 회전하여 같은 것은 하나로 봅니다.\n({n} − 1)! = {n - 1}! = {factorial(n - 1)}", "원순열은 (n − 1)!")
    if t == "adj": return nf(2 * factorial(n - 2), f"{n}명이 원탁에 앉을 때 A와 B가 이웃하는 방법은?", f"A, B를 한 묶음 → {n - 1}개의 원순열 {n - 2}! = {factorial(n - 2)}\n묶음 안에서 자리 바꾸기 2\n{factorial(n - 2)} × 2 = {2 * factorial(n - 2)}", "묶어서 원순열")
    if t == "nonadj": return nf(factorial(n - 1) - 2 * factorial(n - 2), f"{n}명이 원탁에 앉을 때 A와 B가 이웃하지 않는 방법은?", f"전체 {n - 1}! = {factorial(n - 1)}\n이웃하는 경우 2 × {n - 2}! = {2 * factorial(n - 2)}\n{factorial(n - 1)} − {2 * factorial(n - 2)} = {factorial(n - 1) - 2 * factorial(n - 2)}", "전체 − 이웃하는 경우")
    k = r.randint(2, 4)
    return nf(factorial(k - 1) * factorial(k), f"남자 {k}명, 여자 {k}명이 원탁에 교대로 앉는 방법은?", f"남자 {k}명을 원탁에 앉히기 ({k} − 1)! = {factorial(k - 1)}\n남자 사이 {k}자리에 여자 배치 {k}! = {factorial(k)}\n{factorial(k - 1)} × {factorial(k)} = {factorial(k - 1) * factorial(k)}", "한쪽을 먼저 원형으로")
def a1_table(r):
    s, p = r.choice([(4, 2), (3, 2), (4, 1), (3, 3), (6, 1), (5, 2), (5, 1), (4, 3), (3, 4), (6, 2), (3, 1), (5, 3)])
    n = s * p
    return nf(factorial(n - 1) * p, f"정{'사각형' if s == 4 else '삼각형' if s == 3 else '육각형' if s == 6 else '오각형'} 탁자의 각 변에 {p}명씩 {n}명이 앉는 방법은?",
              f"원순열 ({n} − 1)! = {factorial(n - 1)}\n회전해도 겹치지 않는 시작 위치가 한 변에 {p}가지\n{factorial(n - 1)} × {p} = {factorial(n - 1) * p}", "원순열 × (한 변의 자리 수)")
def a1_neck(r):
    n = r.randint(4, 8)
    return nf(factorial(n - 1) // 2, f"서로 다른 구슬 {n}개로 만드는 목걸이는 몇 가지일까요? (뒤집어서 같은 것은 하나로)", f"원순열 ({n} − 1)! = {factorial(n - 1)}\n뒤집기로 같은 것이 2개씩 → ÷ 2 = {factorial(n - 1) // 2}", "목걸이 = 원순열 ÷ 2")
def a1_opp(r):
    n = 2 * r.randint(2, 5); t = r.choice(["opp", "fix"])
    if t == "opp": return nf(factorial(n - 2), f"{n}명이 원탁에 같은 간격으로 앉을 때 A와 B가 서로 마주 보는 방법은?", f"A를 먼저 앉히면(회전 고려 1가지) B의 자리는 맞은편으로 정해짐\n나머지 {n - 2}명 배열 {n - 2}! = {factorial(n - 2)}", "한 사람을 고정하세요.")
    k = r.randint(2, 4)
    return nf(factorial(n - k) * factorial(k), f"{n}명이 원탁에 앉을 때 특정한 {k}명이 모두 이웃하는 방법은?", f"{k}명을 한 묶음 → {n - k + 1}개의 원순열 ({n - k})! = {factorial(n - k)}\n묶음 안 배열 {k}! = {factorial(k)}\n곱 {factorial(n - k) * factorial(k)}", "묶음으로 원순열")
L11 = [("원순열", a1_circ), ("다각형 탁자", a1_table), ("목걸이", a1_neck), ("마주 보기·묶음", a1_opp)]

def a2_pi(r):
    n, k = r.randint(2, 5), r.randint(2, 5)
    t = r.choice(["val", "func", "num"])
    if t == "val": return nf(n ** k, f"{n}Π{k}의 값은?  (서로 다른 {n}개에서 중복을 허락해 {k}개를 택하는 순열)", f"{n}Π{k} = {n}{sup(k)} = {n ** k}", "nΠr = nʳ")
    if t == "func": return nf(k ** n, f"원소가 {n}개인 집합 X에서 원소가 {k}개인 집합 Y로의 함수는 몇 개일까요?", f"X의 각 원소마다 Y의 원소 {k}개 중 하나 → {k}{sup(n)} = {k ** n}", "중복순열")
    d = r.randint(3, 5); L_ = r.randint(3, 4)
    return nf(d ** L_, f"1부터 {d}까지의 숫자로 만들 수 있는 {L_}자리 수는? (같은 숫자 사용 가능)", f"각 자리에 {d}가지 → {d}{sup(L_)} = {d ** L_}", "자리마다 독립")
def a2_zero(r):
    d, L_ = r.randint(3, 5), r.randint(3, 4)
    v = (d - 1) * d ** (L_ - 1)
    return nf(v, f"0부터 {d - 1}까지의 숫자로 만들 수 있는 {L_}자리 수는? (같은 숫자 사용 가능)", f"맨 앞자리: 0 제외 {d - 1}가지, 나머지 {L_ - 1}자리: {d}가지씩\n{d - 1} × {d}{sup(L_ - 1)} = {v}", "맨 앞에 0이 올 수 없습니다.")
def a2_even(r):
    d, L_ = r.randint(4, 7), r.randint(2, 4)
    ev = d // 2
    v = d ** (L_ - 1) * ev
    return nf(v, f"1부터 {d}까지의 숫자로 만들 수 있는 {L_}자리 짝수는? (같은 숫자 사용 가능)", f"일의 자리 짝수 {ev}가지, 나머지 {L_ - 1}자리 {d}가지씩\n{d}{sup(L_ - 1)} × {ev} = {v}", "일의 자리를 먼저")
def a2_flag(r):
    k, m_ = r.randint(2, 4), r.randint(2, 4)
    v = sum(k ** i for i in range(1, m_ + 1))
    return nf(v, f"서로 다른 깃발 {k}종류를 1개에서 {m_}개까지 일렬로 세워 만드는 신호는 몇 가지일까요? (같은 종류 반복 가능)", f"1개 ~ {m_}개 각각 중복순열을 더함\n" + " + ".join(f"{k}{sup(i)}" for i in range(1, m_ + 1)) + f" = {v}", "개수별로 나누어 더하세요.")
L12 = [("중복순열의 값", a2_pi), ("0이 있는 수", a2_zero), ("짝수 만들기", a2_even), ("신호 만들기", a2_flag)]

WORDS = ["SUCCESS", "BANANA", "LETTER", "COFFEE", "APPLE", "MAMMAL", "PEPPER", "BOOKKEEPER"[:7], "STATS", "LEVEL", "RADAR", "TOMATO", "SEESAW"]
def a3_word(r):
    w = r.choice(WORDS); c = Counter(w); v = factorial(len(w))
    for x in c.values(): v //= factorial(x)
    return nf(v, f"{w}의 {len(w)}글자를 일렬로 늘어놓는 방법은?", f"{len(w)}! ÷ (" + " × ".join(f"{x}!" for x in c.values() if x > 1) + f") = {factorial(len(w))} ÷ {factorial(len(w)) // v} = {v}\n(" + ", ".join(f"{k} {x}개" for k, x in c.items() if x > 1) + ")", "같은 것이 있는 순열")
def a3_order(r):
    n, k = r.randint(4, 7), r.randint(2, 4)
    if k >= n: return None
    v = factorial(n) // factorial(k)
    return nf(v, f"1부터 {n}까지의 수를 일렬로 늘어놓을 때 1, 2, …, {k}가 이 순서대로 오는 방법은?".replace(", …, 2", "").replace("1, 2, …, 3", "1, 2, 3"), f"1~{k}을 모두 같은 문자로 보고 늘어놓은 뒤 순서대로 채움\n{n}! ÷ {k}! = {v}", "순서가 정해진 것은 같은 것으로")
def a3_path(r):
    a, b = r.randint(3, 6), r.randint(2, 5); p, q = r.randint(1, a - 1), r.randint(1, b - 1)
    t = r.choice(["all", "via", "avoid"])
    tot = comb(a + b, a); via = comb(p + q, p) * comb(a - p + b - q, a - p)
    if t == "all": return nf(tot, f"오른쪽으로 {a}칸, 위쪽으로 {b}칸 가는 최단 경로는 몇 가지일까요?", f"→ {a}개, ↑ {b}개의 배열: ({a + b})!/({a}!{b}!) = {tot}", "같은 것이 있는 순열")
    if t == "via": return nf(via, f"오른쪽 {a}칸, 위쪽 {b}칸 가는 최단 경로 중 출발점에서 오른쪽 {p}칸, 위쪽 {q}칸인 점 P를 지나는 경로는?", f"출발 → P: {C(p + q, p)} = {comb(p + q, p)}\nP → 도착: {C(a - p + b - q, a - p)} = {comb(a - p + b - q, a - p)}\n곱 {via}", "두 구간으로 나누어 곱하세요.")
    return nf(tot - via, f"오른쪽 {a}칸, 위쪽 {b}칸 가는 최단 경로 중 출발점에서 오른쪽 {p}칸, 위쪽 {q}칸인 점 P를 지나지 않는 경로는?", f"전체 {tot} − P를 지나는 {via} = {tot - via}", "전체 − 지나는 경로")
def a3_digits(r):
    ds = sorted(r.choices([0, 1, 2, 3], k=r.randint(4, 5)))
    if len(set(ds)) < 2: return None
    v = len({p for p in set(permutations(ds)) if p[0] != 0})
    if v < 3: return None
    return nf(v, f"{', '.join(map(str, ds))}를 모두 써서 만드는 {len(ds)}자리 수는 몇 개일까요?", f"같은 것이 있는 순열로 전체 배열을 센 뒤 맨 앞이 0인 경우를 뺍니다.\n결과 {v}개" if 0 in ds else f"같은 것이 있는 순열: {len(ds)}! ÷ (같은 숫자 개수의 계승들의 곱) = {v}", "같은 숫자는 바꿔도 같은 수")
L13 = [("같은 글자 배열", a3_word), ("순서가 정해진 배열", a3_order), ("최단 경로", a3_path), ("같은 숫자로 수 만들기", a3_digits)]

def a4_mult(r):
    ds = list(range(0, r.randint(5, 6))); L_ = r.choice([3, 4]); k = r.choice([5, 2, 3])
    nums = [p for p in permutations(ds, L_) if p[0] != 0 and int("".join(map(str, p))) % k == 0]
    return nf(len(nums), f"{', '.join(map(str, ds))}로 만드는 {L_}자리 수 중 {k}의 배수는? (같은 숫자 사용 불가)", f"{k}의 배수 조건(" + {5: "일의 자리 0 또는 5", 2: "일의 자리 짝수", 3: "각 자리 숫자의 합이 3의 배수"}[k] + f")으로 경우를 나누어 셉니다.\n(맨 앞자리 0 제외) → {len(nums)}개", "끝자리 또는 자리 합으로 나누어 세세요.")
def a4_rank(r):
    w = sorted(r.sample("abcdef", r.randint(4, 5))); tgt = list(w); r.shuffle(tgt)
    allp = sorted(permutations(w)); v = allp.index(tuple(tgt)) + 1
    return nf(v, f"{', '.join(w)}를 한 번씩 써서 사전식으로 늘어놓을 때 {''.join(tgt)}는 몇 번째일까요?", f"앞자리부터 {''.join(tgt)}보다 앞서는 배열을 셉니다.\n" + " + ".join(f"{sorted(set(w) - set(tgt[:i])).index(tgt[i])}×{len(w) - 1 - i}!" for i in range(len(w) - 1)) + f" + 1 = {v}", "앞자리가 더 작은 것부터 세세요.")
def a4_between(r):
    n, k = r.randint(5, 7), r.randint(1, 2)
    v = sum(1 for p in permutations(range(n)) if abs(p.index(0) - p.index(1)) == k + 1)
    return nf(v, f"{n}명을 일렬로 세울 때 A와 B 사이에 정확히 {k}명이 서는 방법은?", f"A, B와 사이의 {k}명을 한 묶음: 사이 {k}명 고르기·배열 {perm(n - 2, k)}, A·B 순서 2\n묶음과 나머지 {n - k - 2}명 배열 {n - k - 1}!\n{perm(n - 2, k)} × 2 × {factorial(n - k - 1)} = {v}", "묶음으로 보세요.")
def a4_alt(r):
    k = r.randint(2, 4); same = r.choice([True, False])
    if same: return nf(2 * factorial(k) ** 2, f"남자 {k}명, 여자 {k}명을 일렬로 교대로 세우는 방법은?", f"남·여 중 누가 먼저인지 2가지\n남자 배열 {k}!, 여자 배열 {k}!\n2 × {factorial(k)} × {factorial(k)} = {2 * factorial(k) ** 2}", "시작 성별 2가지")
    return nf(factorial(k + 1) * factorial(k), f"남자 {k + 1}명, 여자 {k}명을 일렬로 교대로 세우는 방법은?", f"남자가 양 끝에 와야 합니다(남여남…남).\n{k + 1}! × {k}! = {factorial(k + 1) * factorial(k)}", "인원이 많은 쪽이 양 끝")
L14 = [("배수 만들기", a4_mult), ("사전식 순서", a4_rank), ("사이에 끼우기", a4_between), ("교대로 세우기", a4_alt)]

# ================= ch02 조합 =================
def b1_H(r):
    n, k = r.randint(2, 5), r.randint(2, 7)
    t = r.choice(["val", "eq0", "eq1", "ball"])
    if t == "val": return nf(comb(n + k - 1, k), f"{n}H{k}의 값은?  (서로 다른 {n}개에서 중복을 허락해 {k}개를 택하는 조합)", f"nHr = (n + r − 1)Cr\n{n}H{k} = {C(n + k - 1, k)} = {comb(n + k - 1, k)}", "nHr = (n + r − 1)Cr")
    vs = "x + y + z + w + u"[: 4 * n - 3] if n <= 5 else None
    if n < 2: return None
    var = " + ".join("xyzwu"[:n])
    if t == "eq0":
        v = sum(1 for p in product(range(k + 1), repeat=n) if sum(p) == k)
        return nf(v, f"{var} = {k}를 만족하는 음이 아닌 정수해는 몇 쌍일까요?", f"{n}종류에서 중복을 허락해 {k}개 고르기\n{n}H{k} = {C(n + k - 1, k)} = {v}", "중복조합")
    if t == "eq1":
        if k < n: return None
        v = sum(1 for p in product(range(1, k + 1), repeat=n) if sum(p) == k)
        return nf(v, f"{var} = {k}를 만족하는 자연수해는 몇 쌍일까요?", f"각각 1씩 먼저 주고 남은 {k - n}을 나눔\n{n}H{k - n} = {C(k - 1, k - n)} = {v}", "먼저 1씩 나누어 주세요.")
    if k < n: return None
    return nf(comb(k - 1, n - 1), f"똑같은 공 {k}개를 {n}명에게 모두 1개 이상 나눠 주는 방법은?", f"1개씩 먼저 주고 남은 {k - n}개를 {n}명에게 중복을 허락해 분배\n{n}H{k - n} = {comb(k - 1, n - 1)}", "1개씩 먼저")
def b1_ineq(r):
    k = r.randint(2, 6)
    v = sum(1 for p in product(range(k + 1), repeat=3) if sum(p) <= k)
    return nf(v, f"x + y + z ≤ {k}를 만족하는 음이 아닌 정수해는 몇 쌍일까요?", f"여유 변수 w를 넣어 x + y + z + w = {k}\n4H{k} = {C(k + 3, k)} = {v}", "부등식을 등식으로")
def b1_shift(r):
    a, b, s = r.randint(0, 2), r.randint(1, 3), r.randint(6, 10)
    v = sum(1 for x in range(a, s + 1) for y in range(b, s + 1) if s - x - y >= 0)
    return nf(v, f"x ≥ {a}, y ≥ {b}, z ≥ 0이고 x + y + z = {s}인 정수해는 몇 쌍일까요?", f"x = x′ + {a}, y = y′ + {b}로 바꾸면 x′ + y′ + z = {s - a - b}\n3H{s - a - b} = {v}", "최솟값만큼 미리 빼세요.")
L21 = [("중복조합", b1_H), ("부등식의 해", b1_ineq), ("조건이 있는 해", b1_shift)]

def b2_coef(r):
    a, b, n = r.choice([1, 2, 3]), r.choice([1, 2, -1, -2, 3]), r.randint(3, 6); k = r.randint(1, n - 1)
    v = comb(n, k) * a ** k * b ** (n - k)
    return nf(v, f"({'' if a == 1 else a}x{term(b)}){sup(n)}의 전개식에서 x{sup(k) if k > 1 else ''}의 계수는?", f"일반항 {C(n, k)}({'' if a == 1 else a}x){sup(k) if k > 1 else ''}({m(b)}){sup(n - k) if n - k > 1 else ''}\n계수 {comb(n, k)} × {a ** k} × {par(b ** (n - k))} = {m(v)}", "nCr aʳ bⁿ⁻ʳ")
def b2_const(r):
    p, n = r.choice([1, 2]), r.choice([3, 4, 6, 8, 9])
    # (x^p + 1/x)^n: term C(n,k) x^{p k − (n − k)} → const when (p+1)k = n
    if n % (p + 1): return None
    k = n // (p + 1)
    return nf(comb(n, k), f"(x{sup(p) if p > 1 else ''} + 1/x){sup(n)}의 전개식에서 상수항은?", f"일반항 {C(n, 'r')}(x{sup(p) if p > 1 else ''})ʳ(1/x)ⁿ⁻ʳ, 지수 {p}r − ({n} − r) = 0 → r = {k}\n{C(n, k)} = {comb(n, k)}", "x의 지수가 0인 항")
def b2_sum(r):
    n = r.randint(3, 10); t = r.choice(["all", "alt", "odd", "coef"])
    if t == "all": return nf(2 ** n, f"{C(n, 0)} + {C(n, 1)} + … + {C(n, n)}의 값은?", f"(1 + 1)ⁿ = Σ nCr\n2{sup(n)} = {2 ** n}", "x = 1을 대입")
    if t == "alt": return nf(0, f"{C(n, 0)} − {C(n, 1)} + {C(n, 2)} − … + (−1){sup(n)}{C(n, n)}의 값은?", f"(1 − 1)ⁿ = Σ(−1)ʳ nCr = 0", "x = −1 대입")
    if t == "odd": return nf(2 ** (n - 1), f"{C(n, 1)} + {C(n, 3)} + {C(n, 5)} + …(홀수 번째 r만)의 값은?", f"짝수 r의 합 = 홀수 r의 합 = 2ⁿ ÷ 2 = 2{sup(n - 1)} = {2 ** (n - 1)}", "전체의 절반")
    a, b = r.choice([2, 3, 1]), r.choice([-1, 1, -2])
    return nf((a + b) ** n, f"({'' if a == 1 else a}x{term(b)}){sup(n)}의 전개식에서 모든 계수의 합은?", f"x = 1을 대입: ({a}{term(b)}){sup(n)} = {m((a + b) ** n)}", "x = 1 대입")
L22 = [("특정 항의 계수", b2_coef), ("상수항", b2_const), ("이항계수의 합", b2_sum)]

def b3_pas(r):
    t = r.choice(["mid", "rule", "hock", "sym", "row"])
    if t == "mid":
        n = 2 * r.randint(2, 5); return nf(comb(n, n // 2), f"파스칼의 삼각형 n = {n}인 줄의 가운데 수 {C(n, n // 2)}는?", f"파스칼의 삼각형 n번째 줄은 {C(n, 0)}, {C(n, 1)}, …, {C(n, n)}입니다.\n가운데 수 {C(n, n // 2)} = {n}!/({n // 2}! × {n // 2}!) = {comb(n, n // 2)}", "nCr 계산")
    if t == "rule":
        n, k = r.randint(4, 10), r.randint(2, 5)
        if k >= n: return None
        return fill(f"{C(n, k)} = {C(n - 1, k - 1)} + {n - 1}C{{{{1}}}}", [str(k)], f"파스칼의 법칙: nCr = (n−1)C(r−1) + (n−1)Cr\n빈칸 {k}", "바로 위 두 수의 합")
    if t == "hock":
        k, m_ = r.randint(1, 3), r.randint(4, 8)
        v = sum(comb(i, k) for i in range(k, m_ + 1))
        return nf(v, " + ".join(C(i, k) for i in range(k, m_ + 1)) + "의 값은?", f"하키스틱 성질: Σ iCr = (m + 1)C(r + 1)\n{C(m_ + 1, k + 1)} = {v}", "대각선 합은 아래 한 칸")
    if t == "sym":
        n, a = r.randint(6, 12), r.randint(1, 4); b = n - a
        if a == b: return None
        return nf(n, f"nC{a} = nC{b}일 때 n의 값은?", f"nCr = nC(n−r)이므로 {a} + {b} = n → n = {n}", "nCr = nC(n − r)")
    n = r.randint(3, 10); return nf(2 ** n, f"파스칼의 삼각형에서 n = {n}인 줄의 수를 모두 더하면?", f"Σ {n}Cr = 2{sup(n)} = {2 ** n}", "한 줄의 합 = 2ⁿ")
L23 = [("파스칼의 삼각형", b3_pas)]

def b4_group(r):
    sizes = r.choice([(2, 2, 2), (3, 2, 1), (2, 2, 1), (3, 3), (4, 2), (2, 2), (3, 1, 1), (4, 2, 2)])
    n = sum(sizes); v = factorial(n)
    for s_ in sizes: v //= factorial(s_)
    for c in Counter(sizes).values(): v //= factorial(c)
    return nf(v, f"서로 다른 {n}개를 {'개, '.join(map(str, sizes))}개의 {['', '', '두', '세'][len(sizes)]} 묶음으로 나누는 방법은?", f"차례로 고르면 " + " × ".join(C(n - sum(sizes[:i]), s_) for i, s_ in enumerate(sizes)) + "\n크기가 같은 묶음끼리는 순서를 지움 → " + str(v), "같은 크기의 묶음은 그 개수의 계승으로 나눕니다.")
def b4_deal(r):
    k, p = r.randint(2, 3), r.choice([1, 2])
    n = k * p; v = factorial(n) // factorial(p) ** k
    return nf(v, f"서로 다른 책 {n}권을 {k}명에게 {p}권씩 나눠 주는 방법은?", f"사람이 구별되므로 묶음 나누기 후 나눠 줌\n" + " × ".join(C(n - i * p, p) for i in range(k)) + f" = {v}", "받는 사람이 다르면 순서를 지우지 않음")
def b4_mono(r):
    a, b = r.randint(2, 4), r.randint(a if False else 3, 7)
    t = r.choice(["lt", "le"])
    if t == "lt":
        if a > b: return None
        return nf(comb(b, a), f"X = {{1, …, {a}}}에서 Y = {{1, …, {b}}}로의 함수 중 f(1) < f(2) < … < f({a})인 것은 몇 개일까요?".replace("f(1) < f(2) < … < f(2)", "f(1) < f(2)"), f"Y에서 서로 다른 {a}개를 고르면 크기 순으로 한 가지\n{C(b, a)} = {comb(b, a)}", "조합")
    return nf(comb(a + b - 1, a), f"X = {{1, …, {a}}}에서 Y = {{1, …, {b}}}로의 함수 중 f(1) ≤ f(2) ≤ … ≤ f({a})인 것은 몇 개일까요?".replace("f(1) ≤ f(2) ≤ … ≤ f(2)", "f(1) ≤ f(2)"), f"Y에서 중복을 허락해 {a}개 고르기\n{b}H{a} = {comb(a + b - 1, a)}", "중복조합")
def b4_part(r):
    n, k = r.randint(5, 10), r.randint(2, 3)
    def parts(n, k, mx):
        if k == 0: return 1 if n == 0 else 0
        return sum(parts(n - i, k - 1, i) for i in range(1, min(n, mx) + 1))
    v = parts(n, k, n)
    return nf(v, f"{n}을 {k}개의 자연수의 합으로 나타내는 방법은? (더하는 순서는 무시)".replace(f"{n}을", j(n, "를을")), f"큰 수부터 나열하여 빠짐없이 셉니다.\n결과 {v}가지", "큰 수부터 정리해서 세세요.")
L24 = [("묶음 나누기", b4_group), ("나눠 주기", b4_deal), ("증가함수의 개수", b4_mono), ("자연수의 분할", b4_part)]

# ================= ch03 확률 =================
DICE2 = list(product(range(1, 7), repeat=2))
def c1_cnt(r):
    t = r.choice(["sum", "prod", "diff"])
    k = r.randint(2, 12) if t == "sum" else r.choice([6, 12, 4, 8, 18]) if t == "prod" else r.randint(0, 5)
    f = {"sum": lambda p: p[0] + p[1] == k, "prod": lambda p: p[0] * p[1] == k, "diff": lambda p: abs(p[0] - p[1]) == k}[t]
    S = [p for p in DICE2 if f(p)]
    nm = {"sum": f"눈의 합이 {k}", "prod": f"눈의 곱이 {k}", "diff": f"눈의 차가 {k}"}[t]
    return nf(len(S), f"주사위 두 개를 던질 때 {nm}인 사건의 원소는 몇 개일까요?", f"{', '.join(map(str, S)) if S else '없음'}\n→ {len(S)}개", "순서쌍으로 나열하세요.")
def c1_set(r):
    A = set(r.sample(range(1, 7), r.randint(2, 4))); B = set(r.sample(range(1, 7), r.randint(2, 4)))
    t = r.choice(["and", "or", "ex", "comp"])
    s = lambda X: "{" + ", ".join(map(str, sorted(X))) + "}"
    if t == "and": return nf(len(A & B), f"주사위 한 개를 던지는 시행에서 A = {s(A)}, B = {s(B)}일 때 A ∩ B의 원소는 몇 개일까요?", f"A ∩ B = {s(A & B) if A & B else '∅'} → {len(A & B)}개", "두 사건에 공통인 결과")
    if t == "or": return nf(len(A | B), f"주사위 한 개를 던지는 시행에서 A = {s(A)}, B = {s(B)}일 때 A ∪ B의 원소는 몇 개일까요?", f"A ∪ B = {s(A | B)} → {len(A | B)}개", "적어도 하나에 속하는 결과")
    if t == "ex": return num(f"주사위 한 개를 던지는 시행에서 A = {s(A)}, B = {s(B)}는 서로 배반사건일까요?  (그렇다 1, 아니다 0)", 1 if not A & B else 0, f"A ∩ B = {s(A & B) if A & B else '∅'}\n" + ("공통 원소가 없으므로 배반 → 1" if not A & B else "공통 원소가 있으므로 배반 아님 → 0"), "A ∩ B = ∅ ⇔ 배반")
    return nf(6 - len(A), f"주사위 한 개를 던지는 시행에서 A = {s(A)}의 여사건의 원소는 몇 개일까요?", f"Aᶜ = {s(set(range(1, 7)) - A)} → {6 - len(A)}개", "표본공간에서 A를 뺀 것")
L31 = [("주사위 두 개의 사건", c1_cnt), ("사건의 연산", c1_set)]

def c2_dice(r):
    t = r.choice(["sum", "ge", "prododd", "max"])
    k = r.randint(3, 11)
    f, nm = {"sum": (lambda p: p[0] + p[1] == k, f"눈의 합이 {k}"), "ge": (lambda p: p[0] + p[1] >= k, f"눈의 합이 {k} 이상"),
             "prododd": (lambda p: p[0] * p[1] % 2 == 1, "두 눈의 곱이 홀수"), "max": (lambda p: max(p) == k % 6 + 1, f"큰 눈이 {k % 6 + 1}")}[t]
    c = sum(1 for p in DICE2 if f(p))
    return nf(F(c, 36), f"주사위 두 개를 던질 때 {nm}일 확률은? (기약분수로)", f"전체 36가지 중 {nm}인 경우 {c}가지\n{c}/36" + (f" = {fs(F(c, 36))}" if F(c, 36).denominator != 36 else ""), "경우의 수 ÷ 36")
def c2_ball(r):
    w, b, k = r.randint(2, 6), r.randint(2, 6), r.choice([2, 3])
    t = r.choice(["allw", "onew"])
    if t == "allw":
        if k > w: return None
        v = F(comb(w, k), comb(w + b, k))
        return nf(v, f"흰 공 {w}개, 검은 공 {b}개 중 {k}개를 동시에 뽑을 때 모두 흰 공일 확률은? (기약분수로)", f"{C(w, k)} / {C(w + b, k)} = {comb(w, k)}/{comb(w + b, k)} = {fs(v)}", "조합의 비")
    v = F(w * comb(b, k - 1), comb(w + b, k))
    return nf(v, f"흰 공 {w}개, 검은 공 {b}개 중 {k}개를 동시에 뽑을 때 흰 공이 정확히 1개일 확률은? (기약분수로)", f"{C(w, 1)} × {C(b, k - 1)} / {C(w + b, k)} = {w * comb(b, k - 1)}/{comb(w + b, k)} = {fs(v)}", "흰 공 1개, 검은 공 나머지")
def c2_pick(r):
    n, k = r.randint(4, 9), r.randint(2, 3)
    if k >= n: return None
    v = F(k, n)
    return nf(v, f"{n}명 중 {k}명을 뽑을 때 A가 뽑힐 확률은? (기약분수로)", f"A를 포함하는 경우 {C(n - 1, k - 1)} = {comb(n - 1, k - 1)}, 전체 {C(n, k)} = {comb(n, k)}\n{comb(n - 1, k - 1)}/{comb(n, k)} = {fs(v)}", "A를 먼저 뽑아 두세요.")
def c2_stat(r):
    N = r.choice([500, 1000, 2000]); k = r.randint(N // 5, N * 4 // 5)
    v = F(k, N)
    return dec(v, f"압정을 {N:,}번 던져 바늘이 위로 향한 것이 {k:,}번이었습니다. 통계적 확률은? (소수로)", f"통계적 확률 = 상대도수 = {k} ÷ {N} = {float(v):g}", "상대도수")
L32 = [("주사위 확률", c2_dice), ("공 뽑기", c2_ball), ("특정인이 뽑힐 확률", c2_pick), ("통계적 확률", c2_stat)]

def c3_add(r):
    a, b = r.randint(2, 7), r.randint(2, 7); c = r.randint(1, min(a, b) - 1)
    t = r.choice(["union", "inter", "only"])
    pa, pb, pc = F(a, 10), F(b, 10), F(c, 10)
    if a + b - c > 10: return None
    if t == "union": return dec(pa + pb - pc, f"P(A) = {float(pa):g}, P(B) = {float(pb):g}, P(A ∩ B) = {float(pc):g}일 때 P(A ∪ B)는?", f"P(A ∪ B) = P(A) + P(B) − P(A ∩ B)\n= {float(pa):g} + {float(pb):g} − {float(pc):g} = {float(pa + pb - pc):g}", "덧셈정리")
    if t == "inter": return dec(pc, f"P(A ∪ B) = {float(pa + pb - pc):g}, P(A) = {float(pa):g}, P(B) = {float(pb):g}일 때 P(A ∩ B)는?", f"P(A ∩ B) = {float(pa):g} + {float(pb):g} − {float(pa + pb - pc):g} = {float(pc):g}", "덧셈정리를 거꾸로")
    return dec(pa - pc, f"P(A) = {float(pa):g}, P(A ∩ B) = {float(pc):g}일 때 P(A ∩ Bᶜ)는?", f"P(A ∩ Bᶜ) = P(A) − P(A ∩ B) = {float(pa - pc):g}", "A에서 B와 겹치는 부분을 뺍니다.")
def c3_mult(r):
    N = r.choice([20, 30, 40, 50, 60]); p, q = r.sample([2, 3, 4, 5, 6, 7], 2)
    c = sum(1 for x in range(1, N + 1) if x % p == 0 or x % q == 0)
    from math import lcm
    return nf(F(c, N), f"1부터 {N}까지의 카드 중 한 장을 뽑을 때 {p}의 배수 또는 {q}의 배수일 확률은? (기약분수로)", f"{p}의 배수 {N // p}, {q}의 배수 {N // q}, 공배수({lcm(p, q)}의 배수) {N // lcm(p, q)}\n({N // p} + {N // q} − {N // lcm(p, q)})/{N} = {fs(F(c, N))}", "덧셈정리")
def c3_excl(r):
    a, b = r.sample(range(2, 13), 2)
    ca = sum(1 for p in DICE2 if sum(p) == a); cb = sum(1 for p in DICE2 if sum(p) == b)
    return nf(F(ca + cb, 36), f"주사위 두 개를 던질 때 눈의 합이 {a} 또는 {b}일 확률은? (기약분수로)", f"두 사건은 배반: {ca}/36 + {cb}/36 = {ca + cb}/36" + (f" = {fs(F(ca + cb, 36))}" if F(ca + cb, 36).denominator != 36 else ""), "배반사건은 더하기")
L33 = [("확률의 덧셈정리", c3_add), ("배수 카드", c3_mult), ("배반사건", c3_excl)]

def c4_comp(r):
    t = r.choice(["coin", "dice6", "ball", "even"])
    if t == "coin":
        n = r.randint(2, 6); return nf(1 - F(1, 2 ** n), f"동전 {n}개를 던질 때 적어도 한 개가 앞면일 확률은? (기약분수로)", f"여사건: 모두 뒷면 (1/2){sup(n)} = 1/{2 ** n}\n1 − 1/{2 ** n} = {fs(1 - F(1, 2 ** n))}", "적어도 → 여사건")
    if t == "dice6":
        n = r.randint(2, 4); return nf(1 - F(5, 6) ** n, f"주사위를 {n}번 던질 때 6의 눈이 적어도 한 번 나올 확률은? (기약분수로)", f"여사건: 6이 한 번도 안 나옴 (5/6){sup(n)}\n1 − {fs(F(5, 6) ** n)} = {fs(1 - F(5, 6) ** n)}", "적어도 → 여사건")
    if t == "even":
        n = r.randint(2, 5); return nf(1 - F(1, 2 ** n), f"주사위를 {n}번 던질 때 적어도 한 번 짝수가 나올 확률은? (기약분수로)", f"여사건: 모두 홀수 (1/2){sup(n)}\n1 − 1/{2 ** n} = {fs(1 - F(1, 2 ** n))}", "적어도 → 여사건")
    w, b, k = r.randint(2, 5), r.randint(2, 6), r.randint(2, 3)
    if k > b: return None
    v = 1 - F(comb(b, k), comb(w + b, k))
    return nf(v, f"흰 공 {w}개, 검은 공 {b}개 중 {k}개를 뽑을 때 적어도 한 개가 흰 공일 확률은? (기약분수로)", f"여사건: 모두 검은 공 {C(b, k)}/{C(w + b, k)} = {comb(b, k)}/{comb(w + b, k)}\n1 − 그 값 = {fs(v)}", "적어도 → 여사건")
def c4_bday(r):
    n, d = r.randint(2, 4), r.choice([7, 12])
    v = 1 - F(perm(d, n), d ** n)
    return nf(v, f"{n}명의 생일 {'요일' if d == 7 else '달'}이 적어도 두 명 같을 확률은? (각 {'요일' if d == 7 else '달'}은 같은 확률, 기약분수로)", f"여사건: 모두 다름 {d}P{n}/{d}{sup(n)} = {perm(d, n)}/{d ** n}\n1 − 그 값 = {fs(v)}", "모두 다를 확률을 빼세요.")
def c4_more(r):
    t = r.choice(["card", "mult3", "pair"])
    if t == "card":
        n, k, d = r.randint(6, 12), r.randint(1, 3), r.randint(2, 3)
        v = 1 - F(comb(n - k, d), comb(n, d))
        return nf(v, f"당첨 카드 {k}장을 포함한 {n}장 중 {d}장을 뽑을 때 적어도 한 장이 당첨일 확률은? (기약분수로)", f"여사건: 모두 꽝 {C(n - k, d)}/{C(n, d)} = {comb(n - k, d)}/{comb(n, d)}\n1 − 그 값 = {fs(v)}", "적어도 → 여사건")
    if t == "mult3":
        n = r.randint(2, 4); v = 1 - F(2, 3) ** n
        return nf(v, f"주사위를 {n}번 던질 때 3의 배수의 눈이 적어도 한 번 나올 확률은? (기약분수로)", f"한 번에 3의 배수가 아닐 확률 4/6 = 2/3\n1 − (2/3){sup(n)} = {fs(v)}", "적어도 → 여사건")
    b, g, k = r.randint(2, 6), r.randint(1, 4), r.randint(2, 3)
    if k > b: return None
    v = 1 - F(comb(b, k), comb(b + g, k))
    return nf(v, f"남자 {b}명, 여자 {g}명 중 대표 {k}명을 뽑을 때 적어도 한 명이 여자일 확률은? (기약분수로)", f"여사건: 모두 남자 {C(b, k)}/{C(b + g, k)} = {comb(b, k)}/{comb(b + g, k)}\n1 − 그 값 = {fs(v)}", "적어도 → 여사건")
L34 = [("적어도 하나", c4_comp), ("생일 문제", c4_bday), ("여사건 활용", c4_more)]

# ================= ch04 조건부확률 =================
def d1_cond(r):
    a, c = r.randint(3, 8), None
    c = r.randint(1, a - 1); b = r.randint(c + 1, 9)
    t = r.choice(["BA", "AB"])
    if t == "BA": return dec(F(c, a), f"P(A) = {a / 10:g}, P(A ∩ B) = {c / 10:g}일 때 P(B|A)는? (소수로, 나누어떨어지지 않으면 넷째 자리까지 반올림)", f"P(B|A) = P(A ∩ B)/P(A) = {c / 10:g} ÷ {a / 10:g} = {float(F(c, a)):.4f}".rstrip("0"), "P(B|A) = P(A ∩ B)/P(A)", tol=0.0001)
    return dec(F(c, b), f"P(B) = {b / 10:g}, P(A ∩ B) = {c / 10:g}일 때 P(A|B)는? (소수로, 나누어떨어지지 않으면 넷째 자리까지 반올림)", f"P(A|B) = P(A ∩ B)/P(B) = {c / 10:g} ÷ {b / 10:g} = {float(F(c, b)):.4f}".rstrip("0"), "P(A|B) = P(A ∩ B)/P(B)", tol=0.0001)
def d1_table(r):
    gm, gn, bm, bn = [r.randint(3, 15) for _ in range(4)]
    t = r.choice(["g|m", "m|g", "b|n"])
    if t == "g|m": v = F(gm, gm + bm); q, e = "안경을 쓴 학생 중 한 명을 고를 때 여학생일 확률은?", f"안경 쓴 학생 {gm + bm}명 중 여학생 {gm}명 → {fs(v)}"
    elif t == "m|g": v = F(gm, gm + gn); q, e = "여학생 중 한 명을 고를 때 안경을 썼을 확률은?", f"여학생 {gm + gn}명 중 안경 {gm}명 → {fs(v)}"
    else: v = F(bn, bn + gn); q, e = "안경을 쓰지 않은 학생 중 한 명을 고를 때 남학생일 확률은?", f"안경을 쓰지 않은 학생 {bn + gn}명 중 남학생 {bn}명 → {fs(v)}"
    return nf(v, f"어느 반의 여학생은 안경 쓴 학생 {gm}명, 안 쓴 학생 {gn}명, 남학생은 안경 쓴 학생 {bm}명, 안 쓴 학생 {bn}명입니다. {q} (기약분수로)", "조건부확률은 조건에 해당하는 집단만 표본공간으로 봅니다.\n" + e, "조건이 되는 집단을 분모로")
def d1_seq(r):
    w, b = r.randint(2, 6), r.randint(2, 6); t = r.choice(["ww", "bw"])
    if t == "ww": v = F(w - 1, w + b - 1); q = "첫 번째가 흰 공일 때 두 번째도 흰 공일"; e = f"첫 번째 흰 공을 꺼낸 뒤: 흰 공 {w - 1}개, 전체 {w + b - 1}개"
    else: v = F(w, w + b - 1); q = "첫 번째가 검은 공일 때 두 번째가 흰 공일"; e = f"첫 번째 검은 공을 꺼낸 뒤: 흰 공 {w}개, 전체 {w + b - 1}개"
    return nf(v, f"흰 공 {w}개, 검은 공 {b}개가 든 주머니에서 공을 한 개씩 두 번 꺼낼 때(꺼낸 공은 넣지 않음) {q} 확률은? (기약분수로)", e + f" → {fs(v)}", "남은 공으로 생각하세요.")
def d1_die(r):
    A = set(r.sample(range(1, 7), r.randint(2, 4))); B = set(r.sample(range(1, 7), r.randint(2, 4)))
    v = F(len(A & B), len(A))
    s = lambda X: "{" + ", ".join(map(str, sorted(X))) + "}"
    return nf(v, f"주사위 한 개를 던지는 시행에서 A = {s(A)}, B = {s(B)}일 때 P(B|A)는? (기약분수 또는 정수로)", f"A가 일어났다고 보면 표본공간이 {s(A)}\n그중 B인 것 {s(A & B) if A & B else '∅'} → {len(A & B)}/{len(A)}" + (f" = {fm(v)}" if (v.numerator, v.denominator) != (len(A & B), len(A)) else ""), "A를 새 표본공간으로")
L41 = [("조건부확률 공식", d1_cond), ("분할표", d1_table), ("꺼낸 공은 넣지 않을 때", d1_seq), ("주사위 사건", d1_die)]

def d2_seq(r):
    w, b = r.randint(2, 6), r.randint(2, 6); t = r.choice(["ww", "wb", "second"])
    N = w + b
    if t == "ww": v = F(w, N) * F(w - 1, N - 1); e = f"{w}/{N} × {w - 1}/{N - 1} = {fs(v)}"; q = "두 번 모두 흰 공일"
    elif t == "wb": v = F(w, N) * F(b, N - 1); e = f"{w}/{N} × {b}/{N - 1} = {fs(v)}"; q = "첫 번째는 흰 공, 두 번째는 검은 공일"
    else: v = F(w, N); e = f"(흰, 흰) + (검, 흰) = {w}/{N}×{w - 1}/{N - 1} + {b}/{N}×{w}/{N - 1} = {fs(v)}\n(첫 번째와 같은 확률)"; q = "두 번째 공이 흰 공일"
    return nf(v, f"흰 공 {w}개, 검은 공 {b}개에서 한 개씩 두 번 꺼낼 때(넣지 않음) {q} 확률은? (기약분수로)", "곱셈정리 P(A ∩ B) = P(A)P(B|A)\n" + e, "차례로 곱하세요.")
def d2_bayes(r):
    p, sen, fp = r.choice([1, 2, 5, 10]), r.choice([80, 90, 95]), r.choice([5, 10, 20])
    P_, S, Fp = F(p, 100), F(sen, 100), F(fp, 100)
    pos = P_ * S + (1 - P_) * Fp
    t = r.choice(["pos", "post"])
    if t == "pos": return nf(pos, f"어떤 병의 유병률은 {p}%이고, 검사는 환자의 {sen}%, 비환자의 {fp}%를 양성으로 판정합니다. 임의의 한 사람이 양성 판정을 받을 확률은? (기약분수로)", f"환자이면서 양성 {fs(P_)}×{fs(S)} + 비환자이면서 양성 {fs(1 - P_)}×{fs(Fp)}\n= {fs(pos)}", "두 경우로 나누어 더하세요.")
    v = P_ * S / pos
    return nf(v, f"어떤 병의 유병률은 {p}%이고, 검사는 환자의 {sen}%, 비환자의 {fp}%를 양성으로 판정합니다. 양성 판정을 받은 사람이 실제로 환자일 확률은? (기약분수로)", f"P(양성) = {fs(pos)}\nP(환자 ∩ 양성) = {fs(P_ * S)}\n나누면 {fs(v)}", "베이즈 정리")
def d2_lot(r):
    k, n = r.randint(1, 4), r.randint(6, 12)
    return nf(F(k, n), f"당첨 제비 {k}개를 포함한 {n}개에서 두 사람이 차례로 뽑을 때 두 번째 사람이 당첨될 확률은? (기약분수로)", f"(당, 당) + (꽝, 당) = {k}/{n}×{k - 1}/{n - 1} + {n - k}/{n}×{k}/{n - 1} = {fs(F(k, n))}\n순서와 무관하게 같습니다.", "두 경우로 나누세요.")
L42 = [("곱셈정리", d2_seq), ("검사와 베이즈", d2_bayes), ("제비뽑기", d2_lot)]

def d3_ind(r):
    a, b = r.randint(1, 9), r.randint(1, 9); pa, pb = F(a, 10), F(b, 10)
    t = r.choice(["and", "none", "or"])
    if t == "and": v = pa * pb; e = f"독립이면 P(A ∩ B) = P(A)P(B) = {a / 10:g} × {b / 10:g} = {float(v):g}"; q = "P(A ∩ B)"
    elif t == "none": v = (1 - pa) * (1 - pb); e = f"Aᶜ, Bᶜ도 독립: {float(1 - pa):g} × {float(1 - pb):g} = {float(v):g}"; q = "P(Aᶜ ∩ Bᶜ)"
    else: v = 1 - (1 - pa) * (1 - pb); e = f"P(A ∪ B) = 1 − P(Aᶜ)P(Bᶜ) = 1 − {float((1 - pa) * (1 - pb)):g} = {float(v):g}"; q = "P(A ∪ B)"
    return dec(v, f"A, B가 독립이고 P(A) = {a / 10:g}, P(B) = {b / 10:g}일 때 {q}는?", e, "독립 ⇔ P(A ∩ B) = P(A)P(B)")
def d3_check(r):
    A = set(r.sample(range(1, 7), r.choice([2, 3]))); B = set(r.sample(range(1, 7), r.choice([2, 3, 4])))
    v = 1 if F(len(A & B), 6) == F(len(A), 6) * F(len(B), 6) else 0
    s = lambda X: "{" + ", ".join(map(str, sorted(X))) + "}"
    return num(f"주사위 한 개를 던질 때 A = {s(A)}, B = {s(B)}는 서로 독립일까요?  (그렇다 1, 아니다 0)", v,
               f"P(A)P(B) = {len(A)}/6 × {len(B)}/6 = {fs(F(len(A) * len(B), 36))}\nP(A ∩ B) = {len(A & B)}/6 = {fs(F(len(A & B), 6))}\n" + ("같으므로 독립 → 1" if v else "다르므로 종속 → 0"), "P(A ∩ B) = P(A)P(B)인지 확인")
def d3_shoot(r):
    a, b = r.randint(5, 9), r.randint(5, 9); t = r.choice(["both", "one", "atleast"])
    pa, pb = F(a, 10), F(b, 10)
    v = {"both": pa * pb, "one": pa * (1 - pb) + (1 - pa) * pb, "atleast": 1 - (1 - pa) * (1 - pb)}[t]
    nm = {"both": "둘 다 명중할", "one": "정확히 한 명만 명중할", "atleast": "적어도 한 명이 명중할"}[t]
    return dec(v, f"명중률이 {a / 10:g}, {b / 10:g}인 두 사수가 서로 영향 없이 한 발씩 쏠 때 {nm} 확률은?", {"both": f"P = {a / 10:g} × {b / 10:g} = {float(v):g}", "one": f"P = {a / 10:g}×{1 - a / 10:g} + {1 - a / 10:g}×{b / 10:g} = {float(v):g}", "atleast": f"P = 1 − (둘 다 빗나감) = 1 − {1 - a / 10:g}×{1 - b / 10:g} = {float(v):g}"}[t] + "\n(두 사수는 독립이므로 확률을 곱합니다)", "독립사건의 곱")
L43 = [("독립사건의 확률", d3_ind), ("독립 판정", d3_check), ("두 사수", d3_shoot)]

def d4_bin(r):
    n = r.randint(3, 6); k = r.randint(0, n); p = r.choice([F(1, 2), F(1, 3), F(1, 6), F(2, 3)])
    v = comb(n, k) * p ** k * (1 - p) ** (n - k)
    ev = {F(1, 2): "동전의 앞면", F(1, 3): "주사위 눈이 1 또는 2", F(1, 6): "주사위 1의 눈", F(2, 3): "주사위 눈이 3 이상"}[p]
    return nf(v, f"{ev}이 나올 확률이 {fs(p)}인 시행을 {n}번 할 때 정확히 {k}번 나올 확률은? (기약분수로)", f"{C(n, k)} ({fs(p)}){sup(k)} ({fs(1 - p)}){sup(n - k)} = {comb(n, k)} × {fs(p ** k)} × {fs((1 - p) ** (n - k))} = {fs(v)}", "nCk pᵏ qⁿ⁻ᵏ")
def d4_atleast(r):
    n, k = r.randint(3, 6), r.randint(2, 4)
    if k > n: return None
    v = sum(comb(n, i) for i in range(k, n + 1)) * F(1, 2 ** n)
    return nf(v, f"명중률이 1/2인 사수가 {n}번 쏠 때 {k}번 이상 명중할 확률은? (기약분수로)", f"Σ(i={k}~{n}) {n}Ci (1/2){sup(n)} = ({' + '.join(str(comb(n, i)) for i in range(k, n + 1))})/{2 ** n} = {fs(v)}", "각 경우를 더하세요.")
def d4_walk(r):
    n, pos = r.choice([2, 4, 6]), None
    pos = r.choice([x for x in range(-n, n + 1, 2)])
    k = (n + pos) // 2
    v = F(comb(n, k), 2 ** n)
    return nf(v, f"원점에서 출발해 동전을 던져 앞면이면 +1, 뒷면이면 −1만큼 움직입니다. {n}번 던진 뒤 점의 위치가 {m(pos)}일 확률은? (기약분수로)", f"앞면 a번, 뒷면 {n} − a번: a − ({n} − a) = {m(pos)} → a = {k}\n{C(n, k)}/2{sup(n)} = {fs(v)}", "앞면 횟수를 미지수로")
L44 = [("독립시행", d4_bin), ("~번 이상", d4_atleast), ("점의 이동", d4_walk)]

# ================= ch05 확률분포 =================
def e1_dist(r):
    t = r.choice(["coin", "ck", "max", "ball"])
    if t == "coin":
        n, k = r.randint(2, 4), r.randint(0, 3)
        if k > n: return None
        return nf(F(comb(n, k), 2 ** n), f"동전 {n}개를 던질 때 앞면의 개수 X에 대해 P(X = {k})는? (기약분수로)", f"{C(n, k)}/2{sup(n)} = {comb(n, k)}/{2 ** n} = {fs(F(comb(n, k), 2 ** n))}", "이항계수")
    if t == "ck":
        n = r.randint(3, 5); s = n * (n + 1) // 2
        return nf(F(1, s), f"P(X = k) = ck (k = 1, 2, …, {n})가 확률분포일 때 c는? (기약분수로)", f"확률의 합 = 1: c(1 + 2 + … + {n}) = {s}c = 1 → c = 1/{s}", "합이 1")
    if t == "max":
        k = r.randint(1, 6); c = sum(1 for p in DICE2 if max(p) == k)
        return nf(F(c, 36), f"주사위 두 개를 던져 나온 눈 중 큰 수를 X라 할 때 P(X = {k})는? (기약분수로)", f"max = {k}인 경우 {k}² − {k - 1}² = {c}가지\n{c}/36" + (f" = {fs(F(c, 36))}" if F(c, 36).denominator != 36 else ""), "k 이하 − (k−1) 이하")
    w, b, k = r.randint(2, 5), r.randint(2, 5), r.randint(0, 2)
    v = F(comb(w, k) * comb(b, 2 - k), comb(w + b, 2))
    return nf(v, f"흰 공 {w}개, 검은 공 {b}개 중 2개를 뽑을 때 흰 공의 개수 X에 대해 P(X = {k})는? (기약분수로)", f"{C(w, k)} × {C(b, 2 - k)} / {C(w + b, 2)} = {comb(w, k) * comb(b, 2 - k)}/{comb(w + b, 2)} = {fs(v)}", "초기하분포")
L51 = [("확률분포", e1_dist)]

def e2_EV(r):
    t = r.choice(["lin", "var", "sd", "table"])
    a, b = nz(r, -4, 5), r.randint(-6, 6)
    if t == "lin":
        E = r.randint(-3, 8); return nf(a * E + b, f"E(X) = {m(E)}일 때 E({poly((a, 'X'), (b, ''))})는?", f"E(aX + b) = aE(X) + b = {m(a)}×{par(E)}{term(b)} = {m(a * E + b)}", "E(aX + b) = aE(X) + b")
    if t == "var":
        V = r.randint(1, 9); return nf(a * a * V, f"V(X) = {V}일 때 V({poly((a, 'X'), (b, ''))})는?", f"V(aX + b) = a²V(X) = {a * a} × {V} = {a * a * V}  (b는 영향 없음)", "V(aX + b) = a²V(X)")
    if t == "sd":
        s = r.randint(1, 6); return nf(abs(a) * s, f"σ(X) = {s}일 때 σ({poly((a, 'X'), (b, ''))})는?", f"σ(aX + b) = |a|σ(X) = {abs(a)} × {s} = {abs(a) * s}", "σ(aX + b) = |a|σ(X)")
    xs = sorted(r.sample(range(0, 6), 3)); ps = r.choice([(1, 1, 2), (1, 2, 1), (2, 1, 1), (1, 1, 1), (1, 3, 1)])
    T = sum(ps); E = F(sum(x * p for x, p in zip(xs, ps)), T); V = F(sum(x * x * p for x, p in zip(xs, ps)), T) - E * E
    w = r.choice(["E", "V"])
    tbl = ", ".join(f"P(X = {x}) = {fs(F(p, T))}" for x, p in zip(xs, ps))
    if w == "E": return nf(E, f"{tbl}일 때 E(X)는? (기약분수 또는 정수로)", f"E(X) = Σ x·P = " + " + ".join(f"{x}×{fs(F(p, T))}" for x, p in zip(xs, ps)) + f" = {fm(E)}", "Σ xP(x)")
    return nf(V, f"{tbl}일 때 V(X)는? (기약분수 또는 정수로)", f"E(X) = {fm(E)}, E(X²) = {fm(E * E + V)}\nV(X) = E(X²) − {{E(X)}}² = {fm(E * E + V)} − {fs(E * E)} = {fm(V)}", "E(X²) − {E(X)}²")
L52 = [("기댓값과 분산", e2_EV)]

def e3_bin(r):
    t = r.choice(["E", "V", "sd", "np", "P"])
    if t in ("E", "V"):
        n, p = r.choice([10, 20, 50, 100, 200, 300]), r.choice([F(1, 2), F(1, 5), F(3, 10), F(1, 4), F(2, 5)])
        v = n * p if t == "E" else n * p * (1 - p)
        return nf(v, f"X ~ B({n}, {float(p):g})일 때 {'E(X)' if t == 'E' else 'V(X)'}는? (기약분수 또는 정수로)", f"{'E(X) = np' if t == 'E' else 'V(X) = np(1 − p)'} = {n} × {float(p):g}" + ("" if t == "E" else f" × {float(1 - p):g}") + f" = {fm(v)}", "이항분포의 평균과 분산")
    if t == "sd":
        n = r.choice([16, 36, 64, 100, 144, 196, 400]); return nf(F(isqrt(n), 2), f"X ~ B({n}, 1/2)일 때 σ(X)는? (기약분수 또는 정수로)", f"V = {n} × 1/2 × 1/2 = {fs(F(n, 4))}, σ = √{fs(F(n, 4))} = {fm(F(isqrt(n), 2))}", "σ = √(npq)")
    if t == "np":
        n, p = r.choice([(10, F(3, 10)), (20, F(2, 5)), (50, F(1, 5)), (25, F(2, 5)), (40, F(1, 4)), (30, F(1, 3))])
        E, V = n * p, n * p * (1 - p); ask = r.choice(["n", "p"])
        if ask == "n": return nf(n, f"이항분포에서 E(X) = {fm(E)}, V(X) = {fm(V)}일 때 n은?", f"V/E = 1 − p = {fs(V / E)} → p = {fs(p)}\nn = E/p = {n}", "V ÷ E = 1 − p")
        return nf(p, f"이항분포에서 E(X) = {fm(E)}, V(X) = {fm(V)}일 때 p는? (기약분수로)", f"V/E = 1 − p = {fs(V / E)} → p = {fs(p)}", "V ÷ E = 1 − p")
    n, k = r.randint(3, 5), r.randint(0, 3)
    p = r.choice([F(1, 2), F(1, 3)])
    if k > n: return None
    v = comb(n, k) * p ** k * (1 - p) ** (n - k)
    return nf(v, f"X ~ B({n}, {fs(p)})일 때 P(X = {k})는? (기약분수로)", f"{C(n, k)}({fs(p)}){sup(k)}({fs(1 - p)}){sup(n - k)} = {fs(v)}", "nCk pᵏ qⁿ⁻ᵏ")
L53 = [("이항분포", e3_bin)]

def e4_law(r):
    t = r.choice(["count", "var", "scale", "est"])
    if t == "count":
        N, p = r.choice([600, 1200, 3000, 6000]), r.choice([F(1, 6), F(1, 2), F(1, 3)])
        return nf(N * p, f"{'주사위' if p != F(1, 2) else '동전'}를 {N:,}번 던질 때 {'1의 눈' if p == F(1, 6) else '앞면' if p == F(1, 2) else '1 또는 2의 눈'}은 약 몇 번 나올까요?", f"기댓값 np = {N} × {fs(p)} = {N * p}", "큰수의 법칙: 상대도수 → 확률")
    if t == "var":
        n = r.choice([25, 100, 400, 2500]); v = F(1, 4 * n)
        return dec(v, f"X ~ B({n}, 0.5)일 때 V(X/{n})은?", f"V(X/n) = V(X)/n² = p(1 − p)/n = 0.25/{n} = {float(v):g}", "비율의 분산 = pq/n", tol=1e-6)
    if t == "scale":
        k = r.choice([4, 9, 16, 25])
        return nf(F(1, isqrt(k)), f"시행 횟수를 {k}배로 늘리면 비율의 표준편차는 몇 배가 될까요? (기약분수로)", f"σ = √(pq/n) → n이 {k}배면 σ는 1/√{k} = 1/{isqrt(k)}배", "σ ∝ 1/√n")
    N, k = r.choice([1000, 2000, 500]), None
    k = r.randint(N // 5, N * 4 // 5) // 10 * 10; m_ = r.choice([50, 100, 200])
    v = F(k, N) * m_
    if v.denominator != 1: return None
    return nf(v, f"압정을 {N:,}번 던져 바늘이 위로 향한 것이 {k:,}번이었습니다. 그 확률로 {m_}번 던지면 바늘이 위로 향하는 횟수는 약 몇 번일까요?", f"통계적 확률 {k}/{N} = {float(F(k, N)):g}\n{m_} × {float(F(k, N)):g} = {v}", "상대도수로 확률 추정")
L54 = [("큰수의 법칙", e4_law)]

# ================= ch06 연속확률분포 =================
def f1_unif(r):
    L_ = r.randint(2, 10); a, b = sorted(r.sample(range(0, L_ + 1), 2)); t = r.choice(["k", "P"])
    if t == "k": return nf(F(1, L_), f"f(x) = k (0 ≤ x ≤ {L_})가 확률밀도함수일 때 k는? (기약분수로)", f"전체 넓이 = 1: k × {L_} = 1 → k = 1/{L_}", "넓이가 1")
    return nf(F(b - a, L_), f"f(x) = 1/{L_} (0 ≤ x ≤ {L_})일 때 P({a} ≤ X ≤ {b})는? (기약분수 또는 정수로)", f"직사각형 넓이: ({b} − {a}) × 1/{L_} = {fm(F(b - a, L_))}", "넓이 = 확률")
def f1_lin(r):
    L_ = r.choice([1, 2, 3, 4]); t = r.choice(["a", "P", "E"])
    a = F(2, L_ * L_)
    if t == "a": return nf(a, f"f(x) = ax (0 ≤ x ≤ {L_})가 확률밀도함수일 때 a는? (기약분수 또는 정수로)", f"삼각형 넓이 (1/2) × {L_} × {L_}a = 1 → a = {fm(a)}", "넓이 = 1")
    if t == "P":
        c = F(r.randint(1, 2 * L_ - 1), 2)
        if c >= L_: return None
        v = a * c * c / 2
        return nf(v, f"f(x) = {fs(a)}x (0 ≤ x ≤ {L_})일 때 P(0 ≤ X ≤ {fs(c)})는? (기약분수로)".replace("1x", "x"), f"삼각형 넓이 (1/2) × {fs(c)} × {fs(a * c)} = {fs(v)}", "넓이")
    v = a * F(L_ ** 3, 3)
    return nf(v, f"f(x) = {fs(a)}x (0 ≤ x ≤ {L_})일 때 E(X)는? (기약분수 또는 정수로)".replace("1x", "x"), f"E(X) = ∫ x f(x) dx = {fs(a)} × {L_}³/3 = {fm(v)}", "∫ x f(x) dx")
L61 = [("균등분포", f1_unif), ("일차 밀도함수", f1_lin)]

def f2_norm(r):
    mu, s = r.choice([50, 60, 70, 100, 170]), r.choice([2, 4, 5, 10])
    t = r.choice(["axis", "half", "tbl"])
    if t == "axis": return nf(mu, f"X ~ N({mu}, {s}²)의 그래프의 대칭축은 직선 x = ?", f"정규분포 곡선은 평균 m = {mu}에 대해 대칭", "대칭축은 평균")
    if t == "half": return dec(.5, f"X ~ N({mu}, {s}²)에서 P(X ≥ {mu})는?", "평균에 대해 좌우 대칭이므로 평균 이상의 확률은 0.5", "대칭")
    k = r.choice([1, 2, 1.5, .5]); w = r.choice(["le", "ge", "between"])
    z = Z[k]
    if w == "le": v = .5 + z; q = f"P(X ≤ {mu + k * s:g})"; e = f"Z = {k:g} → 0.5 + {z:.4f} = {v:.4f}"
    elif w == "ge": v = .5 - z; q = f"P(X ≥ {mu + k * s:g})"; e = f"Z = {k:g} → 0.5 − {z:.4f} = {v:.4f}"
    else: v = 2 * z; q = f"P({mu - k * s:g} ≤ X ≤ {mu + k * s:g})"; e = f"Z: −{k:g} ~ {k:g} → 2 × {z:.4f} = {v:.4f}"
    return dec(round(v, 4), f"X ~ N({mu}, {s}²)일 때 {q}는? {zt(k)}", e, "표준화 후 표 이용")
L62 = [("정규분포", f2_norm)]

def f3_z(r):
    mu, s = r.choice([50, 60, 70, 100]), r.choice([2, 4, 5, 10, 20])
    t = r.choice(["z", "p", "p2"])
    if t == "z":
        k = r.choice([-2, -1.5, -1, 1, 1.5, 2, 2.5, .5]); x = mu + k * s
        return dec(k, f"X ~ N({mu}, {s}²)에서 X = {x:g}를 표준화한 값 Z는?", f"Z = (X − m)/σ = ({x:g} − {mu})/{s} = {k:g}", "Z = (X − m)/σ")
    if t == "p":
        a, b = sorted(r.sample([-2, -1, 1, 2, 1.5, .5], 2))
        v = (Z[abs(b)] if b > 0 else -Z[abs(b)]) - (Z[abs(a)] if a > 0 else -Z[abs(a)])
        return dec(round(v, 4), f"P({m(f'{a:g}')} ≤ Z ≤ {m(f'{b:g}')})는? {zt(*sorted({abs(a), abs(b)}))}", f"0을 기준으로 나누어 표의 값을 {'더합니다' if a < 0 < b else '뺍니다'}.\n= {v:.4f}", "0 기준으로 나누세요.")
    a, b = sorted(r.sample([-2, -1, 1, 2, .5, 1.5], 2))
    lo, hi = mu + a * s, mu + b * s
    v = (Z[abs(b)] if b > 0 else -Z[abs(b)]) - (Z[abs(a)] if a > 0 else -Z[abs(a)])
    return dec(round(v, 4), f"X ~ N({mu}, {s}²)일 때 P({lo:g} ≤ X ≤ {hi:g})는? {zt(*sorted({abs(a), abs(b)}))}", f"표준화: {m(f'{a:g}')} ≤ Z ≤ {m(f'{b:g}')}\n표의 값을 이용해 넓이를 계산하면 {v:.4f}", "먼저 표준화")
L63 = [("표준화", f3_z)]

def f4_approx(r):
    n, p = r.choice([(100, F(1, 2)), (400, F(1, 2)), (400, F(1, 5)), (100, F(1, 5)), (900, F(1, 10)), (2500, F(1, 2)), (64, F(1, 2)), (144, F(1, 2)),
                     (36, F(1, 2)), (625, F(1, 5)), (1600, F(1, 5)), (900, F(1, 2)), (196, F(1, 2)), (225, F(1, 5)), (400, F(1, 10)), (1600, F(1, 10))])
    mu = n * p; sd2 = n * p * (1 - p); sd = isqrt(int(sd2)) if sd2.denominator == 1 and isqrt(int(sd2)) ** 2 == sd2 else None
    if sd is None: return None
    t = r.choice(["m", "s", "P"])
    if t == "m": return nf(mu, f"X ~ B({n}, {fs(p)})를 근사하는 정규분포의 평균은?", f"np = {n} × {fs(p)} = {mu}", "평균 np")
    if t == "s": return nf(sd, f"X ~ B({n}, {fs(p)})를 근사하는 정규분포의 표준편차는?", f"√(npq) = √({n} × {fs(p)} × {fs(1 - p)}) = √{int(sd2)} = {sd}", "√(npq)")
    k = r.choice([1, 2])
    if r.random() < .5:
        return dec(round(2 * Z[k], 4), f"X ~ B({n}, {fs(p)})일 때 P({int(mu - k * sd)} ≤ X ≤ {int(mu + k * sd)})의 근삿값은? {zt(k)}", f"N({mu}, {sd}²)로 근사, Z: −{k} ~ {k}\n2 × {Z[k]:.4f} = {2 * Z[k]:.4f}", "정규근사 후 표준화")
    x = int(mu + k * sd)
    return dec(round(.5 - Z[k], 4), f"X ~ B({n}, {fs(p)})일 때 P(X ≥ {x})의 근삿값은? {zt(k)}", f"N({mu}, {sd}²)로 근사, Z = ({x} − {mu})/{sd} = {k}\n0.5 − {Z[k]:.4f} = {.5 - Z[k]:.4f}", "정규근사 후 표준화")
L64 = [("이항분포의 정규근사", f4_approx)]

# ================= ch07 통계적 추정 =================
def g1_pop(r):
    xs = sorted(r.sample(range(1, 10), r.randint(3, 4))); t = r.choice(["m", "v", "sm", "sv"])
    mu = F(sum(xs), len(xs))
    if t == "m": return nf(mu, f"모집단이 {{{', '.join(map(str, xs))}}}일 때(각각 같은 비율) 모평균은? (기약분수 또는 정수로)", f"({' + '.join(map(str, xs))})/{len(xs)} = {fm(mu)}", "평균")
    if t == "v":
        v = F(sum(x * x for x in xs), len(xs)) - mu * mu
        return nf(v, f"모집단이 {{{', '.join(map(str, xs))}}}일 때(각각 같은 비율) 모분산은? (기약분수 또는 정수로)", f"모분산 = Σ(x − m)²/N = {fm(v)}  (N으로 나눔)", "모분산은 N으로 나눔")
    if t == "sm": return nf(mu, f"표본 {', '.join(map(str, xs))}의 표본평균은? (기약분수 또는 정수로)", f"({' + '.join(map(str, xs))})/{len(xs)} = {fm(mu)}", "평균")
    v = F(sum((x - mu) ** 2 for x in xs), len(xs) - 1)
    return nf(v, f"표본 {', '.join(map(str, xs))}의 표본분산은? (기약분수 또는 정수로)", f"표본분산 = Σ(x − x̄)²/(n − 1) = {fs(sum((x - mu) ** 2 for x in xs))}/{len(xs) - 1} = {fm(v)}", "표본분산은 n − 1로 나눔")
def g1_samp(r):
    N, k = r.randint(3, 6), r.randint(2, 3)
    t = r.choice(["rep", "norep"])
    if t == "rep": return nf(N ** k, f"모집단 {{1, …, {N}}}에서 크기 {k}인 표본을 복원추출로 순서 있게 뽑는 방법은?", f"매번 {N}가지 → {N}{sup(k)} = {N ** k}", "복원 → 중복순열")
    return nf(perm(N, k), f"모집단 {{1, …, {N}}}에서 크기 {k}인 표본을 비복원추출로 순서 있게 뽑는 방법은?", f"{N}P{k} = {perm(N, k)}", "비복원 → 순열")
L71 = [("모수와 통계량", g1_pop), ("추출 방법의 수", g1_samp)]

def g2_mean(r):
    mu, s, n = r.choice([50, 100, 60, 170]), r.choice([10, 20, 12, 8, 6]), r.choice([4, 9, 16, 25, 36, 100])
    t = r.choice(["E", "sd", "V", "P"])
    if t == "E": return nf(mu, f"평균 {mu}, 표준편차 {s}인 모집단에서 크기 {n}인 표본을 뽑을 때 E(X̄)는?", f"E(X̄) = m = {mu}", "표본평균의 평균 = 모평균")
    if t == "sd": return nf(F(s, isqrt(n)), f"평균 {mu}, 표준편차 {s}인 모집단에서 크기 {n}인 표본을 뽑을 때 σ(X̄)는? (기약분수 또는 정수로)", f"σ(X̄) = σ/√n = {s}/{isqrt(n)} = {fm(F(s, isqrt(n)))}", "σ/√n")
    if t == "V": return nf(F(s * s, n), f"평균 {mu}, 표준편차 {s}인 모집단에서 크기 {n}인 표본을 뽑을 때 V(X̄)는? (기약분수 또는 정수로)", f"V(X̄) = σ²/n = {s * s}/{n} = {fm(F(s * s, n))}", "σ²/n")
    sd = F(s, isqrt(n))
    if sd.denominator != 1: return None
    k = r.choice([1, 2]); x = mu + k * int(sd)
    return dec(round(.5 - Z[k], 4), f"모집단 N({mu}, {s}²)에서 크기 {n}인 표본을 뽑을 때 P(X̄ ≥ {x})는? {zt(k)}", f"X̄ ~ N({mu}, {int(sd)}²), Z = ({x} − {mu})/{int(sd)} = {k}\n0.5 − {Z[k]:.4f} = {.5 - Z[k]:.4f}", "X̄도 정규분포")
L72 = [("표본평균의 분포", g2_mean)]

def g3_ci(r):
    s, n = r.choice([4, 5, 10, 20, 8]), r.choice([16, 25, 64, 100, 400])
    xb = r.choice([50, 60, 100, 170])
    e = 1.96 * s / isqrt(n); t = r.choice(["lo", "hi", "len", "len99"])
    if t == "lo": return dec(round(xb - e, 4), f"x̄ = {xb}, σ = {s}, n = {n}일 때 신뢰도 95% 신뢰구간의 아래 끝은? (1.96 이용)", f"x̄ − 1.96 × σ/√n = {xb} − 1.96 × {s}/{isqrt(n)} = {xb - e:g}", "x̄ ± 1.96σ/√n")
    if t == "hi": return dec(round(xb + e, 4), f"x̄ = {xb}, σ = {s}, n = {n}일 때 신뢰도 95% 신뢰구간의 위 끝은? (1.96 이용)", f"x̄ + 1.96 × σ/√n = {xb} + {e:g} = {xb + e:g}", "x̄ ± 1.96σ/√n")
    if t == "len": return dec(round(2 * e, 4), f"σ = {s}, n = {n}일 때 신뢰도 95% 신뢰구간의 길이는? (1.96 이용)", f"2 × 1.96 × σ/√n = 2 × 1.96 × {s}/{isqrt(n)} = {2 * e:g}", "길이 = 2 × 1.96σ/√n")
    e2 = 2.58 * s / isqrt(n)
    return dec(round(2 * e2, 4), f"σ = {s}, n = {n}일 때 신뢰도 99% 신뢰구간의 길이는? (2.58 이용)", f"2 × 2.58 × {s}/{isqrt(n)} = {2 * e2:g}", "99%는 2.58")
def g3_n(r):
    t = r.choice(["scale", "need"])
    if t == "scale":
        k = r.choice([2, 3, 4, 5])
        return nf(k * k, f"신뢰구간의 길이를 1/{k}로 줄이려면 표본의 크기를 몇 배로 해야 할까요?", f"길이 ∝ 1/√n → √n을 {k}배 → n을 {k * k}배", "길이는 1/√n에 비례")
    s, L_ = r.choice([(10, 3.92), (5, 1.96), (20, 3.92), (10, 1.96), (4, 1.568), (6, 2.352)])
    n = (2 * 1.96 * s / L_) ** 2
    return nf(round(n), f"σ = {s}일 때 신뢰도 95% 신뢰구간의 길이가 {L_:g}이 되는 표본의 크기 n은? (1.96 이용)", f"2 × 1.96 × {s}/√n = {L_:g} → √n = {2 * 1.96 * s / L_:g} → n = {round(n)}", "길이 식을 n에 대해 푸세요.")
L73 = [("모평균의 신뢰구간", g3_ci), ("표본의 크기", g3_n)]

def g4_prop(r):
    n = r.choice([100, 400, 600, 900, 2500]); ph = r.choice([F(1, 2), F(3, 5), F(2, 5), F(1, 5), F(4, 5)])
    t = r.choice(["ph", "V", "lo", "hi"])
    k = n * ph
    if t == "ph": return dec(ph, f"{n}명 중 {k}명이 찬성했을 때 표본비율은?", f"p̂ = {k}/{n} = {float(ph):g}", "표본비율")
    if t == "V": return dec(ph * (1 - ph) / n, f"모비율이 {float(ph):g}이고 n = {n}일 때 V(p̂)는?", f"V(p̂) = p(1 − p)/n = {float(ph * (1 - ph)):g}/{n} = {float(ph * (1 - ph) / n):.6g}", "pq/n", tol=1e-7)
    e = 1.96 * (float(ph * (1 - ph) / n)) ** .5
    v = float(ph) - e if t == "lo" else float(ph) + e
    return dec(round(v, 4), f"p̂ = {float(ph):g}, n = {n}일 때 신뢰도 95% 신뢰구간의 {'아래' if t == 'lo' else '위'} 끝은? (1.96 이용, 넷째 자리까지)", f"p̂ ± 1.96√(p̂(1 − p̂)/n) = {float(ph):g} {'−' if t == 'lo' else '+'} 1.96 × √({float(ph * (1 - ph)):g}/{n}) = {v:.4f}", "p̂ ± 1.96√(p̂q̂/n)", tol=0.0002)
L74 = [("모비율의 추정", g4_prop)]

ALL = {"ch01": [L11, L12, L13, L14], "ch02": [L21, L22, L23, L24], "ch03": [L31, L32, L33, L34], "ch04": [L41, L42, L43, L44],
       "ch05": [L51, L52, L53, L54], "ch06": [L61, L62, L63, L64], "ch07": [L71, L72, L73, L74]}

if __name__ == "__main__":
    tot = 0
    for ch, Ls in ALL.items():
        for i, T in enumerate(Ls, 1):
            per = {1: 40, 2: 20, 3: 14, 4: 10, 5: 8}.get(len(T), 6)
            n = write("c5", ch, f"l0{i}", T, per=per, seed=13 + i); tot += n; print(ch, i, len(T), n)
    print("total", tot)
