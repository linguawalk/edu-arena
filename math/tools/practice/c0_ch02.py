"""코스 0 · 챕터 2 문자와 식 — 연습 문제 은행"""
from core import *

def nz(r, a, b):
    while True:
        x = r.randint(a, b)
        if x: return x

# ---------------- l01 문자의 사용 ----------------
def l01_lin(r):
    a, b, k = nz(r, -6, 6), nz(r, -9, 9), nz(r, -5, 5)
    v = a * k + b
    return num(f"x = {m(k)}일 때, {poly((a, 'x'), (b, ''))}의 값은?", v,
               f"x 자리에 {j(k, '를을', par(k))} 넣습니다. 음수는 괄호로 감싸 대입합니다.\n"
               f"{poly((a, ''))} × {par(k)}{term(b)} = {m(a * k)}{term(b)} = {m(v)}" if a not in (1, -1) else
               f"x 자리에 {j(k, '를을', par(k))} 넣습니다. 음수는 괄호로 감싸 대입합니다.\n"
               f"{'−' if a < 0 else ''}{par(k)}{term(b)} = {m(a * k)}{term(b)} = {m(v)}",
               "음수를 대입할 때는 괄호를 씌우세요.")

def l01_quad(r):
    a, b, k = r.choice([1, 2, -1, 3]), nz(r, -5, 5), nz(r, -4, 4)
    v = a * k * k + b * k
    return num(f"a = {m(k)}일 때, {poly((a, 'a²'), (b, 'a'))}의 값은?", v,
               f"a 자리에 {j(k, '를을', par(k))} 넣습니다.\n{par(k)}² = {k * k}  (괄호째 제곱하므로 양수)\n"
               f"{m(a)} × {k * k} + {par(b)} × {par(k)} = {m(a * k * k)} + {par(b * k)} = {m(v)}",
               "a²에 음수를 넣을 때는 (−k)²처럼 괄호째 제곱하세요.")

def l01_two(r):
    p, q, a, b = nz(r, -5, 5), nz(r, -5, 5), nz(r, -6, 6), nz(r, -6, 6)
    v = p * a + q * b
    return num(f"a = {m(a)}, b = {m(b)}일 때, {poly((p, 'a'), (q, 'b'))}의 값은?", v,
               f"a와 b에 각각 대입합니다.\n{m(p)} × {par(a)} + {par(q)} × {par(b)}\n= {m(p * a)} + {par(q * b)} = {m(v)}",
               "두 문자에 각각 괄호를 씌워 대입하세요.")

def l01_coef(r):
    a, b, c = nz(r, -7, 7), nz(r, -9, 9), nz(r, -9, 9)
    order = r.choice([0, 1])
    e = poly((a, 'x²'), (b, 'x'), (c, '')) if order == 0 else poly((c, ''), (b, 'x'), (a, 'x²'))
    ask = r.choice(["x의 계수", "상수항", "x²의 계수"])
    v = {"x의 계수": b, "상수항": c, "x²의 계수": a}[ask]
    return num(f"다항식 {e}에서 {ask}는?", v,
               f"각 항을 부호와 함께 나누어 봅니다: {', '.join(t for t in [poly((a, 'x²')), poly((b, 'x')), poly((c, ''))])}\n"
               f"{ask}는 {m(v)}  (앞의 부호까지 포함)",
               "항은 부호까지 포함해서 나누세요.")

def l01_degree(r):
    terms = [(nz(r, -6, 6), v) for v in r.sample(["x³", "x²", "x", ""], r.randint(2, 4))]
    d = max({"x³": 3, "x²": 2, "x": 1, "": 0}[v] for _, v in terms)
    if d == 0: return None
    e = poly(*terms)
    return num(f"다항식 {e}의 차수는?", d,
               f"각 항의 차수: " + ", ".join(f"{poly((c, v))} → {({'x³': 3, 'x²': 2, 'x': 1, '': 0})[v]}" for c, v in terms) +
               f"\n다항식의 차수는 가장 높은 항의 차수이므로 {d}",
               "차수가 가장 높은 항을 찾으세요.")

