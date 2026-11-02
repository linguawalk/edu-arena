# socio-arena 레슨 스키마 v1.0

sci-arena·math-arena 레슨 스키마 v1.0을 그대로 따른다. 플레이어(player.html)와 코스 목록(browse.html)도 sci-arena에서 가져와 문구와 채점 정규화만 바꾸었다.

경로: content/level{N}/{course}/ch{NN}/l{NN}.json
- 코스 목록: content/level1/courses.json (11과목, available로 공개 여부 표시)
- 코스 요약: content/level1/{course}/course.json (tools/make_course_index.py가 생성)
- 챕터 목록: content/level1/{course}/ch{NN}/chapter.json
- 챕터 복습 세트: content/level1/{course}/ch{NN}/review.json

## 코스 번호
| id | 과목 | 상태 |
| --- | --- | --- |
| c1 | 한국사Ⅰ | 공개 (8챕터, 레슨 32개, 569문항) |
| c2 | 한국사Ⅱ | 공개 (8챕터, 레슨 32개, 560문항) |
| c3 | 세계사Ⅰ | 공개 (8챕터, 레슨 32개, 560문항) |
| c4 | 세계사Ⅱ | 공개 (8챕터, 레슨 32개, 560문항) |
| c5 | 사회와 문화 | 공개 (8챕터, 레슨 32개, 560문항) |
| c6 | 지리Ⅰ | 공개 (8챕터, 레슨 32개, 561문항) |
| c7 | 지리Ⅱ | 공개 (8챕터, 레슨 32개, 560문항) |
| c8 | 정치와 법Ⅰ | 공개 (8챕터, 레슨 32개, 560문항) |
| c9 | 정치와 법Ⅱ | 공개 (8챕터, 레슨 32개, 560문항) |
| c10 | 윤리Ⅰ | 공개 (8챕터, 레슨 32개, 560문항) |
| c11 | 윤리Ⅱ | 공개 (8챕터, 레슨 32개, 560문항) |

코스 0(중학 과정)은 두지 않는다. 각 과목 첫 단원의 도입 화면이 기초를 다진다.

## 레슨 파일
- course / chapter / lesson: id, 번호, 제목 (lesson.minutes = 예상 소요 시간)
- tags.domain: ["한국사"] 등 과목 태그, tags.region = KR, tags.curriculum = 2022-high
- screens: 화면 배열. stage = intro | discover | summary | apply
- 분량 기준: 레슨당 화면 20~24개, 문항 15~17개, 예제 3개

## 화면 유형
- explain: title, body(문단 배열)
- example: 자료 해석 예제. problem, steps(풀이 단계), answer
- question
  - fill_blank: 사건·인물·제도 이름. blanks[n].answers에 허용 표기(띄어쓰기 변형, 별칭)를 모두 넣는다
  - numeric: 연도. 기원전 연도는 문제에 "기원전 몇 년"으로 묻고 양수로 답한다
  - ordering: 사건 순서 배열
  - written: 서술형. rubric.keyword_groups 중 min_groups_matched개 이상 포함되면 통과
- 공통: hint(적용·복습 문항은 필수), explanation(20자 이상, 줄바꿈으로 단계 구분)

## 채점 정규화 (sci-arena와 다른 점)
- 공백, 가운뎃점(·ㆍ), 따옴표·낫표를 무시한다 ("한일 의정서" = "한일의정서")
- 괄호 속 한자 병기를 무시한다 ("녹읍(祿邑)" = "녹읍")
- 영문은 대소문자를 구분하지 않는다 ("SI" = "si")

## 빌드
```
python3 tools/build_c1_ch01.py content   # 챕터마다 실행 (ch01~ch08)
python3 tools/make_course_index.py content
```
- 공용 도구 tools/sk.py: 저장 전에 문항 수, 화면 수, 예제 수, 풀이 길이, 힌트, 빈칸 수, 복습 출처 레슨을 검사하고 기준을 벗어나면 실패한다
- 코스 공통: tools/c{코스}common.py (복습 문항의 source_lesson 지정)

## 바뀔 수 있는 내용
한국사Ⅱ 챕터 7(역대 정부 목록, 탄핵 심판)과 챕터 8(남북 관계), 세계사Ⅱ 챕터 8(EU 회원 현황, 분쟁과 난민, 기후 협약, 동아시아 역사·영토 갈등)은 현재 상황에 따라 갱신이 필요하다. 그 밖의 역사는 내용이 거의 바뀌지 않지만, 세계 유산·기록 유산 등재 현황과 문화재 반환 상태는 바뀔 수 있다.

