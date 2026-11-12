"""수학 수리논술 에세이 공통 도구. build_essay_cX_*.py에서 씁니다.
수리논술 = 계산 결과만이 아니라 '왜 그런지'를 식과 말로 풀어 쓰는 글.
과제 유형: 성질 증명·설명, 풀이 오류 진단, 두 풀이 비교, 실생활 상황 모델링, 친구에게 원리 설명."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
from essay_kit import essay, chk, src, write_essays

LEN = (350, 700)
SELF_MATH = [("풀이", "물음에 끝까지 답하고 결론(답)을 분명히 밝혔는가"),
             ("논리", "각 단계가 앞 단계나 레슨에서 배운 정의·성질에서 바로 따라 나오는가"),
             ("정확성", "계산, 식, 기호, 단위가 정확한가"),
             ("설명", "읽는 사람이 식을 따라가며 이해할 수 있도록 까닭을 말로 풀어 썼는가")]


def E(prompt, conds, checks, outline, answer, sources=(), length=LEN):
    conds = list(conds) + [f"{length[0]}~{length[1]}자, 3문단 이상"]
    return essay(prompt, conds, checks, outline, answer, sources=sources, length=length, paragraphs=3, self_=SELF_MATH)


def S(*lines, label="제시문", title=None):
    return src(label, lines, title=title)


def run(course, ch, lessons):
    bad = 0
    for no, es in enumerate(lessons, 1):
        try:
            print(write_essays("math", course, ch, no, es))
        except AssertionError as e:
            bad += 1
            print("실패:", e)
    if bad:
        raise SystemExit(1)
