"""규정값 관리: content/rules.json의 값을 빌더에서 불러오고, 사용 기록을 레슨 review 정보로 남긴다.

사용: from rules import rv, used_rules
  rv("min_wage_hourly")          -> 10320 (현재 적용 값)
  rv("min_wage_hourly", "label") -> "최저임금 시간급"
write_chapter()는 레슨 빌드 중 rv()가 불린 키를 lesson.review에 기록한다.
"""
import json, os

PATH = os.path.join(os.path.dirname(__file__), "..", "content", "rules.json")
_R = json.load(open(PATH, encoding="utf-8"))["rules"]
_USED = set()


def rv(key, field="value"):
    _USED.add(key)
    return _R[key][field]


def won(v):
    return f"{v:,}원"


def used_rules(reset=True):
    keys = sorted(_USED)
    if reset: _USED.clear()
    return keys


def review_info(keys):
    if not keys: return None
    return {"rules": keys, "review_by": min(_R[k]["review_by"] for k in keys)}
