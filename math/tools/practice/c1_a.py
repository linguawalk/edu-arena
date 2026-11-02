"""코스 1 · 챕터 1~4 (수와 식의 확장, 집합, 명제와 증명, 방정식) — 연습 문제 은행"""
from core import *
from itertools import product as iprod

def nz(r, a, b):
    while True:
        x = r.randint(a, b)
        if x: return x
def cpx(a, b):
    """a + bi 표기"""
    if b == 0: return m(a)
    bi = ("" if abs(b) == 1 else str(abs(b))) + "i"
    if a == 0: return ("−" if b < 0 else "") + bi
    return f"{m(a)} {'−' if b < 0 else '+'} {bi}"
TF = "  (참이면 1, 거짓이면 0)"

# ================= ch01 =================
# ---- l01 실수와 절댓값
def c1l1_abs(r):
    a, b, k = r.randint(-5, 5), r.randint(-5, 8), nz(r, -6, 6)
    if a == b: return None
    v = abs(k - a) + abs(k - b)
    return num(f"x = {m(k)}일 때 |x{term(-a)}| + |x{term(-b)}|의 값은?", v,
               f"x = {m(k)}를 대입합니다.\n|{m(k)}{term(-a)}| = |{m(k - a)}| = {abs(k - a)}\n|{m(k)}{term(-b)}| = |{m(k - b)}| = {abs(k - b)}\n합: {abs(k - a)} + {abs(k - b)} = {v}",
               "절댓값 안을 먼저 계산하세요.")

def c1l1_range(r):
    a = r.randint(-4, 4); b = a + r.randint(2, 7)
    return num(f"{m(a)} < x < {m(b)}일 때 |x{term(-a)}| + |x{term(-b)}|의 값은?", b - a,
               f"x > {m(a)}이므로 x{term(-a)} > 0 → |x{term(-a)}| = x{term(-a)}\nx < {m(b)}이므로 x{term(-b)} < 0 → |x{term(-b)}| = −x{term(b)}\n"
               f"더하면 (x{term(-a)}) + (−x{term(b)}) = {m(b - a)}  (x가 사라짐)",
               "각 절댓값 안의 부호를 범위로 판단하세요.")

def c1l1_rat(r):
    n = r.choice([2, 3, 5, 6, 7]); c = r.randint(1, 5)
    return fill(f"{c * n}/√{n} = {{{{1}}}}√{n}", [str(c)],
                f"분모와 분자에 √{j(n, '를을')} 곱합니다.\n{c * n}/√{n} = {c * n}√{n}/(√{n} × √{n}) = {c * n}√{n}/{n} = {c}√{n}" if c > 1 else
                f"분모와 분자에 √{j(n, '를을')} 곱합니다.\n{n}/√{n} = {n}√{n}/{n} = √{n}  (계수 1)",
                "분모의 √를 없애려면 분자·분모에 같은 √를 곱하세요.")

def c1l1_conj(r):
    b = r.choice([1, 2, 3, 5, 6, 7, 10]); a = b + 1
    return fill(f"1/(√{a} − √{b}) = √{a} + √{{{{1}}}}" if b > 1 else f"1/(√{a} − 1) = √{a} + {{{{1}}}}", [str(b)],
                f"분모의 켤레 (√{a} + {'√' + str(b) if b > 1 else '1'})를 분자·분모에 곱합니다.\n분모: (√{a})² − ({'√' + str(b) if b > 1 else '1'})² = {a} − {b} = 1\n따라서 √{a} + {'√' + str(b) if b > 1 else '1'}",
                "(a − b)(a + b) = a² − b²을 이용하세요.")

def c1l1_cmp(r):
    a, b, c, d = r.randint(2, 6), r.choice([2, 3, 5, 6, 7]), r.randint(2, 6), r.choice([2, 3, 5, 6, 7])
    L, R = a * a * b, c * c * d
    if L == R or b == d: return None
    sg = ">" if L > R else "<"
    return fill(f"{a}√{b} {{{{1}}}} {c}√{d}  (부등호 >, < 중 하나)", [[sg]],
                f"근호 안으로 넣어 비교합니다.\n{a}√{b} = √({a}² × {b}) = √{L}\n{c}√{d} = √({c}² × {d}) = √{R}\n{L} {sg} {R}이므로 {a}√{b} {sg} {c}√{d}",
                "계수를 제곱해서 근호 안으로 넣으세요.")

def c1l1_int(r):
    n = r.randint(2, 99)
    if isqrt(n) ** 2 == n: return None
    k = isqrt(n)
    if r.random() < .5:
        return num(f"√{n}의 정수 부분은?", k, f"{k}² = {k * k} < {n} < {(k + 1) ** 2} = {k + 1}²\n따라서 {k} < √{n} < {k + 1}, 정수 부분은 {k}",
                   "√n을 사이에 두는 두 제곱수를 찾으세요.")
    c = r.randint(k + 1, k + 8)
    return num(f"{c} − √{n}의 정수 부분은?", c - k - 1,
               f"{k} < √{n} < {k + 1}이므로\n−{k + 1} < −√{n} < −{k}\n{c - k - 1} < {c} − √{n} < {c - k}\n따라서 정수 부분은 {c - k - 1}",
               "√n의 범위를 먼저 구한 뒤 부등식의 각 변을 바꾸세요.")

def c1l1_sq(r):
    a, c = nz(r, -6, -1), r.randint(1, 9)
    v = abs(a) + abs(a + c)
    return num(f"a = {m(a)}일 때 √(a²) + √((a{term(c)})²)의 값은?", v,
               f"√(x²) = |x|입니다.\n√(a²) = |{m(a)}| = {abs(a)}\n√((a{term(c)})²) = |{m(a + c)}| = {abs(a + c)}\n합: {v}",
               "√(x²)은 x가 아니라 |x|입니다.")

L11 = [("절댓값에 대입", c1l1_abs), ("범위가 주어진 절댓값", c1l1_range), ("분모의 유리화", c1l1_rat), ("켤레로 유리화", c1l1_conj),
       ("무리수의 대소", c1l1_cmp), ("정수 부분", c1l1_int), ("√(a²) = |a|", c1l1_sq)]

# ---- l02 다항식의 연산
def c1l2_add(r):
    A = [r.randint(1, 4), nz(r, -6, 6), nz(r, -9, 9)]; B = [nz(r, -3, 3), nz(r, -6, 6), nz(r, -9, 9)]
    op, k = r.choice([("+", 1), ("−", -1)])
    C = [A[i] + k * B[i] for i in range(3)]
    if C[0] == 0: return None
    pa, pb = poly((A[0], 'x²'), (A[1], 'x'), (A[2], '')), poly((B[0], 'x²'), (B[1], 'x'), (B[2], ''))
    return fill(f"A = {pa}, B = {pb}일 때 A {op} B = {{{{1}}}}x² + {{{{2}}}}x + {{{{3}}}}", [ans(C[0]), ans(C[1]), ans(C[2])],
                (f"B의 각 항의 부호를 바꾸어 더합니다.\n" if op == "−" else "동류항끼리 더합니다.\n") +
                f"x²: {m(A[0])} {op} {par(B[0])} = {m(C[0])}\nx: {m(A[1])} {op} {par(B[1])} = {m(C[1])}\n상수: {m(A[2])} {op} {par(B[2])} = {m(C[2])}\n따라서 {poly((C[0], 'x²'), (C[1], 'x'), (C[2], ''))}",
                "같은 차수끼리 계산하세요.")

def c1l2_cube(r):
    a = nz(r, -4, 4)
    return fill(f"(x{term(a)})³ = x³ + {{{{1}}}}x² + {{{{2}}}}x + {{{{3}}}}", [ans(3 * a), ans(3 * a * a), ans(a ** 3)],
                f"(x + a)³ = x³ + 3ax² + 3a²x + a³에 a = {m(a)}\n3a = {m(3 * a)}, 3a² = {3 * a * a}, a³ = {m(a ** 3)}\n따라서 {poly((1, 'x³'), (3 * a, 'x²'), (3 * a * a, 'x'), (a ** 3, ''))}",
                "세제곱 공식: 계수가 1, 3, 3, 1")

def ab_pair(r):
    while True:
        s, p = r.randint(-6, 8), r.randint(-6, 10)
        if s and p and s * s >= 4 * p: return s, p

def c1l2_sq(r):
    s, p = ab_pair(r)
    t = r.choice(["sq", "cube", "diff"])
    if t == "sq":
        return num(f"a + b = {m(s)}, ab = {m(p)}일 때 a² + b²의 값은?", s * s - 2 * p,
                   f"a² + b² = (a + b)² − 2ab\n= {par(s)}² − 2 × {par(p)} = {s * s} {'−' if p > 0 else '+'} {abs(2 * p)} = {m(s * s - 2 * p)}", "(a + b)²을 전개한 식을 이용하세요.")
    if t == "cube":
        v = s ** 3 - 3 * p * s
        return num(f"a + b = {m(s)}, ab = {m(p)}일 때 a³ + b³의 값은?", v,
                   f"a³ + b³ = (a + b)³ − 3ab(a + b)\n= {par(s)}³ − 3 × {par(p)} × {par(s)} = {m(s ** 3)} {'−' if 3 * p * s > 0 else '+'} {abs(3 * p * s)} = {m(v)}", "(a + b)³ = a³ + b³ + 3ab(a + b)")
    return num(f"a + b = {m(s)}, ab = {m(p)}일 때 (a − b)²의 값은?", s * s - 4 * p,
               f"(a − b)² = (a + b)² − 4ab\n= {s * s} − 4 × {par(p)} = {m(s * s - 4 * p)}", "(a − b)² = (a + b)² − 4ab")

def c1l2_recip(r):
    t = r.randint(2, 7); w = r.choice(["2", "3"])
    if w == "2":
        return num(f"x + 1/x = {t}일 때 x² + 1/x²의 값은?", t * t - 2,
                   f"(x + 1/x)² = x² + 2 + 1/x²\nx² + 1/x² = {t}² − 2 = {t * t - 2}", "x + 1/x을 제곱해 보세요.")
    return num(f"x + 1/x = {t}일 때 x³ + 1/x³의 값은?", t ** 3 - 3 * t,
               f"x³ + 1/x³ = (x + 1/x)³ − 3(x + 1/x)\n= {t}³ − 3 × {t} = {t ** 3} − {3 * t} = {t ** 3 - 3 * t}", "a³ + b³ = (a + b)³ − 3ab(a + b), ab = 1")

