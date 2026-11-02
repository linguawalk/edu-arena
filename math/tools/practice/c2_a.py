"""코스 2 · 챕터 1~3 (좌표평면, 원과 도형의 이동, 함수) — 연습 문제 은행"""
from core import *
from math import perm

def nz(r, a, b):
    while True:
        x = r.randint(a, b)
        if x: return x
def pt(x, y): return f"({fm(x)}, {fm(y)})"
TRI = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (7, 24, 25)]
def lin(a, b): return poly((a, 'x'), (b, ''))
def sq(v, c): return f"(x{term(-c)})²" if c else f"{v}²"

# ================= ch01 좌표평면 =================
def d1_line(r):
    a, b = r.sample(range(-9, 10), 2)
    return num(f"수직선 위의 두 점 A({m(a)}), B({m(b)}) 사이의 거리는?", abs(a - b),
               f"수직선 위 두 점 사이 거리 = |b − a|\n|{m(b)} − {par(a)}| = |{m(b - a)}| = {abs(a - b)}", "두 좌표의 차의 절댓값")

def d1_plane(r):
    a, b, c = r.choice(TRI)
    if r.random() < .5: a, b = b, a
    x1, y1 = r.randint(-5, 5), r.randint(-5, 5); sx, sy = r.choice([1, -1]), r.choice([1, -1])
    return num(f"두 점 {pt(x1, y1)}, {pt(x1 + sx * a, y1 + sy * b)} 사이의 거리는?", c,
               f"√((x₂ − x₁)² + (y₂ − y₁)²)\n= √({a}² + {b}²) = √{c * c} = {c}", "x좌표의 차와 y좌표의 차를 제곱해 더하세요.")

def d1_irr(r):
    a, b = r.randint(1, 6), r.randint(1, 6)
    if isqrt(a * a + b * b) ** 2 == a * a + b * b: return None
    x1, y1 = r.randint(-3, 3), r.randint(-3, 3)
    return fill(f"두 점 {pt(x1, y1)}, {pt(x1 + a, y1 - b)} 사이의 거리는 √{{{{1}}}}", [str(a * a + b * b)],
                f"x좌표의 차 {a}, y좌표의 차 {b}\n거리 = √({a}² + {b}²) = √{a * a + b * b}", "제곱해 더한 값이 제곱수가 아니면 √로 둡니다.")

def d1_find(r):
    a, b, c = r.choice(TRI[:4]); x1, y1 = r.randint(-3, 4), r.randint(-3, 4)
    return num(f"A{pt(x1, y1)}, B(a, {m(y1 + b)}) 사이의 거리가 {c}이고 a > {m(x1)}일 때 a의 값은?", x1 + a,
               f"(a − {par(x1)})² + {b}² = {c}²\n(a − {par(x1)})² = {c * c - b * b} → a − {par(x1)} = ±{a}\na > {m(x1)}이므로 a = {m(x1 + a)}", "거리 공식으로 방정식을 세우세요.")

def d1_equi(r):
    x1, y1, x2, y2 = [r.randint(-4, 6) for _ in range(4)]
    if (x1, y1) == (x2, y2): return None
    ax = r.choice(["x", "y"])
    if ax == "x":
        if x1 == x2: return None
        p = F(x2 * x2 + y2 * y2 - x1 * x1 - y1 * y1, 2 * (x2 - x1))
        return num(f"두 점 A{pt(x1, y1)}, B{pt(x2, y2)}에서 같은 거리에 있는 x축 위의 점 P(p, 0)에서 p의 값은? (기약분수 또는 정수로)", p,
                   f"AP² = BP²: (p − {par(x1)})² + {y1 * y1} = (p − {par(x2)})² + {y2 * y2}\np²이 지워지고 {m(2 * (x2 - x1))}p = {x2 * x2 + y2 * y2 - x1 * x1 - y1 * y1}\np = {fm(p)}",
                   "AP = BP를 제곱해서 세우세요.", fmt="fraction" if p.denominator > 1 else "integer")
    if y1 == y2: return None
    q = F(x2 * x2 + y2 * y2 - x1 * x1 - y1 * y1, 2 * (y2 - y1))
    return num(f"두 점 A{pt(x1, y1)}, B{pt(x2, y2)}에서 같은 거리에 있는 y축 위의 점 P(0, q)에서 q의 값은? (기약분수 또는 정수로)", q,
               f"AP² = BP²: {x1 * x1} + (q − {par(y1)})² = {x2 * x2} + (q − {par(y2)})²\nq²이 지워지고 {m(2 * (y2 - y1))}q = {x2 * x2 + y2 * y2 - x1 * x1 - y1 * y1}\nq = {fm(q)}",
               "AP = BP를 제곱해서 세우세요.", fmt="fraction" if q.denominator > 1 else "integer")

def d1_perim(r):
    a, b, c = r.choice(TRI)
    x0, y0 = r.randint(-3, 3), r.randint(-3, 3)
    return num(f"세 점 {pt(x0, y0)}, {pt(x0 + a, y0)}, {pt(x0, y0 + b)}를 꼭짓점으로 하는 삼각형의 둘레는?", a + b + c,
               f"두 변은 축에 평행: {a}, {b}\n빗변: √({a}² + {b}²) = {c}\n둘레 = {a} + {b} + {c} = {a + b + c}", "축에 평행한 두 변과 빗변")

def d1_reflect(r):
    x1, y1, x2, y2 = r.randint(-3, 2), r.randint(1, 5), r.randint(3, 8), r.randint(1, 5)
    dx, dy = x2 - x1, y1 + y2
    s = dx * dx + dy * dy
    if isqrt(s) ** 2 != s: return None
    return num(f"A{pt(x1, y1)}, B{pt(x2, y2)}이고 P가 x축 위를 움직일 때 AP + PB의 최솟값은?", isqrt(s),
               f"B를 x축에 대해 대칭이동: B'{pt(x2, -y2)}\nAP + PB = AP + PB' ≥ AB'\nAB' = √({dx}² + {dy}²) = √{s} = {isqrt(s)}",
               "한 점을 x축에 대해 대칭이동하면 직선 거리가 됩니다.")

L11 = [("수직선 위의 거리", d1_line), ("평면 위의 거리", d1_plane), ("거리가 무리수", d1_irr), ("거리로 좌표 구하기", d1_find),
       ("같은 거리에 있는 점", d1_equi), ("삼각형의 둘레", d1_perim), ("거리의 합의 최솟값", d1_reflect)]

def d2_line(r):
    a, b = r.sample(range(-8, 15), 2); p, q = r.choice([(1, 1), (1, 2), (2, 1), (1, 3), (3, 1), (2, 3)])
    v = F(p * b + q * a, p + q)
    if v.denominator != 1: return None
    return num(f"수직선 위의 A({m(a)}), B({m(b)})를 {p} : {q}로 내분하는 점의 좌표는?" if (p, q) != (1, 1) else f"수직선 위의 A({m(a)}), B({m(b)})의 중점의 좌표는?", int(v),
               f"내분점 = (mb + na)/(m + n) = ({p}×{par(b)} + {q}×{par(a)})/{p + q} = {m(p * b + q * a)}/{p + q} = {m(int(v))}", "가까운 쪽 점에 큰 가중치")

