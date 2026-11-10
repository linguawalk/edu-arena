"""언어와 문학 레벨1(국어·한자·영어) 에세이용 짧은 작성 도구.

이 과목들의 에세이는 문법·규범을 '설명하는 글'이 아니라, 배운 지식을 '도구'로 써서
실제 상황의 과제(고쳐 쓰기, 풀이하기, 안내문·이메일 쓰기, 요약하기 등)를 해내는 글입니다.
분량 400~700자, 3문단.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
from essay_kit import essay, chk, src, write_essays  # noqa: F401

LEN = (400, 700)

SELF_TOOL = [
    ("과제", "제시된 상황에서 요구한 일(고쳐 쓰기·풀이·작성)을 끝까지 해냈는가"),
    ("도구", "레슨에서 배운 지식을 근거로 들어 정확하게 활용했는가"),
    ("정확성", "고친 문장·풀이·영문이 규범과 문법에 맞는가"),
    ("전달", "글을 읽을 사람이 바로 이해하고 쓸 수 있게 썼는가"),
]


def E(prompt, conds, checks, outline, answer, sources=(), length=LEN):
    conds = list(conds) + [f"{length[0]}~{length[1]}자, 3문단 이상"]
    return essay(prompt, conds, checks, outline, answer, sources=sources, length=length, paragraphs=3, self_=SELF_TOOL)


def S(*lines, label="제시문", title=None):
    return src(label, lines, title=title)


def run(course, ch, lessons):
    import json
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    with open(os.path.join(root, "content", "level1", course, f"ch{ch:02d}", "chapter.json"), encoding="utf-8") as f:
        n = len(json.load(f)["lessons"])
    assert len(lessons) == n, f"{course} ch{ch}: 레슨 {n}개인데 에세이 묶음 {len(lessons)}개"
    bad = []
    for no, es in enumerate(lessons, 1):
        try:
            print(write_essays("lit", course, ch, no, es))
        except AssertionError as e:
            bad.append(str(e))
    for b in bad:
        print("실패:", b)
    if bad:
        raise SystemExit(1)
