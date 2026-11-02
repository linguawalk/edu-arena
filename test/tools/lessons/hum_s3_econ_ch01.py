"""인문·사회 S3 · 경제 · 챕터 1 객관식·서술형 실전 (학습 가이드, 자체 제작 문항).
수치는 연습용 가상 자료다. 국제 경제 올림피아드(IEO)는 경제·금융 이론과 사례 분석을 함께 다루는 것으로 알려져 있으나,
세부 구성과 배점은 해마다 바뀔 수 있어 공식 누리집에서 확인해야 한다. 고르는 문항은 ①②③④ 가운데 번호로 답함."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lesson_kit import X, E, N, PR

DOMAIN = ["경제", "실전", "객관식·서술형"]

GUIDE = {"title": "경제 객관식·서술형 실전", "minutes": 150, "screens": [
    X("실전 연습 진행 방법", [
        "국제 경제 올림피아드(IEO)는 경제학과 금융의 이론 문제(객관식과 서술형)와 기업 사례 분석을 함께 다루는 것으로 알려져 있습니다. 문제와 답안은 영어로 쓰므로, 경제 용어를 영어로 정확히 아는 것이 중요합니다.",
        "이 가이드는 S1·S2 경제 트랙의 내용을 실전 형식으로 묶었습니다. 객관식형 확인 문항은 한 문항에 2~3분, 서술형 문제는 한 문제에 20~25분을 목표로 시간을 재며 푸세요.",
        "객관식에서는 계산 문항이 많으므로 공식을 외우는 것보다 '무엇이 무엇에 대한 변화율인가'를 정확히 정의하는 습관이 실수를 줄입니다.",
    ], "intro"),
    X("자주 쓰는 계산과 영어 용어", [
        "가격 탄력성(price elasticity of demand): 중간점 공식 (ΔQ/평균 Q) ÷ (ΔP/평균 P). 실질 이자율(real interest rate) ≈ 명목 이자율 − 물가 상승률. GDP 디플레이터 = 명목 GDP ÷ 실질 GDP × 100.",
        "지출 승수(spending multiplier) = 1/(1 − 한계 소비 성향). 순현재가치(NPV) = Σ 미래 현금 흐름/(1 + r)ᵗ − 초기 투자. 기회비용(opportunity cost)으로 비교 우위(comparative advantage)를 정합니다.",
        "영어 용어: deadweight loss(자중 손실), externality(외부 효과), marginal cost(한계 비용), elasticity(탄력성), inflation(물가 상승), monetary policy(통화 정책), fiscal policy(재정 정책), present value(현재 가치).",
    ]),
    N("가격이 10에서 12로 오르자 수요량이 100에서 80으로 줄었습니다. 중간점 공식으로 구한 수요의 가격 탄력성(절댓값)은? (소수 둘째 자리까지)", 1.22,
      "(20/90) ÷ (2/11)입니다.",
      "수요량 변화율은 20 ÷ 평균 90 ≈ 0.222, 가격 변화율은 2 ÷ 평균 11 ≈ 0.182입니다.\n탄력성 = 0.222 ÷ 0.182 ≈ 1.22입니다.\n1보다 크므로 탄력적이며, 가격을 올리면 총수입이 줄어듭니다.", fmt="decimal", tol=0.01),
    N("한계 소비 성향이 0.8일 때 지출 승수는?", 5,
      "1/(1 − 0.8)입니다.",
      "지출 승수는 1/(1 − 한계 소비 성향)입니다.\n1 − 0.8 = 0.2이므로 1/0.2입니다.\n= 5이며, 정부 지출이 1 늘면 GDP가 최대 5 늘 수 있습니다(단순 모형)."),
    N("명목 GDP가 1200, 실질 GDP가 1000일 때 GDP 디플레이터는?", 120,
      "명목 ÷ 실질 × 100입니다.",
      "GDP 디플레이터는 명목 GDP를 실질 GDP로 나누어 100을 곱한 값입니다.\n1200 ÷ 1000 × 100입니다.\n= 120으로, 기준 연도보다 물가가 20% 올랐음을 뜻합니다."),
    N("A국은 밀 1톤을 생산할 때 옷 2벌을, B국은 밀 1톤을 생산할 때 옷 4벌을 포기해야 합니다. 밀에 비교 우위가 있는 나라는? ① A국 ② B국 ③ 둘 다 ④ 정할 수 없다", 1,
      "밀의 기회비용이 작은 나라입니다.",
      "밀 1톤의 기회비용은 A국이 옷 2벌, B국이 옷 4벌입니다.\n기회비용이 작은 A국이 밀에 비교 우위가 있고, B국은 옷에 비교 우위가 있습니다.\n답은 1입니다."),
    E("초기 투자 1000, 1년 뒤 550, 2년 뒤 605를 받는 사업의 NPV를 할인율 10%로 구하세요.", [
        "1년 뒤 550의 현재 가치는 550/1.1 = 500입니다.",
        "2년 뒤 605의 현재 가치는 605/1.21 = 500입니다.",
        "NPV = 500 + 500 − 1000 = 0이므로 할인율 10%에서 이 사업은 손익이 같은 경계에 있습니다(내부 수익률 = 10%).",
    ], "0"),
    E("명목 이자율 5%, 물가 상승률 7%일 때 실질 이자율과 그 의미를 쓰세요.", [
        "실질 이자율 ≈ 5% − 7% = −2%입니다(정확히는 1.05/1.07 − 1 ≈ −1.9%).",
        "예금하면 이자를 받아도 구매력이 해마다 약 2% 줄어든다는 뜻입니다.",
        "빌리는 사람에게는 실질 부담이 줄어 유리하고, 저축하는 사람에게는 불리해 저축 유인이 약해집니다.",
    ], "약 −2%"),
    PR("[서술형 1] 정부가 생필품에 시장 균형보다 낮은 가격 상한(price ceiling)을 정했습니다. 수요·공급 그래프의 말로 그 효과를 설명하고 정책을 평가하세요(영어 또는 한국어).", [
        "A binding price ceiling below the equilibrium price raises quantity demanded and lowers quantity supplied, creating a shortage equal to the difference.",
        "The quantity actually traded falls to the quantity supplied, so some mutually beneficial trades no longer occur, creating a deadweight loss.",
        "Consumers who obtain the good gain from the lower price, but others cannot buy it at all; non-price rationing (queues, favouritism) and black markets may appear, and quality may fall.",
        "Evaluation: the policy helps some low-income buyers in the short run, but targeted subsidies or cash transfers usually achieve the same goal with less inefficiency.",
    ], [
        ("부족(shortage)의 발생을 설명했다", 2),
        ("거래량 감소와 자중 손실을 설명했다", 2),
        ("분배 효과와 부작용을 설명했다", 1),
        ("대안과 함께 평가했다", 1),
    ], "균형보다 낮은 가격에서 수요량과 공급량을 비교하세요.", "apply"),
    PR("[서술형 2] 중앙은행이 물가 상승을 억제하려고 기준 금리를 올렸습니다. 금리 인상이 총수요, 환율, 물가에 미치는 경로를 설명하고, 부작용 하나를 쓰세요.", [
        "Higher policy rates raise market interest rates, increasing the cost of borrowing; households reduce consumption and firms reduce investment, so aggregate demand falls.",
        "Higher rates attract capital inflows, appreciating the domestic currency; exports become more expensive and imports cheaper, reducing net exports and import prices.",
        "Lower aggregate demand and cheaper imports reduce inflationary pressure, usually with a lag of one to two years.",
        "Side effect: slower growth and higher unemployment in the short run; highly indebted households and firms may face financial stress, which may raise default risks.",
    ], [
        ("소비·투자 경로를 설명했다", 2),
        ("환율 경로를 설명했다", 2),
        ("물가 효과와 시차를 밝혔다", 1),
        ("부작용을 설명했다", 1),
    ], "금리 → 차입 비용 → 총수요의 사슬을 쓰세요.", "apply"),
    PR("[서술형 3] 두 기업이 같은 시장에서 가격 경쟁과 담합 사이에서 선택하는 상황을 게임 이론으로 설명하고, 반복 게임이 결과를 어떻게 바꿀 수 있는지 쓰세요.", [
        "In a one-shot game, each firm has a dominant strategy to cut prices: whatever the rival does, undercutting yields higher profit. The Nash equilibrium is mutual price-cutting, although both would earn more by colluding (a prisoner's dilemma).",
        "Collusion is unstable because each firm has an incentive to cheat on the agreement.",
        "If the game is repeated indefinitely, firms can sustain collusion with strategies such as tit-for-tat or grim trigger: the threat of future punishment outweighs the one-time gain from cheating if firms value future profits enough.",
        "Collusion is more likely with few firms, frequent interaction and observable prices; this is why competition authorities ban cartels and use leniency programmes to destabilise them.",
    ], [
        ("일회 게임의 우월 전략과 내시 균형을 설명했다", 2),
        ("담합의 불안정성을 설명했다", 1),
        ("반복 게임에서 협력이 유지되는 조건을 설명했다", 2),
        ("정책적 함의를 밝혔다", 1),
    ], "일회 게임과 반복 게임을 나누어 쓰세요.", "apply"),
    PR("[사례 분석] 가상의 음료 기업이 설탕세 도입 뒤 매출이 15% 줄었습니다. 기업이 고려할 전략 세 가지를 제시하고, 각 전략의 장단점과 우선순위를 판단하세요.", [
        "Strategy 1 — reformulate products to reduce sugar below the tax threshold: avoids the tax and responds to health trends, but requires R&D and risks changing taste and losing loyal customers.",
        "Strategy 2 — diversify into low-sugar or functional drinks: captures growing demand, but needs marketing investment and faces existing competitors.",
        "Strategy 3 — absorb the tax and keep prices: protects market share in the short run, but reduces margins and does not address the long-term shift in demand.",
        "Priority: reformulation combined with gradual diversification is the most sustainable, because the tax and consumer preferences both point towards lower sugar; absorbing the tax should be only a short-term measure.",
    ], [
        ("현실성 있는 전략 세 가지를 제시했다", 2),
        ("각 전략의 장단점을 밝혔다", 2),
        ("근거 있는 우선순위를 정했다", 2),
    ], "세금을 피하는 전략, 시장을 넓히는 전략, 버티는 전략을 비교하세요.", "apply"),
    PR("[서술형 4] 탄소세(carbon tax)와 배출권 거래제(cap-and-trade)를 비교하고, 어떤 상황에서 어느 정책이 나은지 판단하세요.", [
        "Both policies put a price on carbon emissions, correcting a negative externality by making polluters pay the social cost.",
        "A carbon tax fixes the price and lets the quantity of emissions adjust; it gives firms predictable costs and raises revenue, but the resulting emission level is uncertain.",
        "Cap-and-trade fixes the quantity of emissions and lets the price adjust through trading; it guarantees an emission target and lets reductions occur where they are cheapest, but prices can be volatile.",
        "If meeting a specific emission target is critical, cap-and-trade is preferable; if price stability and simplicity matter more, a carbon tax is better. Many economists favour combining a cap with a price floor and ceiling.",
    ], [
        ("공통 원리(외부 효과 교정)를 설명했다", 1),
        ("탄소세의 특징을 설명했다", 2),
        ("배출권 거래제의 특징을 설명했다", 2),
        ("상황에 따른 판단을 내렸다", 1),
    ], "가격을 정하는가, 양을 정하는가입니다.", "apply"),
    X("실전 뒤의 점검과 자료", [
        "계산 문항은 틀린 이유를 '정의를 잘못 씀 / 계산 실수 / 단위·백분율 혼동'으로 나누어 기록하세요. 같은 종류의 실수가 반복되면 그 개념의 정의를 다시 공부합니다.",
        "서술형은 그래프를 말로 설명하는 연습이 중요합니다. 답안에 그래프를 그릴 수 있으면 축 이름, 곡선 이름, 이동 방향을 반드시 표시하세요.",
        "참고 자료: IEO 공식 누리집의 지난 문제(영문), N. Gregory Mankiw 『Principles of Economics』, Khan Academy의 경제학 강좌(무료, 영문), 한국은행 경제교육 자료.",
    ], "apply"),
]}
