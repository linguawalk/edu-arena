"""예체능 레벨1(음악 이론·음악사·미술 요소·미술사·스포츠와 건강) 에세이용 짧은 작성 도구.

예체능 에세이는 지식을 '설명하는 글'이 아니라, 배운 지식을 근거로 실제 상황의 과제
(연주회 해설, 감상 안내, 전시 해설, 운동 계획서, 안전 안내문, 경기 규칙 설명 등)를 해내는 글입니다.
의견·찬반을 묻지 않고, 견해가 갈리는 문제는 여러 입장을 나란히 제시합니다.
분량 400~700자, 3문단.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
from essay_kit import essay, chk, src, write_essays  # noqa: F401

LEN = (400, 700)

SELF_ARTS = [
    ("과제", "제시된 상황에서 요구한 글(해설·안내·계획·비교)을 끝까지 써냈는가"),
    ("근거", "레슨에서 배운 개념과 용어를 작품·악곡·동작의 구체적인 부분과 연결했는가"),
    ("정확성", "용어, 수치, 작가·시대, 안전 수칙에 관한 사실이 정확한가"),
    ("전달", "글을 읽을 사람(관객·관람객·친구·선수)이 바로 이해하고 따라 할 수 있게 썼는가"),
]


def E(prompt, conds, checks, outline, answer, sources=(), length=LEN):
    conds = list(conds) + [f"{length[0]}~{length[1]}자, 3문단 이상"]
    return essay(prompt, conds, checks, outline, answer, sources=sources, length=length, paragraphs=3, self_=SELF_ARTS)


def S(*lines, label="자료", title=None):
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
            print(write_essays("arts", course, ch, no, es))
        except AssertionError as e:
            bad.append(str(e))
    for b in bad:
        print("실패:", b)
    if bad:
        raise SystemExit(1)
