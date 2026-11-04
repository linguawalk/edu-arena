# Lingua Arena — 전체 커리큘럼 설계서
**Platform:** lingua-arena.org  
**Target:** 한국인 외국어 학습자  
**Framework:** CEFR A1–C2 (언어 5종) + TOEIC 별도  
**Philosophy:** "언어도 훈련이다 — 매일 조금씩, 퍼즐처럼"  
**Last updated:** 2026-06

---

## 1. 전체 규모 요약

| 분야 | 레벨 | 유닛 수 | 문제 수 |
|------|------|---------|---------|
| 영어 (English) | A1–C2 (6단계) | 120 | 3,000 |
| 일본어 (Japanese) | A1–C2 (6단계) | 120 | 3,000 |
| 중국어 (Chinese) | A1–C2 (6단계) | 120 | 3,000 |
| 한자 (Hanja) | A1–C2 (6단계) | 120 | 3,000 |
| 프랑스어 (French) | A1–C2 (6단계) | 120 | 3,000 |
| TOEIC | Part 1–7 문제은행 | 7 파트 | 2,100 |
| TOEIC | 실전 모의고사 | 10회 | 2,000 |
| **합계** | | **~817** | **~19,100** |

> 각 레벨 6단계 × 유닛 20개 × 문제 25개 = 레벨당 500문제 / 언어당 3,000문제

---

## 2. CEFR 레벨 구조 (5개 언어 공통)

| 레벨 | 명칭 | 한국어 설명 | 유닛 수 | 문제 수 |
|------|------|------------|---------|---------|
| A1 | Beginner | 기초 생존 표현 | 20 | 500 |
| A2 | Elementary | 일상 의사소통 | 20 | 500 |
| B1 | Intermediate | 친숙한 주제 표현 | 20 | 500 |
| B2 | Upper-Intermediate | 복잡한 주제 이해 | 20 | 500 |
| C1 | Advanced | 유창하고 자연스러운 표현 | 20 | 500 |
| C2 | Mastery | 원어민 수준 정확성 | 20 | 500 |

**유닛 구성 원칙**
- 유닛 1개 = 하나의 교재 챕터처럼 구성
- 유닛 내 학습 흐름: 어휘 → 문법 → 표현 → 연습 → 종합
- 유닛당 문제 25개, 난이도 점진적 상승
- 설명은 한국어/해당 언어 이중 제공

---

## 3. 퍼즐 유형 (전 언어 공통)

| 유형 | 설명 | 적용 레벨 |
|------|------|----------|
| `multiple_choice` | 4지선다 객관식 | A1–C2 |
| `fill_in_blank` | 빈칸 채우기 (선택) | A1–B2 |
| `word_order` | 단어 순서 배열 (드래그) | A1–B1 |
| `matching` | 단어-의미 짝 맞추기 | A1–A2 |
| `error_correction` | 문장 오류 찾기·수정 | A2–C2 |
| `reading` | 지문 + 독해 문제 | A2–C2 |
| `gap_text` | 연속 빈칸 (지문 내) | B1–C2 |
| `sentence_reorder` | 문장 단락 순서 배열 | B1–C1 |
| `dictation` | 듣기 후 받아쓰기 (Web Speech API) | B1–C2 |
| `speaking_prompt` | 말하기 응답 (Speech Recognition API) | A2–C2 |

---

## 4. 영어 (English) 커리큘럼

### A1 — Beginner (기초 생존 영어)
**핵심 문법:** be동사, 관사, 단복수, 인칭대명사, 단순현재, 의문문 기초, There is/are  
**핵심 어휘:** 200단어

