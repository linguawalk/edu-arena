"""코스 4 · 챕터 1~4 (함수의 극한, 미분계수와 도함수, 도함수의 활용, 적분) — 연습 문제 은행"""
from core import *
import sympy as sp

X = sp.Symbol("x")
def nz(r, a, b):
    while True:
        v = r.randint(a, b)
        if v: return v
def P(*c):
    """계수 높은 차수부터: P(1, 0, -3) → x² − 3"""
    n = len(c) - 1
    names = {0: "", 1: "x", 2: "x²", 3: "x³", 4: "x⁴", 5: "x⁵"}
    return poly(*[(ci, names[n - i]) for i, ci in enumerate(c)])
def E(*c):
    n = len(c) - 1
    return sum(ci * X ** (n - i) for i, ci in enumerate(c))
def Fr(v): return F(str(sp.nsimplify(v)))
def nf(v, prompt, expl, hint):
    v = Fr(v)
    return num(prompt, v, expl, hint, fmt="fraction" if v.denominator > 1 else "integer")
def fx(p): return "x" if p == 0 else f"(x{term(-p)})"
def fsub(a): return str(a).translate(str.maketrans("0123456789-", "₀₁₂₃₄₅₆₇₈₉₋"))
def ev(c, x0): return sum(ci * x0 ** (len(c) - 1 - i) for i, ci in enumerate(c))
def der(c): n = len(c) - 1; return [ci * (n - i) for i, ci in enumerate(c[:-1])]
def ip(c, a, b):
    n = len(c) - 1
    return sum(F(ci, n - i + 1) * (F(b) ** (n - i + 1) - F(a) ** (n - i + 1)) for i, ci in enumerate(c))
def ap(c):
    """원시함수 표기"""
    n = len(c) - 1; out = ""
    for i, ci in enumerate(c):
        k = n - i + 1; co = F(ci, k)
        if co == 0: continue
        v = {1: "x", 2: "x²", 3: "x³", 4: "x⁴", 5: "x⁵", 6: "x⁶"}[k]
        s = (fs(abs(co)) if abs(co) != 1 else "") if co.denominator == 1 else f"({fs(abs(co))})"
        out += ("−" if co < 0 else "") + s + v if not out else (" − " if co < 0 else " + ") + s + v
    return out or "0"

# ================= ch01 함수의 극한 =================
def a1_sub(r):
    c = [r.randint(-3, 3), nz(r, -5, 5), r.randint(-6, 6)]; a = r.randint(-3, 4)
    return nf(ev(c, a), f"lim(x→{m(a)}) ({P(*c)})의 값은?", f"다항함수는 연속이므로 x = {m(a)}를 그대로 대입합니다.\n" + " + ".join(f"{mul(ci, par(a) + (sup(2 - i) if 2 - i > 1 else '')) if 2 - i else m(ci)}" for i, ci in enumerate(c) if ci) + f" = {m(ev(c, a))}",
              "다항함수의 극한은 대입한 값")
def a1_side(r):
    k = r.randint(-2, 3); p, q = nz(r, -3, 3), r.randint(-4, 4); s = r.randint(-4, 4)
    L, R_ = p * k + q, k * k + s
    t = r.choice(["L", "R", "ex"])
    desc = f"f(x) = {poly((p, 'x'), (q, ''))} (x < {m(k)}), x²{term(s)} (x ≥ {m(k)})"
    if t == "ex":
        v = 1 if L == R_ else 0
        return num(f"{desc}일 때 lim(x→{m(k)}) f(x)가 존재할까요?  (그렇다 1, 아니다 0)", v,
                   f"좌극한: {m(p)}×{par(k)}{term(q)} = {m(L)}\n우극한: {par(k)}²{term(s)} = {m(R_)}\n" + ("같으므로 존재 → 1" if v else "다르므로 존재하지 않음 → 0"), "좌극한과 우극한이 같아야 합니다.")
    v = L if t == "L" else R_
    return num(f"{desc}일 때 lim(x→{m(k)}{'−' if t == 'L' else '+'}) f(x)의 값은?", v,
               f"x → {m(k)}{'−' if t == 'L' else '+'}는 {m(k)}보다 {'작은' if t == 'L' else '큰'} 쪽에서 다가가므로 {'위' if t == 'L' else '아래'}의 식을 씁니다.\n{'{}×{}{} = {}'.format(m(p), par(k), term(q), m(L)) if t == 'L' else '{}²{} = {}'.format(par(k), term(s), m(R_))}",
               "어느 쪽 식을 쓸지 먼저 정하세요.")
def a1_inf(r):
    a, b, c, d = nz(r, -6, 6), nz(r, -5, 5), nz(r, -4, 4), nz(r, -5, 5)
    v = F(a, c)
    def tail(k): return f" {'+' if k > 0 else '−'} {abs(k)}/x"
    return nf(v, f"lim(x→∞) ({poly((a, 'x'), (b, ''))})/({poly((c, 'x'), (d, ''))})의 값은? (기약분수 또는 정수로)",
              f"분자·분모를 x로 나누면 ({m(a)}{tail(b)})/({m(c)}{tail(d)})\nx → ∞이면 상수/x → 0이므로 {m(a)} ÷ {par(c)} = {fm(v)}", "최고차항의 계수의 비")
L11 = [("다항함수의 극한", a1_sub), ("좌극한과 우극한", a1_side), ("x → ∞의 극한", a1_inf)]

def a2_fac(r):
    a, b = r.sample(range(-5, 6), 2)
    num_ = P(1, -(a + b), a * b)
    return nf(a - b, f"lim(x→{m(a)}) ({num_})/(x{term(-a)})의 값은?",
              f"x = {m(a)}를 넣으면 0/0 꼴 → 인수분해해서 약분합니다.\n({num_}) = (x{term(-a)})(x{term(-b)})\n약분하면 x{term(-b)} → x = {m(a)} 대입: {m(a - b)}", "0/0 꼴은 인수분해")