def d2_plane(r):
    x1, y1, x2, y2 = [r.randint(-6, 9) for _ in range(4)]; p, q = r.choice([(1, 2), (2, 1), (1, 3), (3, 1), (1, 1), (2, 3)])
    X, Y = F(p * x2 + q * x1, p + q), F(p * y2 + q * y1, p + q)
    if X.denominator != 1 or Y.denominator != 1 or (x1, y1) == (x2, y2): return None
    return fill((f"A{pt(x1, y1)}, B{pt(x2, y2)}를 {p} : {q}로 내분하는 점은 ({{{{1}}}}, {{{{2}}}})" if (p, q) != (1, 1) else f"A{pt(x1, y1)}, B{pt(x2, y2)}의 중점은 ({{{{1}}}}, {{{{2}}}})"), [ans(int(X)), ans(int(Y))],
                f"x: ({p}×{par(x2)} + {q}×{par(x1)})/{p + q} = {m(int(X))}\ny: ({p}×{par(y2)} + {q}×{par(y1)})/{p + q} = {m(int(Y))}", "(mx₂ + nx₁)/(m + n)")

def d2_cent(r):
    pts = [(r.randint(-5, 8), r.randint(-5, 8)) for _ in range(3)]
    sx, sy = sum(p[0] for p in pts), sum(p[1] for p in pts)
    if sx % 3 or sy % 3: return None
    return fill(f"세 점 {', '.join(pt(*p) for p in pts)}을 꼭짓점으로 하는 삼각형의 무게중심은 ({{{{1}}}}, {{{{2}}}})", [ans(sx // 3), ans(sy // 3)],
                f"무게중심 = (세 x좌표의 평균, 세 y좌표의 평균)\nx: {sx} ÷ 3 = {m(sx // 3)}, y: {sy} ÷ 3 = {m(sy // 3)}", "좌표의 평균")

def d2_mid(r):
    x1, y1, mx, my = [r.randint(-5, 6) for _ in range(4)]
    ask = r.choice(["x", "y"])
    return num(f"선분 AB의 중점이 {pt(mx, my)}이고 A{pt(x1, y1)}일 때 B의 {ask}좌표는?", 2 * mx - x1 if ask == "x" else 2 * my - y1,
               f"중점 = (A + B)/2이므로 B = 2 × 중점 − A\nB = ({m(2 * mx - x1)}, {m(2 * my - y1)})", "B = 2M − A")

def d2_para(r):
    A, B, C = [(r.randint(-3, 5), r.randint(-3, 5)) for _ in range(3)]
    D = (A[0] + C[0] - B[0], A[1] + C[1] - B[1])
    if len({A, B, C, D}) < 4: return None
    return fill(f"평행사변형 ABCD에서 A{pt(*A)}, B{pt(*B)}, C{pt(*C)}일 때 D = ({{{{1}}}}, {{{{2}}}})", [ans(D[0]), ans(D[1])],
                f"평행사변형의 두 대각선은 서로를 이등분 → AC의 중점 = BD의 중점\nD = A + C − B = ({m(D[0])}, {m(D[1])})", "대각선의 중점이 같습니다.")

def d2_missing(r):
    pts = [(r.randint(-4, 6), r.randint(-4, 6)) for _ in range(2)]; gx, gy = r.randint(-2, 4), r.randint(-2, 4)
    a = 3 * gx - pts[0][0] - pts[1][0]; b = 3 * gy - pts[0][1] - pts[1][1]
    return num(f"세 점 {pt(*pts[0])}, {pt(*pts[1])}, (a, b)로 이루어진 삼각형의 무게중심이 {pt(gx, gy)}일 때 a + b의 값은?", a + b,
               f"({m(pts[0][0])} + {par(pts[1][0])} + a)/3 = {m(gx)} → a = {m(a)}\n({m(pts[0][1])} + {par(pts[1][1])} + b)/3 = {m(gy)} → b = {m(b)}\na + b = {m(a + b)}", "무게중심 좌표 공식으로 각각 세우세요.")

L12 = [("수직선 위의 내분점", d2_line), ("평면 위의 내분점", d2_plane), ("무게중심", d2_cent), ("중점으로 끝점 구하기", d2_mid),
       ("평행사변형의 꼭짓점", d2_para), ("무게중심으로 꼭짓점", d2_missing)]

def d3_pt(r):
    a, x, y = nz(r, -4, 4), r.randint(-4, 4), r.randint(-6, 6)
    return fill(f"기울기가 {m(a)}이고 점 {pt(x, y)}를 지나는 직선은 y = {poly((a, 'x'))} + {{{{1}}}}", [ans(y - a * x)],
                f"y − {par(y)} = {m(a)}(x − {par(x)})\ny = {poly((a, 'x'))}{term(y - a * x)}\n빈칸: {m(y - a * x)}", "y − y₁ = m(x − x₁)")

def d3_two(r):
    a, b = nz(r, -4, 4), r.randint(-7, 7); x1, x2 = r.sample(range(-3, 5), 2)
    return fill(f"두 점 {pt(x1, a * x1 + b)}, {pt(x2, a * x2 + b)}를 지나는 직선은 y = {{{{1}}}}x + {{{{2}}}}", [ans(a), ans(b)],
                f"기울기 = ({m(a * x2 + b)} − {par(a * x1 + b)})/({m(x2)} − {par(x1)}) = {m(a)}\n한 점 대입: {m(a * x1 + b)} = {mul(a, x1)} + b → b = {m(b)}", "기울기 먼저, 그다음 y절편")

def d3_int(r):
    p, q = nz(r, -6, 6), nz(r, -6, 6)
    t = r.choice(["area", "form"])
    if t == "area":
        v = F(abs(p * q), 2)
        return num(f"직선 x/{par(p)} + y/{par(q)} = 1과 x축, y축으로 둘러싸인 삼각형의 넓이는?".replace("/(", "/(").replace("x/(", "x/(") , fs(v) if v.denominator == 1 else f"{float(v):g}",
                   f"x절편 {m(p)}, y절편 {m(q)}\n넓이 = |{m(p)}| × |{m(q)}| ÷ 2 = {float(v):g}", "절편형: x/a + y/b = 1", fmt="integer" if v.denominator == 1 else "decimal")
    g = gcd(abs(p), abs(q)); L = abs(p * q) // g
    A, B = L // p, L // q
    return fill(f"x절편이 {m(p)}, y절편이 {m(q)}인 직선은 {poly((A, 'x'), (B, 'y'))} = {{{{1}}}}", [ans(L)],
                f"x/{par(p)} + y/{par(q)} = 1의 양변에 {j(L, '를을')} 곱하면 {poly((A, 'x'), (B, 'y'))} = {L}", "절편형 방정식에서 분모를 없애세요.")

def d3_coef(r):
    a, b, c = nz(r, -6, 6), r.choice([1, 2, -1, -2, 3]), nz(r, -9, 9)
    ask = r.choice(["기울기", "y절편"])
    v = F(-a, b) if ask == "기울기" else F(-c, b)
    return num(f"직선 {poly((a, 'x'), (b, 'y'), (c, ''))} = 0의 {ask}는? (기약분수 또는 정수로)", v,
               f"y에 대해 풀면 {poly((b, 'y'))} = {poly((-a, 'x'), (-c, ''))}\ny = {sx(F(-a, b))} {'−' if F(-c, b) < 0 else '+'} {fs(abs(F(-c, b)))}\n{ask}: {fm(v)}", "y = mx + n 꼴로 바꾸세요.",
               fmt="fraction" if v.denominator > 1 else "integer")

def d3_col(r):
    a, b = nz(r, -3, 4), r.randint(-4, 4); x1, x2 = r.sample(range(-3, 4), 2); x3 = r.choice([z for z in range(-6, 8) if z not in (x1, x2)])
    return num(f"세 점 {pt(x1, a * x1 + b)}, {pt(x2, a * x2 + b)}, (k, {m(a * x3 + b)})가 한 직선 위에 있을 때 k의 값은?", x3,
               f"앞의 두 점의 기울기 {m(a)} → 직선 y = {lin(a, b)}\n{m(a * x3 + b)} = {lin(a, b).replace('x', 'k')} → k = {m(x3)}", "두 점으로 직선을 구해 대입하세요.")

L13 = [("기울기와 한 점", d3_pt), ("두 점을 지나는 직선", d3_two), ("절편으로 나타낸 직선", d3_int), ("일반형의 기울기·절편", d3_coef), ("세 점이 한 직선 위에", d3_col)]

def d4_par(r):
    a, b = nz(r, -5, 5), nz(r, -6, 6); x, y = r.randint(-3, 3), r.randint(-5, 5)
    t = r.choice(["par", "perp"])
    if t == "par":
        return fill(f"직선 y = {lin(a, b)}에 평행하고 점 {pt(x, y)}를 지나는 직선은 y = {poly((a, 'x'))} + {{{{1}}}}", [ans(y - a * x)],
                    f"평행 → 기울기 {m(a)}\ny − {par(y)} = {m(a)}(x − {par(x)}) → y절편 {m(y - a * x)}", "평행한 직선은 기울기가 같습니다.")
    s = F(-1, a)
    c = y - s * x
    if c.denominator != 1: return None
    return fill(f"점 {pt(x, y)}를 지나고 직선 y = {lin(a, b)}에 수직인 직선은 y = {sx(s)} + {{{{1}}}}", [ans(int(c))],
                f"수직 → 기울기의 곱이 −1 → 기울기 {fm(s)}\ny = {sx(s)} + n에 대입: {m(y)} = {fm(s * x)} + n → n = {m(int(c))}", "수직이면 기울기의 곱 = −1")

def d4_cond(r):
    p, q = nz(r, -4, 4), nz(r, -4, 4)
    t = r.choice(["par", "perp"])
    if t == "par":
        return num(f"두 직선 ax + {par(q)}y = 1, {par(p)}x + {par(q)}y = 5가 평행할 때 a의 값은?".replace("+ (", "+ (").replace("ax + (", "ax + ("), p,
                   f"평행 조건: a : {m(p)} = {m(q)} : {m(q)} (≠ 1 : 5)\n→ a = {m(p)}", "x, y의 계수 비가 같고 상수항의 비는 다를 때")
    a = F(-q * q, p) if False else None
    # ax + qy = 1 ⟂ px + q2 y = 3: a p + q q2 = 0
    q2 = nz(r, -3, 3); av = F(-q * q2, p)
    return num(f"두 직선 ax + {par(q)}y = 1, {par(p)}x + {par(q2)}y = 3이 수직일 때 a의 값은? (기약분수 또는 정수로)", av,
               f"수직 조건: a × {par(p)} + {par(q)} × {par(q2)} = 0\n{m(p)}a = {m(-q * q2)} → a = {fm(av)}", "a₁a₂ + b₁b₂ = 0", fmt="fraction" if av.denominator > 1 else "integer")

def d4_dist(r):
    a, b, c5 = r.choice([(3, 4, 5), (4, 3, 5), (5, 12, 13), (12, 5, 13), (6, 8, 10), (8, 6, 10)])
    x, y = r.randint(-4, 4), r.randint(-4, 4); d = r.randint(1, 4)
    sgn = r.choice([1, -1])
    c = sgn * d * c5 - a * x - b * y
    return num(f"점 {pt(x, y)}와 직선 {poly((a, 'x'), (b, 'y'), (c, ''))} = 0 사이의 거리는?", d,
               f"|ax₁ + by₁ + c|/√(a² + b²)\n= |{a}×{par(x)} + {b}×{par(y)}{term(c)}|/√({a}² + {b}²) = {abs(a * x + b * y + c)}/{c5} = {d}", "점과 직선 사이의 거리 공식")

def d4_pardist(r):
    a, b, c5 = r.choice([(3, 4, 5), (5, 12, 13), (6, 8, 10), (4, 3, 5)])
    c1 = r.randint(-10, 10); d = r.randint(1, 4); c2 = c1 + d * c5
    return num(f"평행한 두 직선 {poly((a, 'x'), (b, 'y'), (c1, ''))} = 0, {poly((a, 'x'), (b, 'y'), (c2, ''))} = 0 사이의 거리는?", d,
               f"|c₁ − c₂|/√(a² + b²) = |{m(c1)} − {par(c2)}|/{c5} = {d * c5}/{c5} = {d}", "평행선 사이의 거리 = |c₁ − c₂|/√(a² + b²)")

def d4_bis(r):
    x1, y1, x2, y2 = [r.randint(-4, 6) for _ in range(4)]
    if y1 == y2 or x1 == x2: return None
    s = F(-(x2 - x1), y2 - y1); mx, my = F(x1 + x2, 2), F(y1 + y2, 2)
    c = my - s * mx
    if s.denominator != 1 or c.denominator != 1: return None
    return fill(f"A{pt(x1, y1)}, B{pt(x2, y2)}의 수직이등분선은 y = {sx(s)} + {{{{1}}}}", [ans(int(c))],
                f"중점 ({fm(mx)}, {fm(my)}), AB의 기울기 {fm(F(y2 - y1, x2 - x1))} → 수직 기울기 {fm(s)}\ny = {sx(s)} + n에 중점 대입: n = {m(int(c))}", "중점을 지나고 AB에 수직")

def d4_area(r):
    x1, y1, x2, y2 = r.randint(1, 8), r.randint(-4, 6), r.randint(-4, 6), r.randint(1, 8)
    v = F(abs(x1 * y2 - x2 * y1), 2)
    if v == 0: return None
    return num(f"세 점 O(0, 0), A{pt(x1, y1)}, B{pt(x2, y2)}를 꼭짓점으로 하는 삼각형의 넓이는?", fs(v) if v.denominator == 1 else f"{float(v):g}",
               f"넓이 = |x₁y₂ − x₂y₁|/2 = |{x1}×{par(y2)} − {par(x2)}×{par(y1)}|/2 = {abs(x1 * y2 - x2 * y1)}/2 = {float(v):g}", "신발끈 공식(원점 포함)",
               fmt="integer" if v.denominator == 1 else "decimal")

L14 = [("평행·수직인 직선", d4_par), ("평행·수직 조건", d4_cond), ("점과 직선 사이의 거리", d4_dist), ("평행선 사이의 거리", d4_pardist),
       ("수직이등분선", d4_bis), ("좌표로 삼각형 넓이", d4_area)]

# ================= ch02 원과 도형의 이동 =================
def circ(a, b, r2): return f"{sq('x', a) if a else 'x²'} + {sq('y', b).replace('x', 'y') if b else 'y²'} = {r2}"
def e1_std(r):
    a, b, k = r.randint(-5, 5), r.randint(-5, 5), r.randint(1, 7)
    return fill(f"중심이 {pt(a, b)}이고 반지름이 {k}인 원은 {circ(a, b, '{{1}}')}", [str(k * k)],
                f"(x − a)² + (y − b)² = r²에 a = {m(a)}, b = {m(b)}, r = {k}\nr² = {k * k}", "우변은 반지름의 제곱")

def e1_gen(r):
    a, b, k = nz(r, -5, 5), r.randint(-5, 5), r.randint(1, 6)
    c = a * a + b * b - k * k
    ge = poly((1, 'x²'), (1, 'y²'), (-2 * a, 'x'), (-2 * b, 'y'), (c, ''))
    ask = r.choice(["center", "radius"])
    ex = f"완전제곱식으로: (x{term(-a)})² + (y{term(-b)})² = {k * k}"
    if ask == "center":
        return fill(f"원 {ge} = 0의 중심은 ({{{{1}}}}, {{{{2}}}})", [ans(a), ans(b)], ex + f"\n중심 {pt(a, b)}", "x끼리, y끼리 완전제곱식을 만드세요.")
    return num(f"원 {ge} = 0의 반지름은?", k, ex + f"\n반지름 √{k * k} = {k}", "x끼리, y끼리 완전제곱식을 만드세요.")

def e1_diam(r):
    x1, y1 = r.randint(-5, 5), r.randint(-5, 5); dx, dy = 2 * r.randint(-3, 3), 2 * r.randint(-3, 3)
    if dx == dy == 0: return None
    cx, cy = x1 + dx // 2, y1 + dy // 2; R2 = (dx * dx + dy * dy) // 4
    return fill(f"두 점 {pt(x1, y1)}, {pt(x1 + dx, y1 + dy)}를 지름의 양 끝으로 하는 원은 {circ(cx, cy, '{{1}}')}", [str(R2)],
                f"중심 = 중점 {pt(cx, cy)}\n반지름² = (중심에서 한 끝까지 거리)² = {(dx // 2) ** 2} + {(dy // 2) ** 2} = {R2}", "중점이 중심, 지름의 절반이 반지름")

def e1_tan(r):
    a, b = nz(r, -6, 6), nz(r, -6, 6)
    ax = r.choice(["x축", "y축"])
    return num(f"중심이 {pt(a, b)}이고 {ax}에 접하는 원의 반지름은?", abs(b) if ax == "x축" else abs(a),
               f"{ax}에 접하면 반지름 = 중심에서 {ax}까지의 거리 = |{'y' if ax == 'x축' else 'x'}좌표|\n= |{m(b if ax == 'x축' else a)}| = {abs(b) if ax == 'x축' else abs(a)}", "중심과 축 사이의 거리")

def e1_cond(r):
    a, b = nz(r, -5, 5), r.randint(-4, 4)
    return num(f"x² + y²{term(-2 * a, 'x')}{term(-2 * b, 'y')} + k = 0이 원이 되는 정수 k의 최댓값은?", a * a + b * b - 1,
               f"(x{term(-a)})² + (y{term(-b)})² = {a * a + b * b} − k\n원이 되려면 우변 > 0: k < {a * a + b * b}\n정수 k의 최댓값 {a * a + b * b - 1}", "반지름의 제곱이 양수여야 합니다.")

def e1_far(r):
    k = r.randint(1, 6); a, b, c = r.choice(TRI[:4]); d = c
    if d <= k: return None
    t = r.choice(["min", "max"])
    return num(f"원 x² + y² = {k * k} 위의 점과 점 {pt(a, b)} 사이 거리의 {'최솟값' if t == 'min' else '최댓값'}은?", d - k if t == "min" else d + k,
               f"중심(원점)과 점 사이 거리 √({a}² + {b}²) = {d}\n{'최솟값 = ' + str(d) + ' − ' + str(k) + ' = ' + str(d - k) if t == 'min' else '최댓값 = ' + str(d) + ' + ' + str(k) + ' = ' + str(d + k)}",
               "중심까지의 거리 ± 반지름")

L21 = [("원의 방정식", e1_std), ("일반형에서 중심·반지름", e1_gen), ("지름의 양 끝", e1_diam), ("축에 접하는 원", e1_tan), ("원이 될 조건", e1_cond), ("원 위의 점까지 거리", e1_far)]

def e2_count(r):
    k = r.randint(1, 6); a, b, c = r.choice([(3, 4, 5), (4, 3, 5), (1, 1, None), (1, -1, None), (5, 12, 13)])
    dd = r.randint(1, 3 * k)
    if c:
        cst = r.choice([-1, 1]) * dd * c // max(1, 1)
        # 거리 = |cst|/c
        dist = F(abs(cst), c)
    else:
        return None
    v = 2 if dist < k else 1 if dist == k else 0
    return num(f"원 x² + y² = {k * k}와 직선 {poly((a, 'x'), (b, 'y'))} = {m(cst)}의 교점은 몇 개일까요?", v,
               f"중심(원점)과 직선 사이 거리 d = |{m(cst)}|/√({a}² + {b}²) = {fm(dist)}\n반지름 {k}와 비교: " + ("d < r → 2개" if v == 2 else "d = r → 접함, 1개" if v == 1 else "d > r → 0개"),
               "중심과 직선 사이 거리를 반지름과 비교하세요.")

def e2_tangent(r):
    a, b, c = r.choice(TRI[:3]); sx, sy = r.choice([1, -1]), r.choice([1, -1])
    if r.random() < .5: a, b = b, a
    x, y = sx * a, sy * b
    return fill(f"원 x² + y² = {c * c} 위의 점 {pt(x, y)}에서의 접선은 {poly((x, 'x'), (y, 'y'))} = {{{{1}}}}", [str(c * c)],
                f"원 x² + y² = r² 위의 점 (x₁, y₁)에서의 접선: x₁x + y₁y = r²\n→ {poly((x, 'x'), (y, 'y'))} = {c * c}", "x₁x + y₁y = r²")

def e2_chord(r):
    a, b, c = r.choice(TRI[:4]); t = r.choice(["x", "y"])
    return num(f"원 x² + y² = {c * c}와 직선 {t} = {a}가 만나 생기는 현의 길이는?", 2 * b,
               f"중심에서 직선까지 거리 {a}, 반지름 {c}\n현의 절반 = √({c}² − {a}²) = {b}\n현의 길이 = {2 * b}", "반지름, 거리, 현의 절반이 직각삼각형")

def e2_tlen(r):
    a, b, c = r.choice(TRI)
    if r.random() < .5: a, b = b, a
    return num(f"점 ({c}, 0)에서 원 x² + y² = {a * a}에 그은 접선의 길이는?", b,
               f"중심–접점–점이 직각삼각형: 접선² = {c}² − {a}² = {b * b}\n접선의 길이 {b}", "접선은 반지름과 수직")

def e2_far(r):
    k = r.randint(1, 4); a, b, c = r.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13)]); d = r.randint(k + 1, k + 6)
    t = r.choice(["max", "min"])
    return num(f"원 x² + y² = {k * k} 위의 점과 직선 {a}x + {b}y = {d * c} 사이 거리의 {'최댓값' if t == 'max' else '최솟값'}은?", d + k if t == "max" else d - k,
               f"원점과 직선 사이 거리 {d * c}/{c} = {d}\n{'최댓값 = ' + str(d) + ' + ' + str(k) if t == 'max' else '최솟값 = ' + str(d) + ' − ' + str(k)} = {d + k if t == 'max' else d - k}", "중심까지 거리 ± 반지름")