def c1l2_div(r):
    d, q0, rem = nz(r, -4, 4), nz(r, -5, 5), r.randint(-6, 9)
    # (x + d)(x + q0) + rem
    b, c = d + q0, d * q0 + rem
    return fill(f"({poly((1, 'x²'), (b, 'x'), (c, ''))}) ÷ (x{term(d)})의 몫은 x + {{{{1}}}}, 나머지는 {{{{2}}}}", [ans(q0), ans(rem)],
                f"x² ÷ x = x → x(x{term(d)}) = {poly((1, 'x²'), (d, 'x'))}를 빼면 {poly((b - d, 'x'), (c, ''))}\n"
                f"{poly((q0, 'x'))} ÷ x = {m(q0)} → {m(q0)}(x{term(d)}) = {poly((q0, 'x'), (q0 * d, ''))}를 빼면 {m(rem)}\n몫 x{term(q0)}, 나머지 {m(rem)}",
                "최고차항부터 차례로 나누세요.")

def c1l2_syn(r):
    a = nz(r, -3, 3); c3, c2, c1, c0 = r.randint(1, 3), r.randint(-4, 4), r.randint(-5, 5), r.randint(-6, 6)
    q2 = c3; q1 = c2 + a * q2; q0 = c1 + a * q1; R = c0 + a * q0
    return fill(f"({poly((c3, 'x³'), (c2, 'x²'), (c1, 'x'), (c0, ''))}) ÷ (x{term(-a)})의 몫은 {poly((c3, 'x²'))} + {{{{1}}}}x + {{{{2}}}}, 나머지는 {{{{3}}}}", [ans(q1), ans(q0), ans(R)],
                f"조립제법(x = {m(a)}):\n계수 {c3}, {m(c2)}, {m(c1)}, {m(c0)}\n{c3} → {m(c2)} + {par(a)}×{c3} = {m(q1)} → {m(c1)} + {par(a)}×{par(q1)} = {m(q0)} → {m(c0)} + {par(a)}×{par(q0)} = {m(R)}\n"
                f"몫 {poly((q2, 'x²'), (q1, 'x'), (q0, ''))}, 나머지 {m(R)}",
                "조립제법을 쓰면 빠릅니다.")

L12 = [("다항식의 덧셈과 뺄셈", c1l2_add), ("세제곱 공식", c1l2_cube), ("곱셈공식의 변형", c1l2_sq), ("x + 1/x 꼴", c1l2_recip),
       ("이차식 ÷ 일차식", c1l2_div), ("삼차식 ÷ 일차식", c1l2_syn)]

# ---- l03 나머지정리와 인수분해
def cubic(r):
    return [r.randint(1, 2), r.randint(-4, 4), r.randint(-6, 6), r.randint(-8, 8)]
def ev(c, x): return sum(ci * x ** (3 - i) for i, ci in enumerate(c))
def pc(c): return poly((c[0], 'x³'), (c[1], 'x²'), (c[2], 'x'), (c[3], ''))

def c1l3_rem(r):
    c, a = cubic(r), nz(r, -3, 3)
    v = ev(c, a)
    return num(f"f(x) = {pc(c)}를 x{term(-a)}로 나눈 나머지는?", v,
               f"나머지정리: f(x)를 x − a로 나눈 나머지는 f(a)\n여기서 a = {m(a)}\nf({m(a)}) = {' + '.join(f'{par(ci)}×{par(a)}{sup(3 - i)}' if i < 3 else par(ci) for i, ci in enumerate(c))} = {m(v)}".replace("¹", ""),
               "나누는 식이 0이 되는 x를 f(x)에 넣으세요.")

def c1l3_finda(r):
    c, k, b = r.randint(-3, 3), nz(r, -5, 5), r.randint(-6, 6)
    if c == 0: return None
    # x³ + kx + b ÷ (x − c) remainder R
    R = c ** 3 + k * c + b
    return num(f"x³ + ax{term(b)}를 x{term(-c)}로 나눈 나머지가 {m(R)}일 때 a의 값은?", k,
               f"나머지정리로 f({m(c)}) = {m(R)}\n{par(c)}³ + a×{par(c)}{term(b)} = {m(R)}\n{m(c ** 3)}{term(c, 'a')}{term(b)} = {m(R)}\n{poly((c, 'a'))} = {m(R - c ** 3 - b)}" + (f" → a = {m(k)}" if c != 1 else ""),
               "f(c) = 나머지를 세우세요.")

def c1l3_factor(r):
    a, b, k, c = nz(r, -3, 3), r.randint(-4, 4), r.randint(-6, 6), None
    # x³ + b x² + k x + d has factor (x − a) → d = −(a³ + b a² + k a); ask k given d
    d = r.randint(-8, 8)
    kk = F(-(a ** 3 + b * a * a + d), a)
    if kk.denominator != 1: return None
    return num(f"x³{term(b, 'x²')} + kx{term(d)}가 x{term(-a)}를 인수로 가질 때 k의 값은?", int(kk),
               f"인수정리: f({m(a)}) = 0\n{m(a ** 3)}{term(b * a * a)}{term(a, 'k')}{term(d)} = 0\n{poly((a, 'k'))} = {m(-(a ** 3 + b * a * a + d))}" + (f" → k = {m(int(kk))}" if a != 1 else ""),
               "x − a가 인수이면 f(a) = 0입니다.")

def c1l3_roots(r):
    rs = r.sample([-3, -2, -1, 1, 2, 3, 4], 3)
    s, p2, p3 = sum(rs), rs[0] * rs[1] + rs[1] * rs[2] + rs[0] * rs[2], rs[0] * rs[1] * rs[2]
    a, b = sorted(rs[:2])
    c = rs[2]
    return fill(f"{poly((1, 'x³'), (-s, 'x²'), (p2, 'x'), (-p3, ''))} = (x{term(-a)})(x{term(-b)})(x − {{{{1}}}})", [ans(c)],
                f"x = {m(a)}를 대입하면 0이므로 x{term(-a)}가 인수입니다.\n조립제법으로 나누고 남은 이차식을 인수분해하면\n(x{term(-a)})(x{term(-b)})(x{term(-c)})\n따라서 빈칸은 {m(c)}",
                "상수항의 약수를 대입해 0이 되는 값을 찾으세요.")

def c1l3_cubes(r):
    a = r.randint(1, 5); s = r.choice([1, -1])
    if s > 0:
        return fill(f"x³ + {a ** 3} = (x + {a})(x² − {{{{1}}}}x + {a * a})" if a > 1 else "x³ + 1 = (x + 1)(x² − x + {{1}})", [str(a) if a > 1 else "1"],
                    f"a³ + b³ = (a + b)(a² − ab + b²)\nx³ + {a}³ = (x + {a})(x² − {a}x + {a * a})".replace(" − 1x", " − x"), "세제곱의 합 공식")
    return fill(f"x³ − {a ** 3} = (x − {a})(x² + {{{{1}}}}x + {a * a})" if a > 1 else "x³ − 1 = (x − 1)(x² + x + {{1}})", [str(a) if a > 1 else "1"],
                f"a³ − b³ = (a − b)(a² + ab + b²)\nx³ − {a}³ = (x − {a})(x² + {a}x + {a * a})".replace(" + 1x", " + x"), "세제곱의 차 공식")

def c1l3_two(r):
    p, q = r.sample([-2, -1, 1, 2, 3], 2)
    a0, b0 = nz(r, -4, 4), r.randint(-6, 6)
    r1, r2 = a0 * p + b0, a0 * q + b0
    ask = r.choice(["a", "b"])
    return num(f"f(x)를 x{term(-p)}로 나눈 나머지가 {m(r1)}, x{term(-q)}로 나눈 나머지가 {m(r2)}입니다. f(x)를 (x{term(-p)})(x{term(-q)})로 나눈 나머지를 ax + b라 할 때 {ask}의 값은?",
               a0 if ask == "a" else b0,
               f"f(x) = (x{term(-p)})(x{term(-q)})Q(x) + ax + b\nf({m(p)}) = {m(p)}a + b = {m(r1)}, f({m(q)}) = {m(q)}a + b = {m(r2)}\n빼서 풀면 a = {m(a0)}, b = {m(b0)}",
               "나누는 식이 0이 되는 두 값을 대입해 연립하세요.")

def c1l3_pow(r):
    n = r.randint(5, 30); k = r.randint(1, 4); c = r.choice([1, -1])
    v = c ** n + k
    return num(f"x{sup(n)}{term(k)}를 x{term(-c)}로 나눈 나머지는?", v,
               f"나머지정리: x = {m(c)}를 대입합니다.\n{par(c)}{sup(n)}{term(k)} = {m(c ** n)}{term(k)} = {m(v)}",
               "x − a로 나눈 나머지는 f(a)입니다.")

L13 = [("나머지정리", c1l3_rem), ("나머지로 미정계수", c1l3_finda), ("인수정리", c1l3_factor), ("삼차식 인수분해", c1l3_roots),
       ("세제곱의 합과 차", c1l3_cubes), ("이차식으로 나눈 나머지", c1l3_two), ("거듭제곱의 나머지", c1l3_pow)]

# ---- l04 복소수
def c1l4_add(r):
    a, b, c, d = nz(r, -6, 6), nz(r, -6, 6), nz(r, -6, 6), nz(r, -6, 6)
    op = r.choice(["+", "−"]); k = 1 if op == "+" else -1
    x, y = a + k * c, b + k * d
    if y == 0: return None
    return fill(f"({cpx(a, b)}) {op} ({cpx(c, d)}) = {{{{1}}}} + {{{{2}}}}i", [ans(x), ans(y)],
                f"실수부분끼리, 허수부분끼리 계산합니다.\n실수부분: {m(a)} {op} {par(c)} = {m(x)}\n허수부분: {m(b)} {op} {par(d)} = {m(y)}\n따라서 {cpx(x, y)}",
                "실수부분끼리, 허수부분끼리")

def c1l4_mul(r):
    a, b, c, d = nz(r, -4, 4), nz(r, -4, 4), nz(r, -4, 4), nz(r, -4, 4)
    x, y = a * c - b * d, a * d + b * c
    return fill(f"({cpx(a, b)})({cpx(c, d)}) = {{{{1}}}} + {{{{2}}}}i", [ans(x), ans(y)],
                f"분배법칙으로 전개하고 i² = −1을 씁니다.\n{m(a)}×{par(c)} + {m(a)}×{par(d)}i + {m(b)}i×{par(c)} + {m(b)}×{par(d)}i²\n= {m(a * c)}{term(a * d + b * c, 'i')} {'−' if b * d >= 0 else '+'} {abs(b * d)}  (i² = −1)\n= {cpx(x, y)}",
                "i² = −1")

