"""test-arena 커리큘럼 정의.

단계: s1 예선(국내 1차) / s2 본선(국내 2차·최종 선발) / s3 국제(목차·학습 가이드 중심)
과목마다 TRACKS·CHAPTERS·TRACK_ORDER를 둔다 (아래 CURRICULUM).
- math: proof 증명의 기초 · alg 대수 · nt 정수론 · comb 조합 · geo 기하
- sci: 물리(phy-*)부터. 트랙의 group은 탐색 화면에서 과목 묶음 제목으로 쓴다.
레슨이 정의된 챕터만 available = True 가 된다 (build.py가 lessons/ 폴더를 보고 판단).
과목의 available은 열린 챕터가 하나라도 있으면 True로 빌드 때 정해진다.
"""

SUBJECTS = [
    {"id": "math", "title": "수학 올림피아드", "path": "KMO → IMO",
     "description": "대수·정수론·조합·기하와 증명 쓰기", "available": True},
    {"id": "sci", "title": "과학 올림피아드", "path": "KPhO·KChO·KBO·KESO·천문 → 국제",
     "description": "물리·화학·생물·지구과학·천문", "available": False},
    {"id": "info", "title": "정보 올림피아드", "path": "KOI → IOI",
     "description": "자료구조·알고리즘 설계·그래프", "available": False},
    {"id": "hum", "title": "인문·사회 경시", "path": "IPO·IOL·iGeo·IEO·역사",
     "description": "철학·언어학·지리·경제·역사 (개인 시험 부분)", "available": False},
]

STAGES = [
    {"no": 1, "id": "s1", "title": "S1 예선", "level": "국내 1차 시험 수준",
     "description": "교과를 넘어서는 경시 기초 도구와 증명 쓰기. 설명과 문제가 번갈아 나오는 레슨으로 배웁니다."},
    {"no": 2, "id": "s2", "title": "S2 본선", "level": "국내 2차·최종 선발 수준",
     "description": "서술형 증명 중심. 모범 증명과 채점 기준으로 스스로 채점합니다."},
    {"no": 3, "id": "s3", "title": "S3 국제", "level": "IMO 수준",
     "description": "목차와 학습 가이드 중심으로 독학합니다."},
]

TRACKS = {
    "proof": {"title": "증명의 기초", "description": "명제와 증명, 수학적 귀납법, 답안 쓰기"},
    "alg": {"title": "대수", "description": "부등식, 다항식, 수열, 함수방정식"},
    "nt": {"title": "정수론", "description": "약수·배수, 합동식, 소수, 디오판토스 방정식"},
    "comb": {"title": "조합", "description": "세기, 비둘기집 원리, 포함-배제, 그래프"},
    "geo": {"title": "기하", "description": "닮음, 원의 성질, 삼각형의 오심, 기하 변환"},
}

# 단계별 트랙과 챕터 제목. 커리큘럼(v1) 문서의 1장 표를 레슨 단위로 나눈 것.
CHAPTERS = {
    "s1": {
        "proof": ["명제와 증명", "수학적 귀납법", "답안 쓰기"],
        "alg": ["산술·기하 평균 부등식", "코시-슈바르츠 부등식", "다항식", "수열과 점화식"],
        "nt": ["약수·배수와 최대공약수", "합동식", "페르마 소정리", "소수와 소인수분해"],
        "comb": ["세기의 원리 심화", "비둘기집 원리", "포함-배제 원리", "점화식으로 세기"],
        "geo": ["닮음과 비", "원의 성질", "삼각형의 오심", "넓이와 삼각비"],
    },
    "s2": {
        "proof": ["귀납법·귀류법 심화", "답안 작성법"],
        "alg": ["함수방정식", "재배열·젠센 부등식", "SOS와 부등식 전략"],
        "nt": ["위수와 원시근", "디오판토스 방정식", "이차잉여"],
        "comb": ["그래프 이론", "불변량과 단조변량", "극단 원리"],
        "geo": ["체바·메넬라오스 정리", "근축과 방멱", "반전 기초"],
    },
    "s3": {
        "proof": ["출제 경향 분석", "모의고사"],
        "alg": ["다항식 고급", "복합 함수방정식"],
        "nt": ["LTE 보조정리", "p진 평가", "고급 디오판토스"],
        "comb": ["조합 기하", "확률적 방법", "게임"],
        "geo": ["사영기하", "복소수·좌표 기법", "고급 반전"],
    },
}

