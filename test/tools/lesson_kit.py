"""레슨 작성 도우미. 각 함수는 math-arena 레슨 스키마 v1.0의 화면 하나를 만든다.

test-arena 전용 추가 형식
- proof: 자가 채점 증명 문항
  prompt, model_answer(모범 증명 단계 배열), criteria([{text, points}]), hint, explanation(선택)
- code: 설명·예제·문항 화면에 붙는 선택 필드. 고정폭 코드 블록으로 표시 (C 함수로 붙임)
"""


def X(title, body, stage="discover", figure=None):
    s = {"type": "explain", "stage": stage, "title": title, "body": body}
    if figure:
        s["figure"] = figure
    return s


def E(problem, steps, answer, stage="discover", title="예제"):
    return {"type": "example", "stage": stage, "title": title, "problem": problem, "steps": steps, "answer": answer}


def N(prompt, answer, hint, expl, stage="discover", fmt="integer", tol=0):
    """fmt: integer / fraction / decimal. tol: 허용 오차(소수 답에서 반올림 차이를 받아 줄 때)."""
    return {"type": "question", "stage": stage, "qtype": "numeric", "prompt": prompt, "answer": str(answer),
            "answer_format": fmt, "tolerance": tol, "hint": hint, "explanation": expl}


def F(prompt, blanks, hint, expl, stage="discover", unordered=None):
    s = {"type": "question", "stage": stage, "qtype": "fill_blank", "prompt": prompt,
         "blanks": [{"answers": a} for a in blanks], "hint": hint, "explanation": expl}
    if unordered:
        s["unordered_groups"] = unordered
    return s


def O(prompt, steps, shown, hint, expl, stage="discover"):
    """steps: 올바른 순서의 문장들, shown: 화면에 보여 줄 순서(steps의 0부터 시작하는 번호 목록)."""
    items = [{"id": f"o{k + 1}", "text": t} for k, t in enumerate(steps)]
    return {"type": "question", "stage": stage, "qtype": "ordering", "prompt": prompt,
            "items": [items[k] for k in shown], "answer_order": [it["id"] for it in items],
            "hint": hint, "explanation": expl}


def PR(prompt, model, criteria, hint, stage="apply", expl=None):
    s = {"type": "question", "stage": stage, "qtype": "proof", "prompt": prompt, "model_answer": model,
         "criteria": [{"text": t, "points": p} for t, p in criteria], "hint": hint}
    if expl:
        s["explanation"] = expl
    return s


def C(screen, code):
    """화면(설명·예제·문항)에 코드 블록을 붙인다. 코드는 고정폭 글꼴로 줄바꿈 그대로 표시된다."""
    s = dict(screen)
    s["code"] = code.strip("\n")
    return s


# ---------------------------------------------------------------- 도형 그림 (geo 위젯)
def G(alt, *els, maxh=240):
    """도형 그림. 좌표는 수학 좌표(위쪽이 +y)."""
    return {"widget": "geo", "config": {"elements": [e for e in els if e], "alt": alt, "maxh": maxh}, "static": True}


def pt(p, label=None, pos=None, hide=False):
    e = {"t": "pt", "p": [round(p[0], 4), round(p[1], 4)]}
    if label: e["label"] = label
    if pos: e["pos"] = pos
    if hide: e["hide"] = True
    return e


def seg(a, b, dash=False, hl=False):
    e = {"t": "seg", "a": [round(a[0], 4), round(a[1], 4)], "b": [round(b[0], 4), round(b[1], 4)]}
    if dash: e["dash"] = True
    if hl: e["hl"] = True
    return e


def poly(pts, fill=True, hl=False, dash=False):
    e = {"t": "poly", "pts": [[round(x, 4), round(y, 4)] for x, y in pts]}
    if not fill: e["fill"] = False
    if hl: e["hl"] = True
    if dash: e["dash"] = True
    return e


def circ(c, r, dash=False):
    e = {"t": "circle", "c": [round(c[0], 4), round(c[1], 4)], "r": round(r, 4)}
    if dash: e["dash"] = True
    return e


def rt(p, a, b):
    return {"t": "right", "p": list(p), "a": list(a), "b": list(b)}


def ang(p, a, b, label=None, r=22):
    e = {"t": "arc", "p": list(p), "a": list(a), "b": list(b), "r": r}
    if label: e["label"] = label
    return e


def tx(p, s, hl=False):
    e = {"t": "text", "p": [round(p[0], 4), round(p[1], 4)], "s": s}
    if hl: e["hl"] = True
    return e


