"""인문·사회 S3 · 지리 · 챕터 1 영어 서술형·멀티미디어 실전 (학습 가이드, 자체 제작 문항).
iGeo의 시험 구성(영어 서술형 시험, 사진·지도·영상 자료를 보는 멀티미디어 시험, 야외 조사)은 널리 알려진 내용이며, 이 사이트에서는
야외 조사를 다루지 않는다. 자료의 수치는 연습용 가상 자료다. 세부 규정은 공식 누리집에서 확인해야 한다."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lesson_kit import X, E, N, PR, C

DOMAIN = ["지리", "서술형", "영어 서술형·멀티미디어"]

POP = """(Fictional data) Population of Country Z by age group (%)
Age group      1990    2020
0-14            34      18
15-64           61      64
65+              5      18"""

GUIDE = {"title": "영어 서술형·멀티미디어 실전", "minutes": 150, "screens": [
    X("iGeo 시험의 구성", [
        "국제 지리 올림피아드(iGeo)는 영어 서술형 시험(Written Response Test), 사진·지도·그래프·영상을 보고 답하는 멀티미디어 시험(Multimedia Test), 야외 조사(Fieldwork Exercise)로 이루어집니다. 이 사이트에서는 온라인으로 하기 어려운 야외 조사는 다루지 않습니다.",
        "서술형 시험은 모두 영어로 답합니다. S2 '자료 기반 서술형'에서 배운 명령어(기술, 설명, 비교, 평가)와 수치 인용을 영어로 옮기는 것이 이 가이드의 핵심입니다.",
        "멀티미디어 시험은 짧은 시간에 많은 문항을 풀므로, 지도의 축척·방위·등고선, 시차, 기후 그래프, 경관 사진의 단서를 빠르게 읽는 연습이 필요합니다.",
    ], "intro"),
    X("영어 명령어와 답안 표현", [
        "Describe: 보이는 패턴과 수치를 쓴다('The proportion of people aged 65+ increased from 5% in 1990 to 18% in 2020'). Explain: 원인과 과정을 쓴다('This is mainly due to …', 'As a result, …'). Compare: 같은 기준으로 공통점과 차이점을 쓴다('Whereas A …, B …').",
        "Suggest: 자료로 단정할 수 없는 가능한 이유나 방안을 쓴다('One possible reason is …'). Evaluate / Assess: 장단점과 이해관계자를 따진 뒤 판단한다('On balance, …', 'To a large extent …').",
        "수치는 단위와 함께 쓰고, 비율의 차이는 percentage points로 씁니다('an increase of 13 percentage points', 'rose by 260%'). 점수는 대개 '요점 하나에 1점'이므로, 요점을 문단 안에 분명히 나누어 쓰세요.",
    ]),
    N("'Suggest'로 시작하는 문항에서 요구하는 것으로 가장 알맞은 것은? ① 자료의 수치를 그대로 옮기기 ② 자료로 단정할 수 없는 가능한 이유나 방안 제시 ③ 용어의 정의 ④ 지도 그리기", 2,
      "suggest는 '제안하다, 시사하다'입니다.",
      "'Suggest'는 자료만으로 확정할 수 없는 가능한 설명이나 방안을 근거와 함께 제시하라는 명령어입니다.\n수치 옮기기는 'Describe', 정의는 'Define'의 몫입니다.\n답은 2입니다."),
    C(E("가상 나라 Z의 인구 자료로 'Describe the changes in the age structure of Country Z between 1990 and 2020.'에 대한 답을 영어로 쓰세요.", [
        "'The proportion of children aged 0-14 fell sharply from 34% in 1990 to 18% in 2020, a decrease of 16 percentage points.'",
        "'Meanwhile, the proportion of elderly people aged 65+ more than tripled, from 5% to 18%, so that in 2020 there were as many elderly people as children.'",
        "'The working-age population (15-64) remained relatively stable, rising slightly from 61% to 64%. Overall, the population structure shows rapid ageing.'",
    ], "수치 + 변화량 + 전체 경향"), POP),
    C(N("나라 Z의 노년 부양비(65세 이상 ÷ 15~64세 × 100)는 2020년에 얼마인가요? (소수 첫째 자리까지)", 28.1,
        "18 ÷ 64 × 100입니다.",
        "2020년 65세 이상은 18%, 15~64세는 64%입니다.\n노년 부양비는 18 ÷ 64 × 100 ≈ 28.13입니다.\n소수 첫째 자리까지 28.1입니다(1990년 5 ÷ 61 × 100 ≈ 8.2에서 크게 늘었음).", fmt="decimal", tol=0.05), POP),
    X("멀티미디어 문항의 빠른 계산", [
        "축척: 1:50 000 지도에서 4 cm는 4 × 50 000 cm = 200 000 cm = 2 km입니다. 기울기는 높이 차 ÷ 수평 거리이고, 200 m 높이 차가 2 km에 걸쳐 있으면 1 : 10 또는 10%입니다.",
        "시차: 경도 15°마다 1시간이므로 동경 135°인 곳은 0°보다 9시간 빠릅니다(실제 표준시는 국가마다 정한 시간대를 따름). 동쪽이 더 빠른 시각입니다.",
        "경관 사진은 기후(식생, 지붕의 경사, 건물 재료), 지형(하천의 모양, 빙하 지형), 토지 이용(농업 형태, 도시 구조)의 단서를 찾습니다. 하나의 단서로 단정하지 말고 둘 이상을 맞춰 보세요.",
    ]),
    N("1:25 000 지도에서 두 지점 사이가 6 cm입니다. 실제 거리는 몇 km인가요? (소수 첫째 자리까지)", 1.5,
      "6 × 25 000 cm입니다.",
      "지도의 6 cm는 실제로 6 × 25 000 = 150 000 cm입니다.\n100 000 cm = 1 km이므로 150 000 cm = 1.5 km입니다.\n그래서 1.5 km입니다.", fmt="decimal", tol=0.01),
    E("등고선 간격 20 m인 지도에서 A에서 B까지 등고선이 8개 지나고(A가 낮음), 수평 거리가 1.6 km입니다. 평균 기울기를 비와 백분율로 구하세요.", [
        "등고선 8개를 지나므로 높이 차는 8 × 20 = 160 m입니다.",
        "기울기 = 160 m ÷ 1600 m = 0.1입니다.",
        "비로는 1 : 10, 백분율로는 10%입니다.",
    ], "1 : 10, 10%"),
    PR("[문제 1] 나라 Z의 자료로 'Explain the possible causes of the changes in the age structure of Country Z.'에 영어로 답하세요(6점).", [
        "The fall in the proportion of children is likely caused by declining fertility, which may result from urbanisation, higher female participation in education and employment, and the rising cost of raising children.",
        "Wider access to family planning and later marriage could also reduce the number of births per woman.",
        "The rise in the proportion of elderly people is likely due to increasing life expectancy, resulting from improved healthcare, nutrition and sanitation.",
        "Since these causes are not shown directly in the data, further evidence such as fertility rates and life expectancy over time would be needed to confirm them.",
    ], [
        ("출산율 감소와 그 원인을 설명했다", 2),
        ("기대 수명 증가와 그 원인을 설명했다", 2),
        ("인과 표현을 적절한 영어로 썼다", 1),
        ("자료의 한계와 추가 자료를 밝혔다", 1),
    ], "아이 비율 감소와 노인 비율 증가를 나누어 설명하세요.", "apply"),
    PR("[문제 2] 'Explain why temperatures in large cities are often higher than in surrounding rural areas (the urban heat island effect).'에 영어로 답하세요(6점).", [
        "Urban surfaces such as concrete, asphalt and brick absorb more solar radiation during the day and release it slowly at night, keeping cities warmer, especially at night.",
        "Cities have less vegetation and open water, so less energy is used for evapotranspiration and more heats the air.",
        "Human activities — vehicles, air conditioning, industry — release waste heat directly into the urban atmosphere.",
        "Tall buildings trap radiation and reduce wind speeds (urban canyons), and air pollution can trap outgoing long-wave radiation, further raising temperatures.",
    ], [
        ("도시 표면의 열 흡수와 방출을 설명했다", 2),
        ("식생 부족과 증발산을 설명했다", 1),
        ("인공 열 배출을 설명했다", 1),
        ("건물 구조나 대기 오염의 효과를 설명했다", 2),
    ], "표면, 식생, 인간 활동, 구조로 나누세요.", "apply"),
    PR("[문제 3] 'Evaluate the use of green roofs as a strategy to reduce the urban heat island effect.'에 영어로 답하세요(8점). 장점, 한계, 판단을 모두 쓰세요.", [
        "Advantages: green roofs replace heat-absorbing surfaces with vegetation, which cools the air through evapotranspiration and shading; they also reduce stormwater runoff, improve building insulation and provide habitats.",
        "Limitations: they are costly to install and maintain, require roofs strong enough to carry soil and water, and their cooling effect is mostly local, so many buildings must adopt them to affect city-wide temperatures. In dry climates they need irrigation.",
        "Stakeholders: building owners bear the costs, while benefits such as cooler streets and reduced flooding are shared by the wider community, which may justify subsidies.",
        "Judgement: on balance, green roofs are a useful part of a wider strategy, but they are most effective when combined with street trees, reflective (cool) surfaces and urban planning that preserves green space.",
    ], [
        ("장점을 둘 이상 설명했다", 2),
        ("한계를 둘 이상 설명했다", 2),
        ("이해관계자를 고려했다", 2),
        ("근거 있는 판단을 내렸다", 2),
    ], "평가는 장점 → 한계 → 판단입니다.", "apply"),
    PR("[문제 4] 경관 사진(가상): '가파른 지붕의 목조 가옥, 침엽수림, 넓은 U자 모양의 골짜기, 골짜기 바닥의 좁고 긴 호수'. 이 지역의 기후와 지형을 추론하고 근거를 영어로 쓰세요.", [
        "Climate: the steep roofs suggest heavy snowfall, and the coniferous forest suggests a cool climate with cold winters, such as a cool temperate or subarctic climate.",
        "Landform: the broad U-shaped valley indicates glacial erosion; the long narrow lake on the valley floor is likely a ribbon lake formed in a glacially over-deepened trough.",
        "Combined evidence: the region was probably glaciated in the past and now has a cool, snowy climate, typical of mountainous areas at high latitudes or high altitudes.",
        "A single clue would not be sufficient; it is the combination of vegetation, building style and landform that supports this interpretation.",
    ], [
        ("기후 단서를 해석했다", 2),
        ("빙하 지형을 해석했다", 2),
        ("단서를 종합해 결론지었다", 1),
        ("단서 하나로 단정하지 않음을 밝혔다", 1),
    ], "지붕, 식생, 골짜기 모양을 각각 해석하세요.", "apply"),
    PR("[문제 5] 'Compare the advantages and disadvantages of an ageing population for Country Z.'에 영어로 답하세요(6점). 같은 기준으로 비교하세요.", [
        "Economic: a growing elderly population increases spending on pensions and healthcare, and a shrinking future workforce may slow economic growth; however, older people can provide experience and, if healthy, continue working or volunteering.",
        "Social: more elderly people increase the demand for care, often provided by families; on the other hand, grandparents may support childcare and community life.",
        "Spatial: rural areas may become depopulated as young people leave, whereas some regions may benefit from 'silver' industries such as healthcare and leisure services.",
        "Overall, the disadvantages are likely to outweigh the advantages unless policies such as raising the retirement age, encouraging immigration or supporting families are adopted.",
    ], [
        ("경제적 측면을 양쪽으로 비교했다", 2),
        ("사회적 측면을 양쪽으로 비교했다", 2),
        ("공간적 측면이나 정책을 다루었다", 1),
        ("균형 있는 결론을 썼다", 1),
    ], "경제, 사회, 공간의 같은 기준으로 비교하세요.", "apply"),
    X("실전 연습과 자료", [
        "영어 서술형은 '요점 하나 = 1점'이 기본이므로, 문항 점수만큼 서로 다른 요점을 쓰는 연습을 하세요. 6점 문항이면 요점 여섯 개를 목표로, 문단 안에서 요점마다 문장을 나눕니다.",
        "멀티미디어 연습은 지도(축척, 등고선, 방위), 기후 그래프, 인구 피라미드, 위성 사진을 짧은 시간에 많이 보는 것이 좋습니다. 국토지리정보원의 지도 서비스, 위성 지도, 세계은행 자료로 직접 문항을 만들어 보세요.",
        "참고 자료: iGeo 공식 누리집의 지난 서술형·멀티미디어 문제(영문), 영국 지리 교과서의 명령어 안내, Oxford·Cambridge의 지리 시험 채점 기준(mark scheme)을 보면 영어 답안에서 점수를 받는 표현을 익힐 수 있습니다.",
    ], "apply"),
]}
