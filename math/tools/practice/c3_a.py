"""코스 3 · 챕터 1~3 (지수, 로그, 지수함수와 로그함수) — 연습 문제 은행"""
from core import *
from math import log10, floor

SUBD = str.maketrans("0123456789()−/", "₀₁₂₃₄₅₆₇₈₉₍₎₋/")
def sb(n): return str(n).translate(SUBD)
def lg(b, x):
    """log_b x 표기"""
    bs = sb(b) if isinstance(b, int) and b > 0 else f"_({b})"
    return f"log{bs} {x}"
def nz(r, a, b):
    while True:
        x = r.randint(a, b)
        if x: return x
def ipow(b, e): return F(b) ** e
def ex(b, e):
    """b^e 표기 (e 정수면 위첨자, 분수면 ^(p/q))"""
    e = F(e)
    bs = str(b) if not isinstance(b, F) or b.denominator == 1 else f"({fs(b)})"
    if e.denominator == 1: return f"{bs}{sup(int(e))}" if int(e) >= 0 else f"{bs}⁻{sup(-int(e))}"
    return f"{bs}^({fm(e)})"
PW = {2: [2, 4, 8, 16, 32, 64, 128], 3: [3, 9, 27, 81, 243], 5: [5, 25, 125, 625], 7: [7, 49, 343], 10: [10, 100, 1000, 10000]}

def frac_ans(v): return dict(fmt="fraction" if F(v).denominator > 1 else "integer")

# ================= ch01 지수 =================
def a1_root(r):
    n = r.choice([2, 3, 4, 5, 6]); a = r.choice([1, -1]) * r.choice([2, 3, 5, 7, 10, 16, 27, 64])
    if n % 2:
        v = 1
        why = f"n이 홀수이면 실수 a의 n제곱근 중 실수는 항상 1개"
    else:
        v = 2 if a > 0 else 0
        why = f"n이 짝수이면 a > 0일 때 ±ⁿ√a로 2개, a < 0일 때 0개"
    names = {2: "제곱근", 3: "세제곱근", 4: "네제곱근", 5: "다섯제곱근", 6: "여섯제곱근"}
    return num(f"{m(a)}의 {names[n]} 중 실수는 몇 개일까요?", v,
               f"x{sup(n)} = {m(a)}의 실근의 개수를 셉니다.\n{why}\n여기서 n = {n}, a = {m(a)} → {v}개", "n의 홀짝과 a의 부호를 보세요.")

def a1_val(r):
    t = r.choice(["cube", "four", "prod", "nest"])
    if t == "cube":
        k = nz(r, -5, 5)
        return num(f"³√{par(k ** 3)}의 값은?", k, f"{par(k)}³ = {m(k ** 3)}이므로 ³√{par(k ** 3)} = {m(k)}\n세제곱근은 음수도 실수 하나가 있습니다.", "세제곱해서 그 수가 되는 실수")
    if t == "four":
        k = r.randint(2, 5)
        return num(f"⁴√{k ** 4}의 값은?", k, f"{k}⁴ = {k ** 4}이고 ⁴√는 양의 네제곱근\n⁴√{k ** 4} = {k}", "네제곱해서 그 수가 되는 양수")
    if t == "prod":
        n = r.choice([2, 3]); a, b = r.choice([(2, 4), (3, 9), (4, 16), (2, 32), (9, 27), (25, 5), (6, 36)]) if n == 3 else r.choice([(2, 8), (3, 12), (5, 20), (2, 18), (6, 24)])
        v = round((a * b) ** (1 / n))
        if v ** n != a * b: return None
        root = "³√" if n == 3 else "√"
        return num(f"{root}{a} × {root}{b}의 값은?", v, f"ⁿ√a × ⁿ√b = ⁿ√(ab)\n{root}{a * b} = {v}  ({v}{sup(n)} = {a * b})", "근호 안끼리 곱하세요.")
    k = r.choice([2, 3]); p, q = r.choice([(2, 3), (3, 2), (2, 2)])
    v = k; N = k ** (p * q)
    return num(f"{'√' if p == 2 else '³√'}({'√' if q == 2 else '³√'}{N})의 값은?", v,
               f"ᵐ√(ⁿ√a) = ᵐⁿ√a\n= {p * q}제곱근 {N} = {v}  ({v}{sup(p * q)} = {N})", "거듭제곱근의 거듭제곱근은 지수를 곱합니다.")

