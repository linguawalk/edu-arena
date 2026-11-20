/* edu-arena 튜터 — 브라우저 안에서만 동작하는 규칙 기반 학습 도우미.
 * 서버·AI 호출이 없어 운영 비용이 들지 않는다. 기존 문항 JSON(hint, explanation, answer)만으로 동작한다.
 *   Tutor.hints(q)                  단계별 힌트 목록 (저작 힌트 → 풀이 첫 단계 → 풀이 중간까지)
 *   Tutor.diagnoseNumeric(q, raw)   숫자형 오답의 흔한 실수 유형 진단 {code, message} | null
 *   Tutor.diagnoseBlanks(q, vals)   빈칸형에서 맞은 빈칸 알려 주기 {code, message} | null
 *   Tutor.record(r)                 개념별 풀이 기록 (이 기기의 localStorage)
 *   Tutor.weakest(n)                정답률이 낮은 개념 n개
 */
(function (root) {
  "use strict";

  /* ---------- 숫자 해석 (플레이어의 채점 정규화와 같은 규칙) ---------- */
  const SUP = {"⁰":"^0","¹":"^1","²":"^2","³":"^3","⁴":"^4","⁵":"^5","⁶":"^6","⁷":"^7","⁸":"^8","⁹":"^9"};
  function norm(s) {
    return String(s).trim().replace(/\s+/g, "").replace(/[−–—]/g, "-")
      .replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹]/g, c => SUP[c]).replace(/×/g, "*")
      .replace(/<=/g, "≤").replace(/>=/g, "≥").replace(/!=/g, "≠").toLowerCase();
  }
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
  function diagnoseBlanks(q, values) {
    if (!q.blanks || q.blanks.length < 2 || (q.unordered_groups && q.unordered_groups.length)) return null;
    const right = [];
    q.blanks.forEach((b, k) => { if (norm(values[k] == null ? "" : values[k]) && b.answers.map(norm).includes(norm(values[k]))) right.push(k + 1); });
    if (!right.length || right.length === q.blanks.length) return null;
    const rest = q.blanks.map((_, k) => k + 1).filter(n => !right.includes(n));
    return {code: "partial_blanks", message: `맞은 빈칸: ${right.join(", ")}번. 다시 확인할 빈칸: ${rest.join(", ")}번.`};
  }

  /* ---------- 단계별 힌트 ---------- */
  // 정답이 드러나는 줄은 힌트로 쓰지 않는다.
  function answerStrings(q) {
    if (q.qtype === "numeric") return [norm(q.answer)];
    if (q.qtype === "fill_blank") return (q.blanks || []).flatMap(b => b.answers.map(norm));
    return [];
  }
  function leaks(line, answers) {
    const n = norm(line).replace(/[가-힣]+$/, "");      // 끝의 단위("개", "명" 등) 제거
    return answers.some(a => {
      if (!a) return false;
      if (n === a || n.endsWith("=" + a) || n.endsWith("→" + a)) return true;
      if (a.replace(/[^0-9]/g, "").length >= 2) {        // 두 자리 이상 정답은 줄 어디에 있어도 막는다
        const esc = a.replace(/[.*+?^${}()|[\]\\\/]/g, "\\$&");
        return new RegExp("(^|[^0-9.])" + esc + "($|[^0-9.])").test(n);
      }
      return false;
    });
  }
  function hints(q) {
    const out = [];
    if (q.hint) out.push(String(q.hint));
    if (q.qtype !== "numeric" && q.qtype !== "fill_blank") return out;
    const lines = String(q.explanation || "").split("\n").map(t => t.trim()).filter(Boolean);
    if (lines.length < 2) return out;
    const answers = answerStrings(q);
    let steps = 0;
    while (steps < lines.length - 1 && !leaks(lines[steps], answers)) steps++;   // 마지막 줄(결론)은 항상 숨김
    if (steps >= 1) out.push("풀이의 첫 단계: " + lines[0]);
    if (steps >= 2) out.push("이어서: " + lines.slice(1, steps).join("\n"));   // 줄바꿈은 화면에서 white-space:pre-line으로 표시
    return out;
  }

  /* ---------- 개념별 기록 (이 기기에만 저장) ---------- */
  const KEY = "edu-arena:tutor:v1";
  function load() { try { return JSON.parse(root.localStorage.getItem(KEY)) || {v: 1, c: {}}; } catch (e) { return {v: 1, c: {}}; } }
  function save(o) { try { root.localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {} }

  // r: {concept, title, href, first, hints, revealed, codes}
  // first = 힌트 없이 첫 시도에 맞힘. 이것이 ‘완전히 익힌 문항’의 기준이다.
  function record(r) {
    if (!r || !r.concept) return;
    const o = load();
    const c = o.c[r.concept] || (o.c[r.concept] = {n: 0, ok: 0, hint: 0, rev: 0, w: {}, title: r.title || r.concept, href: r.href || "", at: 0});
    c.n++; if (r.first) c.ok++; c.hint += r.hints || 0; if (r.revealed) c.rev++;
    (r.codes || []).forEach(k => { c.w[k] = (c.w[k] || 0) + 1; });
    if (r.title) c.title = r.title;
    if (r.href) c.href = r.href;
    c.at = Date.now();
    const keys = Object.keys(o.c);
    if (keys.length > 400) keys.sort((x, y) => o.c[x].at - o.c[y].at).slice(0, 50).forEach(k => delete o.c[k]);
    save(o);
  }

  function weakest(n, minAttempts, maxRate) {
    n = n || 3; minAttempts = minAttempts || 3; maxRate = maxRate == null ? 0.7 : maxRate;
    const o = load();
    return Object.keys(o.c).map(k => ({concept: k, title: o.c[k].title, href: o.c[k].href, n: o.c[k].n, rate: o.c[k].ok / o.c[k].n, w: o.c[k].w}))
      .filter(x => x.n >= minAttempts && x.rate < maxRate)
      .sort((a, b) => a.rate - b.rate || b.n - a.n).slice(0, n);
  }

  const api = {hints, diagnoseNumeric, diagnoseBlanks, record, weakest, _norm: norm, _frac: frac};
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.Tutor = api;
})(typeof window !== "undefined" ? window : globalThis);