def c1l4_conj(r):
    a, b = nz(r, -7, 7), nz(r, -7, 7)
    return num(f"({cpx(a, b)})({cpx(a, -b)})의 값은?", a * a + b * b,
               f"켤레복소수끼리의 곱: (a + bi)(a − bi) = a² + b²\n= {a * a} + {b * b} = {a * a + b * b}", "(a + bi)(a − bi) = a² − (bi)² = a² + b²")

def c1l4_ipow(r):
    n = r.randint(5, 103)
    v = ["1", "i", "-1", "-i"][n % 4]
    return fill(f"i{sup(n)} = {{{{1}}}}", [[v, v.replace("-", "−")]],
                f"i의 거듭제곱은 i, −1, −i, 1이 4개씩 반복됩니다. (i⁴ = 1)\n{n} = 4 × {n // 4} + {n % 4}\ni{sup(n)} = i{sup(n % 4) if n % 4 else '⁰'} = {v.replace('-', '−')}",
                "지수를 4로 나눈 나머지를 보세요.")

def c1l4_eq(r):
    a, b, c, d = r.randint(-5, 5), r.randint(-5, 5), nz(r, -6, 6), nz(r, -6, 6)
    x, y = c + a, d - b
    return num(f"(x{term(-a)}) + (y{term(b)})i = {cpx(c, d)}일 때 x + y의 값은? (x, y는 실수)", x + y,
               f"복소수가 같으려면 실수부분과 허수부분이 각각 같아야 합니다.\nx{term(-a)} = {m(c)} → x = {m(x)}\ny{term(b)} = {m(d)} → y = {m(y)}\nx + y = {m(x + y)}",
               "실수부분 = 실수부분, 허수부분 = 허수부분")

def c1l4_div(r):
    p, q, c, d = nz(r, -3, 3), nz(r, -3, 3), nz(r, -3, 3), nz(r, -3, 3)
    a, b = p * c - q * d, p * d + q * c
    return fill(f"({cpx(a, b)}) ÷ ({cpx(c, d)}) = {{{{1}}}} + {{{{2}}}}i", [ans(p), ans(q)],
                f"분모의 켤레 {cpx(c, -d)}를 분자·분모에 곱합니다.\n분모: {c * c} + {d * d} = {c * c + d * d}\n분자: ({cpx(a, b)})({cpx(c, -d)}) = {cpx(p * (c * c + d * d), q * (c * c + d * d))}\n"
                f"나누면 {cpx(p, q)}",
                "분모의 켤레복소수를 곱해 분모를 실수로 만드세요.")

def c1l4_neg(r):
    a, b = r.choice([(2, 8), (3, 12), (2, 18), (4, 9), (3, 27), (5, 20), (1, 4), (6, 24), (2, 32)])
    k = isqrt(a * b)
    return num(f"√(−{a}) × √(−{b})의 값은?", -k,
               f"√(−{a}) = √{a}i, √(−{b}) = √{b}i\n곱: √{a}×√{b} × i² = √{a * b} × (−1) = −{k}\n(√(−a)√(−b) = √(ab)가 아님에 주의)",
               "먼저 i를 써서 나타낸 다음 곱하세요.")

def c1l4_z(r):
    a, b = nz(r, -4, 4), nz(r, -4, 4)
    v = -(a * a + b * b)
    return num(f"z = {cpx(a, b)}일 때 z² − {2 * a if a > 0 else '(' + m(2 * a) + ')'}z의 값은?".replace("− (−", "+ ").replace(")z", "z") if a < 0 else f"z = {cpx(a, b)}일 때 z² − {2 * a}z의 값은?", v,
               f"z² − {m(2 * a)}z = (z − {m(a)})² − {a * a}\nz − {m(a)} = {cpx(0, b)}이므로 (z − {m(a)})² = ({cpx(0, b)})² = −{b * b}\n따라서 −{b * b} − {a * a} = {m(v)}".replace("− −", "+ "),
               "z − a = bi를 이용하면 간단합니다.")

L14 = [("복소수의 덧셈과 뺄셈", c1l4_add), ("복소수의 곱셈", c1l4_mul), ("켤레복소수의 곱", c1l4_conj), ("i의 거듭제곱", c1l4_ipow),
       ("복소수가 같을 조건", c1l4_eq), ("복소수의 나눗셈", c1l4_div), ("음수의 제곱근", c1l4_neg), ("식의 값", c1l4_z)]

# ================= ch02 집합 =================
def setstr(s): return "{" + ", ".join(map(str, sorted(s))) + "}"

def c2l1_div(r):
    n = r.choice([6, 8, 10, 12, 15, 16, 18, 20, 24, 28, 30, 36])
    d = divisors(n)
    return num(f"{{x | x는 {n}의 약수}}의 원소는 몇 개일까요?", len(d),
               f"원소나열법으로 쓰면 {setstr(d)}\n따라서 n = {len(d)}", "약수를 빠짐없이 나열하세요.")

def c2l1_prime(r):
    n = r.randint(10, 40); ps = [p for p in range(2, n + 1) if is_prime(p)]
    return num(f"{{x | x는 {n} 이하의 소수}}의 원소는 몇 개일까요?", len(ps),
               f"{setstr(ps)}\n따라서 {len(ps)}개", "2부터 차례로 소수를 찾으세요.")

def c2l1_mult(r):
    k, n = r.randint(2, 5), r.randint(3, 7)
    s = [k * i for i in range(1, n + 1)]
    return num(f"{{x | x = {k}m, m은 {n} 이하의 자연수}}의 원소의 합은?", sum(s),
               f"m = 1, 2, …, {n}을 넣으면 {setstr(s)}\n합: {sum(s)}", "m에 자연수를 차례로 넣어 보세요.")

def c2l1_sum(r):
    A = sorted(r.sample(range(0, 5), r.choice([2, 3])))
    S = sorted({x + y for x in A for y in A})
    return num(f"A = {setstr(A)}일 때 {{x + y | x ∈ A, y ∈ A}}의 원소는 몇 개일까요?", len(S),
               f"가능한 x + y를 모두 구하면 {', '.join(str(x + y) for x in A for y in A)}\n중복을 빼면 {setstr(S)} → {len(S)}개", "같은 값은 한 번만 셉니다.")

def c2l1_range(r):
    a = r.randint(0, 8); b = a + r.randint(1, 8)
    xs = [x for x in range(a + 1, b)]
    return num(f"{{x | {a} < x < {b}인 자연수}}의 원소는 몇 개일까요?", len([x for x in xs if x >= 1]),
               f"{a}보다 크고 {b}보다 작은 자연수: {setstr(xs) if xs else '없음(공집합)'}\n따라서 {len(xs)}개", "양 끝은 포함하지 않습니다.")

def c2l1_quad(r):
    s, p = r.choice([(5, 6), (4, 4), (0, -9), (6, 9), (1, -6), (2, 1), (3, 5), (0, 4), (7, 12)])
    D = s * s - 4 * p
    v = 2 if D > 0 else 1 if D == 0 else 0
    return num(f"A = {{x | x² {'−' if s > 0 else '+'} {abs(s)}x {'+' if p > 0 else '−'} {abs(p)} = 0, x는 실수}}일 때 n(A)는?".replace(" + 0x", "").replace(" − 0x", ""), v,
               f"판별식 D = {s * s} − 4×{par(p)} = {D}\n" + ("서로 다른 실근 2개" if D > 0 else "중근 1개(원소는 하나)" if D == 0 else "실근이 없으므로 공집합") + f"\nn(A) = {v}",
               "중근은 원소 하나로 셉니다.")

def c2l1_mem(r):
    n = r.choice([12, 18, 20, 24, 30, 36]); k = r.randint(2, 12)
    ok = n % k == 0
    sym = "∈" if ok else "∉"
    return fill(f"{k} {{{{1}}}} {{x | x는 {n}의 약수}}  (∈ 또는 ∉)", [[sym]],
                (f"{n} = {k} × {n // k}로 나누어떨어지므로 {k}는 {n}의 약수, 즉 원소입니다." if ok else f"{n} ÷ {k}는 몫 {n // k}, 나머지 {n % k}로 나누어떨어지지 않으므로 원소가 아닙니다.") + f"\n따라서 {k} {sym} {{x | x는 {n}의 약수}}",
                "그 수가 조건을 만족하는지 확인하세요.")

L21 = [("약수의 집합", c2l1_div), ("소수의 집합", c2l1_prime), ("조건제시법 → 원소의 합", c2l1_mult), ("새 집합 만들기", c2l1_sum),
       ("범위 안의 자연수", c2l1_range), ("방정식의 해집합", c2l1_quad), ("원소인지 판단", c2l1_mem)]

def c2l2_sub(r):
    n = r.randint(2, 7); t = r.choice(["all", "proper"])
    if t == "all":
        return num(f"원소가 {n}개인 집합의 부분집합은 몇 개일까요?", 2 ** n,
                   f"각 원소마다 '넣는다/안 넣는다' 2가지씩\n2{sup(n)} = {2 ** n}", "원소 하나당 선택지가 2개입니다.")
    return num(f"원소가 {n}개인 집합의 진부분집합은 몇 개일까요?", 2 ** n - 1,
               f"부분집합 2{sup(n)} = {2 ** n}개에서 자기 자신을 뺍니다.\n{2 ** n} − 1 = {2 ** n - 1}", "진부분집합은 자기 자신을 뺀 부분집합입니다.")

def c2l2_fix(r):
    n = r.randint(4, 7); inc = r.randint(1, 2); exc = r.randint(0, 2)
    if inc + exc >= n: return None
    U = list(range(1, n + 1)); I = U[:inc]; E = U[-exc:] if exc else []
    v = 2 ** (n - inc - exc)
    desc = f"{', '.join(map(str, I))}는 반드시 포함하" + (f"고 {', '.join(map(str, E))}는 포함하지 않는" if E else "는")
    return num(f"{setstr(U)}의 부분집합 중 {desc} 것은 몇 개일까요?", v,
               f"정해진 원소 {inc + exc}개를 빼고 남은 {n - inc - exc}개의 원소만 자유롭게 고릅니다.\n2{sup(n - inc - exc)} = {v}",
               "넣을지 말지 정해진 원소는 빼고 세세요.")

