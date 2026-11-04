#!/usr/bin/env python3
"""외국어 코스 화면(browse.html)이 쓰는 유닛 목록을 만듭니다.

data_v2(쓰기·말하기)와 data(객관식) 폴더의 유닛 제목을 모아
content/catalog.json 하나로 저장합니다. 유닛을 추가하거나 제목을 바꾼 뒤
lingua 폴더에서 실행하세요:

    python3 tools/build_catalog.py
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ["en", "ja", "zh", "fr", "de", "es"]
LEVELS = ["a1", "a2", "b1", "b2", "c1", "c2"]


def read(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def new_units(lang, level):
    out = []
    for n in range(1, 51):
        d = read(os.path.join(ROOT, "data_v2", lang, level, f"{lang}_{level}_u{n:02d}.json"))
        if d and d.get("meta"):
            m = d["meta"]
            out.append([n, m.get("title_ko") or m.get("title", ""), m.get("title", "")])
    return out


def classic_units(lang, level):
    base = os.path.join(ROOT, "data", lang, level)
    out = []
    for n in range(1, 21):
        # play.html과 같은 순서로 찾음
        for name in (f"{lang}_{level}_u{n:02d}.json", f"{level}_u{n:02d}.json", f"u{n:02d}.json"):
            d = read(os.path.join(base, name))
            if d and d.get("meta"):
                m = d["meta"]
                out.append([n, m.get("title_ko") or m.get("title", ""), m.get("title", "")])
                break
    return out


def build():
    cat = {}
    for lang in LANGS:
        cat[lang] = {}
        for level in LEVELS:
            cat[lang][level] = {"new": new_units(lang, level), "classic": classic_units(lang, level)}
    path = os.path.join(ROOT, "content", "catalog.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cat, f, ensure_ascii=False, separators=(",", ":"))
    for lang in LANGS:
        nn = sum(len(cat[lang][v]["new"]) for v in LEVELS)
        nc = sum(len(cat[lang][v]["classic"]) for v in LEVELS)
        print(f"{lang}: 쓰기·말하기 {nn}유닛, 객관식 {nc}유닛")


if __name__ == "__main__":
    build()
