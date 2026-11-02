"""규정값 점검: 점검 주기가 지난 항목과 각 값이 쓰인 레슨 파일을 보여 준다.

사용: python3 tools/check_facts.py [content 경로] [--today YYYY-MM-DD]
종료 코드 1 = 점검이 필요한 항목이 있음
"""
import sys, os, glob, datetime
sys.path.insert(0, os.path.dirname(__file__))
from facts import FACTS

args = [a for a in sys.argv[1:] if not a.startswith("--")]
root = args[0] if args else os.path.join(os.path.dirname(__file__), "..", "content")
today = datetime.date.today()
if "--today" in sys.argv:
    today = datetime.date.fromisoformat(sys.argv[sys.argv.index("--today") + 1])

files = {p: open(p, encoding="utf-8").read() for p in glob.glob(os.path.join(root, "level1", "c*", "ch*", "*.json")) + glob.glob(os.path.join(root, "level[23]", "*", "*", "*.json"))}
due = 0
for key, f in FACTS.items():
    checked = datetime.date.fromisoformat(f["checked"])
    left = f["cycle"] - (today - checked).days
    used = sorted(os.path.relpath(p, root) for p, s in files.items() if f["text"] in s)
    flag = "점검 필요" if left <= 0 else f"{left}일 남음"
    if left <= 0:
        due += 1
    print(f"[{flag}] {key}: {f['text']} (기준 {f['as_of']}, 출처: {f['source']}, 확인 {f['checked']})")
    for u in used:
        print(f"    - {u}")
    if not used:
        print("    - (쓰인 레슨 없음)")
print(f"\n항목 {len(FACTS)}개, 점검 필요 {due}개")
sys.exit(1 if due else 0)