def e2_slope(r):
    m_, t = r.choice([1, 2, 3, -1, -2]), r.randint(1, 3)
    k2 = t * t * (m_ * m_ + 1); v2 = k2 * (m_ * m_ + 1)
    return num(f"원 x² + y² = {k2}에 접하고 기울기가 {m_}인 직선 중 y절편이 양수인 것의 y절편은?", isqrt(v2),
               f"y = {m_}x + n이 접하면 원점과 직선 사이 거리 = 반지름\n|n|/√({m_}² + 1) = √{k2} → n² = {v2} → n = {isqrt(v2)}", "거리 = 반지름")

L22 = [("교점의 개수", e2_count), ("원 위의 점에서의 접선", e2_tangent), ("현의 길이", e2_chord), ("접선의 길이", e2_tlen), ("원과 직선 사이 거리", e2_far), ("기울기가 주어진 접선", e2_slope)]

def e3_pt(r):
    x, y, p, q = [nz(r, -5, 5) for _ in range(4)]
    return fill(f"점 {pt(x, y)}를 x축 방향으로 {m(p)}, y축 방향으로 {m(q)}만큼 평행이동한 점은 ({{{{1}}}}, {{{{2}}}})", [ans(x + p), ans(y + q)],
                f"(x, y) → (x + {par(p)}, y + {par(q)})\n= ({m(x + p)}, {m(y + q)})", "좌표에 이동한 만큼 더하세요.")

