"""course.json에 연습 문항 수 반영"""
import json, glob
SITE = "/home/claude/site/content/level1"
for cf in sorted(glob.glob(f"{SITE}/c*/course.json")):
    c = json.load(open(cf)); tot = 0
    for chm in c["chapters"]:
        ch = json.load(open(cf.replace("course.json", chm["dir"] + "/chapter.json")))
        k = sum(l.get("practice", {}).get("questions", 0) for l in ch["lessons"])
        if k: chm["practice_questions"] = k
        else: chm.pop("practice_questions", None)
        tot += k
    if tot: c["totals"]["practice_questions"] = tot
    else: c["totals"].pop("practice_questions", None)
    json.dump(c, open(cf, "w"), ensure_ascii=False, indent=2)
    print(cf.split("/")[-2], tot)
