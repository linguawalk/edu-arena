"""코스 4 · 챕터 5~8 (수열의 극한과 급수, 여러 가지 함수의 미분, 미분법의 활용, 여러 가지 적분법) — 연습 문제 은행"""
from core import *
from c4_a import P, nf, nz, ev, der, fsub, fx
import math

def ek(k):
    """e^(kx) 표기"""
    return "eˣ" if k == 1 else f"e^({poly((k, 'x'))})"
def dx(j): return "x" if j == 1 else f"({j}x)"
def tf(fn, k): return f"{fn} {poly((k, 'x'))}" if k > 0 else f"{fn}({poly((k, 'x'))})"
def frac_s(v): return fs(v) if F(v).denominator == 1 else f"({fs(v)})"

# ================= ch05 수열의 극한과 급수 =================
def e1_rat(r):
    p, q = nz(r, -6, 6), nz(r, -5, 5); d1, d2 = r.choice([(1, 1), (2, 2), (1, 2), (2, 1)])
    nm = {1: "n", 2: "n²"}
    b, c = r.randint(-5, 5), r.randint(-5, 5)
    if d1 > d2:
        return num(f"수열 ({poly((p, nm[d1]), (b, ''))})/({poly((q, nm[d2]), (c, ''))})은 수렴할까요?  (그렇다 1, 아니다 0)", 0,
                   f"분자의 차수({d1})가 분모의 차수({d2})보다 큽니다.\n분자·분모를 n으로 나누면 분자만 n에 비례해 커지므로 발산합니다 → 0", "차수 비교")
    v = F(p, q) if d1 == d2 else F(0)
    return nf(v, f"lim(n→∞) ({poly((p, nm[d1]), (b, ''))})/({poly((q, nm[d2]), (c, ''))})의 값은? (기약분수 또는 정수로)",
              f"분자 {d1}차, 분모 {d2}차\n" + (f"차수가 같으면 최고차항의 계수의 비: {m(p)} ÷ {par(q)} = {fm(v)}" if d1 == d2 else "분모의 차수가 더 크므로 0으로 수렴합니다."), "최고차항끼리 비교")
def e1_root(r):
    a = nz(r, -8, 8)
    return nf(F(a, 2), f"lim(n→∞) (√(n²{term(a, 'n')}) − n)의 값은? (기약분수 또는 정수로)",
              f"분자를 유리화: (√(n²{term(a, 'n')}) − n)(√(n²{term(a, 'n')}) + n) = {poly((a, 'n'))}\n극한 = lim {poly((a, 'n'))}/(√(n²{term(a, 'n')}) + n) = {m(a)}/(1 + 1) = {fm(F(a, 2))}", "∞ − ∞ 꼴은 유리화")
def e1_alg(r):
    A, B, p, q = r.randint(-5, 6), nz(r, -5, 6), nz(r, -3, 3), nz(r, -3, 3)
    t = r.choice(["lin", "div"])
    if t == "lin": return nf(p * A + q * B, f"lim aₙ = {m(A)}, lim bₙ = {m(B)}일 때 lim ({poly((p, 'aₙ'), (q, 'bₙ'))})의 값은?", f"수렴하는 수열의 극한은 나누어 계산할 수 있습니다.\n{m(p)}×{par(A)} + {par(q)}×{par(B)} = {m(p * A + q * B)}", "극한의 성질")
    return nf(F(A, B), f"lim aₙ = {m(A)}, lim bₙ = {m(B)}일 때 lim aₙ/bₙ의 값은? (기약분수 또는 정수로)", f"분모의 극한이 0이 아니므로 극한의 몫으로 계산합니다.\n{m(A)} ÷ {par(B)} = {fm(F(A, B))}", "lim bₙ ≠ 0일 때 몫의 극한")
L51 = [("유리식의 극한", e1_rat), ("∞ − ∞ 꼴", e1_root), ("극한의 성질", e1_alg)]

def e2_ratio(r):
    p, q = r.sample([2, 3, 4, 5], 2); a, b = r.choice([1, 2, 3]), r.choice([1, 2])
    big = max(p, q)
    # (a·pⁿ⁺¹ + qⁿ)/(b·pⁿ − 1)
    v = F(a * p, b) if p > q else 0
    if p < q: return None
    return nf(v, f"lim(n→∞) ({str(a) + ' × ' if a > 1 else ''}{p}ⁿ⁺¹ + {q}ⁿ)/({str(b) + ' × ' if b > 1 else ''}{p}ⁿ − 1)의 값은? (기약분수 또는 정수로)",
              f"분자·분모를 {p}ⁿ으로 나눕니다.\n({a * p} + ({q}/{p})ⁿ)/({b} − (1/{p})ⁿ)\n|{q}/{p}| < 1이므로 ({q}/{p})ⁿ → 0, (1/{p})ⁿ → 0 → {a * p}" + (f"/{b} = {fm(v)}" if b > 1 else ""), "밑이 가장 큰 거듭제곱으로 나누세요.")
def e2_two(r):
    p, q = r.sample([2, 3, 4, 5, 6], 2); t = r.choice(["small", "big"])
    v = 0 if p < q else 1
    return nf(v, f"lim(n→∞) {p}ⁿ/({p}ⁿ + {q}ⁿ)의 값은?",
              f"분자·분모를 {max(p, q)}ⁿ으로 나누면\n" + (f"({p}/{q})ⁿ/(({p}/{q})ⁿ + 1) → 0/(0 + 1) = 0" if p < q else f"1/(1 + ({q}/{p})ⁿ) → 1/(1 + 0) = 1"), "더 큰 밑으로 나누세요.")
def e2_conv(r):
    c, k = r.randint(-3, 3), r.choice([1, 2, 3, 4])
    # ((x − c)/k)ⁿ 수렴 ⇔ −k < x − c ≤ k
    base = f"(x{term(-c)})ⁿ" if k == 1 else f"((x{term(-c)})/{k})ⁿ"
    return nf(2 * k, f"수열 {base.replace('(x)', 'x')}이 수렴하는 정수 x는 몇 개일까요?",
              f"등비수열 rⁿ이 수렴 ⇔ −1 < r ≤ 1\n−1 < (x{term(-c)})/{k} ≤ 1 → {m(c - k)} < x ≤ {m(c + k)}\n정수 {2 * k}개".replace("/1 ", " ").replace("(x)", "x"), "−1 < r ≤ 1")