| 유닛 | 주제 | 대표 표현 |
|------|------|----------|
| U01 | Greetings & Introductions | Hello, My name is, Nice to meet you |
| U02 | Numbers & Time | 1–100, What time is it? |
| U03 | Colors & Shapes | red, blue, big, small, round |
| U04 | Family & People | mother, father, friend, young, old |
| U05 | Food & Drink | eat, drink, hungry, water, bread |
| U06 | Places & Directions | school, home, left, right, near |
| U07 | Days & Routines | Monday–Sunday, morning, every day |
| U08 | Body & Health | head, hand, sick, feel, doctor |
| U09 | Animals & Nature | cat, dog, tree, big, small |
| U10 | Classroom & Objects | pen, book, table, open, close |
| U11 | Shopping Basics | how much, cheap, buy, money |
| U12 | Weather Basics | sunny, rainy, cold, warm, today |
| U13 | Feelings & Emotions | happy, sad, angry, tired, great |
| U14 | My Home | bedroom, kitchen, clean, big |
| U15 | Transportation Basics | bus, car, walk, take, go |
| U16 | Hobbies Basics | like, watch, play, read, music |
| U17 | Months & Seasons | January–December, spring, winter |
| U18 | Jobs & Work Basics | teacher, doctor, work, job |
| U19 | Sports & Activities | run, swim, play, ball, team |
| U20 | A1 종합 복습 | Mixed review — all A1 topics |

### A2 — Elementary (일상 의사소통)
**핵심 문법:** 단순과거, 미래(will/going to), 조동사(can/must/should), 현재진행, 비교급/최상급, 접속사 기초  
**핵심 어휘:** +300단어 (누적 500)

| 유닛 | 주제 |
|------|------|
| U01 | Shopping & Prices |
| U02 | Transport & Travel |
| U03 | Weather & Seasons |
| U04 | Hobbies & Free Time |
| U05 | Jobs & Daily Routines |
| U06 | Restaurants & Food |
| U07 | Health & Lifestyle |
| U08 | Home & Furniture |
| U09 | Feelings & Opinions |
| U10 | Short Texts: Email & Messages |
| U11 | Past Experiences |
| U12 | Future Plans |
| U13 | Comparing Things |
| U14 | Asking for Help |
| U15 | Invitations & Arrangements |
| U16 | Technology Basics |
| U17 | Culture & Celebrations |
| U18 | At the Doctor |
| U19 | Describing People & Places |
| U20 | A2 종합 복습 |

### B1 — Intermediate (친숙한 주제 표현)
**핵심 문법:** 현재완료(경험/결과), 수동태, 조건문 1형식, 관계대명사, 간접화법, 부정사/동명사 구별  
**핵심 어휘:** +400단어 (누적 900)

| 유닛 | 주제 |
|------|------|
| U01 | Travel Experiences |
| U02 | Work & Career |
| U03 | Environment & Nature |
| U04 | Technology & Daily Life |
| U05 | Health & Medicine |
| U06 | Culture & Traditions |
| U07 | News & Media |
| U08 | Relationships |
| U09 | Education & Learning |
| U10 | Money & Economy |
| U11 | Entertainment |
| U12 | Social Issues |
| U13 | Science & Discovery |
| U14 | Sports & Competition |
| U15 | Food & Cuisine (Global) |
| U16 | Describing Processes |
| U17 | Reported Speech Practice |
| U18 | Reading: Short Articles |
| U19 | Listening: Conversations |
| U20 | B1 종합 복습 |

### B2 — Upper-Intermediate (복잡한 주제 이해)
**핵심 문법:** 가정법 2·3형식, 혼합가정법, 분사구문, 강조구문, 도치, 관계부사, 논문/에세이 표현  
**핵심 어휘:** +500단어 (누적 1,400)

| 유닛 | 주제 |
|------|------|
| U01 | Society & Inequality |
| U02 | Science & Innovation |
| U03 | Global Issues |
| U04 | Arts & Creativity |
| U05 | Law & Ethics |
| U06 | Business & Negotiation |
| U07 | History & Politics |
| U08 | Psychology & Behavior |
| U09 | Urban Life |
| U10 | Sustainability |
| U11 | Academic Reading I |
| U12 | Academic Reading II |
| U13 | Conditional Sentences Practice |
| U14 | Passive Voice Advanced |
| U15 | Essay Writing Expressions |
| U16 | Debate & Argumentation |
| U17 | Complex Listening I |
| U18 | Complex Listening II |
| U19 | Vocabulary in Context |
| U20 | B2 종합 복습 |

### C1 — Advanced (유창하고 자연스러운 표현)
**핵심:** 관용어, 콜로케이션, 학술어, 레지스터 전환, 추측 조동사, 담화 표지  
**핵심 어휘:** +700단어 (누적 2,100)