def c2l2_k(r):
    n, k = r.randint(4, 7), r.randint(1, 3)
    from math import comb
    return num(f"{setstr(range(1, n + 1))}의 부분집합 중 원소가 {k}개인 것은 몇 개일까요?", comb(n, k),
               f"{n}개 중 {k}개를 고르는 방법의 수입니다.\n" + (f"{n} ÷ 1 = {n}" if k == 1 else f"{' × '.join(str(n - i) for i in range(k))} ÷ ({' × '.join(str(k - i) for i in range(k))}) = {comb(n, k)}"),
               f"{n}개 원소 중 {k}개를 고르세요.")

def c2l2_between(r):
    n = r.randint(4, 7); k = r.randint(1, 3)
    return num(f"{setstr(range(1, k + 1))} ⊂ X ⊂ {setstr(range(1, n + 1))}를 만족하는 집합 X는 몇 개일까요?", 2 ** (n - k),
               f"X는 {', '.join(map(str, range(1, k + 1)))}을 반드시 포함하고, 나머지 {n - k}개 원소는 자유롭게 고릅니다.\n2{sup(n - k)} = {2 ** (n - k)}",
               "반드시 들어가는 원소를 빼고 세세요.")

def c2l2_eq(r):
    a, x = r.randint(1, 9), r.randint(2, 15)
    if a == x: return None
    k = r.randint(1, 5)
    return num(f"{{{a}, x + {k}}} = {{{a}, {x + k}}}일 때 x의 값은?" if x + k != a else None, x,
               f"두 집합이 같으면 원소가 모두 같습니다.\nx + {k} = {x + k} → x = {x}", "같은 집합은 원소가 모두 같습니다.") if x + k != a else None

def c2l2_or(r):
    n = r.randint(3, 6)
    U = "abcdef"[:n]
    return num(f"{{{', '.join(U)}}}의 부분집합 중 a 또는 b를 포함하는 것은 몇 개일까요?", 2 ** n - 2 ** (n - 2),
               f"전체 부분집합 2{sup(n)} = {2 ** n}개에서 a, b를 모두 포함하지 않는 것 2{sup(n - 2)} = {2 ** (n - 2)}개를 뺍니다.\n{2 ** n} − {2 ** (n - 2)} = {2 ** n - 2 ** (n - 2)}",
               "여사건: 전체 − (a, b 둘 다 없는 것)")

L22 = [("부분집합의 개수", c2l2_sub), ("조건이 있는 부분집합", c2l2_fix), ("원소 수가 정해진 부분집합", c2l2_k),
       ("사이에 있는 집합", c2l2_between), ("서로 같은 집합", c2l2_eq), ("a 또는 b를 포함", c2l2_or)]

def sets(r):
    N = r.randint(10, 20); p, q = r.sample([2, 3, 4, 5], 2)
    U = set(range(1, N + 1)); A = {x for x in U if x % p == 0}; B = {x for x in U if x % q == 0}
    return N, p, q, U, A, B
def sdesc(N, p, q): return f"U = {{1, 2, …, {N}}}, A = {{x | x는 {p}의 배수}}, B = {{x | x는 {q}의 배수}}일 때"

def c2l3_op(r):
    N, p, q, U, A, B = sets(r)
    ops = [("A ∪ B", A | B), ("A ∩ B", A & B), ("Aᶜ", U - A), ("A − B", A - B), ("(A ∪ B)ᶜ", U - (A | B)), ("Aᶜ ∩ B", (U - A) & B)]
    nm, S = r.choice(ops)
    return num(f"{sdesc(N, p, q)} n({nm})의 값은?", len(S),
               f"A = {setstr(A)}\nB = {setstr(B)}\n{nm} = {setstr(S) if S else '∅'}\nn({nm}) = {len(S)}",
               "먼저 A, B를 원소나열법으로 쓰세요.")

def c2l3_find(r):
    b = r.randint(3, 9); others = r.sample([x for x in range(1, 10) if x != b], 2)
    return num(f"A = {{{others[0]}, {others[1]}, a}}, B = {{{others[1]}, {b}}}이고 A ∩ B = {{{others[1]}, {b}}}일 때 a의 값은?", b,
               f"A ∩ B에 {j(b, '가이')} 있으므로 {j(b, '는은')} A의 원소여야 합니다.\nA의 원소 중 {b}가 될 수 있는 것은 a뿐이므로 a = {b}",
               "교집합의 원소는 두 집합에 모두 들어 있습니다.")

def c2l3_law(r):
    pool = [("(A ∪ B)ᶜ = Aᶜ {{1}} Bᶜ", "∩", "드모르간 법칙: 합집합의 여집합은 여집합들의 교집합입니다.\nA에도 B에도 속하지 않는 원소 = A 밖이면서 B 밖인 원소"),
            ("(A ∩ B)ᶜ = Aᶜ {{1}} Bᶜ", "∪", "드모르간 법칙: 교집합의 여집합은 여집합들의 합집합입니다.\nA와 B 모두에 속하지는 않는 원소 = A 밖이거나 B 밖인 원소"),
            ("A − B = A ∩ {{1}}", "Bᶜ", "A − B는 A에 있고 B에 없는 원소의 집합입니다.\n'B에 없다' = Bᶜ에 있다 → A ∩ Bᶜ"),
            ("A ∩ (B ∪ C) = (A ∩ B) {{1}} (A ∩ C)", "∪", "분배법칙: ∩를 괄호 안의 ∪에 나누어 줍니다.\n벤 다이어그램으로 두 영역이 같음을 확인할 수 있습니다."),
            ("A ∪ (B ∩ C) = (A ∪ B) {{1}} (A ∪ C)", "∩", "분배법칙: ∪를 괄호 안의 ∩에 나누어 줍니다.\n벤 다이어그램으로 두 영역이 같음을 확인할 수 있습니다."),
            ("A ⊂ B이면 A ∪ B = {{1}}", "B", "A의 원소는 모두 B에 들어 있습니다.\n그래서 A와 B를 합쳐도 새로 생기는 원소가 없어 B"),
            ("A ⊂ B이면 A ∩ B = {{1}}", "A", "A의 원소는 모두 B에도 있습니다.\n그래서 공통부분은 A 전체"),
            ("A ∩ Aᶜ = {{1}}", "∅", "Aᶜ는 A에 속하지 않는 원소들입니다.\n둘에 동시에 속하는 원소는 없으므로 공집합"),
            ("(Aᶜ)ᶜ = {{1}}", "A", "A 밖의 원소들의 '밖'은 다시 A입니다.\n여집합의 여집합은 자기 자신")]
    p, a, e = r.choice(pool)
    return fill(p, [[a]], e + f"\n따라서 빈칸은 {a}", "벤 다이어그램을 그려 확인하세요.")

def c2l3_rand(r):
    U = list(range(1, 10)); A = set(r.sample(U, r.randint(3, 5))); B = set(r.sample(U, r.randint(3, 5)))
    nm, S = r.choice([("A ∪ B", A | B), ("A ∩ B", A & B), ("A − B", A - B), ("B − A", B - A)])
    return num(f"A = {setstr(A)}, B = {setstr(B)}일 때 {nm}의 원소의 합은?", sum(S),
               f"{nm} = {setstr(S) if S else '∅'}\n원소의 합: {' + '.join(map(str, sorted(S))) if S else '0'} = {sum(S)}",
               "연산 결과를 먼저 원소나열법으로 쓰세요.")

L23 = [("집합의 연산", c2l3_op), ("교집합으로 미지수", c2l3_find), ("연산 법칙", c2l3_law), ("원소나열법 연산", c2l3_rand)]

def c2l4_basic(r):
    a, b = r.randint(5, 25), r.randint(5, 25); c = r.randint(1, min(a, b) - 1)
    t = r.choice(["union", "inter", "diff", "comp"])
    if t == "union":
        return num(f"n(A) = {a}, n(B) = {b}, n(A ∩ B) = {c}일 때 n(A ∪ B)는?", a + b - c,
                   f"n(A ∪ B) = n(A) + n(B) − n(A ∩ B)\n= {a} + {b} − {c} = {a + b - c}", "겹치는 부분을 두 번 세지 않도록 빼세요.")
    if t == "inter":
        return num(f"n(A) = {a}, n(B) = {b}, n(A ∪ B) = {a + b - c}일 때 n(A ∩ B)는?", c,
                   f"n(A ∩ B) = n(A) + n(B) − n(A ∪ B)\n= {a} + {b} − {a + b - c} = {c}", "합집합 공식을 거꾸로 쓰세요.")
    if t == "diff":
        return num(f"n(A) = {a}, n(A ∩ B) = {c}일 때 n(A − B)는?", a - c,
                   f"n(A − B) = n(A) − n(A ∩ B) = {a} − {c} = {a - c}", "A에서 겹치는 부분을 빼세요.")
    N = a + b + r.randint(0, 10)
    return num(f"n(U) = {N}, n(A) = {a}일 때 n(Aᶜ)은?", N - a, f"n(Aᶜ) = n(U) − n(A) = {N} − {a} = {N - a}", "전체에서 A를 빼세요.")

def c2l4_survey(r):
    N = r.choice([30, 35, 40, 45, 50]); a, b = r.randint(10, 25), r.randint(10, 25); c = r.randint(3, min(a, b) - 2)
    if a + b - c > N: return None
    t = r.choice(["either", "neither", "only"])
    if t == "either":
        return num(f"학생 {N}명 중 수학을 좋아하는 학생 {a}명, 과학을 좋아하는 학생 {b}명, 둘 다 좋아하는 학생 {c}명입니다. 둘 중 하나 이상 좋아하는 학생은 몇 명일까요?", a + b - c,
                   f"n(A ∪ B) = {a} + {b} − {c} = {a + b - c}명", "합집합의 원소의 개수를 구하세요.")
    if t == "neither":
        return num(f"학생 {N}명 중 수학을 좋아하는 학생 {a}명, 과학을 좋아하는 학생 {b}명, 둘 다 좋아하는 학생 {c}명입니다. 둘 다 좋아하지 않는 학생은 몇 명일까요?", N - (a + b - c),
                   f"하나 이상 좋아하는 학생: {a} + {b} − {c} = {a + b - c}\n둘 다 좋아하지 않는 학생: {N} − {a + b - c} = {N - a - b + c}명", "전체 − 합집합")
    return num(f"학생 {N}명 중 수학을 좋아하는 학생 {a}명, 과학을 좋아하는 학생 {b}명, 둘 다 좋아하는 학생 {c}명입니다. 수학만 좋아하는 학생은 몇 명일까요?", a - c,
               f"수학만 = n(A − B) = {a} − {c} = {a - c}명", "둘 다 좋아하는 학생을 빼세요.")

