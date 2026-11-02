"""코스 0 · 챕터 5 도형 기초 — 연습 문제 은행"""
from core import *

TRIPLES = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41)]
def triple(r, maxc=60):
    while True:
        a, b, c = r.choice(TRIPLES); k = r.randint(1, 4)
        if c * k <= maxc: return a * k, b * k, c * k

# ---------------- l01 닮음 ----------------
def l01_side(r):
    p, q = r.choice([(1, 2), (1, 3), (2, 3), (3, 4), (2, 5), (3, 5), (4, 5)])
    k = r.randint(1, 6); s = p * k
    return num(f"닮음비가 {p} : {q}인 두 삼각형에서 작은 삼각형의 한 변이 {s}cm일 때, 이에 대응하는 큰 삼각형의 변은 몇 cm일까요?", q * k,
               f"대응변의 길이의 비가 닮음비입니다.\n{p} : {q} = {s} : x\n{p}x = {q * s} → x = {q * k}",
               "비례식을 세우세요: 작은 변 : 큰 변 = p : q")

def l01_area(r):
    p, q = r.choice([(1, 2), (1, 3), (2, 3), (3, 4), (2, 5), (3, 5), (4, 5), (1, 4)])
    return fill(f"닮음비가 {p} : {q}인 두 도형의 넓이의 비는 {{{{1}}}} : {{{{2}}}}", [str(p * p), str(q * q)],
                f"길이가 {p} : {q}이면 넓이는 가로와 세로가 모두 그 비로 커지므로 제곱의 비입니다.\n{p}² : {q}² = {p * p} : {q * q}",
                "넓이의 비는 닮음비의 제곱입니다.")

def l01_area2(r):
    p, q = r.choice([(1, 2), (1, 3), (2, 3), (3, 4), (2, 5)])
    k = r.randint(1, 5); A = p * p * k
    return num(f"닮음비가 {p} : {q}인 두 도형에서 작은 도형의 넓이가 {A}cm²일 때, 큰 도형의 넓이는 몇 cm²일까요?", q * q * k,
               f"넓이의 비 = {p}² : {q}² = {p * p} : {q * q}\n{p * p} : {q * q} = {A} : x → x = {A} × {q * q} ÷ {p * p} = {q * q * k}",
               "넓이의 비는 닮음비의 제곱입니다.")

def l01_vol(r):
    p, q = r.choice([(1, 2), (1, 3), (2, 3), (1, 4)])
    k = r.randint(1, 6); V = p ** 3 * k
    return num(f"닮음비가 {p} : {q}인 두 입체도형에서 작은 도형의 부피가 {V}cm³일 때, 큰 도형의 부피는 몇 cm³일까요?", q ** 3 * k,
               f"부피의 비는 닮음비의 세제곱입니다: {p}³ : {q}³ = {p ** 3} : {q ** 3}\nx = {V} × {q ** 3} ÷ {p ** 3} = {q ** 3 * k}",
               "부피는 가로·세로·높이가 모두 커지므로 세제곱의 비입니다.")

def l01_shadow(r):
    st, sh = r.choice([(1, 1.5), (1, 2), (2, 3), (1.5, 2), (1, 0.8), (2, 2.5)])
    k = r.choice([2, 3, 4, 5, 6, 8])
    H, S = st * k, sh * k
    g = lambda x: f"{x:g}"
    return num(f"길이 {g(st)}m인 막대의 그림자가 {g(sh)}m일 때, 같은 시각 그림자가 {g(S)}m인 나무의 높이는 몇 m일까요?", g(H),
               f"같은 시각에는 (높이) : (그림자)의 비가 같습니다. (닮은 삼각형)\n{g(st)} : {g(sh)} = x : {g(S)}\nx = {g(st)} × {g(S)} ÷ {g(sh)} = {g(H)}",
               "막대와 나무가 만드는 두 직각삼각형은 닮음입니다.", fmt="integer" if H == int(H) else "decimal")