| 유닛 | 주제 |
|------|------|
| U01 | Idioms & Phrasal Verbs I |
| U02 | Idioms & Phrasal Verbs II |
| U03 | Academic Collocations |
| U04 | Debate & Critical Thinking |
| U05 | Complex Narratives |
| U06 | Satire & Humor |
| U07 | Legal & Formal Writing |
| U08 | Media Literacy |
| U09 | Cross-cultural Communication |
| U10 | Nuance & Implication |
| U11 | Modal Verbs (Speculation) |
| U12 | Discourse Markers Advanced |
| U13 | Register Switching |
| U14 | Long Listening: Lectures |
| U15 | Long Reading: Academic Texts |
| U16 | Summarizing & Paraphrasing |
| U17 | Spoken Fluency Practice |
| U18 | Writing: Reports & Essays |
| U19 | Error Analysis (Advanced) |
| U20 | C1 종합 복습 |

### C2 — Mastery (원어민 수준 정확성)
**핵심:** 수사법, 문학 어휘, 모호한 텍스트 해석, 번역 뉘앙스, 즉흥 발화 정확성  
**핵심 어휘:** +900단어 (누적 3,000)

| 유닛 | 주제 |
|------|------|
| U01 | Rhetorical Devices |
| U02 | Literary Vocabulary |
| U03 | Poetry & Ambiguous Texts |
| U04 | Satire & Irony |
| U05 | Translation Nuance (EN↔KO) |
| U06 | Authentic Editorials |
| U07 | Authentic Speeches |
| U08 | Spontaneous Speaking |
| U09 | Precision & Style |
| U10–U20 | Mixed Authentic Texts & Mastery Practice |

---

## 5. 일본어 (Japanese) 커리큘럼

### 레벨 대응 (JLPT 참조)
| CEFR | JLPT 참조 | 설명 |
|------|-----------|------|
| A1 | N5 수준 | 히라가나·가타카나, 기초 어휘·문법 |
| A2 | N4 수준 | 일상 회화, 기초 한자 100자 |
| B1 | N3 수준 | 친숙한 주제, 한자 300자 |
| B2 | N2 수준 | 복잡한 주제, 한자 1,000자 |
| C1 | N1 수준 | 고급 표현, 한자 2,000자 |
| C2 | N1+ | 원어민 수준, 전문 어휘 |

### A1 유닛 구성
| 유닛 | 주제 | 핵심 내용 |
|------|------|----------|
| U01 | 히라가나 I | あ행–な행, 기본 발음 |
| U02 | 히라가나 II | は행–ん, 탁음·반탁음 |
| U03 | 가타카나 I | ア행–ナ행, 외래어 기초 |
| U04 | 가타카나 II | ハ행–ン, 장음·촉음 |
| U05 | 인사와 자기소개 | はじめまして、よろしく |
| U06 | 숫자와 날짜 | 一二三、何日、何曜日 |
| U07 | 이것·저것·그것 | これ・それ・あれ・どれ |
| U08 | 가족과 사람 | 母・父・友達、～さん |
| U09 | 음식과 식사 | 食べる・飲む、おいしい |
| U10 | 장소와 방향 | 学校・家、右・左・近い |
| U11 | 시간 표현 | ～時、今・朝・毎日 |
| U12 | い형용사 | 大きい・小さい・高い・安い |
| U13 | な형용사 | きれい・元気・好き・嫌い |
| U14 | る동사 활용 | 食べます・見ます |
| U15 | う동사 활용 | 飲みます・書きます |
| U16 | 조사 기초 | は・が・を・に・で・と |
| U17 | 쇼핑 | いくら？・ください・～円 |
| U18 | 날씨·계절 | 晴れ・雨・寒い・暑い |
| U19 | 교실과 학교 | 先生・学生・授業・宿題 |
| U20 | A1 종합 복습 | Mixed review |

*(A2–C2: 영어와 동일한 주제 프레임, 일본어 특화 문법 항목으로 구성)*

---

## 6. 중국어 (Chinese) 커리큘럼

### 레벨 대응 (HSK 참조)
| CEFR | HSK 참조 | 설명 |
|------|----------|------|
| A1 | HSK 1 수준 | 병음, 성조, 기초 150단어 |
| A2 | HSK 2 수준 | 일상 회화, 300단어 |
| B1 | HSK 3–4 수준 | 친숙한 주제, 600단어 |
| B2 | HSK 5 수준 | 복잡한 주제, 1,200단어 |
| C1 | HSK 6 수준 | 고급 표현, 2,500단어 |
| C2 | HSK 6+ | 원어민 수준, 전문 어휘 |

