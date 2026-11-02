"""인문·사회 S3 · 철학 · 챕터 2 4시간 실전 연습 (학습 가이드, 자체 제작 문항).
인용문은 공개된 고전의 널리 알려진 구절이다. 채점 기준은 IPO에서 널리 알려진 평가 요소(주제 이해, 철학적 이해, 논증의 설득력,
일관성, 독창성)를 바탕으로 연습용으로 정리한 것이며 공식 배점이 아니다. 세부 규정은 공식 누리집에서 확인해야 한다."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lesson_kit import X, E, N, PR

DOMAIN = ["철학", "에세이", "4시간 실전 연습"]

QUOTES = """연습용 인용문 네 개 (하나를 골라 4시간 동안 영어로 에세이를 쓴다)
1. "I think, therefore I am." — Descartes, Discourse on the Method
2. "Man is born free, and everywhere he is in chains." — Rousseau, The Social Contract
3. "The limits of my language mean the limits of my world." — Wittgenstein, Tractatus
4. "It is better to be a human being dissatisfied than a pig satisfied." — Mill, Utilitarianism"""

GUIDE = {"title": "4시간 실전 연습", "minutes": 300, "screens": [
    X("실전 연습 진행 방법", [
        "이 가이드는 IPO처럼 인용문 네 개 가운데 하나를 골라 4시간 동안 영어로 에세이를 쓰는 연습입니다. 사전은 대회 규정에 따라 쓸 수 있는 경우가 있으므로, 연습할 때도 종이 사전(영영 또는 영한) 하나만 허용하는 등 실제와 같은 조건을 정하세요.",
        "시간 배분 예: 인용문 고르기와 생각 정리 20분, 개요 25분, 쓰기 165분, 검토 30분. 쓰기 시간 중 서론 20분, 본론 각 35~40분, 반론과 재반론 30분, 결론 15분 정도를 목표로 합니다.",
        "다 쓴 뒤에는 아래 채점 기준으로 스스로 채점하고, 일주일 뒤 같은 에세이를 다시 읽어 보며 고칠 점을 적으세요. 시간이 지나야 자기 글의 빈틈이 보입니다.",
    ], "intro"),
    X("연습용 인용문", [
        "1. \"I think, therefore I am.\" — 데카르트, 『방법서설』. 2. \"Man is born free, and everywhere he is in chains.\" — 루소, 『사회 계약론』. 3. \"The limits of my language mean the limits of my world.\" — 비트겐슈타인, 『논리-철학 논고』. 4. \"It is better to be a human being dissatisfied than a pig satisfied.\" — 밀, 『공리주의』.",
        "인용문을 고를 때는 '가장 좋아하는 철학자'가 아니라 '가장 분명한 논제와 가장 강한 반론을 떠올릴 수 있는 인용문'을 고르세요. 10분 안에 논제 하나와 반론 하나가 떠오르지 않으면 다른 인용문으로 바꾸는 것이 낫습니다.",
        "각 인용문이 속한 분야: 1은 인식론(확실성, 자아), 2는 정치철학(자유와 정당한 권위), 3은 언어 철학(언어와 사고·세계), 4는 윤리학(쾌락의 질). 분야의 기본 논쟁을 알고 있으면 반론을 빠르게 세울 수 있습니다.",
    ], "intro"),
    X("첫 20분의 계획 틀", [
        "인용문을 고른 뒤 첫 20분 동안 종이 한 장에 다음 다섯 줄을 채웁니다: ① 인용문을 내 말로 한 문장 ② 애매한 낱말 두 개와 내가 택할 뜻 ③ 논제 한 문장(동의, 반대, 부분 동의 가운데 하나) ④ 논제를 뒷받침하는 근거 세 개 ⑤ 가장 강한 반론 하나와 그에 대한 답.",
        "이 다섯 줄이 채워지지 않으면 쓰기를 시작하지 마세요. 쓰는 도중에 논제가 바뀌면 서론부터 다시 써야 해 시간을 크게 잃습니다.",
        "개요(25분)에서는 이 다섯 줄을 문단 단위로 펼쳐, 문단마다 첫 문장(주제문)을 영어로 미리 써 둡니다. 주제문만 이어 읽어도 논증이 보이면 좋은 개요입니다.",
    ]),
    N("4시간 시험에서 생각 정리 20분, 개요 25분, 검토 30분을 빼면 쓰는 시간은 몇 분인가요?", 165,
      "240 − 20 − 25 − 30입니다.",
      "4시간은 240분입니다.\n생각 정리 20분, 개요 25분, 검토 30분을 빼면 240 − 75입니다.\n= 165분이 실제로 쓰는 시간입니다."),
    X("채점 기준 (연습용)", [
        "주제 이해(관련성): 인용문을 정확히 읽고 그 철학적 문제를 다루었는가. 철학적 이해: 관련 개념과 입장을 정확히 이해하고 썼는가. 논증의 설득력: 주장이 근거로 뒷받침되고 반론을 다루었는가.",
        "일관성: 서론의 논제에서 결론까지 논리의 흐름이 이어지는가, 문단마다 하나의 역할이 있는가. 독창성: 교과서 요약을 넘어 자기 생각(새로운 예, 구별, 반론)을 보였는가.",
        "이 가이드의 풀이 문제는 이 다섯 요소를 각각 연습합니다. 마지막 문제(문제 5)는 실제 4시간 에세이이며, 채점 기준의 점수 합 10점으로 스스로 채점합니다.",
    ]),
    E("인용문 1(데카르트)로 10분 안에 논제와 가장 강한 반론을 정하는 과정을 보이세요.", [
        "인용문의 주장: 생각하고 있다는 사실에서 내가 존재한다는 것이 의심할 수 없이 확실하게 따라 나온다.",
        "논제 후보: 'The cogito establishes the existence of thinking, but not the existence of a persisting self.'(생각이 있다는 것은 확실하지만, '나'라는 지속하는 주체의 존재까지는 확립하지 못한다.)",
        "가장 강한 반론: 리히텐베르크식 반론 — 'It thinks'라고만 말해야 하며 'I'는 문법이 덧붙인 것이다. 이 반론을 논제의 근거로 쓰고, 데카르트 쪽 재반론(생각은 생각하는 자 없이 있을 수 없다)을 다루면 에세이의 뼈대가 섭니다.",
    ], "논제와 반론을 먼저 정한다"),
    E("인용문 4(밀)로 본론 세 단계를 세우세요.", [
        "본론 1: 밀의 주장을 재구성 — 쾌락에는 양뿐 아니라 질의 차이가 있고, 두 쾌락을 모두 경험한 사람이 한쪽을 선호하면 그것이 더 높은 쾌락이다.",
        "본론 2: 비판 — '경험한 사람의 선호'라는 기준은 쾌락 이외의 가치(존엄, 자율)를 몰래 끌어들여, 쾌락주의의 틀을 벗어난다.",
        "본론 3: 대안 — 인간적 삶의 가치를 쾌락이 아닌 역량의 실현으로 설명하면 인용문의 직관은 지키면서 일관성 문제를 피할 수 있다.",
    ], "재구성 → 비판 → 대안"),
    N("에세이 1500단어를 서론 10%, 본론 60%, 반론과 재반론 20%, 결론 10%로 나누면 본론 세 단계 각각은 몇 단어인가요?", 300,
      "1500 × 0.6 ÷ 3입니다.",
      "본론 전체는 1500 × 0.6 = 900단어입니다.\n세 단계로 똑같이 나눕니다.\n900 ÷ 3 = 300단어씩입니다."),
    PR("[문제 1 · 주제 이해] 인용문 3(비트겐슈타인)을 영어로 풀어 쓰고, 'language'와 'world'를 어떻게 해석할지 두 가지 가능성을 제시한 뒤 하나를 골라 논제를 세우세요.", [
        "Paraphrase: Wittgenstein suggests that what I can meaningfully think and say is bounded by the language I possess, so that whatever lies beyond my language lies beyond my world.",
        "Interpretation A: 'world' means 'the totality of facts I can represent'; then the claim is a thesis about the limits of meaningful representation (what cannot be said cannot be thought).",
        "Interpretation B: 'world' means 'my lived experience and its categories'; then the claim resembles linguistic relativity — speakers of different languages inhabit different worlds.",
        "Thesis (choosing A): 'I will argue that, on the representational reading, the claim is defensible for propositional thought but fails for non-conceptual experience, such as perception of colours we have no word for.'",
    ], [
        ("인용문을 정확히 풀어 썼다", 2),
        ("두 해석을 구별했다", 2),
        ("해석을 골라 논제를 세웠다", 2),
    ], "'world'가 사실의 총체인지, 경험인지 구별하세요.", "apply"),
    PR("[문제 2 · 철학적 이해] 인용문 2(루소)의 '태어날 때는 자유롭지만 어디서나 사슬에 묶여 있다'의 뜻을 루소의 핵심 개념(사회 계약, 일반 의지, 정당한 권위)과 연결해 영어로 설명하세요.", [
        "Rousseau observes that human beings are by nature free and equal, yet in existing societies they live under relations of dependence and domination — the 'chains' of law, property and inequality.",
        "His question is not how to remove all chains, but what could make them legitimate. Rousseau explicitly sets aside the historical question of how the change came about and asks instead under what conditions political authority could be justified.",
        "His answer is the social contract: each person gives himself wholly to the community, and the community is governed by the general will, which aims at the common good rather than private interests.",
        "Because each obeys a law he has himself willed as a citizen, he 'obeys only himself' and remains free in a new, civil sense. The quotation thus states the problem that the theory of the general will is meant to solve.",
    ], [
        ("자연적 자유와 사회의 '사슬'을 설명했다", 2),
        ("물음이 정당성에 관한 것임을 밝혔다", 2),
        ("사회 계약과 일반 의지로 연결했다", 2),
    ], "루소는 사슬을 없애자고 했을까요, 정당하게 만들자고 했을까요?", "apply"),
    PR("[문제 3 · 논증의 설득력] 인용문 1(데카르트)에 대한 리히텐베르크식 반론을 가장 강한 형태로 쓰고, 데카르트의 입장에서 재반론한 뒤 어느 쪽이 더 설득력 있는지 판단하세요(영어).", [
        "Objection (strongest form): What is indubitable in the moment of doubt is only that thinking is occurring. The inference to 'I' assumes that every thought must belong to a substantial subject, but this assumption is not itself indubitable; Descartes should have said 'there is thinking'.",
        "Cartesian reply: A thought is essentially a thought of someone — it has a perspective. The very act of doubting is experienced as my doubting, so the 'I' is given in the thought, not added to it.",
        "Assessment: The reply establishes a minimal subject — the point of view of the present thought — but not a persisting, substantial self that exists across time.",
        "Therefore the objection succeeds against the stronger Cartesian claim (a thinking substance), while the reply preserves a weaker claim (a momentary subject of experience).",
    ], [
        ("반론을 가장 강한 형태로 썼다", 2),
        ("재반론을 정확히 썼다", 2),
        ("구별을 통해 균형 있게 판단했다", 2),
    ], "'최소한의 주체'와 '실체로서의 자아'를 구별하세요.", "apply"),
    PR("[문제 4 · 일관성과 독창성] 인용문 4(밀)에 대한 에세이의 결론 문단을 영어로 쓰세요. 논제를 다시 말하되 반복하지 않고, 논의의 의의와 남은 물음을 밝히세요.", [
        "I have argued that Mill's distinction between higher and lower pleasures captures a genuine insight — that a characteristically human life has a value that mere contentment lacks — but that this insight cannot be accommodated within hedonism.",
        "Mill's test of competent judges smuggles in values such as dignity, which are not themselves pleasures; once these are admitted, the theory is no longer a pure form of utilitarianism.",
        "This matters because it suggests that the most attractive form of utilitarianism may need to count goods other than pleasure, such as knowledge, friendship and the exercise of human capacities.",
        "An open question remains: whether such a pluralist view can still provide a single criterion for right action, which was the original promise of utilitarianism.",
    ], [
        ("논제를 새로운 말로 다시 밝혔다", 2),
        ("논의의 의의를 밝혔다", 2),
        ("남은 물음을 제시하되 새 논증을 시작하지 않았다", 2),
    ], "결론은 요약 + 의의 + 남은 물음입니다.", "apply"),
    PR("[문제 5 · 실전] 연습용 인용문 네 개 가운데 하나를 골라 4시간 동안 영어로 에세이(1200~1800단어)를 쓰세요. 다 쓴 뒤 아래 기준으로 스스로 채점하세요. (모범 답안은 좋은 에세이의 특징을 정리한 것입니다.)", [
        "첫 문단에서 인용문을 풀어 쓰고, 핵심 개념을 정의하며, 한 문장의 논제로 끝맺는다.",
        "본론의 각 문단은 첫 문장에 그 문단의 주장을 두고, 근거(논증, 예, 사고 실험)로 뒷받침하며, 논제와의 관계를 밝힌다.",
        "가장 강한 반론을 공정하게 제시하고, 재반론에서 구별이나 양보를 통해 논제를 지키거나 다듬는다.",
        "결론은 논제를 새로운 말로 다시 밝히고, 의의와 남은 물음을 제시한다. 전체에 걸쳐 영어가 명료하고 용어가 정확하다.",
    ], [
        ("주제 이해: 인용문을 정확히 읽고 문제를 다루었다", 2),
        ("철학적 이해: 개념과 입장을 정확히 썼다", 2),
        ("설득력: 근거와 반론·재반론이 충실하다", 2),
        ("일관성: 논제에서 결론까지 흐름이 이어진다", 2),
        ("독창성: 자기만의 구별, 예, 논증이 있다", 2),
    ], "시간 배분표를 책상 위에 두고 쓰세요.", "apply"),
    X("실전 뒤의 점검과 자료", [
        "채점한 뒤 가장 낮은 기준 하나를 골라, 그 부분만 다시 써 보세요. 예를 들어 '설득력'이 낮았다면 반론 문단만 30분 동안 다시 씁니다. 전체를 다시 쓰는 것보다 효율적입니다.",
        "한 달에 한 번 이상 4시간 실전을 하고, 매번 다른 분야의 인용문을 고르세요. 실전 사이에는 짧은 연습(인용문 하나로 15분 동안 논제와 반론만 쓰기)을 자주 합니다.",
        "참고 자료: IPO 공식 누리집의 지난 인용문과 수상 에세이, Jim Pryor의 'Guidelines on Writing a Philosophy Paper'(누리집 공개, 영문), Stanford Encyclopedia of Philosophy.",
    ], "apply"),
]}