def l01_map(r):
    sc, cm = r.choice([(25000, 4), (50000, 2), (50000, 6), (20000, 5), (100000, 3), (25000, 8), (10000, 15)])
    km = F(sc * cm, 100000)
    return num(f"축척이 1 : {sc}인 지도에서 {cm}cm인 거리는 실제로 몇 km일까요?", f"{float(km):g}",
               f"실제 거리 = {cm} × {sc} = {sc * cm:,}cm\n1km = 100,000cm이므로 {sc * cm:,} ÷ 100,000 = {float(km):g}km",
               "cm → km는 100,000으로 나눕니다.", fmt="integer" if km.denominator == 1 else "decimal")

def l01_par(r):
    ad, db = r.randint(2, 6), r.randint(1, 5); k = r.randint(1, 3)
    ae = ad * k
    ec = F(db * ae, ad)
    if ec.denominator != 1: return None
    return num(f"삼각형 ABC에서 변 AB 위의 점 D, 변 AC 위의 점 E에 대해 DE가 BC와 평행합니다. AD = {ad}, DB = {db}, AE = {ae}일 때 EC의 길이는?", int(ec),
               f"DE ∥ BC이면 AD : DB = AE : EC\n{ad} : {db} = {ae} : x\n{ad}x = {db * ae} → x = {int(ec)}",
               "평행선이 두 변을 같은 비로 나눕니다.")

def l01_pizza(r):
    d1, d2 = r.choice([(20, 30), (20, 40), (30, 40), (24, 36), (25, 30)])
    p1 = r.choice([8000, 10000, 12000, 16000])
    p2 = F(p1 * d2 * d2, d1 * d1)
    if p2.denominator != 1 or p2 % 100: return None
    return num(f"지름 {d1}cm 피자가 {p1:,}원입니다. 넓이에 비례해 가격을 정한다면 지름 {d2}cm 피자는 몇 원일까요?", int(p2),
               f"닮음비 {d1} : {d2} → 넓이의 비 {d1 * d1} : {d2 * d2}\n가격 = {p1} × {d2 * d2}/{d1 * d1} = {int(p2)}원",
               "넓이의 비는 지름의 비의 제곱입니다.")

L01 = [("대응변의 길이", l01_side), ("넓이의 비", l01_area), ("넓이 구하기", l01_area2), ("부피의 비", l01_vol),
       ("그림자로 높이 재기", l01_shadow), ("축척", l01_map), ("평행선과 선분의 비", l01_par), ("닮음의 활용", l01_pizza)]

# ---------------- l02 피타고라스 정리 ----------------
def l02_hyp(r):
    a, b, c = triple(r)
    return num(f"직각을 낀 두 변이 {a}, {b}인 직각삼각형의 빗변의 길이는?", c,
               f"a² + b² = c²\n{a}² + {b}² = {a * a} + {b * b} = {c * c}\nc = √{c * c} = {c}", "두 변의 제곱의 합 = 빗변의 제곱")

def l02_leg(r):
    a, b, c = triple(r)
    return num(f"빗변이 {c}, 다른 한 변이 {a}인 직각삼각형의 나머지 한 변의 길이는?", b,
               f"x² + {a}² = {c}²\nx² = {c * c} − {a * a} = {b * b}\nx = {b}", "빗변의 제곱에서 다른 변의 제곱을 빼세요.")

def l02_irr(r):
    a, b = r.randint(1, 7), r.randint(1, 7)
    s = a * a + b * b
    if isqrt(s) ** 2 == s: return None
    return fill(f"직각을 낀 두 변이 {a}, {b}인 직각삼각형의 빗변의 길이는 √{{{{1}}}}", [str(s)],
                f"빗변² = {a}² + {b}² = {a * a} + {b * b} = {s}\n{j(s, '는은')} 제곱수가 아니므로 빗변 = √{s}", "제곱의 합을 구하세요.")