def l01_omit(r):
    c = r.choice([2, 3, 5, -1, -2, -4, 7])
    a2 = r.choice([True, False])
    parts = ["a", "b"] + (["a"] if a2 else []) + [par(c)]
    r.shuffle(parts)
    res = (("−" if c < 0 else "") + (str(abs(c)) if abs(c) != 1 else "") + ("a²b" if a2 else "ab"))
    alt = res.replace("−", "-")
    return fill(f"{' × '.join(parts)}{'을' if bat(c) and parts[-1] == par(c) else '를'} 곱셈 기호 없이 나타내면 {{{{1}}}}", [[res, alt, alt.replace('²', '^2')]],
                "수를 문자 앞에 쓰고, 문자는 알파벳 순서로 씁니다.\n같은 문자의 곱은 거듭제곱으로 나타냅니다." +
                ("\n1은 생략하고 −1은 −만 씁니다." if abs(c) == 1 else "") + f"\n따라서 {res}",
                "수 → 문자(알파벳 순) 순서로, 같은 문자는 거듭제곱으로 쓰세요.")

def l01_price(r):
    p, q = r.choice([300, 500, 700, 800, 1200]), r.choice([400, 600, 900, 1500])
    x, y = r.randint(2, 9), r.randint(2, 9)
    v = p * x + q * y
    return num(f"한 개에 {p}원인 빵 x개와 {q}원인 우유 y개의 값은 ({p}x + {q}y)원입니다. x = {x}, y = {y}일 때 값은 몇 원일까요?", v,
               f"{p} × {x} + {q} × {y}\n= {p * x} + {q * y} = {v}\n따라서 {v}원",
               "x, y에 개수를 대입하세요.")

def l01_temp(r):
    c = r.choice([-20, -15, -10, -5, 5, 10, 15, 20, 30, 35, 40, 100])
    v = F(9, 5) * c + 32
    return num(f"섭씨온도 C를 화씨온도로 바꾸는 식은 1.8C + 32입니다. {m(c)}°C는 화씨 몇 도일까요?", v,
               f"C = {j(c, '를을', m(c))} 대입합니다.\n1.8 × {par(c)} + 32 = {m(fs(F(9, 5) * c))} + 32 = {m(fs(v))}\n따라서 화씨 {m(fs(v))}도",
               "1.8에 섭씨온도를 곱하고 32를 더하세요.")

L01 = [("일차식에 대입", l01_lin), ("이차식에 대입", l01_quad), ("두 문자에 대입", l01_two), ("계수와 상수항", l01_coef),
       ("다항식의 차수", l01_degree), ("곱셈 기호 생략", l01_omit), ("문자식 활용", l01_price), ("공식에 대입", l01_temp)]

# ---------------- l02 일차식의 계산 ----------------
def l02_like(r):
    a, b, c, d = nz(r, -7, 9), nz(r, -9, 9), nz(r, -7, 7), nz(r, -9, 9)
    if a + c == 0: return None
    return fill(f"{poly((a, 'x'), (b, ''), (c, 'x'), (d, ''))} = {{{{1}}}}x + {{{{2}}}}", [ans(a + c), ans(b + d)],
                f"동류항끼리 모읍니다.\nx항: {poly((a, 'x'))}{term(c, 'x')} = {poly((a + c, 'x'))}\n상수항: {m(b)}{term(d)} = {m(b + d)}\n"
                f"따라서 {poly((a + c, 'x'), (b + d, ''))}",
                "x항끼리, 상수항끼리 따로 계산하세요.")

def l02_dist(r):
    k, a, b = nz(r, -6, 6), nz(r, -5, 5), nz(r, -9, 9)
    if k == 1: return None
    return fill(f"{'−' if k == -1 else par(k)}({poly((a, 'x'), (b, ''))}) = {{{{1}}}}x + {{{{2}}}}", [ans(k * a), ans(k * b)],
                f"괄호 앞의 {j(k, '를을', m(k))} 괄호 안의 각 항에 모두 곱합니다.\n{m(k)} × {poly((a, 'x'))} = {poly((k * a, 'x'))}\n"
                f"{m(k)} × {par(b)} = {m(k * b)}\n따라서 {poly((k * a, 'x'), (k * b, ''))}",
                "분배법칙: 괄호 앞의 수를 두 항에 모두 곱하세요. 부호에 주의!")

