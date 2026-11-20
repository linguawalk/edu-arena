/* edu-arena 튜터 — 브라우저 안에서만 동작하는 규칙 기반 학습 도우미.
 * 서버·AI 호출이 없어 운영 비용이 들지 않는다. 기존 문항 JSON(hint, explanation, answer)만으로 동작한다.
 * 모든 과목 플레이어가 이 파일 하나를 함께 쓴다.
 *
 *   Tutor.hints(q)                      단계별 힌트 목록 (저작 힌트 → 풀이 첫 단계 → 풀이 중간까지)
 *   Tutor.diagnoseNumeric(q, raw)       숫자형 오답의 흔한 실수 유형 진단 {code, message} | null
 *   Tutor.diagnoseBlanks(q, vals, norm) 빈칸형에서 맞은 빈칸 알려주기 (norm: 플레이어의 채점 정규화 함수)
 *   Tutor.concept(q, ctx)               문항이 속한 개념 {id, title, href, subject} | null
 *   Tutor.record(r)                     개념별 풀이 기록 (이 기기의 localStorage)
 *   Tutor.weakest(n)                    정답률이 낮은 개념 n개
 *   Tutor.weakBox(excludeLessonId)      "다시 보면 좋은 개념" 상자(DOM) | null (지금 풀고 있는 레슨은 제외)
 */
