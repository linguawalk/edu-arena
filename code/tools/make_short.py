#!/usr/bin/env python3
"""객관식 content/ 문항 중 값이 짧은 predict_output·fill_blank를 단답형으로 변환한다.
  python3 code/tools/make_short.py python scripting javascript scripting c system_low_level
출력: code/short/<lang>/levelN_unitNN.json (원본은 건드리지 않음)
- 정답 = 원래 정답 보기, 나머지 보기는 wrong_answers(자주 틀리는 답)로 보관
- 변환하지 못한 문항(문장형·여러 줄·보기가 있어야 풀리는 문항)은 건너뛰고 사유를 센다
"""
import json, glob, os, re, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BAD_PROMPT = re.compile(r"다음 중|아래 중|보기|옳은 것|틀린 것|알맞은 것|가장 적절|어느 것|모두 고르")
# 정답이 하나로 정해지지 않는 빈칸(변수 이름, ++/-- 위치, 임의의 값 등)은 단답형으로 쓰지 않는다 (2026-11 수작업 검토)
NAMES = {"c": "C", "cpp": "C++", "rust": "Rust", "visual_basic": "Visual Basic", "csharp": "C#", "java": "Java",
         "python": "Python", "javascript": "JavaScript", "php": "PHP", "basic_early": "BASIC", "pascal": "Pascal",
         "fortran": "FORTRAN", "cobol": "COBOL"}
DENY = {"c_l1_u02_q004", "c_l2_u01_q003", "c_l3_u04_q004", "c_l4_u02_q003", "c_l4_u03_q003", "c_l4_u03_q005",
        "c_l5_u03_q004", "cpp_l2_u03_q003", "cpp_l3_u03_q004", "cpp_l4_u02_q002", "csharp_l1_u01_q003",
        "csharp_l4_u02_q004", "csharp_l6_u02_q005", "java_l1_u01_q003", "java_l6_u02_q005", "java_l3_u03_q003",
        "fortran_l1_u02_q003", "rust_l2_u03_q005", "visual_basic_l1_u01_q003", "visual_basic_l4_u03_q004",
        "visual_basic_l6_u02_q005", "visual_basic_l1_u03_q003", "javascript_l2_u04_q004", "javascript_l6_u03_q002", "python_l1_u01_q003", "python_l6_u03_q004"}
ERRWORD = re.compile(r"오류|에러|error|컴파일|예외|undefined behavior|정의되지|미정의|실행되지", re.I)

def skip_reason(q, lang):
    if not str(q.get("id", "")).startswith(lang + "_l"): return "wrong_language_id"   # 다른 언어 문항이 섞인 경우(원본 오류)
    if q["id"] in DENY: return "ambiguous"
    if q["type"] not in ("predict_output", "fill_blank"): return "type"
    opts = q.get("options") or []
    if len(opts) < 2 or not isinstance(q.get("answer"), int): return "shape"
    a = str(opts[q["answer"]])
    p = q.get("prompt_ko") or ""
    if BAD_PROMPT.search(p): return "prompt_needs_options"
    if "\n" in a or "\\n" in a or "새 줄" in a or "줄바꿈" in a: return "multiline"
    if ERRWORD.search(a): return "error_word"
    if " - " in a: return "sentence"
    if len(a) > 24: return "long"
    if re.search(r"[가-힣]{3,}", a): return "sentence"
    if "," in a and re.search(r"\s", a) and len(a.split()) > 3: return "sentence"
    if re.fullmatch(r"\s*", a): return "empty"
    return None

def variants(a):
    return [str(a).strip()]

CI = {"basic_early", "cobol", "fortran", "pascal", "visual_basic"}   # 대소문자를 구분하지 않는 언어: 빈칸(키워드) 답은 대소문자 무시

def convert(q, lang=""):
    opts = q["options"]; a = opts[q["answer"]]
    wrong = [str(o) for i, o in enumerate(opts) if i != q["answer"]]
    out = {
        "id": q["id"], "type": q["type"], "code": q.get("code"),
        "prompt_ko": q.get("prompt_ko"), "prompt_en": q.get("prompt_en"),
        "expected_answers": variants(a),
        "match": {"case": not (q["type"] == "fill_blank" and lang in CI), "space": "remove" if q["type"] == "fill_blank" else "collapse"},
        "wrong_answers": wrong,
        "explanation_ko": q.get("explanation_ko"), "explanation_en": q.get("explanation_en"),
        "concept_tags": q.get("concept_tags", []), "difficulty": q.get("difficulty", "practice"),
    }
    return {k: v for k, v in out.items() if v is not None}

def main(args):
    pairs = list(zip(args[0::2], args[1::2]))
    stat = collections.Counter(); per = {}
    for lang, cat in pairs:
        for f in sorted(glob.glob(os.path.join(ROOT, "content", cat, lang, "level*_unit*.json"))):
            d = json.load(open(f, encoding="utf-8")); qs = []
            for q in d["questions"]:
                r = skip_reason(q, lang)
                if r: stat[(lang, r)] += 1; continue
                qs.append(convert(q, lang)); stat[(lang, "ok")] += 1
            if not qs: continue
            out = {k: d[k] for k in ("language", "category", "level", "unit", "unit_title") if k in d}
            out["format"] = "short_answer"; out["questions"] = qs
            dst = os.path.join(ROOT, "short", lang, os.path.basename(f)); os.makedirs(os.path.dirname(dst), exist_ok=True)
            json.dump(out, open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            per.setdefault(lang, []).append((d["level"], d["unit"], len(qs), d.get("unit_title", "")))
    man = {}
    for lang, v in per.items():
        man[lang] = {"name": NAMES.get(lang, lang), "units": [{"level": l, "unit": u, "n": n, "title": t} for l, u, n, t in sorted(v)]}
    json.dump(man, open(os.path.join(ROOT, "short", "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for k in sorted(stat): print(k, stat[k])
    for lang, v in per.items(): print(lang, "units", len(v), "questions", sum(x[2] for x in v))

if __name__ == "__main__": main(sys.argv[1:])