L52 = [("지수꼴 분수의 극한", e2_ratio), ("두 거듭제곱의 비", e2_two), ("수렴 조건", e2_conv)]

def e3_tele(r):
    k = r.choice([1, 2, 3]); t = r.choice(["k", "odd", "shift", "shift"])
    if t == "shift":
        a, c = r.randint(1, 8), r.randint(1, 3)
        v = F(1, c * (a + 1)) if False else F(1, a + 1)
        return nf(v, f"Σ(n=1~∞) 1/((n + {a})(n + {a + 1}))의 합은? (기약분수로)",
                  f"1/((n + {a})(n + {a + 1})) = 1/(n + {a}) − 1/(n + {a + 1})\n부분합 = 1/{a + 1} − 1/(n + {a + 1}) → 1/{a + 1}", "부분분수로 나누면 연쇄적으로 지워집니다.")
    if t == "odd":
        return nf(F(1, 2), "Σ(n=1~∞) 1/((2n − 1)(2n + 1))의 합은? (기약분수로)", "1/((2n − 1)(2n + 1)) = (1/2)(1/(2n − 1) − 1/(2n + 1))\n부분합 Sₙ = (1/2)(1 − 1/(2n + 1)) → 1/2", "부분분수 분해 후 부분합의 극한")
    v = F(1, k) * sum(F(1, i) for i in range(1, k + 1))
    return nf(v, f"Σ(n=1~∞) 1/(n(n + {k}))의 합은? (기약분수 또는 정수로)".replace("n + 1))", "n + 1))"),
              f"1/(n(n + {k})) = (1/{k})(1/n − 1/(n + {k}))\n앞의 {k}개 항 1, …, 1/{k}만 남습니다.\n합 = (1/{k})({' + '.join('1/' + str(i) if i > 1 else '1' for i in range(1, k + 1))}) = {fm(v)}".replace("(1/1)", ""), "부분분수로 지워지는 항을 찾으세요.")
def e3_Sn(r):
    a, b, c = r.randint(1, 6), r.randint(1, 4), r.randint(-3, 3)
    t = r.choice(["sum", "a1"])
    if t == "sum": return nf(F(a, b), f"부분합이 Sₙ = {a if a > 1 else ''}n/({b if b > 1 else ''}n{term(c)})인 급수의 합은? (기약분수 또는 정수로)".replace("(n)", "n"), f"급수의 합은 부분합의 극한입니다.\nlim Sₙ = (n의 계수의 비) {a}/{b}" + (f" = {fm(F(a, b))}" if gcd(a, b) > 1 else ""), "급수의 합은 부분합의 극한")
    if b + c == 0: return None
    return nf(F(a, b + c), f"부분합이 Sₙ = {a if a > 1 else ''}n/({b if b > 1 else ''}n{term(c)})인 급수의 첫째항은? (기약분수 또는 정수로)", f"a₁ = S₁ = {a}/({b}{term(c)}) = {fm(F(a, b + c))}", "a₁ = S₁")
def e3_term(r):
    c = r.randint(-6, 8); k = nz(r, -3, 4)
    return nf(F(c, k), f"Σ({poly((k, 'aₙ'), (-c, ''))})가 수렴할 때 lim aₙ의 값은? (기약분수 또는 정수로)",
              f"급수가 수렴하면 일반항은 0으로 수렴합니다.\nlim ({poly((k, 'aₙ'), (-c, ''))}) = 0 → lim aₙ = {fm(F(c, k))}", "Σbₙ 수렴 ⇒ lim bₙ = 0")
L53 = [("부분분수 급수", e3_tele), ("부분합", e3_Sn), ("일반항의 극한", e3_term)]

def e4_sum(r):
    a, rr = r.choice([1, 2, 3, 4, 6, 8, 9]), r.choice([F(1, 2), F(1, 3), F(2, 3), F(-1, 2), F(1, 4), F(3, 4), F(-1, 3)])
    v = a / (1 - rr)
    return nf(v, f"첫째항이 {a}, 공비가 {fm(rr)}인 등비급수의 합은? (기약분수 또는 정수로)", f"|r| < 1이므로 수렴하고, 합 = a/(1 − r) = {a}/(1 − {fpar(rr)}) = {a}/{frac_s(1 - rr)} = {fm(v)}", "a/(1 − r)")
def e4_dec(r):
    t = r.choice(["1", "2"])
    if t == "1":
        d = r.randint(1, 8); v = F(d, 9)
        return nf(v, f"0.{d}{d}{d}…을 기약분수로 나타내면?", f"0.{d} + 0.0{d} + … = 첫째항 {d}/10, 공비 1/10인 등비급수\n합 = ({d}/10)/(1 − 1/10) = {d}/9" + (f" = {fs(v)}" if v.denominator != 9 else ""), "순환소수 = 등비급수")
    d = r.randint(1, 98)
    if d % 11 == 0: return None
    s = f"{d:02d}"; v = F(d, 99)
    return nf(v, f"0.{s}{s}…({s}{'이' if bat(d) else '가'} 반복)를 기약분수로 나타내면?", f"첫째항 {d}/100, 공비 1/100\n합 = ({d}/100)/(1 − 1/100) = {d}/99" + (f" = {fs(v)}" if v.denominator != 99 else ""), "순환소수 = 등비급수")
def e4_ball(r):
    h, rr = r.choice([10, 12, 20, 6, 8, 15]), r.choice([F(1, 2), F(1, 3), F(2, 3), F(3, 4)])
    v = h + 2 * h * rr / (1 - rr)
    return nf(v, f"{h}m 높이에서 떨어뜨린 공이 매번 떨어진 높이의 {fm(rr)}만큼 튀어 오릅니다. 멈출 때까지 움직인 거리는 몇 m일까요? (기약분수 또는 정수로)",
              f"처음 {h}m 낙하 + (오르고 내리기) 2 × ({h}×{fm(rr)} + {h}×{fm(rr)}² + …)\n= {h} + 2 × {fm(h * rr)}/(1 − {fm(rr)}) = {fm(v)}", "튀어 오른 거리는 두 번(위·아래) 셉니다.")