def e3_back(r):
    a, b, p, q = [nz(r, -5, 5) for _ in range(4)]
    return num(f"점 (a, b)를 x축 방향으로 {m(p)}, y축 방향으로 {m(q)}만큼 옮긴 점이 {pt(a + p, b + q)}일 때 a + b의 값은?", a + b,
               f"a + {par(p)} = {m(a + p)} → a = {m(a)}\nb + {par(q)} = {m(b + q)} → b = {m(b)}\na + b = {m(a + b)}", "거꾸로 빼세요.")

def e3_curve(r):
    p, q = nz(r, -4, 4), nz(r, -4, 4)
    t = r.choice(["circle", "line", "parab"])
    if t == "circle":
        k = r.randint(1, 4)
        return fill(f"x² + y² = {k * k}를 x축 방향으로 {m(p)}, y축 방향으로 {m(q)}만큼 평행이동하면 (x − {{{{1}}}})² + (y − {{{{2}}}})² = {k * k}", [ans(p), ans(q)],
                    f"x 대신 x − {par(p)}, y 대신 y − {par(q)}\n중심 (0, 0) → {pt(p, q)}", "도형의 평행이동: x → x − p, y → y − q")
    if t == "line":
        a, b = nz(r, -3, 3), r.randint(-5, 5)
        v = b - a * p + q
        return num(f"직선 y = {lin(a, b)}를 x축 방향으로 {m(p)}, y축 방향으로 {m(q)}만큼 평행이동한 직선의 y절편은?", v,
                   f"y − {par(q)} = {m(a)}(x − {par(p)}){term(b)}\ny = {lin(a, v)}\ny절편 {m(v)}", "x → x − p, y → y − q를 대입")
    return num(f"y = x²을 x축 방향으로 {m(p)}, y축 방향으로 {m(q)}만큼 평행이동한 그래프의 y절편은?", p * p + q,
               f"y = (x{term(-p)})²{term(q)}\nx = 0 대입: {p * p}{term(q)} = {m(p * p + q)}", "꼭짓점이 (p, q)로 옮겨집니다.")

