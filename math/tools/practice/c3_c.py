"""코스 3 · 챕터 6~7 (수열, 수학적 귀납법) — 연습 문제 은행"""
from core import *

def nz(r, a, b):
    while True:
        x = r.randint(a, b)
        if x: return x
SUBD = str.maketrans("0123456789+−n", "₀₁₂₃₄₅₆₇₈₉₊₋ₙ")
def a_(k): return "a" + str(k).translate(SUBD)
def seq(xs): return ", ".join(m(x) if not isinstance(x, F) else fm(x) for x in xs)

# ================= ch06 l01 등차수열 =================
def q1_term(r):
    a, d, n = r.randint(-10, 20), nz(r, -6, 7), r.randint(8, 30)
    return num(f"{seq([a + d * i for i in range(3)])}, …의 제{n}항은?", a + (n - 1) * d,
               f"첫째항 {m(a)}, 공차 {m(d)}\naₙ = a + (n − 1)d = {m(a)} + {n - 1} × {par(d)} = {m(a + (n - 1) * d)}", "aₙ = a + (n − 1)d")

def q1_two(r):
    a, d = r.randint(-8, 15), nz(r, -5, 6); p, q = sorted(r.sample(range(2, 12), 2))
    ask = r.choice(["d", "a"])
    return num(f"등차수열에서 {a_(p)} = {m(a + (p - 1) * d)}, {a_(q)} = {m(a + (q - 1) * d)}일 때 {'공차는' if ask == 'd' else '첫째항은'}?", d if ask == "d" else a,
               f"{a_(q)} − {a_(p)} = ({q} − {p})d → {m((q - p) * d)} = {q - p}d → d = {m(d)}\n" + (f"{a_(p)} = a + {p - 1 if p > 2 else ''}d → a = {m(a + (p - 1) * d)} − {mul(p - 1, d)} = {m(a)}" if ask == "a" else ""),
               "두 항의 차 = (번호 차) × 공차")

def q1_mid(r):
    a, d = r.randint(-10, 20), nz(r, -8, 8)
    return num(f"{m(a)}, x, {j(a + 2 * d, '가이', m(a + 2 * d))} 이 순서대로 등차수열을 이룰 때 x의 값은?", a + d,
               f"등차중항: 2x = {m(a)} + {par(a + 2 * d)} → x = {m(a + d)}", "가운데 항은 양 끝의 평균")

def q1_first_neg(r):
    a, d = r.randint(20, 80), -r.randint(2, 7)
    n = next(k for k in range(1, 200) if a + (k - 1) * d < 0)
    return num(f"첫째항이 {a}, 공차가 {d}인 등차수열에서 처음으로 음수가 되는 항은 제몇 항일까요?".replace(f"{d}인", f"{m(d)}인"), n,
               f"aₙ = {a} + (n − 1)({m(d)}) < 0 → n − 1 > {fs(F(a, -d))} → n > {fs(F(a, -d) + 1)}\n가장 작은 자연수 n = {n}", "aₙ < 0인 가장 작은 n")

def q1_sum(r):
    a, d, n = r.randint(-5, 10), nz(r, -3, 6), r.randint(8, 30)
    S = n * (2 * a + (n - 1) * d) // 2
    return num(f"첫째항이 {m(a)}, 공차가 {m(d)}인 등차수열의 첫째항부터 제{n}항까지의 합은?", S,
               f"Sₙ = n(2a + (n − 1)d)/2 = {n} × ({2 * a} + {n - 1}×{par(d)}) / 2 = {n} × {2 * a + (n - 1) * d} / 2 = {S}", "Sₙ = n{2a + (n − 1)d}/2")

def q1_Sn(r):
    p, q = nz(r, -3, 4), r.randint(-5, 6); k = r.randint(3, 12)
    v = p * (2 * k - 1) + q
    return num(f"Sₙ = {poly((p, 'n²'), (q, 'n'))}일 때 {a_(k)}의 값은?", v,
               f"{a_(k)} = S{str(k).translate(SUBD)} − S{str(k - 1).translate(SUBD)} = {par(p * k * k + q * k)} − {par(p * (k - 1) ** 2 + q * (k - 1))} = {m(v)}", "aₙ = Sₙ − Sₙ₋₁")

L61 = [("일반항", q1_term), ("두 항으로 결정", q1_two), ("등차중항", q1_mid), ("처음으로 음수", q1_first_neg), ("등차수열의 합", q1_sum), ("Sₙ에서 aₙ", q1_Sn)]