def l02_two(r):
    p, a, q, b = r.randint(2, 5), nz(r, -6, 6), r.randint(2, 5), nz(r, -6, 6)
    cx, cc = p - q, p * a + q * b * -1
    if cx == 0: return None
    return fill(f"{p}(x{term(a)}) − {q}(x{term(b)}) = {{{{1}}}}x + {{{{2}}}}", [ans(cx), ans(cc)],
                f"괄호를 풉니다.\n{p}(x{term(a)}) = {poly((p, 'x'), (p * a, ''))}\n−{q}(x{term(b)}) = {poly((-q, 'x'), (-q * b, ''))}  (−{j(q, '를을')} 두 항 모두에 곱함)\n"
                f"동류항 정리: {poly((p, 'x'))} − {q}x = {poly((cx, 'x'))}, {m(p * a)}{term(-q * b)} = {m(cc)}\n따라서 {poly((cx, 'x'), (cc, ''))}",
                "빼는 괄호는 −를 괄호 안 두 항에 모두 곱해야 합니다.")

def l02_div(r):
    k, a, b = r.choice([2, 3, 4, 5]), nz(r, -6, 6), nz(r, -6, 6)
    return fill(f"({poly((k * a, 'x'), (k * b, ''))}) ÷ {k} = {{{{1}}}}x + {{{{2}}}}", [ans(a), ans(b)],
                f"각 항을 {ro(k)} 나눕니다.\n{poly((k * a, 'x'))} ÷ {k} = {poly((a, 'x'))}\n{m(k * b)} ÷ {k} = {m(b)}\n따라서 {poly((a, 'x'), (b, ''))}",
                "괄호 안의 두 항을 각각 나누세요.")

def l02_value(r):
    p, a, q, b, k = r.randint(2, 4), nz(r, -5, 5), r.choice([1, 2]), nz(r, -5, 5), nz(r, -4, 6)
    cx, cc = p - q, p * a - q * b
    if cx == 0: return None
    v = cx * k + cc
    qs = "" if q == 1 else str(q)
    return num(f"{p}(x{term(a)}) − {qs}(x{term(b)})을 간단히 한 다음 x = {j(k, '를을', m(k))} 대입한 값은?", v,
               f"먼저 괄호를 풀어 간단히 합니다: "
               f"{poly((p, 'x'), (p * a, ''), (-q, 'x'), (-q * b, ''))} = {poly((cx, 'x'), (cc, ''))}\n"
               f"x = {m(k)} 대입: {m(cx)} × {par(k)}{term(cc)} = {m(v)}",
               "먼저 식을 간단히 하면 대입이 쉬워집니다.")

def l02_kinds(r):
    pool = ["5a", "−2a", "a²", "3b", "ab", "7", "a", "−a²", "4a", "2b", "−6a", "a³"]
    pick = r.sample(pool, 6)
    like = [t for t in pick if t.rstrip("a").lstrip("−").isdigit() or t in ("a", "−a")]
    like = [t for t in pick if t.endswith("a") and not t.endswith("²a") and "b" not in t and "²" not in t and "³" not in t]
    return num(f"{', '.join(pick)} 중 3a와 동류항인 것은 몇 개일까요?", len(like),
               "동류항은 문자와 차수가 모두 같은 항입니다. 계수는 달라도 됩니다.\n"
               f"3a와 동류항: {', '.join(like) if like else '없음'}\n"
               "a², a³은 차수가 다르고 b, ab는 문자가 다릅니다." + f"\n따라서 {len(like)}개",
               "문자가 a 하나이고 차수가 1인 항을 찾으세요.")

