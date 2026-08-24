# edu-arena 콘텐츠 스키마 설계 (초안)

lingua-arena / code-arena와 일관된 구조를 유지하면서, 교양 콘텐츠 특성에 맞게 조정한 초안입니다.

## 1. 카테고리 트리 구조

```json
{
  "axis": "humanities_social",       // humanities_social | stem | general_knowledge
  "category": "korean_history",       // 세부 카테고리 slug
  "category_label": "한국사",
  "region_or_field": "korea",         // 지역(인문사회) 또는 세부분야(STEM)
  "level": "basic"                    // basic | advanced | expert
}
```

- **인문사회(humanities_social)**: 수능 사탐 8과목 + 역사 5지역 트랙을 `category`로 나열
- **STEM(stem)**: 과학탐구 5영역 + 수학 영역을 `category`로 나열
- **교양상식(general_knowledge)**: 시사 / 문화·생활 / 세계상식 / 과학상식 등 느슨한 서브카테고리

## 2. 문항(Question) 스키마

```json
{
  "id": "kh-basic-0001",
  "axis": "humanities_social",
  "category": "korean_history",
  "level": "basic",
  "type": "multiple_choice",
  "question": "고려를 건국한 인물은 누구인가?",
  "options": ["왕건", "궁예", "견훤", "이성계"],
  "answer": "왕건",
  "explanation": "왕건은 918년 고려를 건국하고 후삼국을 통일했다.",
  "tags": ["고려", "건국"],
  "source_ref": null
}
```

- `type`은 `multiple_choice`로 통일
- `level`은 3단계(basic / advanced / expert)
- `tags`는 검색/연관문항 추천용, 필수 아님

## 3. 최소 문항 수 기준

| 레벨 | 카테고리당 문항 수 |
|---|---|
| basic | 25 이상 |
| advanced | 25 이상 |
| expert | 25 이상 |

레벨별 최소 25문항 기준으로, 카테고리 하나가 이 최소치를 채울 소재가 없으면 상위 카테고리로 통합. (3단계 기준 카테고리당 총 75문항 이상)

## 4. 파일 구성 (예시)

```
/data
  /humanities_social
    korean_history.json
    world_history_asia_oceania.json
    ...
  /stem
    physics.json
    ...
  /general_knowledge
    current_affairs.json
    ...
/CATEGORIES.md   ← 전체 카테고리 트리 문서
```

## 확정된 사항

- 레벨: 3단계 (basic / advanced / expert)
- 최소 문항 수: 레벨당 25문항 이상
- 문제 유형: 객관식(multiple_choice) 단일 유형으로 통일
