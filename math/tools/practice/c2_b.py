"""코스 2 · 챕터 4~6 (이차함수, 유리함수와 무리함수, 함수로 모델링하기) — 연습 문제 은행"""
from core import *

def nz(r, a, b):
    while True:
        x = r.randint(a, b)
        if x: return x
def pt(x, y): return f"({fm(x)}, {fm(y)})"
def qd(a, b, c): return poly((a, 'x²'), (b, 'x'), (c, ''))
def vform(a, p, q):
    s = f"(x{term(-p)})²" if p else "x²"
    return ("" if a == 1 else "−" if a == -1 else m(a)) + s + term(q)
def g(x): return f"{float(x):g}"

# ================= ch04 이차함수 =================
def q1_vertex(r):
    a, p, q = r.choice([1, 2, -1, -2, 3]), r.randint(-5, 5), r.randint(-6, 6)
    t = r.choice(["std", "gen"])
    if t == "std":
        return fill(f"y = {vform(a, p, q)}의 꼭짓점은 ({{{{1}}}}, {{{{2}}}})", [ans(p), ans(q)],
                    f"y = a(x − p)² + q의 꼭짓점은 (p, q)\n여기서 p = {m(p)}, q = {m(q)} → {pt(p, q)}", "부호에 주의: (x + 3)²이면 p = −3")
    b, c = -2 * a * p, a * p * p + q
    return fill(f"y = {qd(a, b, c)}의 꼭짓점은 ({{{{1}}}}, {{{{2}}}})", [ans(p), ans(q)],
                f"완전제곱식으로 바꾸면 y = {vform(a, p, q)}\n꼭짓점 {pt(p, q)}", "x² 계수로 묶고 완전제곱식을 만드세요.")

def q1_comp(r):
    p, q = nz(r, -6, 6), r.randint(-8, 8)
    c = p * p + q
    return fill(f"y = {qd(1, -2 * p, c)} = (x{term(-p)})² + {{{{1}}}}", [ans(q)],
                f"x² {'−' if p > 0 else '+'} {abs(2 * p)}x = (x{term(-p)})² − {p * p}\ny = (x{term(-p)})² − {p * p} + {c} = (x{term(-p)})²{term(q)}", "x 계수의 절반을 제곱해 더하고 빼세요.")

def q1_int(r):
    a, b = sorted(r.sample(range(-5, 7), 2)); k = r.choice([1, -1, 2])
    t = r.choice(["x", "y", "dist"])
    pe = qd(k, -k * (a + b), k * a * b)
    if t == "x":
        return fill(f"y = {pe}의 그래프의 x절편은 {{{{1}}}}, {{{{2}}}}", [ans(a), ans(b)],
                    f"y = 0: {pe} = 0 → {'' if k == 1 else '−' if k == -1 else m(k)}(x{term(-a)})(x{term(-b)}) = 0\nx = {m(a)}, {m(b)}", "y = 0을 놓고 푸세요.", unordered=[[1, 2]])
    if t == "y":
        return num(f"y = {pe}의 그래프의 y절편은?", k * a * b, f"x = 0을 대입하면 y = {m(k * a * b)} (상수항)", "y절편은 상수항입니다.")
    return num(f"y = {pe}의 그래프가 x축과 만나는 두 점 사이의 거리는?", b - a,
               f"x절편: {m(a)}, {m(b)}\n거리 = {m(b)} − {par(a)} = {b - a}", "x절편을 구해 차를 계산하세요.")

def q1_three(r):
    a, b, c = nz(r, -2, 3), r.randint(-5, 5), r.randint(-6, 6)
    x1, x2 = r.sample([1, 2, -1, 3, -2], 2)
    ask = r.choice(["a", "b"])
    return num(f"y = ax² + bx + c의 그래프가 (0, {m(c)}), {pt(x1, a * x1 * x1 + b * x1 + c)}, {pt(x2, a * x2 * x2 + b * x2 + c)}를 지날 때 {ask}의 값은?", a if ask == "a" else b,
               f"(0, {m(c)}) → c = {m(c)}\n{poly((x1 * x1, 'a'), (x1, 'b'))} = {m(a * x1 * x1 + b * x1)}, {poly((x2 * x2, 'a'), (x2, 'b'))} = {m(a * x2 * x2 + b * x2)}\n연립하면 a = {m(a)}, b = {m(b)}",
               "세 점을 대입해 연립하세요.")

def q1_av(r):
    p, q, k = nz(r, -4, 4), r.randint(-5, 5), r.choice([1, 2, -1, 3, -2])
    x0 = r.choice([z for z in range(-3, 4) if z != p])
    y0 = k * (x0 - p) ** 2 + q
    return num(f"꼭짓점이 {pt(p, q)}이고 점 {pt(x0, y0)}를 지나는 포물선 y = a(x{term(-p)})²{term(q)}에서 a의 값은?", k,
               f"점 대입: {m(y0)} = a × ({m(x0)}{term(-p)})²{term(q)} = {(x0 - p) ** 2}a{term(q)}\n{(x0 - p) ** 2}a = {m(y0 - q)} → a = {m(k)}", "지나는 점을 대입하세요.")

def q1_shift(r):
    a, p, q = r.choice([1, 2, 3, -1, -2]), nz(r, -4, 4), r.randint(-5, 5)
    return num(f"y = {'' if a == 1 else '−' if a == -1 else a}x²을 평행이동해 꼭짓점이 {pt(p, q)}가 되게 한 그래프의 y절편은?", a * p * p + q,
               f"y = {vform(a, p, q)}\nx = 0: {m(a)}×{p * p}{term(q)} = {m(a * p * p + q)}".replace("1×", ""), "꼭짓점 꼴로 쓴 뒤 x = 0 대입")

L41 = [("꼭짓점", q1_vertex), ("완전제곱식", q1_comp), ("절편", q1_int), ("세 점으로 결정", q1_three), ("꼭짓점과 한 점", q1_av), ("평행이동한 그래프", q1_shift)]

def q2_ext(r):
    a, p, q = r.choice([1, 2, -1, -2, 3, -3]), r.randint(-5, 5), r.randint(-8, 8)
    b, c = -2 * a * p, a * p * p + q
    t = r.choice(["val", "at"])
    nm = "최솟값" if a > 0 else "최댓값"
    if t == "val":
        return num(f"y = {qd(a, b, c)}의 {nm}은?", q, f"y = {vform(a, p, q)}\n{'아래' if a > 0 else '위'}로 볼록 → 꼭짓점에서 {nm} {m(q)}", "완전제곱식으로 바꾸세요.")
    return num(f"y = {qd(a, b, c)}에서 {nm}을 가지는 x의 값은?", p, f"y = {vform(a, p, q)}\n꼭짓점의 x좌표 {m(p)}에서 {nm}", "꼭짓점의 x좌표")