### A1 유닛 구성
| 유닛 | 주제 | 핵심 내용 |
|------|------|----------|
| U01 | 병음 I | 성모 b/p/m/f/d/t/n/l |
| U02 | 병음 II | 성모 g/k/h/j/q/x/zh/ch/sh/r/z/c/s |
| U03 | 성조 연습 | 1·2·3·4성, 경성, 성조 변화 |
| U04 | 인사와 소개 | 你好、我叫、很高兴认识你 |
| U05 | 숫자와 날짜 | 一–十、月、日、星期 |
| U06 | 이것·저것 | 这・那・什么・哪 |
| U07 | 가족 | 妈妈・爸爸・哥哥・朋友 |
| U08 | 음식 | 吃・喝・好吃・米饭・面条 |
| U09 | 장소 | 学校・家・左・右・近 |
| U10 | 시간 | 现在几点？・早上・今天 |
| U11 | 형용사 기초 | 大・小・多・少・好・坏 |
| U12 | 동사 기초 | 是・有・去・来・看・听 |
| U13 | 쇼핑 | 多少钱？・便宜・贵・买 |
| U14 | 날씨 | 天气・晴・雨・冷・热 |
| U15 | 교통 | 公共汽车・地铁・走路 |
| U16 | 색깔·모양 | 红・蓝・白・大・圆 |
| U17 | 신체·건康 | 头・手・生病・医生 |
| U18 | 취미 | 喜欢・看书・听音乐 |
| U19 | 교실 | 老师・学生・作业・书 |
| U20 | A1 종합 복습 | Mixed review |

---

## 7. 한자 (Hanja) 커리큘럼

### 레벨 대응 (한자능력검정시험 참조)
| CEFR | 검정 참조 | 한자 수 | 설명 |
|------|-----------|---------|------|
| A1 | 8급·7급 수준 | 150자 | 일상 기초 한자, 부수 이해 |
| A2 | 6급·5급 수준 | 500자 | 생활 한자, 단어 형성 |
| B1 | 4급·3급 수준 | 1,000자 | 중학 교과 한자 |
| B2 | 2급 수준 | 1,817자 | 고등 교과, 신문 한자 |
| C1 | 1급 수준 | 3,500자 | 고전·문어체 |
| C2 | 특급 수준 | 5,000자+ | 전문·역사 문헌 |

### 한자 특화 퍼즐 유형
| 유형 | 설명 |
|------|------|
| `stroke_order` | 획순 순서 배열 |
| `radical_match` | 부수 짝 맞추기 |
| `meaning_match` | 훈·음 연결 |
| `compound_build` | 한자 조합해 단어 만들기 |
| `reading_pick` | 문장 속 한자 독음 선택 |
| `context_use` | 문장 속 올바른 한자 선택 |

### A1 유닛 구성
| 유닛 | 주제 | 대표 한자 |
|------|------|----------|
| U01 | 부수 이해 I | 人·口·手·木·水 |
| U02 | 부수 이해 II | 日·月·火·土·金 |
| U03 | 숫자 한자 | 一二三四五六七八九十百千萬 |
| U04 | 방향·위치 | 上下左右中前後東西南北 |
| U05 | 자연 | 山川海空雨雪花草 |
| U06 | 사람과 관계 | 父母兄弟姉妹友人先生 |
| U07 | 신체 | 頭顔目耳口手足心 |
| U08 | 시간 | 年月日時分今昨明 |
| U09 | 색깔 | 白黑赤靑黃綠 |
| U10 | 크기·수량 | 大小多少長短高低 |
| U11 | 동작 동사 | 見聞食飮行來去 |
| U12 | 형용사 | 善惡美醜新古强弱 |
| U13 | 학교·학습 | 學校敎室書冊問答 |
| U14 | 생활·집 | 家門室內外窓庭 |
| U15 | 음식 | 食飯肉魚菜米茶 |
| U16 | 나라·지명 | 韓國中國日本美國 |
| U17 | 계절·날씨 | 春夏秋冬晴曇風雨 |
| U18 | 직업 | 王臣民工農商醫師 |
| U19 | 한자어 단어 I | 學校·道路·病院·電話 |
| U20 | A1 종합 복습 | Mixed review |

