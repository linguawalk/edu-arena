"""레벨1 브라우저 점검: 모든 레슨과 복습을 열어 정답을 넣고 '맞았어요'가 나오는지 확인한다.

사용: (사이트 루트에서 python3 -m http.server 8765 실행 후)
  python3 tools/test_l1.py c1            # c1 전체
  python3 tools/test_l1.py c1 03 04      # c1의 챕터 3, 4만
숫자 정답이 1000 이상이면 천 단위 쉼표를 넣은 형태로 입력해 쉼표 처리도 함께 점검한다.
"""
import json, os, sys, glob
from playwright.sync_api import sync_playwright

ROOT = os.path.join(os.path.dirname(__file__), "..")
URL = "http://localhost:8765/"
course = sys.argv[1]
only = set(sys.argv[2:])

ORDER_JS = """(ans) => {
  const want = ans; for (let guard = 0; guard < 50; guard++){
    const lis = [...document.querySelectorAll('ol.order li')], cur = lis.map(li => li.querySelector('.t').textContent);
    let moved = false;
    for (let k = 0; k < want.length; k++){ const at = cur.indexOf(want[k]); if (at > k){ lis[at].querySelectorAll('button')[0].click(); moved = true; break; } }
    if (!moved) return true; }
  return false; }"""


def fmt_num(a):
    try:
        v = int(a)
        if abs(v) >= 1000: return f"{v:,}"
    except ValueError: pass
    return a


def run_page(page, url, screens, label, errs):
    page.goto(url, wait_until="domcontentloaded"); page.wait_for_selector("main h1, main .prompt", timeout=15000)
    for k, s in enumerate(screens):
        btn = page.locator("#mainBtn")
        if s["type"] == "explain":
            btn.click(); continue
        if s["type"] == "example":
            for _ in range(len(s["steps"]) + 2):
                t = btn.inner_text(); btn.click()
                if t == "계속": break
            continue
        q = s; qt = q["qtype"]
        if qt == "numeric": page.fill("input.ans", fmt_num(q["answer"]))
        elif qt == "fill_blank":
            ins = page.locator(".prompt input")
            for n, b in enumerate(q["blanks"]): ins.nth(n).fill(b["answers"][0])
        elif qt == "ordering":
            t = {it["id"]: it["text"] for it in q["items"]}
            page.evaluate(ORDER_JS, [t[i] for i in q["answer_order"]])
        elif qt == "written": page.fill("textarea", q["model_answer"])
        elif qt == "journal":
            sides = page.locator(".journal .side")
            for si, key in enumerate(("debit", "credit")):
                lines = sides.nth(si).locator(".line")
                for k, (acc, amt) in enumerate(q["answer"][key][::-1]):  # 순서를 바꿔 넣어 순서 무관 채점 점검
                    lines.nth(k).locator("select").select_option(acc); lines.nth(k).locator("input").fill(fmt_num(str(amt)))
        else: errs.append(f"{label} {q['id']}: 지원하지 않는 형식 {qt}");
        if btn.is_disabled(): errs.append(f"{label} {q['id']}: 확인 버튼 비활성"); return
        btn.click()
        cls = page.get_attribute("#fb", "class") or ""
        if "ok" not in cls.split():
            errs.append(f"{label} {q['id']}: 정답 처리 안 됨 ({qt})")
            if page.locator("#revealBtn").is_visible(): pass
            btn.click()  # 두 번째 시도
            if page.locator("#revealBtn").is_visible(): page.click("#revealBtn")
        page.locator("#mainBtn").click()
    page.wait_for_selector(".done", timeout=5000)


def main():
    errs = []; n = 0
    with sync_playwright() as p:
        b = p.chromium.launch(); page = b.new_page(viewport={"width": 1100, "height": 900})
        jserr = []
        page.on("pageerror", lambda e: jserr.append(str(e)))
        page.on("console", lambda m: jserr.append(m.text) if m.type == "error" and "ERR_TUNNEL" not in m.text and "fonts" not in m.text else None)
        for chd in sorted(glob.glob(os.path.join(ROOT, "content", "level1", course, "ch*"))):
            ch = os.path.basename(chd)[2:]
            if only and ch not in only: continue
            for f in sorted(glob.glob(os.path.join(chd, "l*.json"))):
                d = json.load(open(f, encoding="utf-8")); l = os.path.basename(f)[1:3]
                before = len(errs)
                run_page(page, f"{URL}player.html?c={course}&ch={ch}&l={l}", d["screens"], d["lesson"]["id"], errs)
                n += sum(s["type"] == "question" for s in d["screens"])
            d = json.load(open(os.path.join(chd, "review.json"), encoding="utf-8"))
            run_page(page, f"{URL}player.html?c={course}&ch={ch}&review=1", d["questions"], d["review"]["id"], errs)
            n += len(d["questions"])
            print(f"ch{ch} 완료", flush=True)
        page.goto(f"{URL}browse.html?c={course}"); page.wait_for_selector(".chapter", timeout=5000)
        b.close()
    print(f"문항 {n}개 점검, 오류 {len(errs)}개, 스크립트 오류 {len(jserr)}개")
    for e in errs + jserr: print(" -", e)
    sys.exit(1 if errs or jserr else 0)


main()
