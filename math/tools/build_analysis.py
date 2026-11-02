"""해석 트랙 전체(레벨2 대학 미적분학·상미분방정식 + 레벨3 해석학·복소해석·편미분방정식 입문) 생성"""
import guide_linalg as L2
import guide_calculus as CA, guide_ode as OD, guide_real_analysis as RA, guide_complex as CX, guide_pde as PD
import re
for name, mod in [("대학 미적분학", CA), ("상미분방정식", OD), ("해석학", RA), ("복소해석", CX), ("편미분방정식 입문", PD)]:
    # 빈칸 번호 점검: {{k}}가 1..n으로 한 번씩, blanks 수와 일치
    qs = mod.SUBJECT["prereq"]["questions"] + [q for u in mod.U for q in u["selfcheck"]]
    for q in qs:
        if q["qtype"] == "fill_blank":
            ids = [int(k) for k in re.findall(r"\{\{(\d+)\}\}", q["prompt"])]
            assert ids == list(range(1, len(q["blanks"]) + 1)), (name, q["prompt"])
    n = mod.verify(); h = L2.write_subject(mod.SUBJECT, mod.U)
    print(f"{name}: 정답 검증 {n}건, {len(mod.U)}단원, {h}시간, 문항 {len(qs)}")
print("열린 과목:", L2.write_tracks())