def e3_find(r):
    a, b, c, d = [r.randint(-4, 5) for _ in range(4)]
    if (a, b) == (c, d): return None
    ask = r.choice(["x", "y"])
    return num(f"원 (x{term(-a)})² + (y{term(-b)})² = 4를 평행이동했더니 (x{term(-c)})² + (y{term(-d)})² = 4가 되었습니다. {ask}축 방향으로 얼마만큼 옮겼을까요?".replace("(x)²", "x²").replace("(y)²", "y²"),
               c - a if ask == "x" else d - b,
               f"중심이 {pt(a, b)} → {pt(c, d)}\n{ask}축 방향: {m(c if ask == 'x' else d)} − {par(a if ask == 'x' else b)} = {m(c - a if ask == 'x' else d - b)}", "중심의 이동을 보세요.")

L23 = [("점의 평행이동", e3_pt), ("원래 점 찾기", e3_back), ("도형의 평행이동", e3_curve), ("이동량 구하기", e3_find)]

def e4_pt(r):
    x, y = nz(r, -6, 6), nz(r, -6, 6)
    t = r.choice(["x축", "y축", "원점", "y = x", "y = −x"])
    nx, ny = {"x축": (x, -y), "y축": (-x, y), "원점": (-x, -y), "y = x": (y, x), "y = −x": (-y, -x)}[t]
    rule = {"x축": "y좌표의 부호", "y축": "x좌표의 부호", "원점": "두 좌표의 부호", "y = x": "x, y를 서로 바꿈", "y = −x": "x, y를 바꾸고 부호도 모두 바꿈"}[t]
    nm = t if "=" not in t else f"직선 {t}"
    return fill(f"점 {pt(x, y)}를 {nm}에 대하여 대칭이동한 점은 ({{{{1}}}}, {{{{2}}}})", [ans(nx), ans(ny)],
                f"{nm}에 대한 대칭이동: {rule}{'를 바꿈' if '부호' in rule and '바꿈' not in rule else ''}\n{pt(x, y)} → {pt(nx, ny)}", "대칭이동의 규칙을 떠올리세요.")