def e4_conv(r):
    c, k = r.randint(-3, 3), r.choice([1, 2, 3, 4])
    return nf(2 * k - 1, f"Σ(n=1~∞) ((x{term(-c)})/{k})ⁿ이 수렴하는 정수 x는 몇 개일까요?".replace("/1)", ")").replace("((x)", "(x"),
              f"등비급수는 |r| < 1일 때만 수렴\n|x{term(-c)}| < {k} → {m(c - k)} < x < {m(c + k)}\n정수 {2 * k - 1}개".replace("(x)", "x"), "등비급수 수렴 ⇔ −1 < r < 1 (등비수열과 달리 r = 1 제외)")
L54 = [("등비급수의 합", e4_sum), ("순환소수", e4_dec), ("튀는 공", e4_ball), ("수렴 조건", e4_conv)]

# ================= ch06 여러 가지 함수의 미분 =================
def f1_lim(r):
    k, j_ = nz(r, -5, 6), r.choice([1, 2, 3])
    t = r.choice(["e", "ln"])
    v = F(k, j_)
    if t == "e": return nf(v, f"lim(x→0) ({ek(k)} − 1)/{dx(j_)}의 값은? (기약분수 또는 정수로)",
                           f"lim(t→0) (eᵗ − 1)/t = 1 을 이용\n{poly((k, 'x'))} = t로 놓으면 (eᵗ − 1)/t × {fm(v)} → {fm(v)}", "(eᵗ − 1)/t → 1")
    return nf(v, f"lim(x→0) ln(1 {'+' if k > 0 else '−'} {abs(k) if abs(k) != 1 else ''}x)/{dx(j_)}의 값은? (기약분수 또는 정수로)",
              f"lim(t→0) ln(1 + t)/t = 1 을 이용\nt = {poly((k, 'x'))}로 놓으면 ln(1 + t)/t × {fm(v)} → {fm(v)}", "ln(1 + t)/t → 1")
def f1_der(r):
    t = r.choice(["ae", "ln", "lnx2", "xe"])
    if t == "ae":
        a, k = nz(r, -4, 5), nz(r, -3, 3)
        return nf(a * k, f"f(x) = {'' if a == 1 else '−' if a == -1 else a}{ek(k)}일 때 f′(0)의 값은?",
                  f"(e^(kx))′ = ke^(kx)\nf′(x) = {m(a * k)}{ek(k)} → f′(0) = {m(a * k)} × e⁰ = {m(a * k)}", "e^(kx)를 미분하면 k가 앞으로")
    if t == "ln":
        c, a = r.randint(1, 9), r.randint(1, 9)
        return nf(F(1, a), f"f(x) = ln {c if c > 1 else ''}x일 때 f′({a})의 값은? (기약분수로)".replace("ln x", "ln x"), f"ln {c}x = ln {c} + ln x → f′(x) = 1/x\nf′({a}) = {fs(F(1, a))}" if c > 1 else f"(ln x)′ = 1/x → f′({a}) = 1/{a}", "(ln x)′ = 1/x")
    if t == "lnx2":
        n, a = r.randint(2, 5), r.randint(1, 6)
        return nf(F(n, a), f"f(x) = ln x{sup(n)} (x > 0)일 때 f′({a})의 값은? (기약분수 또는 정수로)", f"ln x{sup(n)} = {n} ln x → f′(x) = {n}/x\nf′({a}) = {fm(F(n, a))}", "로그의 성질로 지수를 앞으로")
    k = nz(r, -3, 3); a = r.randint(0, 0)
    return nf(1, f"f(x) = x{ek(k)}일 때 f′(0)의 값은?", f"곱의 미분: f′ = {ek(k)} + x × {m(k)}{ek(k)}\nx = 0: 1 + 0 = 1", "(fg)′ = f′g + fg′")
L61 = [("e와 ln의 극한", f1_lim), ("지수·로그함수의 미분", f1_der)]

def f2_lim(r):
    a, b = nz(r, -6, 6), r.choice([1, 2, 3, 4, 5])
    t = r.choice(["sin", "tan", "cos"])
    if t == "cos":
        a = r.randint(1, 4); v = F(a * a, 2)
        return nf(v, f"lim(x→0) (1 − cos {a if a > 1 else ''}x)/x²의 값은? (기약분수 또는 정수로)", f"1 − cos θ = 2sin²(θ/2) 이용\n= 2sin²({fs(F(a, 2))}x)/x² → 2 × ({fs(F(a, 2))})² = {fm(v)}", "1 − cos θ = 2 sin²(θ/2)")
    v = F(a, b)
    return nf(v, f"lim(x→0) {tf(t, a)}/{dx(b)}의 값은? (기약분수 또는 정수로)",
              f"lim(θ→0) {t} θ/θ = 1\n{t} ({poly((a, 'x'))})/({poly((a, 'x'))}) × {fm(v)} → {fm(v)}", f"{t} θ/θ → 1")
def f2_der(r):
    a, b = r.randint(-4, 5), r.randint(-4, 5)
    if a == 0 and b == 0: return None
    pts = [("0", 0), ("π/2", math.pi / 2), ("π", math.pi), ("π/3", math.pi / 3), ("π/6", math.pi / 6)]
    nm, x = r.choice(pts)
    v = a * math.cos(x) - b * math.sin(x)
    if abs(v - round(v)) > 1e-9: return None
    v = round(v)
    return nf(v, f"f(x) = {poly((a, 'sin x'), (b, 'cos x'))}일 때 f′({nm})의 값은?",
              f"(sin x)′ = cos x, (cos x)′ = −sin x\nf′(x) = {poly((a, 'cos x'), (-b, 'sin x'))}\nf′({nm}) = {m(v)}", "sin → cos, cos → −sin")
