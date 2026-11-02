"""코스 1 · 챕터 5~7 (부등식, 경우의 수, 행렬) — 연습 문제 은행"""
from core import *
from math import comb, perm, factorial

def nz(r, a, b):
    while True:
        x = r.randint(a, b)
        if x: return x
LE = {"≤": ["≤", "<="], "≥": ["≥", ">="], "<": ["<"], ">": [">"]}

# ================= ch05 부등식 =================
def c5l1_lin(r):
    a, x0 = nz(r, -5, 5), nz(r, -6, 8)
    b = nz(r, -9, 9); op = r.choice([">", "<", "≥", "≤"])
    c = a * x0 + b
    flip = {">": "<", "<": ">", "≥": "≤", "≤": "≥"}
    rop = op if a > 0 else flip[op]
    return fill(f"{poly((a, 'x'), (b, ''))} {op} {m(c)}의 해는 x {rop} {{{{1}}}}", [ans(x0)],
                f"{m(b)}{'을' if bat(b) else '를'} 이항: {poly((a, 'x'))} {op} {m(c - b)}\n양변을 {m(a)}로 나눕니다." +
                (" 음수로 나누므로 부등호 방향이 바뀝니다." if a < 0 else "") + f"\nx {rop} {m(x0)}",
                "음수로 나누면 부등호 방향이 바뀝니다.")

def c5l1_sys(r):
    lo, hi = r.randint(-5, 3), None
    hi = lo + r.randint(2, 8)
    a, b = r.randint(1, 3), r.randint(1, 3)
    p, q = r.randint(-5, 5), r.randint(-5, 5)
    t = r.choice(["fill", "count"])
    e1 = f"{poly((a, 'x'), (p, ''))} > {m(a * lo + p)}"; e2 = f"{poly((b, 'x'), (q, ''))} < {m(b * hi + q)}"
    ex = (f"첫째: {poly((a, 'x'))} > {m(a * lo)}" + (f" → x > {m(lo)}" if a != 1 else "") + f"\n둘째: {poly((b, 'x'))} < {m(b * hi)}" + (f" → x < {m(hi)}" if b != 1 else "") +
          f"\n공통 범위: {m(lo)} < x < {m(hi)}")
    if t == "fill":
        return fill(f"연립부등식 {e1}, {e2}의 해는 {{{{1}}}} < x < {{{{2}}}}", [ans(lo), ans(hi)], ex, "각각 풀고 공통 범위를 찾으세요.")
    return num(f"연립부등식 {e1}, {e2}를 만족하는 정수 x는 몇 개일까요?", hi - lo - 1,
               ex + f"\n정수: {', '.join(m(z) for z in range(lo + 1, hi))} → {hi - lo - 1}개", "각각 풀고 공통 범위를 찾으세요.")

def c5l1_double(r):
    a, b = r.randint(2, 4), nz(r, -5, 5); lo, hi = r.randint(-4, 2), None
    hi = lo + r.randint(1, 6)
    return fill(f"{m(a * lo + b)} < {poly((a, 'x'), (b, ''))} ≤ {m(a * hi + b)}의 해는 {{{{1}}}} < x ≤ {{{{2}}}}", [ans(lo), ans(hi)],
                f"각 변에서 {m(b)}{'을' if bat(b) else '를'} 빼면 {m(a * lo)} < {a}x ≤ {m(a * hi)}\n각 변을 {ro(a)} 나누면 {m(lo)} < x ≤ {m(hi)}",
                "세 변에 같은 연산을 하세요.")