def l02_dist(r):
    a, b, c = triple(r, 30)
    x1, y1 = r.randint(-4, 4), r.randint(-4, 4)
    sx, sy = r.choice([1, -1]), r.choice([1, -1])
    if r.random() < .5: a, b = b, a
    x2, y2 = x1 + sx * a, y1 + sy * b
    return num(f"좌표평면 위의 두 점 ({m(x1)}, {m(y1)}), ({m(x2)}, {m(y2)}) 사이의 거리는?", c,
               f"x좌표의 차 {a}, y좌표의 차 {b}를 두 변으로 하는 직각삼각형의 빗변입니다.\n거리² = {a}² + {b}² = {c * c}\n거리 = {c}",
               "좌표의 차를 직각삼각형의 두 변으로 보세요.")

def l02_ladder(r):
    a, b, c = triple(r, 26)
    return num(f"길이 {c}m인 사다리를 벽에 기대 세웠더니 사다리 밑이 벽에서 {a}m 떨어졌습니다. 사다리 꼭대기는 바닥에서 몇 m 높이일까요?", b,
               f"벽, 바닥, 사다리가 직각삼각형을 이룹니다. (사다리가 빗변)\nh² = {c}² − {a}² = {c * c} − {a * a} = {b * b}\nh = {b}",
               "사다리가 빗변입니다.")

def l02_count(r):
    pool = [((3, 4, 5), 1), ((6, 8, 10), 1), ((5, 12, 13), 1), ((7, 24, 25), 1), ((8, 15, 17), 1), ((9, 12, 15), 1),
            ((4, 5, 6), 0), ((6, 8, 11), 0), ((5, 6, 8), 0), ((2, 3, 4), 0), ((7, 8, 10), 0), ((10, 24, 25), 0)]
    pick = r.sample(pool, 4)
    v = sum(x for _, x in pick)
    lines = [f"({a}, {b}, {c}): {a * a} + {b * b} = {a * a + b * b} {'=' if a * a + b * b == c * c else '≠'} {c * c}" for (a, b, c), _ in pick]
    return num(f"세 변이 {', '.join(str(t) for t, _ in pick)}인 삼각형 중 직각삼각형은 몇 개일까요?", v,
               "가장 긴 변의 제곱이 나머지 두 변의 제곱의 합과 같은지 확인합니다.\n" + "\n".join(lines) + f"\n따라서 {v}개",
               "가장 긴 변이 빗변이 되는지 확인하세요.")

def l02_eq(r):
    k = r.randint(1, 8)
    return fill(f"한 변이 {2 * k}인 정삼각형의 높이는 {{{{1}}}}√3입니다." if k > 1 else f"한 변이 2인 정삼각형의 높이는 √{{{{1}}}}입니다.", [str(k) if k > 1 else "3"],
                f"높이는 밑변을 반으로 나눕니다: 빗변 {2 * k}, 밑변의 절반 {k}\nh² = {2 * k}² − {k}² = {4 * k * k} − {k * k} = {3 * k * k}\nh = √{3 * k * k}" + (f" = {k}√3" if k > 1 else ""),
                "정삼각형의 높이는 밑변의 중점으로 내려옵니다.")

def l02_box(r):
    a, b, c, d = r.choice([(1, 2, 2, 3), (2, 3, 6, 7), (1, 4, 8, 9), (2, 6, 9, 11), (4, 4, 7, 9), (6, 6, 7, 11), (2, 10, 11, 15), (3, 4, 12, 13)])
    return num(f"가로 {a}, 세로 {b}, 높이 {c}인 직육면체의 대각선의 길이는?", d,
               f"대각선² = 가로² + 세로² + 높이²\n= {a * a} + {b * b} + {c * c} = {d * d}\n대각선 = {d}",
               "밑면의 대각선을 먼저 구하고, 높이와 함께 다시 피타고라스 정리를 쓰세요.")

L02 = [("빗변 구하기", l02_hyp), ("나머지 한 변", l02_leg), ("빗변이 무리수", l02_irr), ("두 점 사이의 거리", l02_dist),
       ("사다리 문제", l02_ladder), ("직각삼각형 판별", l02_count), ("정삼각형의 높이", l02_eq), ("직육면체의 대각선", l02_box)]

