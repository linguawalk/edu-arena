import json, sys, glob
from playwright.sync_api import sync_playwright
BASE = "http://localhost:8765/"
files = sys.argv[1:]
errs = []
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page()
    pg.on("pageerror", lambda e: errs.append(str(e)))
    for f in files:
        d = json.load(open(f)); parts = f.split("/")
        c, ch, l = parts[-3], parts[-2][2:], parts[-1][1:3]
        url = f"{BASE}player.html?c={c}&ch={ch}&l={l}&practice=1"
        pg.goto(url); pg.wait_for_selector("#main .prompt")
        n = pg.evaluate("screens.length"); gs = pg.evaluate("new Set(screens.map(q=>q.group)).size")
        assert n == 10 and gs == min(10, len(d["practice"]["groups"])), (n, gs)
        # 전체 은행을 정답으로 풀기
        pg.evaluate("screens = data.questions; idx = 0; show()")
        bad = 0
        for i, q in enumerate(d["questions"]):
            pg.wait_for_selector("#main .prompt")
            pg.wait_for_timeout(80); ins = pg.query_selector_all("#main input")
            vals = [q["answer"]] if q["qtype"] == "numeric" else [bl["answers"][-1] for bl in q["blanks"]]
            if i % 7 == 0 and q["qtype"] == "numeric":  # 오답 먼저 한 번
                ins[0].fill("12345"); pg.click("#mainBtn")
                assert "bad" in pg.get_attribute("#fb", "class")
            for inp, v in zip(ins, vals): inp.fill(v.replace("-", "−") if i % 2 else v)
            if pg.is_disabled("#mainBtn"): print("DISABLED", q["id"], vals, pg.evaluate("[...document.querySelectorAll('#main input')].map(i=>[i.value,i.readOnly])"), pg.evaluate("[phase, api && api.ready, idx]")); break
            pg.click("#mainBtn")
            cls = pg.get_attribute("#fb", "class")
            if "ok" not in cls: bad += 1; print("WRONG", f, q["id"], q["prompt"], vals)
            pg.click("#mainBtn")
        pg.wait_for_selector(".done")
        txt = pg.inner_text(".done")
        assert "연습 완료" in txt and "세트" in txt, txt
        assert pg.inner_text("#mainBtn") == "새 문제 10개 더"
        # 다시 뽑으면 본 문항은 피해서
        pg.goto(url); pg.wait_for_selector("#main .prompt")
        print(f.split("content/")[1], "bank", len(d["questions"]), "wrong", bad)
    # 레슨 완료 화면 링크와 목록 링크
    pg.goto(BASE + "browse.html?c=" + files[0].split("/")[-3]); pg.wait_for_selector(".chapter")
    k = len(pg.query_selector_all("a.prac")); print("browse 연습 링크", k, "|", pg.inner_text(".course-head p"))
    print("1회 표시:", [a.inner_text() for a in pg.query_selector_all("a.prac")][:4])
    b.close()
print("page errors", errs)
