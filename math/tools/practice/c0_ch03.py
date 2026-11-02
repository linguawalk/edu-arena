"""코스 0 · 챕터 3 방정식과 연립방정식 — 연습 문제 은행"""
from core import *

def nz(r, a, b):
    while True:
        x = r.randint(a, b)
        if x: return x

def L(a, b, v="x"): return poly((a, v), (b, ""))

# ---------------- l01 등식과 방정식 ----------------
def l01_add(r):
    x, a = r.randint(1, 20), nz(r, -9, 12)
    b = x + a
    return num(f"방정식 x{term(a)} = {m(b)}의 해는?", x,
               f"x{term(a)} = {m(b)}에서 {m(a)}{'을' if bat(a) else '를'} 이항하면 부호가 바뀝니다.\nx = {m(b)}{term(-a)}\nx = {x}",
               "상수항을 반대쪽으로 옮기면 부호가 바뀝니다.")

def l01_mul(r):
    x, a, b = nz(r, -8, 10), r.randint(2, 9), r.randint(1, 15)
    c = a * x - b
    return num(f"방정식 {a}x − {b} = {m(c)}의 해는?", x,
               f"−{j(b, '를을')} 이항합니다: {a}x = {m(c)} + {b} = {m(a * x)}\n양변을 {ro(a)} 나누면 x = {m(x)}",
               "상수항을 먼저 이항한 뒤 x의 계수로 나누세요.")

def l01_frac(r):
    a, x0, b = r.randint(2, 6), r.randint(1, 8), nz(r, -6, 8)
    x = a * x0; c = x0 + b
    return num(f"방정식 x/{a}{term(b)} = {m(c)}의 해는?", x,
               f"{m(b)}{'을' if bat(b) else '를'} 이항: x/{a} = {m(c)}{term(-b)} = {m(x0)}\n양변에 {j(a, '를을')} 곱하면 x = {m(x)}",
               "상수항을 이항한 다음 분모를 양변에 곱하세요.")

def l01_both(r):
    x, a, c = nz(r, -6, 8), r.randint(2, 6), r.randint(1, 4)
    p = r.randint(-5, 15); d = p - (a * x) - c * x
    # p − a x = c x + d
    return num(f"방정식 {p} − {a}x = {L(c, d)}의 해는?" if p else f"방정식 −{a}x = {L(c, d)}의 해는?", x,
               f"x항은 왼쪽, 상수항은 오른쪽으로 이항합니다.\n−{a}x{term(-c, 'x')} = {m(d)}{term(-p)}\n{m(-(a + c))}x = {m(d - p)}\n양변을 {m(-(a + c))}로 나누면 x = {m(x)}",
               "x가 있는 항은 한쪽으로, 수는 다른 쪽으로 모으세요.")

def l01_ident(r):
    q, b = r.randint(2, 6), nz(r, -5, 5)
    p = q * b
    return num(f"등식 ax{term(p)} = {q}(x{term(b)})가 x에 대한 항등식일 때, a의 값은?" if r.random() < .5 else
               f"등식 {q}x{term(p)} = a(x{term(b)})가 x에 대한 항등식일 때, a의 값은?", q,
               f"오른쪽을 전개하면 {q}x{term(q * b)}\n항등식은 양변의 x의 계수와 상수항이 각각 같아야 합니다.\nx의 계수를 비교하면 a = {q}" +
               f"\n(확인: 상수항 {m(p)} = {m(q * b)})",
               "괄호를 풀고 양변의 계수를 비교하세요.")

def l01_trans(r):
    a, b, c = r.randint(2, 9), r.randint(1, 12), r.randint(1, 20)
    return fill(f"{a}x − {b} = {c}에서 −{j(b, '를을')} 이항하면 {a}x = {c} + {{{{1}}}}", [str(b)],
                f"이항하면 부호가 바뀝니다: −{b} → +{b}\n{a}x = {c} + {b}",
                "이항은 등식의 성질(양변에 같은 수 더하기)과 같습니다.")

