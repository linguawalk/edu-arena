"""코스 0 · 챕터 1 수 체계 — 연습 문제 은행"""
from core import *

# ---------------- l01 소인수분해 ----------------
def l01_divcount(r):
    n = r.choice([12, 18, 20, 24, 28, 30, 32, 36, 40, 42, 45, 48, 50, 54, 56, 60, 63, 72, 75, 80, 84, 90, 96, 100])
    ds = divisors(n)
    pairs = [(d, n // d) for d in ds if d * d <= n]
    return num(f"{n}의 약수는 모두 몇 개일까요?", len(ds),
               f"곱해서 {j(n,'가이')} 되는 두 수를 짝지어 찾습니다: " + ", ".join(f"{a}×{b}" for a, b in pairs) +
               f"\n약수를 작은 순으로 쓰면 {', '.join(map(str, ds))}\n따라서 {len(ds)}개입니다.",
               "곱해서 그 수가 되는 두 수를 짝지어 빠짐없이 찾아보세요.")

def l01_primecount(r):
    a = r.choice([1, 10, 20, 30, 40]); b = a + r.choice([9, 19, 29]) if a == 1 else a + r.choice([10, 20])
    ps = [p for p in range(a, b + 1) if is_prime(p)]
    return num(f"{a}부터 {b}까지의 자연수 중 소수는 몇 개일까요?", len(ps),
               f"{a}부터 {b}까지에서 약수가 1과 자기 자신뿐인 수를 찾습니다.\n" +
               ("1은 소수가 아닙니다.\n" if a == 1 else "") +
               f"소수: {', '.join(map(str, ps))}\n따라서 {len(ps)}개입니다.",
               "2, 3, 5, 7로 나누어떨어지는 수를 지우면 남는 수가 소수입니다.")

def l01_fill_exp(r):
    a, b = r.randint(1, 5), r.randint(1, 3)
    n = 2 ** a * 3 ** b
    steps = []; x = n
    while x % 2 == 0: steps.append(f"{x} ÷ 2 = {x // 2}"); x //= 2
    while x % 3 == 0 and x > 1: steps.append(f"{x} ÷ 3 = {x // 3}"); x //= 3
    return fill(f"{j(n,'를을')} 소인수분해하면 {n} = 2^{{{{1}}}} × 3^{{{{2}}}} 입니다.", [str(a), str(b)],
                "작은 소수부터 차례로 나눕니다.\n" + "\n".join(steps) +
                f"\n2로 {a}번, 3으로 {b}번 나누었으므로 {n} = {fstr({2: a, 3: b})}",
                f"{j(n,'를을')} 2로 나누어떨어지지 않을 때까지 나눈 다음 3으로 나눠 보세요.")

def l01_value(r):
    f = {2: r.randint(1, 4), 3: r.randint(0, 2), 5: r.randint(0, 2), 7: r.choice([0, 0, 1])}
    f = {p: e for p, e in f.items() if e}
    if len(f) < 2: return None
    n = 1
    for p, e in f.items(): n *= p ** e
    if n > 1000: return None
    parts = [f"{p}{sup(e) if e > 1 else ''} = {p ** e}" for p, e in sorted(f.items()) if e > 1]
    return num(f"소인수분해한 결과가 {fstr(f)}인 수는 얼마일까요?", n,
               ("거듭제곱부터 계산합니다: " + ", ".join(parts) + "\n" if parts else "") +
               " × ".join(str(p ** e) for p, e in sorted(f.items())) + f" = {n}",
               "거듭제곱을 먼저 계산한 다음 모두 곱하세요.")

def l01_divcount_f(r):
    ps = r.sample([2, 3, 5, 7, 11], r.choice([2, 3]))
    f = {p: r.randint(1, 4) for p in ps}
    n = 1
    for p, e in f.items(): n *= (e + 1)
    es = [f[p] for p in sorted(f)]
    return num(f"{fstr(f)}의 약수는 모두 몇 개일까요?", n,
               f"지수는 차례로 {', '.join(map(str, es))}입니다.\n각각 1을 더하면 {', '.join(str(e + 1) for e in es)}\n"
               f"{' × '.join(str(e + 1) for e in es)} = {n}개",
               "각 소인수의 지수에 1을 더해서 모두 곱하세요.")

def two(r, lo=12, hi=150):
    while True:
        a, b = r.randint(lo, hi), r.randint(lo, hi)
        if a < b and gcd(a, b) > 2 and gcd(a, b) < a: return a, b

def l01_gcd(r):
    a, b = two(r); g = gcd(a, b)
    fa, fb, fg = factor(a), factor(b), factor(g)
    return num(f"{j(a,'와과')} {b}의 최대공약수는 얼마일까요?", g,
               f"소인수분해합니다: {a} = {fstr(fa)}, {b} = {fstr(fb)}\n"
               f"공통인 소인수를 지수가 작은 쪽으로 고르면 {fstr(fg)}\n따라서 최대공약수는 {g}",
               "두 수를 소인수분해하고 공통인 소인수를 찾아보세요.")

def l01_lcm(r):
    a, b = two(r, 6, 60); l = a * b // gcd(a, b)
    if l > 360: return None
    fa, fb, fl = factor(a), factor(b), factor(l)
    return num(f"{j(a,'와과')} {b}의 최소공배수는 얼마일까요?", l,
               f"소인수분해합니다: {a} = {fstr(fa)}, {b} = {fstr(fb)}\n"
               f"나오는 모든 소인수를 지수가 큰 쪽으로 고르면 {fstr(fl)}\n따라서 최소공배수는 {l}",
               "두 수를 소인수분해하고 모든 소인수를 지수가 큰 쪽으로 곱하세요.")

def l01_square(r):
    a, b = two(r, 24, 120); g = gcd(a, b)
    return num(f"가로 {a}cm, 세로 {b}cm인 종이를 남김없이 똑같은 정사각형으로 자르려 합니다. 가장 큰 정사각형의 한 변은 몇 cm일까요?", g,
               f"정사각형의 한 변은 {j(a,'와과')} {j(b,'를을')} 모두 나누어떨어지게 해야 합니다. → 공약수\n"
               f"가장 큰 정사각형이므로 최대공약수를 구합니다.\n{a} = {fstr(factor(a))}, {b} = {fstr(factor(b))} → 최대공약수 {g}\n"
               f"따라서 한 변은 {g}cm (정사각형 {a // g * (b // g)}장)",
               "한 변의 길이는 가로와 세로를 모두 나누어떨어지게 해야 합니다.")

def l01_bus(r):
    a, b = two(r, 6, 30)
    l = a * b // gcd(a, b)
    if l > 120: return None
    h = r.choice([6, 7, 8]); mm = l
    t = f"오전 {h + mm // 60}시" + (f" {mm % 60}분" if mm % 60 else "")
    return num(f"버스 A는 {a}분마다, 버스 B는 {b}분마다 출발합니다. 오전 {h}시에 두 버스가 동시에 출발했다면, 다음에 동시에 출발하는 것은 몇 분 뒤일까요?", l,
               f"A는 {a}의 배수가 되는 시각에, B는 {b}의 배수가 되는 시각에 출발합니다.\n"
               f"동시에 출발하려면 {j(a,'와과')} {b}의 공배수여야 하고, 가장 처음은 최소공배수입니다.\n"
               f"{a} = {fstr(factor(a))}, {b} = {fstr(factor(b))} → 최소공배수 {l}\n따라서 {l}분 뒤({t})",
               "두 버스가 함께 출발하는 시간 간격은 두 배차 간격의 공배수입니다.")

def l01_makesq(r):
    f = {p: r.randint(1, 3) for p in r.sample([2, 3, 5, 7], r.choice([2, 3]))}
    n = 1
    for p, e in f.items(): n *= p ** e
    k = 1
    for p, e in f.items():
        if e % 2: k *= p
    if k == 1 or n > 1500: return None
    odd = [p for p, e in sorted(f.items()) if e % 2]
    return num(f"{n}에 가장 작은 자연수 x를 곱하여 어떤 자연수의 제곱이 되게 하려 합니다. x는 얼마일까요?", k,
               f"{n} = {fstr(f)}\n제곱수는 소인수분해했을 때 모든 지수가 짝수입니다.\n"
               f"지수가 홀수인 소인수는 {', '.join(map(str, odd))}이므로 이것을 한 번씩 더 곱합니다.\n"
               f"x = {' × '.join(map(str, odd))} = {k}",
               "먼저 소인수분해하고, 지수가 홀수인 소인수를 찾아보세요.")

L01 = [("약수의 개수 세기", l01_divcount), ("소수 찾기", l01_primecount), ("소인수분해", l01_fill_exp),
       ("소인수분해된 수 계산", l01_value), ("약수의 개수 공식", l01_divcount_f), ("최대공약수", l01_gcd),
       ("최소공배수", l01_lcm), ("최대공약수 활용", l01_square), ("최소공배수 활용", l01_bus), ("제곱수 만들기", l01_makesq)]

# ---------------- l02 정수와 유리수의 계산 ----------------
def nz(r, a, b):
    while True:
        x = r.randint(a, b)
        if x: return x

def l02_addsub(r):
    a, b = nz(r, -15, 15), nz(r, -15, 15); op = r.choice(["+", "−"])
    v = a + b if op == "+" else a - b
    sb = f"({'+' if b > 0 else '−'}{abs(b)})"
    if op == "+":
        e = f"{par(a)} + {sb}" + ("\n부호가 같으므로 절댓값을 더하고 공통 부호를 붙입니다." if (a > 0) == (b > 0)
                                   else "\n부호가 다르므로 절댓값의 차를 구하고 절댓값이 큰 쪽의 부호를 붙입니다.")
    else:
        e = f"빼기는 빼는 수의 부호를 바꾸어 더하기로 고칩니다.\n{par(a)} − {sb} = {par(a)} + ({'−' if b > 0 else '+'}{abs(b)})"
    return num(f"{par(a)} {op} {sb} 를 계산하세요.", v, e + f"\n= {m(v)}",
               "빼기는 부호를 바꾼 수를 더하는 것과 같습니다.")

def l02_mul3(r):
    a, b, c = nz(r, -6, 6), nz(r, -6, 6), nz(r, -6, 6)
    if min(a, b, c) > 0: return None
    v = a * b * c; neg = sum(x < 0 for x in (a, b, c))
    return num(f"{par(a)} × {par(b)} × {par(c)} 를 계산하세요.", v,
               f"음수가 {neg}개이므로 부호는 {'−' if neg % 2 else '+'}입니다. (음수가 홀수 개면 −, 짝수 개면 +)\n"
               f"절댓값끼리 곱하면 {abs(a)} × {abs(b)} × {abs(c)} = {abs(v)}\n따라서 {m(v)}",
               "부호를 먼저 정하고, 절댓값끼리 곱하세요.")

def l02_temp(r):
    lo, hi = r.randint(-15, -1), r.randint(-3, 18)
    if hi <= lo: return None
    city = r.choice(["산골 마을", "어느 도시", "고원 지대", "북쪽 지방"])
    return num(f"{city}의 새벽 기온이 {m(lo)}°C, 낮 기온이 {m(hi)}°C였습니다. 일교차는 몇 °C일까요?", hi - lo,
               f"일교차 = 최고 기온 − 최저 기온\n{par(hi)} − {par(lo)} = {par(hi)} + {abs(lo)} = {hi - lo}\n따라서 {hi - lo}°C",
               "높은 기온에서 낮은 기온을 빼세요.")

def rfrac(r, den=(2, 3, 4, 5, 6, 8, 9, 10, 12)):
    d = r.choice(den); n = nz(r, -d * 2 + 1, d * 2 - 1)
    f = F(n, d)
    return f if f.denominator > 1 else None

def fpar(f): return f"({fm(f)})" if f < 0 else fm(f)

def l02_fadd(r):
    a, b = rfrac(r), rfrac(r)
    if a is None or b is None or a.denominator == b.denominator: return None
    op = r.choice(["+", "−"]); v = a + b if op == "+" else a - b
    L = a.denominator * b.denominator // gcd(a.denominator, b.denominator)
    an, bn = a * L, b * L
    expr = f"{fm(a)} {op} {fpar(b)}"
    vv = an + bn if op == "+" else an - bn
    return num(f"{expr} 를 계산하세요. (기약분수로)", v,
               f"분모 {j(a.denominator,'와과')} {b.denominator}의 최소공배수 {ro(L)} 통분합니다.\n"
               f"{fm(a)} = {m(an)}/{L}, {fm(b)} = {m(bn)}/{L}\n"
               f"분자끼리 계산: {par(an)} {op} {par(bn)} = {m(vv)} → {m(vv)}/{L}" +
               (f"\n약분하면 {fm(v)}" if F(vv, L).denominator != L else ""),
               f"분모를 {L}로 통분하세요.", fmt="fraction" if v.denominator > 1 else "integer")

def l02_fdiv(r):
    a, b = rfrac(r), rfrac(r)
    if a is None or b is None: return None
    op = r.choice(["×", "÷"]); v = a * b if op == "×" else a / b
    if op == "÷":
        rb = 1 / b
        e = f"나누기는 역수를 곱하는 것으로 바꿉니다: ÷ {fpar(b)} → × {fpar(rb)}\n{fm(a)} × {fpar(rb)}"
    else:
        e = f"분자는 분자끼리, 분모는 분모끼리 곱합니다.\n{fm(a)} × {fpar(b)}"; rb = b
    neg = (a < 0) != (rb < 0)
    e += f"\n부호: {'음수가 한 개이므로 −' if neg else '+'}\n약분해서 계산하면 {fm(v)}"
    return num(f"{fpar(a)} {op} {fpar(b)} 를 계산하세요. (기약분수로)", v, e,
               "나누기는 역수의 곱셈으로 바꾸고, 부호를 먼저 정하세요.", fmt="fraction" if v.denominator > 1 else "integer")

def l02_order(r):
    a, b, c = r.randint(2, 4), r.randint(2, 6), r.choice([2, 4])
    e3 = r.choice([2, 3])
    if (b ** e3) % c: return None
    p1 = -a * a; p2 = (-b) ** e3; v = p1 + p2 // c
    return num(f"−{a}² + (−{b}){sup(e3)} ÷ {c} 를 계산하세요.", v,
               f"거듭제곱부터 계산합니다.\n−{a}² = −({a} × {a}) = {m(p1)}  (괄호가 없으므로 {a}만 제곱)\n"
               f"(−{b}){sup(e3)} = {m(p2)}\n다음으로 나눗셈: {par(p2)} ÷ {c} = {m(p2 // c)}\n"
               f"마지막으로 덧셈: {par(p1)} + {par(p2 // c)} = {m(v)}",
               "거듭제곱 → 곱셈·나눗셈 → 덧셈·뺄셈 순서로 계산하세요. −a²과 (−a)²은 다릅니다.")

def l02_abs(r):
    a, b = nz(r, -20, 20), nz(r, -20, 20)
    op = r.choice(["+", "−"]); v = abs(a) + abs(b) if op == "+" else abs(a) - abs(b)
    return fill(f"|{m(a)}| {op} |{m(b)}| = {{{{1}}}}", [alts(str(v))],
                f"절댓값은 수직선에서 0까지의 거리이므로 항상 0 이상입니다.\n|{m(a)}| = {abs(a)}, |{m(b)}| = {abs(b)}\n{abs(a)} {op} {abs(b)} = {m(v)}",
                "먼저 각각의 절댓값을 구하세요.")

def l02_pow(r):
    n = r.randint(3, 120); k = r.choice([1, 2])
    v = (-1) ** n * k
    pre = "" if k == 1 else "2 × "
    return fill(f"{pre}(−1){sup(n)} = {{{{1}}}}", [alts(str(v)) + (["+1"] if v == 1 else [])],
                f"−1을 짝수 번 곱하면 1, 홀수 번 곱하면 −1입니다.\n{j(n,'는은')} {'짝수' if n % 2 == 0 else '홀수'}이므로 (−1){sup(n)} = {m((-1) ** n)}"
                + (f"\n2 × {par((-1) ** n)} = {m(v)}" if k == 2 else ""),
                "(−1)² = 1, (−1)³ = −1 … 규칙을 찾아보세요.")

def l02_word(r):
    s = r.randint(5, 20); ups = [nz(r, -8, 8) for _ in range(4)]
    v = s + sum(ups)
    days = ["월", "화", "수", "목"]
    desc = ", ".join(f"{d}요일 {'+' if u > 0 else '−'}{abs(u)}" for d, u in zip(days, ups))
    return num(f"어떤 주식이 처음에 {s}만 원이었습니다. 하루 변화가 {desc}(만 원)였다면 목요일 끝의 가격은 몇 만 원일까요?", v,
               f"변화를 모두 더합니다: {' + '.join(par(u) for u in ups)} = {m(sum(ups))}\n"
               f"처음 가격에 더하면 {s} + {par(sum(ups))} = {v}\n따라서 {v}만 원",
               "오른 것은 +, 내린 것은 −로 놓고 모두 더하세요.")

L02 = [("정수의 덧셈과 뺄셈", l02_addsub), ("정수의 곱셈", l02_mul3), ("기온 차", l02_temp),
       ("분수의 덧셈과 뺄셈", l02_fadd), ("분수의 곱셈과 나눗셈", l02_fdiv), ("계산 순서", l02_order),
       ("절댓값", l02_abs), ("−1의 거듭제곱", l02_pow), ("변화량 더하기", l02_word)]

# ---------------- l03 제곱근 ----------------
def l03_side(r):
    k = r.randint(4, 25); what = r.choice(["텃밭", "타일", "광장", "액자", "운동장"])
    unit = "m" if what in ("텃밭", "광장", "운동장") else "cm"
    return num(f"넓이가 {k * k}{unit}²인 정사각형 {what}의 한 변은 몇 {unit}일까요?", k,
               f"한 변을 x라 하면 x² = {k * k}\n{k} × {k} = {k * k}이고 길이는 양수이므로 x = √{k * k} = {k}\n따라서 {k}{unit}",
               "같은 수를 두 번 곱해 넓이가 되는 수를 찾으세요.")

def l03_roots(r):
    k = r.randint(2, 15)
    return fill(f"{k * k}의 제곱근은 {{{{1}}}}와 {{{{2}}}}입니다.", [[str(k), "+" + str(k)], alts(str(-k))],
                f"{k}² = {k * k}이고 (−{k})² = {k * k}입니다.\n양수의 제곱근은 양수와 음수 두 개입니다.\n따라서 {j(k,'와과')} −{k}",
                "제곱해서 그 수가 되는 수는 양수 하나, 음수 하나입니다.", unordered=[[1, 2]])

def l03_negroot(r):
    n = r.choice([2, 3, 5, 6, 7, 10, 11, 13])
    return fill(f"{n}의 음의 제곱근은 {{{{1}}}}", [["-√" + str(n), "−√" + str(n), "-√(" + str(n) + ")"]],
                f"{j(n,'는은')} 제곱수가 아니므로 근호 √를 써서 나타냅니다.\n{n}의 제곱근은 √{n}과 −√{n}\n그중 음수인 것은 −√{n}",
                "양의 제곱근에 −를 붙입니다.")

def l03_sqsum(r):
    a, b = r.randint(2, 12), r.randint(2, 12); op = r.choice(["+", "−"])
    v = a + b if op == "+" else a - b
    return num(f"√({a}²) {op} √((−{b})²) 의 값은?", v,
               f"√(x²)은 x의 절댓값입니다.\n√({a}²) = {a}\n√((−{b})²) = √{b * b} = {b}  (−{j(b,'가이')} 아님)\n{a} {op} {b} = {m(v)}",
               "√((−b)²)은 먼저 (−b)²을 계산한 뒤 양의 제곱근을 구하세요.")

def l03_sqof(r):
    a = r.choice([2, 3, 5, 6, 7, 10, 11, 13, 15]); s = r.choice([1, -1]); c = r.choice([1, 2, 3])
    v = a * c * c
    base = f"{'−' if s < 0 else ''}{c if c > 1 else ''}√{a}"
    return num(f"({base})² 의 값은?", v,
               f"제곱하면 부호는 사라집니다(음수×음수=양수).\n" +
               (f"({c}√{a})² = {c}² × (√{a})² = {c * c} × {a} = {v}" if c > 1 else f"(√{a})² = {a}"),
               "(√a)² = a 를 이용하세요.")

def l03_cmp(r):
    k = r.randint(2, 9); n = r.randint(k * k - 6, k * k + 6)
    if n == k * k or n < 2: return None
    sgn = ">" if n > k * k else "<"
    if r.random() < .5:
        return fill(f"√{n} {{{{1}}}} {k}  (부등호 >, < 중 하나)", [[sgn]],
                    f"{j(k,'를을')} 근호가 있는 꼴로 바꾸면 {k} = √{k * k}\n{n} {sgn} {k * k}이므로 √{n} {sgn} √{k * k}\n따라서 √{n} {sgn} {k}",
                    f"{k} = √{k * k}로 바꿔서 비교하세요.")
    s2 = "<" if sgn == ">" else ">"
    return fill(f"−√{n} {{{{1}}}} −{k}  (부등호 >, < 중 하나)", [[s2]],
                f"먼저 양수끼리 비교: {k} = √{k * k}, {n} {sgn} {k * k}이므로 √{n} {sgn} {k}\n"
                f"양변에 −를 붙이면 부등호 방향이 바뀝니다.\n따라서 −√{n} {s2} −{k}",
                "음수끼리는 절댓값이 큰 쪽이 더 작습니다.")

def l03_count(r):
    k = r.randint(3, 9); strict = r.choice([True, False])
    v = k * k - 1 if strict else k * k
    rel = "보다 작게" if strict else " 이하가 되게"
    return num(f"√n이 {k}{rel} 하는 자연수 n은 모두 몇 개일까요?", v,
               f"양변이 양수이므로 제곱해도 대소가 그대로입니다.\n√n {'<' if strict else '≤'} {k} → n {'<' if strict else '≤'} {k * k}\n"
               f"자연수 n은 1, 2, …, {v}이므로 {v}개",
               f"양변을 제곱하여 n의 범위를 구하세요.")

def l03_natural(r):
    a = r.choice([2, 3, 5, 6, 7, 10]); b = r.choice([1, 4, 9])
    n = a * b
    if b == 1 and r.random() < .5: return None
    return num(f"√({n}x)가 자연수가 되게 하는 가장 작은 자연수 x는?", a,
               f"근호 안이 제곱수여야 √가 자연수가 됩니다.\n{n} = {fstr(factor(n))}\n"
               f"지수가 홀수인 소인수를 곱해 지수를 짝수로 만듭니다. → x = {a}\n확인: {n} × {a} = {n * a} = {isqrt(n * a)}²",
               "근호 안의 수를 소인수분해해서 제곱수로 만드세요.")

def l03_between(r):
    a, b = r.randint(2, 40), r.randint(2, 60)
    lo, hi = -a ** .5, b ** .5
    ints = [z for z in range(-7, 9) if lo < z < hi]
    return num(f"−√{j(a,'와과')} √{b} 사이에 있는 정수는 몇 개일까요?", len(ints),
               f"제곱수와 비교해 위치를 찾습니다.\n{isqrt(a)}² ≤ {a} < {isqrt(a) + 1}² → {isqrt(a)} ≤ √{a} < {isqrt(a) + 1}, 그래서 −√{j(a,'는은')} −{j(isqrt(a) + 1,'와과')} −{isqrt(a)} 사이" +
               (" (정확히 −" + str(isqrt(a)) + ")" if isqrt(a) ** 2 == a else "") +
               f"\n{isqrt(b)}² ≤ {b} < {isqrt(b) + 1}² → √{j(b,'는은')} {j(isqrt(b),'와과')} {isqrt(b) + 1} 사이" +
               (" (정확히 " + str(isqrt(b)) + ")" if isqrt(b) ** 2 == b else "") +
               f"\n사이의 정수: {', '.join(m(z) for z in ints)} → {len(ints)}개 (양 끝은 포함하지 않음)",
               "각 수가 어떤 두 정수 사이에 있는지 제곱수로 확인하세요.")

L03 = [("넓이에서 한 변", l03_side), ("제곱근 두 개", l03_roots), ("음의 제곱근", l03_negroot),
       ("√(a²)의 성질", l03_sqsum), ("제곱근의 제곱", l03_sqof), ("제곱근의 대소", l03_cmp),
       ("범위의 자연수 세기", l03_count), ("자연수가 되는 조건", l03_natural), ("사이의 정수", l03_between)]

# ---------------- l04 무리수와 실수 ----------------
def l04_rep2(r):
    d = r.randint(1, 98)
    if d % 11 == 0: return None
    s = f"{d:02d}"; v = F(d, 99)
    return num(f"0.{s}{s}…({s}{"이" if bat(d) else "가"} 반복)를 기약분수로 나타내세요.", v,
               f"x = 0.{s}{s}…라 하면 100x = {d}.{s}{s}…\n100x − x = {d} → 99x = {d}\nx = {d}/99" +
               (f" = {fs(v)} (약분)" if v.denominator != 99 else " (더 약분되지 않음)"),
               "반복 부분이 두 자리이면 100을 곱해서 빼 보세요.", fmt="fraction")

def l04_rep1(r):
    a, b = r.randint(0, 9), r.randint(1, 9)
    if a == b: return None
    v = F(10 * a + b - a, 90)
    return num(f"0.{a}{b}{b}{b}…({j(b,'가이')} 반복)를 기약분수로 나타내세요.", v,
               f"x = 0.{a}{b}{b}{b}…라 하면\n100x = {a}{b}.{b}{b}…, 10x = {a}.{b}{b}…\n"
               f"100x − 10x = {10 * a + b} − {a} → 90x = {10 * a + b - a}\nx = {10 * a + b - a}/90" + (f" = {fs(v)} (약분)" if v.denominator != 90 else ""),
               "반복이 시작되는 곳을 맞추어 100x와 10x를 빼 보세요.", fmt="fraction")

def l04_simpl(r):
    a, b = r.randint(2, 7), r.choice([2, 3, 5, 6, 7])
    n = a * a * b
    if n > 300: return None
    return fill(f"√{n} = {{{{1}}}}√{{{{2}}}}", [str(a), str(b)],
                f"{j(n,'를을')} (제곱수) × (나머지)로 나눕니다: {n} = {a * a} × {b}\n√{n} = √{a * a} × √{b} = {a}√{b}",
                f"{j(n,'를을')} 나누는 가장 큰 제곱수를 찾으세요.")

def l04_mul(r):
    b = r.choice([2, 3, 5, 6, 7]); p, q = r.randint(1, 4), r.randint(1, 5)
    x, y = b * p * p, b * q * q
    if x == y: return None
    return num(f"√{x} × √{y} 의 값은?", b * p * q,
               f"√a × √b = √(ab)이므로 √{x} × √{y} = √{x * y}\n{x * y} = {b * p * q}²\n따라서 {b * p * q}",
               "√a × √b = √(ab)를 이용하세요.")

def l04_add(r):
    b = r.choice([2, 3, 5, 6, 7]); p, q = r.randint(1, 4), r.randint(1, 5)
    op = r.choice(["+", "−"]); v = p + q if op == "+" else p - q
    if abs(v) <= 1: return None
    x, y = b * p * p, b * q * q
    if x == y: return None
    def s(k, n): return f"√{n} = {k}√{b}" if k > 1 else f"√{n}"
    return fill(f"√{x} {op} √{y} = {{{{1}}}}√{b}", [alts(str(v))],
                f"각각을 a√{b} 꼴로 바꿉니다.\n" + ", ".join(t for t in [s(p, x), s(q, y)] if "=" in t) +
                f"\n근호 안이 같은 것끼리 계수를 계산: {p} {op} {q} = {m(v)}\n따라서 {m(v)}√{b}",
                f"두 수를 모두 □√{b} 꼴로 바꾸세요.")

def l04_between(r):
    a = r.randint(2, 30); b = r.randint(a + 3, 90)
    ints = [z for z in range(1, 10) if a < z * z < b]
    return num(f"√{j(a,'와과')} √{b} 사이에 있는 자연수는 몇 개일까요?", len(ints),
               f"자연수 k가 사이에 있으려면 √{a} < k < √{b}, 즉 {a} < k² < {b}\n"
               f"이 범위의 제곱수: {', '.join(f'{z * z}({z}²)' for z in ints) if ints else '없음'}\n따라서 {len(ints)}개",
               "각 변을 제곱하여 k²의 범위를 구하세요.")

def l04_irr(r):
    pool = [("√9", False), ("√12", True), ("0.121212…", False), ("π", True), ("−√16", False), ("3/7", False),
            ("√0.25", False), ("√2 + 1", True), ("√20", True), ("2.5", False), ("−√5", True), ("√49", False),
            ("1.010010001…", True), ("0.333…", False), ("√(4/9)", False), ("√3 / 2", True)]
    pick = r.sample(pool, 6)
    irr = [s for s, b in pick if b]
    why = {"√9": "=3", "−√16": "=−4", "√0.25": "=0.5", "√49": "=7", "√(4/9)": "=2/3",
           "0.121212…": "순환소수", "0.333…": "순환소수", "3/7": "분수", "2.5": "유한소수"}
    rat = [s + (f"({why[s]})" if s in why else "") for s, b in pick if not b]
    return num(f"다음 수 중 무리수는 몇 개일까요?  {',  '.join(s for s, _ in pick)}", len(irr),
               f"유리수(분수로 나타낼 수 있는 수): {', '.join(rat) if rat else '없음'}\n"
               f"무리수(순환하지 않는 무한소수): {', '.join(irr) if irr else '없음'}\n따라서 {len(irr)}개",
               "근호를 없앨 수 있는지, 순환소수인지 먼저 확인하세요.")

def l04_dec(r):
    d = r.choice([2, 4, 5, 8, 16, 20, 25, 40]); n = r.randint(1, d - 1)
    if gcd(n, d) > 1: return None
    v = n / d; s = f"{v:.6f}".rstrip("0")
    return num(f"{n}/{j(d,'를을')} 소수로 나타내세요.", s,
               f"분모 {d} = {fstr(factor(d))}는 소인수가 2, 5뿐이므로 유한소수가 됩니다.\n{n} ÷ {d} = {s}",
               "분자를 분모로 나누세요.", fmt="decimal")

L04 = [("순환소수 → 분수(두 자리)", l04_rep2), ("순환소수 → 분수(한 자리 반복)", l04_rep1), ("근호 밖으로 꺼내기", l04_simpl),
       ("제곱근의 곱", l04_mul), ("제곱근의 덧셈과 뺄셈", l04_add), ("사이의 자연수", l04_between),
       ("무리수 찾기", l04_irr), ("분수 → 소수", l04_dec)]

if __name__ == "__main__":
    tot = 0
    for l, T in [("l01", L01), ("l02", L02), ("l03", L03), ("l04", L04)]:
        n = write("c0", "ch01", l, T, per=6); tot += n; print(l, n)
    print("total", tot)
