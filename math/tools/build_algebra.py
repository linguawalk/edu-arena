"""대수 트랙 전체(레벨2 선형대수 + 레벨3 현대대수·고급 선형대수) 생성"""
import guide_linalg as L2, guide_abstract_algebra as AA, guide_adv_linear_algebra as ALA
tot = 0
for name, mod in [("선형대수", L2), ("현대대수", AA), ("고급 선형대수", ALA)]:
    n = mod.verify(); h = L2.write_subject(mod.SUBJECT, mod.U)
    q = sum(len(u["selfcheck"]) for u in mod.U) + len(mod.SUBJECT["prereq"]["questions"])
    print(f"{name}: 정답 검증 {n}건, {len(mod.U)}단원, {h}시간, 문항 {q}")
print("열린 과목:", L2.write_tracks())