# ================= l02 등비수열 =================
def q2_term(r):
    a, rr, n = nz(r, -5, 6), r.choice([2, 3, -2, -3]), r.randint(4, 9)
    return num(f"{seq([a * rr ** i for i in range(3)])}, …의 제{n}항은?", a * rr ** (n - 1),
               f"첫째항 {m(a)}, 공비 {m(rr)}\naₙ = arⁿ⁻¹ = {m(a)} × {par(rr)}{sup(n - 1)} = {m(a * rr ** (n - 1))}", "aₙ = arⁿ⁻¹")

def q2_half(r):
    a, n = 2 ** r.randint(3, 7), r.randint(4, 8)
    v = F(a, 2 ** (n - 1))
    return num(f"{seq([F(a, 2 ** i) for i in range(3)])}, …의 제{n}항은? (기약분수 또는 정수로)", v,
               f"공비 1/2 → aₙ = {a} × (1/2){sup(n - 1)} = {fm(v)}", "공비가 분수인 등비수열", fmt="fraction" if v.denominator > 1 else "integer")

def q2_two(r):
    a, rr = nz(r, -4, 5), r.choice([2, 3, -2]); p = r.randint(1, 3); q = p + r.choice([2, 3])
    ask = r.choice(["r", "a"])
    if (q - p) % 2 == 0 and rr < 0: return None
    return num(f"등비수열에서 {a_(p)} = {m(a * rr ** (p - 1))}, {a_(q)} = {m(a * rr ** (q - 1))}일 때 {'공비는' if ask == 'r' else '첫째항은'}?", rr if ask == "r" else a,
               f"{a_(q)} ÷ {a_(p)} = r{sup(q - p)} = {m(rr ** (q - p))} → r = {m(rr)}" + (f"\n{a_(p)} = ar{sup(p - 1) if p > 1 else '⁰'} → a = {m(a)}" if ask == "a" else ""),
               "두 항의 비 = r^(번호 차)")

def q2_mid(r):
    a, b = r.choice([(4, 9), (2, 8), (3, 12), (1, 16), (4, 25), (9, 16), (2, 18), (5, 20)])
    return num(f"{a}, x, {j(b, '가이')} 이 순서대로 등비수열을 이루고 x > 0일 때 x의 값은?", isqrt(a * b),
               f"등비중항: x² = {a} × {b} = {a * b} → x = {isqrt(a * b)}", "x² = ab")

def q2_sum(r):
    a, rr, n = r.randint(1, 5), r.choice([2, 3]), r.randint(3, 8)
    S = a * (rr ** n - 1) // (rr - 1)
    return num(f"첫째항이 {a}, 공비가 {rr}인 등비수열의 첫째항부터 제{n}항까지의 합은?", S,
               f"Sₙ = a(rⁿ − 1)/(r − 1) = {a}({rr}{sup(n)} − 1)/{rr - 1} = {a}×{rr ** n - 1}/{rr - 1} = {S}", "Sₙ = a(rⁿ − 1)/(r − 1)")

def q2_Sn(r):
    b, k = r.choice([2, 3]), r.randint(2, 7)
    v = b ** k - b ** (k - 1)
    return num(f"Sₙ = {b}ⁿ − 1일 때 {a_(k)}의 값은?", v, f"{a_(k)} = S{str(k).translate(SUBD)} − S{str(k - 1).translate(SUBD)} = ({b}{sup(k)} − 1) − ({b}{sup(k - 1)} − 1) = {v}", "aₙ = Sₙ − Sₙ₋₁")

def q2_save(r):
    A, n = r.choice([100, 200, 50]), r.randint(2, 3)
    # 매년 초 A, 연 10% 복리, n년 말 → A×1.1×(1.1^n − 1)/0.1
    v = sum(A * F(11, 10) ** k for k in range(1, n + 1))
    return num(f"매년 초 {A}만 원씩 연 10% 복리로 {n}년 동안 적립하면 {n}년 말 원리합계는 몇 만 원일까요?", f"{float(v):g}",
               f"각 해 적립금이 1.1, 1.1², … 배가 됩니다.\n" + " + ".join(f"{A}×1.1{sup(k)}" for k in range(1, n + 1)) + f" = {float(v):g}", "등비수열의 합", fmt="decimal")

L62 = [("일반항", q2_term), ("공비가 분수", q2_half), ("두 항으로 결정", q2_two), ("등비중항", q2_mid), ("등비수열의 합", q2_sum), ("Sₙ에서 aₙ", q2_Sn), ("적립금", q2_save)]