def l01_word(r):
    x, a = r.randint(2, 15), r.randint(2, 9)
    t = r.choice(["box", "coin"])
    if t == "box":
        return num(f"무게가 x kg인 상자에 {a}kg짜리 추를 더 얹었더니 모두 {x + a}kg이 되었습니다. 상자는 몇 kg일까요?", x,
                   f"식을 세우면 x + {a} = {x + a}\n{j(a, '를을')} 이항하면 x = {x + a} − {a} = {x}\n따라서 {x}kg", "상자 무게 + 추 무게 = 전체 무게")
    k = r.choice([3, 4, 5])
    return num(f"같은 공책 {k}권과 1,000원짜리 펜 한 자루를 사고 {k * x * 100 + 1000:,}원을 냈습니다. 공책 한 권은 몇 원일까요?", x * 100,
               f"공책 한 권을 x원이라 하면 {k}x + 1000 = {k * x * 100 + 1000}\n{k}x = {k * x * 100}\nx = {x * 100}\n따라서 {x * 100}원", "공책 값 × 권수 + 펜 값 = 낸 돈")

L01 = [("x + a = b", l01_add), ("ax − b = c", l01_mul), ("분수 꼴 방정식", l01_frac), ("양변에 x가 있는 방정식", l01_both),
       ("항등식의 계수", l01_ident), ("이항", l01_trans), ("식 세우기", l01_word)]

# ---------------- l02 일차방정식 ----------------
def l02_lin(r):
    x, a, c = nz(r, -7, 9), r.randint(2, 9), r.randint(1, 8)
    if a == c: return None
    b = nz(r, -10, 10); d = a * x + b - c * x
    return num(f"방정식 {L(a, b)} = {L(c, d)}의 해는?", x,
               f"x항은 왼쪽으로, 상수항은 오른쪽으로 이항합니다.\n{a}x{term(-c, 'x')} = {m(d)}{term(-b)}\n{poly((a - c, 'x'))} = {m(d - b)}\nx = {m(x)}",
               "이항할 때 부호가 바뀝니다.")

def l02_paren(r):
    x, p, a = nz(r, -6, 9), r.randint(2, 5), nz(r, -5, 5)
    b = p * (x + a) - x
    return num(f"방정식 {p}(x{term(a)}) = x{term(b)}의 해는?", x,
               f"괄호를 풉니다: {L(p, p * a)} = x{term(b)}\n이항: {p}x − x = {m(b)}{term(-p * a)}\n{poly((p - 1, 'x'))} = {m(b - p * a)}\nx = {m(x)}",
               "먼저 분배법칙으로 괄호를 푸세요.")

def l02_dec(r):
    x = nz(r, -6, 9); a, c = r.randint(1, 9), r.randint(1, 9)
    if a == c: return None
    b = r.randint(-9, 9); d = a * x + b - c * x
    def dd(n): return m(f"{n / 10:g}")
    lhs = f"0.{a}x" + (f" + {dd(b)}" if b > 0 else f" − {dd(-b)}" if b < 0 else "")
    rhs = f"0.{c}x" + (f" + {dd(d)}" if d > 0 else f" − {dd(-d)}" if d < 0 else "")
    return num(f"방정식 {lhs} = {rhs}의 해는?", x,
               f"양변에 10을 곱해 계수를 정수로 만듭니다. (모든 항에 곱함)\n{L(a, b)} = {L(c, d)}\n{poly((a - c, 'x'))} = {m(d - b)}\nx = {m(x)}",
               "모든 항에 10을 곱하세요.")

def l02_frac(r):
    p, q = r.choice([(2, 3), (3, 4), (2, 5), (4, 3), (3, 2)])
    x = p * q * r.randint(-2, 3)
    if x == 0: return None
    c = x // p - x // q
    LL = p * q // gcd(p, q)
    return num(f"방정식 x/{p} − x/{q} = {m(c)}의 해는?", x,
               f"분모 {j(p, '와과')} {q}의 최소공배수 {j(LL, '를을')} 양변에 곱합니다.\n{LL // p}x − {LL // q}x = {m(c * LL)}\n{poly((LL // p - LL // q, 'x'))} = {m(c * LL)}\nx = {m(x)}",
               "분모의 최소공배수를 양변의 모든 항에 곱하세요.")

def l02_frac2(r):
    p, q = r.choice([(2, 3), (4, 6), (3, 5), (4, 3)])
    a, b, s = nz(r, -4, 4), nz(r, -4, 4), r.randint(1, 2)
    # (x + a)/p = (s x + b)/q → q(x+a) = p(sx+b) → (q − ps)x = pb − qa
    k = q - p * s
    if k == 0 or (p * b - q * a) % k: return None
    x = (p * b - q * a) // k
    LL = p * q // gcd(p, q)
    return num(f"방정식 (x{term(a)})/{p} = ({poly((s, 'x'), (b, ''))})/{q}의 해는?", x,
               f"양변에 {j(LL, '를을')} 곱합니다.\n{LL // p}(x{term(a)}) = {LL // q}({poly((s, 'x'), (b, ''))})\n"
               f"{L(LL // p, LL // p * a)} = {L(LL // q * s, LL // q * b)}\n{poly((LL // p - LL // q * s, 'x'))} = {m(LL // q * b - LL // p * a)}\nx = {m(x)}",
               "분모를 없앤 뒤 괄호를 푸세요.")

