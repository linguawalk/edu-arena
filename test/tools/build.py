"""test-arena 콘텐츠 빌드.

tools/lessons/{subj}_{stage}_{track}_ch{NN}.py 를 읽어 content/ 아래 JSON을 만든다.
레슨 파일이 있는 챕터만 available이 된다. 기준을 어기면 빌드를 멈춘다.

사용: python3 tools/build.py
"""
import importlib.util, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import curriculum as C

LESSON_DIR = os.path.join(ROOT, "tools", "lessons")
OUT = os.path.join(ROOT, "content")

# 제작 기준 (content/README.md와 같게 유지)
RULE = {"screens": (16, 22), "questions": (11, 13), "proofs_min": 2, "expl_chars": 60, "expl_steps": 3,
        "explain_chars": 160, "review_questions": 10, "review_proofs_min": 1}
# S3 학습 가이드: 챕터마다 가이드 1개(복습 없음). 핵심 도구 설명·예제·확인 문항·증명 문제·독학 안내.
GUIDE_RULE = {"screens": (14, 24), "proofs_min": 5, "graded_min": 2, "examples_min": 2}
GRADED = {"numeric", "fill_blank", "ordering", "diagram"}


def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def check_question(q, where, errors):
    if not q.get("hint"):
        errors.append(f"{where}: 힌트 없음")
    t = q["qtype"]
    if t in GRADED:
        ex = q.get("explanation") or ""
        if len(ex.replace("\n", "")) < RULE["expl_chars"] or len([l for l in ex.split("\n") if l.strip()]) < RULE["expl_steps"]:
            errors.append(f"{where}: 풀이가 {RULE['expl_chars']}자·{RULE['expl_steps']}단계 미만")
    if t == "numeric":
        ans, fmt = str(q["answer"]), q.get("answer_format")
        if fmt == "integer" and ("." in ans or "/" in ans):
            errors.append(f"{where}: 정수 형식인데 답이 {ans}")
        if fmt == "decimal" and "/" in ans:
            errors.append(f"{where}: 소수 형식인데 답이 분수 {ans}")
    if t == "fill_blank":
        n = len(re.findall(r"\{\{\d+\}\}", q["prompt"]))
        if n != len(q["blanks"]):
            errors.append(f"{where}: 빈칸 수 불일치")
    if t == "ordering":
        if [it["id"] for it in q["items"]] == q["answer_order"]:
            errors.append(f"{where}: 배열 문항이 처음부터 정답 순서")
    if t == "proof":
        if len(q["model_answer"]) < 3 or not q["criteria"]:
            errors.append(f"{where}: 모범 증명 3단계 미만이거나 채점 기준 없음")


def check_lesson(screens, where, errors):
    qs = [s for s in screens if s["type"] == "question"]
    lo, hi = RULE["screens"]
    if not lo <= len(screens) <= hi:
        errors.append(f"{where}: 화면 {len(screens)}개 (기준 {lo}~{hi})")
    lo, hi = RULE["questions"]
    if not lo <= len(qs) <= hi:
        errors.append(f"{where}: 문항 {len(qs)}개 (기준 {lo}~{hi})")
    if sum(q["qtype"] == "proof" for q in qs) < RULE["proofs_min"]:
        errors.append(f"{where}: 증명 문항 {RULE['proofs_min']}개 미만")
    for k, s in enumerate(screens, 1):
        if s["type"] == "explain" and len("".join(s["body"])) < RULE["explain_chars"]:
            errors.append(f"{where} 화면 {k}: 설명 {RULE['explain_chars']}자 미만")
        if s["type"] == "example" and len(s["steps"]) < 3:
            errors.append(f"{where} 화면 {k}: 예제 풀이 3단계 미만")
        if s["type"] == "question":
            check_question(s, f"{where} 화면 {k}", errors)