def vec(a, b, label=None, hl=False, dash=False):
    """화살표(힘·속도 같은 벡터). label은 화살촉 바로 앞에 쓴다."""
    e = {"t": "vec", "a": [round(a[0], 4), round(a[1], 4)], "b": [round(b[0], 4), round(b[1], 4)]}
    if label: e["label"] = label
    if hl: e["hl"] = True
    if dash: e["dash"] = True
    return e


def zigzag(a, b, n=6, w=0.18, lead=0.2):
    """a에서 b까지 지그재그(용수철·저항)를 seg 목록으로 만든다. G(...)에 *zigzag(...)로 넣는다."""
    import math
    dx, dy = b[0] - a[0], b[1] - a[1]
    L = math.hypot(dx, dy); ux, uy = dx / L, dy / L; nx, ny = -uy, ux
    p0 = (a[0] + ux * L * lead, a[1] + uy * L * lead); p1 = (b[0] - ux * L * lead, b[1] - uy * L * lead)
    pts = [a, p0]
    for k in range(1, 2 * n):
        t = k / (2 * n); sgn = 1 if k % 2 else -1
        pts.append((p0[0] + (p1[0] - p0[0]) * t + nx * w * sgn, p0[1] + (p1[1] - p0[1]) * t + ny * w * sgn))
    pts += [p1, b]
    return [seg(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]


def GR(alt, xmin, xmax, ymin, ymax, curves, xstep=1, ystep=1, xlabel="t", ylabel="v", points=None):
    """그래프 그림(좌표평면). curves 예: {"kind": "pw", "pts": [[0,0],[2,4]]}, {"kind": "poly", "coef": [0,0,1]},
    {"kind": "shade", "curve": {...}, "from": 0, "to": 2}."""
    c = {"xmin": xmin, "xmax": xmax, "ymin": ymin, "ymax": ymax, "xstep": xstep, "ystep": ystep,
         "xlabel": xlabel, "ylabel": ylabel, "curves": curves, "alt": alt}
    if points: c["points"] = points
    return {"widget": "graph", "config": c, "static": True}


def pw(*pts, color=None, label=None, at=None):
    """꺾은선. label을 주면 그래프 좌표 at=(x, y)에 곡선과 같은 색으로 이름을 쓴다."""
    c = {"kind": "pw", "pts": [list(p) for p in pts]}
    if color: c["color"] = color
    if label: c["label"] = label; c["at"] = list(at)
    return c


def path(*pts, closed=False, color=None, label=None, at=None):
    """좌표 순서대로 잇는 꺾은선(x가 되돌아가도 됨). 순환 과정처럼 닫힌 곡선은 closed=True."""
    c = {"kind": "path", "pts": [[round(x, 4), round(y, 4)] for x, y in pts]}
    if closed: c["closed"] = True
    if color: c["color"] = color
    if label: c["label"] = label; c["at"] = list(at)
    return c


def arrow(a, b, color=None, label=None):
    """그래프 좌표의 짧은 화살표(순환 방향 표시 등)."""
    c = {"kind": "arrow", "x1": a[0], "y1": a[1], "x2": b[0], "y2": b[1]}
    if color: c["color"] = color
    if label: c["label"] = label
    return c


def with_fig(screen, fig):
    screen["figure"] = fig
    return screen


# 계산 도우미
def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def mid(a, b):
    return lerp(a, b, 0.5)


def on_circle(c, r, deg):
    import math
    return (c[0] + r * math.cos(math.radians(deg)), c[1] + r * math.sin(math.radians(deg)))


def GF(alt, P, edges, directed=False, weights=None, hl=(), r=0.17, maxh=220):
    """그래프 그림. P = {정점: (x, y)}, edges = [(u, v), ...].
    정점은 번호가 든 작은 원, 간선은 선(방향 그래프는 화살표). weights = {(u, v): w}이면 간선 가운데에 가중치를 쓴다.
    hl에 든 간선은 강조한다."""
    import math
    els = []
    for (u, v) in edges:
        (x1, y1), (x2, y2) = P[u], P[v]
        L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
        a = (x1 + ux * r, y1 + uy * r); b = (x2 - ux * r, y2 - uy * r)
        h = (u, v) in hl or (v, u) in hl
        els.append(vec(a, b, hl=h) if directed else seg(a, b, hl=h))
        if weights and ((u, v) in weights or (v, u) in weights):
            w = weights.get((u, v), weights.get((v, u)))
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            els.append(tx((mx - uy * 0.2, my + ux * 0.2), str(w), hl=h))
    for k, (x, y) in P.items():
        els.append(circ((x, y), r))
        els.append(tx((x, y), str(k)))
    return G(alt, *els, maxh=maxh)