def l02_param(r):
    x0, c = r.randint(1, 4), r.randint(2, 5); b = r.randint(1, 9)
    # a x0 + b = c x0 − a → a(x0+1) = c x0 − b
    a = F(c * x0 - b, x0 + 1)
    return num(f"x = {x0}가 방정식 ax + {b} = {c}x − a의 해일 때, a의 값은? (기약분수 또는 정수로)".replace(f"x = {x0}가", j(x0, "가이", f"x = {x0}")), a,
               f"x = {x0}를 대입합니다: {x0}a + {b} = {c * x0} − a\n{x0}a + a = {c * x0} − {b}\n{x0 + 1}a = {c * x0 - b}\na = {fm(a)}".replace(f"x = {x0}를", j(x0, "를을", f"x = {x0}")),
               "해를 대입하면 a에 대한 방정식이 됩니다.", fmt="fraction" if a.denominator > 1 else "integer")

def l02_inf(r):
    c, p = r.randint(2, 6), r.randint(1, 9)
    b = nz(r, -9, 9)
    # ax − p = c x + b 해가 무수히 → a = c, b = −p
    return num(f"x에 대한 방정식 ax − {p} = {c}x + b의 해가 무수히 많을 때, a + b의 값은?", c - p,
               f"해가 무수히 많으려면 양변이 완전히 같은 식이어야 합니다.\nx의 계수: a = {c}\n상수항: −{p} = b\na + b = {c} + (−{p}) = {m(c - p)}",
               "양변의 x의 계수와 상수항이 각각 같아야 합니다.")

L02 = [("ax + b = cx + d", l02_lin), ("괄호가 있는 방정식", l02_paren), ("계수가 소수인 방정식", l02_dec),
       ("계수가 분수인 방정식", l02_frac), ("분수 꼴 양변", l02_frac2), ("해가 주어진 방정식", l02_param), ("해가 무수히 많은 조건", l02_inf)]

# ---------------- l03 연립일차방정식 ----------------
def sol(r, lo=-5, hi=8):
    return nz(r, lo, hi), nz(r, lo, hi)

def l03_add(r):
    x, y = r.randint(1, 12), r.randint(1, 12)
    if x <= y: return None
    s, d = x + y, x - y
    return fill(f"연립방정식 x + y = {s}, x − y = {d}의 해는 x = {{{{1}}}}, y = {{{{2}}}}", [str(x), str(y)],
                f"두 식을 변끼리 더하면 y가 없어집니다: 2x = {s + d} → x = {x}\nx = {x}를 x + y = {s}에 대입: y = {s} − {x} = {y}".replace(f"x = {x}를", j(x, "를을", f"x = {x}")),
                "두 식을 더하면 y가 사라집니다.")

def l03_elim(r):
    x, y = sol(r)
    a, b, d, e = r.randint(1, 4), r.randint(1, 4), r.randint(1, 4), nz(r, -4, 4)
    if a * e - b * d == 0: return None
    c, f = a * x + b * y, d * x + e * y
    return fill(f"연립방정식 {poly((a, 'x'), (b, 'y'))} = {m(c)}, {poly((d, 'x'), (e, 'y'))} = {m(f)}의 해는 x = {{{{1}}}}, y = {{{{2}}}}", [ans(x), ans(y)],
                f"x의 계수를 맞추기 위해 첫째 식에 {d}, 둘째 식에 {j(a, '를을')} 곱합니다.\n{poly((a * d, 'x'), (b * d, 'y'))} = {m(c * d)}\n{poly((a * d, 'x'), (e * a, 'y'))} = {m(f * a)}\n"
                f"빼면 {poly((b * d - e * a, 'y'))} = {m(c * d - f * a)} → y = {m(y)}\n대입하면 {poly((a, 'x'))}{term(b * y)} = {m(c)} → x = {m(x)}",
                "한 미지수의 계수를 같게 맞춘 다음 더하거나 빼세요.")