def check_guide(screens, where, errors):
    qs = [s for s in screens if s["type"] == "question"]
    lo, hi = GUIDE_RULE["screens"]
    if not lo <= len(screens) <= hi:
        errors.append(f"{where}: 화면 {len(screens)}개 (가이드 기준 {lo}~{hi})")
    if sum(q["qtype"] == "proof" for q in qs) < GUIDE_RULE["proofs_min"]:
        errors.append(f"{where}: 증명 문제 {GUIDE_RULE['proofs_min']}개 미만")
    if sum(q["qtype"] in GRADED for q in qs) < GUIDE_RULE["graded_min"]:
        errors.append(f"{where}: 확인 문항 {GUIDE_RULE['graded_min']}개 미만")
    if sum(s["type"] == "example" for s in screens) < GUIDE_RULE["examples_min"]:
        errors.append(f"{where}: 예제 {GUIDE_RULE['examples_min']}개 미만")
    for k, s in enumerate(screens, 1):
        if s["type"] == "explain" and len("".join(s["body"])) < RULE["explain_chars"]:
            errors.append(f"{where} 화면 {k}: 설명 {RULE['explain_chars']}자 미만")
        if s["type"] == "example" and len(s["steps"]) < 3:
            errors.append(f"{where} 화면 {k}: 예제 풀이 3단계 미만")
        if s["type"] == "question":
            check_question(s, f"{where} 화면 {k}", errors)


def number(screens, prefix=""):
    cnt = {"explain": 0, "example": 0, "question": 0}
    tag = {"explain": "s", "example": "e", "question": "q"}
    out = []
    for s in screens:
        cnt[s["type"]] += 1
        out.append({"type": s["type"], "id": f"{prefix}{tag[s['type']]}{cnt[s['type']]}", **{k: v for k, v in s.items() if k != "type"}})
    return out