def a2_cube(r):
    a = nz(r, -3, 3)
    return nf(3 * a * a, f"lim(x→{m(a)}) (x³{term(-a ** 3)})/(x{term(-a)})의 값은?",
              f"x³ − a³ = (x − a)(x² + ax + a²)로 약분\nx² + ({m(a)})x + {a * a} → x = {m(a)}: {a * a} + {m(a * a)} + {a * a} = {3 * a * a}", "세제곱의 차 공식")
def a2_root(r):
    a = r.randint(1, 6)
    return nf(F(1, 2 * a), f"lim(x→0) (√(x + {a * a}) − {a})/x의 값은? (기약분수로)",
              f"분자를 유리화: (√(x + {a * a}) − {a})(√(x + {a * a}) + {a}) = x\n극한 = lim 1/(√(x + {a * a}) + {a}) = 1/({a} + {a}) = {fs(F(1, 2 * a))}", "분자를 유리화하세요.")
def a2_deg(r):
    p, q = nz(r, -6, 6), nz(r, -5, 5); d1, d2 = r.choice([(2, 2), (1, 2), (3, 3), (2, 3)])
    v = F(p, q) if d1 == d2 else 0
    names = {1: "x", 2: "x²", 3: "x³"}
    return nf(v, f"lim(x→∞) ({poly((p, names[d1]), (r.randint(1, 5), ''))})/({poly((q, names[d2]), (r.randint(-5, 5), 'x'), (1, ''))})의 값은? (기약분수 또는 정수로)",
              f"분자 {d1}차, 분모 {d2}차\n" + (f"차수가 같으면 최고차항 계수의 비: {m(p)}/{m(q)} = {fm(v)}" if d1 == d2 else "분모의 차수가 더 크면 0으로 수렴"), "차수를 비교하세요.")
def a2_alg(r):
    A, B, p, q = r.randint(-5, 6), r.randint(-5, 6), nz(r, -3, 3), nz(r, -3, 3)
    t = r.choice(["lin", "prod"])
    if t == "lin":
        return nf(p * A + q * B, f"lim f(x) = {m(A)}, lim g(x) = {m(B)}일 때 lim ({poly((p, 'f(x)'), (q, 'g(x)'))})의 값은?", f"극한의 성질로 나누어 계산합니다.\n{m(p)}×{par(A)} + {par(q)}×{par(B)} = {m(p * A + q * B)}", "극한은 더하기·상수배를 나눌 수 있습니다.")
    return nf(A * B, f"lim f(x) = {m(A)}, lim g(x) = {m(B)}일 때 lim f(x)g(x)의 값은?", f"수렴하는 두 함수의 곱의 극한은 극한의 곱입니다.\n{m(A)} × {par(B)} = {m(A * B)}", "극한의 곱")
L12 = [("0/0 꼴 인수분해", a2_fac), ("세제곱의 차", a2_cube), ("무리식의 극한", a2_root), ("∞/∞ 꼴", a2_deg), ("극한의 성질", a2_alg)]

def a3_cont(r):
    k, p, q, s = r.randint(-2, 3), nz(r, -3, 3), r.randint(-4, 4), nz(r, -3, 3)
    t = r.choice(["a", "k", "a2"])
    if t == "a":
        a = s * k - p * k
        return nf(a, f"f(x) = {poly((p, 'x'))} + a (x < {m(k)}), {poly((s, 'x'))} (x ≥ {m(k)})가 x = {m(k)}에서 연속일 때 a의 값은?",
                  f"연속 ⇔ 좌극한 = 우극한 = f({m(k)})\n{m(p)}×{par(k)} + a = {m(s)}×{par(k)} → a = {m(a)}", "경계에서 두 식의 값을 같게")
    if t == "k":
        c = nz(r, -5, 5)
        return nf(2 * c, f"f(x) = (x² − {c * c})/(x{term(-c)}) (x ≠ {m(c)}), k (x = {m(c)})가 실수 전체에서 연속일 때 k의 값은?",
                  f"k = lim(x→{m(c)}) (x² − {c * c})/(x{term(-c)}) = lim (x{term(c)}) = {m(2 * c)}", "함숫값 = 극한값")
    k = r.choice([1, 2, 3, -1, -2]); b = r.randint(-3, 4)
    a = F(k + b, k * k)
    return nf(a, f"f(x) = ax² (x ≤ {m(k)}), x{term(b)} (x > {m(k)})가 연속일 때 a의 값은? (기약분수 또는 정수로)",
              f"x = {m(k)}에서 a×{par(k)}² = {m(k)}{term(b)} → {k * k}a = {m(k + b)} → a = {fm(a)}", "경계값을 같게")
def a3_disc(r):
    t = r.choice(["sq", "q", "none"])
    if t == "sq":
        a = r.randint(1, 6); return num(f"f(x) = 1/(x² − {a * a})이 불연속인 점은 몇 개일까요?", 2, f"분모가 0인 x² = {a * a} → x = ±{a}\n정의되지 않는 두 점에서 불연속 → 2개", "분모가 0이 되는 점")
    if t == "q":
        a, b = r.sample(range(-5, 6), 2)
        return num(f"f(x) = 1/({P(1, -(a + b), a * b)})이 불연속인 점은 몇 개일까요?", 2, f"분모 (x{term(-a)})(x{term(-b)}) = 0 → x = {m(a)}, {m(b)}\n2개", "분모를 인수분해")
    a = r.randint(1, 6); return num(f"f(x) = 1/(x² + {a})이 불연속인 점은 몇 개일까요?", 0, f"x² + {a} ≥ {a} > 0이므로 분모가 0이 되지 않습니다.\n실수 전체에서 연속 → 0개", "분모가 0이 될 수 있는지 보세요.")
