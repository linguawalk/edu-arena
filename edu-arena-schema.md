# edu-arena 콘텐츠 스키마 설계 (개정 — 12개 과정, 학력 수준 3단계)

## 1. 과정 구조

```json
{
  "axis": "humanities_social",   // humanities_social | stem
  "subject": "history",           // 과정 slug
  "subject_label": "역사",
  "level": 1                      // 1: 고졸 수준 | 2: 대학 1년 수료 | 3: 대학 2년 수료
}
```

- 인문사회 6개(역사/지리/일반사회/정치와 법/경제/문화) + STEM 6개(수학/물리/화학/생물/지구과학/공학) = 12개 과정
- 언어는 lingua-arena, 프로그래밍은 code-arena에서 다루므로 edu-arena는 제외
- 향후 신설 과목도 동일 구조(3단계) 적용, 수요 기반으로 개설

## 2. 문항(Question) 스키마

```json
{
  "id": "history-l1-0001",
  "axis": "humanities_social",
  "subject": "history",
  "level": 1,
  "type": "multiple_choice",
  "question": "...",
  "options": ["...", "...", "...", "..."],
  "answer": "...",
  "explanation": "...",
  "tags": ["..."],
  "source_ref": null
}
```

- `type`은 `multiple_choice`로 통일
- `level`: 1(고졸)/2(대학 1년 수료)/3(대학 2년 수료)

## 3. 목표 문항 수 기준

| 항목 | 기준 |
|---|---|
| 과정×레벨당 문항 수 | 500문항 |
| 과정×레벨당 요약 해설 | A4 10p |
| 초기 제작 범위 | 12개 과정 × 1단계만 |
| 초기 문항 규모 | 500 × 12 = **6,000문항** |
| 초기 해설 규모 | 10p × 12 = **120p** |

- 2·3단계 확장은 참가자 반응(수요)을 보고 결정

## 4. 설명(학습자료) 콘텐츠 구조

```json
{
  "subject": "history",
  "level": 1,
  "unit_title": "...",
  "content_md": "## ...\n\n...",
  "estimated_pages": 2
}
```

- 여러 소단원(unit)으로 나눠 관리, 레벨당 합산 10p 목표
- 파일: `study/{subject}_l{level}.md` — 문항 파일 `data/{subject}_l{level}.json`과 짝을 이룸

## 5. 인증(측정 전용) 트랙 — 별도 제작 없음

- 응시 시 해당 과정×레벨 500문항 풀에서 50문항 무작위 추출
- 통과 기준(예: 70% 이상) 충족 시 배지/인증 발급
- 별도 데이터 제작 불필요

## 6. 파일 구성 (예시)

```
/data
  /humanities_social
    history_l1.json
    geography_l1.json
    ...
  /stem
    mathematics_l1.json
    engineering_l1.json
    ...
/study
  /humanities_social
    history_l1.md
    ...
/CATEGORIES.md
```

## 확정된 사항

- 과정: 12개 (인문사회 6 + STEM 6), 언어·프로그래밍 제외
- 레벨: 3단계 (고졸 / 대학 1년 수료 / 대학 2년 수료) — 전 과정 공통 기준
- 목표 문항 수: 과정×레벨당 500문항, 초기엔 1단계만 제작
- 요약 해설: 과정×레벨당 10p
- 문제 유형: 객관식(multiple_choice) 단일 유형
- 인증: 별도 제작 없이 500문항 풀에서 무작위 추출
- 신규 과목: 수요(신청자 수) 기반으로 추가 개설
