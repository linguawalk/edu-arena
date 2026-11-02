"""바뀔 수 있는 규정값·현황을 한곳에서 관리한다.

레슨 빌더는 값을 직접 쓰지 않고 F("키")로 문장 조각을, V("키")로 정답 값을 가져온다.
값이 바뀌면 이 파일만 고치고 해당 챕터를 다시 빌드한다.
tools/check_facts.py가 점검 주기가 지난 항목과 각 값이 쓰인 레슨을 보여 준다.

lit-arena에서 바뀔 수 있는 값의 예
- 어문 규범 개정: 추가 표준어, 맞춤법·외래어 표기법·로마자 표기법 개정
- 교육용 기초 한자 목록(현행 1,800자)과 한자능력검정시험 급수 체계
- 문학상 수상 현황(노벨 문학상, 부커상 등), 교육과정 개정
수상 현황처럼 해마다 바뀌는 값은 레슨에 '○○년 기준'을 함께 적는다.

항목 필드
- text: 레슨에 들어가는 문장 조각 (기준 시점을 함께 적는다)
- value: 문항 정답으로 쓰는 값 (없으면 None)
- as_of: 기준 시점
- source: 확인한 출처
- checked: 마지막으로 확인한 날짜 (YYYY-MM-DD)
- cycle: 점검 주기(일)
"""

FACTS = {
    "basic_hanja": dict(
        text="현행 교육용 기초 한자는 1,800자(중학교용 900자, 고등학교용 900자)이며 2000년에 조정되었다",
        value="1800", as_of="2000년 조정안", source="교육부 한문 교육용 기초 한자(2000 조정)",
        checked="2026-10-16", cycle=730),
    "norm_spelling": dict(
        text="현행 「한글 맞춤법」은 1988년에 고시되어 1989년 3월부터 시행되었고, 2017년에 일부 개정되었다",
        value="1988", as_of="2017년 일부 개정 반영", source="국립국어원 한국어 어문 규범(korean.go.kr/kornorms)",
        checked="2026-10-19", cycle=365),
    "norm_punctuation": dict(
        text="현행 문장 부호 규정은 2014년에 개정되어 2015년 1월부터 시행되었다",
        value="2014", as_of="2014년 개정", source="국립국어원 한국어 어문 규범(한글 맞춤법 부록)",
        checked="2026-10-19", cycle=365),
    "norm_loanword": dict(
        text="현행 「외래어 표기법」은 1986년부터 시행되었고, 2017년에 표기 세칙 일부가 개정되었다",
        value="1986", as_of="2017년 일부 개정 반영", source="국립국어원 한국어 어문 규범(외래어 표기법)",
        checked="2026-10-19", cycle=365),
    "norm_romanization": dict(
        text="현행 「국어의 로마자 표기법」은 2000년에 고시되었고, 2014년에 일부 개정되었다",
        value="2000", as_of="2014년 일부 개정 반영", source="국립국어원 한국어 어문 규범(국어의 로마자 표기법)",
        checked="2026-10-19", cycle=365),
    "cite_editions": dict(
        text="2026년 10월 기준 APA 양식은 7판(2019), MLA 양식은 9판(2021), 시카고 양식은 18판(2024)이 최신판이다",
        value="7", as_of="2026-10", source="APA Style(apastyle.apa.org), MLA Style Center, Chicago Manual of Style Online",
        checked="2026-10-19", cycle=365),
}


def F(key):
    return FACTS[key]["text"]


def V(key):
    return FACTS[key]["value"]