def a3_ext(r):
    p, q = r.randint(-3, 3), r.randint(-4, 4); lo = r.randint(-3, 1); hi = lo + r.randint(2, 5)
    f = lambda x: (x - p) ** 2 + q
    vals = [f(lo), f(hi)] + ([q] if lo <= p <= hi else []); t = r.choice(["max", "min"])
    v = max(vals) if t == "max" else min(vals)
    return nf(v, f"닫힌구간 [{m(lo)}, {m(hi)}]에서 f(x) = {P(1, -2 * p, p * p + q)}의 {'최댓값' if t == 'max' else '최솟값'}은?",
              f"연속함수는 닫힌구간에서 최댓값·최솟값을 가집니다(최대·최소 정리).\nf = (x{term(-p)})²{term(q)}, 후보: 양 끝 {m(f(lo))}, {m(f(hi))}" + (f", 꼭짓점 {m(q)}" if lo < p < hi else "") + f" → {m(v)}", "꼭짓점과 양 끝값을 비교")
L13 = [("연속이 되는 조건", a3_cont), ("불연속점의 개수", a3_disc), ("최대·최소 정리", a3_ext)]

def a4_n(r):
    a, b = r.randint(0, 3), r.randint(-9, 9)
    c = [1, 0, a, b]
    roots = [n for n in range(-6, 6) if ev(c, n) < 0 < ev(c, n + 1)]
    if len(roots) != 1: return None
    n = roots[0]
    return nf(n, f"f(x) = {P(*c)}에서 f(n) < 0 < f(n + 1)을 만족하는 정수 n은?",
              f"차례로 대입: f({m(n)}) = {m(ev(c, n))} < 0, f({m(n + 1)}) = {m(ev(c, n + 1))} > 0\n사잇값 정리로 ({m(n)}, {m(n + 1)})에 근이 있습니다. → n = {m(n)}", "정수를 차례로 대입해 부호를 보세요.")
def a4_yes(r):
    c = [1, r.randint(-3, 3), r.randint(-5, 5), r.randint(-5, 5)]; a = r.randint(-3, 2); b = a + 1
    fa, fb = ev(c, a), ev(c, b)
    if fa * fb == 0: return None
    v = 1 if fa * fb < 0 else 0
    if v == 0:
        rr = [x for x in sp.Poly(E(*c), X).real_roots() if a < x < b]
        if rr: return None
    return num(f"{P(*c)} = 0은 구간 ({m(a)}, {m(b)})에서 근을 가질까요?  (그렇다 1, 아니다 0)", v,
               f"f({m(a)}) = {m(fa)}, f({m(b)}) = {m(fb)}\n" + ("부호가 다르므로 사잇값 정리에 의해 근이 있습니다 → 1" if v else "부호가 같고 이 구간에서 근이 없습니다 → 0"), "양 끝의 부호를 비교하세요.")
def a4_cnt(r):
    xs = sorted(r.sample(range(-4, 6), 5)); vs = [nz(r, -6, 6) for _ in xs]
    ch = sum(1 for i in range(4) if vs[i] * vs[i + 1] < 0)
    return num(f"연속함수 f에서 {', '.join(f'f({m(x)}) = {m(v)}' for x, v in zip(xs, vs))}입니다. f(x) = 0의 실근은 적어도 몇 개일까요?", ch,
               f"이웃한 두 값의 부호가 바뀌는 곳마다 사잇값 정리로 근이 하나 이상 있습니다.\n부호가 바뀌는 구간 {ch}개 → 적어도 {ch}개", "부호 변화 횟수를 세세요.")
L14 = [("근이 있는 정수 구간", a4_n), ("근의 존재", a4_yes), ("근의 최소 개수", a4_cnt)]

# ================= ch02 미분계수와 도함수 =================
def b1_der(r):
    c = [nz(r, -3, 4), r.randint(-5, 5), r.randint(-5, 5)]; a = r.randint(-3, 4)
    return nf(2 * c[0] * a + c[1], f"f(x) = {P(*c)}일 때 f′({m(a)})의 값은?",
              f"f′(a) = lim(h→0) (f(a + h) − f(a))/h\n계산하면 f′(x) = {P(*der(c))}\nf′({m(a)}) = {m(2 * c[0] * a + c[1])}", "미분계수의 정의 또는 도함수")
def b1_avg(r):
    a, k = nz(r, -3, 4), r.randint(-2, 3); h = r.choice([1, 2, F(1, 10), 3])
    v = a * (2 * k + h)
    return nf(v, f"f(x) = {P(a, 0, 0)}에서 x가 {m(k)}에서 {fm(k + h)}까지 변할 때 평균변화율은?" if F(h).denominator == 1 else f"f(x) = {P(a, 0, 0)}에서 x가 {m(k)}에서 {float(k + h):g}까지 변할 때 평균변화율은? (기약분수 또는 정수로)",
              f"(f(b) − f(a))/(b − a) = {m(a)}(b² − a²)/(b − a) = {m(a)}(a + b)\n= {m(a)} × ({m(k)} + {float(k + h):g}) = {fm(v)}", "Δy/Δx")
def b1_vel(r):
    a, b, t = r.randint(1, 5), r.randint(-4, 6), r.randint(1, 5)
    return nf(2 * a * t + b, f"위치가 s(t) = {poly((a, 't²'), (b, 't'))}(m)일 때 t = {t}초에서의 순간 속도는 초속 몇 m일까요?",
              f"순간 속도 = s′(t) = {poly((2 * a, 't'), (b, ''))}\nt = {t}: {m(2 * a * t + b)}", "위치를 미분하면 속도")
def b1_lim(r):
    d, k, j_ = r.randint(-5, 8), nz(r, -4, 4), r.choice([1, 2, 3])
    v = F(k, j_) * d
    return nf(v, f"f′(a) = {m(d)}일 때 lim(h→0) (f(a + {k}h) − f(a))/{'' if j_ == 1 else j_}h의 값은? (기약분수 또는 정수로)".replace("+ −", "− ").replace("/h", "/h"),
              f"분모를 {k}h로 맞추면 (f(a + {k}h) − f(a))/({k}h) × {k}/{j_}\n→ f′(a) × {fm(F(k, j_))} = {fm(v)}", "분자의 증분과 분모를 같게 맞추세요.")
