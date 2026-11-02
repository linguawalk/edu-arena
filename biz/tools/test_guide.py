"""레벨2·3 가이드 브라우저 점검: 과목 첫 화면(선수 점검)과 모든 단원을 열어 정답을 넣고 '맞았어요'(서술형은 '핵심을 잘 짚었어요')가 나오는지 확인한다.

사용: (사이트 루트에서 python3 -m http.server 8765 실행 후)
  python3 tools/test_guide.py 2 economics micro-principles
  python3 tools/test_guide.py 2            # 레벨2 전체
"""
import json, os, sys, glob
from playwright.sync_api import sync_playwright

ROOT = os.path.join(os.path.dirname(__file__), "..")
URL = "http://localhost:8765/"


def fmt_num(a):
    try:
        v = int(a)
        if abs(v) >= 1000: return f"{v:,}"
    except ValueError: pass
    return a


def answer_cards(page, qs, label, errs):
    cards = page.locator(".qcard")
    if cards.count() != len(qs): errs.append(f"{label}: 문항 수 {cards.count()} ≠ {len(qs)}"); return
    for k, q in enumerate(qs):
        c = cards.nth(k); qt = q["qtype"]
        if qt == "numeric": c.locator("input.ans").fill(fmt_num(q["answer"]))
        elif qt == "fill_blank":
            ins = c.locator(".prompt input")
            for n, b in enumerate(q["blanks"]): ins.nth(n).fill(b["answers"][0])
        elif qt == "written": c.locator("textarea").fill(q["model_answer"])
        else: errs.append(f"{label} {q['id']}: 형식 {qt}"); continue
        btn = c.locator("button.btn:not(.ghost)")
        if btn.is_disabled(): errs.append(f"{label} {q['id']}: 확인 비활성"); continue
        btn.click()
        fb = c.locator(".qfb"); cls = fb.get_attribute("class") or ""
        if "ok" not in cls.split(): errs.append(f"{label} {q['id']}: 정답 처리 안 됨 ({qt}) {fb.inner_text()[:60]}")


def main():
    lv = sys.argv[1]; track = sys.argv[2] if len(sys.argv) > 2 else "*"; sid = sys.argv[3] if len(sys.argv) > 3 else "*"
    subs = sorted(glob.glob(os.path.join(ROOT, "content", f"level{lv}", track, sid, "subject.json")))
    errs = []; n = 0
    with sync_playwright() as p:
        b = p.chromium.launch(); page = b.new_page(viewport={"width": 1100, "height": 900})
        jserr = []
        page.on("pageerror", lambda e: jserr.append(str(e)))
        for sp in subs:
            sub = json.load(open(sp, encoding="utf-8")); t, s = sub["track"], sub["id"]
            page.goto(f"{URL}guide.html?lv={lv}&t={t}&s={s}"); page.wait_for_selector(".qcard", timeout=10000)
            answer_cards(page, sub["prereq"]["questions"], f"{s} 선수", errs); n += len(sub["prereq"]["questions"])
            for u in sub["units"]:
                d = json.load(open(os.path.join(os.path.dirname(sp), u["file"]), encoding="utf-8"))
                page.goto(f"{URL}guide.html?lv={lv}&t={t}&s={s}&u={u['no']}"); page.wait_for_selector(".qcard", timeout=10000)
                answer_cards(page, d["selfcheck"], f"{s} u{u['no']}", errs); n += len(d["selfcheck"])
            print(f"{s} 완료")
        page.goto(f"{URL}guide.html"); page.wait_for_selector(".trk", timeout=10000)
        b.close()
    for e in errs: print(" -", e)
    for e in jserr: print(" - 스크립트:", e)
    print(f"문항 {n}개 점검, 오류 {len(errs)}개, 스크립트 오류 {len(jserr)}개")


if __name__ == "__main__":
    main()