def build_subject(subj, errors):
    cur = C.CURRICULUM[subj]
    TR, CH, ORDER = cur["tracks"], cur["chapters"], cur["order"]
    stages_out = []
    for st in C.STAGES:
        sid = st["id"]
        tracks_out = []
        for tid in ORDER:
            titles = CH[sid].get(tid, [])
            chapters, tot = [], {"lessons": 0, "lesson_questions": 0, "review_questions": 0}
            for no, title in enumerate(titles, 1):
                src = os.path.join(LESSON_DIR, f"{subj}_{sid}_{tid}_ch{no:02d}.py")
                ch_id = f"{subj}-{sid}-{tid}-ch{no:02d}"
                entry = {"no": no, "id": ch_id, "title": title, "dir": f"ch{no:02d}", "available": os.path.exists(src)}
                if entry["available"]:
                    m = load(src)
                    chdir = os.path.join(OUT, subj, sid, tid, f"ch{no:02d}")
                    meta = {"subject": subj, "stage": sid, "track": tid, "work": cur["work"]}
                    lessons_meta = []
                    guide = getattr(m, "GUIDE", None)
                    for k, L in enumerate([guide] if guide else m.LESSONS, 1):
                        lid = f"{ch_id}-l{k:02d}"
                        where = f"{lid}"
                        (check_guide if guide else check_lesson)(L["screens"], where, errors)
                        screens = number(L["screens"])
                        nq = sum(s["type"] == "question" for s in screens)
                        write(os.path.join(chdir, f"l{k:02d}.json"), {
                            "schema_version": "1.0", "site": "test-arena", **meta,
                            "track_title": TR[tid]["title"],
                            "chapter": {"id": ch_id, "no": no, "title": title},
                            "lesson": {"id": lid, "no": k, "title": L["title"], "minutes": L["minutes"], **({"kind": "guide"} if guide else {})},
                            "tags": {"domain": m.DOMAIN, "competition": TR[tid].get("competition", cur["competition"]), "stage": sid},
                            "screens": screens})
                        lessons_meta.append({"no": k, "id": lid, "title": L["title"], "file": f"l{k:02d}.json",
                                             "questions": nq, "screens": len(screens), **({"kind": "guide"} if guide else {})})
                    if guide:
                        write(os.path.join(chdir, "chapter.json"), {
                            "schema_version": "1.0", **meta, "chapter": {"id": ch_id, "no": no, "title": title},
                            "kind": "guide", "lessons": lessons_meta})
                        entry.update({"kind": "guide", "lessons": 1, "lesson_questions": lessons_meta[0]["questions"], "review_questions": 0})
                        tot["lessons"] += 1; tot["lesson_questions"] += entry["lesson_questions"]
                        chapters.append(entry)
                        continue
                    R = m.REVIEW
                    rqs = []
                    for k, (src_l, q) in enumerate(R["questions"], 1):
                        q = dict(q); q["stage"] = "review"
                        check_question(q, f"{ch_id} 복습 {k}", errors)
                        rqs.append({"type": "question", "id": f"r{k}", **{a: b for a, b in q.items() if a != "type"},
                                    "source_lesson": f"{ch_id}-l{src_l:02d}"})
                    if len(rqs) != RULE["review_questions"]:
                        errors.append(f"{ch_id} 복습: 문항 {len(rqs)}개 (기준 {RULE['review_questions']})")
                    if sum(q["qtype"] == "proof" for q in rqs) < RULE["review_proofs_min"]:
                        errors.append(f"{ch_id} 복습: 증명 문항 없음")
                    write(os.path.join(chdir, "review.json"), {
                        "schema_version": "1.0", "site": "test-arena", **meta,
                        "chapter": {"id": ch_id, "no": no, "title": title},
                        "review": {"id": f"{ch_id}-review", "title": R["title"], "minutes": R["minutes"]},
                        "questions": rqs})
                    write(os.path.join(chdir, "chapter.json"), {
                        "schema_version": "1.0", **meta, "chapter": {"id": ch_id, "no": no, "title": title},
                        "lessons": lessons_meta, "review": {"id": f"{ch_id}-review", "file": "review.json", "questions": len(rqs)}})
                    entry.update({"lessons": len(lessons_meta), "lesson_questions": sum(l["questions"] for l in lessons_meta),
                                  "review_questions": len(rqs)})
                    tot["lessons"] += entry["lessons"]; tot["lesson_questions"] += entry["lesson_questions"]
                    tot["review_questions"] += entry["review_questions"]
                chapters.append(entry)
            if not titles:
                continue
            avail = any(c["available"] for c in chapters)
            track = {"id": tid, "title": TR[tid]["title"], "description": TR[tid]["description"],
                     "chapters": len(chapters), "available": avail}
            if TR[tid].get("group"):
                track["group"] = TR[tid]["group"]
            tracks_out.append(track)
            write(os.path.join(OUT, subj, sid, tid, "track.json"), {
                "schema_version": "1.0", "subject": subj, "stage": sid,
                "track": {"id": tid, "title": track["title"], "description": track["description"], "group": TR[tid].get("group")},
                "totals": {**tot, "questions": tot["lesson_questions"] + tot["review_questions"]},
                "chapters": chapters})
        level = cur.get("levels", {}).get(sid, st["level"])
        stages_out.append({**st, "level": level, "available": any(t["available"] for t in tracks_out), "tracks": tracks_out})
    sj = dict(next(s for s in C.SUBJECTS if s["id"] == subj))
    sj["available"] = any(s["available"] for s in stages_out)
    write(os.path.join(OUT, subj, "subject.json"), {"schema_version": "1.0", "subject": sj, "stages": stages_out})
    return sj["available"]


def build():
    errors = []
    open_subj = {subj: build_subject(subj, errors) for subj in C.CURRICULUM}
    subjects = [{**s, "available": open_subj.get(s["id"], False)} for s in C.SUBJECTS]
    write(os.path.join(OUT, "catalog.json"), {"schema_version": "1.0", "site": "test-arena", "subjects": subjects})

    if errors:
        print("빌드 기준 위반:")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    print("빌드 완료")


if __name__ == "__main__":
    build()
