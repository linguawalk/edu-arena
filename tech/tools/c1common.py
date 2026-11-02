"""코스 1(전기전자) 빌더 공통: 회로도 그림 도우미, 복습 출처 태그, 챕터 기록."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from sk import ex, eg, num, fb, order, wr, write_chapter

COURSE_TITLE = "전기전자"


def circ(elements, dots=None, texts=None, alt="회로도"):
    return {"widget": "circuit", "static": True,
            "config": {"elements": elements, "dots": dots or [], "texts": texts or [], "alt": alt}}


def P(t, a, b=None, label=None, **kw):
    d = {"t": t, "a": list(a)}
    if b is not None: d["b"] = list(b)
    if label: d["label"] = label
    d.update(kw)
    return d


def W(a, b):
    return P("wire", a, b)


def left_cell(label="6 V", t="cell"):
    """왼쪽 세로 변에 전지(+가 위)."""
    return [W((0, 0), (0, 0.5)), P(t, (0, 0.5), (0, 1.5), label, side="b"), W((0, 1.5), (0, 2))]


def run(no, title, lessons, review, srcs):
    assert len(review) == len(srcs)
    for q, s in zip(review, srcs):
        q["source_lesson"] = f"c1-ch{no:02d}-l{s:02d}"
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "content")
    write_chapter(root, 1, COURSE_TITLE, no, title, lessons, review, curriculum="tech-level1")