def e4_line(r):
    a, b = nz(r, -4, 4), nz(r, -6, 6)
    t = r.choice(["x축", "y축", "원점"])
    na, nb = {"x축": (-a, -b), "y축": (-a, b), "원점": (a, -b)}[t]
    return fill(f"직선 y = {lin(a, b)}를 {t}에 대하여 대칭이동한 직선은 y = {{{{1}}}}x + {{{{2}}}}", [ans(na), ans(nb)],
                {"x축": f"y 대신 −y: −y = {lin(a, b)} → y = {lin(na, nb)}", "y축": f"x 대신 −x: y = {lin(-a, b).replace('x', '(−x)') if False else lin(a, b).replace('x', '(−x)')} → y = {lin(na, nb)}",
                 "원점": f"x 대신 −x, y 대신 −y: −y = {lin(a, b).replace('x', '(−x)')} → y = {lin(na, nb)}"}[t], "x축 대칭: y → −y, y축 대칭: x → −x")

def e4_inv(r):
    a, b = r.choice([2, 3, 4, -2, -3]), nz(r, -6, 6)
    return fill(f"직선 y = {lin(a, b)}를 직선 y = x에 대하여 대칭이동하면 y = (x + {{{{1}}}})/{a}".replace(f"/{a}", f"/{par(a)}"), [ans(-b)],
                f"x와 y를 바꿉니다: x = {lin(a, b).replace('x', 'y')}\ny에 대해 풀면 y = (x{term(-b)})/{par(a)}\n빈칸: {m(-b)}", "y = x 대칭: x와 y를 바꿉니다.")

def e4_point(r):
    x, y, cx, cy = [r.randint(-4, 5) for _ in range(4)]
    if (x, y) == (cx, cy): return None
    return fill(f"점 {pt(x, y)}를 점 {pt(cx, cy)}에 대하여 대칭이동한 점은 ({{{{1}}}}, {{{{2}}}})", [ans(2 * cx - x), ans(2 * cy - y)],
                f"{pt(cx, cy)}가 두 점의 중점이므로 구하는 점 = 2×{pt(cx, cy)} − {pt(x, y)} = {pt(2 * cx - x, 2 * cy - y)}", "대칭의 중심이 중점")

def e4_min(r):
    x1, y1, x2, y2 = r.randint(-2, 3), r.randint(1, 5), r.randint(4, 9), r.randint(1, 5)
    dx, dy = x2 - x1, y1 + y2; s = dx * dx + dy * dy
    k = 1
    for f_ in range(isqrt(s), 0, -1):
        if s % (f_ * f_) == 0: k = f_; break
    rest = s // (k * k)
    if rest == 1:
        return num(f"A{pt(x1, y1)}, B{pt(x2, y2)}이고 P가 x축 위를 움직일 때 AP + PB의 최솟값은?", k,
                   f"B를 x축에 대해 대칭이동: B'{pt(x2, -y2)}\n최솟값 = AB' = √({dx}² + {dy}²) = {k}", "한 점을 x축에 대해 대칭이동")
    return fill(f"A{pt(x1, y1)}, B{pt(x2, y2)}이고 P가 x축 위를 움직일 때 AP + PB의 최솟값은 {{{{1}}}}√{rest}" if k > 1 else
                f"A{pt(x1, y1)}, B{pt(x2, y2)}이고 P가 x축 위를 움직일 때 AP + PB의 최솟값은 √{{{{1}}}}", [str(k) if k > 1 else str(rest)],
                f"B를 x축에 대해 대칭이동: B'{pt(x2, -y2)}\n최솟값 = AB' = √({dx}² + {dy}²) = √{s}" + (f" = {k}√{rest}" if k > 1 else ""), "한 점을 x축에 대해 대칭이동")

L24 = [("점의 대칭이동", e4_pt), ("직선의 대칭이동", e4_line), ("y = x 대칭(역함수)", e4_inv), ("점에 대한 대칭", e4_point), ("대칭으로 최솟값", e4_min)]

# ================= ch03 함수 =================
def f1_count(r):
    a, b = r.randint(2, 4), r.randint(2, 4)
    t = r.choice(["all", "inj", "bij"])
    if t == "all":
        return num(f"원소가 {a}개인 집합 X에서 원소가 {b}개인 집합 Y로의 함수는 모두 몇 개일까요?", b ** a,
                   f"X의 각 원소마다 Y의 원소 {b}개 중 하나를 대응\n{b}{sup(a)} = {b ** a}", "X의 원소마다 선택지가 있습니다.")
    if t == "inj":
        if a > b: return None
        return num(f"원소가 {a}개인 집합 X에서 원소가 {b}개인 집합 Y로의 일대일함수는 몇 개일까요?", perm(b, a),
                   f"서로 다른 원소에 서로 다른 값 → {b}P{a} = {perm(b, a)}", "이미 쓴 값은 다시 쓸 수 없습니다.")
    from math import factorial
    return num(f"원소가 {a}개인 집합 X에서 X로의 일대일대응은 몇 개일까요?", factorial(a),
               f"{a}개를 일렬로 대응시키는 방법 {a}! = {factorial(a)}", "순열과 같습니다.")

def f1_range(r):
    D = sorted(r.sample(range(-3, 4), r.randint(3, 5)))
    fs_ = [("x²", lambda v: v * v), ("2x + 1", lambda v: 2 * v + 1), ("|x|", abs), ("x² − 1", lambda v: v * v - 1)]
    nm, f = r.choice(fs_)
    Rg = sorted({f(v) for v in D})
    t = r.choice(["n", "sum"])
    return num(f"정의역이 {{{', '.join(m(v) for v in D)}}}인 함수 f(x) = {nm}의 치역의 원소{'는 몇 개일까요?' if t == 'n' else '의 합은?'}", len(Rg) if t == "n" else sum(Rg),
               f"함숫값: {', '.join(m(f(v)) for v in D)}\n치역(중복 제거): {{{', '.join(m(v) for v in Rg)}}}\n{'원소 ' + str(len(Rg)) + '개' if t == 'n' else '합 ' + m(sum(Rg))}",
               "같은 함숫값은 한 번만 셉니다.")

def f1_ab(r):
    a, b = nz(r, -5, 5), r.randint(-6, 6); p, q = r.sample(range(-3, 4), 2)
    ask = r.choice(["a", "b"])
    return num(f"f(x) = ax + b에서 f({m(p)}) = {m(a * p + b)}, f({m(q)}) = {m(a * q + b)}일 때 {ask}의 값은?", a if ask == "a" else b,
               f"{poly((p, 'a'), (1, 'b'))} = {m(a * p + b)}, {poly((q, 'a'), (1, 'b'))} = {m(a * q + b)}\n빼면 {poly((p - q, 'a'))} = {m(a * (p - q))} → a = {m(a)}, b = {m(b)}", "두 식을 연립하세요.")

def f1_sub(r):
    a, b, c = nz(r, -3, 4), r.randint(-5, 5), nz(r, -3, 3)
    k = r.randint(-3, 5)
    # f(x + c) = a x + b → f(t) = a(t − c) + b
    v = a * (k - c) + b
    return num(f"f(x{term(c)}) = {lin(a, b)}일 때 f({m(k)})의 값은?", v,
               f"x{term(c)} = {m(k)}가 되려면 x = {m(k - c)}\nf({m(k)}) = {mul(a, k - c)}{term(b)} = {m(v)}", "괄호 안이 원하는 값이 되는 x를 찾으세요.")