def f2_add(r):
    A, B = r.choice([(45, 30), (60, 45), (45, 45), (30, 60), (60, 30), (90, 30)])
    fn = r.choice(["sin", "cos"]); sg = r.choice(["+", "−"])
    ang = A + B if sg == "+" else A - B
    v = getattr(math, fn)(math.radians(ang))
    tbl = {0: "0", .5: "1/2", -.5: "−1/2", 1: "1", -1: "−1"}
    txt = tbl.get(round(v, 6))
    if txt is None: return None
    return num(f"{fn}({A}° {sg} {B}°)의 값은? (기약분수 또는 정수로)", F(txt.replace("−", "-")),
               f"덧셈정리: {'sin(α ± β) = sin α cos β ± cos α sin β' if fn == 'sin' else 'cos(α ± β) = cos α cos β ∓ sin α sin β'}\n{fn}({ang}°) = {txt}", "덧셈정리 또는 각을 합쳐 계산", fmt="fraction" if "/" in txt else "integer")
L62 = [("삼각함수의 극한", f2_lim), ("삼각함수의 미분", f2_der), ("덧셈정리", f2_add)]

def f3_chain(r):
    t = r.choice(["pow", "e", "sin", "ln", "inv", "sqrt", "quot"])
    if t == "pow":
        a, b, n = nz(r, -3, 3), nz(r, -3, 3), r.randint(2, 5)
        return nf(n * a * b ** (n - 1), f"f(x) = ({poly((a, 'x'), (b, ''))}){sup(n)}일 때 f′(0)의 값은?", f"합성함수의 미분: f′(x) = {n}({poly((a, 'x'), (b, ''))}){sup(n - 1) if n > 2 else ''} × {m(a)}\nf′(0) = {n} × {par(b)}{sup(n - 1) if n > 2 else ''} × {par(a)} = {m(n * a * b ** (n - 1))}", "겉미분 × 속미분")
    if t == "e":
        k, c = nz(r, -4, 4), r.randint(1, 3)
        return nf(k * c, f"f(x) = {c if c > 1 else ''}{ek(k)}일 때 f′(0)의 값은?", f"f′(x) = {c if c > 1 else ''}{ek(k)} × {par(k)}\nf′(0) = {m(k * c)}", "e^(g(x))′ = e^(g(x)) g′(x)")
    if t == "sin":
        k = nz(r, -5, 5); fn = r.choice(["sin", "tan"])
        return nf(k, f"f(x) = {tf(fn, k)}일 때 f′(0)의 값은?",
                  f"f′(x) = {m(k)} × {'cos' if fn == 'sin' else 'sec²'}({m(k)}x)\nf′(0) = {m(k)} × 1 = {m(k)}", "속미분이 앞으로")
    if t == "ln":
        c, a = r.randint(1, 9), nz(r, -3, 3)
        v = F(2 * a, a * a + c)
        return nf(v, f"f(x) = ln(x² + {c})일 때 f′({m(a)})의 값은? (기약분수 또는 정수로)", f"(ln g)′ = g′/g → f′(x) = 2x/(x² + {c})\nf′({m(a)}) = {m(2 * a)}/{a * a + c} = {fm(v)}", "(ln g(x))′ = g′(x)/g(x)")
    if t == "inv":
        c, a = r.randint(-3, 3), r.randint(0, 4)
        if a + c == 0: return None
        v = F(-1, (a + c) ** 2)
        return nf(v, f"f(x) = 1/(x{term(c)})일 때 f′({a})의 값은? (기약분수 또는 정수로)".replace("(x)", "x"), f"f′(x) = −1/(x{term(c)})²\nf′({a}) = −1/{(a + c) ** 2} = {fm(v)}".replace("(x)", "x"), "(1/g)′ = −g′/g²")
    if t == "sqrt":
        a = r.randint(1, 8)
        return nf(F(1, 2 * a), f"f(x) = √x일 때 f′({a * a})의 값은? (기약분수로)", f"f′(x) = 1/(2√x)\nf′({a * a}) = 1/(2 × {a}) = {fs(F(1, 2 * a))}", "(√x)′ = 1/(2√x)")
    a, b = nz(r, -3, 3), r.randint(1, 4)
    v = F(b, b * b)
    return nf(F(1, b), f"f(x) = x/(x + {b})일 때 f′(0)의 값은? (기약분수로)", f"몫의 미분: f′ = ((x + {b}) − x)/(x + {b})² = {b}/(x + {b})²\nf′(0) = {b}/{b * b} = {fs(F(1, b))}", "(f/g)′ = (f′g − fg′)/g²")
L63 = [("몫과 합성함수의 미분", f3_chain), ("곱과 합성", lambda r: f3_chain(r)), ("거듭제곱의 미분", lambda r: f3_chain(r))]
L63 = [("합성·몫의 미분", f3_chain)]

def f4_par(r):
    p, q = r.sample([1, 2, 3, 4], 2); a, b = r.randint(1, 3), r.randint(1, 3)
    t0 = r.choice([1, 2])
    v = F(b * q * t0 ** (q - 1), a * p * t0 ** (p - 1))
    tp = lambda c, e: f"{c if c > 1 else ''}t{sup(e) if e > 1 else ''}"
    return nf(v, f"x = {tp(a, p)}, y = {tp(b, q)}일 때 t = {t0}에서 dy/dx의 값은? (기약분수 또는 정수로)",
              f"dy/dx = (dy/dt)/(dx/dt) = {b * q if b * q > 1 else ''}t{sup(q - 1) if q > 2 else '' if q == 2 else '⁰'}/({a * p if a * p > 1 else ''}t{sup(p - 1) if p > 2 else '' if p == 2 else '⁰'})\nt = {t0}: {b * q * t0 ** (q - 1)}/{a * p * t0 ** (p - 1)} = {fm(v)}".replace("t⁰", "1"), "dy/dx = (dy/dt) ÷ (dx/dt)")