### 규정값 한곳 관리 (사회와 문화부터)
- 통계 수치처럼 바뀌는 값은 tools/facts.py에만 적는다. 항목마다 문장 조각(text), 정답 값(value), 기준 시점, 출처, 마지막 확인일, 점검 주기를 둔다.
- 빌더는 F("키")로 문장을, V("키")로 정답 값을 가져온다. 레슨에 수치를 직접 쓰지 않는다.
- 값이 바뀌면 facts.py를 고치고 해당 챕터 빌더를 다시 실행한다.
- 점검: `python3 tools/check_facts.py content` — 점검 주기가 지난 항목과 각 값이 쓰인 레슨 파일을 보여 주고, 점검할 항목이 있으면 종료 코드 1을 낸다.
- 현재 항목: 합계 출산율(2024·2025), 65세 이상 인구 비율(2025 인구주택총조사), 초고령 사회 진입 시점, 국가 통계 기관명(이상 c5), 세계 인구(80억 돌파 시점·2025 추계), 2024년 지구 평균 기온 상승폭, 2035 국가 온실가스 감축 목표(이상 c6), 수도권 인구 비중 50% 돌파 시점(c7), 선거권·피선거권·정당 가입 연령, 국회의원 정수와 비례 대표제 방식, 광역 자치 단체 수, 국제 연합 회원국 수(이상 c8), 형사 미성년자 연령, 최저 임금, 법정 근로 시간·청소년 근로 시간, 임대차 갱신 요구권, 수사·기소 분리 체계, 2025 노동조합법 개정(이상 c9), 낙태죄 대체 입법 상황, 인공지능 기본법(이상 c10), 방송·통신 규제 기관, 국민기초생활보장 급여 선정 기준과 기준 중위소득, 헌법 개정 현황, 중앙 행정 기관 체계, 민법상 성년 연령과 만 나이 계산(이상 레벨2 가이드).

## 레벨2·3 가이드 (guide)
- tech-arena·math-arena·sci-arena와 같은 공통 단원 템플릿을 쓴다. 레벨2는 11개 학문 트랙 25과목(과목당 10단원), 레벨3은 같은 트랙의 30과목(과목당 8단원, 약 35시간)이 공개되어 있다.
- 트랙 목록: content/guides.json (트랙별 과목, level·available). 다른 트랙 과목을 공유하는 항목은 "t"(원래 트랙)를 가진다
  - 공유: 사회복지 → 사회학의 사회조사방법론, 심리학 → 사회학의 사회통계, 행정학 → 법학의 헌법
- 과목: content/level{2|3}/{트랙}/{과목}/subject.json
  - overview(분야 개요 3문단), tagline, level_note(수준과 목차 검증 기준), review(바뀔 수 있는 내용이 있을 때)
  - prereq: text, links(레벨1 챕터·다른 레벨2 과목·math·sci-arena), questions(선수 점검, id p1~)
  - units: no, title, hours, after(먼저 볼 단원), file / total_hours / next(다음 과목)
- 단원: uNN.json — objectives, checklist, advice(1~2문단, 문단당 80자 이상), resources(kind lecture|video|book|web, provider, title, part, url, lang), hours, selfcheck(레벨1 문항 스키마, stage = selfcheck), review(선택)
- 제작: tools/guide_{과목}.py (공용 도구 tools/gk.py — 트랙 구조, 저장 전 검사: 지문 정답 노출, 순서 문항 표시 순서, 모범 답안과 채점 기준, 자료 형식). 트랙별 공용 자료는 hist_common, soc_common, geo_common, pol_common, phil_common
- 페이지: guide.html (?lv=&t=&s=&u=) — `python3 tools/make_guide.py`가 player.html 공용 코드와 tools/guide_tpl.html로 생성
- 저장: localStorage "socio-arena:guide" = {단원 id: {checks: [체크한 항목 번호], sc: {문항 id: 정답 여부}}}
- 바뀔 수 있는 값은 레벨1과 같이 tools/facts.py의 F()·V()로 쓰고, 그런 단원·과목에는 review(basis, checked, next, watch, facts)를 붙인다. 화면에 "기준 안내" 상자가 나온다
- 점검: `python3 tools/check_facts.py content`(가이드 파일도 함께 검사), `python3 tools/audit.py [--links]`(review 점검 기한과 외부 링크)
- 레벨3 형식: 단원마다 학습 목표 2~3개, 체크리스트 5개, 학습 조언 1문단, 추천 자료, 자가점검 3문항. level_note는 gk.L3NOTE, 레벨3 과목끼리의 단원 링크는 gk.G3R(자료)·gk.G3(선수 링크)
- 레벨3에서 새로 쓴 바뀔 수 있는 값: commercial_act_2025(상법 이사 충실 의무 개정). 그 밖에 min_wage, work_hours, union_act_2025, criminal_age, prosecution_system, gov_org, nbls_rates, abortion_law, ai_basic_act를 다시 쓴다
- 목차 검증: 레벨2는 학과별 개론 교재와 관련 시험(한국사능력검정시험 심화, 사회조사분석사 2급, 임상심리사 2급·청소년상담사 3급, 사회복지사 1급, 공무원 시험 행정학·헌법 등)의 출제 범위. 추천 자료는 무료 공개 자료 우선, 유료 교재는 URL 없이 장 제목만

