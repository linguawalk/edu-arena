# Code Arena — Global Certification Content

전 세계 IT 자격증 준비를 위한 문제 콘텐츠 모음입니다. 각 벤더/자격증별로 폴더가 나뉘어 있으며, 레벨(level)과 유닛(unit) 단위의 JSON 파일로 구성되어 있습니다.

## 폴더 구조

```
certifications/
├── aws/
│   ├── clf-c02/              # AWS Cloud Practitioner (4 levels × 4 units)
│   └── saa-c03/              # AWS Solutions Architect Associate (4 levels × 4 units)
├── oracle/
│   ├── java-ocp/             # Oracle Java OCP 1Z0-829 (7 levels × 4 units)
│   ├── sql-associate/        # Oracle SQL Associate 1Z0-071 (3 levels × 4 units)
│   └── plsql-associate/      # Oracle PL/SQL Associate 1Z0-149 (7 levels × 4 units)
├── microsoft/
│   └── az-900/               # Microsoft Azure Fundamentals (3 levels × 4 units)
├── google/
│   └── cloud-digital-leader/ # Google Cloud Digital Leader (6 levels × 4 units)
├── cisco/
│   └── ccna/                 # Cisco CCNA 200-301 (6 levels × 4 units)
└── lpi/
    ├── lpic-1/                # LPIC-1 101/102 (4 levels × 4 units)
    └── lpic-2/                # LPIC-2 201/202 (4 levels × 4 units)
```

## 파일 형식

각 JSON 파일은 하나의 유닛(unit)을 나타내며 다음 구조를 따릅니다:

```json
{
  "language": "n/a",
  "category": "global_certification",
  "vendor": "벤더명",
  "exam": "시험코드",
  "level": 레벨번호,
  "unit": 유닛번호,
  "unit_title": "유닛 제목",
  "rule_summary_ko": "핵심 개념 요약",
  "examples": [...],
  "questions": [
    {
      "id": "고유ID",
      "type": "concept_matching_item | fill_blank",
      "code": "코드/시나리오 (선택)",
      "prompt_ko": "문제",
      "options": [...],
      "answer": 정답인덱스,
      "explanation_ko": "해설",
      "concept_tags": [...],
      "difficulty": "intro | practice | challenge"
    }
  ]
}
```

## 총계

| 벤더 | 자격증 | 레벨 | 문제 수 |
|---|---|---|---|
| AWS | CLF-C02 | 4 | 96 |
| AWS | SAA-C03 | 4 | 96 |
| Oracle | Java OCP | 7 | 168 |
| Oracle | SQL Associate | 3 | 72 |
| Oracle | PL/SQL Associate | 7 | 168 |
| Microsoft | AZ-900 | 3 | 72 |
| Google Cloud | Cloud Digital Leader | 6 | 144 |
| Cisco | CCNA 200-301 | 6 | 144 |
| LPI | LPIC-1 | 4 | 96 |
| LPI | LPIC-2 | 4 | 96 |
| **합계** | | | **1,152문제** |

모든 문제는 공식 시험 가이드·문서를 기준으로 검증되었으며, 가능한 경우(리눅스 명령어, SQL, Java, 네트워크 설정 등) 실제 실행 결과로 사실관계를 확인했습니다.