def f4_imp(r):
    t = r.choice(["circle", "hyp", "mixed"])
    if t == "circle":
        a, b, c = r.choice([(3, 4, 5), (4, 3, 5), (5, 12, 13), (6, 8, 10), (8, 6, 10)]); sx, sy = r.choice([1, -1]), r.choice([1, -1])
        x, y = sx * a, sy * b
        return nf(F(-x, y), f"x² + y² = {c * c} 위의 점 ({m(x)}, {m(y)})에서 dy/dx의 값은? (기약분수 또는 정수로)", f"양변을 x로 미분: 2x + 2y(dy/dx) = 0 → dy/dx = −x/y\n= −({m(x)})/({m(y)}) = {fm(F(-x, y))}", "음함수 미분: y는 x의 함수")
    if t == "hyp":
        x, y = nz(r, -5, 5), nz(r, -5, 5)
        return nf(F(-y, x), f"xy = {m(x * y)} 위의 점 ({m(x)}, {m(y)})에서 dy/dx의 값은? (기약분수 또는 정수로)", f"곱의 미분: y + x(dy/dx) = 0 → dy/dx = −y/x\n= {fm(F(-y, x))}", "양변을 x로 미분")
    x, y = r.choice([(1, 2), (2, 1), (1, 1), (1, -2), (2, -1), (3, 1)])
    c = x * x + x * y + y * y
    if x + 2 * y == 0: return None
    v = F(-(2 * x + y), x + 2 * y)
    return nf(v, f"x² + xy + y² = {c} 위의 점 ({m(x)}, {m(y)})에서 dy/dx의 값은? (기약분수 또는 정수로)", f"2x + y + xy′ + 2yy′ = 0 → y′ = −(2x + y)/(x + 2y)\n= −({m(2 * x + y)})/({m(x + 2 * y)}) = {fm(v)}", "모든 항을 x로 미분")
def f4_inv(r):
    a, b = r.randint(1, 3), r.randint(1, 4); x0 = r.randint(0, 2)
    c = [1, 0, b, 0] if a == 1 else [a, 0, b, 0]
    y0 = ev(c, x0); d = ev(der(c), x0)
    return nf(F(1, d), f"f(x) = {P(*c)}의 역함수를 g라 할 때 g′({y0})의 값은? (기약분수로)", f"f({x0}) = {y0}이므로 g({y0}) = {x0}\ng′({y0}) = 1/f′({x0}) = 1/{d}", "g′(b) = 1/f′(a) (f(a) = b)", )
L64 = [("매개변수 미분", f4_par), ("음함수 미분", f4_imp), ("역함수의 미분", f4_inv)]

# ================= ch07 미분법의 활용 =================
def g1_sec(r):
    c = [r.randint(-2, 3), r.randint(-4, 4), r.randint(-4, 4), r.randint(-4, 4), r.randint(-3, 3)]
    if c[0] == 0 and c[1] == 0: return None
    a = r.randint(-2, 2); d2 = der(der(c))
    return nf(ev(d2, a), f"f(x) = {P(*c)}일 때 f″({m(a)})의 값은?", f"f′(x) = {P(*der(c))}\nf″(x) = {P(*d2)}\nf″({m(a)}) = {m(ev(d2, a))}", "두 번 미분하세요.")