TRACK_ORDER = ["proof", "alg", "nt", "comb", "geo"]

# ---------------------------------------------------------------- 과학 올림피아드
# 물리 (KPhO → IPhO). 커리큘럼(v1) 문서 2장 표: S1 미적분 기반 역학·전자기 기초 /
# S2 강체·진동, 열역학, 광학, 오차 분석 / S3 상대론·양자 기초, 실험 문제
SCI_TRACKS = {
    "phy-kin": {"group": "물리", "title": "운동과 물리 수학", "description": "차원 분석, 미분·적분으로 보는 운동, 벡터와 포물선 운동"},
    "phy-dyn": {"group": "물리", "title": "역학", "description": "뉴턴 법칙, 에너지, 운동량, 원운동과 중력"},
    "phy-em": {"group": "물리", "title": "전자기 기초", "description": "전기장, 가우스 법칙과 전위, 회로, 자기장과 유도"},
    "phy-rigid": {"group": "물리", "title": "강체와 진동", "description": "강체의 회전, 단진동, 감쇠·강제 진동"},
    "phy-thermo": {"group": "물리", "title": "열역학", "description": "기체 분자 운동론, 열역학 법칙, 열기관"},
    "phy-optics": {"group": "물리", "title": "광학", "description": "기하 광학, 파동 광학"},
    "phy-exp": {"group": "물리", "title": "실험과 오차", "description": "측정과 오차 전파, 그래프 분석"},
    "phy-modern": {"group": "물리", "title": "현대 물리", "description": "특수 상대론, 양자 기초"},
    "phy-lab": {"group": "물리", "title": "실험 문제", "description": "실험 문제 접근법, 모의 실험 과제"},
    # 화학 (KChO → IChO). 문서 2장 표: S1 화학양론·평형·산염기 / S2 열역학·반응속도론, 유기 반응 메커니즘 /
    # S3 분광 분석, 배위화학, 실험 설계
    "chem-stoich": {"group": "화학", "competition": "KChO", "title": "화학양론", "description": "몰과 화학식, 반응의 양적 관계, 용액의 농도, 기체"},
    "chem-eq": {"group": "화학", "competition": "KChO", "title": "화학 평형", "description": "평형 상수, 르샤틀리에 원리, 용해 평형"},
    "chem-acid": {"group": "화학", "competition": "KChO", "title": "산과 염기", "description": "pH, 약산·약염기, 완충 용액, 적정"},
    "chem-thermo": {"group": "화학", "competition": "KChO", "title": "열역학과 반응 속도", "description": "엔탈피·엔트로피·자유 에너지, 속도 법칙"},
    "chem-org": {"group": "화학", "competition": "KChO", "title": "유기 반응", "description": "작용기, 치환·제거·첨가 반응과 메커니즘"},
    "chem-spec": {"group": "화학", "competition": "KChO", "title": "분광 분석", "description": "IR·NMR·질량 분석으로 구조 결정"},
    "chem-coord": {"group": "화학", "competition": "KChO", "title": "배위화학", "description": "착화합물의 구조, 결정장 이론"},
    "chem-lab": {"group": "화학", "competition": "KChO", "title": "실험 설계", "description": "정량 분석, 실험 설계와 오차"},
    # 생물 (KBO → IBO). 문서 2장 표: S1 세포·유전 심화 / S2 분자생물학, 생리학, 생태·진화 / S3 생물정보·통계, 실험 해석
    "bio-cell": {"group": "생물", "competition": "KBO", "title": "세포", "description": "세포 구조, 생체막과 수송, 효소, 세포 호흡과 광합성"},
    "bio-gen": {"group": "생물", "competition": "KBO", "title": "유전", "description": "세포 분열, 멘델 유전과 확장, 연관과 지도, 집단 유전"},
    "bio-mol": {"group": "생물", "competition": "KBO", "title": "분자생물학", "description": "DNA 복제, 전사·번역, 유전자 발현 조절, 생명공학 기법"},
    "bio-phys": {"group": "생물", "competition": "KBO", "title": "생리학", "description": "신경과 근육, 순환·호흡, 항상성, 식물 생리"},
    "bio-eco": {"group": "생물", "competition": "KBO", "title": "생태와 진화", "description": "개체군과 군집, 생태계, 자연 선택과 계통"},
    "bio-info": {"group": "생물", "competition": "KBO", "title": "생물정보와 통계", "description": "서열 분석, 계통수 작성, 생물 통계"},
    "bio-lab": {"group": "생물", "competition": "KBO", "title": "실험 해석", "description": "실험 설계와 대조군, 자료 해석"},
    # 지구과학 (KESO → IESO). 문서 2장 표: S1 지질·대기·해양 기초 / S2 지구계 상호작용, 자료 해석 /
    # S3 야외조사형·팀 과제는 결정 사항(온라인 구현 범위)에 따라 제외
    "earth-geo": {"group": "지구과학", "competition": "KESO", "title": "지질", "description": "광물과 암석, 지구 내부, 판 구조론, 지질 시대"},
    "earth-atmo": {"group": "지구과학", "competition": "KESO", "title": "대기", "description": "대기 구조와 복사, 안정도와 구름, 대기 순환, 날씨"},
    "earth-ocean": {"group": "지구과학", "competition": "KESO", "title": "해양", "description": "해수의 성질, 해류, 파도와 조석, 해양과 기후"},
    "earth-system": {"group": "지구과학", "competition": "KESO", "title": "지구계 상호작용", "description": "물질 순환, 에너지 수지, 기후 변화"},
    "earth-data": {"group": "지구과학", "competition": "KESO", "title": "자료 해석", "description": "지질·기상·해양 자료 읽기와 해석"},
    # 천문 (국내 천문 → IOAA). 문서 2장 표: S1 천구 좌표, 구면삼각법 / S2 항성 물리, 천체역학 /
    # S3 관측 자료 분석(실측 과제는 결정 사항(온라인 구현 범위)에 따라 제외)
    "astro-sphere": {"group": "천문", "competition": "KAO", "title": "천구와 좌표", "description": "천구 좌표계, 구면삼각법, 시간과 역법, 천체의 운동"},
    "astro-star": {"group": "천문", "competition": "KAO", "title": "항성 물리", "description": "등급과 거리, 항성의 복사, H-R도와 항성 진화"},
    "astro-mech": {"group": "천문", "competition": "KAO", "title": "천체역학", "description": "케플러 법칙, 궤도 운동과 에너지, 쌍성과 질량"},
    "astro-data": {"group": "천문", "competition": "KAO", "title": "관측 자료 분석", "description": "측광·분광 자료 분석, 관측 문제 접근법"},
}
SCI_CHAPTERS = {
    "s1": {
        "phy-kin": ["차원 분석과 어림", "미분으로 보는 운동", "적분으로 보는 운동", "벡터와 포물선 운동"],
        "phy-dyn": ["뉴턴 법칙과 자유물체도", "일과 에너지", "운동량과 충돌", "원운동과 만유인력"],
        "phy-em": ["전기력과 전기장", "가우스 법칙과 전위", "축전기와 직류 회로", "자기장과 전자기 유도"],
        "chem-stoich": ["몰과 화학식", "화학 반응식과 양적 관계", "용액의 농도", "기체"],
        "chem-eq": ["평형 상수", "르샤틀리에 원리", "기체 평형", "용해 평형"],
        "chem-acid": ["산과 염기의 정의", "pH와 약산·약염기", "완충 용액", "중화 적정"],
        "bio-cell": ["세포의 구조", "생체막과 물질 수송", "효소", "세포 호흡과 광합성"],
        "bio-gen": ["세포 분열과 염색체", "멘델 유전과 확장", "연관과 유전자 지도", "집단 유전"],
        "earth-geo": ["광물과 암석", "지구 내부와 지진파", "판 구조론", "지질 시대와 연대 측정"],
        "earth-atmo": ["대기의 구조와 복사", "대기 안정도와 구름", "대기 대순환과 바람", "기단과 날씨"],
        "earth-ocean": ["해수의 성질", "해류와 해양 순환", "파도와 조석", "해양과 기후"],
        "astro-sphere": ["천구와 좌표계", "구면삼각법", "시간과 역법", "천체의 일주·연주 운동"],
    },
    "s2": {
        "phy-rigid": ["강체의 회전", "단진동", "감쇠·강제 진동"],
        "phy-thermo": ["기체 분자 운동론", "열역학 법칙", "열기관과 엔트로피"],
        "phy-optics": ["기하 광학", "파동 광학"],
        "phy-exp": ["측정과 오차 전파", "그래프 분석과 선형화"],
        "chem-thermo": ["엔탈피와 헤스 법칙", "엔트로피와 자유 에너지", "반응 속도식", "활성화 에너지와 반응 메커니즘"],
        "chem-org": ["작용기와 명명", "치환과 제거 반응", "첨가 반응", "반응 메커니즘 쓰기"],
        "bio-mol": ["DNA 복제", "전사와 번역", "유전자 발현 조절", "생명공학 기법"],
        "bio-phys": ["신경과 근육", "순환과 호흡", "항상성과 내분비", "식물 생리"],
        "bio-eco": ["개체군과 군집", "생태계", "자연 선택과 진화", "계통과 분류"],
        "earth-system": ["물질 순환", "지구 에너지 수지", "엘니뇨와 기후 변화"],
        "earth-data": ["지질 자료 해석", "기상·해양 자료 해석"],
        "astro-star": ["등급과 거리", "항성의 복사와 스펙트럼", "H-R도와 항성 진화"],
        "astro-mech": ["케플러 법칙", "궤도 운동과 에너지", "쌍성과 질량 측정"],
    },
    "s3": {
        "phy-modern": ["특수 상대론", "양자 기초"],
        "phy-lab": ["실험 문제 접근법", "모의 실험 과제"],
        "chem-spec": ["적외선 분광법", "핵자기 공명", "질량 분석"],
        "chem-coord": ["착화합물의 구조와 이성질체", "결정장 이론"],
        "chem-lab": ["정량 분석", "실험 설계와 오차"],
        "bio-info": ["서열 분석", "계통수 작성", "생물 통계"],
        "bio-lab": ["실험 설계와 대조군", "자료 해석"],
        "astro-data": ["측광·분광 자료 분석", "관측 문제 접근법"],
    },
}
SCI_ORDER = ["phy-kin", "phy-dyn", "phy-em", "phy-rigid", "phy-thermo", "phy-optics", "phy-exp", "phy-modern", "phy-lab",
             "chem-stoich", "chem-eq", "chem-acid", "chem-thermo", "chem-org", "chem-spec", "chem-coord", "chem-lab",
             "bio-cell", "bio-gen", "bio-mol", "bio-phys", "bio-eco", "bio-info", "bio-lab",
             "earth-geo", "earth-atmo", "earth-ocean", "earth-system", "earth-data",
             "astro-sphere", "astro-star", "astro-mech", "astro-data"]

