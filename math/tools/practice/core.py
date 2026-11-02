"""레벨1 '더 연습하기' 문제 은행 생성 공통 도구."""
import json, random, os
from fractions import Fraction as F
from math import gcd, isqrt

SITE = "/home/claude/site"
SUPD = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")
def sup(n): return str(n).translate(SUPD)
def m(x):
    """화면 표기: 음수 부호를 −로"""
    return str(x).replace("-", "−")
def par(x):
    """음수면 괄호"""
    return f"({m(x)})" if x < 0 else str(x)
def fs(fr):
    fr = F(fr)
    return str(fr.numerator) if fr.denominator == 1 else f"{fr.numerator}/{fr.denominator}"
def fm(fr): return m(fs(fr))
def fpar(fr): return f"({fm(fr)})" if F(fr) < 0 else fm(fr)
def alts(x):
    s = str(x)
    out = [s]
    if s.startswith("-"): out.append("−" + s[1:])
    return out

def num(prompt, answer, expl, hint=None, fmt=None):
    if isinstance(answer, F):
        a = fs(answer); fmt = fmt or ("integer" if answer.denominator == 1 else "fraction")
    else:
        a = str(answer); fmt = fmt or "integer"
    return {"type": "question", "qtype": "numeric", "prompt": prompt, "answer": a,
            "answer_format": fmt, "tolerance": 0, "hint": hint, "explanation": expl}

def fill(prompt, blanks, expl, hint=None, unordered=None):
    n = prompt.count("{{")
    assert n == len(blanks), (prompt, blanks)
    for i in range(1, n + 1): assert "{{%d}}" % i in prompt, prompt
    q = {"type": "question", "qtype": "fill_blank", "prompt": prompt,
         "blanks": [{"id": i + 1, "answers": b if isinstance(b, list) else alts(b)} for i, b in enumerate(blanks)],
         "hint": hint, "explanation": expl}
    if unordered: q["unordered_groups"] = unordered
    return q

def factor(n):
    f, p = {}, 2
    while p * p <= n:
        while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
        p += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
def fstr(f): return " × ".join(f"{p}{sup(e) if e > 1 else ''}" for p, e in sorted(f.items()))
def divisors(n): return [d for d in range(1, n + 1) if n % d == 0]
def is_prime(n): return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))

def build(templates, per=6, seed=1, tries=1200, minlen=20):
    """templates: [(제목, 함수(rng)->question)] → 같은 문항 없이 per개씩"""
    pool = []
    for g, (title, fn) in enumerate(templates, 1):
        rng = random.Random(seed * 1000 + g); seen = set(); k = 0
        for _ in range(tries):
            q = fn(rng)
            if q is None or q["prompt"] in seen: continue
            if len(q["explanation"]) < minlen and q.get("hint"):
                q["explanation"] += "\n핵심: " + q["hint"]
            seen.add(q["prompt"]); k += 1
            assert q["explanation"] and len(q["explanation"]) >= 20, q
            for key in ("prompt", "explanation", "hint"):
                if q.get(key): q[key] = fixjosa(q[key])
            q["id"] = f"g{g}-{k}"; q["group"] = g; q["stage"] = "practice"
            pool.append(q)
            if k == per: break
        assert k >= min(per, 4), (title, k)
        if k < per: print(f"  · '{title}' {k}/{per}")
    return pool

def write(c, ch, l, templates, per=6, seed=1, minlen=None):
    if minlen is None: minlen = 20 if c == "c0" else 40 if c in ("c1", "c2") else 60
    d = f"{SITE}/content/level1/{c}/{ch}"
    lesson = json.load(open(f"{d}/{l}.json"))
    pool = build(templates, per, seed, minlen=minlen)
    out = {"schema_version": "1.0", "site": "math-arena", "level": 1,
           "course": lesson["course"], "chapter": lesson["chapter"], "lesson": lesson["lesson"],
           "practice": {"id": lesson["lesson"]["id"] + "-p", "set_size": 10,
                        "groups": [t for t, _ in templates]},
           "questions": pool}
    fn = "p" + l[1:] + ".json"
    json.dump(out, open(f"{d}/{fn}", "w"), ensure_ascii=False, indent=1)
    # chapter.json에 연결
    cj = f"{d}/chapter.json"; chap = json.load(open(cj))
    for les in chap["lessons"]:
        if les["file"] == l + ".json": les["practice"] = {"file": fn, "questions": len(pool)}
    json.dump(chap, open(cj, "w"), ensure_ascii=False, indent=2)
    return len(pool)

def _bat(n):
    n = abs(int(n))
    if n == 0: return True
    if n % 10: return n % 10 in (1, 3, 6, 7, 8)
    return True  # 십·백·천
def j(n, pair, disp=None):
    """숫자 뒤 조사: j(12,'와과') → '12와'. disp가 있으면 그 표기 뒤에 붙임"""
    a, b = pair[0], pair[1:]
    return f"{n if disp is None else disp}{b if _bat(n) else a}"
def ro(n):
    k = abs(int(n))
    rieul = (k % 10 in (1, 7, 8)) if k % 10 else False
    return f"{n}{'로' if (not _bat(n) or rieul) else '으로'}"
bat = _bat

def term(c, v="", first=False):
    """계수 c와 문자 v로 항 만들기. first면 앞 부호 '+' 생략"""
    if c == 0: return ""
    a = abs(c)
    body = (str(a) if (a != 1 or not v) else "") + v
    if first: return ("−" if c < 0 else "") + body
    return (" − " if c < 0 else " + ") + body
def poly(*pairs):
    """poly((3,'x'),(−2,'')) → '3x − 2'"""
    out = ""; 
    for c, v in pairs:
        if c == 0: continue
        out += term(c, v, first=(out == ""))
    return out or "0"
def ans(x):
    """빈칸 정답 후보: 정수/분수, 음수면 −도"""
    s = fs(x) if isinstance(x, F) else str(x)
    out = [s]
    if s.startswith("-"): out.append("−" + s[1:])
    return out

import re as _re
_JP = {"를": ("를", "을"), "을": ("를", "을"), "와": ("와", "과"), "과": ("와", "과"), "는": ("는", "은"), "은": ("는", "은"), "가": ("가", "이")}
def fixjosa(s):
    """숫자(또는 숫자로 끝나는 괄호) 바로 뒤 조사를 받침에 맞게 고침"""
    if not s: return s
    def rep(mt):
        n, close, jo = mt.group(1), mt.group(2), mt.group(3)
        b = _bat(int(n))
        if jo in ("로", "으로"):
            k = int(n); rieul = (k % 10 in (1, 7, 8)) if k % 10 else False
            jo2 = "로" if (not b or rieul) else "으로"
        else:
            jo2 = _JP[jo][1 if b else 0]
        return n + close + jo2
    return _re.sub(r"(\d+)([)\]]?)(으로|로|를|을|와|과|는|은|가)(?![가-힣])", rep, s)

def mul(a, x):
    """계수 a × 값 x 표기 (1, −1은 생략)"""
    if a == 1: return par(x) if not isinstance(x, str) else x
    if a == -1: return "−" + (par(x) if not isinstance(x, str) else x)
    return f"{m(a)}×{par(x) if not isinstance(x, str) else x}"
def sx(s, v="x"):
    """기울기 s를 붙인 항: 1 → x, −1 → −x, 분수 → (p/q)x"""
    s = F(s)
    if s == 1: return v
    if s == -1: return "−" + v
    if s.denominator == 1: return f"{m(int(s))}{v}"
    return f"{'−' if s < 0 else ''}({fs(abs(s))}){v}"