def l02_frac(r):
    a, b = nz(r, -5, 5), nz(r, -5, 5)
    p, q = r.choice([(2, 3), (3, 4), (2, 5)])
    L = p * q
    cx, cc = q + p, q * a + p * b
    return fill(f"(x{term(a)})/{p} + (x{term(b)})/{q} = ({{{{1}}}}x + {{{{2}}}})/{L}", [ans(cx), ans(cc)],
                f"분모 {j(p, '와과')} {q}의 최소공배수 {ro(L)} 통분합니다.\n(x{term(a)})/{p} = {q}(x{term(a)})/{L} = ({poly((q, 'x'), (q * a, ''))})/{L}\n"
                f"(x{term(b)})/{q} = {p}(x{term(b)})/{L} = ({poly((p, 'x'), (p * b, ''))})/{L}\n분자끼리 더하면 ({poly((cx, 'x'), (cc, ''))})/{L}",
                f"분모를 {ro(L)} 통분하고 분자 전체에 곱하세요.")

def l02_rect(r):
    a, b, c = r.randint(2, 5), r.randint(1, 9), r.randint(2, 9)
    return fill(f"가로가 ({a}x + {b})cm, 세로가 {c}cm인 직사각형의 둘레는 ({{{{1}}}}x + {{{{2}}}})cm입니다.", [ans(2 * a), ans(2 * (b + c))],
                f"둘레 = 2 × (가로 + 세로)\n= 2 × ({a}x + {b} + {c}) = 2 × ({a}x + {b + c})\n= {2 * a}x + {2 * (b + c)}",
                "가로와 세로를 더한 다음 2배 하세요.")

L02 = [("동류항 정리", l02_like), ("분배법칙", l02_dist), ("괄호 두 개 풀기", l02_two), ("일차식의 나눗셈", l02_div),
       ("간단히 한 뒤 대입", l02_value), ("동류항 찾기", l02_kinds), ("분수 꼴 일차식", l02_frac), ("둘레를 식으로", l02_rect)]

# ---------------- l03 지수법칙과 다항식의 곱셈 ----------------
def l03_mul(r):
    v = r.choice("axy"); p, q = r.randint(2, 9), r.randint(2, 9)
    return fill(f"{v}{sup(p)} × {v}{sup(q)} = {v}^{{{{1}}}}", [str(p + q)],
                f"밑이 같은 거듭제곱의 곱은 지수를 더합니다.\n{v}{sup(p)} × {v}{sup(q)} = {v}^({p} + {q}) = {v}{sup(p + q)}",
                "곱할 때는 지수를 더합니다.")

def l03_pow(r):
    v = r.choice("axy"); p, q = r.randint(2, 6), r.randint(2, 5)
    return fill(f"({v}{sup(p)}){sup(q)} = {v}^{{{{1}}}}", [str(p * q)],
                f"거듭제곱의 거듭제곱은 지수를 곱합니다.\n({v}{sup(p)}){sup(q)} = {v}^({p} × {q}) = {v}{sup(p * q)}",
                "지수끼리 곱하세요.")

def l03_div(r):
    v = r.choice("axy"); p = r.randint(5, 12); q = r.randint(2, p - 1)
    return fill(f"{v}{sup(p)} ÷ {v}{sup(q)} = {v}^{{{{1}}}}", [str(p - q)],
                f"밑이 같은 거듭제곱의 나눗셈은 지수를 뺍니다.\n{v}{sup(p)} ÷ {v}{sup(q)} = {v}^({p} − {q}) = {v}{sup(p - q)}",
                "나눌 때는 지수를 뺍니다.")

def l03_coefpow(r):
    k, p, n = r.choice([2, 3, -2, -3, 5]), r.randint(2, 4), r.randint(2, 3)
    return fill(f"({'−' if k == -1 else m(k)}a{sup(p)}){sup(n)} = {{{{1}}}}a^{{{{2}}}}", [ans(k ** n), [str(p * n)]],
                f"괄호 안의 수와 문자를 각각 {n}제곱합니다.\n수: {par(k)}{sup(n)} = {m(k ** n)}\n문자: (a{sup(p)}){sup(n)} = a{sup(p * n)}\n따라서 {m(k ** n)}a{sup(p * n)}",
                "수는 수끼리, 문자는 문자끼리 거듭제곱하세요. 음수의 홀수 제곱은 음수입니다.")