def g1_test(r):
    p, q = sorted(r.sample(range(-4, 5), 2))
    if (p + q) % 2: return None
    c = [1, -3 * (p + q) // 2, 3 * p * q, r.randint(-3, 3)]; x0 = r.choice([p, q])
    v = 1 if x0 == q else 0
    return num(f"f(x) = {P(*c)}는 x = {m(x0)}에서 극소일까요?  (그렇다 1, 아니다 0)", v,
               f"f′({m(x0)}) = 0, f″(x) = {P(*der(der(c)))}\nf″({m(x0)}) = {m(ev(der(der(c)), x0))} {'> 0 → 극소' if v else '< 0 → 극대'}", "이계도함수 판정법")
L71 = [("이계도함수", g1_sec), ("이계도함수 판정법", g1_test)]

def g2_infl(r):
    b = 3 * nz(r, -2, 2); cc, d = r.randint(-4, 4), r.randint(-4, 4)
    c = [1, b, cc, d]; x0 = F(-b, 3)
    ask = r.choice(["x", "y"])
    v = x0 if ask == "x" else F(ev(c, int(x0)))
    return nf(v, f"y = {P(*c)}의 변곡점의 {ask}좌표는?", f"y″ = 6x{term(2 * b)} = 0 → x = {m(int(x0))}\n(부호가 바뀌므로 변곡점) y = {m(ev(c, int(x0)))}", "y″ = 0이고 부호가 바뀌는 점")
def g2_cnt(r):
    p = r.choice([-6, -4, -2, -3, 0, 2, 4, 6])
    v = 2 if p < 0 else 0
    return nf(v, f"y = x⁴{term(p, 'x²')}의 변곡점은 몇 개일까요?", f"y″ = 12x²{term(2 * p)}\n" + (f"12x² = {m(-2 * p)} → 부호가 바뀌는 점 2개" if p < 0 else "y″ ≥ 0이고 부호가 바뀌지 않으므로 변곡점 없음"), "y″의 부호 변화")
def g2_coef(r):
    k, yk = r.randint(-2, 3), r.randint(-4, 4)
    a = -3 * k
    b = yk - k ** 3 - a * k * k - 1
    b = F(b, k) if k else None
    if b is None or b.denominator != 1: return None
    ask = r.choice(["a", "b"])
    return nf(a if ask == "a" else int(b), f"y = x³ + ax² + bx + 1의 변곡점이 ({m(k)}, {m(yk)})일 때 {ask}의 값은?",
              f"y″ = 6x + 2a = 0, x = {m(k)} → a = {m(a)}\n점 대입: {m(k ** 3)}{term(a * k * k)}{term(k, 'b')} + 1 = {m(yk)} → b = {m(int(b))}", "y″(k) = 0과 점 대입")
L72 = [("변곡점", g2_infl), ("변곡점의 개수", g2_cnt), ("변곡점으로 계수", g2_coef)]

def g3_roots(r):
    a = r.randint(1, 3)
    t = r.choice(["cnt", "eq"])
    M = 2 * a ** 3
    if t == "cnt": return nf(2 * M - 1, f"x³ − {3 * a * a}x = k가 서로 다른 세 실근을 갖는 정수 k는 몇 개일까요?",
                             f"f(x) = x³ − {3 * a * a}x의 극댓값 f(−{a}) = {M}, 극솟값 f({a}) = −{M}\ny = k가 세 점에서 만나려면 −{M} < k < {M} → 정수 {2 * M - 1}개", "극댓값과 극솟값 사이")
    k = r.choice([M, -M, 0, M + 1, M - 1])
    v = 2 if abs(k) == M else 3 if abs(k) < M else 1
    return nf(v, f"x³ − {3 * a * a}x{term(-k)} = 0의 서로 다른 실근은 몇 개일까요?", f"x³ − {3 * a * a}x = {m(k)}로 보고 극값 ±{M}과 비교\n" + ("극값과 같으면 접하므로 2개" if v == 2 else "극값 사이면 3개" if v == 3 else "극값 바깥이면 1개"), "그래프와 수평선의 교점")
def g3_amgm(r):
    c = r.randint(1, 6); s = r.randint(1, 3)
    return nf(2 * c * s if False else 2 * c, f"x > 0에서 y = x + {c * c}/x의 극솟값은?", f"y′ = 1 − {c * c}/x² = 0 → x = {c}\ny({c}) = {c} + {c} = {2 * c}", "y′ = 0")
def g3_ext(r):
    p, q = sorted(r.sample(range(-3, 4), 2))
    if (p + q) % 2: return None
    c = [1, -3 * (p + q) // 2, 3 * p * q, r.randint(-5, 5)]
    t = r.choice(["diff", "cnt"])
    if t == "cnt": return num(f"y = {P(*c)}의 극값은 모두 몇 개일까요?", 2, f"y′ = 3{fx(p)}{fx(q)} = 0의 서로 다른 두 근에서 부호가 바뀜 → 2개", "y′의 부호 변화")
    return nf(ev(c, p) - ev(c, q), f"y = {P(*c)}의 극댓값과 극솟값의 차는?", f"극대 x = {m(p)}: {m(ev(c, p))}, 극소 x = {m(q)}: {m(ev(c, q))}\n차 {m(ev(c, p) - ev(c, q))}", "두 극값을 구해 빼세요.")
L73 = [("방정식의 실근 개수", g3_roots), ("분수함수의 극값", g3_amgm), ("삼차함수의 극값", g3_ext)]

TRI = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (4, 3, 5), (12, 5, 13)]
def g4_lin(r):
    a, b, c = r.choice(TRI); T = r.randint(1, 5)
    t = r.choice(["speed", "dist"])
    if t == "speed": return nf(c, f"x = {a}t, y = {b}t로 움직이는 점의 속력은?", f"속도 (dx/dt, dy/dt) = ({a}, {b})\n속력 = √({a}² + {b}²) = {c}", "속력 = √((dx/dt)² + (dy/dt)²)")
    return nf(c * T, f"x = {a}t, y = {b}t일 때 t = 0부터 t = {T}까지 움직인 거리는?", f"속력이 {c}로 일정 → 거리 = {c} × {T} = {c * T}", "∫ 속력 dt")
def g4_circ(r):
    R, w = r.randint(1, 6), r.choice([1, 2, 3])
    t = r.choice(["speed", "acc", "len"])
    arg = "t" if w == 1 else f"{w}t"
    if t == "speed": return nf(R * w, f"x = {R if R > 1 else ''}cos {arg}, y = {R if R > 1 else ''}sin {arg}로 움직이는 점의 속력은?", f"dx/dt = −{R * w} sin {arg}, dy/dt = {R * w} cos {arg}\n속력 = √({R * w}²(sin² + cos²)) = {R * w}", "sin² + cos² = 1")
    if t == "acc": return nf(R * w * w, f"x = {R if R > 1 else ''}cos {arg}, y = {R if R > 1 else ''}sin {arg}로 움직이는 점의 가속도의 크기는?", f"가속도 = (−{R * w * w} cos {arg}, −{R * w * w} sin {arg})\n크기 {R * w * w}", "두 번 미분")
    return fill(f"x = {R if R > 1 else ''}cos t, y = {R if R > 1 else ''}sin t일 때 t = 0부터 2π까지 움직인 거리는 {{{{1}}}}π", [str(2 * R)], f"속력 {R}로 2π 동안 → 거리 {R} × 2π = {2 * R}π (원 둘레)", "속력 × 시간")
def g4_par(r):
    p, q, c = r.choice([(4, 3, 5), (6, 8, 10), (12, 5, 13), (8, 6, 10), (8, 15, 17), (12, 9, 15), (16, 12, 20), (24, 7, 25)])
    opts = [(a, t0) for a in (1, 2, 3, 4) for t0 in (1, 2, 3) if 2 * a * t0 == p]
    if not opts: return None
    a, t0 = r.choice(opts); b = q
    vx, vy = p, q; s = c * c
    return nf(isqrt(s), f"x = {a if a > 1 else ''}t², y = {b if b > 1 else ''}t일 때 t = {t0}에서의 속력은?", f"dx/dt = {2 * a}t = {vx}, dy/dt = {b}\n속력 = √({vx}² + {vy}²) = {isqrt(s)}", "속도의 크기")
L74 = [("직선 운동", g4_lin), ("원운동", g4_circ), ("포물선 운동", g4_par)]

# ================= ch08 여러 가지 적분법 =================
def h1_lin(r):
    a, b, n = r.choice([1, 2, 3]), r.randint(-2, 3), r.randint(2, 3)
    v = F((a + b) ** (n + 1) - b ** (n + 1), a * (n + 1))
    return nf(v, f"∫₀¹ ({poly((a, 'x'), (b, ''))}){sup(n)} dx의 값은? (기약분수 또는 정수로)",
              f"t = {poly((a, 'x'), (b, ''))}로 치환: dt = {a}dx, t: {m(b)} → {m(a + b)}\n(1/{a}) × [t{sup(n + 1)}/{n + 1}] = ({par(a + b)}{sup(n + 1)} − {par(b)}{sup(n + 1)})/{a * (n + 1)} = {fm(v)}".replace("(1/1) × ", ""), "일차식 치환")
def h1_fill(r):
    t = r.choice(["e", "cos", "pow", "ln"])
    k = r.randint(2, 6)
    if t == "e": return fill(f"∫ e^({k}x) dx = (1/{{{{1}}}})e^({k}x) + C", [str(k)], f"t = {k}x, dx = dt/{k}\n∫ eᵗ dt/{k} = (1/{k})e^({k}x) + C", "속미분의 역수가 앞에")
    if t == "cos": return fill(f"∫ cos {k}x dx = (1/{{{{1}}}}) sin {k}x + C", [str(k)], f"(sin {k}x)′ = {k} cos {k}x이므로\n∫ cos {k}x dx = (1/{k}) sin {k}x + C", "속미분의 역수")
    if t == "pow":
        n = r.randint(2, 5); c = r.randint(1, 4)
        return fill(f"∫ 2x(x² + {c}){sup(n)} dx = (x² + {c})^{{{{1}}}}/{n + 1} + C", [str(n + 1)], f"t = x² + {c}, dt = 2x dx\n∫ t{sup(n)} dt = t{sup(n + 1)}/{n + 1} + C", "괄호 안을 t로")
    c = r.randint(1, 9)
    return fill(f"∫ 2x/(x² + {c}) dx = ln(x² + {{{{1}}}}) + C", [str(c)], f"분자가 분모의 도함수 → ∫ g′/g dx = ln|g| + C\n= ln(x² + {c}) + C", "∫ g′/g = ln|g|")
def h1_poly(r):
    k, c = r.randint(2, 4), r.randint(1, 3)
    # ∫₀¹ k x^{k−1}(x^k + c) dx = [ (x^k + c)²/2 ]₀¹ = ((1+c)² − c²)/2
    v = F((1 + c) ** 2 - c * c, 2)
    return nf(v, f"∫₀¹ {k}x{sup(k - 1) if k > 2 else ''}(x{sup(k)} + {c}) dx의 값은? (기약분수 또는 정수로)",
              f"t = x{sup(k)} + {c}, dt = {k}x{sup(k - 1) if k > 2 else ''} dx, t: {c} → {c + 1}\n∫ t dt = [t²/2] = ({(c + 1) ** 2} − {c * c})/2 = {fm(v)}", "괄호 안을 t로 치환")
L81 = [("일차식 치환", h1_lin), ("치환적분 공식", h1_fill), ("정적분의 치환", h1_poly)]

def h2_fill(r):
    t = r.choice(["xe", "lnx", "xcos", "xsin"])
    a = r.randint(2, 5)
    if t == "xe": return fill(f"∫ xe^({a}x) dx = (x/{a} − 1/{{{{1}}}})e^({a}x) + C", [str(a * a)],
                               f"u = x, v′ = e^({a}x) → v = e^({a}x)/{a}\n= xe^({a}x)/{a} − ∫ e^({a}x)/{a} dx = (x/{a} − 1/{a * a})e^({a}x) + C", "부분적분: ∫uv′ = uv − ∫u′v")
    if t == "lnx":
        n = r.randint(1, 4)
        return fill(f"∫ x{sup(n) if n > 1 else ''} ln x dx = (x{sup(n + 1)}/{n + 1}) ln x − x{sup(n + 1)}/{{{{1}}}} + C", [str((n + 1) ** 2)],
                    f"u = ln x, v′ = x{sup(n) if n > 1 else ''} → v = x{sup(n + 1)}/{n + 1}\n= (x{sup(n + 1)}/{n + 1}) ln x − ∫ x{sup(n)}/{n + 1} dx = … − x{sup(n + 1)}/{(n + 1) ** 2}".replace("x¹", "x"), "로그를 u로")
    if t == "xcos": return fill(f"∫ x cos {a}x dx = (x/{a}) sin {a}x + (1/{{{{1}}}}) cos {a}x + C", [str(a * a)],
                                 f"u = x, v′ = cos {a}x → v = (1/{a}) sin {a}x\n= (x/{a}) sin {a}x − ∫ (1/{a}) sin {a}x dx = (x/{a}) sin {a}x + (1/{a * a}) cos {a}x + C", "다항식을 u로")
    return fill(f"∫ x sin {a}x dx = −(x/{a}) cos {a}x + (1/{{{{1}}}}) sin {a}x + C", [str(a * a)],
                f"u = x, v′ = sin {a}x → v = −(1/{a}) cos {a}x\n= −(x/{a}) cos {a}x + ∫ (1/{a}) cos {a}x dx = … + (1/{a * a}) sin {a}x + C", "다항식을 u로")
def h2_def(r):
    t = r.choice(["xsin", "lne", "xe"])
    if t == "xsin":
        k = r.randint(1, 4); v = (-1) ** (k + 1) * k
        return nf(F(v), f"∫₀^({k if k > 1 else ''}π) x sin x dx를 π로 나눈 값은?",
                  f"∫ x sin x dx = −x cos x + sin x\n[−x cos x + sin x]₀^({k}π) = −{k}π cos {k}π = {m(v)}π\nπ로 나누면 {m(v)}", "부분적분 후 대입")
    if t == "lne": return nf(1, "∫₁ᵉ ln x dx의 값은?", "∫ ln x dx = x ln x − x\n[x ln x − x]₁ᵉ = (e − e) − (0 − 1) = 1", "u = ln x, v′ = 1")
    return nf(1, "∫₀¹ xeˣ dx의 값은?", "∫ xeˣ dx = (x − 1)eˣ\n[(x − 1)eˣ]₀¹ = 0 − (−1) = 1", "u = x, v′ = eˣ")
def h2_lin(r):
    a, b = nz(r, -4, 5), r.randint(-6, 6)
    if b - a == 0: return None
    return fill(f"∫ ({poly((a, 'x'), (b, ''))})eˣ dx = ({poly((a, 'x'))} + {{{{1}}}})eˣ + C", [ans(b - a)],
                f"u = {poly((a, 'x'), (b, ''))}, v′ = eˣ → v = eˣ\n= ({poly((a, 'x'), (b, ''))})eˣ − ∫ {m(a)}eˣ dx = ({poly((a, 'x'), (b - a, ''))})eˣ + C", "다항식을 u, eˣ를 v′로")
def h2_cos(r):
    k = r.randint(1, 6); v = (-1) ** k - 1
    return nf(v, f"∫₀^({k if k > 1 else ''}π) x cos x dx의 값은?",
              f"∫ x cos x dx = x sin x + cos x (부분적분)\n[x sin x + cos x]₀^({k}π) = (0 + cos {k}π) − (0 + 1) = {m((-1) ** k)} − 1 = {m(v)}", "u = x, v′ = cos x")
L82 = [("부분적분 공식", h2_fill), ("부분적분 정적분", h2_def), ("(ax + b)eˣ의 적분", h2_lin), ("x cos x의 정적분", h2_cos)]

def h3_area(r):
    p, q = r.sample([1, 2, 3, 4, F(1, 2), F(1, 3)], 2)
    A, B = 1 / (F(p) + 1), 1 / (F(q) + 1)
    v = abs(A - B)
    def pw(e): return "x" if e == 1 else (f"x{sup(int(e))}" if F(e).denominator == 1 else ("√x" if e == F(1, 2) else "³√x"))
    up, lo = (pw(p), pw(q)) if A > B else (pw(q), pw(p))
    return nf(v, f"0 ≤ x ≤ 1에서 y = {pw(p)}와 y = {pw(q)} 사이의 넓이는? (기약분수로)",
              f"0 < x < 1에서는 {up} ≥ {lo}\n∫₀¹ {pw(p)} dx = {fs(A)}, ∫₀¹ {pw(q)} dx = {fs(B)}\n넓이 = {fs(max(A, B))} − {fs(min(A, B))} = {fm(v)}", "위 − 아래를 적분")
def h3_vol(r):
    t = r.choice(["sq", "S", "cone"])
    if t == "sq":
        k, a = r.randint(1, 3), r.randint(1, 4)
        v = F(k * k * a ** 3, 3)
        return nf(v, f"x에서 자른 단면이 한 변 {k if k > 1 else ''}x인 정사각형인 입체(0 ≤ x ≤ {a})의 부피는? (기약분수 또는 정수로)", f"V = ∫₀{sup(a)} ({k if k > 1 else ''}x)² dx = {k * k}x³/3 |₀{sup(a)} = {fm(v)}", "단면의 넓이를 적분")
    if t == "S":
        c, a = r.randint(1, 5), r.randint(1, 4)
        return nf(F(c * a * a, 2), f"단면의 넓이가 S(x) = {c if c > 1 else ''}x인 입체(0 ≤ x ≤ {a})의 부피는? (기약분수 또는 정수로)", f"V = ∫₀{sup(a)} {c}x dx = {c}x²/2 |₀{sup(a)} = {fm(F(c * a * a, 2))}", "V = ∫ S(x) dx")
    R, h = r.randint(1, 6), r.randint(1, 6)
    return fill(f"밑면의 반지름 {R}, 높이 {h}인 원뿔의 부피를 정적분으로 구하면 {{{{1}}}}π", [fs(F(R * R * h, 3))],
                f"꼭짓점에서 x만큼 떨어진 단면의 반지름 {R}x/{h}\nV = ∫₀{sup(h)} π({R}x/{h})² dx = π{R * R}{h}³/(3×{h * h}) = {fs(F(R * R * h, 3))}π", "단면 = 원")
L83 = [("곡선 사이의 넓이", h3_area), ("단면을 이용한 부피", h3_vol)]

def h4_len(r):
    t = r.choice(["line", "circle", "seg"])
    if t == "line":
        a, b, c = r.choice(TRI); T = r.randint(1, 4)
        return nf(c * T, f"곡선 x = {a}t, y = {b}t (0 ≤ t ≤ {T})의 길이는?", f"L = ∫₀{sup(T)} √({a}² + {b}²) dt = {c} × {T} = {c * T}", "L = ∫√(x′² + y′²) dt")
    if t == "circle":
        R, k = r.randint(1, 6), r.choice([1, 2])
        return fill(f"x = {R if R > 1 else ''}cos t, y = {R if R > 1 else ''}sin t (0 ≤ t ≤ {'π' if k == 1 else '2π'})의 길이는 {{{{1}}}}π", [str(R * k)],
                    f"√(x′² + y′²) = {R}\nL = {R} × {'π' if k == 1 else '2π'} = {R * k}π", "원의 호 길이")
    k = r.randint(1, 5)
    return fill(f"직선 y = {k if k > 1 else ''}x에서 0 ≤ x ≤ 1 부분의 길이는 √{{{{1}}}}", [str(1 + k * k)], f"L = ∫₀¹ √(1 + (y′)²) dx = √(1 + {k * k}) = √{1 + k * k}", "L = ∫√(1 + y′²) dx")
def h4_v(r):
    n = r.randint(1, 4); t = r.choice(["dist", "disp"])
    if t == "dist": return nf(2 * n, f"v(t) = sin t일 때 t = 0부터 {n if n > 1 else ''}π까지 움직인 거리는?".replace("1π", "π"), f"거리 = ∫|sin t| dt, 반주기마다 2\n2 × {n} = {2 * n}", "거리는 |v|를 적분")
    v = 0 if n % 2 == 0 else 2
    return nf(v, f"v(t) = sin t일 때 t = 0부터 {n if n > 1 else ''}π까지 위치의 변화는?", f"∫₀^({n}π) sin t dt = [−cos t] = 1 − cos {n}π = {v}", "위치의 변화는 v를 적분")
def h4_exp(r):
    k = r.randint(2, 9)
    return nf(k - 1, f"v(t) = eᵗ일 때 t = 0부터 t = ln {k}까지 움직인 거리는?", f"v > 0이므로 거리 = ∫₀^(ln {k}) eᵗ dt = e^(ln {k}) − 1 = {k} − 1 = {k - 1}", "eᵗ의 적분은 eᵗ")
L84 = [("곡선의 길이", h4_len), ("속도로 거리 구하기", h4_v), ("지수 속도", h4_exp)]

ALL = {"ch05": [L51, L52, L53, L54], "ch06": [L61, L62, L63, L64], "ch07": [L71, L72, L73, L74], "ch08": [L81, L82, L83, L84]}

if __name__ == "__main__":
    tot = 0
    for ch, Ls in ALL.items():
        for i, T in enumerate(Ls, 1):
            per = {1: 40, 2: 20, 3: 14, 4: 10, 5: 8}.get(len(T), 6)
            n = write("c4", ch, f"l0{i}", T, per=per, seed=11 + i, ); tot += n; print(ch, i, len(T), n)
    print("total", tot)
