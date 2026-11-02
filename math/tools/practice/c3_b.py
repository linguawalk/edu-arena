"""코스 3 · 챕터 4~5 (삼각함수, 삼각형과 삼각함수) — 연습 문제 은행"""
from core import *
import math

def nz(r, a, b):
    while True:
        x = r.randint(a, b)
        if x: return x
def rad(deg):
    """도 → 'kπ/n' 표기"""
    f_ = F(deg, 180)
    if f_ == 0: return "0"
    if f_.denominator == 1: return ("−" if f_ < 0 else "") + (f"{abs(f_.numerator)}π" if abs(f_.numerator) != 1 else "π")
    n = abs(f_.numerator)
    return ("−" if f_ < 0 else "") + (f"{n}π" if n != 1 else "π") + f"/{f_.denominator}"
# 특수각의 값: (분자 표기, 값) — sin, cos
SV = {0: ("0", 0), 30: ("1/2", .5), 45: ("√2/2", math.sqrt(2) / 2), 60: ("√3/2", math.sqrt(3) / 2), 90: ("1", 1)}
def trig_exact(fn, deg):
    """특수각 삼각함수값 표기와 실수값"""
    d = deg % 360
    s = math.sin(math.radians(d)); c = math.cos(math.radians(d))
    val = {"sin": s, "cos": c, "tan": (s / c if abs(c) > 1e-9 else None)}[fn]
    if val is None: return None, None
    table = {0: "0", .5: "1/2", 1: "1", round(math.sqrt(2) / 2, 6): "√2/2", round(math.sqrt(3) / 2, 6): "√3/2",
             round(math.sqrt(3), 6): "√3", round(math.sqrt(3) / 3, 6): "√3/3"}
    a = round(abs(val), 6)
    txt = table.get(a)
    if txt is None: return None, None
    return (("−" if val < -1e-9 else "") + txt), val