# ---------------------------------------------------------------- 정보 (KOI → IOI)
# 문서 3장 표: 분야 5개 × S1~S3. 수학처럼 트랙(분야)이 단계마다 이어진다.
# 채점은 1단계로 이론 중심: 코드 읽기·연산 횟수·복잡도·정당성 서술을 다루고 코드 제출은 외부 저지로 안내.
INFO_TRACKS = {
    "basic": {"title": "기초", "description": "시간복잡도, 정렬·이분 탐색, 완전 탐색, 정당성 증명"},
    "ds": {"title": "자료구조", "description": "스택·큐·덱, 우선순위 큐, 세그먼트 트리, 유니온 파인드"},
    "design": {"title": "알고리즘 설계", "description": "그리디, 동적 계획법, 분할 정복"},
    "graph": {"title": "그래프", "description": "BFS·DFS, 최단 경로, 최소 신장 트리, 위상 정렬"},
    "mathstr": {"title": "수학·문자열", "description": "정수론 기초, 조합론, 문자열 알고리즘"},
}
INFO_CHAPTERS = {
    "s1": {
        "basic": ["시간복잡도", "정렬", "이분 탐색", "완전 탐색"],
        "ds": ["스택", "큐와 덱", "우선순위 큐"],
        "design": ["그리디", "동적 계획법 입문", "동적 계획법 유형"],
        "graph": ["그래프 표현", "BFS와 DFS", "최단 경로"],
        "mathstr": ["소수와 약수", "GCD와 모듈러 연산"],
    },
    "s2": {
        "basic": ["정당성 증명", "불변식과 귀납"],
        "ds": ["세그먼트 트리", "유니온 파인드"],
        "design": ["분할 정복", "DP 최적화"],
        "graph": ["최소 신장 트리", "위상 정렬", "강한 연결 요소"],
        "mathstr": ["조합론", "KMP", "해싱"],
    },
    "s3": {
        "basic": ["출제 경향 분석", "모의고사"],
        "ds": ["지연 전파", "영속 자료구조"],
        "design": ["볼록 껍질 트릭", "고급 DP"],
        "graph": ["네트워크 플로우", "이분 매칭"],
        "mathstr": ["계산 기하", "접미사 배열"],
    },
}
INFO_ORDER = ["basic", "ds", "design", "graph", "mathstr"]