---

## 8. 프랑스어 (French) 커리큘럼

### 레벨 대응 (DELF/DALF 참조)
| CEFR | 시험 참조 | 설명 |
|------|-----------|------|
| A1 | DELF A1 | 기초 인사, 발음, 기본 문장 |
| A2 | DELF A2 | 일상 회화, 기본 동사 활용 |
| B1 | DELF B1 | 친숙한 주제, 시제 심화 |
| B2 | DELF B2 | 복잡한 주제, 접속법 |
| C1 | DALF C1 | 고급 표현, 학술 텍스트 |
| C2 | DALF C2 | 원어민 수준, 문학 텍스트 |

### A1 유닛 구성
| 유닛 | 주제 | 핵심 내용 |
|------|------|----------|
| U01 | 알파벳과 발음 | alphabet, accent marks (é è ê ç) |
| U02 | 인사와 소개 | Bonjour, Je m'appelle, Enchanté(e) |
| U03 | 숫자와 날짜 | un–vingt, les jours, les mois |
| U04 | 관사 | le/la/les, un/une/des |
| U05 | être 동사 | Je suis, Tu es, Il/Elle est |
| U06 | avoir 동사 | J'ai, Tu as, Il a |
| U07 | 가족 | mère, père, frère, sœur, ami(e) |
| U08 | 색깔과 형용사 | rouge, bleu, grand, petit |
| U09 | 음식과 식사 | manger, boire, le pain, l'eau |
| U10 | 장소와 방향 | école, maison, à gauche, près de |
| U11 | 시간 표현 | Quelle heure est-il? le matin |
| U12 | -er 동사 규칙 활용 | parler, aimer, habiter |
| U13 | 의문문 기초 | Qu'est-ce que c'est? / Est-ce que...? |
| U14 | 쇼핑 | Combien ça coûte? / Je voudrais |
| U15 | 날씨 | Il fait beau/froid, Il pleut |
| U16 | 교통 | le bus, le métro, aller |
| U17 | 취미 | aimer + infinitif, la musique |
| U18 | 신체와 건강 | la tête, la main, je suis malade |
| U19 | 학교와 교실 | le professeur, l'élève, le cahier |
| U20 | A1 종합 복습 | Mixed review |

---

## 9. TOEIC 커리큘럼

> TOEIC은 CEFR 레벨 체계와 별도로 운영합니다.  
> 구성: **파트별 문제은행** + **실전 모의고사 10회**

### 9-1. 파트별 문제은행

| Part | 유형 | 문제 형식 | 목표 문제 수 |
|------|------|----------|------------|
| Part 1 | 사진 묘사 | 사진 보고 4개 문장 중 선택 | 300 |
| Part 2 | 질의 응답 | 질문 듣고 3개 중 적절한 응답 선택 | 300 |
| Part 3 | 짧은 대화 | 대화 듣고 3문제 답변 | 300 |
| Part 4 | 짧은 담화 | 담화 듣고 3문제 답변 | 300 |
| Part 5 | 단문 빈칸 | 문법·어휘 단문 빈칸 채우기 | 300 |
| Part 6 | 장문 빈칸 | 지문 내 4개 빈칸 채우기 | 300 |
| Part 7 | 독해 | 단일/복수 지문 독해 | 300 |
| **합계** | | | **2,100** |

### 9-2. 실전 모의고사 10회

| 회차 | 구성 | 문제 수 | 난이도 |
|------|------|---------|--------|
| 제1회 | LC 100 + RC 100 | 200 | 기초 (600점대 목표) |
| 제2회 | LC 100 + RC 100 | 200 | 기초 |
| 제3회 | LC 100 + RC 100 | 200 | 중급 (700점대 목표) |
| 제4회 | LC 100 + RC 100 | 200 | 중급 |
| 제5회 | LC 100 + RC 100 | 200 | 중급 |
| 제6회 | LC 100 + RC 100 | 200 | 고급 (800점대 목표) |
| 제7회 | LC 100 + RC 100 | 200 | 고급 |
| 제8회 | LC 100 + RC 100 | 200 | 고급 |
| 제9회 | LC 100 + RC 100 | 200 | 최고급 (900점대 목표) |
| 제10회 | LC 100 + RC 100 | 200 | 최고급 |
| **합계** | | **2,000** | |