QUAD = lambda d: [1, 2, 3, 4][int((d % 360) // 90)] if (d % 90) else None

# ================= ch04 l01 일반각과 호도법 =================
def t1_coterm(r):
    a = r.randint(1, 35) * 10 + r.choice([0, 360, 720, -360, -720])
    if a % 360 == 0: return None
    v = a % 360
    return num(f"{m(a)}°의 동경과 같은 위치에 있는, 0° 이상 360° 미만의 각은 몇 도일까요?", v,
               f"360°의 정수배를 더하거나 빼도 동경의 위치는 같습니다.\n{m(a)}° = 360° × {m((a - v) // 360)} + {v}°\n따라서 {v}°", "360°를 더하거나 빼서 0° ~ 360° 사이로")

def t1_quad(r):
    a = r.choice([z for z in range(-700, 1000, 10) if z % 90])
    q = QUAD(a)
    return num(f"{m(a)}°는 제몇사분면의 각일까요?", q,
               f"{m(a)}° = 360° × {m((a - a % 360) // 360)} + {a % 360}°\n{a % 360}°는 제{q}사분면 (0~90 제1, 90~180 제2, 180~270 제3, 270~360 제4)", "먼저 0° ~ 360° 사이로 바꾸세요.")

def t1_conv(r):
    d = r.choice([15, 20, 30, 36, 45, 60, 72, 90, 120, 135, 150, 210, 225, 240, 270, 300, 315, 330])
    if r.random() < .5:
        return num(f"{rad(d)}는 몇 도일까요?", d, f"π = 180°이므로 {rad(d)} = {fs(F(d, 180))} × 180° = {d}°", "π를 180°로 바꾸세요.")
    f_ = F(d, 180)
    if f_.numerator == 1:
        return fill(f"{d}° = π/{{{{1}}}}", [str(f_.denominator)], f"1° = π/180이므로 {d}° = {d}π/180 = π/{f_.denominator}", "도 × π/180")
    return fill(f"{d}° = {{{{1}}}}π/{f_.denominator}", [str(f_.numerator)], f"{d}° = {d}π/180 = {f_.numerator}π/{f_.denominator}", "도 × π/180")

def t1_sector(r):
    rr = r.randint(2, 12); th = r.choice([F(1, 6), F(1, 4), F(1, 3), F(1, 2), F(2, 3), F(3, 4), F(5, 6), F(1, 1)])
    t = r.choice(["arc", "area"])
    if t == "arc":
        v = rr * th
        if v.denominator != 1: return None
        return fill(f"반지름 {rr}, 중심각 {rad(int(th * 180))}인 부채꼴의 호의 길이는 {{{{1}}}}π", [fs(v)],
                    f"l = rθ = {rr} × {rad(int(th * 180))} = {fs(v)}π", "호의 길이 l = rθ")
    v = F(rr * rr, 2) * th
    if v.denominator != 1: return None
    return fill(f"반지름 {rr}, 중심각 {rad(int(th * 180))}인 부채꼴의 넓이는 {{{{1}}}}π", [fs(v)],
                f"S = (1/2)r²θ = (1/2) × {rr * rr} × {rad(int(th * 180))} = {fs(v)}π", "넓이 S = (1/2)r²θ")

def t1_rad(r):
    t = r.choice(["theta", "max"])
    if t == "theta":
        rr, l = r.randint(2, 8), r.randint(1, 12)
        v = F(l, rr)
        return num(f"반지름 {rr}, 호의 길이 {l}인 부채꼴의 중심각은 몇 라디안일까요? (기약분수 또는 정수로)", v, f"l = rθ → θ = l/r = {l}/{rr}" + (f" = {fm(v)}" if (v.numerator, v.denominator) != (l, rr) else "") + "\n(라디안은 단위 없이 씁니다)", "θ = l/r",
                   fmt="fraction" if v.denominator > 1 else "integer")
    P = 4 * r.randint(2, 10)
    return num(f"둘레가 {P}인 부채꼴의 넓이의 최댓값은?", (P // 4) ** 2,
               f"반지름 r, 호 l = {P} − 2r\nS = (1/2)r({P} − 2r) = −(r − {P // 4})² + {(P // 4) ** 2}\nr = {P // 4}일 때 최댓값 {(P // 4) ** 2}", "넓이를 r의 이차함수로")

L41 = [("동경이 같은 각", t1_coterm), ("사분면", t1_quad), ("호도법 ↔ 육십분법", t1_conv), ("부채꼴의 호와 넓이", t1_sector), ("중심각과 최대 넓이", t1_rad)]

# ================= l02 삼각함수의 뜻 =================
TR = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]
def t2_point(r):
    a, b, c = r.choice(TR)
    if r.random() < .5: a, b = b, a
    x, y = a * r.choice([1, -1]), b * r.choice([1, -1])
    fn = r.choice(["sin", "cos", "tan"])
    num_, den = {"sin": (y, c), "cos": (x, c), "tan": (y, x)}[fn]
    v = F(num_, den)
    return num(f"각 θ의 동경 위의 점이 P({m(x)}, {m(y)})일 때 {fn} θ의 값은? (기약분수로)", v,
               f"r = √({x}² + {y}²) = {c}\nsin θ = y/r, cos θ = x/r, tan θ = y/x\n{fn} θ = {m(num_)}/{m(den)}" + (f" = {fm(v)}" if (v.numerator, v.denominator) != (num_, den) else ""), "r을 먼저 구하세요.", fmt="fraction" if v.denominator > 1 else "integer")

def t2_sign(r):
    q = r.randint(1, 4); fn = r.choice(["sin", "cos", "tan"])
    sg = {"sin": [1, 1, -1, -1], "cos": [1, -1, -1, 1], "tan": [1, -1, 1, -1]}[fn][q - 1]
    return num(f"θ가 제{q}사분면의 각일 때 {fn} θ의 부호는?  (양수 1, 음수 −1)", sg,
               f"제{q}사분면에서 x {'> 0' if q in (1, 4) else '< 0'}, y {'> 0' if q in (1, 2) else '< 0'}\n{fn} θ = {'y/r' if fn == 'sin' else 'x/r' if fn == 'cos' else 'y/x'} → {'양수' if sg > 0 else '음수'}",
               "얼(1)–싸(2)–안(3)–코(4): 양수인 함수")

def t2_val(r):
    d = r.choice([z for z in range(-330, 721, 30) if z % 90] + [z for z in range(-315, 721, 45) if z % 90])
    fn = r.choice(["sin", "cos", "tan"])
    txt, val = trig_exact(fn, d)
    if txt is None: return None
    ref = d % 360; ref = min(ref % 180, 180 - ref % 180)
    alts = [txt, txt.replace("−", "-")]
    if "√3/3" in txt: alts += [txt.replace("√3/3", "1/√3"), txt.replace("√3/3", "1/√3").replace("−", "-")]
    if "√2/2" in txt: alts += [txt.replace("√2/2", "1/√2"), txt.replace("√2/2", "1/√2").replace("−", "-")]
    if txt.strip("−") == "1/2": alts += [txt.replace("1/2", "0.5"), txt.replace("1/2", "0.5").replace("−", "-")]
    return fill(f"{fn} ({rad(d)}) = {{{{1}}}}", [alts],
                f"{rad(d)} = {d}°, 동경은 제{QUAD(d)}사분면, 기준각 {ref}°\n{fn} {ref}°의 값에 사분면의 부호를 붙입니다.\n{fn} ({rad(d)}) = {txt}", "기준각과 부호로 구하세요.")

def t2_given(r):
    a, b, c = r.choice(TR)
    if r.random() < .5: a, b = b, a
    q = r.randint(1, 4)
    sx, sy = (1 if q in (1, 4) else -1), (1 if q in (1, 2) else -1)
    x, y = sx * a, sy * b
    give = r.choice(["sin", "cos"]); ask = r.choice(["cos", "tan"] if give == "sin" else ["sin", "tan"])
    gv = F(y, c) if give == "sin" else F(x, c)
    av = {"sin": F(y, c), "cos": F(x, c), "tan": F(y, x)}[ask]
    return num(f"{give} θ = {fm(gv)}이고 θ가 제{q}사분면의 각일 때 {ask} θ의 값은? (기약분수로)", av,
               f"sin²θ + cos²θ = 1에서 {'cos' if give == 'sin' else 'sin'}²θ = 1 − {fs(gv * gv)} = {fs(1 - gv * gv)}\n제{q}사분면이므로 {'cos θ = ' + fm(F(x, c)) if give == 'sin' else 'sin θ = ' + fm(F(y, c))}\n{ask} θ = {fm(av)}",
               "sin²θ + cos²θ = 1과 사분면의 부호", fmt="fraction" if av.denominator > 1 else "integer")

def t2_sum(r):
    a, b, c = r.choice(TR)
    s, co = F(a, c), F(b, c)
    t = r.choice(["sq", "prod"])
    if t == "prod":
        k = s + co
        return num(f"sin θ + cos θ = {fm(k)}일 때 sin θ cos θ의 값은? (기약분수로)", s * co,
                   f"양변을 제곱: 1 + 2 sin θ cos θ = {fs(k * k)}\nsin θ cos θ = ({fs(k * k)} − 1)/2 = {fs(s * co)}", "제곱하면 sin²θ + cos²θ = 1이 나옵니다.", fmt="fraction")
    k = s - co
    v = 1 - k * k
    return num(f"sin θ − cos θ = {fm(k)}일 때 2 sin θ cos θ의 값은? (기약분수로)", v,
               f"제곱: 1 − 2 sin θ cos θ = {fs(k * k)}\n2 sin θ cos θ = 1 − {fs(k * k)} = {fs(v)}", "제곱해 보세요.", fmt="fraction" if v.denominator > 1 else "integer")

L42 = [("동경 위의 점", t2_point), ("삼각함수의 부호", t2_sign), ("특수각의 값", t2_val), ("한 값으로 나머지 구하기", t2_given), ("sin θ ± cos θ", t2_sum)]

# ================= l03 삼각함수의 그래프 =================
def t3_ext(r):
    a, b, fn = nz(r, -4, 5), r.randint(-5, 5), r.choice(["sin", "cos"])
    k = r.choice([1, 2, 3])
    t = r.choice(["max", "min"])
    v = (abs(a) + b) if t == "max" else (-abs(a) + b)
    return num(f"y = {'' if a == 1 else '−' if a == -1 else m(a) + ' '}{fn} {'' if k == 1 else k}x{term(b)}의 {'최댓값' if t == 'max' else '최솟값'}은?".replace("  ", " "), v,
               f"−1 ≤ {fn} {'' if k == 1 else k}x ≤ 1\n{'최댓값' if t == 'max' else '최솟값'} = {'' if t == 'max' else '−'}|{m(a)}|{term(b)} = {m(v)}", "진폭은 |a|, 중심선은 y = b")

def t3_period(r):
    fn = r.choice(["sin", "cos", "tan"]); k = r.choice([F(1), F(2), F(3), F(4), F(1, 2), F(1, 3), F(2, 3)])
    base = F(1) if fn == "tan" else F(2)
    P = base / k
    arg = "x" if k == 1 else f"{fs(k)}x" if k.denominator == 1 else f"(x/{k.denominator})" if k.numerator == 1 else f"({k.numerator}x/{k.denominator})"
    ans_ = fs(P)
    alts = [ans_ + "π" if ans_ != "1" else "π"]
    if P.denominator == 1:
        return fill(f"y = {fn} {arg}의 주기는 {{{{1}}}}π", [[ans_]] if ans_ != "1" else [["1"]],
                    f"y = {fn} kx의 주기는 {'π' if fn == 'tan' else '2π'}/|k|\n= {'π' if fn == 'tan' else '2π'} ÷ {fs(k)} = {ans_ if ans_ != '1' else ''}π", "주기 = 기본 주기 ÷ |k|")
    return fill(f"y = {fn} {arg}의 주기는 π/{{{{1}}}}" if P.numerator == 1 else f"y = {fn} {arg}의 주기는 {P.numerator}π/{{{{1}}}}", [[str(P.denominator)]],
                f"주기 = {'π' if fn == 'tan' else '2π'} ÷ {fs(k)} = {fs(P)}π", "주기 = 기본 주기 ÷ |k|")

def t3_point(r):
    fn = r.choice(["sin", "cos"]); a = r.randint(1, 4); b = r.randint(-3, 3)
    d = r.choice([0, 30, 60, 90, 120, 150, 180, 270])
    sh = r.choice([0, 90, -90, 180])
    txt, val = trig_exact(fn, d - sh)
    if txt is None or abs(a * val - round(a * val)) > 1e-9: return None
    v = round(a * val) + b
    shs = "" if sh == 0 else f" − {rad(sh)}" if sh > 0 else f" + {rad(-sh)}"
    return num(f"y = {'' if a == 1 else a}{fn} (x{shs}){term(b)}에서 x = {rad(d)}일 때의 값은?".replace("(x)", "x"), v,
               (f"{fn} ({rad(d)}{shs}) = {fn} ({rad(d - sh)}) = {txt}" if sh else f"{fn} {rad(d)} = {txt}") + f"\ny = {a} × {txt.replace('−', '(−') + (')' if '−' in txt else '')}{term(b)} = {m(v)}".replace("1 × ", ""), "괄호 안 각을 먼저 계산하세요.")

def t3_asym(r):
    k = r.choice([1, 2, 3, 4])
    v = 2 * k
    if r.random() < .5 and k > 1:
        return fill(f"y = tan {k}x의 그래프에서 이웃한 두 점근선 사이의 간격은 π/{{{{1}}}}", [str(k)],
                    f"y = tan {k}x의 주기는 π/{k}\n점근선도 주기마다 나타나므로 간격은 π/{k}", "점근선 간격 = 주기")
    return fill(f"y = tan {'' if k == 1 else k}x의 그래프의 점근선 중 가장 작은 양수 x는 π/{{{{1}}}}", [str(v)],
                f"tan θ는 θ = π/2 + nπ에서 정의되지 않습니다.\n{'' if k == 1 else k}x = π/2 → x = π/{v}", "tan의 점근선 θ = π/2 + nπ")

L43 = [("최댓값과 최솟값", t3_ext), ("주기", t3_period), ("함숫값", t3_point), ("tan의 점근선", t3_asym)]

# ================= l04 삼각함수의 성질과 방정식 =================
def t4_neg(r):
    d = r.choice([30, 45, 60]); fn = r.choice(["sin", "cos"])
    t = r.choice(["neg", "pi_minus", "pi_plus"])
    ang = {"neg": -d, "pi_minus": 180 - d, "pi_plus": 180 + d}[t]
    txt, val = trig_exact(fn, ang)
    if txt is None or "√" in txt: return None
    shown = {"neg": f"−{rad(d)}", "pi_minus": f"π − {rad(d)}", "pi_plus": f"π + {rad(d)}"}[t]
    rule = {"neg": "sin(−θ) = −sin θ, cos(−θ) = cos θ", "pi_minus": "sin(π − θ) = sin θ, cos(π − θ) = −cos θ", "pi_plus": "sin(π + θ) = −sin θ, cos(π + θ) = −cos θ"}[t]
    base, _ = trig_exact(fn, d)
    return num(f"{fn} ({shown})의 값은? (기약분수 또는 정수로)", F(txt.replace("−", "-")),
               f"{rule}\n{fn} {rad(d)} = {base}이므로 {fn} ({shown}) = {txt}", "각 변환 공식을 쓰세요.", fmt="fraction" if "/" in txt else "integer")

def t4_count(r):
    fn = r.choice(["sin", "cos", "tan"]); vals = {"sin": ["1/2", "−1/2", "√3/2", "1", "0", "−1", "√2/2", "2"], "cos": ["1/2", "−1/2", "−√3/2", "1", "0", "−1", "√2/2"], "tan": ["1", "−1", "√3", "0"]}[fn]
    k = r.choice(vals); kv = {"1/2": .5, "−1/2": -.5, "√3/2": .866, "−√3/2": -.866, "1": 1, "0": 0, "−1": -1, "√2/2": .707, "2": 2, "√3": 1.732}[k]
    if fn == "tan": c = 2
    elif abs(kv) > 1: c = 0
    elif abs(kv) == 1: c = 1
    elif fn == "sin" and kv == 0: c = 2
    else: c = 2
    sols = [d for d in range(0, 360, 15) if (fn != "tan" or d % 180 != 90) and abs({"sin": math.sin, "cos": math.cos, "tan": math.tan}[fn](math.radians(d)) - kv) < 1e-3]
    c = len(sols) if abs(kv) <= 1 or fn == "tan" else 0
    return num(f"0 ≤ x < 2π에서 {fn} x = {k}의 해는 몇 개일까요?", c,
               (f"해: {', '.join(rad(d) for d in sols)}\n→ {c}개" if c else f"−1 ≤ {fn} x ≤ 1이므로 {k}은 불가능 → 0개") +
               ("\n(tan의 주기는 π이므로 한 주기에 하나씩 2개)" if fn == "tan" else ""), "단위원이나 그래프에서 확인하세요.")

def t4_ineq(r):
    fn = r.choice(["sin", "cos"]); k = r.choice(["1/2", "√2/2", "√3/2", "0", "−1/2"]); op = r.choice([">", "<"])
    kv = {"1/2": .5, "√2/2": math.sqrt(2) / 2, "√3/2": math.sqrt(3) / 2, "0": 0, "−1/2": -.5}[k]
    f = {"sin": math.sin, "cos": math.cos}[fn]
    sols = [d for d in range(0, 360, 15) if abs(f(math.radians(d)) - kv) < 1e-6]
    if len(sols) != 2: return None
    a, b = sols
    mid = (a + b) / 2
    inside = (f(math.radians(mid)) > kv) == (op == ">")
    if not inside: return None
    fa, fb = F(a, 180), F(b, 180)
    den = fa.denominator if fa.denominator == fb.denominator else None
    if den is None or fa.numerator == 0: return None
    return fill(f"0 ≤ x < 2π에서 {fn} x {op} {k}의 해는 {rad(a)} < x < {{{{1}}}}π/{fb.denominator}" if fb.denominator > 1 else
                f"0 ≤ x < 2π에서 {fn} x {op} {k}의 해는 {rad(a)} < x < {{{{1}}}}π", [str(fb.numerator)],
                f"{fn} x = {k}인 x: {rad(a)}, {rad(b)}\n그 사이에서 {fn} x {op} {k}\n→ {rad(a)} < x < {rad(b)}", "등호일 때의 해를 먼저 찾고 그래프로 판단하세요.")

def t4_quad(r):
    t = r.choice(["a", "b", "c"])
    if t == "a":
        return num("0 ≤ x < 2π에서 2sin² x − sin x − 1 = 0의 해는 몇 개일까요?", 3,
                   "(2 sin x + 1)(sin x − 1) = 0\nsin x = −1/2 → 7π/6, 11π/6 (2개)\nsin x = 1 → π/2 (1개)\n모두 3개", "sin x = t로 치환")
    if t == "b":
        k = r.choice(["1/4", "3/4", "1/2"]); kv = {"1/4": .5, "3/4": math.sqrt(3) / 2, "1/2": math.sqrt(2) / 2}[k]
        fn = r.choice(["sin", "cos"])
        return num(f"0 ≤ x < 2π에서 {fn}² x = {k}의 해는 몇 개일까요?", 4,
                   f"{fn} x = ±√({k}) → 양수 쪽 2개, 음수 쪽 2개\n모두 4개", "±로 나누어 생각하세요.")
    a = r.choice([1, 2])
    return num(f"0 ≤ x < 2π에서 2cos² x {'−' if a == 1 else '+'} cos x − 1 = 0의 해는 몇 개일까요?" if a == 1 else "0 ≤ x < 2π에서 2cos² x + 3cos x + 1 = 0의 해는 몇 개일까요?", 3,
               ("(2 cos x + 1)(cos x − 1) = 0\ncos x = −1/2 → 2π/3, 4π/3 (2개)\ncos x = 1 → 0 (1개)\n모두 3개") if a == 1 else
               ("(2 cos x + 1)(cos x + 1) = 0\ncos x = −1/2 → 2π/3, 4π/3 (2개)\ncos x = −1 → π (1개)\n모두 3개"), "cos x = t로 치환")

def t4_max(r):
    k = r.randint(0, 3)
    # y = sin x + cos² x + k = −sin² x + sin x + 1 + k → max at sin x = 1/2: 5/4 + k
    return num(f"y = sin x + cos² x{term(k)}의 최댓값은? (기약분수로)", F(5, 4) + k,
               f"cos² x = 1 − sin² x → y = −sin² x + sin x + 1{term(k)}\nsin x = t (−1 ≤ t ≤ 1): y = −(t − 1/2)² + {fs(F(5, 4) + k)}\nt = 1/2일 때 최댓값 {fs(F(5, 4) + k)}", "한 종류의 삼각함수로 통일하세요.", fmt="fraction")

L44 = [("각의 변환", t4_neg), ("방정식의 해의 개수", t4_count), ("삼각부등식", t4_ineq), ("이차식 꼴 방정식", t4_quad), ("최댓값", t4_max)]

# ================= ch05 삼각형과 삼각함수 =================
def s1_R(r):
    t = r.choice(["R", "a", "sin"])
    A = r.choice([30, 90, 150]); R = r.randint(1, 10)
    a = 2 * R * (1 if A == 90 else F(1, 2))
    if t == "R":
        return num(f"A = {A}°, a = {fs(a)}인 삼각형의 외접원의 반지름은?", R,
                   f"사인법칙: a/sin A = 2R\n{fs(a)} ÷ sin {A}° = {fs(a)} ÷ {fs(F(1, 2)) if A != 90 else 1} = {2 * R} = 2R → R = {R}", "a/sin A = 2R")
    if t == "a":
        return num(f"외접원의 반지름이 {R}이고 A = {A}°일 때 a의 값은?", a,
                   f"a = 2R sin A = 2 × {R} × {'1/2' if A != 90 else '1'} = {fs(a)}", "a = 2R sin A")
    a2 = r.randint(1, 2 * R - 1)
    return num(f"외접원의 반지름이 {R}인 삼각형에서 a = {a2}일 때 sin A의 값은? (기약분수로)", F(a2, 2 * R),
               f"sin A = a/(2R) = {a2}/{2 * R} = {fs(F(a2, 2 * R))}", "sin A = a/2R", fmt="fraction")

def s1_side(r):
    A, B = r.sample([30, 45, 60, 90, 120, 135], 2)
    if A + B >= 180: return None
    sA, sB = math.sin(math.radians(A)), math.sin(math.radians(B))
    k = r.randint(1, 6)
    a = sA * 2 * k  # 2R = 2k
    b = sB * 2 * k
    def surd(x):
        for c, rt in [(1, 1), (1, 2), (1, 3), (1, 6)]:
            for co in range(1, 50):
                if abs(x - co * math.sqrt(rt)) < 1e-9: return co, rt
        return None
    sa, sb_ = surd(a), surd(b)
    if not sa or not sb_ or sb_[1] == 1 and sa[1] == 1: return None
    fa = f"{sa[0] if sa[0] > 1 else ''}√{sa[1]}" if sa[1] > 1 else str(sa[0])
    if sb_[1] == 1:
        return num(f"A = {A}°, B = {B}°, a = {fa}일 때 b의 값은?", sb_[0],
                   f"사인법칙: a/sin A = b/sin B\nb = a × sin B / sin A = {fa} × sin {B}° ÷ sin {A}° = {sb_[0]}", "a/sin A = b/sin B")
    return fill(f"A = {A}°, B = {B}°, a = {fa}일 때 b = {{{{1}}}}√{sb_[1]}" if sb_[0] > 1 else f"A = {A}°, B = {B}°, a = {fa}일 때 b = √{{{{1}}}}", [str(sb_[0]) if sb_[0] > 1 else str(sb_[1])],
                f"사인법칙: b = a × sin B / sin A\n= {fa} × sin {B}° ÷ sin {A}° = {sb_[0] if sb_[0] > 1 else ''}√{sb_[1]}", "a/sin A = b/sin B")

def s1_ratio(r):
    p, q, s_ = r.choice([(3, 4, 5), (2, 3, 4), (5, 12, 13), (1, 1, 1), (3, 5, 7), (4, 5, 6)])
    k = r.randint(1, 4); which = r.choice([("a", p), ("b", q), ("c", s_)]); ask = r.choice([("a", p), ("b", q), ("c", s_)])
    if which == ask: return None
    return num(f"sin A : sin B : sin C = {p} : {q} : {s_}이고 {which[0]} = {which[1] * k}일 때 {ask[0]}의 값은?", ask[1] * k,
               f"사인법칙에서 a : b : c = sin A : sin B : sin C = {p} : {q} : {s_}\n{which[0]} = {which[1]}k = {which[1] * k} → k = {k}\n{ask[0]} = {ask[1]} × {k} = {ask[1] * k}", "변의 비 = 사인의 비")

L51 = [("외접원의 반지름", s1_R), ("사인법칙으로 변 구하기", s1_side), ("사인의 비와 변의 비", s1_ratio)]

TRI = [(3, 5, 7, 120), (5, 7, 8, 60), (3, 7, 8, 60), (5, 3, 7, 120), (8, 3, 7, 60), (7, 8, 13, 120), (5, 8, 7, 60), (8, 5, 7, 60), (3, 8, 7, 60),
       (6, 10, 14, 120), (10, 16, 14, 60), (6, 16, 14, 60), (7, 15, 13, 60), (15, 8, 13, 60)]
def s2_side(r):
    b, c, a, A = r.choice(TRI)
    return num(f"두 변이 {b}, {c}이고 끼인각이 {A}°인 삼각형의 나머지 변의 길이는?", a,
               f"코사인법칙: a² = b² + c² − 2bc cos A\n= {b * b} + {c * c} − 2×{b}×{c}×({'1/2' if A == 60 else '−1/2'}) = {a * a}\na = {a}", "a² = b² + c² − 2bc cos A")

def s2_angle(r):
    b, c, a, A = r.choice(TRI)
    t = r.choice(["deg", "cos"])
    if t == "deg":
        return num(f"세 변이 a = {a}, b = {b}, c = {c}일 때 A는 몇 도일까요?", A,
                   f"cos A = (b² + c² − a²)/(2bc) = ({b * b} + {c * c} − {a * a})/{2 * b * c} = {fm(F(b * b + c * c - a * a, 2 * b * c))}\nA = {A}°", "cos A = (b² + c² − a²)/2bc")
    a, b, c = sorted(r.sample(range(2, 10), 3))
    if a + b <= c: return None
    v = F(a * a + b * b - c * c, 2 * a * b)
    return num(f"a = {a}, b = {b}, c = {c}일 때 cos C의 값은? (기약분수 또는 정수로)", v,
               f"cos C = (a² + b² − c²)/(2ab) = ({a * a} + {b * b} − {c * c})/{2 * a * b} = {fm(v)}", "cos C = (a² + b² − c²)/2ab", fmt="fraction" if v.denominator > 1 else "integer")

def s2_type(r):
    a, b, c = sorted(r.sample(range(2, 15), 3))
    if a + b <= c: return None
    d = a * a + b * b - c * c
    v = 1 if d > 0 else 2 if d == 0 else 3
    return num(f"세 변이 {a}, {b}, {c}인 삼각형은?  (예각삼각형 1, 직각삼각형 2, 둔각삼각형 3)", v,
               f"가장 긴 변 {c}의 맞은각을 봅니다.\n{a}² + {b}² = {a * a + b * b}, {c}² = {c * c}\n" + ("합이 더 큼 → 예각삼각형" if d > 0 else "같음 → 직각삼각형" if d == 0 else "합이 더 작음 → 둔각삼각형"),
               "가장 긴 변의 제곱과 나머지 두 변의 제곱의 합 비교")

def s2_irr(r):
    b, c = r.randint(2, 8), r.randint(2, 8); A = r.choice([60, 120])
    a2 = b * b + c * c - (b * c if A == 60 else -b * c)
    if isqrt(a2) ** 2 == a2: return None
    return fill(f"b = {b}, c = {c}, A = {A}°일 때 a = √{{{{1}}}}", [str(a2)],
                f"a² = {b * b} + {c * c} − 2×{b}×{c}×cos {A}° = {b * b + c * c} {'−' if A == 60 else '+'} {b * c} = {a2}\na = √{a2}", "코사인법칙")

L52 = [("코사인법칙: 변", s2_side), ("코사인법칙: 각", s2_angle), ("삼각형의 모양", s2_type), ("결과가 무리수", s2_irr)]

def s3_area(r):
    a, b = r.randint(2, 12), r.randint(2, 12); C = r.choice([30, 150, 90, 60, 120, 45])
    if C in (30, 150, 90):
        v = F(a * b, 4) if C != 90 else F(a * b, 2)
        return num(f"두 변이 {a}, {b}이고 끼인각이 {C}°인 삼각형의 넓이는?", f"{float(v):g}",
                   f"S = (1/2)ab sin C = (1/2) × {a} × {b} × sin {C}° = (1/2) × {a * b} × {'1/2' if C != 90 else '1'} = {float(v):g}", "S = (1/2)ab sin C",
                   fmt="integer" if v.denominator == 1 else "decimal")
    if C in (60, 120):
        v = F(a * b, 4)
        if v.denominator != 1: return None
        return fill(f"두 변이 {a}, {b}이고 끼인각이 {C}°인 삼각형의 넓이는 {{{{1}}}}√3", [str(int(v))],
                    f"S = (1/2) × {a} × {b} × √3/2 = {int(v)}√3", "sin 60° = sin 120° = √3/2")
    v = F(a * b, 4)
    if v.denominator != 1: return None
    return fill(f"두 변이 {a}, {b}이고 끼인각이 45°인 삼각형의 넓이는 {{{{1}}}}√2", [str(int(v))], f"S = (1/2) × {a} × {b} × √2/2 = {int(v)}√2", "sin 45° = √2/2")

def s3_heron(r):
    a, b, c, S = r.choice([(5, 5, 6, 12), (13, 14, 15, 84), (5, 5, 8, 12), (10, 10, 12, 48), (6, 8, 10, 24), (9, 10, 17, 36), (7, 15, 20, 42), (3, 4, 5, 6), (10, 13, 13, 60), (8, 15, 17, 60)])
    return num(f"세 변이 {a}, {b}, {c}인 삼각형의 넓이는?", S,
               f"헤론의 공식: s = ({a} + {b} + {c})/2 = {(a + b + c) // 2}\nS = √(s(s − a)(s − b)(s − c)) = √({(a + b + c) // 2}×{(a + b + c) // 2 - a}×{(a + b + c) // 2 - b}×{(a + b + c) // 2 - c}) = {S}",
               "헤론의 공식 또는 높이를 구하세요.")

def s3_inr(r):
    a, b, c = r.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17)])
    t = r.choice(["r", "R"])
    S = a * b // 2
    if t == "r":
        v = F(2 * S, a + b + c)
        return num(f"세 변이 {a}, {b}, {c}인 삼각형의 내접원의 반지름은?", v,
                   f"직각삼각형, 넓이 S = {S}\nS = (1/2)r(a + b + c) → r = 2S/(a + b + c) = {2 * S}/{a + b + c} = {fm(v)}", "S = (1/2)r(a + b + c)", fmt="fraction" if v.denominator > 1 else "integer")
    return num(f"세 변이 {a}, {b}, {c}인 삼각형의 외접원의 반지름은? (기약분수 또는 정수로)", F(c, 2),
               f"빗변이 {c}인 직각삼각형 → 외접원의 지름 = 빗변\nR = {c}/2" + (f" = {c // 2}" if c % 2 == 0 else ""), "직각삼각형의 외접원 지름은 빗변", fmt="fraction" if c % 2 else "integer")

