"""코스 0 · 챕터 4 일차함수 — 연습 문제 은행"""
from core import *

def nz(r, a, b):
    while True:
        x = r.randint(a, b)
        if x: return x

def pt(x, y): return f"({m(x)}, {m(y)})"
QN = {1: "1", 2: "2", 3: "3", 4: "4"}
def quad(x, y): return 1 if x > 0 and y > 0 else 2 if x < 0 and y > 0 else 3 if x < 0 and y < 0 else 4

# ---------------- l01 좌표와 그래프 ----------------
def l01_quad(r):
    x, y = nz(r, -9, 9), nz(r, -9, 9)
    q = quad(x, y)
    return fill(f"점 {pt(x, y)}{'은' if True else ''} 제{{{{1}}}}사분면 위의 점입니다.", [[str(q)]],
                f"x좌표 {m(x)}{'는' if not bat(x) else '은'} {'양수' if x > 0 else '음수'}, y좌표 {m(y)}{'는' if not bat(y) else '은'} {'양수' if y > 0 else '음수'}입니다.\n"
                f"(+, +) 제1, (−, +) 제2, (−, −) 제3, (+, −) 제4사분면\n따라서 제{q}사분면",
                "x좌표와 y좌표의 부호를 확인하세요.")

def l01_axis(r):
    x, y = nz(r, -9, 9), nz(r, -9, 9)
    ax = r.choice(["x축", "y축"])
    v = abs(y) if ax == "x축" else abs(x)
    return num(f"점 {pt(x, y)}에서 {ax}까지의 거리는?", v,
               f"{ax}까지의 거리는 {'y' if ax == 'x축' else 'x'}좌표의 절댓값입니다.\n|{m(y if ax == 'x축' else x)}| = {v}",
               f"{ax}에 수직으로 내린 길이를 생각하세요.")

def l01_dist(r):
    a, b, c = nz(r, -6, 6), nz(r, -7, 7), nz(r, -7, 7)
    if b == c: return None
    if r.random() < .5:
        return num(f"두 점 {pt(a, b)}, {pt(a, c)} 사이의 거리는?", abs(b - c),
                   f"x좌표가 같으므로 두 점은 세로로 나란히 있습니다.\n거리 = |{m(b)} − {par(c)}| = {abs(b - c)}", "x좌표가 같으면 y좌표의 차를 보세요.")
    return num(f"두 점 {pt(b, a)}, {pt(c, a)} 사이의 거리는?", abs(b - c),
               f"y좌표가 같으므로 두 점은 가로로 나란히 있습니다.\n거리 = |{m(b)} − {par(c)}| = {abs(b - c)}", "y좌표가 같으면 x좌표의 차를 보세요.")

def l01_sym(r):
    x, y = nz(r, -8, 8), nz(r, -8, 8)
    t = r.choice(["x축", "y축", "원점"])
    nx, ny = (x, -y) if t == "x축" else (-x, y) if t == "y축" else (-x, -y)
    rule = {"x축": "y좌표의 부호만", "y축": "x좌표의 부호만", "원점": "x좌표와 y좌표의 부호를 모두"}[t]
    return fill(f"점 {pt(x, y)}{'을' if bat(y) else '를'} {t}에 대하여 대칭이동한 점은 ({{{{1}}}}, {{{{2}}}})", [ans(nx), ans(ny)],
                f"{t}에 대한 대칭이동은 {rule} 바꿉니다.\n{pt(x, y)} → {pt(nx, ny)}",
                f"{t} 대칭: 어느 좌표의 부호가 바뀌는지 생각하세요.")

def l01_area(r):
    x1, y1 = nz(r, -5, 2), nz(r, -4, 3)
    w, h = r.randint(2, 7), r.randint(2, 6)
    A, B, C = (x1, y1), (x1 + w, y1), (x1 + w, y1 + h)
    v = F(w * h, 2)
    return num(f"세 점 A{pt(*A)}, B{pt(*B)}, C{pt(*C)}를 꼭짓점으로 하는 삼각형의 넓이는?", fs(v) if v.denominator == 1 else f"{float(v):g}",
               f"A와 B는 y좌표가 같아 밑변 AB = {m(x1 + w)} − {par(x1)} = {w}\nB와 C는 x좌표가 같아 높이 BC = {m(y1 + h)} − {par(y1)} = {h}\n넓이 = {w} × {h} ÷ 2 = {float(v):g}",
               "축에 평행한 변을 밑변과 높이로 쓰세요.", fmt="integer" if v.denominator == 1 else "decimal")