def l03_mono(r):
    p, q, a, b = nz(r, -6, 6), nz(r, -6, 6), r.randint(1, 4), r.randint(1, 4)
    if abs(p) == 1 or abs(q) == 1: return None
    return fill(f"{m(p)}x{sup(a) if a > 1 else ''} × {'(' if q < 0 else ''}{m(q)}x{sup(b) if b > 1 else ''}{')' if q < 0 else ''} = {{{{1}}}}x^{{{{2}}}}", [ans(p * q), [str(a + b)]],
                f"계수끼리, 문자끼리 곱합니다.\n계수: {m(p)} × {par(q)} = {m(p * q)}\n문자: x{sup(a) if a > 1 else ''} × x{sup(b) if b > 1 else ''} = x{sup(a + b)}\n따라서 {m(p * q)}x{sup(a + b)}",
                "계수는 계수끼리 곱하고, 지수는 더하세요.")

def l03_monodiv(r):
    q, k = r.choice([2, 3, 4, 5, 6]), nz(r, -5, 5)
    a, b = r.randint(2, 5), r.randint(2, 4)
    p = q * k
    return fill(f"{m(p)}a{sup(a)}b{sup(b)} ÷ {q}ab = {{{{1}}}}a^{{{{2}}}}b^{{{{3}}}}", [ans(k), [str(a - 1)], [str(b - 1)]],
                f"계수끼리, 같은 문자끼리 나눕니다.\n계수: {m(p)} ÷ {q} = {m(k)}\na{sup(a)} ÷ a = a{sup(a - 1)}, b{sup(b)} ÷ b = b{sup(b - 1)}\n"
                f"따라서 {m(k)}a{sup(a - 1)}b{sup(b - 1)}" + ("  (지수 1은 생략해서 쓰지만 빈칸에는 1)" if 1 in (a - 1, b - 1) else ""),
                "나눗셈은 지수를 뺍니다.")

def l03_fx(r):
    a, b = nz(r, -7, 7), nz(r, -7, 7)
    return fill(f"(x{term(a)})(x{term(b)}) = x² + {{{{1}}}}x + {{{{2}}}}", [ans(a + b), ans(a * b)],
                f"전개하면 x²{term(a, 'x')}{term(b, 'x')} + {par(a)}×{par(b)}\nx의 계수: {m(a)} + {par(b)} = {m(a + b)}\n상수항: {par(a)} × {par(b)} = {m(a * b)}\n"
                f"따라서 {poly((1, 'x²'), (a + b, 'x'), (a * b, ''))}",
                "(x + a)(x + b) = x² + (a + b)x + ab")

def l03_gx(r):
    p, a, b = r.randint(2, 4), nz(r, -5, 5), nz(r, -5, 5)
    c2, c1, c0 = p, p * b + a, a * b
    return fill(f"({p}x{term(a)})(x{term(b)}) = {{{{1}}}}x² + {{{{2}}}}x + {{{{3}}}}", [ans(c2), ans(c1), ans(c0)],
                f"분배법칙으로 네 번 곱합니다.\n{p}x × x = {p}x², {p}x × {par(b)} = {poly((p * b, 'x'))}\n{par(a)} × x = {poly((a, 'x'))}, {par(a)} × {par(b)} = {m(a * b)}\n"
                f"동류항 정리: {poly((c2, 'x²'), (c1, 'x'), (c0, ''))}",
                "앞 괄호의 각 항을 뒤 괄호의 각 항에 곱하세요.")

def l03_val(r):
    p = r.randint(8, 15); q = r.randint(p - 6, p - 1)
    return num(f"2{sup(p)} ÷ 2{sup(q)}의 값은?", 2 ** (p - q),
               f"지수를 뺍니다: 2{sup(p)} ÷ 2{sup(q)} = 2{sup(p - q)}\n2{sup(p - q)} = {2 ** (p - q)}",
               "지수를 먼저 빼고 계산하세요.")

