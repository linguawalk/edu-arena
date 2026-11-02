"""융합 과정 가이드 공용 자료와 링크.

융합 과정은 12대 국가전략기술을 뼈대로 한 7개 군 22과정(레벨3)과 레벨1에서 바로 이어지는 3개 브리지(레벨2)로 이루어진다.
기술·산업 동향과 규제가 빠르게 바뀌므로 동향·규제 단원에는 review(점검 정보, 대개 6개월 주기)를 붙인다.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gk import *

T = "convergence"
GX = lambda lv, tr, s, u, t: {"kind": "web", "provider": f"tech-arena 레벨{lv}", "title": t, "url": f"guide.html?lv={lv}&t={tr}&s={s}&u={u}"}
GXL = lambda lv, tr, s, u, t: {"title": f"레벨{lv} {t}", "href": f"guide.html?lv={lv}&t={tr}&s={s}&u={u}"}
GXS = lambda lv, tr, s, t: {"title": f"레벨{lv} {t}", "href": f"guide.html?lv={lv}&t={tr}&s={s}"}
GC = lambda lv, s, u, t: {"kind": "web", "provider": f"tech-arena 레벨{lv} 융합", "title": t, "url": f"guide.html?lv={lv}&t=convergence&s={s}&u={u}"}

L2NOTE = "레벨 2 브리지 (응용, 전문대졸 수준). 레벨1을 마친 학습자가 해당 레벨3 융합 과정으로 바로 넘어갈 수 있게 다리를 놓는 입문 과목입니다. 목차 검증 기준: {}. 산업 동향 단원은 점검 정보로 관리합니다."
L3NOTE = "레벨 3 융합 과정 (심화, 대졸·기사 수준). 목차 검증 기준: {}. 기술·산업·규제 동향이 빠르게 바뀌는 분야라 동향 단원에 점검 정보를 붙였습니다. 단원당 자가점검 3문항, 학습 조언 1문단의 가벼운 형식입니다."

SEMI_INDUSTRY = "반도체 산업 동향(공정 노드, 메모리·파운드리 시장, 국가전략기술 지정)"
AI_POLICY = "인공지능 발전과 신뢰 기반 조성 등에 관한 기본법(AI 기본법)과 하위 법령, EU AI Act 등 해외 규제"

NEAMEN = book("McGraw-Hill", "Neamen, Semiconductor Physics and Devices (장 제목으로 표기)")
HENNESSY = book("Morgan Kaufmann", "Hennessy · Patterson, Computer Architecture: A Quantitative Approach (도메인 특화 구조 장)")
SZE_ML = book("Morgan & Claypool", "Sze 외, Efficient Processing of Deep Neural Networks (장 제목으로 표기)")
LINDEN = book("McGraw-Hill", "Reddy, Linden's Handbook of Batteries (장 제목으로 표기)")
EHSANI = book("CRC Press", "Ehsani 외, Modern Electric, Hybrid Electric, and Fuel Cell Vehicles (장 제목으로 표기)")
THRUN = book("MIT Press", "Thrun · Burgard · Fox, Probabilistic Robotics (장 제목으로 표기)")
CRAIG = book("Pearson", "Craig, Introduction to Robotics: Mechanics and Control (장 제목으로 표기)")
LYNCH_R = {"kind": "book", "provider": "Lynch · Park (무료 공개 교재와 강의)", "title": "Modern Robotics: Mechanics, Planning, and Control", "url": "https://hades.mech.northwestern.edu/index.php/Modern_Robotics", "lang": "영어"}
D2L = {"kind": "book", "provider": "Dive into Deep Learning (무료 공개 교재)", "title": "Dive into Deep Learning", "url": "https://d2l.ai/", "lang": "영어"}
GOODFELLOW = {"kind": "book", "provider": "Goodfellow · Bengio · Courville (무료 공개)", "title": "Deep Learning", "url": "https://www.deeplearningbook.org/", "lang": "영어"}
GPP = {"kind": "web", "provider": "3GPP", "title": "3GPP 규격과 릴리스 정보", "url": "https://www.3gpp.org/", "lang": "영어"}
SAE = {"kind": "web", "provider": "SAE International", "title": "J3016 자율주행 단계 정의", "url": "https://www.sae.org/standards/content/j3016_202104/", "lang": "영어"}


def U3(no, title, hours, pre, objs, topics, advice, res, qs, rv=None):
    """레벨3 융합 단원(조언 1문단) 축약 생성기"""
    if rv:
        return unit(no, title, hours, pre, objs, topics, [advice], res, qs, review=rv)
    return unit(no, title, hours, pre, objs, topics, [advice], res, qs)


def SUBJ(sid, title, tagline, overview, basis, prereq_text, links, pq, nxt):
    return {"level": 3, "track": T, "id": sid, "title": title, "tagline": tagline, "overview": overview,
            "level_note": L3NOTE.format(basis), "prereq": {"text": prereq_text, "links": links, "questions": pq}, "next": nxt}


def NX(title, note):
    return {"title": title, "note": note}


def build_all(items):
    for subj, units, ver in items:
        ver()
        write_subject(subj, units)
