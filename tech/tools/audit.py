"""Arena 사이트 콘텐츠 점검 보고서 (math·sci·tech-arena 공통으로 쓸 수 있음).

1) 점검 기한: 단원·과목의 review.next, content/standards.json 항목의 next가 지났거나 곧 돌아오는 것
2) 외부 링크(--links): 가이드의 추천 자료와 선수 링크 가운데 http(s) 주소를 실제로 열어 확인

사용:
  python3 tools/audit.py                   # 이 사이트, 점검 기한만
  python3 tools/audit.py --links           # 링크 검사 포함 (인터넷 필요, 몇 분 걸림)
  python3 tools/audit.py --ahead 3         # 앞으로 3개월 안에 돌아오는 점검도 포함 (기본 2)
  python3 tools/audit.py --out audit.md    # 보고서를 파일로 저장
  python3 tools/audit.py ../sci-arena      # 다른 사이트 저장소 점검
보고서를 Claude에게 주면 해당 항목만 고칩니다.
"""
import argparse, datetime, glob, json, os, sys, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))


def months_ahead(ym, n):
    y, m = map(int, ym.split("-")); m += n
    return f"{y + (m - 1) // 12}-{(m - 1) % 12 + 1:02d}"


def collect(site):
    content = os.path.join(site, "content")
    reviews, links = [], {}
    for path in sorted(glob.glob(os.path.join(content, "level*", "*", "*", "*.json"))):
        d = json.load(open(path, encoding="utf-8"))
        rel = os.path.relpath(path, site)
        name = d.get("title", "")
        if d.get("type") == "guide_unit":
            name = f"{d['subject']} {d['no']}단원 {d['title']}"
        # 레벨1 챕터의 "review"는 복습 레슨이므로, 가이드 과목·단원의 점검 정보만 본다
        if d.get("type") in ("guide_unit", "guide_subject") and isinstance(d.get("review"), dict) and "basis" in d["review"]:
            reviews.append((d["review"]["next"], rel, name, d["review"]))
        for r in d.get("resources", []):
            if str(r.get("url", "")).startswith("http"): links.setdefault(r["url"], []).append(rel)
        for l in d.get("prereq", {}).get("links", []):
            if str(l.get("href", "")).startswith("http"): links.setdefault(l["href"], []).append(rel)
    std = {}
    sp = os.path.join(content, "standards.json")
    if os.path.exists(sp): std = json.load(open(sp, encoding="utf-8")).get("items", {})
    return reviews, std, links


def check_url(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (arena-audit)"})
    for method in ("HEAD", "GET"):
        req.method = method
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                return url, r.status, r.geturl()
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 405, 400, 501): continue
            return url, e.code, ""
        except Exception as e:
            if method == "HEAD": continue
            return url, f"오류: {type(e).__name__}", ""
    return url, "오류", ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("site", nargs="?", default=os.path.dirname(HERE))
    ap.add_argument("--links", action="store_true")
    ap.add_argument("--ahead", type=int, default=2)
    ap.add_argument("--out")
    a = ap.parse_args()
    today = datetime.date.today().strftime("%Y-%m")
    limit = months_ahead(today, a.ahead)
    reviews, std, links = collect(a.site)
    out = [f"# 콘텐츠 점검 보고서 — {os.path.basename(os.path.abspath(a.site))} ({datetime.date.today()})", ""]

    due = [r for r in reviews if r[0] <= limit]
    out.append(f"## 점검 기한 (오늘 {today}, {a.ahead}개월 앞 {limit}까지)")
    out.append(f"review가 붙은 단원·과목 {len(reviews)}개 가운데 {len(due)}개가 대상입니다.")
    for nxt, rel, name, r in sorted(due):
        flag = "지남" if nxt < today else ("이번 달" if nxt == today else "곧")
        out.append(f"- [{flag} {nxt}] {name} — 근거: {r['basis']} / 확인: {r['checked']} / 확인할 것: {r['watch']} ({rel})")
    sdue = [(v.get("next", ""), k, v) for k, v in std.items() if v.get("next", "9999") <= limit]
    out += ["", f"## 규정값 (content/standards.json {len(std)}개 가운데 {len(sdue)}개)"]
    for nxt, k, v in sorted(sdue):
        out.append(f"- [{nxt}] {k} = {v.get('value')} {v.get('unit', '')} — {v.get('text', '')} ({v.get('basis', '')} {v.get('clause', '')})")

    if a.links:
        out += ["", f"## 외부 링크 ({len(links)}개)"]
        with ThreadPoolExecutor(8) as ex:
            res = list(ex.map(check_url, sorted(links)))
        bad = [(u, st, fin) for u, st, fin in res if not (isinstance(st, int) and st < 400)]
        moved = [(u, st, fin) for u, st, fin in res if isinstance(st, int) and st < 400 and fin and fin.rstrip("/") != u.rstrip("/")]
        out.append(f"열리지 않는 링크 {len(bad)}개, 다른 주소로 옮겨진 링크 {len(moved)}개")
        for u, st, _ in bad: out.append(f"- [깨짐 {st}] {u} — 쓰는 곳: {', '.join(sorted(set(links[u]))[:3])}")
        for u, st, fin in moved: out.append(f"- [이동] {u} → {fin}")
    else:
        out += ["", f"외부 링크 {len(links)}개는 검사하지 않았습니다. --links를 붙이면 검사합니다."]

    text = "\n".join(out) + "\n"
    if a.out: open(a.out, "w", encoding="utf-8").write(text)
    sys.stdout.write(text)


if __name__ == "__main__":
    main()
