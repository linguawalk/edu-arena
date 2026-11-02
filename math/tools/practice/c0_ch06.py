"""코스 0 · 챕터 6 자료의 정리 — 연습 문제 은행"""
from core import *
from statistics import median

def g(x): return f"{float(x):g}"

# ---------------- l01 대푯값 ----------------
def l01_mean(r):
    n = r.randint(4, 7); mu = r.randint(4, 20)
    xs = [mu + r.randint(-5, 5) for _ in range(n - 1)]
    last = mu * n - sum(xs)
    if last < 0: return None
    xs.append(last); r.shuffle(xs)
    return num(f"자료 {', '.join(map(str, xs))}의 평균은?", mu,
               f"평균 = (변량의 총합) ÷ (변량의 개수)\n총합 = {' + '.join(map(str, xs))} = {sum(xs)}\n{sum(xs)} ÷ {n} = {mu}",
               "모두 더한 뒤 개수로 나누세요.")

def l01_median(r):
    n = r.choice([5, 6, 7, 8]); xs = r.sample(range(1, 40), n)
    s = sorted(xs); md = F(sum(s[n // 2 - 1:n // 2 + 1]), 2) if n % 2 == 0 else F(s[n // 2])
    expl = f"크기 순으로 나열: {', '.join(map(str, s))}\n"
    expl += (f"개수가 {n}(홀수)이므로 가운데 {n // 2 + 1}번째 값 {s[n // 2]}" if n % 2 else
             f"개수가 {n}(짝수)이므로 가운데 두 값 {j(s[n // 2 - 1], '와과')} {s[n // 2]}의 평균: ({s[n // 2 - 1]} + {s[n // 2]}) ÷ 2 = {g(md)}")
    return num(f"자료 {', '.join(map(str, xs))}의 중앙값은?", g(md), expl,
               "먼저 크기 순으로 나열하세요. 개수가 짝수면 가운데 두 값의 평균입니다.", fmt="integer" if md.denominator == 1 else "decimal")

def l01_mode(r):
    vals = r.sample(range(1, 15), 4); mo = vals[0]
    xs = [mo] * 3 + [vals[1]] * 2 + [vals[2], vals[3]]
    r.shuffle(xs)
    return num(f"자료 {', '.join(map(str, xs))}의 최빈값은?", mo,
               f"각 값이 나온 횟수: " + ", ".join(f"{v}({xs.count(v)}번)" for v in sorted(set(xs))) + f"\n가장 많이 나온 값은 {mo}",
               "가장 많이 나타나는 값을 찾으세요.")

def l01_missing(r):
    n = r.choice([4, 5]); mu = r.randint(5, 15)
    xs = [mu + r.randint(-4, 4) for _ in range(n - 1)]
    a = mu * n - sum(xs)
    if a <= 0: return None
    return num(f"자료 a, {', '.join(map(str, xs))}의 평균이 {mu}일 때 a의 값은?", a,
               f"총합 = 평균 × 개수 = {mu} × {n} = {mu * n}\na + {sum(xs)} = {mu * n}\na = {a}",
               "평균 × 개수 = 총합")

def l01_need(r):
    k = r.choice([3, 4, 5]); m0 = r.randint(70, 85); target = m0 + r.randint(1, 4)
    need = target * (k + 1) - m0 * k
    if need > 100: return None
    return num(f"{k}번의 시험 평균이 {m0}점입니다. 다음 시험에서 몇 점을 받아야 {k + 1}번의 평균이 {target}점이 될까요?", need,
               f"지금까지 총점: {m0} × {k} = {m0 * k}\n목표 총점: {target} × {k + 1} = {target * (k + 1)}\n필요한 점수: {target * (k + 1)} − {m0 * k} = {need}",
               "평균 × 횟수로 총점을 구해 비교하세요.")

def l01_outlier(r):
    base = sorted(r.sample(range(180, 260, 5), 4)); big = r.choice([900, 1000, 1200, 1500])
    xs = base + [big]
    mean = F(sum(xs), 5)
    if mean.denominator != 1: return None
    ask = r.choice(["평균", "중앙값"])
    v = int(mean) if ask == "평균" else base[2]
    return num(f"다섯 명의 월급이 {', '.join(map(str, xs))}(만 원)입니다. {ask}은 몇 만 원일까요?".replace("평균은", "평균은").replace("중앙값은", "중앙값은"), v,
               (f"총합 {sum(xs)} ÷ 5 = {int(mean)}" if ask == "평균" else f"크기 순으로 세 번째 값: {base[2]}") +
               f"\n(평균 {int(mean)}은 큰 값 {big} 때문에 끌려 올라갑니다. 이런 자료는 중앙값({base[2]})이 더 잘 대표합니다.)",
               "극단값이 있으면 평균과 중앙값이 크게 달라집니다.")

def l01_shoe(r):
    sizes = [230, 240, 250, 260, 270]
    cnt = r.sample(range(1, 10), 5)
    mo = sizes[cnt.index(max(cnt))]
    desc = ", ".join(f"{s}mm {c}켤레" for s, c in zip(sizes, cnt))
    return num(f"하루 동안 팔린 운동화가 {desc}입니다. 최빈값은 몇 mm일까요?", mo,
               f"가장 많이 팔린 치수를 찾습니다: {max(cnt)}켤레 → {mo}mm\n최빈값은 개수가 아니라 그 값(치수)입니다.",
               "가장 많이 팔린 '치수'가 답입니다.")

L01 = [("평균", l01_mean), ("중앙값", l01_median), ("최빈값", l01_mode), ("평균에서 변량 구하기", l01_missing),
       ("목표 평균", l01_need), ("극단값과 대푯값", l01_outlier), ("도수로 최빈값", l01_shoe)]

# ---------------- l02 산포도 ----------------
def l02_dev(r):
    mu, x = r.randint(5, 80), r.randint(-9, 9)
    return fill(f"평균이 {mu}인 자료에서 변량 {mu + x}의 편차는 {{{{1}}}}", [ans(x)],
                f"편차 = 변량 − 평균\n{mu + x} − {mu} = {m(x)}", "편차 = 변량 − 평균 (음수일 수 있음)")

def l02_lastdev(r):
    ds = [r.randint(-5, 5) for _ in range(r.randint(3, 4))]
    x = -sum(ds)
    return num(f"어떤 자료의 편차가 {', '.join(m(d) for d in ds)}, x일 때 x의 값은?", x,
               f"편차의 합은 항상 0입니다.\n{' + '.join(par(d) for d in ds)} + x = 0\n{m(sum(ds))} + x = 0 → x = {m(x)}",
               "편차를 모두 더하면 0입니다.")

def l02_var(r):
    n = r.choice([4, 5]); mu = r.randint(3, 12)
    while True:
        ds = [r.randint(-4, 4) for _ in range(n - 1)]; ds.append(-sum(ds))
        if abs(ds[-1]) <= 6 and any(ds): break
    xs = [mu + d for d in ds]
    v = F(sum(d * d for d in ds), n)
    return num(f"자료 {', '.join(map(str, xs))}의 분산은?", g(v),
               f"평균 = {sum(xs)} ÷ {n} = {mu}\n편차: {', '.join(m(d) for d in ds)}\n편차의 제곱의 합: {' + '.join(str(d * d) for d in ds)} = {sum(d * d for d in ds)}\n분산 = {sum(d * d for d in ds)} ÷ {n} = {g(v)}",
               "평균 → 편차 → 편차의 제곱의 평균 순서로 구하세요.", fmt="integer" if v.denominator == 1 else "decimal")

def l02_vdev(r):
    n = r.choice([4, 5])
    ds = [r.randint(-4, 4) for _ in range(n - 1)]; ds.append(-sum(ds))
    if not any(ds) or abs(ds[-1]) > 6: return None
    r.shuffle(ds)
    v = F(sum(d * d for d in ds), n)
    return num(f"어떤 자료의 편차가 {', '.join(m(d) for d in ds)}일 때 분산은?", g(v),
               f"분산 = (편차의 제곱의 합) ÷ (개수)\n= ({' + '.join(str(d * d) for d in ds)}) ÷ {n} = {sum(d * d for d in ds)} ÷ {n} = {g(v)}",
               "편차를 제곱해서 평균을 내세요.", fmt="integer" if v.denominator == 1 else "decimal")

def l02_sd(r):
    s = r.randint(2, 12)
    return num(f"분산이 {s * s}인 자료의 표준편차는?", s,
               f"표준편차 = √(분산) = √{s * s} = {s}", "표준편차는 분산의 양의 제곱근입니다.")

def l02_trans(r):
    t = r.choice(["add_var", "mul_sd", "add_sd", "mul_var"])
    v, c = r.randint(2, 9), r.randint(2, 5)
    if t == "add_var":
        return num(f"분산이 {v}인 자료의 모든 변량에 {c * 3}을 더하면 분산은?", v,
                   f"모든 변량에 같은 수를 더하면 평균도 그만큼 커지고 편차는 그대로입니다.\n따라서 분산은 {v} 그대로", "흩어진 정도는 변하지 않습니다.")
    if t == "add_sd":
        return num(f"표준편차가 {v}인 자료의 모든 변량에서 {c}를 빼면 표준편차는?", v,
                   f"모든 변량을 같은 만큼 옮기면 편차는 변하지 않습니다.\n따라서 표준편차는 {v} 그대로", "모두 똑같이 옮기면 퍼진 정도는 그대로입니다.")
    if t == "mul_sd":
        return num(f"표준편차가 {v}인 자료의 모든 변량을 {c}배 하면 표준편차는?", v * c,
                   f"변량을 {c}배 하면 편차도 {c}배가 됩니다.\n표준편차 = {v} × {c} = {v * c}", "편차가 몇 배가 되는지 생각하세요.")
    return num(f"분산이 {v}인 자료의 모든 변량을 {c}배 하면 분산은?", v * c * c,
               f"변량을 {c}배 하면 편차도 {c}배, 편차의 제곱은 {c}² = {c * c}배\n분산 = {v} × {c * c} = {v * c * c}", "분산은 편차의 '제곱'의 평균입니다.")

def l02_cmp(r):
    a, b = r.sample(range(2, 12), 2)
    cls = r.choice([("A", "B"), ("1", "2"), ("가", "나")])
    better = cls[0] if a < b else cls[1]
    return fill(f"두 반의 수학 평균이 같고 표준편차가 {cls[0]}반 {a}점, {cls[1]}반 {b}점입니다. 성적이 더 고른 반은 {{{{1}}}}반입니다.", [[better, better + "반"]],
                f"표준편차가 작을수록 변량이 평균 주위에 모여 있어 고릅니다.\n{min(a, b)} < {max(a, b)}이므로 {better}반",
                "표준편차가 작은 쪽이 더 고릅니다.")

L02 = [("편차", l02_dev), ("편차의 합", l02_lastdev), ("분산 구하기", l02_var), ("편차로 분산", l02_vdev),
       ("표준편차", l02_sd), ("변량을 바꾸면", l02_trans), ("산포도 비교", l02_cmp)]

# ---------------- l03 도수분포와 그래프 ----------------
def l03_count(r):
    xs = sorted(r.sample(range(10, 45), 9)); lo = r.choice([10, 20, 30]); hi = lo + 10
    c = [x for x in xs if lo <= x < hi]
    return num(f"기록 {', '.join(map(str, xs))} 중 {lo} 이상 {hi} 미만인 것은 몇 개일까요?", len(c),
               f"{lo} ≤ x < {hi}인 값: {', '.join(map(str, c)) if c else '없음'}\n({j(hi, '는은')} '미만'이라 포함하지 않습니다.)\n따라서 {len(c)}개",
               "'이상'은 포함, '미만'은 포함하지 않습니다.")

def l03_mark(r):
    w = r.choice([2, 4, 5, 10, 20]); lo = w * r.randint(1, 10)
    if r.random() < .5:
        return num(f"계급이 {lo} 이상 {lo + w} 미만일 때 계급값은?", g(F(2 * lo + w, 2)),
                   f"계급값 = (양 끝 값의 합) ÷ 2 = ({lo} + {lo + w}) ÷ 2 = {g(F(2 * lo + w, 2))}", "계급의 가운데 값입니다.",
                   fmt="integer" if (2 * lo + w) % 2 == 0 else "decimal")
    return num(f"계급이 {lo} 이상 {lo + w} 미만일 때 계급의 크기는?", w,
               f"계급의 크기 = {lo + w} − {lo} = {w}", "계급의 양 끝 값의 차입니다.")

def l03_rel(r):
    N = r.choice([20, 25, 40, 50]); f = r.randint(1, N // 3)
    v = F(f, N)
    if (v * 100).denominator != 1: return None
    return num(f"총도수가 {N}인 자료에서 도수가 {f}인 계급의 상대도수는?", g(v),
               f"상대도수 = (계급의 도수) ÷ (총도수) = {f} ÷ {N} = {g(v)}", "도수를 전체로 나누세요.", fmt="decimal")

def l03_freq(r):
    N = r.choice([20, 40, 50, 80, 200]); rv = r.choice([0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4])
    f = N * rv
    if abs(f - round(f)) > 1e-9: return None
    return num(f"총 {N}명인 자료에서 어떤 계급의 상대도수가 {rv:g}이면 그 계급의 도수는 몇 명일까요?", round(f),
               f"도수 = 총도수 × 상대도수 = {N} × {rv:g} = {round(f)}명", "상대도수 = 도수 ÷ 총도수를 거꾸로 쓰세요.")

def table(r):
    w = r.choice([5, 10]); fs_ = [r.randint(1, 9) for _ in range(4)]
    rows = [(i * w, (i + 1) * w, f) for i, f in enumerate(fs_)]
    desc = ", ".join(f"{a} 이상 {b} 미만 {f}명" for a, b, f in rows)
    return w, rows, desc

def l03_total(r):
    w, rows, desc = table(r)
    k = r.randint(1, 3); below = rows[k][0]
    v = sum(f for a, b, f in rows if b <= below)
    return num(f"통학 시간(분) 도수분포표가 {desc}입니다. 통학 시간이 {below}분 미만인 학생은 몇 명일까요?", v,
               f"{below}분 미만은 앞의 {k}개 계급입니다.\n" + " + ".join(str(f) for a, b, f in rows[:k]) + f" = {v}명",
               "해당 계급들의 도수를 모두 더하세요.")

def l03_avg(r):
    w, rows, desc = table(r)
    N = sum(f for *_, f in rows); S = sum(F(a + b, 2) * f for a, b, f in rows)
    v = S / N
    if (v * 100).denominator != 1: return None
    return num(f"통학 시간(분) 도수분포표가 {desc}입니다. (계급값 × 도수)의 합으로 평균을 어림하면 몇 분일까요?", g(v),
               "계급값: " + ", ".join(g(F(a + b, 2)) for a, b, _ in rows) + "\n(계급값 × 도수)의 합: " + " + ".join(f"{g(F(a + b, 2))}×{f}" for a, b, f in rows) +
               f" = {g(S)}\n총도수 {N}\n평균 ≈ {g(S)} ÷ {N} = {g(v)}",
               "각 계급의 계급값을 그 계급 학생들의 대표값으로 씁니다.", fmt="integer" if v.denominator == 1 else "decimal")

def l03_kth(r):
    w, rows, desc = table(r)
    N = sum(f for *_, f in rows); k = r.randint(1, N)
    acc = 0
    for a, b, f in rows:
        acc += f
        if acc >= k: break
    return num(f"통학 시간(분) 도수분포표가 {desc}입니다. 통학 시간이 짧은 쪽부터 {k}번째인 학생이 속한 계급의 계급값은?", g(F(a + b, 2)),
               "누적 도수를 구합니다: " + ", ".join(f"{b}분 미만 {sum(f2 for a2, b2, f2 in rows if b2 <= b)}명" for a, b, f in rows) +
               f"\n{k}번째 학생은 {a} 이상 {b} 미만 계급에 속합니다.\n계급값 = ({a} + {b}) ÷ 2 = {g(F(a + b, 2))}",
               "도수를 앞에서부터 누적해 보세요.", fmt="integer" if (a + b) % 2 == 0 else "decimal")

def l03_cmp(r):
    na, nb = r.choice([(30, 20), (25, 40), (20, 25), (40, 50), (30, 25)])
    fa, fb = r.randint(2, na // 3), r.randint(2, nb // 3)
    ra, rb = F(fa, na), F(fb, nb)
    if ra == rb: return None
    better = "A" if ra > rb else "B"
    return fill(f"A반 {na}명 중 {fa}명, B반 {nb}명 중 {fb}명이 90점 이상입니다. 90점 이상 학생의 비율이 더 높은 반은 {{{{1}}}}반입니다.", [[better, better + "반"]],
                f"인원이 다르므로 상대도수로 비교합니다.\nA반: {fa} ÷ {na} = {float(ra):.3g}\nB반: {fb} ÷ {nb} = {float(rb):.3g}\n따라서 {better}반",
                "전체 인원이 다르면 비율(상대도수)로 비교해야 합니다.")

L03 = [("계급에 속한 자료 세기", l03_count), ("계급값과 계급의 크기", l03_mark), ("상대도수", l03_rel), ("상대도수로 도수", l03_freq),
       ("~ 미만인 도수", l03_total), ("도수분포표의 평균", l03_avg), ("몇 번째 학생의 계급", l03_kth), ("상대도수 비교", l03_cmp)]

# ---------------- l04 상관관계 ----------------
POS = ["키가 클수록 발 크기가 대체로 크다", "공부 시간이 길수록 시험 점수가 대체로 높다", "기온이 높을수록 아이스크림 판매량이 대체로 많다",
       "자동차 속력이 빠를수록 정지 거리가 대체로 길다", "운동 시간이 길수록 소모 열량이 대체로 많다", "가족 수가 많을수록 한 달 식비가 대체로 많다",
       "몸무게가 무거울수록 키가 대체로 크다", "나무의 나이가 많을수록 둘레가 대체로 굵다"]
NEG = ["게임 시간이 길수록 성적이 대체로 낮다", "겨울철 기온이 낮을수록 난방비가 대체로 많다", "산의 높이가 높을수록 기온이 대체로 낮다",
       "자동차 나이가 많을수록 중고 가격이 대체로 낮다", "결석 횟수가 많을수록 성적이 대체로 낮다", "물건 값이 비쌀수록 판매량이 대체로 적다",
       "스마트폰 사용 시간이 길수록 수면 시간이 대체로 짧다", "운동량이 많을수록 체지방률이 대체로 낮다"]
NONE = ["키와 수학 점수", "생일(월)과 몸무게", "신발 끈 색깔과 달리기 기록", "이름의 글자 수와 키", "출석 번호와 영어 점수", "혈액형과 시력"]

def l04_pos(r):
    s = r.choice(POS + NEG)
    v = "양" if s in POS else "음"
    return fill(f"{s}면 두 변량 사이에는 {{{{1}}}}의 상관관계가 있습니다.", [[v, v + "의"]],
                ("한 변량이 커질 때 다른 변량도 대체로 커지면 양의 상관관계" if v == "양" else "한 변량이 커질 때 다른 변량은 대체로 작아지면 음의 상관관계") +
                f"\n따라서 {v}의 상관관계", "한쪽이 커질 때 다른 쪽이 커지는지 작아지는지 보세요.")

def l04_none(r):
    s = r.choice(NONE)
    return fill(f"{s} 사이에는 상관관계가 {{{{1}}}}.", [["없다", "없습니다"]],
                f"{s}의 경우 한쪽이 변할 때 다른 쪽이 일정한 경향으로 변하지 않습니다.\n따라서 상관관계가 없다",
                "한쪽이 커질 때 다른 쪽에 일정한 경향이 있는지 생각하세요.")

def l04_trend(r):
    a, b = r.choice([2, 3, 5, -2, -3, 10, -5]), r.randint(20, 60)
    xs = [1, 2, 3] if abs(a) < 10 else [2, 4, 6]
    step = xs[1] - xs[0]
    pts = ", ".join(f"({x}, {a * x + b})" for x in xs)
    nx = xs[-1] + step * r.randint(1, 3)
    return num(f"자료 {pts}가 같은 경향을 이어 간다고 할 때, x = {nx}에 해당하는 y의 값은?", a * nx + b,
               f"x가 {step} 늘 때 y는 {m(a * step)}씩 변합니다.\nx = {xs[-1]}에서 {nx}까지 {(nx - xs[-1]) // step}번 더 변하므로\ny = {a * xs[-1] + b} {'+' if a > 0 else '−'} {abs(a * step)} × {(nx - xs[-1]) // step} = {a * nx + b}",
               "x가 일정하게 늘 때 y가 얼마씩 변하는지 찾으세요.")

def l04_count(r):
    n = 6; pts = [(r.choice(range(40, 101, 5)), r.choice(range(40, 101, 5))) for _ in range(n)]
    if len(set(pts)) < n: return None
    t = r.choice(["gt", "both"])
    if t == "gt":
        c = [p for p in pts if p[1] > p[0]]
        return num(f"학생 6명의 (국어, 영어) 점수가 {', '.join(map(str, pts))}입니다. 영어 점수가 국어 점수보다 높은 학생은 몇 명일까요?", len(c),
                   f"(국어, 영어)에서 둘째 값이 더 큰 것: {', '.join(map(str, c)) if c else '없음'}\n따라서 {len(c)}명\n(산점도에서는 직선 y = x의 위쪽에 있는 점들입니다.)",
                   "두 점수를 하나씩 비교하세요.")
    k = r.choice([70, 75, 80])
    c = [p for p in pts if p[0] >= k and p[1] >= k]
    return num(f"학생 6명의 (국어, 영어) 점수가 {', '.join(map(str, pts))}입니다. 두 과목 모두 {k}점 이상인 학생은 몇 명일까요?", len(c),
               f"두 값이 모두 {k} 이상인 것: {', '.join(map(str, c)) if c else '없음'}\n따라서 {len(c)}명",
               "두 조건을 모두 만족해야 합니다.")

CAUSE = [("아이스크림 판매량과 물놀이 사고 수", "기온(더운 날씨)"), ("소방차 출동 수와 화재 피해액", "화재의 규모"),
         ("우산 판매량과 교통사고 수", "비(강수량)"), ("어린이의 손 크기와 어휘력", "나이"), ("난방비와 감기 환자 수", "추운 날씨"),
         ("수영장 이용객 수와 에어컨 판매량", "기온(더운 날씨)"), ("핫팩 판매량과 빙판길 낙상 사고 수", "추운 날씨")]
def l04_cause(r):
    a, c = r.choice(CAUSE)
    kw = c.split("(")[0]
    return fill(f"{a}: 두 변량이 함께 늘어나는 공통 원인으로 가장 알맞은 것은 {{{{1}}}}입니다.", [[c, kw] + ([c.split("(")[1].rstrip(")")] if "(" in c else [])],
                f"두 변량이 함께 변해도 한쪽이 다른 쪽의 원인이라고 단정할 수 없습니다.\n둘 다 '{c}'의 영향을 받아 함께 변하는 것입니다.",
                "두 가지에 모두 영향을 주는 제3의 요인을 생각하세요.")

L04 = [("양·음의 상관관계", l04_pos), ("상관관계가 없는 경우", l04_none), ("경향으로 예측", l04_trend), ("산점도 자료 세기", l04_count), ("공통 원인", l04_cause)]

if __name__ == "__main__":
    tot = 0
    for l, T in [("l01", L01), ("l02", L02), ("l03", L03), ("l04", L04)]:
        n = write("c0", "ch06", l, T, per=6); tot += n; print(l, n)
    print("total", tot)
