// 튜터 단위 테스트 + 전 과목 문항 점검. 실행: node tools/test_tutor.js
const fs = require("fs"), path = require("path");
const T = require(require("path").resolve(__dirname, "../assets/tutor.js"));
let fail = 0;
const eq = (name, got, want) => { const ok = JSON.stringify(got) === JSON.stringify(want); if (!ok){ fail++; console.log("FAIL", name, "got", JSON.stringify(got), "want", JSON.stringify(want)); } };
const num = (answer, fmt, prompt) => ({qtype:"numeric", answer, answer_format: fmt || "integer", prompt: prompt || "계산하세요.", tolerance: 0});
const code = (q, raw) => { const d = T.diagnoseNumeric(q, raw); return d && d.code; };

// --- 단위 테스트 ---
eq("sign", code(num("-2"), "2"), "sign");
eq("sign unicode minus", code(num("−2"), "2"), "sign");
eq("sign zero answer", code(num("0"), "0"), null);
eq("same value (unreduced) -> null", code(num("-1/3","fraction"), "-2/6"), null);
eq("reciprocal", code(num("3/4","fraction"), "4/3"), "reciprocal");
eq("reciprocal int", code(num("5"), "1/5"), "reciprocal");
eq("numerator", code(num("3/8","fraction"), "5/8"), "numerator");
eq("denominator", code(num("3/8","fraction"), "3/10"), "denominator");
eq("magnitude x10", code(num("12"), "120"), "magnitude");
eq("magnitude /10", code(num("0.5","decimal"), "0.05"), "magnitude");
eq("factor2 double", code(num("12"), "24"), "factor2");
eq("factor2 half", code(num("12"), "6"), "factor2");
eq("off by one", code(num("12"), "11"), "off_by_one");
eq("off by one tiny answer skipped", code(num("1"), "2"), null);
eq("digit swap", code(num("12"), "21"), "digit_swap");
eq("echo operand", code(num("6","integer","18과 24의 최대공약수는?"), "24"), "echo_operand");
eq("garbage input", code(num("12"), "abc"), null);
eq("empty input", code(num("12"), ""), null);
eq("yes/no question 0 vs 1", code(num("0"), "1"), null);
eq("yes/no question 1 vs 0", code(num("1"), "0"), null);
eq("blanks partial", (T.diagnoseBlanks({blanks:[{answers:["2"]},{answers:["3"]},{answers:["5"]}]}, ["2","4","5"])||{}).message, "맞은 빈칸: 1, 3번. 다시 확인할 빈칸: 2번.");
eq("blanks none right", T.diagnoseBlanks({blanks:[{answers:["2"]},{answers:["3"]}]}, ["9","8"]), null);
eq("blanks single blank skipped", T.diagnoseBlanks({blanks:[{answers:["2"]}]}, ["9"]), null);
eq("blanks empty not counted right", T.diagnoseBlanks({blanks:[{answers:[""]},{answers:["3"]}]}, ["","8"]), null);

// 힌트: 정답이 드러나는 줄 차단
const q1 = {qtype:"numeric", answer:"12", hint:"소인수분해하세요.", explanation:"84 = 2² × 3 × 7\n지수에 1씩 더해 곱합니다: (2 + 1) × (1 + 1) × (1 + 1)\n= 12개"};
eq("hints q1", T.hints(q1), ["소인수분해하세요.", "풀이의 첫 단계: 84 = 2² × 3 × 7", "이어서: 지수에 1씩 더해 곱합니다: (2 + 1) × (1 + 1) × (1 + 1)"]);
const q2 = {qtype:"numeric", answer:"-2", hint:"곱셈을 먼저 하세요.", explanation:"곱셈을 먼저: (−4) × 3 = −12\n−12 − (−10) = −12 + 10\n= −2"};
eq("hints q2 blocks last", T.hints(q2).length, 3);
const q3 = {qtype:"numeric", answer:"12", explanation:"2 + 10 = 12\n따라서 12"};
eq("hints q3 leak on first line -> none", T.hints(q3), []);
eq("hints single-line explanation", T.hints({qtype:"numeric", answer:"3", hint:"h", explanation:"한 줄"}), ["h"]);
eq("hints non-numeric only authored", T.hints({qtype:"ordering", hint:"h", explanation:"a\nb\nc"}), ["h"]);

