# test-arena 콘텐츠 구조 v1.0

레슨 스키마는 math-arena 레슨 스키마 v1.0을 그대로 쓰고, 자가 채점 증명 문항(proof)을 더했다.
콘텐츠는 직접 고치지 않고 `tools/lessons/*.py`를 고친 뒤 `python3 tools/build.py`로 다시 만든다.

## 경로
- 분야 목록: content/catalog.json
- 분야: content/{subj}/subject.json (단계 s1~s3, 단계별 트랙)
- 트랙: content/{subj}/s{N}/{track}/track.json (챕터 목록, available)
- 챕터: content/{subj}/s{N}/{track}/ch{NN}/chapter.json, l{NN}.json, review.json
- 레슨 원본: tools/lessons/{subj}_s{N}_{track}_ch{NN}.py (이 파일이 있는 챕터만 열림)

## 수학 단계·트랙
- 단계: s1 예선(국내 1차) · s2 본선(국내 2차·최종 선발) · s3 국제(목차·가이드 중심)
- 트랙: proof 증명의 기초 · alg 대수 · nt 정수론 · comb 조합 · geo 기하
- 챕터 제목은 tools/curriculum.py에서 관리

## 제작 기준 (build.py가 검사)
- 레슨: 화면 16~22개, 문항 11~13개, 그중 증명 문항 2개 이상
- 모든 문항에 힌트
- 채점형 문항(numeric, fill_blank, ordering, diagram) 풀이: 60자 이상, 3단계 이상(줄바꿈으로 구분)
- 설명 화면: 160자 이상, "왜 그런지" 문단 포함
- 예제: 풀이 3단계 이상
- 챕터 복습: 10문항, 그중 증명 문항 1개 이상
- 문항은 모두 자체 제작. 대회 기출은 싣지 않음

## S3 학습 가이드 (build.py가 검사)
- 레슨 파일 대신 GUIDE 하나를 내보내면 그 챕터는 가이드 1개로 만들어지고 복습은 없다(chapter.json의 kind = "guide")
- 화면 14~24개, 예제 2개 이상, 확인 문항(채점형) 2개 이상, 증명 문제 5개 이상
- 설명·예제·채점형 풀이 기준은 레슨과 같다. 증명 문제의 채점 기준은 대체로 7점 만점
- 짜임: 사용법·핵심 도구 설명 → 예제 → 확인 문항 → 증명 문제 → 독학 순서와 참고 자료 → 자기 점검

## proof 문항 (자가 채점)
- prompt, model_answer(모범 증명 단계 배열), criteria([{text, points}]), hint, explanation(선택)
- 플레이어 흐름: 증명 쓰기(빈칸으로 두어도 됨) → 확인 → 모범 증명과 채점 기준 표시 → 내 답안에 있는 기준을 체크 → 채점 완료
- 만점이면 맞힌 문항으로 센다

## 저장
- localStorage "test-arena:progress" = {레슨·복습 id: {done, first(한 번에 맞힌 수), total, at}}
