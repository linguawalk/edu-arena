# 레벨1 '더 연습하기' 문제 은행

- core.py: 공통 도구 (num, fill, build, write, 조사 처리)
- c0_ch01.py ~ c0_ch06.py: 코스0 챕터별 템플릿
- c1_a.py(챕터1~4), c1_b.py(챕터5~7): 코스1 템플릿
- c2_a.py(챕터1~3), c2_b.py(챕터4~6): 코스2 템플릿
- c3_a.py(챕터1~3), c3_b.py(챕터4~5), c3_c.py(챕터6~7): 코스3 템플릿
- c4_a.py(챕터1~4), c4_b.py(챕터5~8): 코스4 템플릿
- c5.py: 코스5 템플릿
- c6.py: 코스6 템플릿 (이차곡선, 평면벡터, 공간도형·공간좌표)
  실행하면 content/level1/cX/chNN/pNN.json 생성, chapter.json 연결
- verify.py: 식으로 읽을 수 있는 문항을 sympy로 독립 검산 (python3 verify.py "…/c0/ch0*/p0*.json")
- verify_brute.py: 경우의 수·집합·행렬 문항을 완전탐색으로 검산
- verify_c3.py: 로그·Σ·점화식·삼각함수값 검산
- verify_c4.py: 극한·미분·정적분 문항 검산
- verify_c5.py: 경우의 수·확률 문항 완전탐색 검산
- verify_c6.py: 코스6 문장 재해석 검산 (곡선·벡터·정육면체 기하 재계산)
- totals.py: course.json에 연습 문항 수 반영
- test_practice.py: 사이트 폴더에서 python3 -m http.server 8765 실행 후, 은행 전체를 정답 입력해 채점 확인

core.py의 SITE 경로를 저장소 위치로 바꾸어 실행합니다.
