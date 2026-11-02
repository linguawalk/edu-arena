"""코스 6 · 기하 (이차곡선, 평면벡터, 공간도형과 공간좌표) — 연습 문제 은행"""
from core import *
import math

def nz(r, a, b):
    while True:
        v = r.randint(a, b)
        if v: return v
def nf(v, prompt, expl, hint):
    v = F(v)
    return num(prompt, v, expl, hint, fmt="fraction" if v.denominator > 1 else "integer")
def vec(*xs): return "(" + ", ".join(m(x) if not isinstance(x, F) else fm(x) for x in xs) + ")"
TRI = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (4, 3, 5), (12, 5, 13), (8, 6, 10)]
Q4 = [(1, 2, 2, 3), (2, 3, 6, 7), (1, 4, 8, 9), (2, 6, 9, 11), (4, 4, 7, 9), (6, 6, 7, 11), (2, 10, 11, 15), (3, 4, 12, 13), (2, 2, 1, 3)]

# ================= ch01 포물선 =================
def p1_def(r):
    p = nz(r, -6, 6); t = r.choice(["vtx", "dist", "fd", "pt"])
    if t == "vtx":
        c = r.randint(-3, 3); return nf(c, f"초점이 ({m(c + p)}, 0), 준선이 x = {m(c - p)}인 포물선의 꼭짓점의 x좌표는?", f"꼭짓점은 초점과 준선의 한가운데\n({m(c + p)} + {par(c - p)}) ÷ 2 = {m(c)}", "초점과 준선의 중점")
    if t == "dist":
        d = r.randint(2, 15); return nf(d, f"포물선 위의 점 P와 초점 사이의 거리가 {d}이면 P와 준선 사이의 거리는?", f"포물선은 초점까지의 거리와 준선까지의 거리가 같은 점의 자취\n따라서 {d}", "포물선의 정의")
    if t == "fd":
        d = 2 * r.randint(1, 8); return nf(d // 2, f"초점과 준선 사이의 거리가 {d}일 때 꼭짓점과 초점 사이의 거리는?", f"꼭짓점은 초점과 준선의 중점 → {d} ÷ 2 = {d // 2}", "중점")
    a = abs(p); x = 2 * a * r.randint(1, 3)
    y = F(x * x, 4 * a)
    return nf(y, f"초점이 (0, {a}), 준선이 y = −{a}인 포물선 위에서 x좌표가 {x}인 점의 y좌표는? (기약분수 또는 정수로)", f"포물선 x² = 4py, p = {a} → x² = {4 * a}y\n{x}² = {4 * a}y → y = {fm(y)}", "x² = 4py")
def p2_eq(r):
    p = nz(r, -6, 6); ax = r.choice(["y", "x"]); t = r.choice(["focus", "dir", "make"])
    eq = f"y² = {m(4 * p)}x" if ax == "y" else f"x² = {m(4 * p)}y"
    if t == "focus": return nf(p, f"포물선 {eq}의 초점의 {'x' if ax == 'y' else 'y'}좌표는?", f"{eq} = 4p{'x' if ax == 'y' else 'y'} → 4p = {m(4 * p)}, p = {m(p)}\n초점 {'(' + m(p) + ', 0)' if ax == 'y' else '(0, ' + m(p) + ')'}", "y² = 4px의 초점 (p, 0)")
    if t == "dir": return nf(-p, f"포물선 {eq}의 준선은 {'x' if ax == 'y' else 'y'} = ?", f"4p = {m(4 * p)} → p = {m(p)}\n준선 {'x' if ax == 'y' else 'y'} = −p = {m(-p)}", "준선은 −p")
    return nf(4 * p, f"초점이 {'(' + m(p) + ', 0)' if ax == 'y' else '(0, ' + m(p) + ')'}, 준선이 {'x' if ax == 'y' else 'y'} = {m(-p)}인 포물선이 {'y² = k x' if ax == 'y' else 'x² = k y'}일 때 k의 값은?".replace("k x", "kx").replace("k y", "ky"),
              f"p = {m(p)} → 4p = {m(4 * p)}\n{eq}", "4p")
def p3_tan(r):
    p, t = r.randint(1, 4), nz(r, -3, 3)
    x1, y1 = p * t * t, 2 * p * t
    kind = r.choice(["int", "slope"])
    if kind == "int":
        b = F(y1, 2) * 0 + F(p * t, 1)  # tangent y = (1/t)x + pt
        return fill(f"포물선 y² = {4 * p}x 위의 점 ({x1}, {m(y1)})에서의 접선은 y = {fm(F(1, t)) if abs(t) != 1 else ('' if t == 1 else '−')}x + {{{{1}}}}".replace("y = 1/", "y = (1/").replace("/" + str(abs(t)) + "x", "/" + str(abs(t)) + ")x") if abs(t) != 1 else f"포물선 y² = {4 * p}x 위의 점 ({x1}, {m(y1)})에서의 접선은 y = {'' if t == 1 else '−'}x + {{{{1}}}}",
                    [ans(p * t)], f"y₁y = 2p(x + x₁) → {m(y1)}y = {2 * p}(x + {x1})\ny = {fm(F(2 * p, y1))}x + {fm(F(2 * p * x1, y1))}", "y₁y = 2p(x + x₁)")
    m_ = nz(r, -3, 3)
    v = F(p, m_)
    return nf(v, f"포물선 y² = {4 * p}x에 접하고 기울기가 {m(m_)}인 직선의 y절편은? (기약분수 또는 정수로)", f"y = mx + p/m 꼴의 접선 (p = {p})\n{p}/{par(m_)} = {fm(v)}", "y² = 4px의 접선 y = mx + p/m")
def p3_x2(r):
    p, m_ = r.randint(1, 4), nz(r, -4, 4)
    return nf(2 * p * m_, f"포물선 x² = {4 * p}y의 접선 중 기울기가 {m(m_)}인 것의 접점의 x좌표는?", f"y = x²/{4 * p}, y′ = x/{2 * p} = {m(m_)} → x = {m(2 * p * m_)}", "미분해서 기울기")
def p4_app(r):
    t = r.choice(["dish", "fd"])
    if t == "dish":
        R, d = r.choice([(4, 1), (6, 3), (6, 1), (8, 2), (10, 5), (12, 3), (4, 2), (9, 3)])
        f = F(R * R, 4 * d)
        return nf(f, f"지름 {2 * R}m, 깊이 {d}m인 포물면 접시의 초점은 바닥에서 몇 m 높이일까요? (기약분수 또는 정수로)", f"꼭짓점을 원점으로 x² = 4py, 점 ({R}, {d}) 대입: {R * R} = {4 * d}p\np = {fm(f)} (초점은 꼭짓점에서 p만큼 위)", "x² = 4py에 가장자리 대입")
    p, x = r.randint(1, 5), r.randint(1, 10)
    return nf(x + p, f"포물선 y² = {4 * p}x 위에서 x좌표가 {x}인 점과 초점 사이의 거리는?", f"초점까지 거리 = 준선 x = −{p}까지 거리 = {x} + {p} = {x + p}", "정의: 준선까지 거리와 같음")
L11 = [("포물선의 정의", p1_def)]; L12 = [("포물선의 방정식", p2_eq)]; L13 = [("포물선의 접선", p3_tan), ("접점", p3_x2)]; L14 = [("포물선의 활용", p4_app), ("포물선의 정의", p1_def)]

# ================= ch02 타원 =================
def ell():
    return [(5, 3, 4), (5, 4, 3), (13, 5, 12), (13, 12, 5), (10, 6, 8), (10, 8, 6), (17, 8, 15), (17, 15, 8), (25, 7, 24), (2, 1, None)]
def e1_def(r):
    a, b, c = r.choice([(5, 4, 3), (5, 3, 4), (13, 12, 5), (13, 5, 12), (10, 8, 6), (10, 6, 8), (17, 15, 8), (17, 8, 15), (25, 24, 7)])
    t = r.choice(["b", "c", "pf", "len"])
    if t == "b": return nf(b, f"a = {a}, c = {c}인 타원(a > b)에서 b의 값은?", f"타원: b² = a² − c² = {a * a} − {c * c} = {b * b} → b = {b}", "b² = a² − c²")
    if t == "c": return nf(c, f"a = {a}, b = {b}인 타원에서 c의 값은?", f"c² = a² − b² = {a * a} − {b * b} = {c * c} → c = {c}", "c² = a² − b²")
    if t == "len": return nf(2 * b, f"a = {a}, c = {c}인 타원의 단축의 길이는?", f"b = √({a * a} − {c * c}) = {b}\n단축 2b = {2 * b}", "단축 = 2b")
    d = r.randint(1, 2 * a - 1)
    return nf(2 * a - d, f"두 초점 F, F′까지의 거리의 합이 {2 * a}인 타원 위의 점 P에서 PF = {d}이면 PF′은?", f"PF + PF′ = 2a = {2 * a}\nPF′ = {2 * a} − {d} = {2 * a - d}", "거리의 합이 일정")
def e2_eq(r):
    a, b, c = r.choice([(5, 4, 3), (5, 3, 4), (13, 12, 5), (13, 5, 12), (10, 8, 6), (10, 6, 8), (17, 15, 8)])
    vert = r.choice([False, True]); t = r.choice(["foc", "major", "minor", "make"])
    eq = f"x²/{b * b} + y²/{a * a} = 1" if vert else f"x²/{a * a} + y²/{b * b} = 1"
    if t == "foc": return fill(f"타원 {eq}의 초점은 " + ("(0, ±{{1}})" if vert else "(±{{1}}, 0)"), [str(c)], f"c² = {a * a} − {b * b} = {c * c} → c = {c}\n장축이 {'y' if vert else 'x'}축 위", "c² = (큰 분모) − (작은 분모)")
    if t == "major": return nf(2 * a, f"타원 {eq}의 장축의 길이는?", f"큰 분모 {a * a} = a² → a = {a}\n장축 2a = {2 * a}", "장축 = 2a")
    if t == "minor": return nf(2 * b, f"타원 {eq}의 단축의 길이는?", f"작은 분모 {b * b} = b² → b = {b}\n단축 2b = {2 * b}", "단축 = 2b")
    return fill(f"두 초점이 (±{c}, 0)이고 장축의 길이가 {2 * a}인 타원은 x²/{a * a} + y²/{{{{1}}}} = 1", [str(b * b)], f"a = {a}, c = {c} → b² = {a * a} − {c * c} = {b * b}", "b² = a² − c²")
def e3_tan(r):
    if r.random() < .6:
        x0, y0 = nz(r, -4, 4), nz(r, -4, 4); A, B = 2 * x0 * x0, 2 * y0 * y0
    else:
        A, B = r.choice([(8, 2), (4, 1), (9, 4), (25, 9), (16, 9), (12, 3), (18, 2), (20, 5)])
    pts = [(x, y) for x in range(-8, 9) for y in range(-8, 9) if x * x * B + y * y * A == A * B and x and y]
    if not pts: return None
    x, y = r.choice(pts)
    t = r.choice(["line", "slope0"])
    if t == "line":
        L_ = 1  # x x1 / A + y y1 / B = 1 → multiply by A B / g
        g_ = gcd(gcd(abs(x * B), abs(y * A)), A * B)
        return fill(f"타원 x²/{A} + y²/{B} = 1 위의 점 ({m(x)}, {m(y)})에서의 접선은 {poly((x * B // g_, 'x'), (y * A // g_, 'y'))} = {{{{1}}}}", [ans(A * B // g_)],
                    f"접선: x₁x/{A} + y₁y/{B} = 1 → {m(x)}x/{A} + {m(y)}y/{B} = 1\n양변에 {A * B // g_}을 곱해 정리하면 {poly((x * B // g_, 'x'), (y * A // g_, 'y'))} = {A * B // g_}", "x₁x/a² + y₁y/b² = 1")
    return nf(isqrt(B) if isqrt(B) ** 2 == B else None, f"타원 x²/{A} + y²/{B} = 1에 접하고 기울기가 0인 직선 중 y > 0인 것은 y = ?", f"y축 위의 꼭짓점 (0, ±√{B})에서 접선이 수평 → y = {isqrt(B)}", "단축의 끝점") if isqrt(B) ** 2 == B else None
def e3_k(r):
    a2, b2, m_ = r.randint(2, 9), r.randint(1, 9), r.randint(1, 3)
    v = a2 * m_ * m_ + b2
    return nf(v, f"직선 y = {'' if m_ == 1 else m_}x + k가 타원 x²/{a2} + y²/{b2} = 1에 접할 때 k²의 값은?", f"접선 조건: k² = a²m² + b² = {a2}×{m_ * m_} + {b2} = {v}", "k² = a²m² + b²")
def e4_app(r):
    a, b, c = r.choice([(5, 4, 3), (5, 3, 4), (13, 12, 5), (10, 8, 6), (17, 15, 8)])
    t = r.choice(["peri", "aph", "area", "dist"])
    if t == "peri": return nf(a - c, f"장반경 a = {a}, 초점 거리 c = {c}인 타원 궤도에서 초점(태양)과 가장 가까운 거리는?", f"근일점 거리 = a − c = {a} − {c} = {a - c}", "a − c")
    if t == "aph": return nf(a + c, f"장반경 a = {a}, 초점 거리 c = {c}인 타원 궤도에서 초점(태양)과 가장 먼 거리는?", f"원일점 거리 = a + c = {a} + {c} = {a + c}", "a + c")
    if t == "dist": return nf(2 * c, f"타원 x²/{a * a} + y²/{b * b} = 1의 두 초점 사이의 거리는?", f"c² = {a * a} − {b * b} = {c * c} → c = {c}\n두 초점 (±{c}, 0) 사이 2c = {2 * c}", "2c")
    A, B = r.randint(2, 7), r.randint(1, 5)
    return fill(f"타원 x²/{A * A} + y²/{B * B} = 1의 넓이는 {{{{1}}}}π", [str(A * B)], f"타원의 넓이 = πab = π × {A} × {B} = {A * B}π", "πab")
L21 = [("타원의 정의", e1_def)]; L22 = [("타원의 방정식", e2_eq)]; L23 = [("타원의 접선", e3_tan), ("접선 조건", e3_k)]; L24 = [("타원의 활용", e4_app)]

# ================= ch03 쌍곡선 =================
H = [(3, 4, 5), (4, 3, 5), (5, 12, 13), (12, 5, 13), (6, 8, 10), (8, 6, 10), (8, 15, 17), (15, 8, 17)]
def h1_def(r):
    a, b, c = r.choice(H); t = r.choice(["b", "c", "e", "pf"])
    if t == "b": return nf(b, f"a = {a}, c = {c}인 쌍곡선에서 b의 값은?", f"쌍곡선: b² = c² − a² = {c * c} − {a * a} = {b * b} → b = {b}", "b² = c² − a²")
    if t == "c": return nf(c, f"a = {a}, b = {b}인 쌍곡선에서 c의 값은?", f"c² = a² + b² = {a * a} + {b * b} = {c * c} → c = {c}", "c² = a² + b²")
    if t == "e": return nf(F(c, a), f"a = {a}, c = {c}인 쌍곡선의 이심률은? (기약분수로)", f"e = c/a = {c}/{a}" + (f" = {fs(F(c, a))}" if gcd(a, c) > 1 else "") + "\n(쌍곡선은 e > 1)", "e = c/a")
    d = r.randint(2 * a + 1, 4 * a)
    return nf(d + 2 * a, f"두 초점 F, F′까지의 거리의 차가 {2 * a}인 쌍곡선 위의 점 P에서 PF = {d}일 때 PF′이 될 수 있는 값 중 큰 것은?", f"|PF − PF′| = {2 * a} → PF′ = {d} ± {2 * a}\n큰 값 {d + 2 * a}", "거리의 차가 일정")
def h2_eq(r):
    a, b, c = r.choice(H); vert = r.choice([False, True]); t = r.choice(["foc", "major", "vtx", "make"])
    eq = f"x²/{b * b} − y²/{a * a} = −1" if vert else f"x²/{a * a} − y²/{b * b} = 1"
    if t == "foc": return fill(f"쌍곡선 {eq}의 초점은 " + ("(0, ±{{1}})" if vert else "(±{{1}}, 0)"), [str(c)], f"c² = {a * a} + {b * b} = {c * c} → c = {c}", "c² = a² + b²")
    if t == "major": return nf(2 * a, f"쌍곡선 {eq}의 주축의 길이는?", f"주축의 반 a = √{a * a} = {a}, 주축 2a = {2 * a}" + ("\n(우변이 −1이면 주축이 y축 위)" if vert else ""), "주축 = 2a")
    if t == "vtx": return nf(a, f"쌍곡선 {eq}의 꼭짓점 중 {'y' if vert else 'x'}좌표가 양수인 것의 {'y' if vert else 'x'}좌표는?", f"꼭짓점 {'(0, ±' if vert else '(±'}{a}{')' if vert else ', 0)'} → {a}", "꼭짓점은 주축 위")
    return fill(f"두 초점이 (±{c}, 0)이고 주축의 길이가 {2 * a}인 쌍곡선은 x²/{a * a} − y²/{{{{1}}}} = 1", [str(b * b)], f"a = {a}, c = {c} → b² = {c * c} − {a * a} = {b * b}", "b² = c² − a²")
def h3_asym(r):
    a, b = r.randint(1, 6), r.randint(1, 6)
    if a == b and r.random() < .5: return None
    v = F(b, a)
    return nf(v, f"쌍곡선 x²/{a * a} − y²/{b * b} = 1의 점근선 중 기울기가 양수인 것의 기울기는? (기약분수 또는 정수로)".replace("x²/1 ", "x² ").replace("y²/1 ", "y² "), f"점근선 y = ±(b/a)x = ±({b}/{a})x\n양수 기울기 {fm(v)}", "y = ±(b/a)x")
def h3_tan(r):
    if r.random() < .6:
        x0, y0 = r.choice([2, 4, 6]), nz(r, -5, 5); A, B = x0 * x0 // 2, y0 * y0
    else:
        A, B = r.choice([(4, 3), (1, 1), (3, 1), (2, 1), (4, 5), (9, 4), (8, 4), (5, 4)])
    pts = [(x, y) for x in range(1, 13) for y in range(-10, 11) if x * x * B - y * y * A == A * B and y]
    if not pts: return None
    x, y = r.choice(pts); g_ = gcd(gcd(abs(x * B), abs(y * A)), A * B)
    return fill(f"쌍곡선 x²/{A} − y²/{B} = 1 위의 점 ({m(x)}, {m(y)})에서의 접선은 {poly((x * B // g_, 'x'), (-y * A // g_, 'y'))} = {{{{1}}}}".replace("x²/1 ", "x² ").replace("y²/1 ", "y² "), [ans(A * B // g_)],
                f"접선: x₁x/{A} − y₁y/{B} = 1 → {m(x)}x/{A} − {par(y)}y/{B} = 1\n정리하면 {poly((x * B // g_, 'x'), (-y * A // g_, 'y'))} = {A * B // g_}", "x₁x/a² − y₁y/b² = 1")
def h4_kind(r):
    t = r.choice(["c", "e", "p", "h"])
    a, b, c = r.randint(1, 5), r.randint(1, 5), r.randint(-4, 4)
    if t == "c": e, v = f"x² + y²{term(2 * c, 'x')} = {a * a}", 1
    elif t == "e":
        if a == b: return None
        e, v = f"{a * a if a > 1 else ''}x² + {b * b if b > 1 else ''}y²{term(2 * c, 'y')} = {a * a * b * b}", 2
    elif t == "p": e, v = r.choice([(f"y² = {m(nz(r, -9, 9))}x", 3), (f"x²{term(c, 'x')} = {m(nz(r, -9, 9))}y", 3)])
    else: e, v = f"{a * a if a > 1 else ''}x² − {b * b if b > 1 else ''}y²{term(c, 'x')} = {a * a * b * b}", 4
    why = {1: "x², y²의 계수가 같고 부호가 같음 → 원", 2: "x², y²의 계수 부호가 같고 크기가 다름 → 타원", 3: "x², y² 중 하나만 있음 → 포물선", 4: "x², y²의 계수 부호가 다름 → 쌍곡선"}[v]
    return nf(v, f"{e}은 어떤 곡선일까요?  (원 1, 타원 2, 포물선 3, 쌍곡선 4 중 번호)", f"이차항을 봅니다.\n{why} → {v}", "x², y²의 계수를 비교")
L31 = [("쌍곡선의 정의", h1_def)]; L32 = [("쌍곡선의 방정식", h2_eq)]; L33 = [("점근선", h3_asym), ("쌍곡선의 접선", h3_tan)]; L34 = [("이차곡선의 판별", h4_kind), ("쌍곡선의 정의", h1_def), ("타원의 정의", e1_def)]

# ================= ch04 평면벡터 =================
def v1_len(r):
    a, b, c = r.choice(TRI); x1, y1 = r.randint(-4, 4), r.randint(-4, 4); sx, sy = r.choice([1, -1]), r.choice([1, -1])
    return nf(c, f"A({m(x1)}, {m(y1)}), B({m(x1 + sx * a)}, {m(y1 + sy * b)})일 때 |AB|(벡터 AB의 크기)는?", f"AB = ({m(sx * a)}, {m(sy * b)})\n|AB| = √({a}² + {b}²) = {c}", "크기 = √(x² + y²)")
def v2_size(r):
    t = r.choice(["perp", "scal"])
    if t == "perp":
        a, b, c = r.choice(TRI); return nf(c, f"|a| = {a}, |b| = {b}이고 a와 b가 수직일 때 |a + b|는?", f"|a + b|² = |a|² + 2a·b + |b|² = {a * a} + 0 + {b * b} = {c * c}\n|a + b| = {c}", "수직이면 a·b = 0")
    k, s = nz(r, -5, 5), r.randint(1, 6)
    return nf(abs(k) * s, f"|a| = {s}일 때 |{m(k)}a|는?".replace("|1a|", "|a|"), f"|ka| = |k||a| = {abs(k)} × {s} = {abs(k) * s}", "실수배의 크기")
def v2_coef(r):
    p, q, k, m_ = r.randint(-4, 5), r.randint(-4, 5), r.randint(-4, 5), r.randint(-4, 5)
    ask = r.choice(["k", "m"])
    # (k − 1)a + 2b = p a + q b → k = p + 1, m = 2? keep generic: (k + c)a + d b = p a + m b
    c, d = r.randint(-3, 3), r.randint(1, 5)
    return nf(p - c if ask == "k" else d, f"영벡터가 아니고 평행하지 않은 a, b에 대해 (k{term(c)})a + {d}b = {m(p)}a + mb일 때 {ask}의 값은?".replace("(k)a", "ka").replace(" 1b", " b"),
              f"a, b가 평행하지 않으면 계수끼리 같아야 합니다.\nk{term(c)} = {m(p)} → k = {m(p - c)}, m = {d}", "계수 비교")
def v3_comp(r):
    a, b, c, d = [r.randint(-5, 6) for _ in range(4)]; k, l = nz(r, -3, 3), nz(r, -3, 3)
    t = r.choice(["lin", "par", "unit", "ab"])
    if t == "lin":
        return fill(f"{m(k)}{vec(a, b)} + {par(l)}{vec(c, d)} = ({{{{1}}}}, {{{{2}}}})".replace("1(", "(").replace("+ (1)(", "+ (").replace("−1(", "−("), [ans(k * a + l * c), ans(k * b + l * d)],
                    f"성분끼리: x = {m(k)}×{par(a)} + {par(l)}×{par(c)} = {m(k * a + l * c)}\ny = {m(k)}×{par(b)} + {par(l)}×{par(d)} = {m(k * b + l * d)}", "성분끼리 계산")
    if t == "par":
        p, q, s_ = nz(r, -4, 4), nz(r, -4, 4), nz(r, -3, 3)
        return nf(q * s_, f"{vec(p * s_, 'k')}와 {vec(p, q)}가 평행할 때 k의 값은?".replace("'k'", "k"), f"평행 ⇔ 한쪽이 다른 쪽의 실수배\n{m(p * s_)} = {m(s_)}×{par(p)} → k = {m(s_)}×{par(q)} = {m(q * s_)}", "성분의 비가 같음")
    if t == "unit":
        a_, b_, c_ = r.choice(TRI); sx = r.choice([1, -1])
        return fill(f"{vec(sx * a_, b_)}와 같은 방향의 단위벡터는 ({{{{1}}}}/{c_}, {b_}/{c_})", [ans(sx * a_)], f"크기 {c_}로 나눔: ({m(sx * a_)}/{c_}, {b_}/{c_})", "벡터 ÷ 크기")
    return fill(f"A({m(a)}, {m(b)}), B({m(c)}, {m(d)})일 때 AB = ({{{{1}}}}, {{{{2}}}})", [ans(c - a), ans(d - b)], f"AB = B − A = ({m(c)} − {par(a)}, {m(d)} − {par(b)}) = ({m(c - a)}, {m(d - b)})", "종점 − 시점")
def v4_dot(r):
    t = r.choice(["comp", "angle", "perp", "deg", "self"])
    if t == "comp":
        a, b, c, d = [r.randint(-5, 6) for _ in range(4)]
        return nf(a * c + b * d, f"{vec(a, b)}·{vec(c, d)}의 값은?", f"내적 = x₁x₂ + y₁y₂ = {m(a)}×{par(c)} + {par(b)}×{par(d)} = {m(a * c + b * d)}", "성분끼리 곱해서 더함")
    if t == "angle":
        a, b, th = r.randint(1, 6), r.randint(1, 6), r.choice([60, 120, 90, 0, 180])
        cs = {60: F(1, 2), 120: F(-1, 2), 90: 0, 0: 1, 180: -1}[th]
        return nf(a * b * cs, f"|a| = {a}, |b| = {b}이고 이루는 각이 {th}°일 때 a·b는? (기약분수 또는 정수로)", f"a·b = |a||b|cos θ = {a} × {b} × cos {th}° = {a * b} × {fm(F(cs))} = {fm(a * b * cs)}", "|a||b|cos θ")
    if t == "perp":
        a, c, d = nz(r, -4, 4), nz(r, -5, 5), nz(r, -5, 5)
        v = F(-a * c, d)
        return nf(v, f"{vec(a, 'k').replace(chr(39), '')}와 {vec(c, d)}가 수직일 때 k의 값은? (기약분수 또는 정수로)".replace("'k'", "k"), f"수직 ⇔ 내적 0: {m(a)}×{par(c)} + k×{par(d)} = 0\n{poly((d, 'k'))} = {m(-a * c)} → k = {fm(v)}", "내적 = 0")
    if t == "deg":
        u, w, th = r.choice([((1, 0), (1, 1), 45), ((1, 0), (0, 1), 90), ((1, 1), (-1, 1), 90), ((1, 0), (-1, 1), 135), ((2, 0), (1, 1), 45), ((0, 1), (1, 1), 45), ((1, 0), (-1, 0), 180), ((1, 2), (2, 4), 0)])
        return nf(th, f"{vec(*u)}과 {vec(*w)}이 이루는 각은 몇 도일까요?", f"cos θ = (a·b)/(|a||b|) = {u[0] * w[0] + u[1] * w[1]}/(√{u[0] ** 2 + u[1] ** 2} × √{w[0] ** 2 + w[1] ** 2})\n→ θ = {th}°", "cos θ = a·b/(|a||b|)")
    a, b = r.randint(-6, 6), r.randint(-6, 6)
    return nf(a * a + b * b, f"{vec(a, b)}·{vec(a, b)}의 값은?", f"자기 자신과의 내적 = 크기의 제곱 = {a * a} + {b * b} = {a * a + b * b}", "a·a = |a|²")
L41 = [("벡터의 크기", v1_len), ("실수배·수직의 크기", v2_size)]; L42 = [("크기 계산", v2_size), ("계수 비교", v2_coef)]; L43 = [("성분 계산", v3_comp)]; L44 = [("내적", v4_dot)]

# ================= ch05 벡터의 활용 =================
def w1_line(r):
    x0, y0, a, b = r.randint(-4, 4), r.randint(-4, 4), nz(r, -4, 4), nz(r, -4, 4)
    t = r.choice(["param", "normal", "slope"])
    if t == "param":
        tt = r.randint(-2, 3); return nf(x0 + a * tt, f"점 ({m(x0)}, {m(y0)})를 지나고 방향벡터가 {vec(a, b)}인 직선 (x, y) = ({m(x0)}, {m(y0)}) + t{vec(a, b)}에서 t = {m(tt)}일 때 점의 x좌표는?", f"x = {m(x0)} + {m(a)}×{par(tt)} = {m(x0 + a * tt)}", "x = x₀ + at")
    if t == "normal":
        return fill(f"점 ({m(x0)}, {m(y0)})를 지나고 법선벡터가 {vec(a, b)}인 직선은 {poly((a, 'x'), (b, 'y'))} = {{{{1}}}}", [ans(a * x0 + b * y0)], f"법선벡터 (a, b)에 수직 → a(x − x₀) + b(y − y₀) = 0\n{poly((a, 'x'), (b, 'y'))} = {m(a)}×{par(x0)} + {par(b)}×{par(y0)} = {m(a * x0 + b * y0)}", "a(x − x₀) + b(y − y₀) = 0")
    return nf(F(b, a), f"방향벡터가 {vec(a, b)}인 직선의 기울기는? (기약분수 또는 정수로)", f"기울기 = (y 성분)/(x 성분) = {m(b)}/{m(a)} = {fm(F(b, a))}", "b/a")
def w2_circ(r):
    t = r.choice(["rad", "diam", "apol", "tan"])
    if t == "rad":
        a, b, k = r.randint(-4, 4), r.randint(-4, 4), r.randint(1, 8); return nf(k, f"|p − {vec(a, b)}| = {k}가 나타내는 원의 반지름은?", f"점 {vec(a, b)}에서 거리가 {k}인 점의 자취 → 반지름 {k}", "|p − c| = r")
    if t == "diam":
        x1, x2 = sorted(r.sample(range(-6, 7), 2))
        if (x2 - x1) % 2: return None
        return nf((x2 - x1) // 2, f"A({m(x1)}, 0), B({m(x2)}, 0)에 대해 (p − a)·(p − b) = 0이 나타내는 원의 반지름은?", f"PA ⊥ PB인 점 P → AB를 지름으로 하는 원\n반지름 ({m(x2)} − {par(x1)})/2 = {(x2 - x1) // 2}", "지름 위의 원주각은 90°")
    if t == "apol":
        d, k = r.choice([3, 6, 9, 4, 8]), 2
        # |PA| = 2|PB|, A(0,0), B(d,0): x²+y² = 4((x−d)²+y²) → 3x² − 8dx + 4d² + 3y² = 0 → center 4d/3, r 2d/3
        ask = r.choice(["r", "c"])
        return nf(F(2 * d, 3) if ask == "r" else F(4 * d, 3), f"A(0, 0), B({d}, 0)에 대해 |PA| = 2|PB|인 점 P의 자취는 원입니다. 그 {'반지름' if ask == 'r' else '중심의 x좌표'}는? (기약분수 또는 정수로)",
                  f"x² + y² = 4((x − {d})² + y²) → 3x² − {8 * d}x + 3y² + {4 * d * d} = 0\n(x − {fs(F(4 * d, 3))})² + y² = ({fs(F(2 * d, 3))})² → 중심 {fs(F(4 * d, 3))}, 반지름 {fs(F(2 * d, 3))}", "식을 세워 완전제곱식으로")
    a, b, c = r.choice(TRI); x, y = a * r.choice([1, -1]), b * r.choice([1, -1])
    return fill(f"원 x² + y² = {c * c} 위의 점 ({m(x)}, {m(y)})에서의 접선은 {poly((x, 'x'), (y, 'y'))} = {{{{1}}}}", [str(c * c)], f"접점의 위치벡터 p₁에 수직: p₁·p = r²\n{poly((x, 'x'), (y, 'y'))} = {c * c}", "x₁x + y₁y = r²")
def w3_pp(r):
    t = r.choice(["perp", "par", "col", "proj"])
    if t == "perp":
        a, c = nz(r, -4, 4), nz(r, -4, 4); d = nz(r, -4, 4)
        v = F(-a * c, d)
        if v.denominator != 1: return None
        return nf(v, f"{vec(a, 'k')}와 {vec(c, d)}가 수직일 때 k의 값은?".replace("'k'", "k"), f"내적 0: {m(a)}×{par(c)} + {m(d)}k = 0 → k = {m(int(v))}", "수직 ⇔ 내적 0")
    if t == "par":
        c, d, s_ = nz(r, -4, 4), nz(r, -4, 4), nz(r, -3, 3)
        return nf(c * s_, f"(k, {m(d * s_)})와 {vec(c, d)}가 평행할 때 k의 값은?", f"({m(d * s_)}) = {m(s_)} × {par(d)} → k = {m(s_)} × {par(c)} = {m(c * s_)}", "실수배")
    if t == "col":
        x0, y0, a, b = r.randint(-3, 3), r.randint(-3, 3), nz(r, -3, 3), nz(r, -3, 3); tt = r.choice([2, 3, -1, -2])
        return nf(y0 + b * tt, f"세 점 A({m(x0)}, {m(y0)}), B({m(x0 + a)}, {m(y0 + b)}), C({m(x0 + a * tt)}, k)가 한 직선 위에 있을 때 k의 값은?", f"AC = t·AB: AB = ({m(a)}, {m(b)}), x 성분 비 t = {m(tt)}\nk = {m(y0)} + {m(tt)}×{par(b)} = {m(y0 + b * tt)}", "AC가 AB의 실수배")
    a, b, c = r.choice(TRI)
    u = r.choice([(1, 0), (0, 1)])
    v = a if u == (1, 0) else b
    return nf(v, f"a = ({a}, {b})를 b = {vec(*u)} 방향으로 정사영한 길이는?", f"정사영 길이 = a·b/|b| = {v}/1 = {v}", "a·b ÷ |b|")
def w4_pos(r):
    t = r.choice(["div", "cent", "mid"])
    if t == "div":
        p, q = r.choice([(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2)])
        return fill(f"선분 AB를 {p} : {q}로 내분하는 점의 위치벡터는 ({q if q > 1 else ''}a + {{{{1}}}}b)/{p + q}", [str(p)], f"내분점 = (n·a + m·b)/(m + n) (m : n = {p} : {q})\n= ({q}a + {p}b)/{p + q}", "가까운 쪽에 큰 가중치")
    pts = [(r.randint(-6, 9), r.randint(-6, 9)) for _ in range(3)]
    sx = sum(x for x, _ in pts)
    if sx % 3: return None
    return nf(sx // 3, f"세 점 {', '.join(vec(*p_) for p_ in pts)}을 꼭짓점으로 하는 삼각형의 무게중심의 x좌표는?", f"무게중심의 위치벡터 (a + b + c)/3\nx좌표 ({' + '.join(m(x) for x, _ in pts)})/3 = {m(sx // 3)}", "(a + b + c)/3")
L51 = [("직선의 벡터방정식", w1_line)]; L52 = [("원의 벡터방정식", w2_circ)]; L53 = [("평행과 수직", w3_pp)]; L54 = [("위치벡터", w4_pos)]

# ================= ch06 공간도형 =================
CV = dict(zip("ABCDEFGH", [(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0,0,1),(1,0,1),(1,1,1),(0,1,1)]))
CE = [e for e in ["AB","BC","CD","DA","EF","FG","GH","HE","AE","BF","CG","DH"]]
def edir(e): return tuple(abs(a - b) for a, b in zip(CV[e[0]], CV[e[1]]))
CF = {"ABCD": (2, 0), "EFGH": (2, 1), "ABFE": (1, 0), "DCGH": (1, 1), "ADHE": (0, 0), "BCGF": (0, 1)}
def s1_cube(r):
    e1, e2 = r.sample(CE, 2)
    if set(e1) & set(e2): v, why = 1, f"점 {(set(e1) & set(e2)).pop()}에서 만남"
    elif edir(e1) == edir(e2): v, why = 2, "같은 방향의 모서리 → 평행"
    else: v, why = 3, "만나지도 않고 평행하지도 않음 → 꼬인 위치"
    return nf(v, f"정육면체 ABCD-EFGH에서 모서리 {e1}와 {e2}의 위치 관계는?  (만난다 1, 평행하다 2, 꼬인 위치 3 중 번호)", f"정육면체 그림에서 확인합니다.\n{e1}와 {e2}: {why} → {v}", "같은 평면 위에 있는지 먼저 보세요.")
def s1_count(r):
    if r.random() < .6:
        e = r.choice(CE); k = r.choice(["skew", "par", "meet"])
        nm = {"skew": "꼬인 위치에 있는", "par": "평행한", "meet": "만나는"}[k]
        lst = [f for f in CE if f != e and ({"skew": not (set(e) & set(f)) and edir(e) != edir(f), "par": edir(e) == edir(f), "meet": bool(set(e) & set(f))}[k])]
        return nf(len(lst), f"정육면체 ABCD-EFGH에서 모서리 {e}와 {nm} 모서리는 몇 개일까요?", f"하나씩 확인하면 {', '.join(lst)}\n→ {len(lst)}개", "그림을 그려 세세요.")
    fc = r.choice(list(CF)); ax, lv = CF[fc]; k = r.choice(["pe", "ve", "vf", "pf", "in"])
    on = lambda e: all(CV[c][ax] == lv for c in e)
    if k == "pe": lst = [e for e in CE if not any(CV[c][ax] == lv for c in e)]; nm = "평행한 모서리"
    elif k == "ve": lst = [e for e in CE if edir(e)[ax] == 1]; nm = "수직인 모서리"
    elif k == "in": lst = [e for e in CE if on(e)]; nm = "포함된 모서리"
    elif k == "vf": lst = [f for f, (a2, _) in CF.items() if a2 != ax]; nm = "수직인 면"
    else: lst = [f for f, (a2, l2) in CF.items() if a2 == ax and l2 != lv]; nm = "평행한 면"
    return nf(len(lst), f"정육면체 ABCD-EFGH에서 면 {fc}와 {nm}{'은' if nm.endswith('면') else '는'} 몇 개일까요?", f"하나씩 확인하면 {', '.join(lst)}\n→ {len(lst)}개", "그림을 그려 세세요.")
def s2_three(r):
    a, b, c = r.choice(TRI + [(7, 24, 25), (24, 7, 25), (20, 21, 29), (15, 8, 17), (12, 9, 15), (15, 20, 25), (10, 24, 26), (24, 10, 26)])
    k = r.choice([1, 1, 2, 3]) if c * 3 < 80 else 1; a, b, c = a * k, b * k, c * k; t = r.choice(["PH", "OH", "PO"])
    if t == "PH": return nf(c, f"평면 α 밖의 점 P에서 α에 내린 수선의 발이 O, O에서 α 위의 직선 l에 내린 수선의 발이 H입니다. PO = {a}, OH = {b}일 때 PH는?", f"삼수선 정리로 PH ⊥ l, △POH는 직각삼각형\nPH = √({a}² + {b}²) = {c}", "삼수선 정리 + 피타고라스")
    if t == "OH": return nf(b, f"삼수선 정리 상황에서 PO = {a}, PH = {c}일 때 OH는?", f"OH = √({c}² − {a}²) = {b}", "직각삼각형 POH")
    return nf(a, f"삼수선 정리 상황에서 OH = {b}, PH = {c}일 때 PO는?", f"PO = √({c}² − {b}²) = {a}", "직각삼각형 POH")
def s3_proj(r):
    L_, th = r.randint(2, 20), r.choice([60, 0, 90])
    t = r.choice(["len", "area", "area30"])
    if t == "len":
        v = {60: F(L_, 2), 0: L_, 90: 0}[th]
        return nf(v, f"길이 {L_}인 선분이 평면과 {th}°를 이룰 때 정사영의 길이는? (기약분수 또는 정수로)", f"정사영의 길이 = l cos θ = {L_} × cos {th}° = {fm(v)}", "l cos θ")
    if t == "area":
        S = r.randint(2, 30); return nf(F(S, 2), f"넓이 {S}인 도형이 평면과 60°를 이룰 때 정사영의 넓이는? (기약분수 또는 정수로)", f"S′ = S cos θ = {S} × 1/2 = {fm(F(S, 2))}", "S cos θ")
    S = 2 * r.randint(1, 15)
    return fill(f"넓이 {S}인 도형이 평면과 30°를 이룰 때 정사영의 넓이는 {{{{1}}}}√3", [str(S // 2)], f"S′ = S cos 30° = {S} × √3/2 = {S // 2}√3", "cos 30° = √3/2")
def s4_dih(r):
    t = r.choice(["half", "root2", "cube"])
    if t == "half":
        S = r.randint(2, 20); return nf(60, f"넓이 {2 * S}인 도형의 정사영의 넓이가 {S}일 때 두 평면이 이루는 각은 몇 도일까요?", f"cos θ = {S}/{2 * S} = 1/2 → θ = 60°", "cos θ = S′/S")
    if t == "root2":
        S = 2 * r.randint(1, 10); return nf(45, f"넓이 {S}인 도형의 정사영의 넓이가 {S // 2}√2일 때 두 평면이 이루는 각은 몇 도일까요?", f"cos θ = {S // 2}√2/{S} = √2/2 → θ = 45°", "cos θ = S′/S")
    return nf(45, "정육면체 ABCD-EFGH에서 면 ABCD와 평면 ABGH가 이루는 이면각은 몇 도일까요?", "AB에 수직인 단면(정사각형 BCGF)에서 보면 BC와 BG가 이루는 각\n대각선과 변의 각 → 45°", "교선에 수직인 단면")
L61 = [("모서리의 위치 관계", s1_cube), ("개수 세기", s1_count)]; L62 = [("삼수선 정리", s2_three)]; L63 = [("정사영", s3_proj)]; L64 = [("이면각", s4_dih), ("정사영", s3_proj)]

# ================= ch07 공간좌표 =================
def c1_pt(r):
    x, y, z = nz(r, -6, 6), nz(r, -6, 6), nz(r, -6, 6)
    t = r.choice(["xy", "yz", "zx", "o", "xa", "za"])
    nm, (nx, ny, nz_) = {"xy": ("xy평면", (x, y, -z)), "yz": ("yz평면", (-x, y, z)), "zx": ("zx평면", (x, -y, z)), "o": ("원점", (-x, -y, -z)),
                          "xa": ("x축", (x, -y, -z)), "za": ("z축", (-x, -y, z))}[t]
    return fill(f"점 {vec(x, y, z)}을 {nm}에 대하여 대칭이동한 점은 ({{{{1}}}}, {{{{2}}}}, {{{{3}}}})".replace(f"{vec(x, y, z)}을", vec(x, y, z) + ("을" if bat(abs(z)) else "를")), [ans(nx), ans(ny), ans(nz_)],
                f"{nm}에 대한 대칭: " + {"xy": "z좌표의 부호만", "yz": "x좌표의 부호만", "zx": "y좌표의 부호만", "o": "세 좌표의 부호 모두", "xa": "x좌표는 그대로, 나머지 부호", "za": "z좌표는 그대로, 나머지 부호"}[t] + f" 바꿈\n→ {vec(nx, ny, nz_)}", "어느 좌표가 그대로인지 보세요.")
def c2_dist(r):
    a, b, c, d = r.choice(Q4); x, y, z = [r.randint(-3, 3) for _ in range(3)]
    s = [r.choice([1, -1]) for _ in range(3)]
    return nf(d, f"두 점 {vec(x, y, z)}, {vec(x + s[0] * a, y + s[1] * b, z + s[2] * c)} 사이의 거리는?", f"√(Δx² + Δy² + Δz²) = √({a}² + {b}² + {c}²) = √{d * d} = {d}", "공간의 거리 공식")
def c2_div(r):
    A = [r.randint(-5, 6) for _ in range(3)]; B = [r.randint(-5, 6) for _ in range(3)]; p, q = r.choice([(1, 1), (1, 2), (2, 1), (1, 3), (3, 1)])
    P = [F(p * b + q * a, p + q) for a, b in zip(A, B)]
    if any(v.denominator != 1 for v in P): return None
    k = r.randint(0, 2)
    return nf(P[k], f"A{vec(*A)}, B{vec(*B)}를 {p} : {q}로 내분하는 점의 {'xyz'[k]}좌표는?" if (p, q) != (1, 1) else f"A{vec(*A)}, B{vec(*B)}의 중점의 {'xyz'[k]}좌표는?",
              f"({p}×{par(B[k])} + {q}×{par(A[k])})/{p + q} = {m(int(P[k]))}", "평면과 같은 내분점 공식")
def c3_sph(r):
    a, b, c = [r.randint(-4, 4) for _ in range(3)]; R = r.randint(1, 6)
    t = r.choice(["c", "r", "touch", "origin"])
    if t in ("c", "r"):
        k = a * a + b * b + c * c - R * R
        eq = poly((1, 'x²'), (1, 'y²'), (1, 'z²'), (-2 * a, 'x'), (-2 * b, 'y'), (-2 * c, 'z'), (k, ''))
        if t == "c": return fill(f"구 {eq} = 0의 중심은 ({{{{1}}}}, {{{{2}}}}, {{{{3}}}})", [ans(a), ans(b), ans(c)], f"완전제곱식: (x{term(-a)})² + (y{term(-b)})² + (z{term(-c)})² = {R * R}\n중심 {vec(a, b, c)}".replace("(x)²", "x²").replace("(y)²", "y²").replace("(z)²", "z²"), "x, y, z끼리 완전제곱식")
        return nf(R, f"구 {eq} = 0의 반지름은?", f"(x{term(-a)})² + (y{term(-b)})² + (z{term(-c)})² = {R * R} → 반지름 {R}".replace("(x)²", "x²").replace("(y)²", "y²").replace("(z)²", "z²"), "완전제곱식")
    if t == "touch":
        pl = r.choice(["xy", "yz", "zx"]); v = abs({"xy": c, "yz": a, "zx": b}[pl])
        if v == 0: return None
        return nf(v, f"중심이 {vec(a, b, c)}이고 {pl}평면에 접하는 구의 반지름은?", f"{pl}평면까지의 거리 = |{'z' if pl == 'xy' else 'x' if pl == 'yz' else 'y'}좌표| = {v}", "평면까지의 거리")
    return nf(a * a + b * b + c * c, f"중심이 {vec(a, b, c)}이고 원점을 지나는 구의 반지름의 제곱은?", f"r² = {a}² + {b}² + {c}² = {a * a + b * b + c * c}".replace("−", "(−").replace("² +", "² +"), "중심과 원점 사이 거리의 제곱")
def c4_vec(r):
    t = r.choice(["len", "dot", "perp", "add"])
    if t == "len":
        a, b, c, d = r.choice(Q4); return nf(d, f"벡터 ({a}, {b}, {c})의 크기는?", f"√({a}² + {b}² + {c}²) = √{d * d} = {d}", "√(x² + y² + z²)")
    u = [r.randint(-4, 5) for _ in range(3)]; v = [r.randint(-4, 5) for _ in range(3)]
    if t == "dot": return nf(sum(a * b for a, b in zip(u, v)), f"{vec(*u)}·{vec(*v)}의 값은?", f"{' + '.join(f'{par(a)}×{par(b)}' for a, b in zip(u, v))} = {m(sum(a * b for a, b in zip(u, v)))}", "성분끼리 곱해 더함")
    if t == "perp":
        if v[2] == 0: return None
        k = F(-(u[0] * v[0] + u[1] * v[1]), v[2])
        if k.denominator != 1: return None
        return nf(k, f"({m(u[0])}, {m(u[1])}, k)와 {vec(*v)}가 수직일 때 k의 값은?", f"내적 0: {m(u[0] * v[0] + u[1] * v[1])} + {m(v[2])}k = 0 → k = {m(int(k))}", "내적 = 0")
    c = nz(r, -3, 3)
    w = [a + c * b for a, b in zip(u, v)]
    return fill(f"{vec(*u)} + {par(c)}{vec(*v)} = ({{{{1}}}}, {{{{2}}}}, {{{{3}}}})".replace("+ 1(", "+ (").replace("+ (−1)(", "− ("), [ans(x) for x in w], f"성분끼리: " + ", ".join(f"{m(a)} + {par(c)}×{par(b)} = {m(x)}" for a, b, x in zip(u, v, w)), "성분끼리 계산")
L71 = [("대칭이동", c1_pt)]; L72 = [("거리", c2_dist), ("내분점", c2_div)]; L73 = [("구의 방정식", c3_sph)]; L74 = [("공간벡터", c4_vec)]

ALL = {"ch01": [L11, L12, L13, L14], "ch02": [L21, L22, L23, L24], "ch03": [L31, L32, L33, L34], "ch04": [L41, L42, L43, L44],
       "ch05": [L51, L52, L53, L54], "ch06": [L61, L62, L63, L64], "ch07": [L71, L72, L73, L74]}

if __name__ == "__main__":
    tot = 0
    for ch, Ls in ALL.items():
        for i, T in enumerate(Ls, 1):
            per = {1: 40, 2: 20, 3: 14, 4: 10, 5: 8}.get(len(T), 6)
            n = write("c6", ch, f"l0{i}", T, per=per, seed=17 + i); tot += n; print(ch, i, len(T), n)
    print("total", tot)