L21 = [("미분계수", b1_der), ("평균변화율", b1_avg), ("순간 속도", b1_vel), ("미분계수의 변형", b1_lim)]

def b2_tan(r):
    c = [nz(r, -3, 3), r.randint(-4, 4), r.randint(-5, 5)]; a = r.randint(-3, 3)
    s = 2 * c[0] * a + c[1]; y0 = ev(c, a); b = y0 - s * a
    t = r.choice(["slope", "int"])
    if t == "slope": return nf(s, f"y = {P(*c)} 위의 점 ({m(a)}, {m(y0)})에서의 접선의 기울기는?", f"y′ = {P(*der(c))}\nx = {m(a)}: {m(s)}", "접선의 기울기 = 미분계수")
    return nf(b, f"y = {P(*c)} 위의 점 ({m(a)}, {m(y0)})에서의 접선의 y절편은?", f"기울기 f′({m(a)}) = {m(s)}\ny − {par(y0)} = {m(s)}(x − {par(a)}) → y = {poly((s, 'x'), (b, ''))}\ny절편 {m(b)}", "y − f(a) = f′(a)(x − a)")
def b2_diff(r):
    k, q = nz(r, -2, 3), nz(r, -3, 3)
    a = 2 * q * k; b = q * k * k - a * k
    ask = r.choice(["a", "b"])
    return nf(a if ask == "a" else b, f"f(x) = {P(q, 0, 0)} (x < {m(k)}), ax + b (x ≥ {m(k)})가 x = {m(k)}에서 미분가능할 때 {ask}의 값은?",
              f"미분가능 ⇒ 연속: {m(q)}×{par(k)}² = {poly((k, 'a'), (1, 'b'))}\n미분계수 일치: {m(2 * q)}×{par(k)} = a → a = {m(a)}\nb = {m(q * k * k)} − {mul(a, k)} = {m(b)}", "연속 + 기울기 일치")
L22 = [("접선", b2_tan), ("미분가능할 조건", b2_diff)]

def b3_pow(r):
    n = r.randint(2, 9); t = r.choice(["exp", "val", "find"])
    if t == "exp": return fill(f"(x{sup(n)})′ = {n}x^{{{{1}}}}", [str(n - 1)], f"(xⁿ)′ = nxⁿ⁻¹\n(x{sup(n)})′ = {n}x{sup(n - 1) if n > 2 else ''}" if n > 2 else "(x²)′ = 2x (지수 1)", "지수를 앞으로 내리고 1을 뺍니다.")
    if t == "val":
        a = nz(r, -2, 3); return nf(n * a ** (n - 1), f"f(x) = x{sup(n)}일 때 f′({m(a)})의 값은?", f"f′(x) = {n}x{sup(n - 1)}\nf′({m(a)}) = {n} × {par(a)}{sup(n - 1)} = {m(n * a ** (n - 1))}", "(xⁿ)′ = nxⁿ⁻¹")
    a = nz(r, -6, 6); c = r.randint(1, 4)
    return nf(a, f"f(x) = {c if c > 1 else ''}x²에서 f′(a) = {m(2 * c * a)}일 때 a의 값은?", f"f′(x) = {2 * c}x\n{2 * c}a = {m(2 * c * a)} → a = {m(a)}", "도함수를 구해 방정식을 푸세요.")
L23 = [("거듭제곱의 미분", b3_pow), ("상수·일차의 미분", lambda r: nf(nz(r, -9, 9) * 0, f"({m(r.randint(2, 30))})′의 값은?", "상수함수는 변하지 않으므로 순간변화율이 0입니다.\n(c)′ = 0", "상수의 미분은 0")),
       ("다항함수의 미분계수", lambda r: b4_val(r))]

def b4_val(r):
    c = [nz(r, -3, 3), r.randint(-4, 4), r.randint(-5, 5), r.randint(-5, 5)]; a = r.randint(-2, 3)
    d = der(c)
    return nf(ev(d, a), f"f(x) = {P(*c)}일 때 f′({m(a)})의 값은?", f"f′(x) = {P(*d)}\nf′({m(a)}) = {m(ev(d, a))}", "항별로 미분하세요.")
def b4_prod(r):
    p, q, s = nz(r, -3, 3), r.randint(-4, 4), r.randint(-4, 4); a = r.randint(-2, 3)
    # (x + p)(x² + q x + s)
    c = [1, p + q, p * q + s, p * s]
    return nf(ev(der(c), a), f"f(x) = (x{term(p)})({P(1, q, s)})일 때 f′({m(a)})의 값은?",
              f"곱의 미분: f′ = 1×({P(1, q, s)}) + (x{term(p)})({P(2, q)})\nx = {m(a)}: {m(ev([1, q, s], a))} + {m(a + p)}×{par(2 * a + q)} = {m(ev(der(c), a))}", "(fg)′ = f′g + fg′")
def b4_power(r):
    a, b, n = nz(r, -3, 3), r.randint(-3, 3), r.randint(2, 4); x0 = r.randint(-1, 2)
    v = n * a * (a * x0 + b) ** (n - 1)
    return nf(v, f"f(x) = ({poly((a, 'x'), (b, ''))}){sup(n)}일 때 f′({m(x0)})의 값은?", f"f′(x) = {n}({poly((a, 'x'), (b, ''))}){sup(n - 1) if n > 2 else ''} × {m(a)}\nx = {m(x0)}: {n} × {par(a * x0 + b)}{sup(n - 1) if n > 2 else ''} × {par(a)} = {m(v)}", "{(ax + b)ⁿ}′ = n(ax + b)ⁿ⁻¹ × a")
