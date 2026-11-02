"""코스 6(세무 일반) 빌더 공통: 세율표 계산 도우미, 계정, 챕터 기록."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from sk import ex, eg, num, fb, order, wr, write_chapter
from rules import rv, won
from c5common import jr
from c2common import pct


def bracket_tax(base, key):
    """누진세율표로 세액 계산(원 미만 버림)."""
    tax, lo = 0, 0
    for hi, rate in rv(key):
        top = base if hi is None else min(base, hi)
        if top > lo: tax += (top - lo) * rate / 100
        if hi is None or base <= hi: break
        lo = hi
    return int(tax + 1e-9)


def prog_deduction(key):
    """누진공제액 목록 [(상한, 세율, 누진공제)]."""
    out, ded, prev_rate, lo = [], 0, 0, 0
    for hi, rate in rv(key):
        ded += lo * (rate - prev_rate) / 100
        out.append((hi, rate, int(ded))); prev_rate = rate; lo = hi or lo
    return out


def earned_deduction(total):
    lo = 0
    for hi, base, rate in rv("earned_income_deduction"):
        if hi is None or total <= hi:
            return int(min(base + (total - lo) * rate / 100, 20000000) + 1e-9)
        lo = hi


def man(v):
    if v % 10000: return f"{v:,}원"
    eok, m = divmod(v // 10000, 10000)
    if eok and m: return f"{eok:,}억 {m:,}만 원"
    if eok: return f"{eok:,}억 원"
    return f"{m:,}만 원"


def run(no, title, lessons, review, srcs):
    assert len(review) == len(srcs)
    for q, s in zip(review, srcs):
        q["source_lesson"] = f"c6-ch{no:02d}-l{s:02d}"
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "content")
    write_chapter(root, 6, "세무 일반", no, title, lessons, review, curriculum="2022-voc")