def c2l4_mult(r):
    N = r.choice([50, 60, 100, 120, 200]); p, q = r.sample([2, 3, 4, 5, 6, 7], 2)
    from math import lcm
    L_ = lcm(p, q); a, b, c = N // p, N // q, N // L_
    t = r.choice(["or", "neither"])
    if t == "or":
        return num(f"1부터 {N}까지 자연수 중 {p}의 배수 또는 {q}의 배수는 몇 개일까요?", a + b - c,
                   f"{p}의 배수 {a}개, {q}의 배수 {b}개, 둘 다의 배수({L_}의 배수) {c}개\n{a} + {b} − {c} = {a + b - c}", "공배수는 최소공배수의 배수입니다.")
    return num(f"1부터 {N}까지 자연수 중 {p}의 배수도 {q}의 배수도 아닌 수는 몇 개일까요?", N - (a + b - c),
               f"{p} 또는 {q}의 배수: {a} + {b} − {c} = {a + b - c}개 ({L_}의 배수 {c}개 중복)\n{N} − {a + b - c} = {N - a - b + c}", "전체에서 합집합을 빼세요.")

def c2l4_three(r):
    N = r.choice([30, 60, 90, 120]); p, q, s = 2, 3, 5
    if r.random() < .5: p, q, s = 2, 3, 7
    from math import lcm
    v = sum(1 for x in range(1, N + 1) if x % p == 0 or x % q == 0 or x % s == 0)
    a, b, c = N // p, N // q, N // s; ab, bc, ca, abc = N // (p * q), N // (q * s), N // (p * s), N // (p * q * s)
    return num(f"1부터 {N}까지 자연수 중 {p}, {q}, {s} 중 적어도 하나의 배수는 몇 개일까요?", v,
               f"세 집합의 포함배제:\n({a} + {b} + {c}) − ({ab} + {bc} + {ca}) + {abc} = {v}", "더하고, 두 개씩 겹친 것 빼고, 세 개 겹친 것 더하기")

def c2l4_minmax(r):
    N = r.randint(30, 50); a, b = r.randint(15, N - 5), r.randint(15, N - 5)
    if a + b <= N: return None
    t = r.choice(["min", "max"])
    if t == "min":
        return num(f"n(U) = {N}, n(A) = {a}, n(B) = {b}일 때 n(A ∩ B)의 최솟값은?", a + b - N,
                   f"n(A ∩ B) = {a} + {b} − n(A ∪ B)\nn(A ∪ B) ≤ {N}이므로 n(A ∩ B) ≥ {a + b} − {N} = {a + b - N}", "합집합이 가장 클 때(= 전체) 교집합이 가장 작습니다.")
    return num(f"n(U) = {N}, n(A) = {a}, n(B) = {b}일 때 n(A ∩ B)의 최댓값은?", min(a, b),
               f"A ∩ B는 A와 B 각각에 포함되므로 n(A ∩ B) ≤ min({a}, {b}) = {min(a, b)}\n작은 집합이 큰 집합에 포함될 때 최대", "작은 집합이 큰 집합 안에 쏙 들어갈 때입니다.")

L24 = [("합집합·교집합 공식", c2l4_basic), ("설문 조사", c2l4_survey), ("배수의 개수", c2l4_mult), ("세 집합의 포함배제", c2l4_three), ("교집합의 최대·최소", c2l4_minmax)]

# ================= ch03 명제와 증명 =================
def c3l1_truth(r):
    N = r.randint(8, 20)
    conds = [("x는 소수", lambda x: is_prime(x)), ("x는 짝수", lambda x: x % 2 == 0), ("x는 3의 배수", lambda x: x % 3 == 0),
             (f"x는 {N}의 약수", lambda x: N % x == 0), ("x는 홀수", lambda x: x % 2 == 1), ("x² < 30", lambda x: x * x < 30)]
    nm, f = r.choice(conds); neg = r.random() < .4
    S = [x for x in range(1, N + 1) if f(x) != neg]
    return num(f"U = {{1, 2, …, {N}}}에서 조건 {'~' if neg else ''}p의 진리집합의 원소는 몇 개일까요?  (p: {nm})", len(S),
               (f"p의 진리집합의 여집합이 ~p의 진리집합입니다.\n" if neg else "") + f"진리집합: {setstr(S)}\n따라서 {len(S)}개",
               "U의 원소 중 조건을 만족하는 것을 모으세요.")

def c3l1_neg(r):
    a = r.randint(-5, 9); op = r.choice([">", "<", "≥", "≤"])
    ng = {">": "≤", "<": "≥", "≥": "<", "≤": ">"}[op]
    return fill(f"'x {op} {m(a)}'의 부정은 'x {{{{1}}}} {m(a)}'", [[ng, {"≤": "<=", "≥": ">="}.get(ng, ng)]],
                f"부정은 반대쪽 전체입니다. 경계 {m(a)}의 포함 여부도 바뀝니다.\n'x {op} {m(a)}'의 부정 → 'x {ng} {m(a)}'", "'>'의 부정은 '≤'입니다.")

def c3l1_mult(r):
    a, b = r.sample([2, 3, 4, 5, 6, 8, 9, 10, 12, 15], 2)
    t = r.choice(["mult", "div"])
    if t == "mult":
        v = 1 if a % b == 0 else 0
        return num(f"'x가 {a}의 배수이면 x는 {b}의 배수이다'{TF}", v,
                   (f"{a} = {b} × {a // b}이므로 {a}의 배수는 모두 {b}의 배수입니다. → 참" if v else f"반례: x = {a}는 {a}의 배수지만 {b}의 배수가 아닙니다. → 거짓"),
                   "P ⊂ Q인지 확인하세요.")
    v = 1 if b % a == 0 else 0
    return num(f"'x가 {a}의 약수이면 x는 {b}의 약수이다'{TF}", v,
               (f"{a}의 약수는 모두 {b}의 약수입니다({b} = {a} × {b // a}). → 참" if v else f"반례: x = {a}는 {a}의 약수지만 {b}의 약수가 아닙니다. → 거짓"),
               "약수의 집합 사이 포함 관계를 보세요.")

def c3l1_counter(r):
    k = r.randint(1, 9)
    return num(f"'x² = {k * k}이면 x = {k}'의 반례가 되는 x의 값은?", -k,
               f"x² = {k * k}을 만족하는 x는 {j(k, '와과')} −{k}\n이 중 x = {k}가 아닌 −{j(k, '가이')} 반례입니다.", "가정은 만족하지만 결론은 만족하지 않는 값")

def c3l1_param(r):
    a = r.randint(-3, 8)
    t = r.choice(["gt", "lt"])
    if t == "gt":
        return num(f"'x > {m(a)}이면 x > k'가 참이 되는 실수 k의 최댓값은?", a,
                   f"P = {{x | x > {m(a)}}} ⊂ Q = {{x | x > k}}이어야 합니다.\n수직선에서 k ≤ {m(a)}일 때 성립 → k의 최댓값 {m(a)}", "P ⊂ Q가 되도록 수직선에 그려 보세요.")
    return num(f"'x < {m(a)}이면 x < k'가 참이 되는 실수 k의 최솟값은?", a,
               f"P = {{x | x < {m(a)}}} ⊂ Q = {{x | x < k}}이어야 합니다.\nk ≥ {m(a)}일 때 성립 → k의 최솟값 {m(a)}", "P ⊂ Q가 되도록 수직선에 그려 보세요.")

def c3l1_quad(r):
    a, b = r.sample(range(-5, 7), 2)
    return num(f"실수 전체에서 조건 '{poly((1, 'x²'), (-(a + b), 'x'), (a * b, ''))} = 0'의 진리집합의 원소의 합은?", a + b,
               f"인수분해: (x{term(-a)})(x{term(-b)}) = 0 → x = {m(a)} 또는 {m(b)}\n진리집합 {{{m(a)}, {m(b)}}}, 합 {m(a + b)}", "방정식의 해가 진리집합입니다.")

L31 = [("진리집합", c3l1_truth), ("조건의 부정", c3l1_neg), ("배수·약수 명제", c3l1_mult), ("반례", c3l1_counter), ("참이 되는 범위", c3l1_param), ("방정식의 진리집합", c3l1_quad)]

def c3l2_conv(r):
    a, b = r.sample([2, 3, 4, 6, 8, 9, 12, 18], 2)
    orig = 1 if a % b == 0 else 0; conv = 1 if b % a == 0 else 0
    kind = r.choice(["역", "이", "대우"])
    v = orig if kind == "대우" else conv
    stmt = f"'x가 {a}의 배수이면 x는 {b}의 배수이다'"
    forms = {"역": f"x가 {b}의 배수이면 x는 {a}의 배수이다", "이": f"x가 {a}의 배수가 아니면 x는 {b}의 배수가 아니다", "대우": f"x가 {b}의 배수가 아니면 x는 {a}의 배수가 아니다"}
    why_o = f"{a}의 배수는 모두 {b}의 배수입니다({a} = {b} × {a // b})." if orig else f"{a}의 배수 {a}는 {b}의 배수가 아닙니다."
    why_c = f"{b}의 배수는 모두 {a}의 배수입니다({b} = {a} × {b // a})." if conv else f"{b}의 배수 {b}는 {a}의 배수가 아닙니다."
    return num(f"명제 {stmt}의 {kind}{TF}", v,
               f"{kind}: '{forms[kind]}'\n" + ("대우는 원래 명제와 참·거짓이 같습니다.\n원래 명제: " + why_o if kind == "대우" else
               ("역: " if kind == "역" else "이는 역의 대우이므로 역과 참·거짓이 같습니다.\n역: ") + why_c) + f"\n따라서 {'참 → 1' if v else '거짓 → 0'}",
               "대우 ↔ 원래 명제, 이 ↔ 역 은 참·거짓이 같습니다.")

