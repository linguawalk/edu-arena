"""인문·사회 S3 · 철학 · 챕터 1 외국어 철학 에세이 (학습 가이드, 자체 제작 문항).
인용문은 공개된 고전의 널리 알려진 구절을 영어로 옮긴 것이다. 영어 예문과 모범 문단은 이 가이드를 위해 쓴 것이다.
IPO의 형식(네 인용문 가운데 하나, 모국어가 아닌 공식 언어, 4시간)은 S2에서 소개한 내용이며, 세부 규정은 해마다 공식 누리집에서 확인해야 한다."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lesson_kit import X, E, N, PR

DOMAIN = ["철학", "에세이", "외국어 철학 에세이"]

GUIDE = {"title": "외국어 철학 에세이 학습 가이드", "minutes": 120, "screens": [
    X("이 가이드의 사용법", [
        "인문·사회 S3는 국제 대회 수준의 실전을 학습 가이드로 독학합니다. 철학은 국제 철학 올림피아드(IPO)처럼 모국어가 아닌 언어(대개 영어)로 에세이를 쓰는 연습이 핵심입니다. 이 가이드는 영어 철학 에세이의 표현과 구조를, 다음 챕터는 4시간 실전 연습을 다룹니다.",
        "풀이 문제는 영어로 쓰는 것을 원칙으로 합니다. 모범 답안도 영어 문장을 함께 실었으므로, 먼저 스스로 쓰고 비교한 뒤 채점 기준으로 점수를 매기세요.",
        "선수 지식: S2 '철학 에세이의 구조'(논제, 정의, 논증, 반론과 재반론, 결론)와 윤리학·인식론·정치철학 주제.",
    ], "intro"),
    X("영어 철학 에세이의 기본 표현", [
        "논제 제시: 'In this essay I will argue that …', 'I shall defend the claim that …'. 개념 정의: 'By X I mean …', 'Let us understand X as …'. 논증 단계: 'The first premise is …', 'It follows that …', 'Therefore …'.",
        "반론과 재반론: 'One might object that …', 'A natural objection is …', 'In reply, …', 'This objection fails because …'. 양보: 'It must be conceded that …, but …'. 결론: 'I conclude that …', 'If my argument is sound, then …'.",
        "채점자는 화려한 어휘보다 명료함을 봅니다. 한 문장에 한 주장, 한 문단에 한 단계라는 원칙을 지키고, 접속 표현(however, therefore, moreover)으로 논리의 흐름을 드러내세요.",
    ]),
    N("'One might object that …'은 에세이의 어느 부분에서 쓰는 표현인가요? ① 논제 제시 ② 개념 정의 ③ 반론 제시 ④ 결론", 3,
      "object는 '반대하다'입니다.",
      "'One might object that …'은 '…라고 반대할 수 있다'는 뜻입니다.\n자기 논증에 대한 반론을 소개할 때 씁니다.\n답은 3입니다."),
    X("인용문을 영어로 읽기", [
        "IPO의 인용문은 원문이나 공식 번역으로 주어집니다. 예: 'Man is by nature a political animal.'(아리스토텔레스, 『정치학』), 'Act only according to that maxim whereby you can at the same time will that it should become a universal law.'(칸트, 『윤리 형이상학 정초』), 'the life of man, solitary, poor, nasty, brutish, and short.'(홉스, 『리바이어던』).",
        "영어 인용문에서는 핵심 낱말의 철학적 뜻을 정확히 짚어야 합니다. 'by nature'(본성상, 관습이 아니라), 'maxim'(행위의 주관적 원칙), 'universal law'(모든 이성적 존재에게 적용되는 법칙)처럼, 일상적인 뜻과 다른 전문적인 뜻이 있습니다.",
        "에세이 첫 문단에서는 인용문을 자기 말로 풀어 쓰고(paraphrase), 그 안의 애매한 낱말을 어떻게 이해할지 밝히세요. 이것이 채점 기준의 '주제 이해'에 해당합니다.",
    ]),
    E("칸트의 인용문 'Act only according to that maxim whereby you can at the same time will that it should become a universal law.'을 에세이 첫 문단에서 풀어 쓰는 문장을 예로 드세요.", [
        "먼저 핵심 개념을 정의합니다: 'By a maxim, Kant means the subjective principle on which an agent acts, such as \"I will lie when it benefits me.\"'",
        "다음으로 시험의 내용을 풀어 씁니다: 'The test asks whether I could consistently will that everyone act on my maxim.'",
        "마지막으로 논제를 밝힙니다: 'In this essay I will argue that this test captures something essential about moral wrongness, but that it cannot by itself determine which actions are permissible.'",
    ], "정의 → 풀어 쓰기 → 논제"),
    N("영어 에세이에서 4시간 동안 1500단어를 쓰려면, 계획 30분과 검토 30분을 빼고 1분에 평균 몇 단어를 써야 하나요? (소수 첫째 자리까지)", 8.3,
      "쓰는 시간은 240 − 60 = 180분입니다.",
      "4시간 = 240분에서 계획 30분과 검토 30분을 빼면 쓰는 시간은 180분입니다.\n1500 ÷ 180 ≈ 8.33입니다.\n1분에 약 8.3단어로, 생각하며 쓰기에 충분한 속도입니다.", fmt="decimal", tol=0.05),
    X("자주 하는 실수와 고쳐 쓰기", [
        "한국어로 생각한 문장을 그대로 옮기면 주어가 빠지거나 문장이 지나치게 길어집니다. 'It is because …' 같은 모호한 구문보다 'The reason is that …', 'This is so because …'처럼 주어와 동사가 분명한 문장을 쓰세요.",
        "'I think', 'In my opinion'을 남발하면 주장이 약해 보입니다. 논증으로 뒷받침한 주장은 'X is the case because …'처럼 단정적으로 쓰고, 불확실한 부분만 'It seems that …', 'arguably'로 표시하세요.",
        "철학 용어는 정확히 쓰세요: valid(타당한, 형식), sound(건전한, 타당하고 전제가 참), necessary(필요), sufficient(충분), premise(전제), conclusion(결론), counterexample(반례).",
    ]),
    E("다음 문장을 철학 에세이에 맞게 고쳐 쓰세요: 'I think Hobbes is wrong because people are not so bad.'", [
        "문제: 'I think'로 주장이 약하고, 'wrong'이 무엇에 대한 것인지, 'not so bad'가 무슨 뜻인지 불분명하며 근거가 없습니다.",
        "고쳐 쓰기: 'Hobbes's claim that life without a state would be \"solitary, poor, nasty, brutish, and short\" rests on the premise that humans are primarily motivated by self-preservation and fear.'",
        "이어서: 'This premise is doubtful, since anthropological evidence of cooperation in small stateless societies suggests that humans are also moved by reciprocity and trust.'",
    ], "주장 대상, 전제, 근거를 분명히"),
    PR("[문제 1] 아리스토텔레스의 'Man is by nature a political animal.'에 대해 영어로 서론 문단(5~7문장)을 쓰세요. 인용문 풀어 쓰기, 핵심 개념 정의, 논제를 포함하세요.", [
        "Aristotle claims that human beings are, by nature, political animals: that is, that living in a political community is not an artificial addition to human life but part of what it is to flourish as a human being.",
        "By 'by nature' I understand 'as an expression of the characteristic capacities of the species', in contrast to 'by convention'. By 'political' I understand 'belonging to a community that deliberates about justice and the common good'.",
        "The claim is significant because, if it is true, a solitary life could not be a fully good human life, and the state would not be merely a contract for mutual protection.",
        "In this essay I will argue that Aristotle is right that human flourishing requires community, but wrong to identify that community with the political state.",
    ], [
        ("인용문을 정확히 풀어 썼다", 2),
        ("핵심 개념을 정의했다", 2),
        ("논제를 분명히 밝혔다", 1),
        ("영어 표현이 명료하다", 1),
    ], "풀어 쓰기 → 정의 → 의의 → 논제 순서입니다.", "apply"),
    PR("[문제 2] 칸트의 보편 법칙 정식에 대한 대표적인 반론 하나와 그에 대한 재반론을 영어 문단으로 쓰세요.", [
        "Objection: One might object that the universal law test is too permissive, since a cleverly specific maxim can always be universalized. For example, 'I will lie whenever my name is Kim and it is Tuesday' could be universalized without contradiction.",
        "Reply: In reply, a Kantian can argue that a maxim must describe the agent's actual reason for acting. My reason for lying is not that my name is Kim, but that lying benefits me; the morally relevant maxim is therefore 'I will lie when it benefits me', which fails the test.",
        "This reply shows that the test depends on an honest description of one's reasons, which is itself a moral achievement.",
        "It must be conceded, however, that the test alone does not tell us how to describe our maxims, so it needs to be supplemented by an account of practical reasoning.",
    ], [
        ("반론을 구체적인 예와 함께 제시했다", 2),
        ("재반론을 논리적으로 제시했다", 2),
        ("재반론의 한계를 인정했다", 1),
        ("영어 표현과 연결어가 적절하다", 1),
    ], "지나치게 구체적인 준칙을 생각해 보세요.", "apply"),
    PR("[문제 3] 다음 논증을 영어로 정리하고 타당성(valid)과 건전성(sound)을 평가하세요: '모든 지식은 경험에서 온다. 수학적 지식은 경험에서 오지 않는다. 따라서 수학적 지식은 지식이 아니다.'", [
        "Premise 1: All knowledge comes from experience. Premise 2: Mathematical knowledge does not come from experience. Conclusion: Therefore, mathematical knowledge is not knowledge.",
        "The argument is valid: if both premises are true, the conclusion must be true (it has the form 'All K are E; M is not E; so M is not K').",
        "However, it is not sound if either premise is false. A rationalist will reject Premise 1, holding that some knowledge is a priori; an empiricist like Mill might reject Premise 2, holding that mathematics is a very general empirical science.",
        "Since the conclusion is highly implausible, the argument is best read as a reductio: it shows that Premise 1 and Premise 2 cannot both be accepted.",
    ], [
        ("논증을 영어로 정확히 정리했다", 2),
        ("타당성을 바르게 판정했다", 1),
        ("전제를 공격하는 두 입장을 들었다", 2),
        ("귀류법으로 읽는 해석을 제시했다", 1),
    ], "타당과 건전을 구별하세요.", "apply"),
    PR("[문제 4] 홉스의 자연 상태 인용문을 주제로 한 에세이의 개요를 영어로 쓰세요(서론, 본론 세 단계, 반론과 재반론, 결론).", [
        "Introduction: paraphrase the quotation; define 'state of nature' and 'state'; thesis: Hobbes is right that some coercive authority is needed for security, but wrong that life without a state must be a war of all against all.",
        "Body 1: reconstruct Hobbes's argument from equality, scarcity and diffidence to war. Body 2: challenge the premise of pure self-interest with evidence of reciprocity and trust. Body 3: argue that informal institutions can secure cooperation in small groups but not in large anonymous societies.",
        "Objection and reply: Objection — cooperation in small groups still depends on the threat of punishment, which is a proto-state. Reply — punishment by peers differs from a sovereign's monopoly of force, so it does not vindicate Hobbes's absolutism.",
        "Conclusion: Hobbes identifies a real problem of security in large societies, but his solution overstates both the misery of stateless life and the need for an absolute sovereign.",
    ], [
        ("서론과 논제를 분명히 했다", 1),
        ("본론 세 단계가 논리적으로 이어진다", 2),
        ("반론과 재반론이 핵심을 겨눈다", 2),
        ("결론이 논제와 일치한다", 1),
    ], "논제를 '부분적으로 동의'로 세우면 깊이가 생깁니다.", "apply"),
    PR("[문제 5] 다음 영어 문단의 문제점을 지적하고 고쳐 쓰세요: 'Utilitarianism is bad. It says we should make people happy. But sometimes making people happy is bad. So utilitarianism is wrong. I think this is a strong argument.'", [
        "문제: 'bad', 'wrong'이 무슨 뜻인지 불분명하고, 공리주의를 '사람들을 행복하게 하라'로 지나치게 단순화했으며, '때로 행복하게 하는 것이 나쁘다'의 예가 없고, 마지막 문장은 근거 없는 자기 평가다.",
        "Rewrite: 'Utilitarianism holds that the right action is the one that maximizes overall happiness. A well-known objection is that this principle can require us to sacrifice an innocent person whenever doing so produces greater total happiness, as when a judge convicts an innocent man to prevent a riot.'",
        "'If utilitarianism permits such an act, it conflicts with a deeply held conviction that individuals have rights which may not be overridden by aggregate gains. A utilitarian may reply that a practice of punishing the innocent would reduce happiness in the long run; however, this reply makes the wrongness of the act depend on contingent consequences, which seems to misdescribe why it is wrong.'",
        "고친 문단은 이론을 정확히 정의하고, 구체적인 반례, 예상 반론과 재반론을 갖추며, 자기 평가 대신 논증으로 설득한다.",
    ], [
        ("원래 문단의 문제점을 정확히 지적했다", 2),
        ("이론을 정확히 정의해 고쳤다", 1),
        ("구체적 반례와 반론·재반론을 넣었다", 2),
        ("명료한 영어로 썼다", 1),
    ], "정의, 예, 반론이 빠져 있습니다.", "apply"),
    X("자기 점검과 독학 자료", [
        "영어 에세이를 쓴 뒤 다음을 점검하세요: 논제가 첫 문단 끝에 한 문장으로 있는가, 각 문단의 첫 문장이 그 문단의 주장인가, 반론을 가장 강한 형태로 다루었는가, 결론이 새 주장을 꺼내지 않는가.",
        "영어 실력을 기르려면 짧은 철학 글을 영어로 많이 읽으세요. 『Stanford Encyclopedia of Philosophy』(무료, 영문)의 항목 서론, Nigel Warburton 『Philosophy: The Basics』, Thomas Nagel 『What Does It All Mean?』이 좋은 출발점입니다.",
        "IPO 공식 누리집에서 지난 대회의 인용문과 상위 에세이를 볼 수 있습니다. 같은 인용문으로 직접 써 본 뒤 비교하세요. 다음 챕터 '4시간 실전 연습'에서 시간을 재고 전체 에세이를 씁니다.",
    ], "apply"),
]}