def f1_root(r):
    c = r.randint(-5, 6)
    return num(f"함수 f(x) = √(x{term(-c)})의 정의역에서 가장 작은 x는?", c,
               f"근호 안이 0 이상: x{term(-c)} ≥ 0 → x ≥ {m(c)}\n가장 작은 x = {m(c)}", "√ 안은 0 이상")

L31 = [("함수의 개수", f1_count), ("치역", f1_range), ("일차함수의 결정", f1_ab), ("f(x + c) 꼴", f1_sub), ("정의역", f1_root)]

def f2_abs(r):
    a, b = r.randint(-4, 5), r.randint(-5, 5)
    t = r.choice(["min", "two"])
    if t == "min":
        return num(f"y = |x{term(-a)}|{term(b)}의 최솟값은?", b,
                   f"|x{term(-a)}| ≥ 0이고 x = {m(a)}일 때 0\n최솟값 = 0{term(b)} = {m(b)}", "절댓값은 0이 최소")
    c = a + r.randint(1, 7)
    return num(f"y = |x{term(-a)}| + |x{term(-c)}|의 최솟값은?", c - a,
               f"{m(a)} ≤ x ≤ {m(c)}일 때 두 거리의 합이 일정 = {c - a}\n최솟값 {c - a}", "두 점 사이에 있을 때 최소")

def f2_piece(r):
    a, b, c = nz(r, -3, 3), r.randint(-4, 4), r.randint(-4, 4)
    p, q = r.randint(-5, -1), r.randint(0, 4)
    v = (a * p + b) + (q * q + c)
    return num(f"f(x) = {lin(a, b)} (x < 0), x²{term(c)} (x ≥ 0)일 때 f({m(p)}) + f({q})의 값은?", v,
               f"{m(p)} < 0 → f({m(p)}) = {mul(a, p)}{term(b)} = {m(a * p + b)}\n{q} ≥ 0 → f({q}) = {q}²{term(c)} = {m(q * q + c)}\n합 {m(v)}", "x의 범위에 맞는 식을 쓰세요.")

def f2_cont(r):
    k, a, b = r.randint(-3, 3), nz(r, -3, 3), r.randint(-4, 4)
    c2 = nz(r, -3, 3)
    av = a * k + b - c2 * k
    return num(f"f(x) = {lin(a, b)} (x ≤ {m(k)}), {poly((c2, 'x'))} + a (x > {m(k)})의 그래프가 끊기지 않을 때 a의 값은?", av,
               f"x = {m(k)}에서 두 식의 값이 같아야 합니다.\n{mul(a, k)}{term(b)} = {mul(c2, k)} + a\n{m(a * k + b)} = {m(c2 * k)} + a → a = {m(av)}", "경계에서 두 식의 값을 같게")

def f2_vmin(r):
    a, b = nz(r, -4, 4), r.randint(-6, 6)
    c = a * a + b
    return num(f"f(x) = {poly((1, 'x²'), (-2 * a, 'x'), (c, ''))}의 최솟값은?", b,
               f"완전제곱식: (x{term(-a)})²{term(b)}\nx = {m(a)}일 때 최솟값 {m(b)}", "완전제곱식으로 바꾸세요.")

def f2_cnt(r):
    a, k = r.randint(-3, 3), r.randint(-2, 4)
    v = 2 if k > 0 else 1 if k == 0 else 0
    return num(f"y = |x{term(-a)}|의 그래프와 직선 y = {m(k)}의 교점은 몇 개일까요?", v,
               f"y = |x{term(-a)}|는 꼭짓점 ({m(a)}, 0)인 V자 모양(최솟값 0)\ny = {m(k)}" + (" > 0 → 2개" if k > 0 else " = 0 → 꼭짓점에서 1개" if k == 0 else " < 0 → 0개"), "V자 그래프를 그려 보세요.")

def f2_pass(r):
    a, b, x = nz(r, -4, 5), r.randint(-6, 6), nz(r, -5, 5)
    return num(f"f(x) = {lin(a, b)}의 그래프가 점 (k, {m(a * x + b)})를 지날 때 k의 값은?", x,
               f"{m(a * x + b)} = {lin(a, b).replace('x', 'k')}\n{poly((a, 'k'))} = {m(a * x)}" + (f" → k = {m(x)}" if a != 1 else ""), "점의 좌표를 대입하세요.")

L32 = [("절댓값 함수의 최솟값", f2_abs), ("구간별로 정의된 함수", f2_piece), ("끊기지 않을 조건", f2_cont), ("이차함수의 최솟값", f2_vmin), ("교점의 개수", f2_cnt), ("그래프 위의 점", f2_pass)]

def f3_val(r):
    a, b, c, d = nz(r, -3, 4), r.randint(-4, 4), nz(r, -3, 3), r.randint(-4, 4); k = r.randint(-3, 4)
    which = r.choice(["g∘f", "f∘g"])
    f = lambda x: a * x + b; g = lambda x: c * x + d
    v = g(f(k)) if which == "g∘f" else f(g(k))
    inner = f(k) if which == "g∘f" else g(k)
    return num(f"f(x) = {lin(a, b)}, g(x) = {lin(c, d)}일 때 ({which})({m(k)})의 값은?", v,
               f"({which})({m(k)}) = {which[0]}({which[2]}({m(k)}))\n{which[2]}({m(k)}) = {m(inner)}\n{which[0]}({m(inner)}) = {m(v)}", "안쪽 함수부터 계산하세요.")

def f3_expr(r):
    a = nz(r, -4, 4)
    which = r.choice(["g∘f", "f∘g"])
    if which == "g∘f":
        return fill(f"f(x) = x{term(a)}, g(x) = x²일 때 (g∘f)(x) = x² + {{{{1}}}}x + {{{{2}}}}", [ans(2 * a), ans(a * a)],
                    f"g(f(x)) = (x{term(a)})² = x²{term(2 * a, 'x')} + {a * a}", "f(x)를 g의 x 자리에 넣으세요.")
    return fill(f"f(x) = x{term(a)}, g(x) = x²일 때 (f∘g)(x) = x² + {{{{1}}}}", [ans(a)],
                f"f(g(x)) = g(x){term(a)} = x²{term(a)}", "g(x)를 f의 x 자리에 넣으세요.")

def f3_find(r):
    a, b = r.choice([2, 3, -2]), nz(r, -4, 4); p, q = nz(r, -3, 3), r.randint(-5, 5)
    # f = ax + b, g∘f = p(ax + b) + q → g(x) = px + q
    return fill(f"f(x) = {lin(a, b)}, (g∘f)(x) = {lin(p * a, p * b + q)}이고 g가 일차함수일 때 g(x) = {poly((p, 'x'))} + {{{{1}}}}", [ans(q)],
                f"g(x) = mx + n이면 g(f(x)) = m({lin(a, b)}) + n = {poly((a, 'm'))}x + {m(b)}m + n\nx의 계수: {m(a)}m = {m(p * a)} → m = {m(p)}\n상수항: {mul(b, p)} + n = {m(p * b + q)} → n = {m(q)}",
                "g를 일차식으로 놓고 계수를 비교하세요.")