def l03_sub(r):
    x, y = sol(r)
    p = nz(r, -3, 3); q = y - p * x
    a = r.randint(1, 4); s = a * x + y
    return fill(f"연립방정식 y = {poly((p, 'x'), (q, ''))}, {poly((a, 'x'), (1, 'y'))} = {m(s)}의 해는 x = {{{{1}}}}, y = {{{{2}}}}", [ans(x), ans(y)],
                f"첫째 식을 둘째 식의 y에 대입합니다.\n{poly((a, 'x'))} + ({poly((p, 'x'), (q, ''))}) = {m(s)}\n{poly((a + p, 'x'))}{term(q)} = {m(s)} → x = {m(x)}\n"
                f"y = {m(p)} × {par(x)}{term(q)} = {m(y)}",
                "y = … 꼴의 식을 다른 식에 대입하세요.")

def l03_count(r):
    a, b = r.choice([(1, 1), (1, 2), (2, 1), (1, 3), (2, 3), (3, 2)])
    n = r.randint(8, 20)
    pairs = [(x, y) for x in range(1, n) for y in range(1, n) if a * x + b * y == n]
    if not pairs: return None
    return num(f"{poly((a, 'x'), (b, 'y'))} = {j(n, '를을')} 만족하는 자연수 순서쌍 (x, y)는 몇 개일까요?", len(pairs),
               f"x에 1, 2, 3, …을 차례로 넣어 y가 자연수인 경우를 찾습니다.\n" + ", ".join(f"({x}, {y})" for x, y in pairs) + f"\n따라서 {len(pairs)}개",
               "x = 1부터 차례로 넣어 보세요. y도 자연수여야 합니다.")

def l03_plug(r):
    x, y = r.randint(1, 6), r.randint(1, 6); a, b = r.randint(1, 5), nz(r, -4, 5)
    return num(f"(x, y) = ({x}, {y})가 방정식 {poly((a, 'x'), (b, 'y'))} = k의 해일 때, k의 값은?", a * x + b * y,
               f"x = {x}, y = {y}를 대입합니다.\nk = {a} × {x} + {par(b)} × {y} = {m(a * x + b * y)}",
               "해를 식에 대입하면 등식이 성립합니다.")

def l03_param(r):
    x, y = r.randint(1, 5), nz(r, -4, 4); a = r.randint(1, 5)
    d = x - y; c = a * x + y
    return num(f"연립방정식 ax + y = {m(c)}, x − y = {m(d)}의 해에서 x = {x}일 때, a의 값은?", a,
               f"x = {x}를 x − y = {m(d)}에 대입: y = {x} − {par(d)} = {m(y)}\n" f"ax + y = {m(c)}에 x = {x}, y = {m(y)} 대입: {x}a{term(y)} = {m(c)}\n{x}a = {m(c - y)} → a = {a}".replace(f"x = {x}를", j(x, "를을", f"x = {x}")),
               "먼저 a가 없는 식에서 y를 구하세요.")

def l03_none(r):
    p, q, k = r.randint(1, 3), r.randint(1, 4), r.randint(2, 3)
    c = r.randint(1, 9); e = c * k + r.randint(1, 3)
    return num(f"연립방정식 {poly((p, 'x'), (q, 'y'))} = {c}, {poly((p * k, 'x'))} + ay = {e}의 해가 없을 때, a의 값은?", q * k,
               f"해가 없으려면 두 식의 x, y의 계수 비는 같고 상수항의 비는 달라야 합니다.\nx의 계수가 {p} → {ro(p * k)} {k}배이므로 y의 계수도 {k}배: a = {q} × {k} = {q * k}\n"
               f"상수항은 {c} × {k} = {c * k} ≠ {e}이므로 해가 없습니다.",
               "첫째 식을 몇 배 하면 둘째 식의 x의 계수가 되는지 보세요.")

def l03_word(r):
    x, y = r.randint(5, 15) * 100, r.randint(5, 20) * 100
    a, b, c, d = r.randint(1, 4), r.randint(1, 4), r.randint(1, 4), r.randint(1, 4)
    if a * d == b * c or x == y: return None
    s1, s2 = a * x + b * y, c * x + d * y
    return num(f"사과 {a}개와 배 {b}개는 {s1:,}원, 사과 {c}개와 배 {d}개는 {s2:,}원입니다. 사과 한 개는 몇 원일까요?", x,
               f"사과 x원, 배 y원이라 하면\n{poly((a, 'x'), (b, 'y'))} = {s1}, {poly((c, 'x'), (d, 'y'))} = {s2}\n"
               f"y의 계수를 맞춰 빼면: {poly((a * d - b * c, 'x'))} = {s1 * d - s2 * b} → x = {x}\n(배는 y = {y}원)\n따라서 사과는 {x}원",
               "두 미지수로 식 두 개를 세우세요.")