def l03_unit(r):
    b, n = r.choice([2, 3, 7, 8, 4, 9]), r.randint(10, 60)
    cyc = []
    x = b % 10
    while x not in cyc: cyc.append(x); x = x * b % 10
    v = cyc[(n - 1) % len(cyc)]
    return num(f"{b}{sup(n)}의 일의 자리 숫자는?", v,
               f"일의 자리만 보면 {b}¹, {b}², … 의 일의 자리는 {', '.join(map(str, cyc[:-1] + [j(cyc[-1], '가이')]))} 반복됩니다. (주기 {len(cyc)})\n"
               f"{n} ÷ {len(cyc)}의 나머지는 {n % len(cyc)}" + (f" → 주기의 마지막" if n % len(cyc) == 0 else f" → 주기의 {n % len(cyc)}번째") +
               f"\n따라서 일의 자리 숫자는 {v}",
               "거듭제곱의 일의 자리가 반복되는 규칙을 찾으세요.")

L03 = [("지수법칙: 곱", l03_mul), ("지수법칙: 거듭제곱", l03_pow), ("지수법칙: 나눗셈", l03_div), ("수와 문자의 거듭제곱", l03_coefpow),
       ("단항식의 곱셈", l03_mono), ("단항식의 나눗셈", l03_monodiv), ("(x + a)(x + b) 전개", l03_fx), ("(px + a)(x + b) 전개", l03_gx),
       ("거듭제곱 값", l03_val), ("일의 자리 숫자", l03_unit)]

# ---------------- l04 곱셈공식과 인수분해 기초 ----------------
def l04_sq(r):
    a = nz(r, -9, 9)
    return fill(f"(x{term(a)})² = x² + {{{{1}}}}x + {{{{2}}}}", [ans(2 * a), ans(a * a)],
                f"(x + a)² = x² + 2ax + a²에 a = {j(a, '를을', m(a))} 넣습니다.\n2a = {m(2 * a)}, a² = {a * a}\n따라서 {poly((1, 'x²'), (2 * a, 'x'), (a * a, ''))}",
                "가운데 항 2ab를 빠뜨리지 마세요.")

def l04_diff(r):
    a = r.randint(2, 12)
    return fill(f"(x + {a})(x − {a}) = x² − {{{{1}}}}", [str(a * a)],
                f"(a + b)(a − b) = a² − b²\n(x + {a})(x − {a}) = x² − {a}² = x² − {a * a}",
                "합과 차의 곱은 제곱의 차입니다.")

def l04_num(r):
    k = r.randint(1, 9); t = r.choice(["sq+", "sq-", "pm"])
    if t == "sq+":
        v = (100 + k) ** 2
        return num(f"{100 + k}²을 곱셈공식을 이용해 계산하세요.", v,
                   f"{100 + k}² = (100 + {k})² = 100² + 2×100×{k} + {k}²\n= 10000 + {200 * k} + {k * k} = {v}", "(100 + a)² 꼴로 바꾸세요.")
    if t == "sq-":
        v = (100 - k) ** 2
        return num(f"{100 - k}²을 곱셈공식을 이용해 계산하세요.", v,
                   f"{100 - k}² = (100 − {k})² = 100² − 2×100×{k} + {k}²\n= 10000 − {200 * k} + {k * k} = {v}", "(100 − a)² 꼴로 바꾸세요.")
    v = 10000 - k * k
    return num(f"{100 - k} × {j(100 + k, '를을')} 계산하세요.", v,
               f"(100 − {k})(100 + {k}) = 100² − {k}²\n= 10000 − {k * k} = {v}", "합과 차의 곱 공식을 이용하세요.")