def b4_param(r):
    a, b = nz(r, -4, 4), nz(r, -5, 5); p, q = r.sample([0, 1, 2, -1], 2)
    ask = r.choice(["a", "b"])
    return nf(a if ask == "a" else b, f"f(x) = ax² + bx에서 f′({m(p)}) = {m(2 * a * p + b)}, f′({m(q)}) = {m(2 * a * q + b)}일 때 {ask}의 값은?",
              f"f′(x) = 2ax + b\n{poly((2 * p, 'a'), (1, 'b'))} = {m(2 * a * p + b)}, {poly((2 * q, 'a'), (1, 'b'))} = {m(2 * a * q + b)}\n연립하면 a = {m(a)}, b = {m(b)}", "도함수에 대입해 연립")
L24 = [("다항함수의 미분계수", b4_val), ("곱의 미분", b4_prod), ("(ax + b)ⁿ의 미분", b4_power), ("미분계수로 계수 구하기", b4_param)]
L23[2] = ("다항함수의 미분계수", b4_val)

# ================= ch03 도함수의 활용 =================
def c1_tan(r):
    c = [1, r.randint(-3, 3), r.randint(-4, 4), r.randint(-4, 4)]; a = r.randint(-2, 2)
    s, y0 = ev(der(c), a), ev(c, a); b = y0 - s * a
    return fill(f"y = {P(*c)} 위의 점 ({m(a)}, {m(y0)})에서의 접선은 y = {poly((s, 'x'))} + {{{{1}}}}" if s else f"y = {P(*c)} 위의 점 ({m(a)}, {m(y0)})에서의 접선은 y = {{{{1}}}}", [ans(b)],
                f"f′(x) = {P(*der(c))}, f′({m(a)}) = {m(s)}\ny − {par(y0)} = {m(s)}(x − {par(a)}) → y = {poly((s, 'x'), (b, ''))}", "y − f(a) = f′(a)(x − a)")
def c1_slope(r):
    k, p = nz(r, -3, 3), r.randint(-4, 4); m_ = 2 * k + p
    return nf(k, f"y = {P(1, p, r.randint(-3, 3))}의 접선 중 기울기가 {m(m_)}인 것의 접점의 x좌표는?", f"y′ = 2x{term(p)} = {m(m_)}\n2x = {m(m_ - p)} → x = {m(k)}", "y′ = 주어진 기울기")
def c1_mvt(r):
    a, b = sorted(r.sample(range(-4, 7), 2)); c = [nz(r, -3, 3), r.randint(-4, 4), r.randint(-5, 5)]
    return nf(F(a + b, 2), f"구간 [{m(a)}, {m(b)}]에서 f(x) = {P(*c)}에 대해 평균값 정리를 만족하는 c는? (기약분수 또는 정수로)",
              f"(f({m(b)}) − f({m(a)}))/({m(b)} − {par(a)}) = {fm(F(ev(c, b) - ev(c, a), b - a))}\nf′(c) = {m(2 * c[0])}c{term(c[1])} = {fm(F(ev(c, b) - ev(c, a), b - a))} → c = {fm(F(a + b, 2))}\n(이차함수는 항상 구간의 중점)", "f′(c) = 평균변화율")
def c1_norm(r):
    a = nz(r, -4, 4)
    return nf(F(-1, 2 * a), f"y = x² 위의 점 ({m(a)}, {a * a})에서 접선에 수직인 직선의 기울기는? (기약분수로)", f"접선의 기울기 2×{par(a)} = {m(2 * a)}\n수직 → 기울기의 곱 −1: {fm(F(-1, 2 * a))}", "수직 ⇔ 기울기의 곱 = −1")
L31 = [("접선의 방정식", c1_tan), ("기울기가 주어진 접선", c1_slope), ("평균값 정리", c1_mvt), ("법선의 기울기", c1_norm)]