const qt = {qtype:"fill_blank", blanks:[{answers:["삼권분립"]}], explanation:"삼권분립은 권력을 나눕니다\n입법·행정·사법으로 나뉩니다\n따라서 삼권분립"};
eq("text answer leaks on first line -> no derived", T.hints(qt), []);
const qt2 = {qtype:"fill_blank", blanks:[{answers:["삼권분립"]}], explanation:"권력을 셋으로 나눕니다\n입법·행정·사법으로 나뉩니다\n그 원리를 무엇이라 하는가"};
eq("text answer not in lines -> derived", T.hints(qt2).length, 2);
eq("single-char text answer -> no derived", T.hints({qtype:"fill_blank", blanks:[{answers:["가"]}], explanation:"a\nb\nc"}), []);
eq("chem loose leak (H₂O vs H2O): stops before leaking line", T.hints({qtype:"fill_blank", blanks:[{answers:["H₂O"]}], explanation:"수소와 산소가 결합합니다\n생성물은 H2O입니다\n끝"}), ["풀이의 첫 단계: 수소와 산소가 결합합니다"]);
eq("blanks custom norm (case-sensitive)", (T.diagnoseBlanks({blanks:[{answers:["Mg"]},{answers:["Na"]}]}, ["mg","Na"], s => String(s).trim()) || {}).message, "맞은 빈칸: 2번. 다시 확인할 빈칸: 1번.");

// --- 말뭉치 점검 ---
const roots = ["math","sci","socio","biz","tech","lit","arts"].map(x => require("path").resolve(__dirname, "..", x, "content"));
const qs = [];
const walkAll = (root) => (function walk(dir){ for (const e of fs.readdirSync(dir, {withFileTypes:true})) { const p = path.join(dir, e.name);
  if (e.isDirectory()) walk(p); else if (e.name.endsWith(".json")) { let d; try { d = JSON.parse(fs.readFileSync(p, "utf8")); } catch (x) { continue; }
    (function w(o){ if (Array.isArray(o)) o.forEach(w); else if (o && typeof o === "object") { if (o.type === "question") { o.__subj = root.split("/").slice(-2)[0]; qs.push(o); } Object.values(o).forEach(w); } })(d); } } })(root);
roots.forEach(walkAll);
console.log("문항", qs.length);

const per = {}; let err = 0, leakCount = 0, correctDiag = 0; const leakEx = [];
for (const q of qs) {
  const P = per[q.__subj] || (per[q.__subj] = {n:0, hint:0, multi:0, derived:0, authoredOnly:0, numeric:0, fill:0});
  P.n++;
  try {
    const h = T.hints(q); if (h.length) P.hint++; if (h.length >= 2) P.multi++;
    const d = h.slice(q.hint ? 1 : 0); if (d.length) P.derived++;
    if (q.qtype === "numeric" || q.qtype === "fill_blank") {
      const answers = q.qtype === "numeric" ? [q.answer] : q.blanks.flatMap(b => b.answers);
      for (const line of d) for (const a of answers) { const A = T._loose(a), L = T._loose(line.replace(/^(풀이의 첫 단계|이어서): /, ""));
        if (!A) continue;
        const isNum = /^[-+]?[\d./]+$/.test(A);
        let hit = false;
        if (isNum) { if (A.replace(/[^0-9]/g, "").length >= 2) hit = new RegExp("(^|[^0-9.])" + A.replace(/[.*+?^${}()|[\]\\\/]/g, "\\$&") + "($|[^0-9.])").test(L.replace(/[가-힣]+$/, "")); }
        else if (A.length >= 2) hit = L.includes(A);
        if (hit) { leakCount++; if (leakEx.length < 5) leakEx.push([q.__subj, q.id, a, line]); } }
    }
    if (q.qtype === "numeric") { P.numeric++; if (T.diagnoseNumeric(q, q.answer)) correctDiag++; }
    if (q.qtype === "fill_blank") { P.fill++; T.diagnoseBlanks(q, q.blanks.map(() => "x")); }
  } catch (e) { err++; if (err < 5) console.log("ERR", q.id, e.message); }
}
for (const [k, P] of Object.entries(per)) console.log(k.padEnd(6), `문항 ${P.n} · 힌트 있음 ${P.hint} (${Math.round(P.hint/P.n*100)}%) · 2단계+ ${P.multi} · 풀이에서 뽑은 힌트 ${P.derived}`);
console.log({totalQuestions: qs.length, leakCount, errors: err, correctAnswerDiagnosed: correctDiag}); if (leakEx.length) console.log("노출 예:", JSON.stringify(leakEx, null, 1));
if (leakCount || err || correctDiag) fail++;
console.log(fail ? "FAILED " + fail : "ALL PASSED");
process.exit(fail ? 1 : 0);