def l01_onaxis(r):
    k, b = nz(r, -6, 6), nz(r, -6, 6)
    if r.random() < .5:
        return num(f"점 (a {'+' if k < 0 else '−'} {abs(k)}, {m(b)})가 y축 위에 있을 때, a의 값은?", k,
                   f"y축 위의 점은 x좌표가 0입니다.\na {'+' if k < 0 else '−'} {abs(k)} = 0 → a = {m(k)}", "y축 위의 점의 x좌표는 0입니다.")
    return num(f"점 ({m(b)}, 2a {'+' if k < 0 else '−'} {2 * abs(k)})가 x축 위에 있을 때, a의 값은?", k,
               f"x축 위의 점은 y좌표가 0입니다.\n2a {'+' if k < 0 else '−'} {2 * abs(k)} = 0 → 2a = {m(2 * k)} → a = {m(k)}", "x축 위의 점의 y좌표는 0입니다.")

def l01_rule(r):
    a, b = r.randint(2, 5), r.randint(-3, 6); n = r.randint(8, 20)
    pts = ", ".join(pt(x, a * x + b) for x in range(0, 4))
    return num(f"순서쌍 {pts}가 같은 규칙을 이어 갈 때, x = {n}이면 y는?", a * n + b,
               f"x가 1씩 늘 때 y는 {a}씩 늘고, x = 0일 때 y = {m(b)}입니다.\n규칙: y = {poly((a, 'x'), (b, ''))}\nx = {n} 대입: {a} × {n}{term(b)} = {a * n + b}",
               "x가 1 늘 때 y가 얼마나 느는지, x = 0일 때 y가 얼마인지 보세요.")

def l01_sign(r):
    sa, sb = r.choice([(-1, 1), (1, -1), (-1, -1), (1, 1)])
    forms = [("a", "b", lambda a, b: (a, b)), ("−a", "b", lambda a, b: (-a, b)), ("ab", "a", lambda a, b: (a * b, a)),
             ("a − b", "ab", lambda a, b: (a - b, a * b)), ("b", "−a", lambda a, b: (b, -a)), ("a²", "b", lambda a, b: (a * a, b))]
    fx, fy, f = r.choice(forms)
    if fx == "a − b" and sa == sb: return None
    x, y = f(sa * 2, sb * 3)
    q = quad(x, y)
    cond = f"a {'<' if sa < 0 else '>'} 0, b {'<' if sb < 0 else '>'} 0"
    return fill(f"{cond}일 때 점 ({fx}, {fy})는 제{{{{1}}}}사분면 위의 점입니다.", [[str(q)]],
                f"{fx}의 부호: {'+' if x > 0 else '−'},  {fy}의 부호: {'+' if y > 0 else '−'}\n({'+' if x > 0 else '−'}, {'+' if y > 0 else '−'})이므로 제{q}사분면",
                "각 좌표의 부호만 따지세요. 음수 × 음수 = 양수.")

L01 = [("사분면", l01_quad), ("축까지의 거리", l01_axis), ("두 점 사이의 거리", l01_dist), ("대칭이동", l01_sym),
       ("좌표로 넓이", l01_area), ("축 위의 점", l01_onaxis), ("규칙 찾기", l01_rule), ("부호와 사분면", l01_sign)]

# ---------------- l02 정비례와 반비례 ----------------
def l02_px(r):
    k, x = r.choice([2, 3, 4, 5, 200, 500, 1500]), r.randint(2, 12)
    return num(f"y = {k}x에서 y = {k * x}일 때 x의 값은?", x,
               f"{k * x} = {k}x\n양변을 {ro(k)} 나누면 x = {x}", "y에 값을 넣고 x에 대해 푸세요.")

def l02_prop(r):
    k, x0, x1 = nz(r, -6, 6), r.randint(1, 6), nz(r, -8, 10)
    if x0 == x1: return None
    return num(f"y가 x에 정비례하고 x = {x0}일 때 y = {m(k * x0)}입니다. x = {m(x1)}일 때 y의 값은?", k * x1,
               f"y = ax로 놓고 대입: {m(k * x0)} = {x0}a → a = {m(k)}\ny = {poly((k, 'x'))}\nx = {m(x1)}이면 y = {m(k)} × {par(x1)} = {m(k * x1)}",
               "정비례는 y = ax 꼴입니다.")

