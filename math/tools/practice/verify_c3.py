"""코스3: 로그·Σ·점화식·삼각함수값을 sympy로 독립 검산"""
import json, re, sys, glob
import sympy as sp
k, n, x = sp.symbols("k n x")
SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
def S(t):
    t = t.replace("−", "-").replace("×", "*").replace("π", "pi")
    t = re.sub(r"√(\d+|[a-z])", r"sqrt(\1)", t).replace("√", "sqrt")
    t = re.sub(r"([⁰¹²³⁴⁵⁶⁷⁸⁹]+)", lambda mt: "**" + mt.group(1).translate(SUP), t)
    t = t.replace("ᵏ", "**k").replace("ⁿ", "**n").replace("^", "**")
    t = re.sub(r"(\d)\s*([a-z(])", r"\1*\2", t); t = re.sub(r"\)\s*\(", ")*(", t); t = re.sub(r"([kn])\(", r"\1*(", t)
    return sp.sympify(t, locals={"k": k, "n": n, "x": x, "pi": sp.pi})
def ans(q):
    return sp.nsimplify(q["answer"].replace("−", "-")) if q.get("answer") else None
ok = bad = 0
def chk(c, f, q, info=""):
    global ok, bad
    if c: ok += 1
    else: bad += 1; print("BAD", f.split("level1/")[1], q["id"], q["prompt"][:80], info)
for f in sorted(glob.glob(sys.argv[1])):
    for q in json.load(open(f))["questions"]:
        p = q["prompt"]
        try:
            if (mt := re.match(r"log([₀₁₂₃₄₅₆₇₈₉]+) \(?([0-9/]+)\)?의 값은", p)):
                b = int(mt[1].translate(SUB)); X = sp.Rational(mt[2]); chk(sp.simplify(sp.log(X, b) - ans(q)) == 0, f, q); continue
            if (mt := re.match(r"Σ\(k=(\d+)~(\d+)\) (.+?)의 값은", p)):
                a_, b_ = int(mt[1]), int(mt[2]); e = S(mt[3]); v = sp.summation(e, (k, a_, b_)); chk(abs(float(v) - float(ans(q))) < 1e-9, f, q, v); continue
            if (mt := re.match(r"(sin|cos|tan) \((.+?)\) = \{\{1\}\}$", p)):
                v = getattr(sp, mt[1])(S(mt[2])); w = S(q["blanks"][0]["answers"][0]); chk(sp.simplify(v - w) == 0, f, q, v); continue
            if (mt := re.match(r"(sin|cos) \((.+?)\)의 값은", p)):
                v = getattr(sp, mt[1])(S(mt[2])); chk(sp.simplify(v - ans(q)) == 0, f, q); continue
            if (mt := re.match(r"a₁ = (.+?), aₙ₊₁ = (.+?)일 때 a([₀₁₂₃₄₅₆₇₈₉]+)의 값은", p)) and "a₂" not in p:
                a1 = S(mt[1]); rhs = mt[2].replace("aₙ", "A"); N = int(mt[3].translate(SUB))
                A = sp.Symbol("A"); e = S(rhs.replace("A", "(A)")) if "A" in rhs else None
                cur = a1
                for i in range(1, N): cur = sp.nsimplify(e.subs({A: cur, n: i}))
                chk(cur == ans(q), f, q, cur); continue
            if (mt := re.match(r"(.+?), …의 제(\d+)항은", p)) and "1, 1, 2" not in p:
                xs = [S(t) for t in mt[1].split(", ")]; N = int(mt[2])
                if len(xs) == 3 and xs[1] - xs[0] == xs[2] - xs[1]: v = xs[0] + (N - 1) * (xs[1] - xs[0])
                elif len(xs) == 3 and xs[0] != 0 and xs[1] / xs[0] == xs[2] / xs[1]: v = xs[0] * (xs[1] / xs[0]) ** (N - 1)
                else: continue
                chk(sp.nsimplify(v) == ans(q), f, q, v); continue
        except Exception as e:
            print("ERR", f.split("level1/")[1], q["id"], e)
print("코스3 검산", ok, "불일치", bad)