def c3l2_ineq(r):
    a, b = r.sample(range(-3, 6), 2)
    orig = 1 if a >= b else 0
    kind = r.choice(["원래 명제", "역", "대우"])
    v = {"원래 명제": orig, "대우": orig, "역": 1 if b >= a else 0}[kind]
    return num(f"'x > {m(a)}이면 x > {m(b)}'의 {kind}{TF}" if kind != "원래 명제" else f"'x > {m(a)}이면 x > {m(b)}'{TF}", v,
               (f"역: 'x > {m(b)}이면 x > {m(a)}'\n" if kind == "역" else "") + (f"대우는 원래 명제와 참·거짓이 같습니다.\n" if kind == "대우" else "") +
               f"{'{x | x > ' + m(b) + '} ⊂ {x | x > ' + m(a) + '}' if kind == '역' else '{x | x > ' + m(a) + '} ⊂ {x | x > ' + m(b) + '}'}" +
               (" 성립 → 참" if v else " 불성립 → 거짓"), "진리집합의 포함 관계로 판단하세요.")

def c3l2_chain(r):
    p, q, s = r.sample(["p", "q", "r", "s"], 3)
    t = r.choice([0, 1])
    if t == 0:
        return fill(f"{p} → {q}, {q} → {s}가 참이면 {{{{1}}}} → {s}도 참", [[p]],
                    f"삼단논법: {p} → {q}이고 {q} → {s}이면 {p} → {s}\n진리집합으로 보면 포함 관계가 이어지기 때문입니다.\n따라서 빈칸은 {p}", "포함 관계가 이어집니다.")
    return fill(f"{p} → {q}, ~{s} → ~{q}가 참이면 {p} → {{{{1}}}}도 참", [[s]],
                f"~{s} → ~{q}의 대우는 {q} → {s} (대우도 참)\n{p} → {q}, {q} → {s}이므로 삼단논법으로 {p} → {s}\n따라서 빈칸은 {s}", "먼저 대우로 바꾸세요.")

def c3l2_contra(r):
    a = r.randint(1, 9)
    pool = [(f"'x = {a}이면 x² = {a * a}'의 대우는 'x² ≠ {a * a}이면 x {{{{1}}}} {a}'", "≠", "대우: 가정과 결론을 바꾸고 둘 다 부정"),
            (f"'x = {a}이면 x² = {a * a}'의 역은 'x² = {a * a}이면 x = {{{{1}}}}'", str(a), "역: 가정과 결론을 바꿈"),
            (f"'x > {a}이면 x² > {a * a}'의 대우는 'x² ≤ {a * a}이면 x {{{{1}}}} {a}'", "≤", "대우: 가정과 결론을 바꾸고 둘 다 부정 (>의 부정은 ≤)")]
    p, ans_, e = r.choice(pool)
    return fill(p, [[ans_, {"≤": "<="}.get(ans_, ans_)]], e + f"\n따라서 빈칸은 {ans_}", "역·이·대우의 정의를 떠올리세요.")

L32 = [("배수 명제의 역·이·대우", c3l2_conv), ("부등식 명제", c3l2_ineq), ("삼단논법", c3l2_chain), ("역과 대우 만들기", c3l2_contra)]

CH = "  (① 충분조건  ② 필요조건  ③ 필요충분조건 중 번호)"
def c3l3_ineq(r):
    a, b = r.sample(range(-3, 8), 2)
    v = 1 if a > b else 2
    return num(f"x > {m(a)}는 x > {m(b)}이기 위한 조건입니다.{CH}", v,
               f"P = {{x | x > {m(a)}}}, Q = {{x | x > {m(b)}}}\n" + (f"{m(a)} > {m(b)}이므로 P ⊂ Q → p ⇒ q, 역은 거짓 → 충분조건(①)" if v == 1 else f"{m(a)} < {m(b)}이므로 Q ⊂ P → q ⇒ p → 필요조건(②)"),
               "작은 집합이 큰 집합의 충분조건입니다.")

def c3l3_mult(r):
    a, b = r.choice([(4, 2), (6, 3), (6, 2), (12, 4), (10, 5), (9, 3), (12, 6), (8, 4)])
    if r.random() < .5:
        return num(f"'x는 {a}의 배수'는 'x는 {b}의 배수'이기 위한 조건입니다.{CH}", 1,
                   f"{a}의 배수는 모두 {b}의 배수 → p ⇒ q\n{b}의 배수 중 {a}의 배수가 아닌 것({b})이 있어 역은 거짓 → 충분조건(①)", "어느 쪽 집합이 더 작은지 보세요.")
    return num(f"'x는 {b}의 배수'는 'x는 {a}의 배수'이기 위한 조건입니다.{CH}", 2,
               f"{a}의 배수 ⇒ {b}의 배수 (q ⇒ p)\n반대는 거짓 → 필요조건(②)", "어느 쪽 집합이 더 작은지 보세요.")

def c3l3_suff(r):
    a, b = r.randint(-5, 2), r.randint(3, 9)
    t = r.choice(["suff", "nec"])
    if t == "suff":
        return num(f"p: {m(a)} < x < {b}, q: x < k일 때 p가 q이기 위한 충분조건이 되는 k의 최솟값은?", b,
                   f"p ⇒ q이려면 P ⊂ Q: 구간 ({m(a)}, {b})가 x < k 안에 들어가야 합니다.\nk ≥ {b} → 최솟값 {b}", "P ⊂ Q가 되도록 수직선에 그려 보세요.")
    return num(f"p: x ≤ k, q: x ≤ {b}일 때 p가 q이기 위한 필요조건이 되는 k의 최솟값은?", b,
               f"p가 필요조건 ⇔ q ⇒ p ⇔ Q ⊂ P\nx ≤ {b} ⊂ x ≤ k이려면 k ≥ {b} → 최솟값 {b}", "필요조건이면 Q ⊂ P입니다.")

def c3l3_iff(r):
    a, b = r.sample(range(-4, 7), 2)
    return num(f"p: {poly((1, 'x²'), (-(a + b), 'x'), (a * b, ''))} = 0, q: x = k 또는 x = {m(b)}일 때 p가 q이기 위한 필요충분조건이 되는 k의 값은?", a,
               f"P = {{{m(a)}, {m(b)}}}  (인수분해: (x{term(-a)})(x{term(-b)}) = 0)\nQ = {{k, {m(b)}}}\nP = Q이어야 하므로 k = {m(a)}", "필요충분조건 ⇔ 진리집합이 같다")

L33 = [("부등식의 조건", c3l3_ineq), ("배수의 조건", c3l3_mult), ("충분·필요조건의 범위", c3l3_suff), ("필요충분조건", c3l3_iff)]

def c3l4_amgm(r):
    k = r.randint(1, 8)
    t = r.choice(["min", "at", "ab", "max"])
    if t == "min":
        return num(f"x > 0일 때 x + {k * k}/x의 최솟값은?", 2 * k,
                   f"산술·기하평균: x + {k * k}/x ≥ 2√(x × {k * k}/x) = 2√{k * k} = {2 * k}\n(x = {k}일 때 등호)", "a + b ≥ 2√(ab)")
    if t == "at":
        return num(f"x > 0일 때 x + {k * k}/x가 최솟값을 가지는 x의 값은?", k,
                   f"등호는 x = {k * k}/x일 때 성립\nx² = {k * k}, x > 0 → x = {k}", "등호 조건: 두 항이 같을 때")
    if t == "ab":
        return num(f"a > 0, b > 0, ab = {k * k}일 때 a + b의 최솟값은?", 2 * k,
                   f"a + b ≥ 2√(ab) = 2√{k * k} = {2 * k}\n(a = b = {k}일 때 등호)", "산술·기하평균의 관계")
    return num(f"a > 0, b > 0, a + b = {2 * k}일 때 ab의 최댓값은?", k * k,
               f"{2 * k} = a + b ≥ 2√(ab) → √(ab) ≤ {k} → ab ≤ {k * k}\n(a = b = {k}일 때 등호)", "합이 일정하면 곱은 두 수가 같을 때 최대")

def c3l4_shift(r):
    c, k = r.randint(1, 5), r.randint(1, 6)
    return num(f"x > {c}일 때 x + {k * k}/(x − {c})의 최솟값은?", 2 * k + c,
               f"x + {k * k}/(x − {c}) = (x − {c}) + {k * k}/(x − {c}) + {c}\nx − {c} > 0이므로 ≥ 2√{k * k} + {c} = {2 * k + c}\n(x − {c} = {k}, 즉 x = {k + c}일 때 등호)",
               f"x − {j(c, '를을')} 한 덩어리로 보세요.")

def c3l4_cs(r):
    a, b = r.sample([1, 2, 3, 4], 2)
    s = a * a + b * b
    return num(f"실수 x, y가 x² + y² = {s}를 만족할 때 {poly((a, 'x'), (b, 'y'))}의 최댓값은?", s,
               f"코시–슈바르츠: ({a}x + {b}y)² ≤ ({a}² + {b}²)(x² + y²) = {s} × {s}\n따라서 {poly((a, 'x'), (b, 'y'))} ≤ {s}\n(x : y = {a} : {b}, 즉 x = {a}, y = {b}일 때 등호)",
               "(ax + by)² ≤ (a² + b²)(x² + y²)")

def c3l4_odd(r):
    m_, rem = r.choice([(2, 1), (3, 1), (3, 2), (4, 1), (4, 3), (5, 2)])
    return fill(f"n = {m_}k + {rem}이면 n² = {m_ * m_}k² + {{{{1}}}}k + {{{{2}}}}", [str(2 * m_ * rem), str(rem * rem)],
                f"({m_}k + {rem})² = {m_ * m_}k² + 2 × {m_}k × {rem} + {rem}²\n= {m_ * m_}k² + {2 * m_ * rem}k + {rem * rem}",
                "(a + b)² = a² + 2ab + b²")

L34 = [("산술·기하평균", c3l4_amgm), ("한 덩어리로 보기", c3l4_shift), ("코시–슈바르츠 부등식", c3l4_cs), ("직접 증명의 식 계산", c3l4_odd)]

# ================= ch04 방정식 =================
def c4l1_roots(r):
    a, b = r.sample(range(-6, 8), 2)
    return fill(f"{poly((1, 'x²'), (-(a + b), 'x'), (a * b, ''))} = 0의 두 근은 {{{{1}}}}, {{{{2}}}}", [ans(a), ans(b)],
                f"곱이 {m(a * b)}, 합이 {m(a + b)}인 두 수: {j(a, '와과', m(a))} {m(b)}\n(x{term(-a)})(x{term(-b)}) = 0 → x = {m(a)} 또는 {m(b)}",
                "인수분해해 보세요.", unordered=[[1, 2]])