def l02_inv(r):
    a = r.choice([12, 18, 24, 30, 36, 48, 60, -12, -24])
    ds = [d for d in divisors(abs(a))]
    x0, x1 = r.sample(ds, 2)
    return num(f"y가 x에 반비례하고 x = {x0}일 때 y = {m(a // x0)}입니다. x = {x1}일 때 y의 값은?", a // x1,
               f"반비례는 xy가 일정합니다: xy = {x0} × {par(a // x0)} = {m(a)}\ny = {m(a)}/x\nx = {x1}이면 y = {m(a)} ÷ {x1} = {m(a // x1)}",
               "반비례에서는 x × y가 항상 같습니다.")

def l02_a_lin(r):
    a, x = nz(r, -5, 5), nz(r, -4, 4)
    return num(f"y = ax의 그래프가 점 {pt(x, a * x)}를 지날 때, a의 값은?", a,
               f"점의 좌표를 대입: {m(a * x)} = a × {par(x)}\na = {m(a * x)} ÷ {par(x)} = {m(a)}", "그래프가 지나는 점의 좌표를 식에 넣으세요.")

def l02_a_inv(r):
    x, y = nz(r, -6, 6), nz(r, -6, 6)
    return num(f"y = a/x의 그래프가 점 {pt(x, y)}를 지날 때, a의 값은?", x * y,
               f"y = a/x이면 a = xy\na = {m(x)} × {par(y)} = {m(x * y)}", "a = xy 입니다.")

def l02_gear(r):
    a, b, n = r.choice([20, 24, 30, 36, 40]), r.choice([12, 15, 16, 18, 20, 24, 45, 48, 60]), r.randint(2, 6)
    if a == b or (a * n) % b: return None
    return num(f"톱니가 {a}개인 톱니바퀴 A와 톱니가 {b}개인 톱니바퀴 B가 맞물려 돌고 있습니다. A가 {n}바퀴 돌 때 B는 몇 바퀴 돌까요?", a * n // b,
               f"맞물린 톱니 수는 같습니다: {a} × {n} = {a * n}개\nB의 회전수 = {a * n} ÷ {b} = {a * n // b}\n(톱니 수와 회전수는 반비례)",
               "두 바퀴가 맞물려 지나간 톱니 수는 같습니다.")

def l02_lattice(r):
    n = r.choice([6, 8, 10, 12, 15, 16, 18, 20, 24, 30])
    d = divisors(n)
    return num(f"y = {n}/x의 그래프 위의 점 중 x좌표와 y좌표가 모두 정수인 점은 몇 개일까요?", 2 * len(d),
               f"x가 {n}의 약수여야 y도 정수입니다.\n양의 약수: {', '.join(map(str, d))} → {len(d)}개\nx가 음의 약수일 때도 (−1, −{n})처럼 정수 좌표가 되므로 2배: {2 * len(d)}개",
               "x는 양의 약수와 음의 약수 모두 될 수 있습니다.")