# ================= l03 Σ =================
def sig(f, a, b, s): return f"Σ(k={a}~{b}) {s}"
def q3_basic(r):
    n = r.randint(4, 20); t = r.choice(["k", "ck", "c", "k2", "k3"])
    if t == "k": return num(f"{sig(None, 1, n, 'k')}의 값은?", n * (n + 1) // 2, f"Σk = n(n + 1)/2 = {n}×{n + 1}/2 = {n * (n + 1) // 2}", "Σk = n(n + 1)/2")
    if t == "ck":
        c = r.randint(2, 5); return num(f"{sig(None, 1, n, f'{c}k')}의 값은?", c * n * (n + 1) // 2, f"Σ{c}k = {c} × n(n + 1)/2 = {c} × {n * (n + 1) // 2} = {c * n * (n + 1) // 2}", "상수는 Σ 밖으로")
    if t == "c":
        c = r.randint(2, 9); return num(f"{sig(None, 1, n, str(c))}의 값은?", c * n, f"Σc = cn = {c} × {n} = {c * n}", "상수를 n번 더함")
    if t == "k2":
        n = r.randint(3, 12); v = n * (n + 1) * (2 * n + 1) // 6
        return num(f"{sig(None, 1, n, 'k²')}의 값은?", v, f"Σk² = n(n + 1)(2n + 1)/6 = {n}×{n + 1}×{2 * n + 1}/6 = {v}", "Σk² 공식")
    n = r.randint(3, 10); v = (n * (n + 1) // 2) ** 2
    return num(f"{sig(None, 1, n, 'k³')}의 값은?", v, f"Σk³ = {{n(n + 1)/2}}² = {n * (n + 1) // 2}² = {v}", "Σk³ = (Σk)²")

def q3_lin(r):
    n, p, q = r.randint(5, 20), nz(r, -3, 4), r.randint(-5, 5)
    v = p * n * (n + 1) // 2 + q * n
    return num(f"{sig(None, 1, n, f'({poly((p, 'k'), (q, ''))})')}의 값은?", v,
               f"{m(p)}Σk{term(q)}×{n} = {m(p)} × {n * (n + 1) // 2}{term(q * n)} = {m(v)}".replace(f"{term(q)}×{n}", f" + {par(q)}×{n}"), "나누어 계산하세요.")

def q3_quad(r):
    n, t = r.randint(3, 10), r.choice(["k(k+1)", "k²−1", "k²+k", "(2k−1)"])
    f = {"k(k+1)": lambda k: k * (k + 1), "k²−1": lambda k: k * k - 1, "k²+k": lambda k: k * k + k, "(2k−1)": lambda k: 2 * k - 1}[t]
    v = sum(f(k) for k in range(1, n + 1)); s2, s1 = n * (n + 1) * (2 * n + 1) // 6, n * (n + 1) // 2
    ex = {"k(k+1)": f"Σk² + Σk = {s2} + {s1}", "k²−1": f"Σk² − {n} = {s2} − {n}", "k²+k": f"Σk² + Σk = {s2} + {s1}", "(2k−1)": f"2Σk − {n} = {2 * s1} − {n}"}[t]
    disp = {"k(k+1)": "k(k + 1)", "k²−1": "(k² − 1)", "k²+k": "(k² + k)", "(2k−1)": "(2k − 1)"}[t]
    return num(f"{sig(None, 1, n, disp)}의 값은?", v, f"{ex} = {v}", "Σ의 성질로 나누세요.")

def q3_prop(r):
    A, B, p, q = r.randint(2, 20), r.randint(-5, 10), nz(r, -3, 4), nz(r, -3, 3)
    return num(f"Σ(k=1~n) aₖ = {A}, Σ(k=1~n) bₖ = {m(B)}일 때 Σ(k=1~n) ({poly((p, 'aₖ'), (q, 'bₖ'))})의 값은?", p * A + q * B,
               f"Σ(paₖ + qbₖ) = pΣaₖ + qΣbₖ\n= {m(p)}×{A} + {par(q)}×{par(B)} = {m(p * A + q * B)}", "Σ의 선형성")

def q3_range(r):
    a, b = r.randint(3, 10), r.randint(12, 25)
    v = b * (b + 1) // 2 - (a - 1) * a // 2
    return num(f"{sig(None, a, b, 'k')}의 값은?", v, f"Σ(k=1~{b}) k − Σ(k=1~{a - 1}) k = {b * (b + 1) // 2} − {(a - 1) * a // 2} = {v}", "1부터의 합에서 빼세요.")

L63 = [("기본 공식", q3_basic), ("일차식의 합", q3_lin), ("이차식의 합", q3_quad), ("Σ의 성질", q3_prop), ("중간부터의 합", q3_range)]

# ================= l04 여러 가지 수열의 합 =================
def q4_tele(r):
    t = r.choice(["k(k+1)", "odd", "root"])
    if t == "k(k+1)":
        n = r.randint(4, 30); v = F(n, n + 1)
        return num(f"Σ(k=1~{n}) 1/(k(k + 1))의 값은? (기약분수로)", v, f"1/(k(k + 1)) = 1/k − 1/(k + 1)\n연쇄적으로 지워져 1 − 1/{n + 1} = {fs(v)}", "부분분수", fmt="fraction")
    if t == "odd":
        n = r.randint(3, 15); v = F(n, 2 * n + 1)
        return num(f"Σ(k=1~{n}) 1/((2k − 1)(2k + 1))의 값은? (기약분수로)", v, f"= (1/2)Σ(1/(2k − 1) − 1/(2k + 1)) = (1/2)(1 − 1/{2 * n + 1}) = {fs(v)}", "부분분수에 1/2", fmt="fraction")
    s = r.randint(2, 10); n = s * s - 1
    return num(f"Σ(k=1~{n}) 1/(√(k + 1) + √k)의 값은?", s - 1, f"유리화: 1/(√(k + 1) + √k) = √(k + 1) − √k\n합 = √{n + 1} − √1 = {s} − 1 = {s - 1}", "분모를 유리화하면 연쇄적으로 지워집니다.")

def q4_diff(r):
    a, d0, dd = r.randint(1, 5), r.randint(1, 3), r.randint(1, 3); n = r.randint(6, 15)
    xs = [a]
    for i in range(n - 1): xs.append(xs[-1] + d0 + i * dd)
    return num(f"{seq(xs[:5])}, …의 제{n}항은?", xs[-1],
               f"계차수열: {seq([xs[i + 1] - xs[i] for i in range(4)])}, … (첫째항 {d0}, 공차 {dd})\naₙ = {a} + Σ(k=1~{n - 1}) ({poly((dd, 'k'), (d0 - dd, ''))}) = {xs[-1]}", "계차수열을 이용하세요.")

def q4_alt(r):
    n = 2 * r.randint(5, 50)
    t = r.choice(["lin", "sq"])
    if t == "lin":
        return num(f"1 − 2 + 3 − 4 + … + {n - 1} − {n}의 값은?", -n // 2, f"(1 − 2) + (3 − 4) + … : −1이 {n // 2}번\n= {m(-n // 2)}", "두 개씩 묶으세요.")
    n = 2 * r.randint(2, 8)
    v = sum((-1) ** (k + 1) * k * k for k in range(1, n + 1))
    return num(f"1² − 2² + 3² − 4² + … + {n - 1}² − {n}²의 값은?", v,
               f"(2k − 1)² − (2k)² = −(4k − 1)\nΣ(k=1~{n // 2}) −(4k − 1) = −(4 × {n // 2 * (n // 2 + 1) // 2} − {n // 2}) = {m(v)}", "두 개씩 묶어 제곱의 차")

def q4_group(r):
    n = r.randint(10, 60)
    g = 1
    while g * (g + 1) // 2 < n: g += 1
    pos = n - (g - 1) * g // 2
    return num(f"1, 1, 2, 1, 2, 3, 1, 2, 3, 4, …의 제{n}항은?", pos,
               f"군수열: 제k군은 1, 2, …, k (k개)\n제{g - 1}군까지 {(g - 1) * g // 2}개 → 제{n}항은 제{g}군의 {pos}번째 = {pos}", "몇 번째 군인지 먼저 찾으세요.")

def q4_geo(r):
    n, c = r.randint(3, 8), r.choice([0, 1])
    v = 2 ** (n + 1) - 2 + (n * (n + 1) // 2 if c else 0)
    return num(f"Σ(k=1~{n}) ({'2ᵏ + k' if c else '2ᵏ'})의 값은?", v,
               f"Σ2ᵏ = 2(2{sup(n)} − 1) = {2 ** (n + 1) - 2}" + (f", Σk = {n * (n + 1) // 2}\n합 {v}" if c else ""), "등비수열의 합 공식")

L64 = [("부분분수·유리화로 지우기", q4_tele), ("계차수열", q4_diff), ("부호가 바뀌는 합", q4_alt), ("군수열", q4_group), ("등비 + 등차", q4_geo)]

# ================= ch07 l01 수열의 귀납적 정의 =================
def rec_list(a1, f, n):
    xs = [a1]
    for k in range(1, n): xs.append(f(xs[-1], k))
    return xs

def r1_basic(r):
    t = r.choice(["add", "mul", "addn", "muln", "fib"])
    if t == "add":
        a, d, n = r.randint(-5, 9), nz(r, -4, 6), r.randint(5, 20)
        return num(f"a₁ = {m(a)}, aₙ₊₁ = aₙ{term(d)}일 때 {a_(n)}의 값은?", a + (n - 1) * d, f"공차 {m(d)}인 등차수열\n{a_(n)} = {m(a)} + {n - 1}×{par(d)} = {m(a + (n - 1) * d)}", "등차수열의 점화식")
    if t == "mul":
        a, rr, n = r.randint(1, 5), r.choice([2, 3, -2]), r.randint(3, 7)
        return num(f"a₁ = {a}, aₙ₊₁ = {m(rr)}aₙ일 때 {a_(n)}의 값은?", a * rr ** (n - 1), f"공비 {m(rr)}인 등비수열\n{a_(n)} = {a} × {par(rr)}{sup(n - 1)} = {m(a * rr ** (n - 1))}", "등비수열의 점화식")
    if t == "addn":
        a, c, n = r.randint(1, 5), r.choice([1, 2, 3]), r.randint(4, 12)
        xs = rec_list(a, lambda x, k: x + c * k, n)
        return num(f"a₁ = {a}, aₙ₊₁ = aₙ + {'' if c == 1 else c}n일 때 {a_(n)}의 값은?", xs[-1],
                   f"{a_(n)} = a₁ + Σ(k=1~{n - 1}) {'' if c == 1 else c}k = {a} + {c} × {(n - 1) * n // 2} = {xs[-1]}", "aₙ = a₁ + Σ(계차)")
    if t == "muln":
        n = r.randint(3, 6)
        xs = rec_list(1, lambda x, k: x * (k + 1), n)
        return num(f"a₁ = 1, aₙ₊₁ = (n + 1)aₙ일 때 {a_(n)}의 값은?", xs[-1], f"a₂ = 2, a₃ = 6, … → aₙ = n!\n{a_(n)} = {n}! = {xs[-1]}", "몇 항 써 보세요.")
    n = r.randint(6, 12); a, b = r.choice([(1, 1), (1, 2), (2, 1), (1, 3)])
    xs = [a, b]
    while len(xs) < n: xs.append(xs[-1] + xs[-2])
    return num(f"a₁ = {a}, a₂ = {b}, aₙ₊₂ = aₙ₊₁ + aₙ일 때 {a_(n)}의 값은?", xs[-1], f"차례로: {seq(xs)}\n{a_(n)} = {xs[-1]}", "앞의 두 항을 더해 나가세요.")

def r1_period(r):
    a = r.choice([2, 3, -1, F(1, 2)]); n = r.randint(5, 30)
    if a == 1: return None
    xs = [F(a)]
    for _ in range(n - 1): xs.append(1 / (1 - xs[-1]))
    return num(f"a₁ = {fm(a)}, aₙ₊₁ = 1/(1 − aₙ)일 때 {a_(n)}의 값은? (기약분수 또는 정수로)", xs[-1],
               f"a₁ = {fm(xs[0])}, a₂ = {fm(xs[1])}, a₃ = {fm(xs[2])}, a₄ = {fm(xs[3])} → 주기 3\n{n} ÷ 3의 나머지 {n % 3} → {a_(n)} = {fm(xs[-1])}", "몇 항 계산해 규칙을 찾으세요.",
               fmt="fraction" if xs[-1].denominator > 1 else "integer")

def r1_mean(r):
    a, d, n = r.randint(-3, 6), nz(r, -3, 5), r.randint(5, 12)
    return num(f"a₁ = {m(a)}, a₂ = {m(a + d)}이고 2aₙ₊₁ = aₙ + aₙ₊₂일 때 {a_(n)}의 값은?", a + (n - 1) * d,
               f"2aₙ₊₁ = aₙ + aₙ₊₂ → 등차수열, 공차 {m(d)}\n{a_(n)} = {m(a)} + {n - 1}×{par(d)} = {m(a + (n - 1) * d)}", "등차중항 꼴의 점화식")

L71 = [("점화식으로 항 구하기", r1_basic), ("주기가 있는 수열", r1_period), ("등차중항 점화식", r1_mean)]

def r2_lin(r):
    p, q, a = r.choice([2, 3]), r.randint(-3, 3), r.randint(1, 5); n = r.randint(4, 7)
    if q == 0: return None
    xs = rec_list(a, lambda x, k: p * x + q, n)
    al = F(q, 1 - p)
    return num(f"a₁ = {a}, aₙ₊₁ = {p}aₙ{term(q)}일 때 {a_(n)}의 값은?", xs[-1],
               f"aₙ₊₁ − ({fm(al)}) = {p}(aₙ − ({fm(al)}))로 변형 → 공비 {p}인 등비수열\n{a_(n)} = {fm(al)} + ({a} − ({fm(al)}))×{p}{sup(n - 1)} = {xs[-1]}\n(차례로: {seq(xs)})", "aₙ₊₁ − α = p(aₙ − α) 꼴")

def r2_diff(r):
    t = r.choice(["2n", "3^n"])
    if t == "2n":
        a, c, n = r.randint(1, 5), r.choice([2, 4]), r.randint(5, 12)
        xs = rec_list(a, lambda x, k: x + c * k, n)
        return num(f"a₁ = {a}, aₙ₊₁ − aₙ = {c}n일 때 {a_(n)}의 값은?", xs[-1], f"{a_(n)} = {a} + Σ(k=1~{n - 1}) {c}k = {a} + {c} × {(n - 1) * n // 2} = {xs[-1]}", "계차의 합")
    b, n = r.choice([2, 3]), r.randint(3, 6)
    xs = rec_list(1, lambda x, k: x + b ** k, n)
    return num(f"a₁ = 1, aₙ₊₁ − aₙ = {b}ⁿ일 때 {a_(n)}의 값은?", xs[-1], f"{a_(n)} = 1 + Σ(k=1~{n - 1}) {b}ᵏ = 1 + {sum(b ** k for k in range(1, n))} = {xs[-1]}", "계차가 등비수열")

def r2_ratio(r):
    t = r.choice(["n/(n+1)", "(n+2)/n"])
    n = r.randint(4, 15)
    if t == "n/(n+1)":
        return num(f"a₁ = 1, aₙ₊₁ = (n/(n + 1))aₙ일 때 {a_(n)}의 값은? (기약분수로)", F(1, n),
                   f"aₙ = a₁ × (1/2)(2/3)…((n − 1)/n) = 1/n (곱이 연쇄적으로 지워짐)\n{a_(n)} = 1/{n}", "곱하면 지워집니다.", fmt="fraction")
    n = r.randint(3, 10)
    v = n * (n + 1) // 2
    return num(f"a₁ = 1, aₙ₊₁ = ((n + 2)/n)aₙ일 때 {a_(n)}의 값은?", v,
               f"aₙ = 1 × (3/1)(4/2)(5/3)…((n + 1)/(n − 1)) = n(n + 1)/2\n{a_(n)} = {n}×{n + 1}/2 = {v}", "몇 개 곱해 지워지는 규칙을 보세요.")

def r2_Sn(r):
    t = r.choice(["2a-1", "quad"])
    if t == "2a-1":
        n = r.randint(3, 9)
        return num(f"Sₙ = 2aₙ − 1일 때 {a_(n)}의 값은?", 2 ** (n - 1),
                   f"n = 1: a₁ = 2a₁ − 1 → a₁ = 1\naₙ = Sₙ − Sₙ₋₁ = 2aₙ − 2aₙ₋₁ → aₙ = 2aₙ₋₁\n{a_(n)} = 2{sup(n - 1)} = {2 ** (n - 1)}", "Sₙ − Sₙ₋₁ = aₙ")
    p, q, n = nz(r, -2, 3), r.randint(-4, 4), r.randint(3, 15)
    v = p * (2 * n - 1) + q
    return num(f"Sₙ = {poly((p, 'n²'), (q, 'n'))}일 때 {a_(n)}의 값은?", v, f"{a_(n)} = Sₙ − Sₙ₋₁ = {p * n * n + q * n} − {par(p * (n - 1) ** 2 + q * (n - 1))} = {m(v)}", "aₙ = Sₙ − Sₙ₋₁")

def r2_hanoi(r):
    n = r.randint(3, 10)
    return num(f"하노이의 탑에서 원판 n개를 옮기는 최소 횟수 aₙ은 aₙ₊₁ = 2aₙ + 1, a₁ = 1을 만족합니다. 원판 {n}개일 때 최소 횟수는?", 2 ** n - 1,
               f"aₙ + 1 = 2(aₙ₋₁ + 1) → aₙ + 1 = 2ⁿ\n{a_(n)} = 2{sup(n)} − 1 = {2 ** n - 1}", "aₙ + 1을 한 덩어리로")

L72 = [("aₙ₊₁ = paₙ + q", r2_lin), ("계차 점화식", r2_diff), ("곱의 점화식", r2_ratio), ("합과 일반항", r2_Sn), ("하노이의 탑", r2_hanoi)]

def r3_step(r):
    t = r.choice(["sum", "odd", "sq", "geo", "tri", "cube", "gsum"])
    if t == "geo":
        return fill("(2ᵏ − 1) + 2ᵏ = 2^(k + {{1}}) − 1", [["1"]], "1 + 2 + 4 + … + 2ᵏ⁻¹ = 2ᵏ − 1의 귀납 단계\n2ᵏ + 2ᵏ = 2ᵏ⁺¹이므로 2ᵏ⁺¹ − 1", "같은 거듭제곱 두 개의 합")
    if t == "tri":
        return fill("k(k + 1)(k + 2)/3 + (k + 1)(k + 2) = (k + 1)(k + 2)(k + {{1}})/3", [["3"]],
                    "Σk(k + 1) = n(n + 1)(n + 2)/3의 귀납 단계\n(k + 1)(k + 2)로 묶으면 (k + 1)(k + 2)(k/3 + 1) = (k + 1)(k + 2)(k + 3)/3", "공통인수로 묶으세요.")
    if t == "cube":
        return fill("{k(k + 1)/2}² + (k + 1)³ = {(k + 1)(k + {{1}})/2}²", [["2"]],
                    "(k + 1)²{k²/4 + (k + 1)} = (k + 1)²(k² + 4k + 4)/4 = {(k + 1)(k + 2)/2}²", "(k + 1)²으로 묶으세요.")
    if t == "gsum":
        return fill("(3ᵏ − 1)/2 + 3ᵏ = (3^(k + {{1}}) − 1)/2", [["1"]], "1 + 3 + … + 3ᵏ⁻¹ = (3ᵏ − 1)/2의 귀납 단계\n(3ᵏ − 1 + 2·3ᵏ)/2 = (3·3ᵏ − 1)/2 = (3ᵏ⁺¹ − 1)/2", "통분해서 정리하세요.")
    if t == "sum":
        return fill("k(k + 1)/2 + (k + 1) = (k + 1)(k + {{1}})/2", [["2"]], "k(k + 1)/2 + 2(k + 1)/2 = (k + 1)(k + 2)/2\n공통인수 (k + 1)로 묶습니다.", "(k + 1)로 묶으세요.")
    if t == "odd":
        return fill("k² + (2k + 1) = (k + {{1}})²", [["1"]], "k² + 2k + 1 = (k + 1)²\n1 + 3 + … + (2n − 1) = n²의 귀납 단계", "완전제곱식")
    return fill("k(k + 1)(2k + 1)/6 + (k + 1)² = (k + 1)(k + 2)(2k + {{1}})/6", [["3"]],
                "(k + 1)[k(2k + 1) + 6(k + 1)]/6 = (k + 1)(2k² + 7k + 6)/6 = (k + 1)(k + 2)(2k + 3)/6", "(k + 1)로 묶고 인수분해")

def r3_div(r):
    b, d = r.choice([(4, 3), (5, 4), (7, 6), (3, 2), (9, 8), (6, 5), (11, 10)])
    return fill(f"{b}ᵏ⁺¹ − 1 = {b}({b}ᵏ − 1) + {{{{1}}}}", [str(b - 1)],
                f"{b}ᵏ⁺¹ − 1 = {b}·{b}ᵏ − {b} + {b} − 1 = {b}({b}ᵏ − 1) + {b - 1}\n{b}ᵏ − 1이 {d}의 배수이면 {b}ᵏ⁺¹ − 1도 {d}의 배수", "{b}을 묶어 내고 나머지를 정리하세요.".replace("{b}", str(b)))

def r3_ineq(r):
    t = r.choice([("2ⁿ > n²", lambda n: 2 ** n > n * n), ("3ⁿ > 2n + 1", lambda n: 3 ** n > 2 * n + 1), ("2ⁿ > 2n + 1", lambda n: 2 ** n > 2 * n + 1),
                  ("2ⁿ > n³", lambda n: 2 ** n > n ** 3), ("n! > 2ⁿ", lambda n: __import__('math').factorial(n) > 2 ** n), ("3ⁿ > n³", lambda n: 3 ** n > n ** 3)])
    nm, f = t
    a = next(k for k in range(60, 0, -1) if not f(k - 1)) if not all(f(k) for k in range(1, 60)) else 1
    return num(f"{nm}이 n ≥ a인 모든 자연수에서 성립할 때 a의 최솟값은?", a,
               f"작은 n부터 확인: " + ", ".join(f"n = {k}: {'참' if f(k) else '거짓'}" for k in range(max(1, a - 3), a + 2)) + f"\nn = {a}부터 성립 → a = {a}", "작은 수부터 직접 대입해 보세요.")

def r3_base(r):
    b, d = r.choice([(4, 3), (5, 4), (7, 3), (7, 6), (3, 2), (9, 4)])
    n = r.randint(1, 4)
    return num(f"{b}ⁿ − 1이 {d}의 배수임을 증명할 때, n = {n}이면 {b}ⁿ − 1의 값은?", b ** n - 1,
               f"{b}{sup(n)} − 1 = {b ** n - 1} = {d} × {(b ** n - 1) // d}  ({d}의 배수 확인)", "직접 계산하세요.")

L73 = [("귀납 단계의 식 변형", r3_step), ("배수 증명의 변형", r3_div), ("부등식이 성립하는 시작", r3_ineq), ("첫 단계 확인", r3_base)]

def r4_count(r):
    t = r.choice(["odd", "cube", "diag", "hand", "newhand", "addv"])
    if t == "odd":
        n = r.randint(5, 30); return num(f"처음 {n}개 홀수 1 + 3 + 5 + …의 합은?", n * n, f"1 + 3 + … + (2n − 1) = n²\n{n}² = {n * n}", "n개 홀수의 합 = n²")
    if t == "cube":
        n = r.randint(3, 10); return num(f"1³ + 2³ + … + {n}³의 값은?", (n * (n + 1) // 2) ** 2, f"= (1 + 2 + … + {n})² = {n * (n + 1) // 2}² = {(n * (n + 1) // 2) ** 2}", "세제곱의 합 = (합)²")
    if t == "diag":
        n = r.randint(5, 15); return num(f"{n}각형의 대각선은 몇 개일까요?", n * (n - 3) // 2, f"n(n − 3)/2 = {n}×{n - 3}/2 = {n * (n - 3) // 2}", "각 꼭짓점에서 n − 3개, 두 번 세므로 ÷2")
    if t == "hand":
        n = r.randint(4, 20); return num(f"{n}명이 서로 한 번씩 악수하면 모두 몇 번일까요?", n * (n - 1) // 2, f"n(n − 1)/2 = {n}×{n - 1}/2 = {n * (n - 1) // 2}", "두 명씩 짝짓기")
    if t == "newhand":
        n = r.randint(5, 20); return num(f"{n}명이 모두 서로 악수한 뒤 1명이 새로 와서 모두와 악수하면 악수는 몇 번 늘어날까요?", n, f"새로 온 사람이 기존 {n}명과 한 번씩 → {n}번", "aₙ₊₁ = aₙ + n")
    n = r.randint(5, 12)
    return num(f"{n}각형에 꼭짓점을 하나 더해 {n + 1}각형을 만들 때 늘어나는 대각선은 몇 개일까요?", n - 1,
               f"{(n + 1) * (n - 2) // 2} − {n * (n - 3) // 2} = {n - 1}\n(새 꼭짓점에서 {n + 1 - 3}개 + 원래 변 하나가 대각선이 됨)", "dₙ₊₁ − dₙ = n − 1")

def r4_step(r):
    t = r.choice(["geo", "frac", "five"])
    if t == "geo":
        return fill("2ᵏ⁺¹ − 1 + 2ᵏ⁺¹ = 2^(k + {{1}}) − 1", [["2"]], "2ᵏ⁺¹ + 2ᵏ⁺¹ = 2 × 2ᵏ⁺¹ = 2ᵏ⁺²\n따라서 2^(k + 2) − 1", "같은 거듭제곱 두 개의 합")
    if t == "frac":
        return fill("k/(k + 1) + 1/((k + 1)(k + 2)) = (k + 1)/(k + {{1}})", [["2"]], "통분: (k(k + 2) + 1)/((k + 1)(k + 2)) = (k + 1)²/((k + 1)(k + 2)) = (k + 1)/(k + 2)", "통분하세요.")
    b = r.choice([5, 6, 8, 9])
    return fill(f"{b}ᵏ⁺¹ − 1 = {b}({b}ᵏ − 1) + {{{{1}}}}", [str(b - 1)], f"{b}ᵏ⁺¹ − 1 = {b}({b}ᵏ − 1) + {b} − 1 = {b}({b}ᵏ − 1) + {b - 1}", "묶어 내고 남는 수")

L74 = [("규칙과 개수", r4_count), ("귀납 단계 계산", r4_step), ("부등식이 성립하는 시작", r3_ineq), ("합 공식의 귀납 단계", r3_step), ("배수 증명", r3_div)]

ALL = {"ch06": [L61, L62, L63, L64], "ch07": [L71, L72, L73, L74]}

if __name__ == "__main__":
    tot = 0
    for ch, Ls in ALL.items():
        for i, T in enumerate(Ls, 1):
            per = 6 if len(T) >= 7 else 8 if len(T) >= 5 else 10 if len(T) >= 4 else 14 if len(T) == 3 else 20
            n = write("c3", ch, f"l0{i}", T, per=per, seed=5 + i); tot += n; print(ch, i, len(T), n)
    print("total", tot)
