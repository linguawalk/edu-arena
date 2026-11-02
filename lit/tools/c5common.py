"""코스 5(영어Ⅰ: 영어의 구조) 빌더 공통: 복습 출처 태그와 챕터 기록."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from facts import F, V  # noqa: F401
from sk import ex, eg, num, fb, order, wr, write_chapter

D = ["영어"]


def run(no, title, lessons, review, srcs):
    assert len(review) == len(srcs)
    for q, s in zip(review, srcs):
        q["source_lesson"] = f"c5-ch{no:02d}-l{s:02d}"
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "content")
    write_chapter(root, 5, "영어Ⅰ", no, title, lessons, review, curriculum="2022-high")
