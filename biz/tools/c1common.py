"""코스 1(경제) 빌더 공통: 그래프 도우미, 복습 출처 태그와 챕터 기록."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from sk import ex, eg, num, fb, order, wr, write_chapter
from rules import rv, won


def graph(xl, yl, xr, yr, curves, points=None, xs=1, ys=1):
    return {"widget": "graph", "static": True, "config": {
        "xlabel": xl, "ylabel": yl, "xmin": xr[0], "xmax": xr[1], "ymin": yr[0], "ymax": yr[1],
        "xstep": xs, "ystep": ys, "curves": curves, "points": points or []}}


def line(c0, c1, a, b, label=None, color=None, **kw):
    """y = c0 + c1·x 를 x∈[a, b]에서 그린다. label은 오른쪽 끝에 붙는다."""
    d = {"kind": "poly", "coef": [c0, c1], "from": a, "to": b}
    if label: d["label"] = label
    if color: d["color"] = color
    d.update(kw)
    return d


def vline(x): return {"kind": "vline", "x": x}
def hline(y): return {"kind": "hline", "y": y}


BLUE, RED, GREEN = "#1D3FA8", "#C2410C", "#1E7A50"


def market(curves, points=None, q=(0, 10), p=(0, 10), qs=1, ps=1, xl="수량", yl="가격"):
    """수요·공급 그래프(가로축 수량, 세로축 가격)."""
    return graph(xl, yl, q, p, curves, points, qs, ps)


def run(no, title, lessons, review, srcs):
    assert len(review) == len(srcs)
    for q, s in zip(review, srcs):
        q["source_lesson"] = f"c1-ch{no:02d}-l{s:02d}"
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "content")
    write_chapter(root, 1, "경제", no, title, lessons, review, curriculum="2022-high")