def cub(r):
    """f′ = 3(x − p)(x − q), p < q, p + q 짝수"""
    while True:
        p, q = sorted(r.sample(range(-4, 5), 2))
        if (p + q) % 2 == 0: break
    c0 = r.randint(-5, 5)
    return p, q, [1, -3 * (p + q) // 2, 3 * p * q, c0]
def c2_int(r):
    p, q, c = cub(r); t = r.choice(["dec", "inc", "len"])
    pe = P(*c)
    ex = f"f′(x) = {P(*der(c))} = 3{fx(p)}{fx(q)}"
    if t == "dec": return fill(f"f(x) = {pe}이 감소하는 구간은 {{{{1}}}} < x < {{{{2}}}}", [ans(p), ans(q)], ex + f"\nf′ < 0 ⇔ {m(p)} < x < {m(q)}", "f′(x) < 0인 구간")
    if t == "inc": return fill(f"f(x) = {pe}이 증가하는 구간은 x < {{{{1}}}} 또는 x > {{{{2}}}}", [ans(p), ans(q)], ex + f"\nf′ > 0 ⇔ x < {m(p)} 또는 x > {m(q)}", "f′(x) > 0인 구간")
    return nf(q - p, f"f(x) = {pe}이 감소하는 구간의 길이는?", ex + f"\n감소 구간 ({m(p)}, {m(q)}) → 길이 {q - p}", "f′(x) < 0인 구간")
def c2_k(r):
    b = 3 * nz(r, -3, 3)
    return nf(F(b * b, 3), f"f(x) = x³{term(b, 'x²')} + kx가 실수 전체에서 증가하는 k의 최솟값은?",
              f"f′(x) = 3x²{term(2 * b, 'x')} + k ≥ 0이 항상 성립해야 합니다.\nD/4 = {b * b} − 3k ≤ 0 → k ≥ {fm(F(b * b, 3))}", "f′(x) ≥ 0 ⇔ 판별식 ≤ 0")
def c2_q(r):
    k, a, c0 = nz(r, -5, 5), r.choice([1, 2, 3]), r.randint(-5, 5)
    t = r.choice(["inc", "dec"])
    if t == "inc":
        return fill(f"f(x) = {P(-a, 2 * a * k, c0)}이 증가하는 구간은 x < {{{{1}}}}", [ans(k)],
                    f"f′(x) = {P(-2 * a, 2 * a * k)} > 0\n{2 * a}x < {m(2 * a * k)} → x < {m(k)}", "f′(x) > 0")
    return fill(f"f(x) = {P(a, -2 * a * k, c0)}이 감소하는 구간은 x < {{{{1}}}}", [ans(k)],
                f"f′(x) = {P(2 * a, -2 * a * k)} < 0\n{2 * a}x < {m(2 * a * k)} → x < {m(k)}", "f′(x) < 0")
def c2_pt(r):
    p, q, c = cub(r); x0 = r.choice([z for z in range(-6, 7) if z not in (p, q)])
    v = 1 if ev(der(c), x0) > 0 else 0
    return num(f"f(x) = {P(*c)}는 x = {m(x0)}에서 증가하고 있을까요?  (그렇다 1, 아니다 0)", v,
               f"f′(x) = 3{fx(p)}{fx(q)}\nf′({m(x0)}) = {m(ev(der(c), x0))} {'> 0 → 증가 중' if v else '< 0 → 감소 중'}", "f′의 부호를 보세요.")
L32 = [("증가·감소 구간", c2_int), ("항상 증가할 조건", c2_k), ("이차함수의 증가·감소", c2_q), ("한 점에서의 증감", c2_pt)]

def c3_ext(r):
    p, q, c = cub(r); t = r.choice(["max", "min", "sum"])
    fp, fq = ev(c, p), ev(c, q)
    ex = f"f′(x) = 3{fx(p)}{fx(q)} → x = {m(p)}에서 극대, x = {m(q)}에서 극소\nf({m(p)}) = {m(fp)}, f({m(q)}) = {m(fq)}"
    if t == "max": return nf(fp, f"f(x) = {P(*c)}의 극댓값은?", ex, "f′ = 0인 점에서 부호 변화를 보세요.")
    if t == "min": return nf(fq, f"f(x) = {P(*c)}의 극솟값은?", ex, "f′ = 0인 점에서 부호 변화를 보세요.")
    return nf(fp + fq, f"f(x) = {P(*c)}의 극댓값과 극솟값의 합은?", ex + f"\n합 {m(fp + fq)}", "두 극값을 각각 구하세요.")
def c3_coef(r):
    p, q, c = cub(r); ask = r.choice(["a", "b"])
    return nf(c[1] if ask == "a" else c[2], f"f(x) = x³ + ax² + bx가 x = {m(p)}에서 극대, x = {m(q)}에서 극소일 때 {ask}의 값은?",
              f"f′(x) = 3x² + 2ax + b의 두 근이 {m(p)}, {m(q)}\n근과 계수: −2a/3 = {m(p + q)}, b/3 = {m(p * q)}\na = {m(c[1])}, b = {m(c[2])}", "f′(x) = 3(x − α)(x − β)")
def c3_rng(r):
    p, q, c = cub(r); lo = r.randint(p - 2, p); hi = r.randint(q, q + 2)
    xs = [lo, hi, p, q]; vals = [ev(c, x) for x in xs]; t = r.choice(["max", "min"])
    v = max(vals) if t == "max" else min(vals)
    return nf(v, f"구간 [{m(lo)}, {m(hi)}]에서 f(x) = {P(*c)}의 {'최댓값' if t == 'max' else '최솟값'}은?",
              f"후보: 양 끝과 극점\n" + ", ".join(f"f({m(x)}) = {m(val)}" for x, val in zip(xs, vals)) + f"\n{'최댓값' if t == 'max' else '최솟값'} {m(v)}", "극값과 양 끝값을 비교")
L33 = [("극값", c3_ext), ("극값으로 계수", c3_coef), ("구간에서 최대·최소", c3_rng)]

def c4_va(r):
    a, b = r.randint(-4, 4), r.randint(-5, 5); t0 = r.randint(1, 4); w = r.choice(["v", "a"])
    c = [1, a, b, 0]
    v = ev(der(c), t0); acc = ev(der(der(c)), t0)
    return nf(v if w == "v" else acc, f"수직선 위의 점의 위치가 x(t) = {P(*c).replace('x', 't')}일 때 t = {t0}에서의 {'속도' if w == 'v' else '가속도'}는?",
              f"v(t) = x′(t) = {P(*der(c)).replace('x', 't')}, a(t) = v′(t) = {P(*der(der(c))).replace('x', 't')}\nt = {t0}: {'v' if w == 'v' else 'a'} = {m(v if w == 'v' else acc)}", "위치 → 미분 → 속도 → 미분 → 가속도")
def c4_turn(r):
    p, q = sorted(r.sample(range(1, 7), 2))
    if (p + q) % 2: return None
    c = [1, -3 * (p + q) // 2, 3 * p * q, 0]
    t = r.choice(["cnt", "first"])
    if t == "cnt": return num(f"x(t) = {P(*c).replace('x', 't')} (t > 0)에서 운동 방향이 바뀌는 것은 몇 번일까요?", 2, f"v(t) = 3(t − {p})(t − {q})\nt = {p}, {q}에서 v의 부호가 바뀜 → 2번", "v(t) = 0이고 부호가 바뀌는 시각")
    return nf(p, f"x(t) = {P(*c).replace('x', 't')} (t > 0)에서 처음으로 운동 방향이 바뀌는 시각은?", f"v(t) = 3(t − {p})(t − {q}) = 0\n처음 부호가 바뀌는 시각 t = {p}", "v(t) = 0")
def c4_ball(r):
    v0 = 10 * r.randint(1, 5); T = v0 // 10; w = r.choice(["t", "h", "v"])
    if w == "t": return nf(T, f"높이가 h(t) = {v0}t − 5t²(m)인 공이 최고점에 도달하는 시각은 몇 초 후일까요?", f"v(t) = {v0} − 10t = 0 → t = {T}", "최고점에서 속도 0")
    if w == "h": return nf(5 * T * T, f"높이가 h(t) = {v0}t − 5t²(m)인 공의 최고 높이는 몇 m일까요?", f"v = {v0} − 10t = 0 → t = {T}\nh({T}) = {v0 * T} − {5 * T * T} = {5 * T * T}", "속도 0인 순간의 높이")
    return nf(v0, f"높이가 h(t) = {v0}t − 5t²(m)인 공이 땅에 닿는 순간의 속력은 초속 몇 m일까요?", f"h = 0: t = {2 * T}\nv({2 * T}) = {v0} − {20 * T} = −{v0} → 속력 {v0}", "속력 = |속도|")
def c4_rate(r):
    s, a = r.randint(1, 5), r.randint(2, 10)
    return nf(2 * a * s, f"정사각형의 한 변이 매초 {s}cm씩 늘어납니다. 한 변이 {a}cm일 때 넓이의 변화율은 매초 몇 cm²일까요?",
              f"S = x², dS/dt = 2x × dx/dt\n= 2 × {a} × {s} = {2 * a * s}", "넓이를 시간에 대해 미분하세요.")
L34 = [("속도와 가속도", c4_va), ("운동 방향이 바뀌는 시각", c4_turn), ("던진 공", c4_ball), ("변화율", c4_rate)]

# ================= ch04 적분 =================
def d1_fill(r):
    n = r.randint(1, 5); k = r.randint(1, 4)
    co = k * (n + 1)
    nm = {1: "x", 2: "x²", 3: "x³", 4: "x⁴", 5: "x⁵"}
    return fill(f"∫ {co}{nm[n]} dx = {{{{1}}}}x{sup(n + 1)} + C", [str(k)], f"∫ xⁿ dx = xⁿ⁺¹/(n + 1) + C\n{co}x{sup(n + 1)}/{n + 1} = {k if k > 1 else ''}x{sup(n + 1)}", "지수를 1 올리고 그 수로 나눕니다.")
def d1_init(r):
    c = [nz(r, -3, 3), r.randint(-4, 4), r.randint(-4, 4)]; f0 = r.randint(-5, 5); k = r.randint(-2, 3)
    v = ip(c, 0, k) + f0
    return nf(v, f"f′(x) = {P(*c)}, f(0) = {m(f0)}일 때 f({m(k)})의 값은?", f"f(x) = {ap(c)} + C, f(0) = C = {m(f0)}\nf({m(k)}) = {fm(ip(c, 0, k))}{term(f0)} = {fm(v)}", "부정적분 후 적분상수를 정하세요.")
def d1_d(r):
    c = [nz(r, -3, 3), r.randint(-4, 4), r.randint(-4, 4)]; a = r.randint(-2, 3)
    return nf(ev(c, a), f"d/dx ∫ ({P(*c)}) dx를 x = {m(a)}에서 계산한 값은?", f"미분과 적분은 서로 거꾸로 → d/dx ∫ f(x) dx = f(x)\nf({m(a)}) = {m(ev(c, a))}", "적분한 뒤 미분하면 원래 함수")
L41 = [("부정적분 공식", d1_fill), ("초깃값으로 함수 결정", d1_init), ("미분과 적분의 관계", d1_d)]

def d2_area(r):
    t = r.choice(["const", "lin", "abs"])
    if t == "const":
        c, a, b = r.randint(1, 6), r.randint(-2, 1), r.randint(2, 5)
        return nf(c * (b - a), f"∫{fsub(a)}{sup(b)} {c} dx의 값은?", f"y = {c}과 x축 사이의 직사각형 넓이\n{c} × ({b} − {par(a)}) = {c * (b - a)}", "상수함수의 정적분 = 직사각형 넓이")
    if t == "lin":
        b = r.randint(1, 6); k = r.randint(1, 3)
        return nf(F(k * b * b, 2), f"∫₀{sup(b)} {k if k > 1 else ''}x dx의 값은?", f"y = {k if k > 1 else ''}x와 x축이 만드는 삼각형\n{b} × {k * b} ÷ 2 = {fm(F(k * b * b, 2))}", "삼각형의 넓이")
    a = r.randint(1, 4)
    return nf(a * a, f"∫{fsub(-a)}{sup(a)} |x| dx의 값은?", f"두 삼각형의 넓이 합: 2 × ({a} × {a} ÷ 2) = {a * a}", "y = |x| 아래 넓이")
def d2_add(r):
    A, B = r.randint(-5, 8), r.randint(-5, 8); a, b, c = sorted(r.sample(range(-2, 6), 3))
    t = r.choice(["sum", "diff"])
    if t == "sum": return nf(A + B, f"∫{fsub(a)}{sup(b)} f(x) dx = {m(A)}, ∫{fsub(b)}{sup(c)} f(x) dx = {m(B)}일 때 ∫{fsub(a)}{sup(c)} f(x) dx의 값은?", f"구간을 이어 붙이면 더해집니다.\n{m(A)} + {par(B)} = {m(A + B)}", "∫ₐᵇ + ∫ᵇᶜ = ∫ₐᶜ")
    return nf(A + B - A, f"∫{fsub(a)}{sup(c)} f(x) dx = {m(A + B)}, ∫{fsub(a)}{sup(b)} f(x) dx = {m(A)}일 때 ∫{fsub(b)}{sup(c)} f(x) dx의 값은?", f"∫ₐᶜ = ∫ₐᵇ + ∫ᵇᶜ\n{m(A + B)} − {par(A)} = {m(B)}", "구간을 나누세요.")
def d2_odd(r):
    a = r.randint(1, 4); n = r.choice([1, 3, 5]); k = r.randint(1, 5)
    return nf(0, f"∫{fsub(-a)}{sup(a)} {k if k > 1 else ''}x{sup(n) if n > 1 else ''} dx의 값은?", f"{k if k > 1 else ''}x{sup(n) if n > 1 else ''}는 홀함수(그래프가 원점 대칭)\n양쪽 넓이가 부호만 반대 → 0", "홀함수를 대칭 구간에서 적분하면 0")
L42 = [("넓이로 구하는 정적분", d2_area), ("구간의 덧셈", d2_add), ("홀함수의 정적분", d2_odd)]

def d3_def(r):
    c = [r.randint(-2, 3), r.randint(-4, 4), r.randint(-4, 4)]; a, b = sorted(r.sample(range(-2, 4), 2))
    if c[0] == 0 and c[1] == 0: return None
    v = ip(c, a, b)
    return nf(v, f"∫{fsub(a)}{sup(b)} ({P(*c)}) dx의 값은? (기약분수 또는 정수로)", f"원시함수 F(x) = {ap(c)}\nF({m(b)}) − F({m(a)}) = {fm(ip(c, 0, b))} − {fpar(ip(c, 0, a))} = {fm(v)}", "F(b) − F(a)")
def d3_cube(r):
    c = [1, r.randint(-3, 3), r.randint(-3, 3), 0]; a, b = sorted(r.sample(range(-2, 3), 2))
    v = ip(c, a, b)
    return nf(v, f"∫{fsub(a)}{sup(b)} ({P(*c)}) dx의 값은? (기약분수 또는 정수로)", f"원시함수 F(x) = {ap(c)}\nF({m(b)}) − F({m(a)}) = {fm(v)}", "항별로 적분하세요.")
def d3_ftc(r):
    c = [nz(r, -3, 3), r.randint(-4, 4), r.randint(-4, 4)]; a = r.randint(-2, 3); lo = r.randint(-1, 2)
    t = r.choice(["d", "zero"])
    if t == "d": return nf(ev(c, a), f"f(x) = ∫{fsub(lo)}ˣ ({P(*c).replace('x', 't')}) dt일 때 f′({m(a)})의 값은?", f"미적분의 기본정리: f′(x) = {P(*c)}\nf′({m(a)}) = {m(ev(c, a))}", "d/dx ∫ₐˣ g(t) dt = g(x)")
    return nf(0, f"f(x) = ∫{fsub(lo)}ˣ ({P(*c).replace('x', 't')}) dt일 때 f({m(lo)})의 값은?", f"위끝과 아래끝이 같으면 정적분은 0\nf({m(lo)}) = ∫{fsub(lo)}{sup(lo)} … = 0", "∫ₐᵃ = 0")
L43 = [("다항함수의 정적분", d3_def), ("삼차식의 정적분", d3_cube), ("미적분의 기본정리", d3_ftc)]

def d4_par(r):
    a, b = sorted(r.sample(range(-3, 5), 2)); k = r.choice([1, -1, 2])
    v = F(abs(k) * (b - a) ** 3, 6)
    return nf(v, f"y = {'' if k == 1 else '−' if k == -1 else k}(x{term(-a)})(x{term(-b)})와 x축으로 둘러싸인 부분의 넓이는? (기약분수 또는 정수로)".replace("(x)", "x"),
              f"x절편 {m(a)}, {m(b)}\n넓이 = |∫{fsub(a)}{sup(b)} {'' if k == 1 else '−' if k == -1 else k}(x{term(-a)})(x{term(-b)}) dx| = {str(abs(k)) + '×' if abs(k) != 1 else ''}({b} − {par(a)})³/6 = {fm(v)}".replace("(x)", "x"),
              "포물선과 x축: |a|(β − α)³/6")
def d4_line(r):
    a, b = sorted(r.sample(range(-3, 5), 2))
    s, c = a + b, -a * b
    v = F((b - a) ** 3, 6)
    return nf(v, f"y = x²과 y = {poly((s, 'x'), (c, ''))}로 둘러싸인 부분의 넓이는? (기약분수 또는 정수로)",
              f"교점: x² = {poly((s, 'x'), (c, ''))} → (x{term(-a)})(x{term(-b)}) = 0 → x = {m(a)}, {m(b)}\n넓이 = ∫{fsub(a)}{sup(b)} (직선 − 포물선) dx = ({b} − {par(a)})³/6 = {fm(v)}", "위 − 아래를 적분")
def d4_dist(r):
    c = r.randint(1, 4); T = r.randint(c + 1, c + 4); w = r.choice(["disp", "dist"])
    disp = F(T * T, 2) - c * T; dist = F(c * c, 2) + F((T - c) ** 2, 2)
    v = disp if w == "disp" else dist
    return nf(v, f"속도가 v(t) = t − {c}일 때 t = 0부터 t = {T}까지 {'위치의 변화' if w == 'disp' else '움직인 거리'}는? (기약분수 또는 정수로)",
              (f"위치의 변화 = ∫₀{sup(T)} (t − {c}) dt = {fm(disp)}" if w == "disp" else f"움직인 거리 = ∫₀{sup(T)} |t − {c}| dt\n= {fm(F(c * c, 2))} + {fm(F((T - c) ** 2, 2))} = {fm(dist)}"),
              "위치 변화는 ∫v, 거리는 ∫|v|")
L44 = [("포물선과 x축", d4_par), ("포물선과 직선", d4_line), ("속도와 거리", d4_dist)]

ALL = {"ch01": [L11, L12, L13, L14], "ch02": [L21, L22, L23, L24], "ch03": [L31, L32, L33, L34], "ch04": [L41, L42, L43, L44]}

if __name__ == "__main__":
    tot = 0
    for ch, Ls in ALL.items():
        for i, T in enumerate(Ls, 1):
            per = {2: 20, 3: 14, 4: 10, 5: 8}.get(len(T), 6)
            n = write("c4", ch, f"l0{i}", T, per=per, seed=7 + i); tot += n; print(ch, i, len(T), n)
    print("total", tot)
