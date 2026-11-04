# 외국어 (edu-arena/lingua)

예전 lingua-arena 저장소(linguawalk/lingua-arena)의 콘텐츠를 그대로 옮긴 폴더입니다. 코딩(code/)과 같은 방식으로 통합했습니다.

- `browse.html`: edu-arena 공통 레이아웃의 코스 화면. 왼쪽은 언어 6개 × 형식(쓰기·말하기 / 객관식), 오른쪽은 CEFR A1–C2 레벨별 유닛 목록.
- `content/catalog.json`: browse.html이 읽는 유닛 제목 목록. 유닛을 추가하거나 제목을 바꾼 뒤 `python3 tools/build_catalog.py`로 다시 만듭니다.
- 학습 화면은 그대로입니다: `task.html`(쓰기·말하기), `checkpoint.html`(레벨 체크포인트), `placement.html`(배치고사), `lesson.html`·`play.html`(기존 객관식).
- 데이터: `data_v2/`(언어당 300유닛, 유닛당 쓰기 2 + 말하기 2), `data/`(기존 객관식, 레벨당 20유닛 × 25문항).
- 예전 주소(`index.html`, `units_v2.html`, `units.html`, `languages/xx/index.html`)는 browse.html로 넘겨 줍니다.
- 외국인을 위한 한국어 과정은 edu-arena 통합 때 뺐습니다(원본은 linguawalk/lingua-arena 저장소에 남아 있음).
- 학습 화면의 안내 문구는 한국어가 기본이고, EN/KO 버튼으로 바꿀 수 있습니다.
- `docs/curriculum.md`: 원래 커리큘럼 문서.