def c5l1_buy(r):
    p, q = r.choice([(800, 500), (1200, 700), (1000, 600), (1500, 900)])
    n = r.randint(8, 15); M = r.randint(q * n // 100 + 2, p * n // 100 - 1) * 100
    x = (M - q * n) // (p - q)
    if x <= 0 or x >= n: return None
    return num(f"한 개 {p:,}원인 사과와 {q:,}원인 귤을 합해 {n}개 사고 {M:,}원 이하를 내려고 합니다. 사과는 최대 몇 개 살 수 있을까요?", x,
               f"사과를 x개라 하면 {p}x + {q}({n} − x) ≤ {M}\n{p - q}x ≤ {M - q * n} → x ≤ {fs(F(M - q * n, p - q))}\n최대 {x}개",
               "부등식을 세운 뒤 조건에 맞는 가장 큰 자연수를 찾으세요.")

def c5l1_nat(r):
    a, b, c = r.randint(2, 5), r.randint(1, 9), r.randint(10, 40)
    k = (c + b - 1) // a if (c + b) % a == 0 else (c + b) // a
    cnt = len([n for n in range(1, 100) if a * n - b < c])
    return num(f"어떤 자연수의 {a}배에서 {j(b, '를을')} 뺀 값이 {c}보다 작습니다. 이런 자연수는 몇 개일까요?", cnt,
               f"{a}n − {b} < {c} → {a}n < {c + b} → n < {fs(F(c + b, a))}\n자연수 n = 1, …, {cnt} → {cnt}개", "부등식을 세우고 자연수만 세세요.")

def c5l1_none(r):
    a = r.randint(-3, 6)
    return num(f"연립부등식 x > {m(a)}, x < k의 해가 없도록 하는 실수 k의 최댓값은?", a,
               f"해가 있으려면 {m(a)} < x < k인 x가 있어야 하므로 k > {m(a)}\n해가 없으려면 k ≤ {m(a)} → 최댓값 {m(a)}", "수직선에서 두 범위가 겹치지 않을 조건")

L51 = [("일차부등식", c5l1_lin), ("연립부등식", c5l1_sys), ("A < B ≤ C 꼴", c5l1_double), ("개수 구하기", c5l1_buy), ("자연수의 개수", c5l1_nat), ("해가 없을 조건", c5l1_none)]

def c5l2_basic(r):
    a, b = r.randint(-5, 5), r.randint(1, 7)
    t = r.choice(["lt", "ge"])
    if t == "lt":
        return fill(f"|x{term(-a)}| < {b}의 해는 {{{{1}}}} < x < {{{{2}}}}", [ans(a - b), ans(a + b)],
                    f"|A| < {b} ⇔ −{b} < A < {b}\n−{b} < x{term(-a)} < {b}\n{m(a - b)} < x < {m(a + b)}", "|A| < k ⇔ −k < A < k")
    return fill(f"|x{term(-a)}| ≥ {b}의 해는 x ≤ {{{{1}}}} 또는 x ≥ {{{{2}}}}", [ans(a - b), ans(a + b)],
                f"|A| ≥ {b} ⇔ A ≤ −{b} 또는 A ≥ {b}\nx ≤ {m(a - b)} 또는 x ≥ {m(a + b)}", "|A| ≥ k ⇔ A ≤ −k 또는 A ≥ k")

def c5l2_count(r):
    a, b = r.randint(-5, 6), r.randint(1, 6); strict = r.choice([True, False])
    v = 2 * b - 1 if strict else 2 * b + 1
    return num(f"|x{term(-a)}| {'<' if strict else '≤'} {b}을 만족하는 정수 x는 몇 개일까요?".replace(f"{b}을", j(b, "를을")), v,
               f"{m(a - b)} {'<' if strict else '≤'} x {'<' if strict else '≤'} {m(a + b)}\n정수: {', '.join(m(z) for z in range(a - b + (1 if strict else 0), a + b + (0 if strict else 1)))} → {v}개",
               "범위를 구한 뒤 양 끝 포함 여부에 주의하세요.")

def c5l2_lin(r):
    p, q, s = r.randint(2, 3), nz(r, -5, 5), r.randint(1, 9)
    lo, hi = F(-s - q, p), F(s - q, p)
    if lo.denominator != 1 or hi.denominator != 1: return None
    return fill(f"|{p}x{term(q)}| ≤ {s}의 해는 {{{{1}}}} ≤ x ≤ {{{{2}}}}", [ans(int(lo)), ans(int(hi))],
                f"−{s} ≤ {p}x{term(q)} ≤ {s}\n{m(-s - q)} ≤ {p}x ≤ {m(s - q)}\n{m(int(lo))} ≤ x ≤ {m(int(hi))}", "세 변으로 나누어 푸세요.")

def c5l2_twoabs(r):
    a, b = sorted(r.sample(range(-4, 7), 2))
    t = r.choice(["min", "solve"])
    if t == "min":
        return num(f"|x{term(-a)}| + |x{term(-b)}|의 최솟값은?", b - a,
                   f"수직선에서 x와 {m(a)}, x와 {m(b)} 사이 거리의 합입니다.\nx가 {m(a)}와 {m(b)} 사이에 있을 때 최소: {m(b)} − {par(a)} = {b - a}", "두 점까지의 거리의 합으로 생각하세요.")
    c = b - a + 2 * r.randint(1, 3)
    lo, hi = F(a + b - c, 2), F(a + b + c, 2)
    if lo.denominator != 1: return None
    return fill(f"|x{term(-a)}| + |x{term(-b)}| < {c}의 해는 {{{{1}}}} < x < {{{{2}}}}", [ans(int(lo)), ans(int(hi))],
                f"x < {m(a)}: −2x + {m(a + b)} < {c} → x > {m(int(lo))}\n{m(a)} ≤ x < {m(b)}: {b - a} < {c} 항상 성립\nx ≥ {m(b)}: 2x − {m(a + b)} < {c} → x < {m(int(hi))}\n합치면 {m(int(lo))} < x < {m(int(hi))}".replace("− −", "+ ").replace("+ −", "− "),
                "꺾이는 점을 기준으로 구간을 나누세요.")

def c5l2_center(r):
    a, k = r.randint(-4, 6), r.randint(1, 4)
    return num(f"|x − a| < {k}의 해가 {m(a - k)} < x < {m(a + k)}일 때 a의 값은?", a,
               f"|x − a| < {k} ⇔ a − {k} < x < a + {k}\na − {k} = {m(a - k)} → a = {m(a)}", "해 구간의 가운데가 a입니다.")

L52 = [("|x − a|와 부등식", c5l2_basic), ("정수의 개수", c5l2_count), ("|px + q| ≤ s", c5l2_lin), ("절댓값 두 개", c5l2_twoabs), ("해로 a 구하기", c5l2_center)]

def c5l3_fac(r):
    a, b = sorted(r.sample(range(-5, 7), 2))
    t = r.choice(["lt", "le", "ge", "cnt"])
    pe = poly((1, 'x²'), (-(a + b), 'x'), (a * b, ''))
    if t in ("lt", "le"):
        o = "<" if t == "lt" else "≤"
        return fill(f"{pe} {o} 0의 해는 {{{{1}}}} {o} x {o} {{{{2}}}}", [ans(a), ans(b)],
                    f"인수분해: (x{term(-a)})(x{term(-b)}) {o} 0\n아래로 볼록한 포물선이 x축 아래(또는 위에 닿는) 부분 → 두 근 사이\n{m(a)} {o} x {o} {m(b)}", "(x − α)(x − β) < 0 ⇔ α < x < β")
    if t == "ge":
        return fill(f"{pe} ≥ 0의 해는 x ≤ {{{{1}}}} 또는 x ≥ {{{{2}}}}", [ans(a), ans(b)],
                    f"(x{term(-a)})(x{term(-b)}) ≥ 0\n두 근의 바깥쪽 → x ≤ {m(a)} 또는 x ≥ {m(b)}", "(x − α)(x − β) > 0 ⇔ 두 근의 바깥")
    return num(f"{pe} < 0을 만족하는 정수 x는 몇 개일까요?", b - a - 1,
               f"(x{term(-a)})(x{term(-b)}) < 0 → {m(a)} < x < {m(b)}\n정수 {b - a - 1}개", "두 근 사이의 정수를 세세요.")

def c5l3_neg(r):
    a, b = sorted(r.sample(range(-4, 6), 2))
    return fill(f"{poly((-1, 'x²'), (a + b, 'x'), (-a * b, ''))} > 0의 해는 {{{{1}}}} < x < {{{{2}}}}", [ans(a), ans(b)],
                f"양변에 −1을 곱하면 부등호가 바뀝니다: {poly((1, 'x²'), (-(a + b), 'x'), (a * b, ''))} < 0\n(x{term(-a)})(x{term(-b)}) < 0 → {m(a)} < x < {m(b)}", "x²의 계수를 양수로 만드세요.")

def c5l3_always(r):
    c = r.randint(1, 6)
    t = r.choice(["cnt", "max"])
    if t == "cnt":
        return num(f"x² + kx + {c * c} > 0이 모든 실수 x에 대해 성립하는 정수 k는 몇 개일까요?", 4 * c - 1,
                   f"항상 양수 ⇔ D < 0: k² − {4 * c * c} < 0 ⇔ −{2 * c} < k < {2 * c}\n정수 k는 {4 * c - 1}개", "판별식 D < 0")
    return num(f"x² − 2kx + {c * c} ≥ 0이 모든 실수 x에 대해 성립하는 k의 최댓값은?", c,
               f"D/4 = k² − {c * c} ≤ 0 ⇔ −{c} ≤ k ≤ {c}\n최댓값 {c}", "D ≤ 0")

def c5l3_make(r):
    a, b = sorted(r.sample(range(-4, 8), 2))
    return fill(f"해가 {m(a)} < x < {m(b)}인 이차부등식은 x² + {{{{1}}}}x + {{{{2}}}} < 0", [ans(-(a + b)), ans(a * b)],
                f"(x{term(-a)})(x{term(-b)}) < 0을 전개합니다.\n{poly((1, 'x²'), (-(a + b), 'x'), (a * b, ''))} < 0", "해가 α < x < β ⇔ (x − α)(x − β) < 0")

def c5l3_sys(r):
    a, b = sorted(r.sample(range(-3, 7), 2)); c = r.randint(2, 5)
    S = [x for x in range(-10, 11) if a < x < b and x * x < c * c]
    return num(f"연립부등식 {poly((1, 'x²'), (-(a + b), 'x'), (a * b, ''))} < 0, x² − {c * c} < 0을 만족하는 정수 x는 몇 개일까요?", len(S),
               f"첫째: {m(a)} < x < {m(b)}\n둘째: −{c} < x < {c}\n공통: {m(max(a, -c))} < x < {m(min(b, c))}\n정수: {', '.join(m(z) for z in S) if S else '없음'} → {len(S)}개",
               "각각 풀고 공통 범위를 찾으세요.")

def c5l3_word(r):
    s = r.choice([8, 10, 12, 14]); k = r.randint(2, s // 2 - 1); A = k * (s - k)
    S = [x for x in range(1, s) if x * (s - x) >= A]
    return num(f"가로 x, 세로 {s} − x인 직사각형의 넓이가 {A} 이상이 되는 자연수 x는 몇 개일까요?", len(S),
               f"x({s} − x) ≥ {A} → x² − {s}x + {A} ≤ 0 → (x − {k})(x − {s - k}) ≤ 0\n{k} ≤ x ≤ {s - k} → {len(S)}개", "부등식을 세워 정리하세요.")

L53 = [("인수분해형 이차부등식", c5l3_fac), ("x²의 계수가 음수", c5l3_neg), ("항상 성립할 조건", c5l3_always), ("해로 부등식 만들기", c5l3_make),
       ("연립 이차부등식", c5l3_sys), ("이차부등식의 활용", c5l3_word)]

def c5l4_coef(r):
    a, b = sorted(r.sample(range(-4, 7), 2))
    ask = r.choice(["a", "b"])
    return num(f"x² + ax + b < 0의 해가 {m(a)} < x < {m(b)}일 때 {ask}의 값은?", -(a + b) if ask == "a" else a * b,
               f"해가 {m(a)} < x < {m(b)} ⇔ (x{term(-a)})(x{term(-b)}) < 0 ⇔ {poly((1, 'x²'), (-(a + b), 'x'), (a * b, ''))} < 0\na = {m(-(a + b))}, b = {m(a * b)}", "(x − α)(x − β) < 0을 전개해 비교하세요.")

def c5l4_neg(r):
    p, q = r.randint(1, 4), r.randint(1, 5)
    # ax² + bx + c > 0 해 −p < x < q, c 주어짐: a(x + p)(x − q) = a x² + a(p − q) x − a p q, a < 0
    k = r.randint(1, 3); a = -k; c = -a * p * q; b = a * (p - q)
    ask = r.choice(["a", "b"])
    return num(f"ax² + bx + {c} > 0의 해가 −{p} < x < {q}일 때 {ask}의 값은?", a if ask == "a" else b,
               f"해가 두 근 사이이므로 a < 0이고 ax² + bx + {c} = a(x + {p})(x − {q})\n상수항 비교: −{p * q}a = {c} → a = {m(a)}\nx의 계수: b = a({p} − {q}) = {m(b)}",
               "a(x − α)(x − β) 꼴로 놓고 계수를 비교하세요.")

def c5l4_real(r):
    a = r.randint(1, 5)
    t = r.choice(["real", "sign"])
    if t == "real":
        return num(f"x² + {2 * a}x + k = 0이 실근을 가지는 k의 최댓값은?", a * a,
                   f"실근 ⇔ D/4 = {a * a} − k ≥ 0 ⇔ k ≤ {a * a}\n최댓값 {a * a}", "D ≥ 0")
    c = r.randint(1, 6)
    return num(f"x² + x + k − {c} = 0의 두 근의 부호가 서로 다를 때 정수 k의 최댓값은?", c - 1,
               f"두 근의 부호가 다르면 두 근의 곱 < 0\nk − {c} < 0 → k < {c}\n정수 k의 최댓값 {c - 1}", "부호가 다른 두 근 ⇔ 곱 < 0")

def c5l4_ball(r):
    t1, t2 = r.choice([(1, 3), (1, 2), (2, 3), (1, 4), (2, 4), (1, 5)])
    v = 5 * (t1 + t2); H = 5 * t1 * t2
    return num(f"위로 던진 공의 t초 후 높이가 ({v}t − 5t²)m입니다. 높이가 {H}m 이상인 시간은 몇 초 동안일까요?", t2 - t1,
               f"{v}t − 5t² ≥ {H} → 5t² − {v}t + {H} ≤ 0 → t² − {t1 + t2}t + {t1 * t2} ≤ 0\n(t − {t1})(t − {t2}) ≤ 0 → {t1} ≤ t ≤ {t2}\n{t2 - t1}초 동안", "부등식을 세워 5로 나누세요.")

def c5l4_int(r):
    k = r.randint(2, 6)
    return num(f"|x| < a를 만족하는 정수가 {2 * k - 1}개일 때 자연수 a의 값은?", k,
               f"|x| < a ⇔ −a < x < a, 정수는 −(a − 1)부터 a − 1까지 2a − 1개\n2a − 1 = {2 * k - 1} → a = {k}", "−a < x < a의 정수 개수는 2a − 1")

L54 = [("해로 계수 구하기", c5l4_coef), ("x²의 계수가 음수인 경우", c5l4_neg), ("근의 조건", c5l4_real), ("던진 공의 높이", c5l4_ball), ("정수 개수로 a 구하기", c5l4_int)]

# ================= ch06 경우의 수 =================
def c6l1_sum(r):
    a, b = r.randint(2, 6), r.randint(2, 6)
    t = r.choice(["sum", "prod"])
    if t == "sum":
        return num(f"버스로 가는 방법이 {a}가지, 기차로 가는 방법이 {b}가지일 때 가는 방법은 모두 몇 가지일까요?", a + b,
                   f"버스와 기차는 동시에 일어나지 않으므로 합의 법칙\n{a} + {b} = {a + b}가지", "동시에 일어나지 않으면 더합니다.")
    c = r.randint(2, 4)
    return num(f"A에서 B로 가는 길이 {a}가지, B에서 C로 가는 길이 {b}가지, C에서 D로 가는 길이 {c}가지입니다. A에서 D로 가는 방법은?", a * b * c,
               f"A→B, B→C, C→D를 연이어 하므로 곱의 법칙\n{a} × {b} × {c} = {a * b * c}가지", "잇달아 일어나면 곱합니다.")

def c6l1_dice(r):
    t = r.choice(["sum", "even", "odd", "mult"])
    if t == "sum":
        s1, s2 = r.sample(range(2, 13), 2)
        c = lambda s: sum(1 for i in range(1, 7) for j_ in range(1, 7) if i + j_ == s)
        return num(f"주사위 두 개를 던질 때 눈의 합이 {s1} 또는 {s2}인 경우는 몇 가지일까요?", c(s1) + c(s2),
                   f"합이 {s1}: {c(s1)}가지, 합이 {s2}: {c(s2)}가지\n동시에 일어날 수 없으므로 {c(s1)} + {c(s2)} = {c(s1) + c(s2)}가지", "각각 세어 더하세요.")
    if t == "even": return num("주사위 두 개를 던질 때 두 눈이 모두 짝수인 경우는 몇 가지일까요?", 9, "각 주사위의 짝수 눈: 2, 4, 6 → 3가지\n3 × 3 = 9가지", "곱의 법칙")
    if t == "odd": return num("주사위 두 개를 던질 때 눈의 곱이 홀수인 경우는 몇 가지일까요?", 9, "곱이 홀수 ⇔ 두 눈 모두 홀수(1, 3, 5)\n3 × 3 = 9가지", "곱이 홀수이려면 둘 다 홀수")
    k = r.choice([2, 3, 4, 5, 6])
    v = sum(1 for i in range(1, 7) for j_ in range(1, 7) if (i + j_) % k == 0)
    return num(f"주사위 두 개를 던질 때 눈의 합이 {k}의 배수인 경우는 몇 가지일까요?", v,
               f"합이 될 수 있는 {k}의 배수: {', '.join(str(s) for s in range(k, 13, k))}\n각각의 경우를 더하면 {v}가지", "가능한 합을 나누어 세세요.")

def c6l1_div(r):
    n = r.choice([24, 36, 48, 60, 72, 90, 100, 120, 144, 180, 200])
    f = factor(n); v = 1
    for e in f.values(): v *= e + 1
    return num(f"{n}의 약수는 몇 개일까요?", v,
               f"{n} = {fstr(f)}\n각 소인수를 고르는 방법: " + " × ".join(f"({e} + 1)" for e in f.values()) + f" = {v}", "소인수분해 후 (지수 + 1)을 곱하세요.")

def c6l1_digits(r):
    k = r.randint(3, 5); t = r.choice(["rep", "norep", "zero"])
    ds = list(range(1, k + 1))
    if t == "rep":
        return num(f"{', '.join(map(str, ds))}로 세 자리 수를 만들 때(같은 숫자 사용 가능) 모두 몇 개일까요?", k ** 3,
                   f"각 자리에 {k}가지씩\n{k} × {k} × {k} = {k ** 3}개", "자리마다 고를 수 있는 숫자 수를 곱하세요.")
    if t == "norep":
        return num(f"{', '.join(map(str, ds))}로 세 자리 수를 만들 때(같은 숫자 사용 불가) 모두 몇 개일까요?", k * (k - 1) * (k - 2),
                   f"백의 자리 {k}가지, 십의 자리 {k - 1}가지, 일의 자리 {k - 2}가지\n{k} × {k - 1} × {k - 2} = {k * (k - 1) * (k - 2)}개", "한 번 쓴 숫자는 빼고 세세요.")
    ds = list(range(0, k + 1))
    return num(f"{', '.join(map(str, ds))}로 세 자리 수를 만들 때(같은 숫자 사용 불가) 모두 몇 개일까요?", k * k * (k - 1),
               f"백의 자리에는 0이 올 수 없으므로 {k}가지\n십의 자리: 남은 {k}개, 일의 자리: {k - 1}개\n{k} × {k} × {k - 1} = {k * k * (k - 1)}개", "맨 앞자리에 0이 올 수 없습니다.")

def c6l1_color(r):
    c = r.randint(3, 6); n = r.randint(3, 4)
    v = c * (c - 1) ** (n - 1)
    return num(f"일렬로 붙은 {n}개 영역을 {c}가지 색으로 칠합니다. 이웃한 영역은 다른 색으로 칠할 때 방법은? (같은 색 여러 번 사용 가능)", v,
               f"첫 영역 {c}가지, 이후 영역은 바로 앞 영역의 색만 빼고 {c - 1}가지씩\n{c} × {c - 1}{sup(n - 1)} = {v}", "앞 영역과만 다르면 됩니다.")

def c6l1_pay(r):
    a, b = r.randint(1, 3), r.randint(1, 4)
    t = r.choice(["way", "amount"])
    if t == "way":
        return num(f"1,000원 지폐 {a}장과 100원 동전 {b}개의 일부 또는 전부로 지불하는 방법은 몇 가지일까요? (0원 제외)", (a + 1) * (b + 1) - 1,
                   f"지폐 0~{a}장: {a + 1}가지, 동전 0~{b}개: {b + 1}가지\n({a + 1}) × ({b + 1}) − 1(0원) = {(a + 1) * (b + 1) - 1}", "각각 0개부터 선택할 수 있습니다.")
    v = len({1000 * i + 500 * k for i in range(a + 1) for k in range(b + 1)} - {0})
    return num(f"1,000원 지폐 {a}장과 500원 동전 {b}개로 지불할 수 있는 금액은 몇 가지일까요? (0원 제외)", v,
               f"500원 동전 2개 = 1,000원이므로 금액이 겹칩니다.\n지폐를 모두 500원으로 바꾸면 500원짜리 {2 * a + b}개 → 500원 ~ {500 * (2 * a + b):,}원\n{2 * a + b}가지", "금액이 겹치는지 확인하세요.")

L61 = [("합과 곱의 법칙", c6l1_sum), ("주사위 두 개", c6l1_dice), ("약수의 개수", c6l1_div), ("숫자 만들기", c6l1_digits), ("색칠하기", c6l1_color), ("지불 방법과 금액", c6l1_pay)]

def c6l2_val(r):
    t = r.choice(["P", "fact", "solve"])
    if t == "P":
        n = r.randint(4, 9); k = r.randint(2, min(4, n))
        return num(f"₍{n}₎P₍{k}₎의 값은?".replace("₍", "").replace("₎", "") if False else f"{n}P{k}의 값은?  (서로 다른 {n}개에서 {k}개를 택하는 순열)", perm(n, k),
                   f"{n}P{k} = {' × '.join(str(n - i) for i in range(k))} = {perm(n, k)}", "n부터 1씩 줄여 k개를 곱하세요.")
    if t == "fact":
        n = r.randint(3, 7)
        return num(f"{n}!의 값은?", factorial(n), f"{n}! = {' × '.join(str(i) for i in range(n, 0, -1))} = {factorial(n)}", "n!은 1부터 n까지의 곱")
    n = r.randint(4, 12)
    return num(f"nP2 = {n * (n - 1)}일 때 자연수 n의 값은?", n,
               f"nP2 = n(n − 1) = {n * (n - 1)}\n연속한 두 자연수의 곱이 {n * (n - 1)} → {n} × {n - 1}\nn = {n}", "n(n − 1)로 나타내세요.")

def c6l2_line(r):
    n = r.randint(4, 7); t = r.choice(["adj", "nonadj", "front", "ends"])
    if t == "adj":
        v = factorial(n - 1) * 2
        return num(f"A, B를 포함한 {n}명을 일렬로 세울 때 A와 B가 이웃하는 방법은?", v,
                   f"A, B를 한 묶음으로 보면 {n - 1}명 → {n - 1}! = {factorial(n - 1)}\n묶음 안에서 A, B 순서 2가지\n{factorial(n - 1)} × 2 = {v}", "이웃하는 것은 한 묶음으로 보세요.")
    if t == "nonadj":
        v = factorial(n) - factorial(n - 1) * 2
        return num(f"A, B를 포함한 {n}명을 일렬로 세울 때 A와 B가 이웃하지 않는 방법은?", v,
                   f"전체 {n}! = {factorial(n)}\n이웃하는 경우 {n - 1}! × 2 = {factorial(n - 1) * 2}\n{factorial(n)} − {factorial(n - 1) * 2} = {v}", "전체 − 이웃하는 경우")
    if t == "front":
        return num(f"{n}명을 일렬로 세울 때 A가 맨 앞에 서는 방법은?", factorial(n - 1),
                   f"A를 맨 앞에 고정하고 나머지 {n - 1}명을 세웁니다.\n{n - 1}! = {factorial(n - 1)}", "고정된 사람은 빼고 세세요.")
    return num(f"{n}명을 일렬로 세울 때 양 끝에 A와 B가 서는 방법은?", 2 * factorial(n - 2),
               f"양 끝에 A, B를 세우는 방법 2가지(A…B, B…A)\n가운데 {n - 2}명: {n - 2}! = {factorial(n - 2)}\n2 × {factorial(n - 2)} = {2 * factorial(n - 2)}", "양 끝을 먼저 정하세요.")

def c6l2_gap(r):
    b, g = r.randint(3, 5), r.randint(2, 3)
    if g > b + 1: return None
    v = factorial(b) * perm(b + 1, g)
    return num(f"남자 {b}명, 여자 {g}명을 일렬로 세울 때 여자끼리 이웃하지 않는 방법은?", v,
               f"남자 {b}명을 먼저 세움: {b}! = {factorial(b)}\n남자 사이와 양 끝 {b + 1}자리 중 {g}곳에 여자를 세움: {b + 1}P{g} = {perm(b + 1, g)}\n{factorial(b)} × {perm(b + 1, g)} = {v}",
               "이웃하면 안 되는 사람은 나중에 사이사이에 넣으세요.")

def c6l2_num(r):
    k = r.randint(4, 6); t = r.choice(["even5", "zero3", "zero3even"])
    if t == "even5":
        ds = list(range(1, k + 1)); ev = len([d for d in ds if d % 2 == 0])
        return num(f"1부터 {k}까지 숫자를 한 번씩 모두 써서 만드는 {k}자리 짝수는 몇 개일까요?", ev * factorial(k - 1),
                   f"일의 자리에 짝수 {ev}가지\n나머지 {k - 1}자리: ({k - 1})! = {factorial(k - 1)}\n{ev} × {factorial(k - 1)} = {ev * factorial(k - 1)}", "일의 자리를 먼저 정하세요.")
    ds = list(range(0, k))
    if t == "zero3":
        v = (k - 1) * (k - 1) * (k - 2)
        return num(f"{', '.join(map(str, ds))}로 만드는 세 자리 수(같은 숫자 사용 불가)는 몇 개일까요?", v,
                   f"백의 자리: 0 제외 {k - 1}가지\n십의 자리: {k - 1}가지, 일의 자리: {k - 2}가지\n{k - 1} × {k - 1} × {k - 2} = {v}", "맨 앞자리에 0이 올 수 없습니다.")
    evens = [d for d in ds if d % 2 == 0]
    v = (k - 1) * (k - 2) + (len(evens) - 1) * (k - 2) * (k - 2)
    return num(f"{', '.join(map(str, ds))}로 만드는 세 자리 짝수(같은 숫자 사용 불가)는 몇 개일까요?", v,
               f"일의 자리가 0: 백 {k - 1} × 십 {k - 2} = {(k - 1) * (k - 2)}\n일의 자리가 0이 아닌 짝수({len(evens) - 1}가지): 백(0과 그 수 제외) {k - 2} × 십 {k - 2} = {(len(evens) - 1) * (k - 2) * (k - 2)}\n합 {v}",
               "일의 자리가 0인 경우와 아닌 경우로 나누세요.")

def c6l2_word(r):
    w = r.choice(["MATH", "CODE", "STAR", "LOVE", "BRAIN", "PLANT", "MUSIC"])
    n = len(w); t = r.choice(["all", "order"])
    if t == "all":
        return num(f"{w}의 {n}글자를 일렬로 늘어놓는 방법은?", factorial(n), f"서로 다른 {n}개의 순열: {n}! = {factorial(n)}", "모두 다른 글자입니다.")
    a, b = w[0], w[-1]
    return num(f"{w}의 글자를 일렬로 늘어놓을 때 {a}{'이' if a in 'LMNR' else '가'} {b}보다 앞에 오는 방법은?", factorial(n) // 2,
               f"전체 {n}! = {factorial(n)}\n{a}{'이' if a in 'LMNR' else '가'} 앞인 경우와 {b}{'이' if b in 'LMNR' else '가'} 앞인 경우는 같은 수이므로 절반\n{factorial(n)} ÷ 2 = {factorial(n) // 2}", "대칭을 이용하세요.")

L62 = [("순열의 값", c6l2_val), ("이웃하기·위치 고정", c6l2_line), ("이웃하지 않게", c6l2_gap), ("숫자 만들기", c6l2_num), ("글자 배열", c6l2_word)]

def c6l3_val(r):
    t = r.choice(["C", "solve", "sym"])
    if t == "C":
        n = r.randint(5, 10); k = r.randint(2, 4)
        return num(f"{n}C{k}의 값은?  (서로 다른 {n}개에서 {k}개를 택하는 조합)", comb(n, k),
                   f"{n}C{k} = {n}P{k} ÷ {k}! = {perm(n, k)} ÷ {factorial(k)} = {comb(n, k)}", "nCr = nPr ÷ r!")
    if t == "solve":
        n = r.randint(4, 12)
        return num(f"nC2 = {comb(n, 2)}일 때 자연수 n의 값은?", n,
                   f"nC2 = n(n − 1)/2 = {comb(n, 2)} → n(n − 1) = {n * (n - 1)}\nn = {n}", "n(n − 1)/2로 나타내세요.")
    n = r.randint(8, 15); k = n - r.randint(1, 3)
    return num(f"{n}C{k}의 값은?", comb(n, k),
               f"nCr = nC(n−r)이므로 {n}C{k} = {n}C{n - k}\n= {comb(n, n - k)}", "nCr = nC(n − r)")

def c6l3_inc(r):
    n, k = r.randint(6, 10), r.randint(2, 4)
    t = r.choice(["in", "out", "atleast"])
    if t == "in":
        return num(f"{n}명 중 {k}명을 뽑을 때 A가 반드시 포함되는 방법은?", comb(n - 1, k - 1),
                   f"A를 먼저 뽑고 나머지 {n - 1}명 중 {k - 1}명\n{n - 1}C{k - 1} = {comb(n - 1, k - 1)}", "A를 먼저 뽑아 두세요.")
    if t == "out":
        return num(f"{n}명 중 {k}명을 뽑을 때 A가 포함되지 않는 방법은?", comb(n - 1, k),
                   f"A를 빼고 {n - 1}명 중 {k}명\n{n - 1}C{k} = {comb(n - 1, k)}", "A를 제외하고 고르세요.")
    b, g = r.randint(3, 6), r.randint(2, 5)
    v = comb(b + g, k) - comb(b, k)
    return num(f"남학생 {b}명, 여학생 {g}명 중 {k}명을 뽑을 때 여학생이 적어도 한 명 포함되는 방법은?", v,
               f"전체 {b + g}C{k} = {comb(b + g, k)}\n남학생만 뽑는 경우 {b}C{k} = {comb(b, k)}\n{comb(b + g, k)} − {comb(b, k)} = {v}", "전체 − (여학생이 없는 경우)")

def c6l3_mix(r):
    b, g, x, y = r.randint(3, 6), r.randint(3, 5), r.randint(1, 3), r.randint(1, 3)
    if x > b or y > g: return None
    return num(f"남학생 {b}명, 여학생 {g}명 중 남학생 {x}명, 여학생 {y}명을 뽑는 방법은?", comb(b, x) * comb(g, y),
               f"{b}C{x} × {g}C{y} = {comb(b, x)} × {comb(g, y)} = {comb(b, x) * comb(g, y)}", "따로 뽑아 곱하세요.")

def c6l3_geo(r):
    t = r.choice(["tri", "diag", "para", "line"])
    if t == "tri":
        n = r.randint(5, 10)
        return num(f"원 위의 {n}개 점으로 만들 수 있는 삼각형은 몇 개일까요?", comb(n, 3),
                   f"원 위의 세 점은 한 직선 위에 있지 않으므로 3개를 고르면 삼각형\n{n}C3 = {comb(n, 3)}", "세 점을 고르는 조합")
    if t == "diag":
        n = r.randint(5, 12)
        return num(f"{n}각형의 대각선은 몇 개일까요?", comb(n, 2) - n,
                   f"두 꼭짓점을 잇는 선분 {n}C2 = {comb(n, 2)}개 중 변 {n}개를 뺍니다.\n{comb(n, 2)} − {n} = {comb(n, 2) - n}", "선분 − 변")
    if t == "para":
        a, b = r.randint(3, 6), r.randint(3, 5)
        return num(f"평행한 직선 {a}개와 이들과 만나는 다른 방향의 평행한 직선 {b}개로 만들어지는 평행사변형은 몇 개일까요?", comb(a, 2) * comb(b, 2),
                   f"각 방향에서 2개씩 고르면 평행사변형 하나\n{a}C2 × {b}C2 = {comb(a, 2)} × {comb(b, 2)} = {comb(a, 2) * comb(b, 2)}", "각 방향에서 두 직선씩")
    n = r.randint(5, 10)
    return num(f"어느 세 점도 한 직선 위에 있지 않은 {n}개의 점으로 만들 수 있는 직선은 몇 개일까요?", comb(n, 2),
               f"두 점이 직선 하나를 결정합니다.\n{n}C2 = {comb(n, 2)}", "두 점을 고르는 조합")

def c6l3_group(r):
    n, k = r.choice([(4, 2), (6, 2), (6, 3), (8, 4), (9, 3)])
    g = n // k
    v = 1
    for i in range(g): v *= comb(n - i * k, k)
    v //= factorial(g)
    return num(f"{n}명을 {k}명씩 {g}개 조로 나누는 방법은? (조 이름 없음)", v,
               f"차례로 뽑으면 " + " × ".join(f"{n - i * k}C{k}" for i in range(g)) + f"\n크기가 같은 조 {g}개는 순서가 없으므로 {g}!로 나눕니다.\n= {v}", "똑같은 크기의 조는 순서를 지워야 합니다.")

L63 = [("조합의 값", c6l3_val), ("특정인 포함·제외", c6l3_inc), ("남녀 나누어 뽑기", c6l3_mix), ("도형과 조합", c6l3_geo), ("조 나누기", c6l3_group)]

def c6l4_circle(r):
    n = r.randint(4, 8); t = r.choice(["basic", "adj"])
    if t == "basic":
        return num(f"{n}명이 원탁에 앉는 방법은?", factorial(n - 1),
                   f"원순열: 회전해서 같은 것을 하나로 봅니다.\n({n} − 1)! = {factorial(n - 1)}", "원순열은 (n − 1)!")
    return num(f"{n}명이 원탁에 앉을 때 특정한 2명이 이웃하는 방법은?", factorial(n - 2) * 2,
               f"2명을 한 묶음 → {n - 1}개의 원순열 {n - 2}! = {factorial(n - 2)}\n묶음 안 순서 2\n{factorial(n - 2)} × 2 = {factorial(n - 2) * 2}", "묶음을 하나로 보고 원순열")

def c6l4_multi(r):
    w = r.choice(["AABB", "AAAB", "BANANA", "APPLE", "LEVEL", "SEESAW", "COFFEE", "AABBC", "PAPER", "TOMATO"])
    from collections import Counter
    c = Counter(w); v = factorial(len(w))
    for x in c.values(): v //= factorial(x)
    rep = [f"{k} {x}개" for k, x in c.items() if x > 1]
    return num(f"{w}의 {len(w)}글자를 일렬로 늘어놓는 방법은?", v,
               f"같은 것이 있는 순열: {len(w)}! ÷ (" + " × ".join(f"{x}!" for x in c.values() if x > 1) + f")\n({', '.join(rep)})\n= {factorial(len(w))} ÷ {factorial(len(w)) // v} = {v}",
               "같은 글자끼리 바꾼 것은 같은 배열입니다.")

def c6l4_grid(r):
    a, b = r.randint(2, 6), r.randint(2, 5)
    return num(f"가로로 {a}칸, 세로로 {b}칸 가는 격자 최단 경로는 몇 가지일까요?", comb(a + b, a),
               f"→ {a}번, ↑ {b}번을 늘어놓는 방법\n({a + b})! ÷ ({a}! × {b}!) = {a + b}C{a} = {comb(a + b, a)}", "같은 것이 있는 순열로 보세요.")

def c6l4_func(r):
    n, k = r.randint(3, 5), r.randint(2, 4)
    t = r.choice(["letters", "signal", "ball"])
    if t == "letters":
        return num(f"서로 다른 편지 {n}통을 {k}명에게 나눠 주는 방법은? (한 통도 못 받는 사람이 있어도 됨)", k ** n,
                   f"편지마다 {k}명 중 한 명을 고릅니다.\n{k}{sup(n)} = {k ** n}", "중복순열: 대상마다 선택지 수를 곱하세요.")
    if t == "signal":
        return num(f"0과 1로 만들 수 있는 {n + 1}자리 신호는 몇 가지일까요? (맨 앞 0 가능)", 2 ** (n + 1),
                   f"각 자리마다 2가지\n2{sup(n + 1)} = {2 ** (n + 1)}", "중복순열")
    return num(f"서로 다른 공 {n}개를 서로 다른 상자 2개에 넣는 방법은? (빈 상자가 없도록)", 2 ** n - 2,
               f"공마다 상자 2개 중 하나: 2{sup(n)} = {2 ** n}\n한 상자에 모두 넣는 2가지를 뺍니다.\n{2 ** n} − 2 = {2 ** n - 2}", "빈 상자가 생기는 경우를 빼세요.")

def c6l4_H(r):
    n, k = r.randint(2, 4), r.randint(3, 7)
    t = r.choice(["drink", "nonneg", "pos", "apple"])
    if t == "drink":
        return num(f"{n}종류의 음료 중에서 중복을 허락해 {k}잔을 고르는 방법은?", comb(n + k - 1, k),
                   f"중복조합 {n}H{k} = {n + k - 1}C{k} = {comb(n + k - 1, k)}", "nHr = (n + r − 1)Cr")
    if t == "nonneg":
        return num(f"x + y + z = {k}를 만족하는 음이 아닌 정수해는 몇 쌍일까요?", comb(k + 2, 2),
                   f"x, y, z 세 종류 중 중복을 허락해 {k}개 고르기\n3H{k} = {k + 2}C{k} = {comb(k + 2, 2)}", "중복조합")
    if t == "pos":
        return num(f"x + y + z = {k}를 만족하는 자연수해는 몇 쌍일까요?", comb(k - 1, 2),
                   f"x = x' + 1 … 로 바꾸면 x' + y' + z' = {k - 3} (음이 아닌 정수)\n3H{k - 3} = {k - 1}C{k - 3} = {comb(k - 1, 2)}", "먼저 1씩 나누어 주세요.")
    return num(f"똑같은 사과 {k}개를 {n}명에게 나눠 주는 방법은? (못 받는 사람이 있어도 됨)", comb(n + k - 1, k),
               f"{n}명 중 중복을 허락해 {k}번 고르는 것과 같습니다.\n{n}H{k} = {n + k - 1}C{k} = {comb(n + k - 1, k)}", "같은 물건 나누기는 중복조합")

def c6l4_binom(r):
    a, n = r.choice([1, 2, 3]), r.randint(4, 6); k = r.randint(1, n - 1)
    v = comb(n, k) * a ** k
    return num(f"({'' if a == 1 else a}x + 1){sup(n)}의 전개식에서 x{sup(k) if k > 1 else ''}의 계수는?", v,
               f"일반항: {n}C{k} × ({'' if a == 1 else a}x){sup(k) if k > 1 else ''} × 1{sup(n - k)}\n계수: {n}C{k} × {a}{sup(k)} = {comb(n, k)} × {a ** k} = {v}".replace("¹", ""), "이항정리 일반항 nCr aʳ")

L64 = [("원순열", c6l4_circle), ("같은 것이 있는 순열", c6l4_multi), ("최단 경로", c6l4_grid), ("중복순열", c6l4_func), ("중복조합", c6l4_H), ("이항계수", c6l4_binom)]

# ================= ch07 행렬 =================
def M(a): return "[" + " ; ".join(" ".join(m(x) for x in row) for row in a) + "]"
def rnd(r, lo=-4, hi=6, n=2, k=2): return [[r.randint(lo, hi) for _ in range(k)] for _ in range(n)]

def c7l1_rule(r):
    rules = [("i + j", lambda i, j_: i + j_), ("i × j", lambda i, j_: i * j_), ("2i − j", lambda i, j_: 2 * i - j_), ("i − j", lambda i, j_: i - j_), ("i² − j", lambda i, j_: i * i - j_)]
    nm, f = r.choice(rules); n, k = r.choice([(2, 2), (2, 3), (3, 2), (3, 3)])
    A = [[f(i, j_) for j_ in range(1, k + 1)] for i in range(1, n + 1)]
    t = r.choice(["entry", "sum"])
    if t == "entry":
        i, j_ = r.randint(1, n), r.randint(1, k)
        return num(f"aᵢⱼ = {nm}인 {n} × {k} 행렬의 ({i}, {j_}) 성분은?", A[i - 1][j_ - 1],
                   f"({i}, {j_}) 성분은 i = {i}, j = {j_}를 대입: {nm.replace('i', str(i)).replace('j', str(j_))} = {m(A[i - 1][j_ - 1])}\n(전체 행렬 {M(A)})", "i는 행, j는 열 번호입니다.")
    return num(f"aᵢⱼ = {nm}인 {n} × {k} 행렬의 성분을 모두 더하면?", sum(map(sum, A)),
               f"행렬을 구하면 {M(A)}\n성분의 합: {m(sum(map(sum, A)))}", "모든 (i, j)에 대해 계산하세요.")

def c7l1_eq(r):
    x, y = r.randint(-5, 6), r.randint(-5, 6); b, c = r.randint(-3, 5), r.randint(-3, 5)
    t = r.choice(["xy", "ab"])
    if t == "xy":
        return num(f"[x {m(b)} ; {m(c)} y] = {M([[x, b], [c, y]])}일 때 x + y의 값은?", x + y,
                   f"두 행렬이 같으면 같은 위치의 성분이 모두 같습니다.\nx = {m(x)}, y = {m(y)}\nx + y = {m(x + y)}", "같은 위치끼리 비교하세요.")
    s, d = x + y, x - y
    ask = r.choice(["a", "b"])
    return num(f"[a + b {m(b)} ; {m(c)} a − b] = [{m(s)} {m(b)} ; {m(c)} {m(d)}]일 때 {ask}의 값은?", x if ask == "a" else y,
               f"a + b = {m(s)}, a − b = {m(d)}\n더하면 2a = {m(s + d)} → a = {m(x)}, b = {m(y)}", "연립방정식을 세우세요.")

def c7l1_size(r):
    n, k = r.randint(1, 4), r.randint(1, 4)
    return num(f"{n} × {k} 행렬의 성분은 모두 몇 개일까요?", n * k, f"행 {n}개, 열 {k}개\n성분 수 = {n} × {k} = {n * k}", "행의 수 × 열의 수")

L71 = [("규칙으로 정한 행렬", c7l1_rule), ("서로 같은 행렬", c7l1_eq), ("행렬의 크기", c7l1_size)]

def c7l2_add(r):
    A, B = rnd(r), rnd(r); op = r.choice(["+", "−"]); k = 1 if op == "+" else -1
    C = [[A[i][j_] + k * B[i][j_] for j_ in range(2)] for i in range(2)]
    i, j_ = r.randint(0, 1), r.randint(0, 1)
    shown = [[m(C[a][b]) if (a, b) != (i, j_) else "{{1}}" for b in range(2)] for a in range(2)]
    return fill(f"{M(A)} {op} {M(B)} = [" + " ; ".join(" ".join(row) for row in shown) + "]", [ans(C[i][j_])],
                f"같은 위치끼리 {'더합니다' if k == 1 else '뺍니다'}.\n({i + 1}, {j_ + 1}) 성분: {m(A[i][j_])} {op} {par(B[i][j_])} = {m(C[i][j_])}\n결과 {M(C)}", "같은 위치의 성분끼리 계산하세요.")

def c7l2_scal(r):
    A, k = rnd(r), r.choice([-3, -2, 2, 3, 4])
    C = [[k * x for x in row] for row in A]
    t = r.choice(["sum", "entry"])
    if t == "sum":
        return num(f"A = {M(A)}일 때 {m(k)}A의 성분을 모두 더하면?", sum(map(sum, C)),
                   f"{m(k)}A = {M(C)}\n성분의 합 {m(sum(map(sum, C)))}  (= {m(k)} × {m(sum(map(sum, A)))})", "모든 성분에 k를 곱합니다.")
    p, q = r.randint(2, 4), r.randint(1, 3)
    return num(f"A = {M(A)}일 때 {p}A − {q}A의 (1, 2) 성분은?", (p - q) * A[0][1],
               f"{p}A − {q}A = {p - q}A\n(1, 2) 성분: {p - q} × {par(A[0][1])} = {m((p - q) * A[0][1])}", "동류항처럼 계산하세요.")

def c7l2_solve(r):
    X, A = rnd(r, -3, 4), rnd(r, -3, 6); k = r.choice([2, 3])
    B = [[k * X[i][j_] + A[i][j_] for j_ in range(2)] for i in range(2)]
    i, j_ = r.randint(0, 1), r.randint(0, 1)
    return num(f"{k}X + A = B, A = {M(A)}, B = {M(B)}일 때 X의 ({i + 1}, {j_ + 1}) 성분은?", X[i][j_],
               f"X = (B − A) ÷ {k}\n({i + 1}, {j_ + 1}) 성분: ({m(B[i][j_])} − {par(A[i][j_])}) ÷ {k} = {m(X[i][j_])}", "일차방정식처럼 X에 대해 푸세요.")

def c7l2_sumdiff(r):
    A, B = rnd(r, -3, 5), rnd(r, -3, 5)
    S = [[A[i][j_] + B[i][j_] for j_ in range(2)] for i in range(2)]; D = [[A[i][j_] - B[i][j_] for j_ in range(2)] for i in range(2)]
    which, i, j_ = r.choice(["A", "B"]), r.randint(0, 1), r.randint(0, 1)
    v = A[i][j_] if which == "A" else B[i][j_]
    return num(f"A + B = {M(S)}, A − B = {M(D)}일 때 {which}의 ({i + 1}, {j_ + 1}) 성분은?", v,
               f"{'두 식을 더하면 2A' if which == 'A' else '두 식을 빼면 2B'} = {M([[S[a][b] + (1 if which == 'A' else -1) * D[a][b] for b in range(2)] for a in range(2)])}\n"
               f"({i + 1}, {j_ + 1}) 성분: {m(S[i][j_] + (1 if which == 'A' else -1) * D[i][j_])} ÷ 2 = {m(v)}", "두 식을 더하거나 빼세요.")

L72 = [("덧셈과 뺄셈", c7l2_add), ("실수배", c7l2_scal), ("행렬 방정식", c7l2_solve), ("합과 차로 구하기", c7l2_sumdiff)]

def mul(A, B): return [[sum(A[i][k] * B[k][j_] for k in range(len(B))) for j_ in range(len(B[0]))] for i in range(len(A))]

def c7l3_entry(r):
    A, B = rnd(r, -3, 4), rnd(r, -3, 4); C = mul(A, B)
    i, j_ = r.randint(0, 1), r.randint(0, 1)
    shown = [[m(C[a][b]) if (a, b) != (i, j_) else "{{1}}" for b in range(2)] for a in range(2)]
    return fill(f"{M(A)}{M(B)} = [" + " ; ".join(" ".join(row) for row in shown) + "]", [ans(C[i][j_])],
                f"({i + 1}, {j_ + 1}) 성분 = A의 {i + 1}행 · B의 {j_ + 1}열\n= {m(A[i][0])}×{par(B[0][j_])} + {par(A[i][1])}×{par(B[1][j_])} = {m(C[i][j_])}\n결과 {M(C)}",
                "행 × 열을 곱해 더하세요.")

def c7l3_row(r):
    a, b, c, d = [r.randint(-3, 6) for _ in range(4)]
    return num(f"[{m(a)} {m(b)}]와 [{m(c)} ; {m(d)}]의 곱은? (1 × 1 행렬의 성분)", a * c + b * d,
               f"{m(a)}×{par(c)} + {par(b)}×{par(d)} = {m(a * c + b * d)}", "행 × 열")

def c7l3_pow(r):
    t = r.choice(["shear", "diag", "swap"])
    n = r.randint(3, 12)
    if t == "shear":
        k = r.randint(1, 4)
        return num(f"[1 {k} ; 0 1]{sup(n)}의 (1, 2) 성분은?", k * n,
                   f"[1 {k} ; 0 1]² = [1 {2 * k} ; 0 1], [1 {k} ; 0 1]³ = [1 {3 * k} ; 0 1] …\n(1, 2) 성분은 {k}씩 늘어나므로 {k} × {n} = {k * n}", "몇 번 곱해 보고 규칙을 찾으세요.")
    if t == "diag":
        p, q = r.randint(2, 3), r.randint(1, 3); n = r.randint(2, 5)
        return num(f"[{p} 0 ; 0 {q}]{sup(n)}의 (1, 1) 성분은?", p ** n,
                   f"대각행렬의 거듭제곱은 대각성분만 거듭제곱: [{p}{sup(n)} 0 ; 0 {q}{sup(n)}]\n(1, 1) 성분 {p}{sup(n)} = {p ** n}", "대각성분끼리만 곱해집니다.")
    v = 1 if n % 2 == 0 else 0
    return num(f"A = [0 1 ; 1 0]일 때 A{sup(n)}의 (1, 1) 성분은?", v,
               f"A² = [1 0 ; 0 1] = E이므로 A의 짝수 제곱은 E, 홀수 제곱은 A\n{n}은 {'짝수' if n % 2 == 0 else '홀수'} → (1, 1) 성분 {v}", "A²을 먼저 계산하세요.")

def c7l3_comm(r):
    A, B = rnd(r, -2, 3), rnd(r, -2, 3)
    AB, BA = mul(A, B), mul(B, A)
    which = r.choice(["AB", "BA"]); i, j_ = r.randint(0, 1), r.randint(0, 1)
    C = AB if which == "AB" else BA; X, Y = (A, B) if which == "AB" else (B, A)
    return num(f"A = {M(A)}, B = {M(B)}일 때 {which}의 ({i + 1}, {j_ + 1}) 성분은?", C[i][j_],
               f"{which}의 ({i + 1}, {j_ + 1}) 성분 = {which[0]}의 {i + 1}행 · {which[1]}의 {j_ + 1}열\n= {m(X[i][0])}×{par(Y[0][j_])} + {par(X[i][1])}×{par(Y[1][j_])} = {m(C[i][j_])}\n(AB와 BA는 일반적으로 다릅니다)",
               "곱하는 순서에 주의하세요.")

def c7l3_price(r):
    a, b, p, q = r.randint(1, 6), r.randint(1, 6), r.choice([500, 700, 800, 1000, 1200]), r.choice([300, 600, 900, 1500])
    return num(f"사과 {a}개, 배 {b}개를 사는 수량 [{a} {b}]와 가격 [{p} ; {q}]를 곱한 총액은?", a * p + b * q,
               f"[{a} {b}][{p} ; {q}] = {a}×{p} + {b}×{q} = {a * p} + {b * q} = {a * p + b * q}", "행 × 열")

L73 = [("곱의 성분", c7l3_entry), ("행 × 열", c7l3_row), ("거듭제곱의 규칙", c7l3_pow), ("곱하는 순서", c7l3_comm), ("곱셈의 활용", c7l3_price)]

def c7l4_det(r):
    a, b, c, d = [nz(r, -5, 6) for _ in range(4)]
    return num(f"A = {M([[a, b], [c, d]])}일 때 ad − bc의 값은?", a * d - b * c,
               f"ad − bc = {m(a)}×{par(d)} − {par(b)}×{par(c)} = {m(a * d)} − {par(b * c)} = {m(a * d - b * c)}", "ad − bc")

def c7l4_inv(r):
    while True:
        a, b, c, d = [nz(r, -4, 5) for _ in range(4)]
        if a * d - b * c in (1, -1): break
    D = a * d - b * c
    I = [[d * D, -b * D], [-c * D, a * D]]
    i, j_ = r.randint(0, 1), r.randint(0, 1)
    shown = [[m(I[x][y]) if (x, y) != (i, j_) else "{{1}}" for y in range(2)] for x in range(2)]
    return fill(f"A = {M([[a, b], [c, d]])}일 때 A⁻¹ = [" + " ; ".join(" ".join(row) for row in shown) + "]", [ans(I[i][j_])],
                f"ad − bc = {m(D)}\nA⁻¹ = (1/{m(D)})[d −b ; −c a] = (1/{m(D)}){M([[d, -b], [-c, a]])} = {M(I)}", "A⁻¹ = (1/(ad − bc))[d −b ; −c a]")

def c7l4_sys(r):
    while True:
        a, b, c, d = [nz(r, -3, 4) for _ in range(4)]
        if a * d - b * c: break
    x, y = r.randint(-4, 5), r.randint(-4, 5)
    p, q = a * x + b * y, c * x + d * y
    return fill(f"{M([[a, b], [c, d]])}[x ; y] = [{m(p)} ; {m(q)}]의 해는 x = {{{{1}}}}, y = {{{{2}}}}", [ans(x), ans(y)],
                f"연립방정식 {poly((a, 'x'), (b, 'y'))} = {m(p)}, {poly((c, 'x'), (d, 'y'))} = {m(q)}\nad − bc = {m(a * d - b * c)} ≠ 0 → 해가 하나\n풀면 x = {m(x)}, y = {m(y)}",
                "행렬식을 연립방정식으로 바꾸어 푸세요.")

def c7l4_sing(r):
    b, c, d = nz(r, -4, 5), nz(r, -4, 5), nz(r, -4, 5)
    a = F(b * c, d)
    return num(f"A = [a {m(b)} ; {m(c)} {m(d)}]의 역행렬이 없을 때 a의 값은? (기약분수 또는 정수로)", a,
               f"역행렬이 없으려면 ad − bc = 0\n{m(d)}a − {par(b)}×{par(c)} = 0 → {m(d)}a = {m(b * c)} → a = {fm(a)}", "ad − bc = 0", fmt="fraction" if a.denominator > 1 else "integer")

def c7l4_k(r):
    a, b, c = nz(r, -3, 4), nz(r, -3, 4), r.choice([2, 3])
    k = b * c
    return num(f"연립방정식 {poly((a, 'x'))} + ky = 1, {poly((a * c, 'x'), (b * c * c, 'y'))} = 5의 해가 하나로 정해지지 않는 k의 값은?" if False else
               f"연립방정식 {poly((a, 'x'))} + ky = 1, {poly((a * c, 'x'), (b * c, 'y'))} = 5의 해가 하나로 정해지지 않는 k의 값은?", b,
               f"계수행렬 [{m(a)} k ; {m(a * c)} {m(b * c)}]의 ad − bc = 0이어야 합니다.\n{m(a)}×{par(b * c)} − k×{par(a * c)} = 0 → k = {m(b)}", "계수행렬의 ad − bc = 0")

L74 = [("ad − bc", c7l4_det), ("역행렬", c7l4_inv), ("행렬로 연립방정식", c7l4_sys), ("역행렬이 없는 조건", c7l4_sing), ("해가 하나가 아닌 조건", c7l4_k)]

ALL = {"ch05": [L51, L52, L53, L54], "ch06": [L61, L62, L63, L64], "ch07": [L71, L72, L73, L74]}

if __name__ == "__main__":
    tot = 0
    for ch, Ls in ALL.items():
        for i, T in enumerate(Ls, 1):
            per = 6 if len(T) >= 7 else 8 if len(T) >= 5 else 10 if len(T) >= 4 else 14
            n = write("c1", ch, f"l0{i}", T, per=per); tot += n; print(ch, i, len(T), n)
    print("total", tot)