(function (root) {
  "use strict";

  /* ---------- 숫자 해석 ---------- */
  const SUP = {"⁰":"^0","¹":"^1","²":"^2","³":"^3","⁴":"^4","⁵":"^5","⁶":"^6","⁷":"^7","⁸":"^8","⁹":"^9"};
  function norm(s) {
    return String(s).trim().replace(/\s+/g, "").replace(/[−–—]/g, "-")
      .replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹]/g, c => SUP[c]).replace(/×/g, "*")
      .replace(/<=/g, "≤").replace(/>=/g, "≥").replace(/!=/g, "≠").toLowerCase();
  }
  // 정답 노출 검사용: 과목마다 다른 표기(H₂O, H2O, x^2 등)를 최대한 같게 본다 (더 많이 걸러내는 쪽이 안전)
  const SUB = {"₀":"0","₁":"1","₂":"2","₃":"3","₄":"4","₅":"5","₆":"6","₇":"7","₈":"8","₉":"9","⁺":"+","⁻":"-"};
  const loose = s => norm(s).replace(/[₀-₉⁺⁻]/g, c => SUB[c]).replace(/[\^°{}_]/g, "");

  function frac(s) {
    s = norm(s).replace(/^\+/, "");
    let m;
    if ((m = s.match(/^(-?\d+)\/(-?\d+)$/))) { const d = +m[2]; return d === 0 ? null : [+m[1], d]; }
    if ((m = s.match(/^(-?)(\d*)\.(\d+)$/))) { const den = Math.pow(10, m[3].length); const n = +(m[2] || 0) * den + +m[3]; return [m[1] ? -n : n, den]; }
    if (/^-?\d+$/.test(s)) return [+s, 1];
    return null;
  }
  const gcd = (a, b) => { a = Math.abs(a); b = Math.abs(b); while (b) { [a, b] = [b, a % b]; } return a; };
  function reduce(f) {
    let n = f[0], d = f[1];
    if (d < 0) { n = -n; d = -d; }
    const g = gcd(n, d) || 1;
    return [n / g, d / g];
  }
  const val = f => f[0] / f[1];
  const close = (x, y) => Math.abs(x - y) <= 1e-9 * Math.max(1, Math.abs(x), Math.abs(y));

  /* ---------- 오답 진단: 숫자형 ---------- */
  function promptNumbers(prompt) {
    const out = [];
    const re = /-?\d+(?:\.\d+)?(?:\/\d+)?/g;
    let m;
    const s = String(prompt).replace(/[−–—]/g, "-");
    while ((m = re.exec(s))) { const f = frac(m[0]); if (f) out.push(val(reduce(f))); }
    return out;
  }
  function digitsKey(n) { return String(Math.abs(n)).split("").sort().join(""); }

  // 정답이 아닌 입력이 들어왔을 때만 호출한다. 정답 자체를 알려 주지 않는 완곡한 문장만 쓴다.
  function diagnoseNumeric(q, raw) {
    const u0 = frac(raw), a0 = frac(q.answer);
    if (!u0 || !a0) return null;
    const u = reduce(u0), a = reduce(a0), uv = val(u), av = val(a);
    if (close(uv, av)) return null;                       // 같은 값이면 진단 대상이 아님
    if (av === 0) return null;                            // 0이 정답이면 비율·부호 규칙이 의미 없음

    if (close(uv, -av))
      return {code: "sign", message: "부호를 다시 확인해 보세요."};

    if (!(Math.abs(a[0]) === 1 && Math.abs(a[1]) === 1) && u[0] === a[1] && u[1] === a[0] && !(u[0] === 1 && u[1] === 1))
      return {code: "reciprocal", message: "분자와 분모를 서로 바꿔 쓴 것 같아요."};

    if (q.answer_format === "fraction" && a[1] !== 1) {
      if (u[1] === a[1] && u[0] !== a[0]) return {code: "numerator", message: "분모는 맞아요. 분자를 다시 계산해 보세요."};
      if (u[0] === a[0] && u[1] !== a[1]) return {code: "denominator", message: "분자는 맞아요. 분모를 다시 계산해 보세요."};
    }

    const ratio = uv / av;
    if ([10, 0.1, 100, 0.01].some(r => close(ratio, r)))
      return {code: "magnitude", message: "자릿수(0의 개수나 소수점 위치)가 어긋난 것 같아요."};

    if (Math.abs(av) >= 2 && (close(ratio, 2) || close(ratio, 0.5)))
      return {code: "factor2", message: "2를 곱하거나 나누는 단계에서 실수가 없었는지 확인해 보세요."};

    if (Number.isInteger(uv) && Number.isInteger(av) && Math.abs(av) >= 2 && Math.abs(uv - av) === 1)
      return {code: "off_by_one", message: "거의 맞았어요. 마지막 계산이나 ‘포함하는지 여부’를 다시 확인해 보세요."};

    if (Number.isInteger(uv) && Number.isInteger(av) && Math.abs(av) >= 10 && digitsKey(uv) === digitsKey(av))
      return {code: "digit_swap", message: "숫자는 비슷한데 자리가 바뀐 것 같아요. 자릿수를 다시 확인해 보세요."};

    const nums = promptNumbers(q.prompt);
    if (nums.length >= 2 && nums.some(n => close(n, uv)))
      return {code: "echo_operand", message: "문제에 나온 수를 그대로 쓴 것 같아요. 구하려는 값이 무엇인지 문제를 다시 읽어 보세요."};

    return null;
  }

  /* ---------- 오답 진단: 빈칸형 (맞은 칸 알려 주기) ---------- */
  // normFn: 플레이어가 채점에 쓰는 정규화 함수. 과목마다 다르므로(예: 과학은 대소문자 구분) 가능하면 넘겨 받는다.
  function diagnoseBlanks(q, values, normFn) {
    const nf = normFn || norm;
    if (!q.blanks || q.blanks.length < 2 || (q.unordered_groups && q.unordered_groups.length)) return null;
    const right = [];
    q.blanks.forEach((b, k) => {
      const v = nf(values[k] == null ? "" : values[k]);
      if (v && b.answers.map(nf).includes(v)) right.push(k + 1);
    });
    if (!right.length || right.length === q.blanks.length) return null;
    const rest = q.blanks.map((_, k) => k + 1).filter(n => !right.includes(n));
    return {code: "partial_blanks", message: `맞은 빈칸: ${right.join(", ")}번. 다시 확인할 빈칸: ${rest.join(", ")}번.`};
  }

  /* ---------- 단계별 힌트 ---------- */
  // 정답이 드러나는 줄은 힌트로 쓰지 않는다.
  //  - 숫자 정답: 줄이 ‘=정답’으로 끝나거나, 두 자리 이상이면 줄 어디에 있어도 막는다.
  //  - 글자 정답(두 글자 이상): 줄 어디에든 들어 있으면 막는다.
  //  - 한 글자 글자 정답: 줄에 흔히 나오는 글자라 판별이 어려우므로 풀이에서 뽑은 힌트를 쓰지 않는다.
  function answerStrings(q) {
    if (q.qtype === "numeric") return [loose(q.answer)];
    if (q.qtype === "fill_blank") return (q.blanks || []).flatMap(b => b.answers.map(loose));
    return [];
  }
  const NUMERIC = /^[-+]?[\d./]+$/;
  function leaks(line, answers) {
    const full = loose(line), stripped = full.replace(/[가-힣]+$/, "");      // 끝의 단위("개", "명" 등) 제거
    return answers.some(a => {
      if (!a) return false;
      if (NUMERIC.test(a)) {
        if (stripped === a || stripped.endsWith("=" + a) || stripped.endsWith("→" + a)) return true;
        if (a.replace(/[^0-9]/g, "").length >= 2) {
          const esc = a.replace(/[.*+?^${}()|[\]\\\/]/g, "\\$&");
          return new RegExp("(^|[^0-9.])" + esc + "($|[^0-9.])").test(stripped);
        }
        return false;
      }
      if (a.length >= 2) return full.includes(a);
      return full === a || full.endsWith("=" + a) || full.endsWith("→" + a);
    });
  }
  function hints(q) {
    const out = [];
    if (q.hint) out.push(String(q.hint));
    if (q.qtype !== "numeric" && q.qtype !== "fill_blank") return out;
    const lines = String(q.explanation || "").split("\n").map(t => t.trim()).filter(Boolean);
    if (lines.length < 2) return out;
    const answers = answerStrings(q);
    if (answers.some(a => a && !NUMERIC.test(a) && a.length < 2)) return out;     // 한 글자 글자 정답
    let steps = 0;
    while (steps < lines.length - 1 && !leaks(lines[steps], answers)) steps++;   // 마지막 줄(결론)은 항상 숨김
    if (steps >= 1) out.push("풀이의 첫 단계: " + lines[0]);
    if (steps >= 2) out.push("이어서: " + lines.slice(1, steps).join("\n"));   // 줄바꿈은 white-space:pre-line으로 표시
    return out;
  }

  /* ---------- 개념 식별 ---------- */
  // 과목 구분: 같은 도메인을 쓰는 여러 플레이어(/math/, /sci/, /socio/olympiad/ …)가 기록을 섞지 않도록 경로를 접두어로 쓴다.
  const nsOf = () => root.location.pathname.replace(/^\/+/, "").replace(/\/?[^/]*$/, "") || "root";
  const baseOf = () => root.location.pathname.replace(/[^/]*$/, "");
  const subjectOf = () => { const t = String(root.document && root.document.title || "").split(" · "); return t.length >= 3 ? t[t.length - 2] : ""; };

  // ctx: {data, chapterMeta, isReview, course, ch, level}
  function concept(q, ctx) {
    const d = ctx.data || {}, ns = nsOf(), subject = subjectOf();
    const lid = q.source_lesson || (!ctx.isReview && d.lesson && d.lesson.id);
    const m = lid && /^(.*)-ch(\d+)-l(\d+)$/.exec(lid);
    if (m) {
      const t = ctx.chapterMeta && ctx.chapterMeta.lessons && ctx.chapterMeta.lessons.find(l => l.id === lid);
      const title = (t && t.title) || (d.lesson && d.lesson.id === lid ? d.lesson.title : "");
      if (title) {
        const p = new URLSearchParams();
        if (ctx.level && ctx.level !== "1") p.set("level", ctx.level);
        p.set("c", ctx.course || m[1]); p.set("ch", m[2]); p.set("l", m[3]);
        return {id: ns + ":" + lid, title, subject, href: baseOf() + "player.html?" + p.toString()};
      }
    }
    if (d.chapter) return {id: ns + ":" + d.chapter.id, title: d.chapter.title, subject,
      href: baseOf() + "browse.html?c=" + encodeURIComponent(ctx.course || "") + "#ch" + (ctx.ch || "")};
    return null;
  }

  /* ---------- 개념별 기록 (이 기기에만 저장) ---------- */
  const KEY = "edu-arena:tutor:v1";
  function load() { try { return JSON.parse(root.localStorage.getItem(KEY)) || {v: 1, c: {}}; } catch (e) { return {v: 1, c: {}}; } }
  function save(o) { try { root.localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {} }

  // r: {concept, title, href, subject, first, hints, revealed, codes}
  // first = 힌트 없이 첫 시도에 맞힘. 이것이 ‘완전히 익힌 문항’의 기준이다.
  function record(r) {
    if (!r || !r.concept) return;
    const o = load();
    const c = o.c[r.concept] || (o.c[r.concept] = {n: 0, ok: 0, hint: 0, rev: 0, w: {}, title: r.title || r.concept, href: r.href || "", subject: r.subject || "", at: 0});
    c.n++; if (r.first) c.ok++; c.hint += r.hints || 0; if (r.revealed) c.rev++;
    (r.codes || []).forEach(k => { c.w[k] = (c.w[k] || 0) + 1; });
    if (r.title) c.title = r.title;
    if (r.href) c.href = r.href;
    if (r.subject) c.subject = r.subject;
    c.at = Date.now();
    const keys = Object.keys(o.c);
    if (keys.length > 600) keys.sort((x, y) => o.c[x].at - o.c[y].at).slice(0, 60).forEach(k => delete o.c[k]);
    save(o);
  }

  function weakest(n, minAttempts, maxRate) {
    n = n || 3; minAttempts = minAttempts || 3; maxRate = maxRate == null ? 0.7 : maxRate;
    const o = load();
    return Object.keys(o.c).map(k => ({concept: k, title: o.c[k].title, href: o.c[k].href, subject: o.c[k].subject, n: o.c[k].n, rate: o.c[k].ok / o.c[k].n, w: o.c[k].w}))
      .filter(x => x.n >= minAttempts && x.rate < maxRate)
      .sort((a, b) => a.rate - b.rate || b.n - a.n).slice(0, n);
  }

  /* ---------- 화면 조각 (스타일을 자체 포함해 플레이어마다 CSS를 고치지 않아도 된다) ---------- */
  function injectStyle() {
    const doc = root.document;
    if (!doc || !doc.head || doc.getElementById("tutor-style")) return;
    const st = doc.createElement("style"); st.id = "tutor-style";
    st.textContent = ".hintbox p{margin:0;white-space:pre-line}.hintbox p+p{margin-top:8px}.tutornote{margin:6px 0 0;font-size:15px}";
    doc.head.appendChild(st);
  }
  function weakBox(excludeLessonId) {
    const w = weakest(3).filter(x => x.concept !== nsOf() + ":" + excludeLessonId);
    if (!w.length) return null;
    const doc = root.document, box = doc.createElement("div");
    box.style.cssText = "margin:22px 0 0;padding:14px 16px;border-radius:10px;background:var(--blue-soft,#E7ECFA);font-size:16px;line-height:1.6";
    const h = doc.createElement("b"); h.textContent = "다시 보면 좋은 개념"; box.appendChild(h);
    const ul = doc.createElement("ul"); ul.style.cssText = "margin:6px 0 0;padding-left:1.2em";
    w.forEach(x => {
      const li = doc.createElement("li"), a = doc.createElement(x.href ? "a" : "span");
      if (x.href) { a.href = x.href; a.style.cssText = "color:var(--blue,#1D3FA8);font-weight:700"; }
      a.textContent = (x.subject ? x.subject + " · " : "") + x.title; li.appendChild(a);
      li.appendChild(doc.createTextNode(` — 힌트 없이 한 번에 맞힌 비율 ${Math.round(x.rate * 100)}% (${x.n}문항)`));
      ul.appendChild(li);
    });
    box.appendChild(ul);
    return box;
  }
  injectStyle();

  const api = {hints, diagnoseNumeric, diagnoseBlanks, concept, record, weakest, weakBox, _norm: norm, _frac: frac, _loose: loose};
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.Tutor = api;
})(typeof window !== "undefined" ? window : globalThis);
