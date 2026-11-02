"""코스4: 극한·미분·적분 문항을 sympy로 독립 검산"""
import json, re, sys, glob
import sympy as sp
x, n, t = sp.symbols("x n t")
SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻", "0123456789-"); SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉₋", "0123456789-")
def S(s):
    s = re.sub(r"(\d) × (\d)", r"\1*\2", s); s = s.replace("−", "-").replace("×", "*").replace("π", "pi").replace("ⁿ⁺¹", "**(n+1)").replace("ⁿ", "**n").replace("eˣ", "exp(x)").replace("ᵉ", "E")
    s = re.sub(r"e\^\(", "exp(", s)
    s = re.sub(r"ln\s+x([⁰¹²³⁴⁵⁶⁷⁸⁹]+)", r"log(x\1)", s)
    s = re.sub(r"ln\s*\(", "log(", s); s = re.sub(r"ln\s+([a-z0-9²³⁴]+)", r"log(\1)", s)
    s = re.sub(r"(sin|cos|tan)\s+(\d*[a-z])", r"\1(\2)", s)
    s = re.sub(r"√\(", "sqrt(", s); s = re.sub(r"√(\d+|[a-z])", r"sqrt(\1)", s)
    s = re.sub(r"([⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)", lambda mm: "**(" + mm.group(1).translate(SUP) + ")", s)
    s = re.sub(r"(\d)\s*([a-z(])", r"\1*\2", s); s = re.sub(r"\)\s*\(", ")*(", s)
    s = re.sub(r"\b([xnt])\s*\(", r"\1*(", s); s = re.sub(r"\b([xnt])\s*(exp|sin|cos|log|sqrt)", r"\1*\2", s)
    s = re.sub(r"\)\s*([a-z])", r")*\1", s)
    return sp.sympify(s, locals={"x": x, "n": n, "t": t, "E": sp.E, "pi": sp.pi})
def A(q): return sp.nsimplify(q["answer"].replace("−", "-"))
ok = bad = 0
def chk(c, f, q, info=""):
    global ok, bad
    if c: ok += 1
    else: bad += 1; print("BAD", f.split("level1/")[1], q["id"], q["prompt"][:90], info)
for f in sorted(glob.glob(sys.argv[1])):
    for q in json.load(open(f))["questions"]:
        p = q["prompt"]
        try:
            if (m := re.match(r"lim\(x→(−?\d+|∞|0)\) (.+?)의 값은", p)):
                a = sp.oo if m[1] == "∞" else int(m[1].replace("−", "-")); v = sp.limit(S(m[2]), x, a); chk(sp.simplify(v - A(q)) == 0, f, q, v); continue
            if (m := re.match(r"lim\(n→∞\) (.+?)의 값은", p)):
                v = sp.limit(S(m[1]), n, sp.oo); chk(sp.simplify(v - A(q)) == 0, f, q, v); continue
            if (m := re.match(r"f\(x\) = (.+?)일 때 f(′|″)\((.+?)\)의 값은", p)) and "(x <" not in p and "∫" not in m[1]:
                e = S(m[1].replace(" (x > 0)", "")); d = sp.diff(e, x, 1 if m[2] == "′" else 2); v = d.subs(x, S(m[3]))
                chk(sp.simplify(v - A(q)) == 0, f, q, v); continue
            if (m := re.match(r"∫([₀₁₂₃₄₅₆₇₈₉₋]+)\^?\(?([^ )]*?)\)? \((.+?)\) dx의 값은", p)) or (m := re.match(r"∫([₀₁₂₃₄₅₆₇₈₉₋]+)([⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+) \((.+?)\) dx의 값은", p)):
                lo = int(m[1].translate(SUB)); up = S(m[2].translate(SUP))
                v = sp.integrate(S(m[3]), (x, lo, up)); chk(sp.simplify(v - A(q)) == 0, f, q, v); continue
        except Exception as e:
            print("ERR", f.split("level1/")[1], q["id"], p[:60], e)
print("코스4 검산", ok, "불일치", bad)