L03 = [("가감법(기본)", l03_add), ("가감법(계수 맞추기)", l03_elim), ("대입법", l03_sub), ("자연수 해의 개수", l03_count),
       ("해를 대입", l03_plug), ("미지수 a 구하기", l03_param), ("해가 없는 조건", l03_none), ("연립방정식 활용", l03_word)]

# ---------------- l04 방정식의 활용 ----------------
def l04_num(r):
    x, a, k = r.randint(3, 20), r.randint(1, 9), r.randint(2, 5)
    if r.random() < .5:
        return num(f"어떤 수에서 {j(a, '를을')} 뺀 뒤 {k}배 했더니 {k * (x - a)}{'이' if bat(k * (x - a)) else '가'} 되었습니다. 어떤 수는?", x,
                   f"어떤 수를 x라 하면 {k}(x − {a}) = {k * (x - a)}\nx − {a} = {x - a}\nx = {x}", "어떤 수를 x로 놓고 문장 그대로 식을 세우세요.")
    return num(f"어떤 수의 {k}배에 {j(a, '를을')} 더했더니 {k * x + a}{'이' if bat(k * x + a) else '가'} 되었습니다. 어떤 수는?", x,
               f"어떤 수를 x라 하면 {k}x + {a} = {k * x + a}\n{k}x = {k * x}\nx = {x}", "어떤 수를 x로 놓으세요.")

def l04_consec(r):
    n, k = r.randint(5, 40), r.choice([2, 3, 4])
    s = k * n + k * (k - 1) // 2
    what = r.choice(["자연수", "짝수"]) if k <= 3 else "자연수"
    if what == "짝수":
        n2 = 2 * n; s = k * n2 + k * (k - 1)
        return num(f"연속하는 {k}개의 짝수의 합이 {s}일 때, 가장 작은 수는?", n2,
                   f"가장 작은 수를 x라 하면 " + ", ".join(["x"] + [f"x + {2 * i}" for i in range(1, k)]) + f"\n합: {k}x + {k * (k - 1)} = {s}\n{k}x = {s - k * (k - 1)} → x = {n2}",
                   "연속하는 짝수는 2씩 커집니다.")
    return num(f"연속하는 {k}개의 자연수의 합이 {s}일 때, 가장 작은 수는?", n,
               f"가장 작은 수를 x라 하면 " + ", ".join(["x"] + [f"x + {i}" for i in range(1, k)]) + f"\n합: {k}x + {k * (k - 1) // 2} = {s}\n{k}x = {s - k * (k - 1) // 2} → x = {n}",
               "가장 작은 수를 x로 놓으세요.")

def l04_age(r):
    s, k = r.randint(6, 15), r.choice([2, 3])
    t = r.randint(2, 15); f = k * (s + t) - t
    if f - s < 20 or f > 60: return None
    return num(f"어머니는 {f}세, 딸은 {s}세입니다. 몇 년 후에 어머니의 나이가 딸 나이의 {k}배가 될까요?", t,
               f"x년 후라 하면 {f} + x = {k}({s} + x)\n{f} + x = {k * s} + {k}x\n{f - k * s} = {k - 1}x → x = {t}\n확인: {t}년 후 {f + t}세와 {s + t}세",
               "x년 후에는 두 사람 모두 x살씩 많아집니다.")

def l04_buy(r):
    p, q = r.choice([(1000, 500), (1200, 700), (800, 300), (1500, 1000)])
    n = r.randint(6, 15); x = r.randint(1, n - 1)
    tot = p * x + q * (n - x)
    return num(f"한 자루에 {p:,}원인 볼펜과 {q:,}원인 연필을 합해 {n}자루 사고 {tot:,}원을 냈습니다. 볼펜은 몇 자루일까요?", x,
               f"볼펜을 x자루라 하면 연필은 ({n} − x)자루\n{p}x + {q}({n} − x) = {tot}\n{p - q}x + {q * n} = {tot}\n{p - q}x = {tot - q * n} → x = {x}",
               "볼펜 수를 x로 놓으면 연필 수는 (전체 − x)입니다.")