def q2_range(r):
    p = r.randint(-2, 4); q = r.randint(-5, 5); lo = r.randint(-3, 3); hi = lo + r.randint(2, 4)
    f = lambda x: (x - p) ** 2 + q
    vals = [f(x) for x in (lo, hi)] + ([f(p)] if lo <= p <= hi else [])
    t = r.choice(["max", "min"])
    v = max(vals) if t == "max" else min(vals)
    return num(f"{m(lo)} ≤ x ≤ {m(hi)}에서 y = {qd(1, -2 * p, p * p + q)}의 {'최댓값' if t == 'max' else '최솟값'}은?", v,
               f"y = {vform(1, p, q)}, 꼭짓점의 x = {m(p)}" + (" (범위 안)" if lo <= p <= hi else " (범위 밖)") +
               f"\nf({m(lo)}) = {m(f(lo))}, f({m(hi)}) = {m(f(hi))}" + (f", f({m(p)}) = {m(q)}" if lo < p < hi else "") + f"\n{'최댓값' if t == 'max' else '최솟값'} {m(v)}",
               "꼭짓점이 범위 안인지 확인하고 양 끝값과 비교하세요.")

def q2_rect(r):
    t = r.choice(["rect", "diff", "sum2", "wall"])
    if t == "rect":
        P = 4 * r.randint(2, 10)
        return num(f"둘레가 {P}인 직사각형의 넓이의 최댓값은?", (P // 4) ** 2,
                   f"가로 x, 세로 {P // 2} − x → 넓이 x({P // 2} − x) = −(x − {P // 4})² + {(P // 4) ** 2}\nx = {P // 4}(정사각형)일 때 최댓값 {(P // 4) ** 2}", "넓이를 이차함수로 나타내세요.")
    if t == "diff":
        d = 2 * r.randint(1, 8)
        return num(f"차가 {d}인 두 수의 곱의 최솟값은?", -(d // 2) ** 2,
                   f"두 수 x, x + {d} → 곱 x(x + {d}) = (x + {d // 2})² − {(d // 2) ** 2}\n최솟값 −{(d // 2) ** 2}", "곱을 이차함수로")
    if t == "sum2":
        s = 2 * r.randint(1, 6)
        return num(f"x + y = {s}일 때 x² + y²의 최솟값은?", s * s // 2,
                   f"y = {s} − x → x² + ({s} − x)² = 2x² − {2 * s}x + {s * s} = 2(x − {s // 2})² + {s * s // 2}\n최솟값 {s * s // 2}", "한 문자를 없애세요.")
    L_ = 4 * r.randint(3, 12)
    return num(f"길이 {L_}m인 울타리로 한 면이 벽인 직사각형 밭을 만들 때 밭의 넓이의 최댓값은 몇 m²일까요?", L_ * L_ // 8,
               f"벽에 수직인 변 x, 평행한 변 {L_} − 2x → 넓이 x({L_} − 2x) = −2(x − {L_ // 4})² + {L_ * L_ // 8}\n최댓값 {L_ * L_ // 8}", "울타리는 세 변만 씁니다.")

def q2_ball(r):
    v = 10 * r.randint(1, 5)
    t_ = v // 10; h = 5 * t_ * t_
    ask = r.choice(["h", "t"])
    return num(f"위로 던진 공의 t초 후 높이가 ({v}t − 5t²)m일 때 {'가장 높이 올라간 높이는 몇 m일까요?' if ask == 'h' else '가장 높이 올라가는 것은 몇 초 후일까요?'}", h if ask == "h" else t_,
               f"{v}t − 5t² = −5(t − {t_})² + {h}\nt = {t_}초일 때 최고 높이 {h}m", "완전제곱식으로 바꾸세요.")

def q2_k(r):
    a = nz(r, -5, 5); mn = r.randint(-5, 6)
    return num(f"y = x²{term(2 * a, 'x')} + k의 최솟값이 {m(mn)}일 때 k의 값은?", mn + a * a,
               f"y = (x{term(a)})² + k − {a * a}\n최솟값 k − {a * a} = {m(mn)} → k = {m(mn + a * a)}", "최솟값을 k로 나타내세요.")

L42 = [("최댓값·최솟값", q2_ext), ("범위가 있는 최대·최소", q2_range), ("도형과 최대·최소", q2_rect), ("던진 공", q2_ball), ("최솟값으로 k 구하기", q2_k)]

def q3_cnt(r):
    a, b, c = 1, nz(r, -8, 8), r.randint(-6, 10)
    D = b * b - 4 * c
    v = 2 if D > 0 else 1 if D == 0 else 0
    return num(f"y = {qd(a, b, c)}의 그래프와 x축의 교점은 몇 개일까요?", v,
               f"x² {'+' if b > 0 else '−'} {abs(b)}x {'+' if c >= 0 else '−'} {abs(c)} = 0의 판별식 D = {b * b} − {4 * c} = {m(D)}\n".replace(" + 0 = 0", " = 0") +
               ("D > 0 → 2개" if v == 2 else "D = 0 → 접함, 1개" if v == 1 else "D < 0 → 0개"), "판별식의 부호")

def q3_k(r):
    a = nz(r, -5, 5)
    t = r.choice(["tan", "none", "two"])
    if t == "tan":
        return num(f"y = x²{term(2 * a, 'x')} + k의 그래프가 x축에 접할 때 k의 값은?", a * a,
                   f"접하려면 D/4 = {a * a} − k = 0 → k = {a * a}", "D = 0")
    if t == "none":
        return num(f"y = x²{term(2 * a, 'x')} + k의 그래프가 x축과 만나지 않는 정수 k의 최솟값은?", a * a + 1,
                   f"D/4 = {a * a} − k < 0 → k > {a * a}\n정수 최솟값 {a * a + 1}", "D < 0")
    return num(f"y = −x²{term(2 * a, 'x')} + k의 그래프가 x축과 서로 다른 두 점에서 만나는 정수 k의 최솟값은?", -a * a + 1,
               f"−x²{term(2 * a, 'x')} + k = 0 → x²{term(-2 * a, 'x')} − k = 0\nD/4 = {a * a} + k > 0 → k > {m(-a * a)}\n정수 최솟값 {m(-a * a + 1)}", "D > 0")

def q3_dist(r):
    p, d = r.randint(-3, 4), r.randint(1, 5)
    # roots p − d, p + d: x² − 2p x + p² − d²; given distance 2d find k
    return num(f"y = x²{term(-2 * p, 'x')} + k의 그래프가 x축과 만나는 두 점 사이의 거리가 {2 * d}일 때 k의 값은?", p * p - d * d,
               f"두 근 α, β: α + β = {m(2 * p)}, αβ = k\n(α − β)² = (α + β)² − 4αβ = {4 * p * p} − 4k = {4 * d * d}\nk = {m(p * p - d * d)}", "(α − β)² = (α + β)² − 4αβ")

def q3_ineq(r):
    a, b = sorted(r.sample(range(-4, 7), 2))
    lo, hi = r.randint(a - 3, a), r.randint(b, b + 3)
    S = [z for z in range(lo, hi + 1) if (z - a) * (z - b) >= 0]
    return num(f"y = (x{term(-a)})(x{term(-b)})의 그래프에서 {m(lo)} ≤ x ≤ {m(hi)}인 정수 x 중 y ≥ 0인 것은 몇 개일까요?", len(S),
               f"y ≥ 0 ⇔ x ≤ {m(a)} 또는 x ≥ {m(b)} (그래프가 x축 위 또는 위에 닿음)\n해당 정수: {', '.join(m(z) for z in S)} → {len(S)}개", "그래프가 x축 위에 있는 부분")

def q3_between(r):
    k0 = r.randint(1, 5); a = r.randint(-2, 3)
    # x² − 2a x + k = 0 roots straddle k0: f(k0) < 0 → k0² − 2a k0 + k < 0 → k < 2a k0 − k0²
    bound = 2 * a * k0 - k0 * k0
    return num(f"x²{term(-2 * a, 'x')} + k = 0의 두 근 사이에 {k0}이 있도록 하는 정수 k의 최댓값은?".replace(f"{k0}이", j(k0, "가이")), bound - 1,
               f"f(x) = x²{term(-2 * a, 'x')} + k라 하면 f({k0}) < 0이어야 합니다.\n{k0 * k0}{term(-2 * a * k0)} + k < 0 → k < {m(bound)}\n정수 최댓값 {m(bound - 1)}", "두 근 사이의 값에서 함숫값이 음수")

L43 = [("x축과의 교점", q3_cnt), ("교점 조건과 k", q3_k), ("두 교점 사이의 거리", q3_dist), ("그래프와 부등식", q3_ineq), ("근의 위치", q3_between)]

def q4_cnt(r):
    a, b, p, q = r.choice([1, -1]), r.randint(-4, 4), nz(r, -4, 4), r.randint(-5, 5)
    # y = a x² + b x  vs y = p x + q → a x² + (b − p) x − q = 0
    D = (b - p) ** 2 + 4 * a * q
    v = 2 if D > 0 else 1 if D == 0 else 0
    return num(f"y = {qd(a, b, 0)}의 그래프와 직선 y = {poly((p, 'x'), (q, ''))}의 교점은 몇 개일까요?", v,
               f"{qd(a, b, 0)} = {poly((p, 'x'), (q, ''))} → {qd(a, b - p, -q)} = 0\nD = {m(D)} → " + ("2개" if v == 2 else "접함, 1개" if v == 1 else "0개"), "연립한 이차방정식의 판별식")

def q4_tan(r):
    p, b = nz(r, -4, 4), r.randint(-3, 3)
    # y = x² + b x and y = p x + k tangent: x² + (b − p) x − k = 0, D = 0 → k = −(b − p)²/4
    if (b - p) % 2: return None
    k = -((b - p) // 2) ** 2
    return num(f"y = {qd(1, b, 0)}의 그래프와 직선 y = {poly((p, 'x'))} + k가 접할 때 k의 값은?", k,
               f"{qd(1, b - p, 0)} − k = 0이 중근 → D = {(b - p) ** 2} + 4k = 0\nk = {m(k)}", "연립한 방정식이 중근")

def q4_vieta(r):
    p, q = nz(r, -4, 4), r.randint(-6, 6)
    t = r.choice(["sum", "prod"])
    return num(f"y = x²과 직선 y = {poly((p, 'x'), (q, ''))}의 두 교점의 x좌표의 {'합' if t == 'sum' else '곱'}은?", p if t == "sum" else -q,
               f"x² = {poly((p, 'x'), (q, ''))} → {qd(1, -p, -q)} = 0\n근과 계수의 관계: 합 = {m(p)}, 곱 = {m(-q)}", "연립한 이차방정식의 근과 계수의 관계")

def q4_horiz(r):
    a, c = r.choice([1, -1]), r.randint(-4, 6)
    t = r.choice(["kmax", "chord"])
    if t == "kmax" and a == -1:
        return num(f"y = −x²{term(c)}과 직선 y = k가 서로 다른 두 점에서 만나는 정수 k의 최댓값은?", c - 1,
                   f"y = −x²{term(c)}의 최댓값은 {m(c)}\nk < {m(c)}이어야 두 점 → 정수 최댓값 {m(c - 1)}", "꼭짓점보다 아래")
    k = r.randint(1, 6)
    return num(f"y = x²과 직선 y = {k * k}가 만나는 두 점 사이의 거리는?", 2 * k,
               f"x² = {k * k} → x = ±{k}\n거리 = {k} − (−{k}) = {2 * k}", "교점의 x좌표 차")

def q4_close(r):
    m_ = nz(r, -4, 4); c = r.randint(-8, -1)
    x0 = F(m_, 2)
    t = r.choice(["x", "y"])
    v = x0 if t == "x" else x0 * x0
    return num(f"y = x² 위의 점 중 직선 y = {poly((m_, 'x'), (c, ''))}와의 거리가 가장 짧은 점의 {t}좌표는? (기약분수 또는 정수로)", v,
               f"그 점에서의 접선이 주어진 직선과 평행 → 기울기 {m(m_)}\ny = x²의 접선 기울기 2x = {m(m_)} → x = {fm(x0)}, y = {fm(x0 * x0)}", "주어진 직선과 평행한 접선의 접점",
               fmt="fraction" if v.denominator > 1 else "integer")

L44 = [("교점의 개수", q4_cnt), ("접할 조건", q4_tan), ("교점의 x좌표", q4_vieta), ("수평선과의 교점", q4_horiz), ("가장 가까운 점", q4_close)]

# ================= ch05 유리함수와 무리함수 =================
def r1_simp(r):
    a = nz(r, -6, 6)
    t = r.choice(["sq", "div", "mul"])
    if t == "sq":
        return fill(f"(x² − {a * a})/(x{term(-abs(a))}) = x + {{{{1}}}}  (x ≠ {abs(a)})", [str(abs(a))],
                    f"분자 인수분해: (x + {abs(a)})(x − {abs(a)})\n약분하면 x + {abs(a)}", "분자를 인수분해해 약분하세요.")
    if t == "div":
        b = abs(a)
        return fill(f"(x² − {b * b})/x ÷ (x − {b})/x = x + {{{{1}}}}", [str(b)],
                    f"나눗셈은 역수의 곱: (x + {b})(x − {b})/x × x/(x − {b})\n= x + {b}", "역수를 곱해 약분하세요.")
    b = abs(a)
    return fill(f"x/(x + {b}) × (x + {b})/x² = 1/{{{{1}}}}", [["x"]],
                f"(x + {b})와 x를 약분: x × (x + {b}) / ((x + {b}) × x²) = 1/x", "공통인수를 약분하세요.")

def r1_part(r):
    a = r.randint(1, 5)
    return fill(f"1/(x(x + {a})) = (1/{{{{1}}}})(1/x − 1/(x + {a}))", [str(a)],
                f"1/x − 1/(x + {a}) = {a}/(x(x + {a}))\n따라서 1/(x(x + {a})) = (1/{a})(1/x − 1/(x + {a}))", "부분분수 분해")

def r1_tele(r):
    n = r.randint(4, 20); d = r.choice([1, 2])
    if d == 1:
        v = F(n, n + 1)
        return num(f"1/(1·2) + 1/(2·3) + … + 1/({n}·{n + 1})의 값은? (기약분수로)", v,
                   f"1/(k(k + 1)) = 1/k − 1/(k + 1)\n더하면 가운데가 지워져 1 − 1/{n + 1} = {fs(v)}", "부분분수로 나누면 연쇄적으로 지워집니다.", fmt="fraction")
    k = r.randint(2, 6); last = 2 * k - 1
    v = F(1, 2) * (1 - F(1, last + 2))
    return num(f"1/(1·3) + 1/(3·5) + … + 1/({last}·{last + 2})의 값은? (기약분수로)", v,
               f"1/(k(k + 2)) = (1/2)(1/k − 1/(k + 2))\n합 = (1/2)(1 − 1/{last + 2}) = {fs(v)}", "부분분수 분해에 1/2이 붙습니다.", fmt="fraction")

def r1_ratio(r):
    a, b = r.sample(range(1, 7), 2)
    t = r.choice(["ratio", "frac"])
    if t == "ratio":
        v = F(a + b, a)
        return num(f"x : y = {a} : {b}일 때 (x + y)/x의 값은? (기약분수 또는 정수로)", v,
                   f"x = {a if a > 1 else ''}k, y = {b if b > 1 else ''}k로 놓으면 (x + y)/x = {a + b}k/{a}k = {fm(v)}", "x = ak, y = bk로 놓으세요.", fmt="fraction" if v.denominator > 1 else "integer")
    k = r.randint(2, 6)
    v = F(k + 1, k - 1)
    return num(f"a/b = {k}일 때 (a + b)/(a − b)의 값은? (기약분수 또는 정수로)", v,
               f"a = {k}b를 대입: ({k}b + b)/({k}b − b) = {k + 1}/{k - 1} = {fm(v)}", "a를 b로 나타내세요.", fmt="fraction" if v.denominator > 1 else "integer")

def r1_xy(r):
    x, y = r.sample(range(1, 9), 2)
    s, p = x + y, x * y
    v = F(s, p)
    if r.random() < .5:
        return num(f"1/x + 1/y = {fm(v)}, x + y = {s}일 때 xy의 값은?", p,
                   f"1/x + 1/y = (x + y)/(xy) = {s}/(xy) = {fm(v)}\nxy = {s} ÷ {fm(v)} = {p}", "통분하면 (x + y)/(xy)")
    k = r.randint(1, 6)
    return num(f"x − 1/x = {k}일 때 x² + 1/x²의 값은?", k * k + 2,
               f"(x − 1/x)² = x² − 2 + 1/x²\nx² + 1/x² = {k}² + 2 = {k * k + 2}", "제곱해 보세요.")

L51 = [("유리식의 약분", r1_simp), ("부분분수", r1_part), ("부분분수의 합", r1_tele), ("비례식", r1_ratio), ("식의 값", r1_xy)]

def r2_asym(r):
    k, p, q = nz(r, -6, 6), nz(r, -5, 5), r.randint(-5, 5)
    return fill(f"y = {m(k)}/(x{term(-p)}){term(q)}의 점근선은 x = {{{{1}}}}, y = {{{{2}}}}", [ans(p), ans(q)],
                f"y = k/(x − p) + q의 점근선은 x = p, y = q\n→ x = {m(p)}, y = {m(q)}", "분모가 0이 되는 x, 더해진 상수 q")

def r2_conv(r):
    a, c, p = nz(r, -4, 4), nz(r, -6, 6), nz(r, -4, 4)
    # y = (a x + b)/(x − p) = a + (b + a p)/(x − p)
    b = c - a * p
    return fill(f"y = ({poly((a, 'x'), (b, ''))})/(x{term(-p)}) = {m(c)}/(x{term(-p)}) + {{{{1}}}}", [ans(a)],
                f"분자를 (x{term(-p)})로 나누면 {poly((a, 'x'), (b, ''))} = {m(a)}(x{term(-p)}){term(c)}\ny = {m(a)} + {m(c)}/(x{term(-p)}) → 빈칸 {m(a)} (수평 점근선 y = {m(a)})",
                "분자를 분모로 나누세요.")

def r2_k(r):
    x, y = nz(r, -5, 5), nz(r, -5, 5)
    t = r.choice(["pass", "origin"])
    if t == "pass":
        return num(f"y = k/x의 그래프가 점 {pt(x, y)}를 지날 때 k의 값은?", x * y, f"k = xy = {m(x)}×{par(y)} = {m(x * y)}", "k = xy")
    p, q = nz(r, -4, 4), nz(r, -4, 4)
    return num(f"y = k/(x{term(-p)}){term(q)}의 그래프가 원점을 지날 때 k의 값은?", p * q,
               f"(0, 0) 대입: 0 = k/(0{term(-p)}){term(q)} → k/{par(-p)} = {m(-q)} → k = {m(p * q)}", "원점 (0, 0)을 대입하세요.")

def r2_range(r):
    k = r.choice([2, 4, 6, 8, 12]); lo = r.choice([d for d in divisors(k) if d < k]); hi = r.choice([d for d in divisors(k) if d > lo])
    t = r.choice(["max", "min"])
    return num(f"{lo} ≤ x ≤ {hi}에서 y = {k}/x의 {'최댓값' if t == 'max' else '최솟값'}은?", k // lo if t == "max" else k // hi,
               f"x > 0에서 y = {k}/x는 감소 → x = {lo}에서 최대 {k // lo}, x = {hi}에서 최소 {k // hi}", "감소함수는 왼쪽 끝이 최대")

def r2_excl(r):
    p, q = nz(r, -6, 6), nz(r, -6, 6)
    t = r.choice(["dom", "rng"])
    if t == "dom":
        return num(f"y = 1/(x{term(-p)}){term(q)}의 정의역에서 제외되는 x는?", p, f"분모가 0이 되는 x{term(-p)} = 0 → x = {m(p)}", "분모 ≠ 0")
    return num(f"y = 1/(x{term(-p)}){term(q)}의 치역에서 빠지는 값은?", q, f"1/(x{term(-p)})은 0이 될 수 없으므로 y ≠ {m(q)}", "수평 점근선의 값")

L52 = [("점근선", r2_asym), ("표준형으로 바꾸기", r2_conv), ("그래프와 k", r2_k), ("범위에서 최대·최소", r2_range), ("정의역과 치역", r2_excl)]

def r3_dom(r):
    a, b = sorted(r.sample(range(-4, 9), 2))
    return num(f"√({m(b)} − x) + √(x{term(-a)})의 값이 실수가 되는 정수 x는 몇 개일까요?".replace("√(0 − x)", "√(−x)"), b - a + 1,
               f"{m(b)} − x ≥ 0 그리고 x{term(-a)} ≥ 0 → {m(a)} ≤ x ≤ {m(b)}\n정수 {b - a + 1}개", "근호 안이 모두 0 이상")

def r3_rat(r):
    a, b = r.choice([(2, 1), (3, 1), (3, 2), (5, 3), (5, 2), (6, 5), (7, 3), (7, 5)])
    return fill(f"1/(√{a} + √{b}) + 1/(√{a} − √{b}) = {{{{1}}}}√{a}" if a - b != 1 else f"1/(√{a} + √{b}) + 1/(√{a} − √{b}) = {{{{1}}}}√{a}",
                [str(F(2, a - b)) if F(2, a - b).denominator == 1 else f"{F(2, a - b).numerator}/{F(2, a - b).denominator}"],
                f"통분: ((√{a} − √{b}) + (√{a} + √{b}))/({a} − {b}) = 2√{a}/{a - b}\n= " + (f"{fs(F(2, a - b))}√{a}" if F(2, a - b).denominator == 1 else f"({fs(F(2, a - b))})√{a}"), "분모를 통분하면 (√a)² − (√b)²")

def r3_val(r):
    a, b = r.randint(1, 4), r.choice([2, 3, 5, 6, 7])
    t = r.choice(["sum", "prod", "sq", "poly"])
    if t == "poly":
        return num(f"x = √{b} + {a}일 때 x²{term(-2 * a, 'x')}의 값은?", b - a * a,
                   f"x − {a} = √{b} → (x − {a})² = {b}\nx² − {2 * a}x + {a * a} = {b} → x² − {2 * a}x = {m(b - a * a)}", "x − a = √b를 제곱하세요.")
    s, p = 2 * a, a * a - b
    v = {"sum": s, "prod": p, "sq": s * s - 2 * p}[t]
    nm = {"sum": "x + y", "prod": "xy", "sq": "x² + y²"}[t]
    return num(f"x = {a} + √{b}, y = {a} − √{b}일 때 {nm}의 값은?", v,
               f"x + y = {s}, xy = {a}² − {b} = {m(p)}" + (f"\nx² + y² = (x + y)² − 2xy = {s * s} − {m(2 * p)} = {m(v)}" if t == "sq" else f"\n{nm} = {m(v)}"), "켤레 무리수의 합과 곱")

def r3_eq(r):
    x = r.randint(2, 9); c = r.randint(1, x - 1)
    t = r.choice(["lin", "simple"])
    if t == "simple":
        a = r.randint(-3, 5)
        return num(f"√(x{term(a)}) = {c}의 해는?", c * c - a, f"양변을 제곱: x{term(a)} = {c * c} → x = {m(c * c - a)}\n확인: √{c * c} = {c} ✓", "양변을 제곱하세요.")
    # √(x + k) = x − c with solution x
    k = (x - c) ** 2 - x
    # other root check
    other = [z for z in range(-20, 30) if z != x and z + k >= 0 and z - c >= 0 and (z - c) ** 2 == z + k]
    if other: return None
    return num(f"√(x{term(k)}) = x − {c}의 해는?", x,
               f"양변을 제곱: x{term(k)} = (x − {c})² → {poly((1, 'x²'), (-(2 * c + 1), 'x'), (c * c - k, ''))} = 0\n근을 구한 뒤 x − {c} ≥ 0인 것만 남깁니다(무연근 제거) → x = {x}", "제곱한 뒤 반드시 대입해 확인하세요.")

def r3_nested(r):
    a, b = r.choice([(2, 1), (3, 1), (3, 2), (5, 1), (5, 3), (6, 1), (7, 2), (4, 3)])
    t = r.choice(["plus", "minus"])
    if t == "plus":
        return fill(f"√({a + b} + 2√{a * b}) = √{a} + √{{{{1}}}}" if b != 1 else f"√({a + b} + 2√{a * b}) = √{a} + {{{{1}}}}", [str(b)],
                    f"합이 {a + b}, 곱이 {a * b}인 두 수 {j(a, '와과')} {b}\n√({a + b} + 2√{a * b}) = √{a} + √{b}" + (" = √" + str(a) + " + 1" if b == 1 else ""), "√(a + b + 2√(ab)) = √a + √b")
    return fill(f"√({a + b} − 2√{a * b}) = √{a} − √{{{{1}}}}" if b != 1 else f"√({a + b} − 2√{a * b}) = √{a} − {{{{1}}}}", [str(b)],
                f"합이 {a + b}, 곱이 {a * b}이고 {a} > {b}\n√({a + b} − 2√{a * b}) = √{a} − √{b}" + (" = √" + str(a) + " − 1" if b == 1 else ""), "√(a + b − 2√(ab)) = √a − √b (a > b)")

L53 = [("근호가 정의될 조건", r3_dom), ("분모의 유리화", r3_rat), ("식의 값", r3_val), ("무리방정식", r3_eq), ("이중근호", r3_nested)]

def r4_dr(r):
    a, p, q = r.choice([1, -1]), r.randint(-5, 5), r.randint(-5, 5)
    t = r.choice(["dom", "rng"])
    e = f"{'−' if a < 0 else ''}√(x{term(-p)}){term(q)}".replace("√(x)", "√x")
    if t == "dom":
        return num(f"y = {e}의 정의역에서 가장 작은 x는?", p, f"x{term(-p)} ≥ 0 → x ≥ {m(p)}", "근호 안 ≥ 0")
    return num(f"y = {e}의 치역에서 가장 {'작은' if a > 0 else '큰'} y는?", q,
               f"{'√' if a > 0 else '−√'}(x{term(-p)}){' ≥ 0' if a > 0 else ' ≤ 0'} → y {'≥' if a > 0 else '≤'} {m(q)}".replace("(x)", "x"), "√ 부분은 0 이상")

def r4_pass(r):
    a, x = r.choice([1, 2, 3, 4, 6, 8]), r.randint(1, 8)
    v = a * x
    if isqrt(v) ** 2 != v: return None
    return num(f"y = √(ax)의 그래프가 점 ({x}, {isqrt(v)})를 지날 때 a의 값은?", a, f"{isqrt(v)} = √({x}a) → {v} = {x}a → a = {a}", "제곱해서 푸세요.")

def r4_inv(r):
    p = r.randint(-4, 4); q = r.randint(-3, 3)
    return fill(f"y = √(x{term(-p)}){term(q)}의 역함수는 y = (x{term(-q)})² + {{{{1}}}}  (x ≥ {m(q)})".replace("(x)", "x"), [ans(p)],
                f"y{term(-q)} = √(x{term(-p)}) → 제곱: (y{term(-q)})² = x{term(-p)}\nx = (y{term(-q)})²{term(p)}, x와 y를 바꿈 → y = (x{term(-q)})²{term(p)}".replace("(x)", "x").replace("(y)", "y"), "x에 대해 풀고 x, y를 바꾸세요.")

def r4_ext(r):
    p = r.randint(-3, 3); lo = p + r.randint(0, 3) ** 2; hi = lo + r.randint(3, 20)
    a = r.choice([1, -1]); q = r.randint(-3, 4)
    vals = [(a * (x - p) ** .5 + q) for x in (lo, hi)]
    if any(abs(v - round(v)) > 1e-9 for v in vals): return None
    t = r.choice(["max", "min"])
    v = round(max(vals) if t == "max" else min(vals))
    return num(f"{m(lo)} ≤ x ≤ {m(hi)}에서 y = {'−' if a < 0 else ''}√(x{term(-p)}){term(q)}의 {'최댓값' if t == 'max' else '최솟값'}은?".replace("(x)", "x"), v,
               f"{'증가' if a > 0 else '감소'}함수 → 양 끝값 비교: x = {m(lo)}일 때 {m(g(vals[0]))}, x = {m(hi)}일 때 {m(g(vals[1]))}\n{'최댓값' if t == 'max' else '최솟값'} {m(v)}", "무리함수는 한 방향으로만 증가/감소")

def r4_meet(r):
    a = r.randint(1, 5)
    # √x = x − a? choose y = √(x + c) with inverse intersection on y=x: √(x + c) = x → x² − x − c = 0, x ≥ 0
    x = r.randint(2, 6); c = x * x - x
    return num(f"y = √(x + {c})의 그래프와 그 역함수의 그래프의 교점의 x좌표는?", x,
               f"증가함수와 역함수의 교점은 y = x 위\n√(x + {c}) = x → x² − x − {c} = 0 → (x − {x})(x + {x - 1}) = 0\nx ≥ 0이므로 x = {x}", "y = x와의 교점을 구하세요.")

L54 = [("정의역과 치역", r4_dr), ("지나는 점", r4_pass), ("역함수", r4_inv), ("범위에서 최대·최소", r4_ext), ("역함수와의 교점", r4_meet)]

# ================= ch06 함수로 모델링하기 =================
def m1_prop(r):
    t = r.choice(["water", "fuel", "speed", "work", "gas"])
    if t == "water":
        a, b = r.randint(2, 9), r.randint(3, 15)
        return num(f"1분에 {a}L씩 물이 나오는 수도에서 {b}분 동안 나오는 물은 몇 L일까요?", a * b, f"정비례 y = {a}x\nx = {b} → y = {a * b}L", "y = ax")
    if t == "fuel":
        k, n = r.choice([10, 12, 15, 16, 20]), r.randint(2, 8)
        return num(f"휘발유 1L로 {k}km를 가는 자동차가 {k * n}km를 가려면 휘발유가 몇 L 필요할까요?", n, f"거리 = {k} × (휘발유 양)\n{k * n} ÷ {k} = {n}L", "정비례")
    if t == "speed":
        v1, t1, v2 = r.choice([(60, 3, 90), (40, 6, 80), (80, 3, 60), (50, 6, 75), (90, 2, 60), (120, 2, 80)])
        return num(f"시속 {v1}km로 {t1}시간 걸리는 거리를 시속 {v2}km로 가면 몇 시간 걸릴까요?", F(v1 * t1, v2),
                   f"거리 = {v1} × {t1} = {v1 * t1}km (일정)\n시간 = {v1 * t1} ÷ {v2} = {fs(F(v1 * t1, v2))}시간 (속력과 시간은 반비례)", "거리가 같으면 속력과 시간은 반비례",
                   fmt="fraction" if F(v1 * t1, v2).denominator > 1 else "integer")
    if t == "work":
        a, d, b = r.choice([(12, 6, 9), (10, 6, 15), (8, 9, 12), (6, 10, 4), (15, 4, 10), (20, 3, 12)])
        return num(f"{a}명이 {d}일 걸리는 일을 {b}명이 하면 며칠 걸릴까요?", F(a * d, b),
                   f"전체 일의 양 = {a} × {d} = {a * d}(명·일)\n{a * d} ÷ {b} = {fs(F(a * d, b))}일 (인원과 일수는 반비례)", "사람 수 × 일수가 일정",
                   fmt="fraction" if F(a * d, b).denominator > 1 else "integer")
    p1, v1, p2 = r.choice([(2, 6, 3), (3, 8, 4), (4, 9, 6), (2, 15, 5), (5, 4, 2)])
    return num(f"온도가 일정할 때 기체의 압력 P와 부피 V는 반비례합니다. P = {p1}일 때 V = {v1}이면 P = {p2}일 때 V는?", F(p1 * v1, p2),
               f"PV = {p1} × {v1} = {p1 * v1} (일정)\nV = {p1 * v1} ÷ {p2} = {fs(F(p1 * v1, p2))}", "PV가 일정", fmt="fraction" if F(p1 * v1, p2).denominator > 1 else "integer")

def m1_lin(r):
    t = r.choice(["taxi", "candle", "tank", "bill"])
    if t == "taxi":
        b, p, k = r.choice([3800, 4800, 4000]), r.choice([800, 1000, 1200]), r.randint(3, 15)
        return num(f"택시 기본요금이 {b:,}원이고 1km마다 {p:,}원씩 더해집니다. {k}km를 가면 몇 원일까요?", b + p * k,
                   f"요금 = {b} + {p}x\nx = {k}: {b} + {p * k} = {b + p * k}원", "일차함수 모델")
    if t == "candle":
        L_, d = r.choice([(20, 0.5), (24, 2), (30, 1.5), (18, 0.6), (25, 1.25)])
        return num(f"길이 {L_}cm인 양초가 1분에 {g(d)}cm씩 탑니다. 다 타는 데 몇 분 걸릴까요?", g(L_ / d), f"{L_} − {g(d)}x = 0 → x = {L_} ÷ {g(d)} = {g(L_ / d)}분", "남은 길이 = 0", fmt="integer" if L_ / d == int(L_ / d) else "decimal")
    if t == "tank":
        V, d = r.choice([100, 120, 200, 150]), r.choice([2, 4, 5])
        left = V - d * r.randint(3, V // d - 2)
        return num(f"물 {V}L가 든 탱크에서 1분에 {d}L씩 물이 빠집니다. {left}L가 남는 것은 몇 분 후일까요?", (V - left) // d,
                   f"남은 양 = {V} − {d}x = {left} → {d}x = {V - left} → x = {(V - left) // d}분", "남은 양을 일차식으로")
    b, p = r.choice([1000, 2000, 3000]), r.choice([100, 120, 150])
    kwh = r.randint(50, 200); tot = b + p * kwh
    return num(f"기본요금 {b:,}원에 1kWh당 {p}원인 전기요금이 {tot:,}원이면 사용량은 몇 kWh일까요?", kwh,
               f"{b} + {p}x = {tot} → {p}x = {tot - b} → x = {kwh}", "일차방정식을 세우세요.")

def m2_avg(r):
    t = r.choice(["sq", "lin", "inv", "cube", "root"])
    if t == "sq":
        a, b = sorted(r.sample(range(-3, 6), 2)); k = r.choice([1, 2, -1])
        return num(f"f(x) = {'' if k == 1 else '−' if k == -1 else k}x²에서 x가 {m(a)}에서 {m(b)}까지 변할 때 평균변화율은?", k * (a + b),
                   f"(f({m(b)}) − f({m(a)}))/({m(b)} − {par(a)}) = ({m(k * b * b)} − {par(k * a * a)})/{b - a} = {m(k * (a + b))}", "Δy/Δx")
    if t == "lin":
        a, b = nz(r, -5, 5), r.randint(-5, 5)
        return num(f"f(x) = {poly((a, 'x'), (b, ''))}에서 어떤 구간을 잡아도 평균변화율은?", a, f"일차함수의 평균변화율은 항상 기울기 {m(a)}", "일차함수는 기울기가 일정")
    if t == "inv":
        a, b = r.sample([1, 2, 3, 4, 5, 6], 2)
        v = F(F(1, b) - F(1, a), b - a)
        return num(f"f(x) = 1/x에서 x가 {a}에서 {b}까지 변할 때 평균변화율은? (기약분수로)", v,
                   f"(1/{b} − 1/{a}) ÷ ({b} − {a}) = ({fm(F(1, b) - F(1, a))}) ÷ {par(b - a)} = {fm(v)}", "Δy/Δx", fmt="fraction")
    if t == "cube":
        a, b = sorted(r.sample(range(-3, 4), 2))
        v = F(b ** 3 - a ** 3, b - a)
        return num(f"f(x) = x³에서 x가 {m(a)}에서 {m(b)}까지 변할 때 평균변화율은?", v, f"({m(b ** 3)} − {par(a ** 3)})/{b - a} = {fm(v)}", "Δy/Δx")
    a, b = r.sample([1, 4, 9, 16, 25], 2)
    v = F(isqrt(b) - isqrt(a), b - a)
    return num(f"f(x) = √x에서 x가 {a}에서 {b}까지 변할 때 평균변화율은? (기약분수로)", v,
               f"(√{b} − √{a})/({b} − {a}) = ({isqrt(b)} − {isqrt(a)})/{b - a} = {fm(v)}", "Δy/Δx", fmt="fraction" if v.denominator > 1 else "integer")

def m2_find(r):
    t = r.choice(["a_shift", "a_end", "coef"])
    if t == "a_shift":
        a, h = r.randint(-3, 5), r.choice([1, 2, 4])
        return num(f"f(x) = x²에서 x가 a에서 a + {h}까지 변할 때 평균변화율이 {2 * a + h}이면 a의 값은?", a,
                   f"((a + {h})² − a²)/{h} = 2a + {h} = {2 * a + h} → a = {m(a)}", "평균변화율을 a로 나타내세요.")
    if t == "a_end":
        a = r.randint(1, 9)
        return num(f"f(x) = x²에서 x가 0에서 a까지 변할 때 평균변화율이 {a}이면 a의 값은? (a > 0)", a, f"(a² − 0)/(a − 0) = a = {a}", "평균변화율 = a")
    k, a, b = r.choice([2, 3, -1, 4]), r.randint(0, 2), r.randint(3, 5)
    return num(f"f(x) = kx²에서 x가 {a}에서 {b}까지 변할 때 평균변화율이 {k * (a + b)}이면 k의 값은?", k,
               f"k({b * b} − {a * a})/{b - a} = k × {a + b} = {k * (a + b)} → k = {m(k)}", "k를 묶어서 계산하세요.")

def m2_real(r):
    t = r.choice(["temp", "pop", "pos"])
    if t == "temp":
        h1, h2, T1 = r.choice([(9, 15, 12), (6, 14, 4), (8, 12, 10)]) ; d = r.randint(2, 4) * (h2 - h1) // 2
        T2 = T1 + d
        return num(f"오전 {h1}시에 {T1}°C, {'오후 ' + str(h2 - 12) if h2 > 12 else '오전 ' + str(h2)}시에 {T2}°C였습니다. 시간당 평균 기온 변화는 몇 °C일까요?", F(d, h2 - h1),
                   f"({T2} − {T1}) ÷ ({h2} − {h1}) = {d} ÷ {h2 - h1} = {fm(F(d, h2 - h1))}°C", "변화량 ÷ 시간", fmt="fraction" if F(d, h2 - h1).denominator > 1 else "integer")
    if t == "pop":
        a, y = r.choice([2000, 3000, 5000]), r.choice([4, 5, 8])
        d = 100 * r.randint(2, 10) * y // y
        return num(f"어느 마을 인구가 {y}년 동안 {a:,}명에서 {a + d * y:,}명으로 늘었습니다. 한 해 평균 몇 명씩 늘었을까요?", d,
                   f"({a + d * y} − {a}) ÷ {y} = {d * y} ÷ {y} = {d}명", "변화량 ÷ 기간")
    a, b = sorted(r.sample(range(0, 7), 2))
    return num(f"t초 후 위치가 s(t) = t²m일 때 t = {a}에서 t = {b}까지 평균 속력은 초속 몇 m일까요?", a + b,
               f"({b * b} − {a * a}) ÷ ({b} − {a}) = {b * b - a * a} ÷ {b - a} = {a + b}", "위치의 변화 ÷ 시간")

def m3_fit(r):
    t = r.choice(["lin", "sq", "sq1", "inv", "geo"])
    if t == "lin":
        a, b = nz(r, -4, 6), r.randint(-5, 10); n = r.randint(6, 15)
        return num(f"x = 0, 1, 2, 3일 때 y = {', '.join(m(a * x + b) for x in range(4))}입니다. 같은 규칙이면 x = {n}일 때 y는?", a * n + b,
                   f"x가 1 늘 때 y는 {m(a)}씩 → y = {poly((a, 'x'), (b, ''))}\nx = {n}: {m(a * n + b)}", "증가량이 일정하면 일차함수")
    if t in ("sq", "sq1"):
        c = 0 if t == "sq" else r.randint(-3, 4); n = r.randint(5, 9)
        return num(f"x = 1, 2, 3, 4일 때 y = {', '.join(m(x * x + c) for x in range(1, 5))}입니다. 같은 규칙이면 x = {n}일 때 y는?", n * n + c,
                   f"y = x²{term(c)} 규칙\nx = {n}: {n * n}{term(c)} = {n * n + c}", "제곱수와 비교해 보세요.")
    if t == "inv":
        k = r.choice([12, 24, 36, 60]); xs = sorted(r.sample([d for d in divisors(k) if d < k], 3)); x4 = r.choice([d for d in divisors(k) if d not in xs])
        return num(f"x = {', '.join(map(str, xs))}일 때 y = {', '.join(str(k // x) for x in xs)}입니다. 같은 규칙이면 x = {x4}일 때 y는?", k // x4,
                   f"xy가 항상 {k} → y = {k}/x\nx = {x4}: {k // x4}", "xy를 계산해 보세요.")
    a, rr = r.choice([1, 2, 3, 5]), r.choice([2, 3])
    n = r.randint(5, 8)
    return num(f"{', '.join(str(a * rr ** i) for i in range(4))}, … 로 늘어날 때 {n}번째 수는?", a * rr ** (n - 1),
               f"매번 {rr}배 → n번째 = {a} × {rr}^(n − 1)\n{n}번째 = {a} × {rr}{sup(n - 1)} = {a * rr ** (n - 1)}", "곱해지는 비율을 찾으세요.")

def m3_model(r):
    t = r.choice(["two", "ax2", "kx", "cell", "half"])
    if t == "two":
        b, a = r.randint(-3, 5), nz(r, -3, 4); x1 = r.randint(2, 4); n = r.randint(5, 10)
        return num(f"두 점 (0, {m(b)}), ({x1}, {m(a * x1 + b)})를 지나는 일차 모델로 x = {n}일 때 y를 예측하면?", a * n + b,
                   f"기울기 ({m(a * x1 + b)} − {par(b)})/{x1} = {m(a)} → y = {poly((a, 'x'), (b, ''))}\nx = {n}: {m(a * n + b)}", "두 점으로 직선을 구하세요.")
    if t == "ax2":
        a, x = r.choice([2, 3, 5, -1]), r.randint(2, 4)
        return num(f"y = ax² 모델이 점 ({x}, {a * x * x})를 지날 때 a의 값은?", a, f"{a * x * x} = a × {x * x} → a = {m(a)}", "대입하세요.")
    if t == "kx":
        k = r.choice([12, 20, 24, 30, 40, 60]); x1 = r.choice([d for d in divisors(k) if 1 < d < k]); x2 = r.choice([d for d in divisors(k) if d != x1])
        return num(f"y = k/x 모델이 점 ({x1}, {k // x1})를 지날 때 x = {x2}에서 y는?", k // x2, f"k = {x1} × {k // x1} = {k}\ny = {k}/{x2} = {k // x2}", "k = xy")
    if t == "cell":
        p, h = r.choice([20, 30, 15]), r.randint(1, 3)
        n = h * 60 // p
        return num(f"세포 1개가 {p}분마다 2배가 됩니다. {h}시간 후에는 몇 개일까요?", 2 ** n, f"{h}시간 = {h * 60}분 → {n}번 두 배\n2{sup(n)} = {2 ** n}개", "몇 번 두 배가 되는지 세세요.")
    a0, h, T = r.choice([(100, 4, 12), (80, 3, 9), (160, 2, 8), (64, 5, 15)])
    n = T // h
    return num(f"약 {a0}mg이 {h}시간마다 절반으로 줄어듭니다. {T}시간 후에는 몇 mg일까요?", F(a0, 2 ** n),
               f"{T} ÷ {h} = {n}번 절반 → {a0} × (1/2){sup(n)} = {fs(F(a0, 2 ** n))}mg", "몇 번 절반이 되는지 세세요.", fmt="fraction" if F(a0, 2 ** n).denominator > 1 else "integer")

def m4_mix(r):
    t = r.choice(["plan", "sales", "conv", "price", "fall"])
    if t == "plan":
        A, b, p = r.choice([20000, 30000, 25000]), r.choice([5000, 10000]), r.choice([200, 250, 300, 500])
        if (A - b) % p: return None
        return num(f"요금제 A는 월 {A:,}원, 요금제 B는 기본 {b:,}원에 1분당 {p}원입니다. 두 요금이 같아지는 것은 몇 분 쓸 때일까요?", (A - b) // p,
                   f"{b} + {p}x = {A} → {p}x = {A - b} → x = {(A - b) // p}분\n(이보다 많이 쓰면 A가 유리)", "두 요금을 같다고 놓으세요.")
    if t == "sales":
        N = 2 * r.randint(20, 50)
        ask = r.choice(["x", "R"])
        return num(f"한 개에 x천 원으로 팔면 하루에 ({N} − x)개가 팔립니다. 매출이 가장 클 때 {'x의 값은?' if ask == 'x' else '매출은 몇천 원일까요?'}", N // 2 if ask == "x" else (N // 2) ** 2,
                   f"매출 = x({N} − x) = −(x − {N // 2})² + {(N // 2) ** 2}\nx = {N // 2}일 때 최대 {(N // 2) ** 2}천 원", "매출을 이차함수로 나타내세요.")
    if t == "conv":
        C = r.choice([10, 20, 25, 30, 35, 40, 100])
        F_ = F(9, 5) * C + 32
        return num(f"화씨온도 F = 1.8C + 32에서 F = {fs(F_)}일 때 섭씨온도 C는?", C, f"{fs(F_)} = 1.8C + 32 → 1.8C = {fs(F_ - 32)} → C = {C}", "일차방정식을 푸세요.")
    if t == "price":
        c, pct, d = r.choice([10000, 20000, 15000]), r.choice([10, 20, 30]), r.choice([500, 1000, 2000])
        v = c * (100 + pct) // 100 - d
        return num(f"원가 x원에 {pct}% 이익을 붙인 뒤 {d:,}원을 할인합니다. 원가가 {c:,}원이면 판매가는 몇 원일까요?", v,
                   f"판매가 = {1 + pct / 100:g}x − {d}\nx = {c}: {c * (100 + pct) // 100} − {d} = {v}원", "함수식에 대입하세요.")
    v0 = 5 * r.randint(2, 6)
    return num(f"공의 높이가 h = −5t² + {v0}t(m)일 때 공이 땅에 떨어지는 것은 몇 초 후일까요?", v0 // 5,
               f"h = 0: −5t² + {v0}t = −5t(t − {v0 // 5}) = 0\nt > 0 → t = {v0 // 5}초", "h = 0인 양수 t")

L61 = [("비례 관계", m1_prop), ("일차함수 모델", m1_lin), ("최대·최소 모델", q2_rect), ("모델링 종합", m4_mix)]
L62 = [("평균변화율 계산", m2_avg), ("평균변화율로 미지수", m2_find), ("생활 속 평균변화율", m2_real)]
L63 = [("규칙 찾기", m3_fit), ("모델 세우고 예측", m3_model)]
L64 = [("모델링 종합", m4_mix), ("이차함수 최대·최소", q2_rect), ("비례 모델", m1_prop), ("일차 모델", m1_lin), ("성장·감소 모델", m3_model)]

ALL = {"ch04": [L41, L42, L43, L44], "ch05": [L51, L52, L53, L54], "ch06": [L61, L62, L63, L64]}

if __name__ == "__main__":
    tot = 0
    for ch, Ls in ALL.items():
        for i, T in enumerate(Ls, 1):
            per = 6 if len(T) >= 7 else 8 if len(T) >= 5 else 10 if len(T) >= 4 else 14 if len(T) == 3 else 20
            n = write("c2", ch, f"l0{i}", T, per=per, seed=1 + (i if ch == "ch06" else 0)); tot += n; print(ch, i, len(T), n)
    print("total", tot)
