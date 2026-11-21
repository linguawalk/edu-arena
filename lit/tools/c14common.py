"""코스 14(중국어Ⅱ) 빌더 공통: 복습 출처 태그와 챕터 기록.

중국어 답은 한자, 병음(성조 부호 있는 것과 없는 것), 한글 표기를 함께 허용한다(입력기 부담을 줄이기 위함).
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from facts import F, V  # noqa: F401
from sk import ex, eg, num, fb, order, wr, write_chapter

D = ["중국어"]
REGION = "CN"


def run(no, title, lessons, review, srcs):
    assert len(review) == len(srcs)
    for L in lessons:
        L["region"] = REGION
    for q, s in zip(review, srcs):
        q["source_lesson"] = f"c14-ch{no:02d}-l{s:02d}"
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "content")
    write_chapter(root, 14, "중국어Ⅱ", no, title, lessons, review, curriculum="2022-high")