def l04_common(r):
    g, a, b = r.choice([2, 3, 4, 5, 6]), r.randint(1, 5), r.randint(1, 7)
    if gcd(a, b) > 1: return None
    return fill(f"{g * a}x + {g * b} = {{{{1}}}}({'' if a == 1 else a}x + {{{{2}}}})", [str(g), str(b)],
                f"{j(g * a, '와과')} {g * b}의 최대공약수는 {g}입니다.\n{g * a}x + {g * b} = {g} × {'' if a == 1 else a}x + {g} × {b}\n= {g}({'' if a == 1 else a}x + {b})",
                "두 항에 공통으로 들어 있는 가장 큰 수를 묶어 내세요.")

def l04_dsq(r):
    a = r.randint(2, 12)
    return fill(f"x² − {a * a} = (x + {{{{1}}}})(x − {{{{2}}}})", [str(a), str(a)],
                f"{a * a} = {a}²이므로 x² − {a}²\n제곱의 차: a² − b² = (a + b)(a − b)\n따라서 (x + {a})(x − {a})",
                f"{a * a}이 어떤 수의 제곱인지 찾으세요.")

def l04_tri(r):
    a, b = r.randint(1, 8), r.randint(1, 8)
    if a == b: return None
    return fill(f"x² + {a + b}x + {a * b} = (x + {{{{1}}}})(x + {{{{2}}}})", [str(a), str(b)],
                f"곱해서 {a * b}, 더해서 {j(a + b, '가이')} 되는 두 수를 찾습니다.\n{a} × {b} = {a * b}, {a} + {b} = {a + b}\n따라서 (x + {a})(x + {b})",
                f"곱이 {a * b}이고 합이 {a + b}인 두 정수를 찾으세요.", unordered=[[1, 2]])

def l04_tri2(r):
    a, b = r.randint(1, 9), r.randint(1, 9)
    if a == b: return None
    s = a - b
    mid = ("+ " if s > 0 else "− ") + poly((abs(s), 'x'))
    return fill(f"x² {mid} − {a * b} = (x + {{{{1}}}})(x − {{{{2}}}})", [str(a), str(b)],
                f"곱해서 −{a * b}, 더해서 {j(s, '가이', m(s))} 되는 두 수를 찾습니다.\n{a} × (−{b}) = −{a * b}, {a} + (−{b}) = {m(s)}\n따라서 (x + {a})(x − {b})",
                f"곱이 −{a * b}이고 합이 {m(s)}인 두 정수를 찾으세요. 부호가 다른 두 수입니다.")

def l04_perf(r):
    a = r.randint(2, 12)
    return fill(f"x² + {2 * a}x + {a * a} = (x + {{{{1}}}})²", [str(a)],
                f"{a * a} = {a}²이고 {2 * a}x = 2 × x × {a}입니다.\n완전제곱식 a² + 2ab + b² = (a + b)²\n따라서 (x + {a})²",
                "상수항이 어떤 수의 제곱인지, 가운데 항이 그 수의 2배인지 확인하세요.")

def l04_k(r):
    k, a = r.choice([2, 3, 5]), r.randint(2, 6)
    return fill(f"{k}x² − {k * a * a} = {{{{1}}}}(x + {{{{2}}}})(x − {{{{3}}}})", [str(k), str(a), str(a)],
                f"먼저 공통인수 {ro(k)} 묶습니다: {k}(x² − {a * a})\n괄호 안을 제곱의 차로: x² − {a}² = (x + {a})(x − {a})\n따라서 {k}(x + {a})(x − {a})",
                "공통인수를 먼저 묶은 다음 제곱의 차를 이용하세요.")

L04 = [("(x + a)² 전개", l04_sq), ("합과 차의 곱", l04_diff), ("곱셈공식으로 수 계산", l04_num), ("공통인수 묶기", l04_common),
       ("제곱의 차 인수분해", l04_dsq), ("x² + (a+b)x + ab 인수분해", l04_tri), ("부호가 다른 인수분해", l04_tri2),
       ("완전제곱식", l04_perf), ("두 단계 인수분해", l04_k)]

if __name__ == "__main__":
    tot = 0
    for l, T in [("l01", L01), ("l02", L02), ("l03", L03), ("l04", L04)]:
        n = write("c0", "ch02", l, T, per=6); tot += n; print(l, n)
    print("total", tot)
