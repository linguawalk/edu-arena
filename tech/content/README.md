# tech-arena 레슨 스키마 v1.0

math-arena·sci-arena와 같은 스키마·플레이어를 쓴다. 차이점만 적는다.

## 구조
- 레벨1 코스: c1 전기전자, c2 기계, c3 화학공학, c4 컴퓨터 (코스 0 없음)
- 경로: content/level1/{c1~c4}/ch{NN}/l{NN}.json, chapter.json, review.json / 코스 목록 content/level1/courses.json
- 과학 원리는 다시 설명하지 않고 sci-arena 해당 과목을 선수로 안내한다 (courses.json의 prereq)

## 추가 위젯: circuit (정적 회로도)
- figure: {"widget": "circuit", "static": true, "config": {"elements": [...], "dots": [[x,y]], "texts": [[x,y,"글자"]], "alt": "설명"}}
- elements[i]: {"t": 종류, "a": [x,y], "b": [x,y], "label": "R1", "side": "b"(라벨을 반대쪽에), "style": "zigzag"(미국식 저항), "open": false(닫힌 스위치)}
- 종류: wire, cell, battery, source(교류), resistor, lamp, switch, ammeter, voltmeter, fuse, diode, led, capacitor, ground
- 좌표는 격자 단위, y는 아래로 증가. 전지는 a 쪽이 (+)극, 다이오드는 a → b 방향으로 전류가 흐른다
- 빌더 도우미: tools/c1common.py (circ, P, W, left_cell)

## 빌드
- python3 tools/build_c1_ch01.py content && python3 tools/make_course_index.py content
- 단계 A 엄격 검사: 레슨당 문항 15~17개, 화면 20~24개, 예제 3개, 채점형 풀이 20자 이상, 적용·복습 문항 힌트 필수

## 레벨2·3 가이드 (guide)
- 트랙 목록: content/guides.json (10개 분야 + 융합, 과목별 level·available). 다른 트랙 과목을 공유하는 항목은 "t"(원래 트랙)를 가진다
  - 공유: 전자 → 전기의 회로이론·전기자기학, 토목·건축 → 기계의 정역학(토목은 재료역학도)
- 과목: content/level{2|3}/{트랙}/{과목}/subject.json
  - overview(분야 개요 3문단), tagline, level_note(수준과 목차 검증 기준)
  - prereq: text, links(레벨1 챕터·sci-arena·math-arena), questions(선수 점검, id p1~)
  - units: no, title, hours, after(먼저 볼 단원), file / total_hours / next(다음 과목)
- 단원: uNN.json (math-arena·sci-arena 공통 단원 템플릿)
  - objectives, checklist, advice(1~2문단, 문단당 80자 이상), resources(kind lecture|video|book|web, provider, title, part, url, lang), hours, selfcheck(레벨1 문항 스키마, stage = selfcheck)
- 제작: tools/guide_{과목}.py (공용 도구 tools/gk.py — 트랙 구조, 저장 전 검사). 수치 정답은 각 스크립트의 verify()에서 다시 계산
- 페이지: guide.html (?lv=&t=&s=&u=) — tools/make_guide.py가 player.html 공용 코드로 생성
- 저장: localStorage "tech-arena:guide" = {단원 id: {checks: [체크한 항목 번호], sc: {문항 id: 정답 여부}}}
- 목차 검증: 레벨2는 산업기사, 레벨3은 기사 필기 과목 구성(누락 방지용). 추천 자료는 무료 공개 자료 우선, 유료 교재는 URL 없이 장 번호만

## 바뀔 수 있는 내용의 관리 (review, standards, audit)
- 법령·기준·시험 제도·시장 수치처럼 바뀔 수 있는 내용이 있는 과목·단원에는 review를 붙인다
  - review: {basis(근거), checked(확인 YYYY-MM), next(다음 점검 YYYY-MM), watch(무엇이 바뀌면 고칠지), standards(쓰는 규정값 키)}
  - 화면에는 "기준 안내" 상자(근거와 확인 시점)가, 로드맵 카드에는 "기준 확인 필요"가 표시된다
  - 원리만 다루는 단원에는 붙이지 않는다
  - 주의: 레벨1 챕터의 "review"는 복습 레슨이다. 점검 정보는 가이드(type guide_unit·guide_subject)에서만 쓴다
- 규정값: content/standards.json {items: {키: {value, unit, text, basis, clause, checked, next}}}
  - 가이드 스크립트는 std(키)로 값을 불러 문항·해설·체크리스트에 쓴다
  - 기준이 바뀌면 standards.json 값을 고치고 해당 tools/guide_*.py를 다시 실행하면 함께 바뀐다
- 점검 보고서: python3 tools/audit.py [--links] [--ahead 개월] [--out 파일] [사이트 경로]
  - 점검 기한이 지났거나 곧 돌아오는 단원·규정값, (--links) 열리지 않거나 옮겨진 외부 링크를 보고한다
  - math·sci-arena 저장소에도 그대로 쓸 수 있다