def l04_round(r):
    a, b = r.choice([(4, 6), (3, 6), (2, 3), (4, 12), (3, 5), (6, 10)])
    d = a * b * r.randint(1, 2) // gcd(a, b)
    if d > 30: return None
    T = F(d, a) + F(d, b)
    h, mm = int(T), int((T - int(T)) * 60)
    if (T * 60).denominator != 1: return None
    ts = f"{h}시간" + (f" {mm}분" if mm else "")
    return num(f"집에서 공원까지 갈 때는 시속 {a}km, 올 때는 같은 길을 시속 {b}km로 걸어 모두 {ts}이 걸렸습니다. 집에서 공원까지는 몇 km일까요?", d,
               f"거리를 x km라 하면 (시간) = (거리) ÷ (속력)\nx/{a} + x/{b} = {fs(T)}\n양변에 {j(a * b // gcd(a, b), '를을')} 곱하면 {poly((a * b // gcd(a, b) // a, 'x'), (a * b // gcd(a, b) // b, 'x'))} = {fs(T * (a * b // gcd(a, b)))}\nx = {d}",
               "갈 때 시간 + 올 때 시간 = 전체 시간")

def l04_chase(r):
    v1, v2 = r.choice([(60, 80), (50, 75), (40, 60), (60, 90), (70, 105)])
    t0 = r.randint(5, 20)
    if (v1 * t0) % (v2 - v1): return None
    x = v1 * t0 // (v2 - v1)
    return num(f"동생이 분속 {v1}m로 집을 나선 지 {t0}분 후에 형이 분속 {v2}m로 같은 길을 따라갔습니다. 형이 출발한 지 몇 분 후에 동생을 만날까요?", x,
               f"형이 출발한 지 x분 후에 만난다면, 동생은 ({t0} + x)분 걸은 것입니다.\n두 사람이 간 거리가 같으므로 {v1}({t0} + x) = {v2}x\n{v1 * t0} = {v2 - v1}x → x = {x}",
               "만날 때 두 사람이 이동한 거리가 같습니다.")

def l04_water(r):
    a, w = r.choice([10, 12, 15, 20]), r.choice([200, 300, 400, 500])
    b = r.choice([4, 5, 6, 8])
    if b >= a: return None
    salt = F(a * w, 100); tot = salt * 100 / b
    if tot.denominator != 1: return None
    x = tot - w
    return num(f"{a}% 소금물 {w}g에 물을 몇 g 더 넣으면 {b}% 소금물이 될까요?", x,
               f"소금의 양은 변하지 않습니다: {w} × {a}/100 = {fs(salt)}g\n물 x g을 넣으면 ({w} + x) × {b}/100 = {fs(salt)}\n{w} + x = {fs(tot)} → x = {fs(x)}",
               "물을 넣어도 소금의 양은 그대로입니다.")

def l04_mix(r):
    a, b = r.choice([(5, 10), (4, 12), (6, 15), (3, 8), (5, 20)])
    tot = r.choice([300, 400, 500, 600])
    x = r.randint(1, tot // 100 - 1) * 100
    c = F(a * x + b * (tot - x), tot)
    if c.denominator != 1: return None
    return num(f"{a}% 소금물과 {b}% 소금물을 섞어 {c}% 소금물 {tot}g을 만들었습니다. {a}% 소금물은 몇 g 섞었을까요?", x,
               f"{a}% 소금물을 x g이라 하면 {b}% 소금물은 ({tot} − x)g\n소금의 양: {a}x/100 + {b}({tot} − x)/100 = {tot} × {c}/100\n"
               f"양변에 100을 곱하면 {a}x + {b * tot} − {b}x = {c * tot}\n{b - a}x = {b * tot - c * tot} → x = {x}",
               "섞기 전 소금의 양의 합 = 섞은 뒤 소금의 양")

L04 = [("어떤 수 구하기", l04_num), ("연속하는 수", l04_consec), ("나이 문제", l04_age), ("개수와 금액", l04_buy),
       ("왕복 거리", l04_round), ("따라잡기", l04_chase), ("소금물 희석", l04_water), ("소금물 섞기", l04_mix)]

if __name__ == "__main__":
    tot = 0
    for l, T in [("l01", L01), ("l02", L02), ("l03", L03), ("l04", L04)]:
        n = write("c0", "ch03", l, T, per=6); tot += n; print(l, n)
    print("total", tot)