def c1q_formula(r):
    b, c = nz(r, -5, 5), r.randint(-8, 6)
    D = b * b - c
    if D <= 0 or isqrt(D) ** 2 == D: return None
    return fill(f"{poly((1, 'x²'), (-2 * b, 'x'), (c, ''))} = 0의 근은 x = {m(b)} ± √{{{{1}}}}", [str(D)],
                f"짝수 공식: x = b' ± √(b'² − ac), b' = {m(b)}\nx = {m(b)} ± √({b * b}{term(-c)}) = {m(b)} ± √{D}", "근의 공식(짝수 공식)을 쓰세요.")

def c4l1_cpx(r):
    a, b = r.randint(-4, 4), r.randint(1, 5)
    c = a * a + b * b
    return fill(f"{poly((1, 'x²'), (-2 * a, 'x'), (c, ''))} = 0의 근은 x = " + (f"{m(a)} ± {{{{1}}}}i" if a else "±{{1}}i"), [str(b)],
                f"x = {m(a)} ± √({a * a} − {c}) = {m(a)} ± √(−{b * b}) = {m(a)} ± {b}i" if a else f"x² = −{b * b} → x = ±{b}i",
                "판별식이 음수이면 허근입니다.")

def c4l1_abs(r):
    a, b = r.randint(-5, 6), r.randint(1, 8)
    return num(f"|x{term(-a)}| = {b}의 모든 해의 합은?", 2 * a,
               f"x{term(-a)} = {b} 또는 x{term(-a)} = −{b}\nx = {m(a + b)} 또는 x = {m(a - b)}\n합: {m(2 * a)}", "절댓값 안이 ±값이 되는 두 경우")

def c4l1_abs2(r):
    p, q, s = r.randint(2, 3), r.randint(-4, 4), r.randint(1, 6)
    # |px − q| = x + s
    sols = []
    for sg in (1, -1):
        x = F(s + sg * q, sg * p - 1) if sg * p - 1 != 0 else None
        # sg*(px − q) = x + s → (sg p − 1) x = s + sg q
        if x is not None and x + s >= 0 and sg * (p * x - q) >= 0: sols.append(x)
    if len(sols) != 2: return None
    v = sum(sols)
    return num(f"|{p}x{term(-q)}| = x + {s}의 모든 해의 합은? (기약분수 또는 정수로)", v,
               f"{p}x{term(-q)} ≥ 0일 때: {p}x{term(-q)} = x + {s} → x = {fm(sols[0])}\n{p}x{term(-q)} < 0일 때: −({p}x{term(-q)}) = x + {s} → x = {fm(sols[1])}\n두 해 모두 조건을 만족 → 합 {fm(v)}",
               "절댓값 안의 부호로 경우를 나누고, 구한 해가 그 경우에 맞는지 확인하세요.", fmt="fraction" if v.denominator > 1 else "integer")

def c4l1_other(r):
    a, b = r.sample(range(-5, 8), 2); s = a + b
    return num(f"{poly((1, 'x²'), (-s, 'x'))} + k = 0의 한 근이 {m(a)}일 때 다른 한 근은?", b,
               f"두 근의 합 = {m(s)} (근과 계수의 관계)\n다른 근 = {m(s)} − {par(a)} = {m(b)}\n(참고: k = {m(a)} × {par(b)} = {m(a * b)})", "근과 계수의 관계를 쓰면 빠릅니다.")

def c4l1_rect(r):
    w, d = r.randint(3, 12), r.randint(1, 6)
    return num(f"가로가 세로보다 {d} 긴 직사각형의 넓이가 {w * (w + d)}입니다. 세로의 길이는?", w,
               f"세로를 x라 하면 x(x + {d}) = {w * (w + d)}\nx² + {d}x − {w * (w + d)} = 0 → (x − {w})(x + {w + d}) = 0\nx > 0이므로 x = {w}",
               "길이는 양수인 근만 답이 됩니다.")

L41 = [("인수분해로 풀기", c4l1_roots), ("근의 공식", c1q_formula), ("허근", c4l1_cpx), ("절댓값 방정식", c4l1_abs),
       ("경우를 나누는 절댓값 방정식", c4l1_abs2), ("다른 한 근", c4l1_other), ("이차방정식의 활용", c4l1_rect)]

def quad(r):
    while True:
        a, b, c = r.choice([1, 1, 2, 3]), nz(r, -8, 8), nz(r, -8, 8)
        return a, b, c

def c4l2_D(r):
    a, b, c = quad(r); D = b * b - 4 * a * c
    t = r.choice(["D", "cnt"])
    if t == "D":
        return num(f"{poly((a, 'x²'), (b, 'x'), (c, ''))} = 0의 판별식 D의 값은?", D, f"D = b² − 4ac = {par(b)}² − 4×{a}×{par(c)} = {b * b} {'−' if 4 * a * c > 0 else '+'} {abs(4 * a * c)} = {m(D)}", "D = b² − 4ac")
    v = 2 if D > 0 else 1 if D == 0 else 0
    return num(f"{poly((a, 'x²'), (b, 'x'), (c, ''))} = 0의 서로 다른 실근은 몇 개일까요?", v,
               f"D = b² − 4ac = {par(b)}² − 4×{a}×{par(c)} = {m(D)}\n" + ("D > 0 → 서로 다른 두 실근" if D > 0 else "D = 0 → 중근(실근 1개)" if D == 0 else "D < 0 → 허근(실근 0개)"), "판별식의 부호를 보세요.")

def c4l2_k(r):
    a = nz(r, -6, 6)
    t = r.choice(["double", "imag"])
    if t == "double":
        return num(f"x² {'+' if a > 0 else '−'} {abs(2 * a)}x + k = 0이 중근을 가질 때 k의 값은?", a * a,
                   f"중근 ⇔ D/4 = {a}² − k = 0\nk = {a * a}", "D = 0")
    return num(f"x² {'+' if a > 0 else '−'} {abs(2 * a)}x + k = 0이 허근을 가지는 정수 k의 최솟값은?", a * a + 1,
               f"허근 ⇔ D/4 = {a * a} − k < 0 ⇔ k > {a * a}\n정수 k의 최솟값 {a * a + 1}", "D < 0")

def c4l2_vieta(r):
    a, b, c = quad(r)
    t = r.choice(["sum", "prod", "sq", "inv", "diff"])
    s, p = F(-b, a), F(c, a)
    pe = poly((a, 'x²'), (b, 'x'), (c, ''))
    if t == "sum": return num(f"{pe} = 0의 두 근의 합은?", s, f"ax² + bx + c = 0에서 a = {a}, b = {m(b)}\n두 근의 합 α + β = −b/a = {m(-b)}/{a} = {fm(s)}", "근과 계수의 관계", fmt="fraction" if s.denominator > 1 else "integer")
    if t == "prod": return num(f"{pe} = 0의 두 근의 곱은?", p, f"ax² + bx + c = 0에서 a = {a}, c = {m(c)}\n두 근의 곱 αβ = c/a = {m(c)}/{a} = {fm(p)}", "근과 계수의 관계", fmt="fraction" if p.denominator > 1 else "integer")
    if t == "sq":
        v = s * s - 2 * p
        return num(f"{pe} = 0의 두 근 α, β에 대해 α² + β²의 값은?", v, f"α + β = {fm(s)}, αβ = {fm(p)}\nα² + β² = (α + β)² − 2αβ = {fm(s * s)} − {fm(2 * p)} = {fm(v)}", "(α + β)² − 2αβ", fmt="fraction" if v.denominator > 1 else "integer")
    if t == "inv":
        v = s / p
        return num(f"{pe} = 0의 두 근 α, β에 대해 1/α + 1/β의 값은?", v, f"α + β = {fm(s)}, αβ = {fm(p)}\n1/α + 1/β = (α + β)/(αβ) = {fm(s)} ÷ {fpar(p)} = {fm(v)}", "통분하면 (α + β)/(αβ)", fmt="fraction" if v.denominator > 1 else "integer")
    v = s * s - 4 * p
    return num(f"{pe} = 0의 두 근 α, β에 대해 (α − β)²의 값은?", v, f"(α − β)² = (α + β)² − 4αβ = {fm(s * s)} − {fm(4 * p)} = {fm(v)}", "(α + β)² − 4αβ", fmt="fraction" if v.denominator > 1 else "integer")

def c4l2_make(r):
    t = r.choice(["int", "sqrt", "cpx"])
    if t == "int":
        a, b = r.sample(range(-5, 8), 2)
        return fill(f"두 근이 {m(a)}, {m(b)}인 이차방정식은 x² + {{{{1}}}}x + {{{{2}}}} = 0", [ans(-(a + b)), ans(a * b)],
                    f"x² − (두 근의 합)x + (두 근의 곱) = 0\n합 {m(a + b)}, 곱 {m(a * b)}\n→ {poly((1, 'x²'), (-(a + b), 'x'), (a * b, ''))} = 0", "x² − (합)x + (곱) = 0")
    p, q = nz(r, -3, 4), r.choice([2, 3, 5, 6, 7])
    if t == "sqrt":
        return fill(f"두 근이 {m(p)} + √{q}, {m(p)} − √{q}인 이차방정식은 x² + {{{{1}}}}x + {{{{2}}}} = 0", [ans(-2 * p), ans(p * p - q)],
                    f"합: {m(2 * p)}, 곱: ({m(p)} + √{q})({m(p)} − √{q}) = {par(p)}² − {q} = {m(p * p - q)}\n→ x² − (합)x + (곱) = {poly((1, 'x²'), (-2 * p, 'x'), (p * p - q, ''))} = 0", "x² − (합)x + (곱) = 0")
    return fill(f"두 근이 {cpx(p, q)}, {cpx(p, -q)}인 이차방정식은 x² + {{{{1}}}}x + {{{{2}}}} = 0", [ans(-2 * p), ans(p * p + q * q)],
                f"합: {m(2 * p)}, 곱: {p}² + {q}² = {p * p + q * q}\n→ {poly((1, 'x²'), (-2 * p, 'x'), (p * p + q * q, ''))} = 0", "켤레복소수의 곱은 a² + b²")

L42 = [("판별식", c4l2_D), ("판별식으로 k 구하기", c4l2_k), ("근과 계수의 관계", c4l2_vieta), ("두 근으로 방정식 만들기", c4l2_make)]

