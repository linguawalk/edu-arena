"""코스 2(금융생활) 빌더 공통: 규정값, 계산 도우미, 복습 출처 태그와 챕터 기록."""
import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from sk import ex, eg, num, fb, order, wr, write_chapter
from rules import rv, won
from c1common import graph, line, market, BLUE, RED, GREEN


def pct(x):
    """4.75 -> '4.75%', 9.5 -> '9.5%', 20 -> '20%'"""
    s = f"{x:.3f}".rstrip("0").rstrip(".")
    return s + "%"


def manwon(v):
    """100000000 -> '1억 원', 50000000 -> '5,000만 원'"""
    if v % 100000000 == 0: return f"{v // 100000000:,}억 원"
    if v % 10000 == 0: return f"{v // 10000:,}만 원"
    return won(v)


def floor_won(x):
    return int(math.floor(x + 1e-9))


def run(no, title, lessons, review, srcs):
    assert len(review) == len(srcs)
    for q, s in zip(review, srcs):
        q["source_lesson"] = f"c2-ch{no:02d}-l{s:02d}"
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "content")
    write_chapter(root, 2, "금융생활", no, title, lessons, review, curriculum="2022-high")