# ---------------------------------------------------------------- 인문·사회 경시
# 문서 4장 표: 철학(IPO)·언어학(IOL)·지리(iGeo)·경제(IEO)·역사. 팀 과제·야외조사·토론은 제외하고 개인 시험 부분만.
# 대부분 서술형이라 자가 채점(모범 답안 + 채점 기준)이 중심이고, 판별·분석 문항은 번호나 빈칸으로 자동 채점한다.
HUM_TRACKS = {
    "phil": {"title": "철학", "competition": "IPO", "description": "논증과 오류, 윤리학·인식론·정치철학 에세이"},
    "ling": {"title": "언어학", "competition": "IOL", "description": "낯선 언어의 음운·형태·통사·문자 체계 퍼즐"},
    "geo": {"title": "지리", "competition": "iGeo", "description": "지도·사진·통계 자료 해석과 서술형"},
    "econ": {"title": "경제", "competition": "IEO", "description": "미시·거시·금융 기초와 서술형"},
    "hist": {"title": "역사", "competition": "역사 탐구·에세이", "description": "사료 읽기, 탐구 보고서, 역사 에세이"},
}
HUM_CHAPTERS = {
    "s1": {
        "phil": ["논증의 구조", "연역 논증", "귀납 논증", "비형식적 오류"],
        "ling": ["형태 분석", "어순과 일치", "수 체계"],
        "geo": ["지도 읽기", "사진 자료 해석", "통계 자료 해석"],
        "econ": ["미시경제 기초", "거시경제 기초", "금융 기초"],
        "hist": ["사료 읽기", "탐구 주제 설정"],
    },
    "s2": {
        "phil": ["철학 에세이의 구조", "윤리학 주제", "인식론 주제", "정치철학 주제"],
        "ling": ["음운 퍼즐", "형태 퍼즐", "통사 퍼즐", "문자 체계 퍼즐"],
        "geo": ["자료 기반 서술형"],
        "econ": ["경제·금융 서술형"],
        "hist": ["한국사 사료 분석 탐구 보고서"],
    },
    "s3": {
        "phil": ["외국어 철학 에세이", "4시간 실전 연습"],
        "ling": ["개인전 실전"],
        "geo": ["영어 서술형·멀티미디어 실전"],
        "econ": ["객관식·서술형 실전"],
        "hist": ["영어 역사 에세이"],
    },
}
HUM_ORDER = ["phil", "ling", "geo", "econ", "hist"]

# 과목별 묶음. levels는 단계별 수준 문구, competition은 레슨 JSON의 대회 태그,
# work는 서술형 문항 이름(math: 증명, sci: 풀이).
CURRICULUM = {
    "math": {"tracks": TRACKS, "chapters": CHAPTERS, "order": TRACK_ORDER, "competition": "KMO", "work": "증명",
             "levels": {"s3": "IMO 수준"}},
    "sci": {"tracks": SCI_TRACKS, "chapters": SCI_CHAPTERS, "order": SCI_ORDER, "competition": "KPhO", "work": "풀이",
            "levels": {"s3": "IPhO 등 국제 대회 수준"}},
    "info": {"tracks": INFO_TRACKS, "chapters": INFO_CHAPTERS, "order": INFO_ORDER, "competition": "KOI", "work": "풀이",
             "levels": {"s3": "IOI 수준"}},
    "hum": {"tracks": HUM_TRACKS, "chapters": HUM_CHAPTERS, "order": HUM_ORDER, "competition": "IPO", "work": "답안",
            "levels": {"s3": "국제 대회 수준"}},
}
