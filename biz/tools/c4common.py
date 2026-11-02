"""코스 4(회계 원리) 빌더 공통: 계정 목록, 분개 문항 도우미, 챕터 기록."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from sk import ex, eg, num, fb, order, wr, jr as _jr, write_chapter
from rules import rv, won

# 계정 과목 (일반기업회계기준·전산회계 교재 관행 이름). 선택지는 이 순서(자산 → 부채 → 자본 → 수익 → 비용)로 보인다.
ASSETS = ["현금", "보통예금", "당좌예금", "정기예금", "단기매매증권", "외상매출금", "받을어음", "대손충당금", "미수금", "선급금",
          "선급비용", "미수수익", "단기대여금", "가지급금", "현금과부족", "상품", "소모품", "토지", "건물", "차량운반구", "비품", "기계장치",
          "감가상각누계액", "건설중인자산", "특허권", "장기대여금"]
LIAB = ["외상매입금", "지급어음", "미지급금", "선수금", "미지급비용", "선수수익", "예수금", "가수금", "미지급배당금", "단기차입금", "유동성장기부채", "장기차입금", "사채"]
EQUITY = ["자본금", "주식발행초과금", "인출금", "이익준비금", "이익잉여금"]
REVENUE = ["상품매출", "이자수익", "임대료", "수수료수익", "배당금수익", "유형자산처분이익", "단기매매증권처분이익", "단기매매증권평가이익", "잡이익"]
EXPENSE = ["상품매출원가", "급여", "복리후생비", "여비교통비", "임차료", "통신비", "수도광열비", "세금과공과", "광고선전비", "보험료", "수선비", "소모품비",
           "차량유지비", "운반비", "수수료비용", "이자비용", "감가상각비", "무형자산상각비", "대손상각비", "유형자산처분손실", "단기매매증권처분손실", "단기매매증권평가손실", "잡손실"]
CLOSING = ["손익"]
ALL = ASSETS + LIAB + EQUITY + REVENUE + EXPENSE + CLOSING
KIND = {**{a: "자산" for a in ASSETS}, **{a: "부채" for a in LIAB}, **{a: "자본" for a in EQUITY},
        **{a: "수익" for a in REVENUE}, **{a: "비용" for a in EXPENSE}}


def jr(i, stage, prompt, debit, credit, expl, extra=(), hint=None):
    """정답 계정 + extra(헷갈리기 쉬운 계정)를 선택지로, 총 6개가 안 되면 기본 계정으로 채운다."""
    names = {a for a, _ in debit} | {a for a, _ in credit} | set(extra)
    for filler in ["현금", "보통예금", "외상매출금", "외상매입금", "자본금", "상품", "미지급금", "미수금"]:
        if len(names) >= 6: break
        names.add(filler)
    bad = names - set(ALL)
    assert not bad, f"{i}: 계정 목록에 없음 {bad}"
    return _jr(i, stage, prompt, debit, credit, expl, [a for a in ALL if a in names], hint=hint)


def run(no, title, lessons, review, srcs):
    assert len(review) == len(srcs)
    for q, s in zip(review, srcs):
        q["source_lesson"] = f"c4-ch{no:02d}-l{s:02d}"
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "content")
    write_chapter(root, 4, "회계 원리", no, title, lessons, review, curriculum="2022-voc")