# ---------------- l03 삼각비 ----------------
def l03_ratio(r):
    a, b, c = r.choice(TRIPLES[:5])
    if r.random() < .5: a, b = b, a
    k = r.randint(1, 3)
    which = r.choice(["sin", "cos", "tan"])
    num_, den = {"sin": (a, c), "cos": (b, c), "tan": (a, b)}[which]
    name = {"sin": "BC/AB (대변/빗변)", "cos": "AC/AB (밑변/빗변)", "tan": "BC/AC (대변/밑변)"}[which]
    return fill(f"∠C = 90°, BC = {a * k}, AC = {b * k}, AB = {c * k}인 직각삼각형에서 {which} A = {{{{1}}}}/{{{{2}}}}  (기약분수로)", [str(num_), str(den)],
                f"{which} A = {name}\n= {num_ * k}/{den * k}" + (f" = {num_}/{den}" if k > 1 else ""),
                "∠A에서 보면 BC는 마주 보는 변(대변), AC는 이웃한 변(밑변), AB는 빗변입니다.")

SPEC = [("sin 30°", ["1/2", "0.5"]), ("cos 30°", ["√3/2"]), ("tan 30°", ["√3/3", "1/√3"]),
        ("sin 45°", ["√2/2", "1/√2"]), ("cos 45°", ["√2/2", "1/√2"]), ("tan 45°", ["1"]),
        ("sin 60°", ["√3/2"]), ("cos 60°", ["1/2", "0.5"]), ("tan 60°", ["√3"])]
def l03_spec(r):
    a, b = r.sample(SPEC, 2)
    if r.random() < .5:
        nm, vals = a
        return fill(f"{nm} = {{{{1}}}}", [vals],
                    f"특수각의 삼각비\n30°, 60°: 세 변의 비가 1 : √3 : 2인 직각삼각형\n45°: 세 변의 비가 1 : 1 : √2인 직각이등변삼각형\n따라서 {nm} = {vals[0]}",
                    "1 : √3 : 2, 1 : 1 : √2 삼각형을 그려 보세요.")
    return None

def l03_specsum(r):
    combos = [("sin 30° + cos 60°", "1"), ("tan 45° + sin 30°", "3/2"), ("sin 60° × cos 30°", "3/4"), ("tan 60° × tan 30°", "1"),
              ("cos 60° × tan 45°", "1/2"), ("sin 45° × cos 45°", "1/2"), ("2 sin 30° + tan 45°", "2"), ("(sin 60°)² + (cos 60°)²", "1"),
              ("tan 45° − cos 60°", "1/2"), ("4 sin 30° × cos 60°", "1")]
    e, v = r.choice(combos)
    vals = {"sin 30°": "1/2", "cos 60°": "1/2", "tan 45°": "1", "sin 60°": "√3/2", "cos 30°": "√3/2", "tan 60°": "√3", "tan 30°": "√3/3",
            "sin 45°": "√2/2", "cos 45°": "√2/2"}
    used = [k for k in vals if k in e]
    sub = e
    for k in used: sub = sub.replace(k, f"({vals[k]})")
    return num(f"{e}의 값은?", F(v), "값을 넣습니다: " + ", ".join(f"{k} = {vals[k]}" for k in used) + f"\n{sub}\n= {v}",
               "특수각의 삼각비 값을 대입하세요.", fmt="fraction" if "/" in v else "integer")

