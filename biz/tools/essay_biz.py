"""경제와 경영 레벨1 코스 에세이용 짧은 작성 도구 (분량 400~700자, 3문단)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
from essay_kit import essay, chk, src, write_essays  # noqa: F401

LEN = (400, 700)


def E(prompt, conds, checks, outline, answer, sources=()):
    conds = list(conds) + [f"{LEN[0]}~{LEN[1]}자, 3문단 이상"]
    return essay(prompt, conds, checks, outline, answer, sources=sources, length=LEN, paragraphs=3)


def run(course, ch, lessons):
    import json
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    with open(os.path.join(root, "content", "level1", course, f"ch{ch:02d}", "chapter.json"), encoding="utf-8") as f:
        n = len(json.load(f)["lessons"])
    assert len(lessons) == n, f"{course} ch{ch}: 레슨 {n}개인데 에세이 묶음 {len(lessons)}개"
    bad = []
    for no, es in enumerate(lessons, 1):
        try:
            print(write_essays("biz", course, ch, no, es))
        except AssertionError as e:
            bad.append(str(e))
    for b in bad:
        print("실패:", b)
    if bad:
        raise SystemExit(1)