def f3_iter(r):
    t = r.choice(["add", "flip", "neg"])
    n, x0 = r.randint(5, 30), r.randint(-3, 5)
    if t == "add":
        c = nz(r, -3, 4)
        return num(f"f(x) = x{term(c)}일 때 f를 {n}번 합성한 함수에 {m(x0)}을 넣은 값은?".replace(f"{m(x0)}을", j(x0, '를을', m(x0))), x0 + n * c,
                   f"한 번 합성할 때마다 {m(c)}씩 더해집니다.\n{m(x0)} + {n}×{par(c)} = {m(x0 + n * c)}", "규칙을 찾으세요.")
    if t == "flip":
        k = r.randint(1, 6)
        v = x0 if n % 2 == 0 else k - x0
        return num(f"f(x) = {k} − x일 때 f를 {n}번 합성한 함수에 {m(x0)}을 넣은 값은?".replace(f"{m(x0)}을", j(x0, '를을', m(x0))), v,
                   f"f(f(x)) = {k} − ({k} − x) = x → 두 번 합성하면 제자리\n{n}은 {'짝수 → x' if n % 2 == 0 else '홀수 → f(x)'} = {m(v)}", "f∘f를 먼저 계산하세요.")
    a, b = r.choice([2, 3]), r.randint(-3, 3)
    v = x0
    for _ in range(2): v = a * v + b
    return num(f"f(x) = {lin(a, b)}일 때 (f∘f)({m(x0)})의 값은?", v,
               f"f({m(x0)}) = {m(a * x0 + b)}\nf({m(a * x0 + b)}) = {m(v)}", "두 번 차례로 넣으세요.")

def f3_param(r):
    a, b = nz(r, -3, 3), r.randint(-4, 4); k = r.randint(-3, 3); c = r.randint(-5, 5)
    inner = a * 1 + b
    # g(x) = x² + c; (g∘f)(1) = inner² + c
    return num(f"f(x) = {lin(a, b)}, g(x) = x² + k이고 (g∘f)(1) = {inner * inner + c}일 때 k의 값은?", c,
               f"f(1) = {m(inner)}\ng({m(inner)}) = {inner * inner} + k = {inner * inner + c} → k = {m(c)}", "f(1)부터 계산하세요.")

L33 = [("합성함수의 값", f3_val), ("합성함수의 식", f3_expr), ("합성에서 함수 구하기", f3_find), ("반복 합성", f3_iter), ("합성함수와 미정계수", f3_param)]

def f4_val(r):
    a, b = r.choice([2, 3, -2, -3, 4, 5]), r.randint(-6, 6); x = r.randint(-4, 5)
    return num(f"f(x) = {lin(a, b)}일 때 f⁻¹({m(a * x + b)})의 값은?", x,
               f"f⁻¹({m(a * x + b)}) = k ⇔ f(k) = {m(a * x + b)}\n{lin(a, b).replace('x', 'k')} = {m(a * x + b)} → k = {m(x)}", "f(k) = 값이 되는 k를 찾으세요.")

def f4_expr(r):
    a, b = r.choice([2, 3, 4, 5]), nz(r, -5, 5)
    c = F(-b, a)
    if c.denominator != 1: return None
    return fill(f"f(x) = {lin(a, b)}일 때 f⁻¹(x) = x/{a} + {{{{1}}}}", [ans(int(c))],
                f"y = {lin(a, b)}를 x에 대해 풀면 x = (y{term(-b)})/{a}\nx와 y를 바꾸면 y = x/{a}{term(int(c))}", "x에 대해 풀고 x, y를 바꾸세요.")

def f4_fix(r):
    a, b = r.choice([2, 3, -2, -1, 4]), r.randint(-6, 6)
    if a == 1: return None
    x = F(-b, a - 1)
    return num(f"f(x) = {lin(a, b)}의 그래프와 그 역함수의 그래프가 직선 y = x 위에서 만나는 점의 x좌표는? (기약분수 또는 정수로)", x,
               f"y = x 위의 교점: f(x) = x\n{lin(a, b)} = x → {poly((a - 1, 'x'))} = {m(-b)} → x = {fm(x)}", "f(x) = x를 푸세요.", fmt="fraction" if x.denominator > 1 else "integer")

def f4_comp(r):
    a, b, c = r.choice([2, 3]), r.randint(-4, 4), r.choice([2, 3, 4])
    k = r.randint(-3, 4)
    # (f⁻¹∘g)(k) where f = x + b, g = c x
    v = c * k - b
    return num(f"f(x) = x{term(b)}, g(x) = {c}x일 때 (f⁻¹∘g)({m(k)})의 값은?", v,
               f"g({m(k)}) = {m(c * k)}\nf⁻¹({m(c * k)}) = t ⇔ t{term(b)} = {m(c * k)} → t = {m(v)}", "g부터 계산한 뒤 역함수를 적용하세요.")

def f4_ab(r):
    a, b = r.choice([2, 3, -2, 4]), r.randint(-5, 5); p, q = r.sample(range(-3, 4), 2)
    return num(f"f(x) = ax + b에서 f⁻¹({m(a * p + b)}) = {m(p)}, f({m(q)}) = {m(a * q + b)}일 때 a + b의 값은?", a + b,
               f"f⁻¹({m(a * p + b)}) = {m(p)} ⇔ f({m(p)}) = {m(a * p + b)}\n{poly((p, 'a'), (1, 'b'))} = {m(a * p + b)}, {poly((q, 'a'), (1, 'b'))} = {m(a * q + b)}\n연립하면 a = {m(a)}, b = {m(b)} → a + b = {m(a + b)}", "역함수 조건을 f의 값으로 바꾸세요.")

def f4_piece(r):
    a, b = r.choice([2, 3]), r.randint(1, 3); y = r.randint(b + 1, 12)
    x = F(y - b, a)
    return num(f"f(x) = x + {b} (x < 0), {a}x + {b} (x ≥ 0)일 때 f⁻¹({y})의 값은? (기약분수 또는 정수로)", x,
               f"x < 0이면 f(x) < {b}, x ≥ 0이면 f(x) ≥ {b}\n{y} ≥ {b}이므로 {a}x + {b} = {y} → x = {fm(x)}", "값의 범위로 어느 식인지 정하세요.", fmt="fraction" if x.denominator > 1 else "integer")

L34 = [("역함수의 값", f4_val), ("역함수의 식", f4_expr), ("y = x 위의 교점", f4_fix), ("합성과 역함수", f4_comp), ("역함수 조건", f4_ab), ("구간별 함수의 역함수", f4_piece)]

ALL = {"ch01": [L11, L12, L13, L14], "ch02": [L21, L22, L23, L24], "ch03": [L31, L32, L33, L34]}

if __name__ == "__main__":
    tot = 0
    for ch, Ls in ALL.items():
        for i, T in enumerate(Ls, 1):
            per = 6 if len(T) >= 7 else 8 if len(T) >= 5 else 10 if len(T) >= 4 else 14
            n = write("c2", ch, f"l0{i}", T, per=per); tot += n; print(ch, i, len(T), n)
    print("total", tot)