def l03_side(r):
    ang = r.choice([30, 60]); h = 2 * r.randint(1, 10)
    what = r.choice(["adj", "opp"])
    if ang == 60 and what == "adj" or ang == 30 and what == "opp":
        return num(f"빗변이 {h}이고 ∠A = {ang}°인 직각삼각형에서 ∠A의 {'이웃변(밑변)' if what == 'adj' else '대변'}의 길이는?", h // 2,
                   f"{'cos' if what == 'adj' else 'sin'} {ang}° = 1/2\n길이 = {h} × 1/2 = {h // 2}", f"{'cos' if what == 'adj' else 'sin'} {ang}°를 이용하세요.")
    return fill(f"빗변이 {h}이고 ∠A = {ang}°인 직각삼각형에서 ∠A의 {'이웃변(밑변)' if what == 'adj' else '대변'}의 길이는 {{{{1}}}}√3", [str(h // 2)],
                f"{'cos' if what == 'adj' else 'sin'} {ang}° = √3/2\n길이 = {h} × √3/2 = {h // 2}√3", f"{'cos' if what == 'adj' else 'sin'} {ang}°를 이용하세요.")

def l03_elev(r):
    d = r.choice([10, 12, 15, 20, 25, 30, 40])
    ang = r.choice([45, 60, 30])
    if ang == 45:
        return num(f"건물에서 {d}m 떨어진 곳에서 건물 꼭대기를 올려본각이 45°입니다. 눈높이를 무시하면 건물의 높이는 몇 m일까요?", d,
                   f"높이 = {d} × tan 45° = {d} × 1 = {d}m", "높이 = 거리 × tan(올려본각)")
    if ang == 60:
        return fill(f"건물에서 {d}m 떨어진 곳에서 건물 꼭대기를 올려본각이 60°입니다. 눈높이를 무시하면 건물의 높이는 {{{{1}}}}√3 m", [str(d)],
                    f"높이 = {d} × tan 60° = {d}√3 m", "높이 = 거리 × tan(올려본각)")
    if d % 3: return None
    return fill(f"건물에서 {d}m 떨어진 곳에서 건물 꼭대기를 올려본각이 30°입니다. 눈높이를 무시하면 건물의 높이는 {{{{1}}}}√3 m", [str(d // 3)],
                f"높이 = {d} × tan 30° = {d} × √3/3 = {d // 3}√3 m", "높이 = 거리 × tan(올려본각), tan 30° = √3/3")

def l03_given(r):
    a, b, c = r.choice(TRIPLES[:4]); k = r.randint(1, 4)
    return num(f"직각삼각형 ABC에서 ∠C = 90°, sin A = {a}/{c}, AB = {c * k}일 때 BC의 길이는?", a * k,
               f"sin A = BC/AB이므로 BC = AB × sin A\n= {c * k} × {a}/{c} = {a * k}", "sin A = (대변)/(빗변)")

def l03_ramp(r):
    b, h = r.choice([(4, 3), (5, 2), (8, 3), (6, 1), (10, 3)])
    k = r.randint(2, 4)
    return num(f"밑변 {b}m, 높이 {h}m인 경사로와 같은 기울기의 경사로를 밑변 {b * k}m로 만들면 높이는 몇 m일까요?", h * k,
               f"같은 각도이면 tan 값(높이/밑변)이 같습니다.\n{h}/{b} = x/{b * k} → x = {h * k}", "tan A = 높이/밑변이 같아야 합니다.")

L03 = [("세 변으로 삼각비", l03_ratio), ("특수각의 삼각비", l03_spec), ("특수각 계산", l03_specsum), ("특수각으로 변의 길이", l03_side),
       ("올려본각", l03_elev), ("삼각비로 변 구하기", l03_given), ("기울기가 같은 경사로", l03_ramp)]

# ---------------- l04 원의 성질 ----------------
def l04_chord(r):
    a, b, c = triple(r, 30)
    return num(f"반지름이 {c}인 원에서 중심까지의 거리가 {a}인 현의 길이는?", 2 * b,
               f"중심에서 현에 내린 수선은 현을 이등분합니다.\n(현의 절반)² = {c}² − {a}² = {c * c} − {a * a} = {b * b} → 절반 = {b}\n현 = 2 × {b} = {2 * b}",
               "반지름, 중심까지의 거리, 현의 절반이 직각삼각형을 이룹니다.")

def l04_cdist(r):
    a, b, c = triple(r, 30)
    return num(f"반지름이 {c}인 원에서 길이가 {2 * b}인 현과 중심 사이의 거리는?", a,
               f"현의 절반은 {b}\n거리² = {c}² − {b}² = {c * c} − {b * b} = {a * a}\n거리 = {a}",
               "현의 절반을 먼저 구하세요.")

def l04_tan(r):
    a, b, c = triple(r, 30)
    return num(f"반지름이 {a}인 원의 중심에서 {c}만큼 떨어진 점 P에서 원에 접선을 그었습니다. 점 P에서 접점까지의 거리는?", b,
               f"접선은 접점에서 반지름과 수직입니다.\n(접선의 길이)² = {c}² − {a}² = {c * c} − {a * a} = {b * b}\n접선의 길이 = {b}",
               "중심, 접점, P가 직각삼각형을 이룹니다.")

def l04_insc(r):
    t = r.choice(["c2i", "i2c"])
    x = r.randint(10, 85)
    if t == "c2i":
        return num(f"한 호에 대한 중심각이 {2 * x}°일 때, 그 호에 대한 원주각은 몇 도일까요?", x,
                   f"원주각은 같은 호에 대한 중심각의 절반입니다.\n{2 * x}° ÷ 2 = {x}°", "원주각 = 중심각 × 1/2")
    return num(f"원주각이 {x}°일 때 같은 호에 대한 중심각은 몇 도일까요?", 2 * x,
               f"중심각은 원주각의 2배입니다.\n{x}° × 2 = {2 * x}°", "중심각 = 원주각 × 2")

def l04_cyc(r):
    x = r.randint(50, 130)
    return num(f"원에 내접하는 사각형 ABCD에서 ∠A = {x}°일 때, ∠C는 몇 도일까요?", 180 - x,
               f"원에 내접하는 사각형의 마주 보는 두 각의 합은 180°입니다.\n∠C = 180° − {x}° = {180 - x}°",
               "마주 보는 각의 합은 180°")

def l04_diam(r):
    x = r.randint(15, 75)
    return num(f"삼각형 ABC의 세 꼭짓점이 원 위에 있고 변 AB가 지름입니다. ∠A = {x}°일 때 ∠B는 몇 도일까요?", 90 - x,
               f"지름에 대한 원주각은 90°이므로 ∠C = 90°\n∠B = 180° − 90° − {x}° = {90 - x}°", "지름에 대한 원주각은 직각입니다.")

def l04_ext(r):
    x = r.randint(40, 150)
    return num(f"원 밖의 점 P에서 원 O에 그은 두 접선의 접점을 A, B라 합니다. ∠AOB = {x}°일 때 ∠APB는 몇 도일까요?", 180 - x,
               f"접선과 반지름은 수직이므로 ∠OAP = ∠OBP = 90°\n사각형 OAPB의 내각의 합 360°에서\n∠APB = 360° − 90° − 90° − {x}° = {180 - x}°",
               "사각형 OAPB에서 두 각이 직각입니다.")

def l04_iso(r):
    x = r.randint(20, 70)
    return num(f"원 O 위의 두 점 A, B에 대해 ∠OAB = {x}°일 때, 중심각 ∠AOB는 몇 도일까요?", 180 - 2 * x,
               f"OA = OB(반지름)이므로 삼각형 OAB는 이등변삼각형: ∠OBA = {x}°\n∠AOB = 180° − {x}° − {x}° = {180 - 2 * x}°",
               "두 반지름으로 만든 삼각형은 이등변삼각형입니다.")

L04 = [("현의 길이", l04_chord), ("현과 중심 사이의 거리", l04_cdist), ("접선의 길이", l04_tan), ("원주각과 중심각", l04_insc),
       ("내접사각형", l04_cyc), ("지름과 원주각", l04_diam), ("두 접선이 이루는 각", l04_ext), ("반지름과 이등변삼각형", l04_iso)]

if __name__ == "__main__":
    tot = 0
    for l, T in [("l01", L01), ("l02", L02), ("l03", L03), ("l04", L04)]:
        n = write("c0", "ch05", l, T, per=6); tot += n; print(l, n)
    print("total", tot)