def l02_rect(r):
    a = r.choice([24, 36, 48, 60, 72]); x = r.choice([d for d in divisors(a) if 2 <= d <= a // 2])
    return num(f"넓이가 {a}cm²인 직사각형의 가로를 x cm, 세로를 y cm라 할 때, x = {x}이면 y는?", a // x,
               f"xy = {a}이므로 y = {a}/x (반비례)\nx = {x}이면 y = {a} ÷ {x} = {a // x}", "가로 × 세로 = 넓이")

L02 = [("정비례식 풀기", l02_px), ("정비례 관계", l02_prop), ("반비례 관계", l02_inv), ("y = ax의 a", l02_a_lin),
       ("y = a/x의 a", l02_a_inv), ("톱니바퀴", l02_gear), ("정수 좌표 세기", l02_lattice), ("넓이가 일정한 직사각형", l02_rect)]

# ---------------- l03 일차함수와 기울기 ----------------
def l03_f(r):
    a, b, k = nz(r, -6, 6), nz(r, -9, 9), nz(r, -5, 5)
    return num(f"f(x) = {poly((a, 'x'), (b, ''))}일 때 f({m(k)})의 값은?", a * k + b,
               f"x 자리에 {par(k)} 대입\nf({m(k)}) = {m(a)} × {par(k)}{term(b)} = {m(a * k)}{term(b)} = {m(a * k + b)}", "x 대신 괄호 안의 수를 넣으세요.")

def l03_inv(r):
    a, b, k = nz(r, -6, 6), nz(r, -9, 9), nz(r, -6, 6)
    return num(f"f(x) = {poly((a, 'x'), (b, ''))}에서 f(a) = {m(a * k + b)}일 때, a의 값은?", k,
               f"{poly((a, 'a'), (b, ''))} = {m(a * k + b)}\n{poly((a, 'a'))} = {m(a * k)}\na = {m(k)}", "f(a)는 x 자리에 a를 넣은 식입니다.")

def l03_int(r):
    a, x0 = nz(r, -5, 5), nz(r, -6, 6)
    b = -a * x0
    return fill(f"y = {poly((a, 'x'), (b, ''))}의 그래프에서 x절편은 {{{{1}}}}, y절편은 {{{{2}}}}", [ans(x0), ans(b)],
                f"x절편: y = 0을 대입 → {poly((a, 'x'))}{term(b)} = 0 → x = {m(x0)}\ny절편: x = 0을 대입 → y = {m(b)}",
                "x절편은 y = 0, y절편은 x = 0일 때입니다.")

def l03_slope(r):
    x1, y1, x2, y2 = nz(r, -5, 5), nz(r, -6, 6), nz(r, -5, 5), nz(r, -6, 6)
    if x1 == x2: return None
    s = F(y2 - y1, x2 - x1)
    return num(f"두 점 {pt(x1, y1)}, {pt(x2, y2)}를 지나는 직선의 기울기는?", s,
               f"기울기 = (y의 증가량)/(x의 증가량)\n= ({m(y2)} − {par(y1)}) / ({m(x2)} − {par(x1)}) = {m(y2 - y1)}/{m(x2 - x1)}" + (f" = {fm(s)}" if (s.numerator, s.denominator) != (y2 - y1, x2 - x1) else ""),
               "두 점의 y좌표 차를 x좌표 차로 나누세요.", fmt="fraction" if s.denominator > 1 else "integer")

def l03_incr(r):
    a, b, d = nz(r, -6, 6), nz(r, -9, 9), r.randint(2, 6)
    return num(f"y = {poly((a, 'x'), (b, ''))}에서 x가 {d}만큼 증가하면 y는 얼마만큼 증가할까요? (감소하면 음수로)", a * d,
               f"기울기 = (y의 증가량)/(x의 증가량) = {m(a)}\ny의 증가량 = {m(a)} × {d} = {m(a * d)}", "y의 증가량 = 기울기 × x의 증가량")

def l03_pt(r):
    a, x, y = nz(r, -5, 5), nz(r, -5, 5), nz(r, -8, 8)
    b = y - a * x
    return fill(f"기울기가 {m(a)}이고 점 {pt(x, y)}를 지나는 직선은 y = {poly((a, 'x'))} + {{{{1}}}}", [ans(b)],
                f"y = {poly((a, 'x'))} + b에 점을 대입: {m(y)} = {m(a)} × {par(x)} + b\n{m(y)} = {m(a * x)} + b → b = {m(b)}",
                "y = ax + b에 지나는 점을 대입하세요.")

def l03_two(r):
    a, b = nz(r, -4, 4), nz(r, -7, 7); x1, x2 = r.sample(range(-4, 5), 2)
    return fill(f"두 점 {pt(x1, a * x1 + b)}, {pt(x2, a * x2 + b)}를 지나는 직선은 y = {{{{1}}}}x + {{{{2}}}}", [ans(a), ans(b)],
                f"기울기 = ({m(a * x2 + b)} − {par(a * x1 + b)}) / ({m(x2)} − {par(x1)}) = {m(a * (x2 - x1))}/{m(x2 - x1)} = {m(a)}\n"
                f"y = {poly((a, 'x'))} + b에 {pt(x1, a * x1 + b)} 대입: {m(a * x1 + b)} = {m(a * x1)} + b → b = {m(b)}",
                "기울기를 먼저 구하고, 한 점을 대입해 y절편을 구하세요.")

def l03_par(r):
    a, b, c = nz(r, -6, 6), nz(r, -6, 6), nz(r, -6, 6)
    if b == c: return None
    t = r.choice(["par", "shift"])
    if t == "par":
        return num(f"y = kx{term(c)}의 그래프가 y = {poly((a, 'x'), (b, ''))}의 그래프와 평행할 때, k의 값은?", a,
                   f"평행한 두 직선은 기울기가 같고 y절편이 다릅니다.\n기울기 비교: k = {m(a)}", "평행 ↔ 기울기가 같다")
    return fill(f"y = {poly((a, 'x'))}의 그래프를 y축 방향으로 {m(c)}만큼 평행이동하면 y = {poly((a, 'x'))} + {{{{1}}}}", [ans(c)],
                f"y축 방향 평행이동은 식에 그 값을 더합니다.\ny = {poly((a, 'x'), (c, ''))}", "y축 방향으로 k만큼 이동하면 + k")

def l03_word(r):
    t = r.choice(["water", "candle"])
    if t == "water":
        s, d = r.choice([10, 15, 20, 25]), r.choice([2, 4, 5])
        if (100 - s) % d: return None
        return num(f"{s}°C의 물을 데우면 1분마다 {d}°C씩 올라갑니다. 물이 100°C가 되는 것은 몇 분 후일까요?", (100 - s) // d,
                   f"x분 후 온도 y = {d}x + {s}\n{d}x + {s} = 100 → {d}x = {100 - s} → x = {(100 - s) // d}", "온도 = 처음 온도 + (1분 상승량) × 시간")
    L0, d = r.choice([20, 24, 30, 36]), r.choice([2, 3, 4])
    if L0 % d: return None
    h = r.randint(1, L0 // d - 1); left = L0 - d * h
    return num(f"길이가 {L0}cm인 양초가 1시간에 {d}cm씩 탑니다. 양초의 길이가 {left}cm가 되는 것은 불을 붙인 지 몇 시간 후일까요?", h,
               f"x시간 후 길이 y = {L0} − {d}x\n{L0} − {d}x = {left} → {d}x = {L0 - left} → x = {h}", "길이 = 처음 길이 − (1시간에 줄어드는 길이) × 시간")

L03 = [("함숫값", l03_f), ("함숫값에서 a 구하기", l03_inv), ("x절편과 y절편", l03_int), ("두 점으로 기울기", l03_slope),
       ("y의 증가량", l03_incr), ("기울기와 한 점", l03_pt), ("두 점을 지나는 직선", l03_two), ("평행과 평행이동", l03_par), ("일차함수 활용", l03_word)]

# ---------------- l04 일차함수와 일차방정식 ----------------
def l04_solve(r):
    b = r.choice([1, 2, 3, -1, -2]); m1, c1 = nz(r, -4, 4), nz(r, -6, 6)
    a, c = -m1 * b, -c1 * b
    # a x + b y + c = 0 → y = m1 x + c1
    return fill(f"일차방정식 {poly((a, 'x'), (b, 'y'), (c, ''))} = 0을 y에 대해 풀면 y = {{{{1}}}}x + {{{{2}}}}", [ans(m1), ans(c1)],
                f"y항만 남기고 이항: {poly((b, 'y'))} = {poly((-a, 'x'), (-c, ''))}" + (f"\n양변을 {m(b) if b > 0 else '(' + m(b) + ')'}로 나누면 y = {poly((m1, 'x'), (c1, ''))}" if b != 1 else ""),
                "y가 있는 항만 왼쪽에 남기고 y의 계수로 나누세요.")

def l04_inter(r):
    x, y = nz(r, -4, 5), nz(r, -5, 6)
    a1, a2 = r.sample([-3, -2, -1, 1, 2, 3], 2)
    b1, b2 = y - a1 * x, y - a2 * x
    return fill(f"두 직선 y = {poly((a1, 'x'), (b1, ''))}와 y = {poly((a2, 'x'), (b2, ''))}의 교점은 ({{{{1}}}}, {{{{2}}}})", [ans(x), ans(y)],
                f"교점은 두 식을 동시에 만족하므로 y끼리 같다고 놓습니다.\n{poly((a1, 'x'), (b1, ''))} = {poly((a2, 'x'), (b2, ''))}\n{poly((a1 - a2, 'x'))} = {m(b2 - b1)} → x = {m(x)}\n"
                f"y = {m(a1)} × {par(x)}{term(b1)} = {m(y)}",
                "두 식의 y를 같다고 놓고 x를 구하세요.")

def l04_axes(r):
    a, x0 = nz(r, -4, 4), nz(r, -6, 6)
    b = -a * x0
    if b == 0: return None
    v = F(abs(x0) * abs(b), 2)
    return num(f"직선 y = {poly((a, 'x'), (b, ''))}와 x축, y축으로 둘러싸인 삼각형의 넓이는?", f"{float(v):g}",
               f"x절편: 0 = {poly((a, 'x'), (b, ''))} → x = {m(x0)}\ny절편: {m(b)}\n넓이 = |{m(x0)}| × |{m(b)}| ÷ 2 = {float(v):g}",
               "x절편과 y절편을 구해 직각삼각형의 두 변으로 쓰세요.", fmt="integer" if v.denominator == 1 else "decimal")

def l04_twoarea(r):
    # y = x + p, y = −x + q 와 x축
    p, q = r.randint(-2, 5), r.randint(2, 9)
    xi, yi = F(q - p, 2), F(q + p, 2)
    if yi <= 0: return None
    base = q - (-p); v = F(base) * yi / 2
    return num(f"두 직선 y = {poly((1, 'x'), (p, ''))}, y = {poly((-1, 'x'), (q, ''))}와 x축으로 둘러싸인 삼각형의 넓이는?", f"{float(v):g}",
               f"x절편: 첫 직선 x = {m(-p)}, 둘째 직선 x = {q} → 밑변 {base}\n교점: x{term(p)} = −x + {q} → x = {fm(xi)}, y = {fm(yi)} → 높이 {fm(yi)}\n넓이 = {base} × {fm(yi)} ÷ 2 = {float(v):g}",
               "밑변은 두 x절편 사이, 높이는 교점의 y좌표입니다.", fmt="integer" if v.denominator == 1 else "decimal")

def l04_hv(r):
    x, y = nz(r, -7, 7), nz(r, -7, 7)
    if r.random() < .5:
        return num(f"점 {pt(x, y)}를 지나고 y축에 평행한 직선의 방정식은 x = ?", x,
                   f"y축에 평행한 직선 위의 점은 모두 x좌표가 같습니다.\n따라서 x = {m(x)}", "y축에 평행 → x좌표가 일정")
    return num(f"점 {pt(x, y)}를 지나고 x축에 평행한 직선의 방정식은 y = ?", y,
               f"x축에 평행한 직선 위의 점은 모두 y좌표가 같습니다.\n따라서 y = {m(y)}", "x축에 평행 → y좌표가 일정")

def l04_inf(r):
    a, b = nz(r, -5, 5), nz(r, -6, 6)
    return num(f"연립방정식 kx − y = {m(b)}, {poly((a, 'x'))} − y = c의 해가 무수히 많을 때, k + c의 값은?", a + b,
               f"해가 무수히 많으려면 두 일차방정식이 같은 직선이어야 합니다.\nx의 계수: k = {m(a)}, 상수항: c = {m(b)}\nk + c = {m(a + b)}",
               "두 식의 모든 계수가 같아야 합니다.")

def l04_none(r):
    a, b, c = nz(r, -4, 4), nz(r, -6, 6), nz(r, -6, 6)
    if b == c: return None
    return num(f"두 직선 y = {poly((a, 'x'), (b, ''))}와 y = {poly((a, 'x'), (c, ''))}의 교점은 몇 개일까요?", 0,
               f"두 직선의 기울기가 {m(a)}로 같고 y절편이 {j(b, '와과', m(b))} {m(c)}로 다릅니다.\n→ 평행하므로 만나지 않습니다. 교점 0개",
               "기울기와 y절편을 비교하세요.")

def l04_plan(r):
    b1, p1 = r.choice([10000, 12000, 15000]), r.choice([100, 150, 200])
    b2, p2 = b1 + r.choice([4000, 6000, 8000]), p1 - r.choice([50, 100])
    if p2 <= 0 or (b2 - b1) % (p1 - p2): return None
    x = (b2 - b1) // (p1 - p2)
    return num(f"A 요금제는 기본료 {b1:,}원에 1분당 {p1}원, B 요금제는 기본료 {b2:,}원에 1분당 {p2}원입니다. 통화 시간이 몇 분일 때 두 요금이 같을까요?", x,
               f"x분 통화할 때 A: {b1} + {p1}x, B: {b2} + {p2}x\n{b1} + {p1}x = {b2} + {p2}x\n{p1 - p2}x = {b2 - b1} → x = {x}\n(이보다 오래 통화하면 B가 유리)",
               "두 요금을 일차함수로 나타내 같다고 놓으세요.")

L04 = [("y에 대해 풀기", l04_solve), ("두 직선의 교점", l04_inter), ("축과 만드는 삼각형", l04_axes), ("두 직선과 x축의 삼각형", l04_twoarea),
       ("축에 평행한 직선", l04_hv), ("해가 무수히 많은 조건", l04_inf), ("평행한 두 직선", l04_none), ("요금제 비교", l04_plan)]

if __name__ == "__main__":
    tot = 0
    for l, T in [("l01", L01), ("l02", L02), ("l03", L03), ("l04", L04)]:
        n = write("c0", "ch04", l, T, per=6); tot += n; print(l, n)
    print("total", tot)
