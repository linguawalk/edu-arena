"""점검 스크립트: 규정값의 점검 기한과 각 값을 쓰는 레슨을 보여 준다.

사용: python3 tools/audit.py [기준일 YYYY-MM-DD] [--days 90]
기한이 지났거나 기준일로부터 days일 안에 다가오는 항목을 표시한다.
"""
import json, os, sys, glob, datetime

ROOT = os.path.join(os.path.dirname(__file__), "..", "content")
args = [a for a in sys.argv[1:] if not a.startswith("--")]
today = datetime.date.fromisoformat(args[0]) if args else datetime.date.today()
days = int(sys.argv[sys.argv.index("--days") + 1]) if "--days" in sys.argv else 90
rules = json.load(open(os.path.join(ROOT, "rules.json"), encoding="utf-8"))["rules"]
usage = {k: [] for k in rules}
for p in sorted(glob.glob(os.path.join(ROOT, "level1", "c*", "ch*", "*.json"))):
    d = json.load(open(p, encoding="utf-8"))
    rev = (d.get("lesson") or d.get("review") or {}).get("review") if isinstance(d.get("lesson") or d.get("review"), dict) else None
    for k in (rev or {}).get("rules", []):
        usage.setdefault(k, []).append((d.get("lesson") or d.get("review"))["id"])
print(f"기준일 {today}, {days}일 이내 점검 대상")
bad = 0
for k, r in sorted(rules.items(), key=lambda kv: kv[1]["review_by"]):
    due = datetime.date.fromisoformat(r["review_by"]); left = (due - today).days
    flag = "기한 지남" if left < 0 else ("임박" if left <= days else "정상")
    if flag != "정상": bad += 1
    v = r['value']; vs = f"{v:,}{r['unit']}" if isinstance(v, (int, float)) else "표 " + str(len(v)) + "구간"
    print(f"- [{flag}] {r['label']} = {vs} (점검 기한 {due}, {left}일) / 사용 레슨 {len(usage.get(k, []))}개")
    for lid in usage.get(k, []): print(f"    {lid}")
unknown = set(usage) - set(rules)
if unknown: print("rules.json에 없는 키:", unknown); bad += 1
sys.exit(1 if bad and "--strict" in sys.argv else 0)