def c4l3_cubic(r):
    rs = r.sample([-3, -2, -1, 1, 2, 3, 4, 5], 3)
    s, p2, p3 = sum(rs), rs[0] * rs[1] + rs[1] * rs[2] + rs[2] * rs[0], rs[0] * rs[1] * rs[2]
    pe = poly((1, 'x³'), (-s, 'x²'), (p2, 'x'), (-p3, ''))
    t = r.choice(["third", "sum", "prod", "pair"])
    if t == "third":
        a, b, c = rs
        return fill(f"{pe} = 0의 세 근은 {m(a)}, {m(b)}, {{{{1}}}}", [ans(c)],
                    f"세 근의 합 = −(x²의 계수) = {m(s)} (근과 계수의 관계)\n나머지 근 = {m(s)} − {par(a)} − {par(b)} = {m(c)}", "세 근의 합 = −(x²의 계수)")
    if t == "sum": return num(f"{pe} = 0의 세 근의 합은?", s, f"x³ + ax² + bx + c = 0의 세 근 α, β, γ에 대해\nα + β + γ = −a = {m(s)}", "근과 계수의 관계")
    if t == "prod": return num(f"{pe} = 0의 세 근의 곱은?", p3, f"x³ + ax² + bx + c = 0의 세 근 α, β, γ에 대해\nαβγ = −c = {m(p3)}", "근과 계수의 관계")
    return num(f"{pe} = 0의 세 근 α, β, γ에 대해 αβ + βγ + γα의 값은?", p2, f"x³ + ax² + bx + c = 0의 세 근 α, β, γ에 대해\nαβ + βγ + γα = b = {m(p2)}", "근과 계수의 관계")

def c4l3_bi(r):
    a, b = r.sample([1, 2, 3, 4], 2)
    t = r.choice(["cnt", "max", "mixed"])
    if t == "mixed":
        return num(f"x⁴ {'+' if b * b - a * a > 0 else '−'} {abs(b * b - a * a)}x² − {a * a * b * b} = 0의 실근은 몇 개일까요?", 2,
                   f"x² = t로 치환: t² {'+' if b * b - a * a > 0 else '−'} {abs(b * b - a * a)}t − {a * a * b * b} = (t − {a * a})(t + {b * b}) = 0\nx² = {a * a} → x = ±{a} (실근 2개)\nx² = −{b * b} → 허근\n따라서 실근 2개", "x² = t로 치환하세요.")
    pe = f"x⁴ − {a * a + b * b}x² + {a * a * b * b} = 0"
    if t == "cnt":
        return num(f"{pe}의 실근은 몇 개일까요?", 4, f"x² = t: t² − {a * a + b * b}t + {a * a * b * b} = (t − {a * a})(t − {b * b}) = 0\nx = ±{a}, ±{b} → 4개", "x² = t로 치환하세요.")
    return num(f"{pe}의 실근 중 가장 큰 값은?", max(a, b), f"(x² − {a * a})(x² − {b * b}) = 0 → x = ±{a}, ±{b}\n가장 큰 값 {max(a, b)}", "x² = t로 치환하세요.")

def c4l3_omega(r):
    while True:
        n, k = r.randint(4, 40), r.randint(2, 30)
        if {n % 3, k % 3} == {1, 2} or (n % 3 == 0 and k % 3 == 0): break
    v = 0 if n % 3 else 3
    return num(f"ω가 x² + x + 1 = 0의 한 근일 때 ω{sup(n)} + ω{sup(k)} + 1의 값은?", v,
               f"ω³ = 1이므로 지수를 3으로 나눈 나머지만 봅니다.\nω{sup(n)} = ω{sup(n % 3) if n % 3 else '⁰'}, ω{sup(k)} = ω{sup(k % 3) if k % 3 else '⁰'}\n" +
               ("ω² + ω + 1 = 0" if v == 0 else "1 + 1 + 1 = 3") + f" → {v}", "ω³ = 1, ω² + ω + 1 = 0")

def c4l3_root(r):
    t, a = r.randint(-3, 3), r.randint(-4, 4)
    b, c = r.randint(-5, 5), None
    if t == 0: return None
    # x³ + a x² + b x + d with root t → d = −(t³ + a t² + b t); ask a given d
    d = r.randint(-8, 8)
    aa = F(-(t ** 3 + b * t + d), t * t)
    if aa.denominator != 1: return None
    return num(f"x³ + ax²{term(b, 'x')}{term(d)} = 0의 한 근이 {m(t)}일 때 a의 값은?", int(aa),
               f"x = {m(t)}를 대입: {m(t ** 3)}{term(t * t, 'a')}{term(b * t)}{term(d)} = 0\n{poly((t * t, 'a'))} = {m(-(t ** 3 + b * t + d))}" + (f" → a = {m(int(aa))}" if t * t != 1 else ""), "근을 대입하면 등식이 성립합니다.")

L43 = [("삼차방정식과 근과 계수", c4l3_cubic), ("복이차방정식", c4l3_bi), ("ω의 성질", c4l3_omega), ("근으로 계수 구하기", c4l3_root)]

def c4l4_sp(r):
    a, b = r.sample(range(-4, 9), 2); x, y = max(a, b), min(a, b)
    return num(f"x + y = {m(x + y)}, xy = {m(x * y)}이고 x > y일 때 x의 값은?", x,
               f"x, y는 {poly((1, 't²'), (-(x + y), 't'), (x * y, ''))} = 0의 두 근\n(t{term(-x)})(t{term(-y)}) = 0 → t = {m(x)}, {m(y)}\nx > y이므로 x = {m(x)}".replace("− −", "+ "),
               "합과 곱을 아는 두 수는 이차방정식의 두 근입니다.")

def c4l4_cyc(r):
    x, y, z = r.randint(-3, 8), r.randint(-3, 8), r.randint(-3, 8)
    ask = r.choice(["x + y + z", "x", "y", "z"])
    v = {"x + y + z": x + y + z, "x": x, "y": y, "z": z}[ask]
    return num(f"x + y = {m(x + y)}, y + z = {m(y + z)}, z + x = {m(z + x)}일 때 {ask}의 값은?", v,
               f"세 식을 모두 더하면 2(x + y + z) = {m(2 * (x + y + z))} → x + y + z = {m(x + y + z)}\n" +
               (f"{ask} = (x + y + z) − ({'y + z' if ask == 'x' else 'z + x' if ask == 'y' else 'x + y'}) = {m(v)}" if ask != "x + y + z" else ""),
               "세 식을 모두 더해 보세요.")

def c4l4_sq(r):
    x, y = r.randint(1, 6), r.randint(-5, 5)
    if x == y or x - y <= 0: return None
    d, s = x - y, x * x + y * y
    # other solution: x = y + d → 2y² + 2dy + d² − s = 0 → y = y or y2
    y2 = -d - y; x2 = y2 + d
    if x2 > 0 and x2 != x: return None
    ask = r.choice(["x", "y"])
    return num(f"x − y = {d}, x² + y² = {s}의 해 중 x > 0인 해의 {ask}의 값은?", x if ask == "x" else y,
               f"x = y + {d}를 대입: (y + {d})² + y² = {s}\n{poly((2, 'y²'), (2 * d, 'y'), (d * d - s, ''))} = 0 → y = {m(y)} 또는 {m(y2)}\n대응하는 x = {m(x)} 또는 {m(x2)}, x > 0인 해: x = {m(x)}, y = {m(y)}",
               "일차식을 한 문자에 대해 풀어 이차식에 대입하세요.")

def c4l4_lin3(r):
    x, y, z = r.randint(-3, 5), r.randint(-3, 5), r.randint(-3, 5)
    return fill(f"x + y + z = {m(x + y + z)}, x − y = {m(x - y)}, y − z = {m(y - z)}의 해는 x = {{{{1}}}}, y = {{{{2}}}}, z = {{{{3}}}}", [ans(x), ans(y), ans(z)],
                f"x = y{term(x - y)}, z = y{term(-(y - z))}를 첫 식에 대입\n3y{term(x - y - (y - z))} = {m(x + y + z)} → y = {m(y)}\nx = {m(x)}, z = {m(z)}",
                "x와 z를 y로 나타내 대입하세요.")

def c4l4_comp(r):
    a, b = nz(r, -5, 5), nz(r, -5, 5)
    return num(f"실수 x, y가 {poly((1, 'x²'), (1, 'y²'), (-2 * a, 'x'), (-2 * b, 'y'), (a * a + b * b, ''))} = 0을 만족할 때 x + y의 값은?", a + b,
               f"완전제곱식으로: (x{term(-a)})² + (y{term(-b)})² = 0\n실수의 제곱의 합이 0이면 각각 0 → x = {m(a)}, y = {m(b)}\nx + y = {m(a + b)}",
               "완전제곱식의 합 = 0 꼴로 바꾸세요.")

def c4l4_rect(r):
    a, b = r.sample(range(2, 15), 2)
    return num(f"둘레가 {2 * (a + b)}, 넓이가 {a * b}인 직사각형의 긴 변의 길이는?", max(a, b),
               f"두 변을 x, y라 하면 x + y = {a + b}, xy = {a * b}\nt² − {a + b}t + {a * b} = 0 → t = {min(a, b)}, {max(a, b)}\n긴 변 {max(a, b)}",
               "두 변의 합과 곱을 구하세요.")

def c4l4_nat(r):
    k = r.choice([1, 2, 3, 5, 7, 8, 11, 15, 17, 23])
    n = k + 1; d = divisors(n)
    return num(f"xy − x − y = {k}을 만족하는 자연수 해 (x, y)는 몇 쌍일까요?", len(d),
               f"양변에 1을 더하면 (x − 1)(y − 1) = {n}\nx − 1, y − 1은 0 이상의 정수이고 곱이 {n} → {n}의 양의 약수 쌍\n" + ", ".join(f"({p}, {n // p})" for p in d) + f" → {len(d)}쌍",
               "인수분해 꼴 (x − 1)(y − 1)을 만드세요.")

L44 = [("합과 곱", c4l4_sp), ("세 식을 더하기", c4l4_cyc), ("일차·이차 연립", c4l4_sq), ("세 미지수 연립", c4l4_lin3),
       ("완전제곱식의 합", c4l4_comp), ("둘레와 넓이", c4l4_rect), ("자연수 해", c4l4_nat)]

ALL = {"ch01": [L11, L12, L13, L14], "ch02": [L21, L22, L23, L24], "ch03": [L31, L32, L33, L34], "ch04": [L41, L42, L43, L44]}

if __name__ == "__main__":
    tot = 0
    for ch, Ls in ALL.items():
        for i, T in enumerate(Ls, 1):
            per = 6 if len(T) >= 7 else 8 if len(T) >= 5 else 10 if len(T) >= 4 else 14
            n = write("c1", ch, f"l0{i}", T, per=per); tot += n; print(ch, i, len(T), n)
    print("total", tot)