def a1_cmp(r):
    a, m_, b, n = r.choice([(3, 3, 2, 2), (2, 3, 3, 4), (5, 3, 3, 2), (4, 4, 3, 3), (10, 3, 3, 2), (2, 2, 3, 3), (6, 3, 2, 2)])
    L = m_ * n
    A, B = a ** (L // m_), b ** (L // n)
    if A == B: return None
    sg = ">" if A > B else "<"
    rm = {2: "√", 3: "³√", 4: "⁴√"}
    R = sup(L) + "√"
    return fill(f"{rm[m_]}{a} {{{{1}}}} {rm[n]}{b}  (부등호 >, < 중 하나)", [[sg]],
                f"{L}제곱근으로 맞춥니다.\n{rm[m_]}{a} = {R}({a}{sup(L // m_)}) = {R}{A}\n{rm[n]}{b} = {R}({b}{sup(L // n)}) = {R}{B}\n{A} {sg} {B}이므로 {rm[m_]}{a} {sg} {rm[n]}{b}",
                "같은 차수의 거듭제곱근으로 바꾸세요.")

L11 = [("실수인 거듭제곱근의 개수", a1_root), ("거듭제곱근의 값", a1_val), ("거듭제곱근의 대소", a1_cmp)]

def a2_val(r):
    b = r.choice([2, 3, 4, 5, 8, 9, 16, 25, 27, 32, 64, 81])
    base = {4: 2, 8: 2, 16: 2, 32: 2, 64: 2, 9: 3, 27: 3, 81: 3, 25: 5}.get(b, b)
    k = 1
    while base ** k != b: k += 1
    q = r.choice([d for d in (1, 2, 3, 4, 5, 6) if k % d == 0 or d == 1])
    p = r.choice([1, 2, 3, -1, -2, -3])
    e = F(p, q)
    if e.denominator != q: return None
    v = F(base) ** (k * e)
    if (k * e).denominator != 1 or abs(v) > 3000 or v < F(1, 1000): return None
    return num(f"{ex(b, e)}의 값은? (기약분수 또는 정수로)", v,
               f"{b} = {base}{sup(k)}이므로 {ex(b, e)} = {base}^({k} × {fm(e)}) = {ex(base, k * e)}\n= {fm(v)}", "밑을 소수의 거듭제곱으로 바꾸세요.", **frac_ans(v))

def a2_form(r):
    t = r.choice(["root", "inv", "asa", "sq"])
    m_, n = r.randint(2, 7), r.randint(2, 6)
    rt = "√" if n == 2 else sup(n) + "√"
    if t == "root":
        if gcd(m_, n) > 1: return None
        return fill(f"{rt}(a{sup(m_)}) = a^({m_}/{{{{1}}}})", [str(n)],
                    f"ⁿ√(aᵐ) = a^(m/n)\n여기서 m = {m_}, n = {n} → a^({m_}/{n})", "근호의 차수가 분모가 됩니다.")
    if t == "inv":
        return fill(f"1/{rt}a = a^(−1/{{{{1}}}})", [str(n)], f"ⁿ√a = a^(1/n), 역수는 지수의 부호를 바꿉니다.\n1/ⁿ√a = a^(−1/{n})", "역수 = 음의 지수")
    if t == "asa":
        k = r.randint(1, 4)
        return fill(f"a{sup(k) if k > 1 else ''}√a = a^({{{{1}}}}/2)", [str(2 * k + 1)], f"a{sup(k) if k > 1 else ''} = a^({2 * k}/2), √a = a^(1/2)\n곱하면 지수를 더해 a^({2 * k + 1}/2)", "지수를 분모 2로 통일하세요.")
    b = r.choice([2, 3, 5, 6, 7])
    return fill(f"{b}^(1/2) = √{{{{1}}}}", [str(b)], f"a^(1/2)은 a의 양의 제곱근입니다.\n{b}^(1/2) = √{b}", "지수 1/2 = 제곱근")

def a2_neg(r):
    a, k = r.choice([2, 3, 4, 5, 10]), r.randint(1, 4)
    t = r.choice(["neg", "recip"])
    if t == "neg":
        v = F(1, a ** k)
        return num(f"{a}⁻{sup(k)}의 값은? (기약분수로)", v, f"a⁻ⁿ = 1/aⁿ\n{a}⁻{sup(k)} = 1/{a}{sup(k)} = {fs(v)}", "음의 지수는 역수", fmt="fraction")
    return num(f"(1/{a})⁻{sup(k)}의 값은?", a ** k, f"(1/a)⁻ⁿ = aⁿ\n(1/{a})⁻{sup(k)} = {a}{sup(k)} = {a ** k}", "역수의 음의 지수")

L12 = [("유리수 지수의 값", a2_val), ("거듭제곱근 ↔ 지수", a2_form), ("음의 지수", a2_neg)]

def a3_law(r):
    b = r.choice([2, 3, 5]); p, q = F(r.randint(-3, 5), r.choice([1, 2, 3])), F(r.randint(-3, 5), r.choice([1, 2, 3]))
    t = r.choice(["mul", "div"])
    e = p + q if t == "mul" else p - q
    if e.denominator != 1 or abs(e) > 8: return None
    v = F(b) ** int(e)
    return num(f"{ex(b, p)} {'×' if t == 'mul' else '÷'} {ex(b, q)}의 값은? (기약분수 또는 정수로)", v,
               f"밑이 같으면 지수를 {'더합니다' if t == 'mul' else '뺍니다'}.\n{fm(p)} {'+' if t == 'mul' else '−'} {fpar(q)} = {fm(e)}\n{ex(b, e)} = {fm(v)}", "aˣ × aʸ = aˣ⁺ʸ, aˣ ÷ aʸ = aˣ⁻ʸ", **frac_ans(v))

def a3_mixed(r):
    b = r.choice([2, 3]); k1, k2 = r.sample([1, 2, 3, 4, 5], 2)
    p, q = F(r.randint(1, 4), r.choice([1, 2, 3])), F(r.randint(-3, 3), r.choice([1, 2, 3]))
    e = k1 * p + k2 * q
    if e.denominator != 1 or not 0 <= e <= 10 or (p.denominator == 1 and q.denominator == 1) or q == 0: return None
    v = b ** int(e)
    return num(f"{ex(b ** k1, p)} × {ex(b ** k2, q)}의 값은?", v,
               f"{b ** k1} = {b}{sup(k1)}, {b ** k2} = {b}{sup(k2)}\n지수: {k1} × {fm(p)} + {k2} × {fpar(q)} = {fm(e)}\n{b}{sup(int(e))} = {v}", "밑을 같게 맞추세요.")

def a3_solve(r):
    b = r.choice([2, 3]); k1, k2 = r.sample([2, 3, 4, 5], 2)
    x = F(k2, k1)
    return num(f"{b ** k1}ˣ = {b ** k2}일 때 x의 값은? (기약분수 또는 정수로)", x,
               f"{b ** k1} = {b}{sup(k1)}, {b ** k2} = {b}{sup(k2)}\n{b}^({k1}x) = {b}{sup(k2)} → {k1}x = {k2} → x = {fm(x)}", "밑을 같게 만들어 지수를 비교하세요.", **frac_ans(x))

def a3_sym(r):
    t = r.randint(3, 7)
    if r.random() < .5:
        return num(f"2ˣ + 2⁻ˣ = {t}일 때 4ˣ + 4⁻ˣ의 값은?", t * t - 2,
                   f"(2ˣ + 2⁻ˣ)² = 4ˣ + 2 + 4⁻ˣ\n4ˣ + 4⁻ˣ = {t}² − 2 = {t * t - 2}", "제곱하면 가운데 항이 2")
    return num(f"a^(1/2) + a^(−1/2) = {t}일 때 a + a⁻¹의 값은?", t * t - 2,
               f"(a^(1/2) + a^(−1/2))² = a + 2 + a⁻¹\na + a⁻¹ = {t}² − 2 = {t * t - 2}", "제곱해 보세요.")

L13 = [("지수법칙", a3_law), ("밑을 맞춰 계산", a3_mixed), ("지수 방정식(기본)", a3_solve), ("대칭식", a3_sym)]

def a4_growth(r):
    t = r.choice(["dbl", "tri", "half"])
    if t == "dbl":
        a, n = r.choice([100, 500, 1000, 3000]), r.randint(2, 6)
        return num(f"{a:,}원이 매년 2배가 되면 {n}년 후에는 얼마일까요?", a * 2 ** n, f"{a} × 2{sup(n)} = {a} × {2 ** n} = {a * 2 ** n}원", "a × 2ⁿ")
    if t == "tri":
        a, n = r.choice([10, 50, 100]), r.randint(2, 5)
        return num(f"세균 {a}마리가 1시간마다 3배가 되면 {n}시간 후에는 몇 마리일까요?", a * 3 ** n, f"{a} × 3{sup(n)} = {a} × {3 ** n} = {a * 3 ** n}마리", "a × 3ⁿ")
    h, k = r.choice([2, 3, 5, 10]), r.randint(2, 5); a = 2 ** k * r.choice([1, 3, 5, 25])
    T = h * r.randint(1, k)
    return num(f"반감기가 {h}년인 물질 {a}g은 {T}년 후 몇 g이 남을까요?", a // 2 ** (T // h),
               f"{T} ÷ {h} = {T // h}번 반감 → {a} × (1/2){sup(T // h)} = {a // 2 ** (T // h)}g", "반감기마다 절반")

def a4_eq(r):
    b = r.choice([2, 3, 5]); x = r.randint(-3, 5); c = r.randint(-3, 3)
    t = r.choice(["shift", "recip"])
    if t == "shift":
        rhs = F(b) ** (x + c)
        return num(f"{b}^(x{term(c)}) = {fm(rhs)}의 해는?", x, f"{fm(rhs)} = {ex(b, x + c)}\nx{term(c)} = {x + c} → x = {m(x)}", "우변을 같은 밑으로 쓰세요.")
    rhs = F(1, b) ** x
    return num(f"(1/{b})ˣ = {fm(rhs)}의 해는?", x, f"(1/{b})ˣ = {b}⁻ˣ, {fm(rhs)} = {ex(b, -x)}\n−x = {m(-x)} → x = {m(x)}", "(1/b)ˣ = b⁻ˣ")

def a4_quad(r):
    b = r.choice([2, 3]); p, q = r.sample([1, 2, 3, 4], 2)
    P, Q = b ** p, b ** q
    return num(f"{b * b}ˣ − {P + Q} × {b}ˣ + {P * Q} = 0의 모든 해의 합은?", p + q,
               f"{b}ˣ = t (t > 0)로 놓으면 t² − {P + Q}t + {P * Q} = 0 → (t − {P})(t − {Q}) = 0\nt = {P}, {Q} → x = {p}, {q}\n합 {p + q}", "bˣ = t로 치환하세요.")

def a4_ineq(r):
    b = r.choice([2, 3]); k = r.randint(1, 6)
    t = r.choice(["gt", "lt_inv", "cnt"])
    if t == "gt":
        return num(f"{b}ˣ > {b ** k}의 해가 x > a일 때 a의 값은?", k, f"{b ** k} = {b}{sup(k)}, 밑 {b} > 1이므로 부등호 방향 그대로\nx > {k}", "밑이 1보다 크면 방향 유지")
    if t == "lt_inv":
        return num(f"(1/{b})ˣ < {b ** k}의 해가 x > a일 때 a의 값은?", -k, f"(1/{b})ˣ = {b}⁻ˣ < {b}{sup(k)} → −x < {k} → x > {m(-k)}", "1/b를 b⁻¹로 바꾸세요.")
    return num(f"{b}ˣ ≤ {b ** k}를 만족하는 자연수 x는 몇 개일까요?", k, f"{b}ˣ ≤ {b}{sup(k)} → x ≤ {k}\n자연수 1, …, {k} → {k}개", "지수끼리 비교")

L14 = [("지수적 증가·감소", a4_growth), ("지수방정식", a4_eq), ("치환하는 지수방정식", a4_quad), ("지수부등식", a4_ineq)]

# ================= ch02 로그 =================
def b1_val(r):
    b = r.choice([2, 3, 4, 5, 8, 9, 10, 16, 25, 27])
    base = {4: 2, 8: 2, 16: 2, 9: 3, 27: 3, 25: 5}.get(b, b); kb = 1
    while base ** kb != b: kb += 1
    e = r.randint(-3, 6); X = F(base) ** e
    if X > 100000 or X < F(1, 1000): return None
    v = F(e, kb)
    xs = fs(X) if X.denominator == 1 else f"({fs(X)})"
    return num(f"{lg(b, xs)}의 값은? (기약분수 또는 정수로)", v,
               f"{b}의 몇 제곱이 {fs(X)}인가를 묻습니다.\n{b} = {base}{sup(kb)}, {fs(X)} = {ex(base, e)}\n({base}{sup(kb)})ˣ = {ex(base, e)} → {kb}x = {m(e)}" + (f" → x = {fm(v)}" if kb != 1 else ""), "logₐ b = c ⇔ aᶜ = b", **frac_ans(v))

def b1_inv(r):
    t = r.choice(["x", "base", "power"])
    if t == "x":
        b, k = r.choice([2, 3, 5]), r.randint(1, 5)
        return num(f"{lg(b, 'x')} = {k}일 때 x의 값은?", b ** k, f"logₐ x = c ⇔ x = aᶜ\nx = {b}{sup(k)} = {b ** k}", "지수 꼴로 바꾸세요.")
    if t == "base":
        a, k = r.randint(2, 9), r.choice([2, 3])
        return num(f"logₓ {a ** k} = {k}일 때 x의 값은? (x > 0, x ≠ 1)", a, f"x{sup(k)} = {a ** k} → x = {a} (밑은 양수)", "밑을 미지수로 놓고 지수 꼴로 바꾸세요.")
    b, n = r.choice([2, 3, 5, 10]), r.randint(2, 20)
    return num(f"{b}^({lg(b, n)})의 값은?", n, f"a^(logₐ x) = x\n따라서 {n}", "a^(logₐ x) = x")

def b1_dom(r):
    a, b = sorted(r.sample(range(-2, 9), 2))
    if b - a < 3: return None
    S = [x for x in range(a + 1, b) if x - a != 1]
    return num(f"log_(x{term(-a)}) ({m(b)} − x)가 정의되는 정수 x는 몇 개일까요?", len(S),
               f"밑 조건: x{term(-a)} > 0, x{term(-a)} ≠ 1 → x > {m(a)}, x ≠ {m(a + 1)}\n진수 조건: {m(b)} − x > 0 → x < {m(b)}\n정수: {', '.join(m(z) for z in S)} → {len(S)}개",
               "밑 > 0, 밑 ≠ 1, 진수 > 0")

L21 = [("로그의 값", b1_val), ("로그의 정의 이용", b1_inv), ("로그가 정의될 조건", b1_dom)]

def b2_sum(r):
    b = r.choice([2, 3, 5, 6]); k = r.randint(2, 5); X = b ** k
    if X > 300: return None
    p = r.choice([d for d in divisors(X) if 1 < d < X] or [b])
    t = r.choice(["add", "sub"])
    if t == "add":
        return num(f"{lg(b, p)} + {lg(b, X // p)}의 값은?", k, f"logₐ x + logₐ y = logₐ xy\n{lg(b, X)} = {lg(b, f'{b}{sup(k)}')} = {k}", "곱으로 합치세요.")
    c = r.choice([2, 3, 5, 7]);
    return num(f"{lg(b, X * c)} − {lg(b, c)}의 값은?", k, f"logₐ x − logₐ y = logₐ (x/y)\n{lg(b, f'({X * c}/{c})')} = {lg(b, X)} = {k}", "나눗셈으로 합치세요.")

def b2_coef(r):
    b = r.choice([2, 3, 5]); a, c = r.randint(2, 4), r.randint(2, 4)
    # a log_b (b·k) − log_b (k^a) = a
    k = r.choice([2, 3, 5, 7])
    if k == b: return None
    return num(f"{a} {lg(b, b * k)} − {lg(b, k ** a)}의 값은?", a,
               f"{a} {lg(b, b * k)} = {lg(b, f'{b * k}{sup(a)}')}\n{lg(b, f'({b * k}{sup(a)}/{k}{sup(a)})')} = {lg(b, f'{b}{sup(a)}')} = {a}", "계수를 지수로 올려 합치세요.")

def b2_change(r):
    t = r.choice(["base", "chain", "inv"])
    if t == "base":
        b, x = r.choice([(4, 8), (8, 4), (9, 27), (27, 9), (25, 5), (16, 8), (8, 32), (4, 32), (27, 3), (16, 64)])
        import math
        p = round(math.log(b, 2 if b in (4, 8, 16) else 3 if b in (9, 27) else 5)); q = round(math.log(x, 2 if b in (4, 8, 16) else 3 if b in (9, 27) else 5))
        v = F(q, p)
        return num(f"{lg(b, x)}의 값은? (기약분수 또는 정수로)", v, f"밑 변환: {lg(b, x)} = log {x} / log {b}\n= {q} log c / {p} log c = {fm(v)}  (c는 공통 밑)", "같은 밑의 거듭제곱으로 쓰세요.", **frac_ans(v))
    if t == "chain":
        a, b, k = r.choice([2, 3]), r.choice([5, 7, 3, 6]), r.randint(2, 4)
        if a == b: return None
        return num(f"{lg(a, b)} × {lg(b, a ** k)}의 값은?", k, f"logₐ b × log_b c = logₐ c\n{lg(a, a ** k)} = {k}", "밑 변환하면 사슬처럼 지워집니다.")
    a, b = r.sample([2, 3, 5, 7, 11], 2)
    return num(f"{lg(a, b)} × {lg(b, a)}의 값은?", 1, f"logₐ b × log_b a = (log b / log a) × (log a / log b) = 1", "역수 관계")

L22 = [("로그의 합과 차", b2_sum), ("계수가 있는 로그", b2_coef), ("밑 변환", b2_change)]

L2v = {2: 0.3010, 3: 0.4771}
def b3_digits(r):
    b = r.choice([2, 3]); n = r.randint(10, 100)
    L = n * L2v[b]
    if abs(L - round(L)) < 0.02: return None
    return num(f"log {b} ≈ {L2v[b]:.4f}일 때 {b}{sup(n)}은 몇 자리 수일까요?", floor(L) + 1,
               f"log {b}{sup(n)} = {n} × {L2v[b]:.4f} = {L:.4f}\n정수 부분 {floor(L)} → {floor(L) + 1}자리", "log의 정수 부분 + 1")

def b3_frac(r):
    b = r.choice([2, 3]); n = r.randint(5, 40)
    L = -n * L2v[b]
    if abs(L - round(L)) < 0.02: return None
    return num(f"log {b} ≈ {L2v[b]:.4f}일 때 (1/{b}){sup(n)}은 소수점 아래 몇째 자리에서 처음으로 0이 아닌 숫자가 나타날까요?", -floor(L),
               f"log (1/{b}){sup(n)} = −{n} × {L2v[b]:.4f} = {m(f'{L:.4f}')} = {m(floor(L))} + {L - floor(L):.4f}\n정수 부분 {m(floor(L))} → 소수점 아래 {-floor(L)}째 자리", "정수 부분이 −k이면 k째 자리")

def b3_val(r):
    b = r.choice([2, 3]); k = nz(r, -3, 4)
    v = L2v[b] + k
    X = F(b) * F(10) ** k
    return num(f"log {b} ≈ {L2v[b]:.4f}일 때 log {g_(X)}의 값은?", f"{v:.4f}".rstrip("0").rstrip("."),
               f"{g_(X)} = {b} × 10{sup(k) if k >= 0 else '⁻' + sup(-k)}\nlog {g_(X)} = log {b} + {par(k)} = {L2v[b]:.4f} + {par(k)} = {m(f'{v:.4f}')}", "log (a × 10ⁿ) = log a + n", fmt="decimal")

def g_(x): return f"{float(x):g}" if F(x).denominator != 1 else str(int(x))

def b3_pow10(r):
    k = r.randint(-4, 6)
    return num(f"log {g_(F(10) ** k)}의 값은?", k, f"{g_(F(10) ** k)} = 10{sup(k) if k >= 0 else '⁻' + sup(-k)}\nlog 10ⁿ = n → {m(k)}", "10의 몇 제곱인가")

L23 = [("자릿수", b3_digits), ("소수의 첫 자리", b3_frac), ("상용로그의 값", b3_val), ("10의 거듭제곱", b3_pow10)]

def b4_eq(r):
    t = r.choice(["basic", "sum", "quad"])
    if t == "basic":
        b, k, c = r.choice([2, 3, 5]), r.randint(1, 4), r.randint(-3, 5)
        return num(f"{lg(b, f'(x{term(c)})')} = {k}의 해는?", b ** k - c, f"x{term(c)} = {b}{sup(k)} = {b ** k}\nx = {m(b ** k - c)}\n(진수 {b ** k} > 0 확인)", "지수 꼴로 바꾸세요.")
    if t == "sum":
        b = 2; d = r.randint(1, 6); x = r.randint(d + 1, 12)
        P = x * (x - d)
        if P & (P - 1): return None
        k = P.bit_length() - 1
        return num(f"{lg(b, 'x')} + {lg(b, f'(x − {d})')} = {k}의 해는?", x,
                   f"{lg(b, f'x(x − {d})')} = {k} → x(x − {d}) = {P}\nx² − {d}x − {P} = 0 → x = {x} 또는 {m(-(P // x))}\n진수 조건 x > {d} → x = {x}", "합친 뒤 진수 조건으로 무연근을 버리세요.")
    p, q = r.sample([1, 2, 3, 4], 2); b = r.choice([2, 3])
    return num(f"({lg(b, 'x')})² − {p + q} {lg(b, 'x')} + {p * q} = 0의 두 해의 곱은?", b ** (p + q),
               f"{lg(b, 'x')} = t: t² − {p + q}t + {p * q} = 0 → t = {p}, {q}\nx = {b}{sup(p)}, {b}{sup(q)} → 곱 {b}{sup(p + q)} = {b ** (p + q)}", "log를 t로 치환하세요.")

def b4_ineq(r):
    b, k, c = r.choice([2, 3]), r.randint(1, 4), r.randint(-2, 3)
    t = r.choice(["up", "down"])
    if t == "up":
        S = [x for x in range(-c + 1, b ** k - c)]
        return num(f"{lg(b, f'(x{term(c)})')} < {k}를 만족하는 정수 x는 몇 개일까요?".replace("(x)", "x"), len(S),
                   f"진수 조건: x{term(c)} > 0\n밑 {b} > 1 → x{term(c)} < {b ** k}\n{m(-c)} < x < {m(b ** k - c)} → 정수 {len(S)}개", "진수 조건과 함께 푸세요.")
    S = [x for x in range(-c + 1, b ** k - c)]
    return num(f"log_(1/{b}) (x{term(c)}) > −{k}를 만족하는 정수 x는 몇 개일까요?".replace("(x)", "x"), len(S),
               f"진수 조건: x{term(c)} > 0\n밑 1/{b} < 1 → 부등호 방향이 바뀜: x{term(c)} < (1/{b})⁻{sup(k)} = {b ** k}\n{m(-c)} < x < {m(b ** k - c)} → 정수 {len(S)}개", "밑이 1보다 작으면 방향이 바뀝니다.")

def b4_app(r):
    t = r.choice(["ph", "ratio", "db"])
    if t == "ph":
        k = r.randint(1, 13)
        return num(f"pH = −log [H⁺]입니다. 수소 이온 농도가 10⁻{sup(k)}인 용액의 pH는?", k, f"pH = −log 10⁻{sup(k)} = −(−{k}) = {k}", "log 10ⁿ = n")
    if t == "ratio":
        a, b = sorted(r.sample(range(1, 12), 2))
        return num(f"pH {a}인 용액의 수소 이온 농도는 pH {b}인 용액의 몇 배일까요?", 10 ** (b - a),
                   f"[H⁺] = 10⁻ᵖᴴ → 10⁻{sup(a)} ÷ 10⁻{sup(b)} = 10{sup(b - a)} = {10 ** (b - a)}배", "pH가 1 작으면 농도는 10배")
    k = r.randint(1, 12)
    return num(f"소리의 세기 L = 10 log (I/I₀)(dB)입니다. 세기 I가 I₀의 10{sup(k)}배인 소리는 몇 dB일까요?", 10 * k, f"L = 10 log 10{sup(k)} = 10 × {k} = {10 * k}dB", "log 10ⁿ = n")

L24 = [("로그방정식", b4_eq), ("로그부등식", b4_ineq), ("로그의 활용", b4_app)]

# ================= ch03 지수함수와 로그함수 =================
def c1_asym(r):
    b, p, q = r.choice([2, 3, "1/2", "1/3"]), nz(r, -4, 4), r.randint(-5, 5)
    bs = str(b) if isinstance(b, int) else f"({b})"
    t = r.choice(["exp", "log"])
    if t == "exp":
        return num(f"y = {bs}^(x{term(-p)}){term(q)}의 그래프의 점근선은 직선 y = ?".replace("^(x)", "ˣ"), q,
                   f"y = aˣ의 점근선은 y = 0 (x축)\n평행이동: x축 방향 {m(p)}, y축 방향 {m(q)} → 점근선 y = {m(q)}", "y축 방향 이동만 점근선을 바꿉니다.")
    return num(f"y = log{sb(b) if isinstance(b, int) else '_(' + b + ')'} (x{term(-p)}){term(q)}의 그래프의 점근선은 직선 x = ?".replace("(x)", "x"), p,
               f"y = logₐ x의 점근선은 x = 0 (y축)\nx축 방향으로 {m(p)}만큼 이동 → x = {m(p)}", "x축 방향 이동만 점근선을 바꿉니다.")

def c1_range(r):
    b = r.choice([2, 3, F(1, 2), F(1, 3)]); lo, hi = r.randint(-3, 0), r.randint(1, 4)
    vals = [F(b) ** lo, F(b) ** hi]
    t = r.choice(["max", "min"])
    v = max(vals) if t == "max" else min(vals)
    bs = fs(b) if F(b).denominator == 1 else f"({fs(b)})"
    return num(f"{m(lo)} ≤ x ≤ {hi}에서 y = {bs}ˣ의 {'최댓값' if t == 'max' else '최솟값'}은? (기약분수 또는 정수로)", v,
               f"밑 {fs(b)} {'> 1 → 증가함수' if b > 1 else '< 1 → 감소함수'}\nx = {m(lo)}: {fm(vals[0])}, x = {hi}: {fm(vals[1])}\n{'최댓값' if t == 'max' else '최솟값'} {fm(v)}", "양 끝값을 비교하세요.", **frac_ans(v))

def c1_lrange(r):
    b = r.choice([2, 3]); inv = r.choice([True, False]); a1, a2 = sorted(r.sample(range(-2, 5), 2))
    xs = [F(b) ** a1, F(b) ** a2]
    t = r.choice(["max", "min"])
    vals = [(-a1 if inv else a1), (-a2 if inv else a2)]
    v = max(vals) if t == "max" else min(vals)
    base = f"_(1/{b})" if inv else sb(b)
    return num(f"{fm(xs[0])} ≤ x ≤ {fm(xs[1])}에서 y = log{base} x의 {'최댓값' if t == 'max' else '최솟값'}은?", v,
               f"x = {fm(xs[0])}: {m(vals[0])}, x = {fm(xs[1])}: {m(vals[1])}\n({'감소' if inv else '증가'}함수) → {'최댓값' if t == 'max' else '최솟값'} {m(v)}", "양 끝값")

def c1_comp(r):
    b = r.choice([2, 3]); p, q = r.randint(-3, 3), r.randint(0, 4)
    t = r.choice(["exp", "log"])
    if t == "exp":
        v = F(b) ** q
        return num(f"y = {b}^(x² {'−' if p > 0 else '+'} {abs(2 * p)}x + {p * p + q})의 최솟값은?".replace(" + 0x", "").replace(" − 0x", ""), int(v),
                   f"지수 x²{term(-2 * p, 'x')} + {p * p + q} = (x{term(-p)})² + {q} ≥ {q}\n밑 {b} > 1 → 최솟값 {b}{sup(q)} = {int(v)}", "지수 부분의 최솟값을 먼저 구하세요.")
    k = r.randint(0, 4)
    return num(f"y = {lg(b, f'(x² {chr(8722) if p > 0 else chr(43)} {abs(2 * p)}x + {p * p + b ** k})')}의 최솟값은?".replace(" + 0x", "").replace(" − 0x", ""), k,
               f"진수 (x{term(-p)})² + {b ** k} ≥ {b ** k}\n밑 {b} > 1 → 최솟값 {lg(b, b ** k)} = {k}", "진수의 최솟값을 먼저 구하세요.")

def c1_pass(r):
    b = r.choice([2, 3]); x = r.randint(-2, 5); c = r.randint(-3, 3)
    v = F(b) ** (x + c)
    return num(f"y = {b}^(x{term(c)})의 그래프 위에서 x = {m(x)}인 점의 y좌표는? (기약분수 또는 정수로)".replace("^(x)", "ˣ"), v,
               f"y = {b}^({m(x)}{term(c)}) = {ex(b, x + c)} = {fm(v)}", "x를 대입하세요.", **frac_ans(v))

L31 = [("점근선", c1_asym), ("지수함수의 최대·최소", c1_range), ("그래프 위의 점", c1_pass), ("합성된 최솟값", c1_comp)]
L32 = [("점근선", c1_asym), ("로그함수의 최대·최소", c1_lrange), ("합성된 최솟값", c1_comp)]

def c3_inv(r):
    b, c = r.choice([2, 3]), r.randint(-3, 4); k = r.randint(0, 4)
    t = r.choice(["val", "form"])
    if t == "val":
        return num(f"f(x) = {b}ˣ{term(c)}일 때 f⁻¹({b ** k + c})의 값은?", k, f"f(t) = {b ** k + c} → {b}ᵗ = {b ** k} → t = {k}", "f(t) = 값이 되는 t를 찾으세요.")
    p = r.randint(1, 4)
    return fill(f"y = {b}^(x − {p})의 역함수는 y = {lg(b, 'x')} + {{{{1}}}}", [str(p)],
                f"x와 y를 바꾸면 x = {b}^(y − {p})\ny − {p} = {lg(b, 'x')} → y = {lg(b, 'x')} + {p}", "x, y를 바꾸고 y에 대해 푸세요.")

def c3_cmp(r):
    t = r.choice(["exp", "log"])
    if t == "exp":
        b = r.choice(["2", "3", "(1/2)", "(1/3)"]); p, q = r.sample([0.2, 0.3, 0.5, 0.7, 1.5, -0.5], 2)
        inc = "/" not in b
        sg = (">" if p > q else "<") if inc else ("<" if p > q else ">")
        return fill(f"{b}^{p:g} {{{{1}}}} {b}^{q:g}  (부등호 >, < 중 하나)", [[sg]],
                    f"밑 {b.strip('()')} {'> 1 → 지수가 클수록 큼' if inc else '< 1 → 지수가 클수록 작음'}\n{p:g} {'>' if p > q else '<'} {q:g}이므로 {sg}", "밑과 1의 대소를 먼저 보세요.")
    b = r.choice([2, 3]); x = r.randint(2, 30); k = r.randint(1, 3)
    if x == b ** k: return None
    sg = ">" if x > b ** k else "<"
    return fill(f"{lg(b, x)} {{{{1}}}} {k}  (부등호 >, < 중 하나)", [[sg]],
                f"{k} = {lg(b, b ** k)}\n{x} {sg} {b ** k}이고 밑 {b} > 1이므로 {sg}", "정수를 같은 밑의 로그로 바꾸세요.")

L33 = [("역함수", c3_inv), ("대소 비교", c3_cmp)]

def c4_quad(r):
    b = r.choice([2, 3]); p, q = r.sample([1, 2, 3, 4], 2)
    if r.random() < .5:
        return a4_quad(r)
    return num(f"({lg(b, 'x')})² − {p + q} {lg(b, 'x')} + {p * q} = 0의 두 해의 곱은?", b ** (p + q),
               f"{lg(b, 'x')} = t: (t − {p})(t − {q}) = 0 → x = {b}{sup(p)}, {b}{sup(q)}\n곱 {b ** (p + q)}", "치환하세요.")

def c4_expineq(r):
    b = r.choice([2, 3]); c = r.randint(1, 4)
    t = r.choice(["a", "b"])
    if t == "a":
        return num(f"{b}^(2x) < {b}^(x + {c})의 해가 x < a일 때 a의 값은?", c, f"밑 {b} > 1 → 2x < x + {c} → x < {c}", "지수끼리 비교")
    k = r.randint(1, 4)
    return num(f"(1/{b})^(x − {c}) ≥ (1/{b}){sup(k)}의 해가 x ≤ a일 때 a의 값은?", c + k, f"밑 1/{b} < 1 → 방향이 바뀜: x − {c} ≤ {k} → x ≤ {c + k}", "밑이 1보다 작으면 방향 반대")

L34 = [("치환하는 방정식", c4_quad), ("지수부등식", c4_expineq), ("로그부등식", b4_ineq), ("로그방정식", b4_eq)]

ALL = {"ch01": [L11, L12, L13, L14], "ch02": [L21, L22, L23, L24], "ch03": [L31, L32, L33, L34]}

if __name__ == "__main__":
    tot = 0
    for ch, Ls in ALL.items():
        for i, T in enumerate(Ls, 1):
            per = 6 if len(T) >= 7 else 8 if len(T) >= 5 else 10 if len(T) >= 4 else 14 if len(T) == 3 else 20
            n = write("c3", ch, f"l0{i}", T, per=per, seed=1 + i); tot += n; print(ch, i, len(T), n)
    print("total", tot)