### 9-3. TOEIC 파트별 전략 유닛

| 유닛 | 내용 |
|------|------|
| T-U01 | Part 1 공략: 사진 묘사 핵심 패턴 |
| T-U02 | Part 2 공략: 의문사별 응답 전략 |
| T-U03 | Part 3 공략: 대화 유형 분석 |
| T-U04 | Part 4 공략: 담화 유형 분석 |
| T-U05 | Part 5 공략: 품사·시제·어휘 전략 |
| T-U06 | Part 6 공략: 흐름 파악 전략 |
| T-U07 | Part 7 공략: 단일지문 속독 전략 |
| T-U08 | Part 7 공략: 복수지문 연계 전략 |
| T-U09 | TOEIC 빈출 어휘 1000 |
| T-U10 | TOEIC 빈출 표현·콜로케이션 |

---

## 10. Question ID 스키마

```
{lang}_{level}_{unit}_{question}

예시:
en_a1_u01_q001        → 영어 A1 Unit01 첫 번째 문제
ja_b1_u05_q012        → 일본어 B1 Unit05 12번 문제
zh_a2_u03_q007        → 중국어 A2 Unit03 7번 문제
hj_a1_u04_q020        → 한자 A1 Unit04 20번 문제
fr_c1_u11_q003        → 프랑스어 C1 Unit11 3번 문제
toeic_p5_q045         → TOEIC Part5 45번 문제
toeic_mock01_lc_q023  → 모의고사 1회 LC 23번
```

| 코드 | 언어 |
|------|------|
| `en` | English |
| `ja` | Japanese |
| `zh` | Chinese |
| `hj` | Hanja |
| `fr` | French |
| `toeic` | TOEIC |

---

## 11. Question JSON 스키마

```json
{
  "id": "en_a1_u01_q001",
  "type": "multiple_choice",
  "prompt": "What does 'Nice to meet you' mean?",
  "choices": ["만나서 반갑습니다", "잘 지내세요?", "안녕히 가세요", "감사합니다"],
  "answer": 0,
  "difficulty": 1,
  "tags": ["greeting", "social", "a1"],
  "explanation": {
    "en": "A common phrase used when meeting someone for the first time.",
    "ko": "처음 만날 때 쓰는 인사 표현입니다."
  },
  "media": null
}
```

**difficulty 척도:** 1(매우 쉬움) – 5(매우 어려움)  
**media:** `null` 또는 `{ "type": "audio", "src": "path/to/file" }` 형태

---

## 12. 폴더 구조 (GitHub 저장소)

```
lingua-arena/
├── index.html
├── docs/
│   ├── curriculum.md          ← 이 파일
│   ├── roadmap.md
│   └── schema.md
├── data/
│   ├── en/
│   │   ├── a1/
│   │   │   ├── u01.json … u20.json
│   │   ├── a2/ … c2/
│   ├── ja/
│   │   ├── a1/ … c2/
│   ├── zh/
│   │   ├── a1/ … c2/
│   ├── hj/
│   │   ├── a1/ … c2/
│   ├── fr/
│   │   ├── a1/ … c2/
│   └── toeic/
│       ├── parts/
│       │   ├── p1.json … p7.json
│       └── mock/
│           ├── mock01.json … mock10.json
├── assets/
│   ├── css/
│   └── js/
└── README.md
```

---

## 13. Phase별 제작 로드맵

| Phase | 내용 | 목표 문제 수 | 누적 |
|-------|------|------------|------|
| **Phase 1** | 영어 A1·A2 완성 + 플레이어 MVP | 1,000 | 1,000 |
| **Phase 2** | 영어 B1·B2 + TOEIC Part 5·7 문제은행 | 1,200 | 2,200 |
| **Phase 3** | 일본어 A1·A2 + 한자 A1·A2 | 2,000 | 4,200 |
| **Phase 4** | 중국어 A1·A2 + 프랑스어 A1·A2 | 2,000 | 6,200 |
| **Phase 5** | TOEIC 모의고사 10회 완성 | 2,000 | 8,200 |
| **Phase 6** | 전 언어 B1–C2 완성 | 9,500 | 19,100 |

---

*Part of the Arena Family: mind-arena.org · code-arena.org · lingua-arena.org*