def s3_quad(r):
    p, q = r.randint(2, 12), r.randint(2, 12)
    t = r.choice(["diag", "para"])
    if t == "diag":
        v = F(p * q, 4)
        return num(f"두 대각선이 {p}, {q}이고 끼인각이 30°인 사각형의 넓이는?", f"{float(v):g}",
                   f"S = (1/2) × {p} × {q} × sin 30° = {float(v):g}", "S = (1/2)pq sin θ", fmt="integer" if v.denominator == 1 else "decimal")
    v = F(p * q, 2)
    if v.denominator != 1: return None
    return fill(f"두 변이 {p}, {q}이고 끼인각이 60°인 평행사변형의 넓이는 {{{{1}}}}√3", [str(int(v))],
                f"평행사변형 = 삼각형 2개 → S = ab sin θ = {p} × {q} × √3/2 = {int(v)}√3", "평행사변형의 넓이 = ab sin θ")

L53 = [("두 변과 끼인각", s3_area), ("세 변으로 넓이", s3_heron), ("내접원·외접원", s3_inr), ("사각형의 넓이", s3_quad)]

def s4_elev(r):
    d = r.choice([10, 12, 15, 20, 24, 30, 50, 100]); ang = r.choice([30, 45, 60])
    if ang == 45:
        return num(f"건물에서 {d}m 떨어진 곳에서 꼭대기를 올려본각이 45°입니다. 눈높이를 무시하면 건물의 높이는 몇 m일까요?", d, f"높이 = {d} × tan 45° = {d}m", "높이 = 거리 × tan")
    if ang == 60:
        return fill(f"{d}m 떨어진 곳에서 올려본각이 60°일 때 높이는 {{{{1}}}}√3 m", [str(d)], f"높이 = {d} × tan 60° = {d}√3 m", "tan 60° = √3")
    if d % 3: return None
    return fill(f"{d}m 떨어진 곳에서 올려본각이 30°일 때 높이는 {{{{1}}}}√3 m", [str(d // 3)], f"높이 = {d} × tan 30° = {d} × √3/3 = {d // 3}√3 m", "tan 30° = √3/3")

def s4_lake(r):
    b, c, a, A = r.choice(TRI)
    return num(f"P에서 호수 양 끝 A, B까지 각각 {b}km, {c}km이고 ∠APB = {A}°일 때 AB는 몇 km일까요?", a,
               f"코사인법칙: AB² = {b}² + {c}² − 2×{b}×{c}×cos {A}° = {a * a}\nAB = {a}km", "코사인법칙")

def s4_slope(r):
    L_, ang = r.choice([10, 20, 30, 40, 50, 80]), 30
    return num(f"경사각 30°인 비탈길을 {L_}m 올라가면 높이는 몇 m 올라갈까요?", L_ // 2, f"높이 = {L_} × sin 30° = {L_} × 1/2 = {L_ // 2}m", "높이 = 빗변 × sin")

def s4_ship(r):
    a, b, c = r.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17)])
    k = r.choice([1, 2])
    return num(f"두 배가 같은 곳에서 출발해 한 배는 동쪽으로 시속 {a}km, 다른 배는 북쪽으로 시속 {b}km로 갑니다. {k}시간 후 두 배 사이의 거리는 몇 km일까요?", c * k,
               f"{k}시간 후 {a * k}km, {b * k}km → 직각삼각형\n거리 = √({a * k}² + {b * k}²) = {c * k}km", "두 방향이 직각입니다.")

def s4_approach(r):
    d = r.choice([10, 20, 30, 40, 50])
    return fill(f"탑 쪽으로 {d}m 다가가며 올려본각이 30°에서 60°로 바뀌었다면 탑의 높이는 {{{{1}}}}√3 m", [fs(F(d, 2))],
                f"올려본각 30°, 60°인 두 지점과 꼭대기가 이루는 삼각형은 이등변삼각형 → 가까운 지점에서 꼭대기까지 {d}m\n높이 = {d} × sin 60° = {fs(F(d, 2))}√3 m",
                "외각의 성질로 이등변삼각형을 찾으세요.")

L54 = [("올려본각", s4_elev), ("코사인법칙 측량", s4_lake), ("비탈길", s4_slope), ("두 배 사이 거리", s4_ship), ("두 지점에서 측량", s4_approach)]

ALL = {"ch04": [L41, L42, L43, L44], "ch05": [L51, L52, L53, L54]}

if __name__ == "__main__":
    tot = 0
    for ch, Ls in ALL.items():
        for i, T in enumerate(Ls, 1):
            per = 6 if len(T) >= 7 else 8 if len(T) >= 5 else 10 if len(T) >= 4 else 14 if len(T) == 3 else 20
            n = write("c3", ch, f"l0{i}", T, per=per, seed=3 + i); tot += n; print(ch, i, len(T), n)
    print("total", tot)
