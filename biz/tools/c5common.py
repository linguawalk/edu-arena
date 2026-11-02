"""코스 5(회계 실무) 빌더 공통: 확장 계정 목록, 분개 문항 도우미, 챕터 기록."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from sk import ex, eg, num, fb, order, wr, jr as _jr, write_chapter
from rules import rv, won
import c4common as C4

# c4 계정에 실무 계정을 더한다(자산 → 부채 → 자본 → 수익 → 비용 순서 유지).
ASSETS = C4.ASSETS[:]
ASSETS[ASSETS.index("받을어음") + 1:ASSETS.index("받을어음") + 1] = ["부도어음과수표"]
ASSETS[ASSETS.index("선급비용"):ASSETS.index("선급비용")] = ["부가세대급금"]
ASSETS[ASSETS.index("상품") + 1:ASSETS.index("상품") + 1] = ["원재료", "재공품", "제품"]
LIAB = C4.LIAB[:]
LIAB[LIAB.index("예수금") + 1:LIAB.index("예수금") + 1] = ["부가세예수금", "미지급세금"]
LIAB += ["퇴직급여충당부채"]
EQUITY = C4.EQUITY[:]
REVENUE = C4.REVENUE[:]
REVENUE[REVENUE.index("상품매출") + 1:REVENUE.index("상품매출") + 1] = ["제품매출"]
EXPENSE = C4.EXPENSE[:]
EXPENSE[EXPENSE.index("상품매출원가") + 1:EXPENSE.index("상품매출원가") + 1] = ["제품매출원가"]
EXPENSE[EXPENSE.index("급여") + 1:EXPENSE.index("급여") + 1] = ["퇴직급여", "임금"]
EXPENSE[EXPENSE.index("임차료"):EXPENSE.index("임차료")] = ["기업업무추진비"]
EXPENSE[EXPENSE.index("소모품비") + 1:EXPENSE.index("소모품비") + 1] = ["도서인쇄비"]
EXPENSE[EXPENSE.index("대손상각비") + 1:EXPENSE.index("대손상각비") + 1] = ["매출채권처분손실"]
EXPENSE[EXPENSE.index("잡손실"):EXPENSE.index("잡손실")] = ["기부금"]
REVENUE.insert(REVENUE.index("잡이익"), "대손충당금환입")
EXPENSE.insert(EXPENSE.index("잡손실"), "재고자산감모손실")
COST = ["제조간접비"]
ALL = ASSETS + LIAB + EQUITY + REVENUE + EXPENSE + COST + C4.CLOSING
assert len(ALL) == len(set(ALL))


def jr(i, stage, prompt, debit, credit, expl, extra=(), hint=None):
    names = {a for a, _ in debit} | {a for a, _ in credit} | set(extra)
    for filler in ["현금", "보통예금", "외상매출금", "외상매입금", "부가세대급금", "부가세예수금", "미지급금", "미수금"]:
        if len(names) >= 6: break
        names.add(filler)
    bad = names - set(ALL)
    assert not bad, f"{i}: 계정 목록에 없음 {bad}"
    return _jr(i, stage, prompt, debit, credit, expl, [a for a in ALL if a in names], hint=hint)


def run(no, title, lessons, review, srcs):
    assert len(review) == len(srcs)
    for q, s in zip(review, srcs):
        q["source_lesson"] = f"c5-ch{no:02d}-l{s:02d}"
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "content")
    write_chapter(root, 5, "회계 실무", no, title, lessons, review, curriculum="2022-voc")
