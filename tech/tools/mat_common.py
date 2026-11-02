"""재료 트랙 가이드 공용 자료와 링크. 레벨1 재료 과목이 없으므로 레벨2 입문을 넓게(12단원) 잡는다."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gk import *

T = "materials"
MIT3091 = OCW("3.091", "Introduction to Solid-State Chemistry (2018년 가을)", "3-091-introduction-to-solid-state-chemistry-fall-2018")
CALLISTER = book("Wiley", "Callister · Rethwisch, Materials Science and Engineering: An Introduction (번역본 『재료과학과 공학』, 장 제목으로 표기)")
ASKELAND = book("Cengage", "Askeland · Wright, The Science and Engineering of Materials (장 제목으로 표기)")
DOITPOMS = {"kind": "web", "provider": "DoITPoMS (케임브리지 대학교, 무료)", "title": "재료과학 교육용 자료와 시뮬레이션", "url": "https://www.doitpoms.ac.uk/", "lang": "영어"}
MPROJ = {"kind": "web", "provider": "Materials Project (무료 데이터베이스)", "title": "계산 재료 물성 데이터베이스", "url": "https://materialsproject.org/", "lang": "영어"}
ASHBY = book("Butterworth-Heinemann", "Ashby, Materials Selection in Mechanical Design (장 제목으로 표기)")
DIETER = book("McGraw-Hill", "Dieter, Mechanical Metallurgy (장 제목으로 표기)")
KASAP = book("McGraw-Hill", "Kasap, Principles of Electronic Materials and Devices (장 제목으로 표기)")
POLY = book("Wiley", "Fried, Polymer Science and Technology (장 제목으로 표기)")
BARSOUM = book("CRC Press", "Barsoum, Fundamentals of Ceramics (장 제목으로 표기)")
CULLITY = book("Pearson", "Cullity · Stock, Elements of X-Ray Diffraction (장 제목으로 표기)")
LENG = book("Wiley", "Leng, Materials Characterization (장 제목으로 표기)")

G2 = lambda u, t: {"title": f"레벨2 재료공학 입문 · {u}단원 {t}", "href": f"guide.html?lv=2&t=materials&s=materials-intro&u={u}"}
G2R = lambda u, t: {"kind": "web", "provider": "tech-arena 레벨2", "title": f"재료공학 입문 {u}단원 {t}", "url": f"guide.html?lv=2&t=materials&s=materials-intro&u={u}"}
GX = lambda lv, tr, s, u, t: {"kind": "web", "provider": f"tech-arena 레벨{lv}", "title": t, "url": f"guide.html?lv={lv}&t={tr}&s={s}&u={u}"}
GXL = lambda lv, tr, s, u, t: {"title": f"레벨{lv} {t}", "href": f"guide.html?lv={lv}&t={tr}&s={s}&u={u}"}

L2NOTE = "레벨 2 (응용, 전문대졸·산업기사 수준). 목차 검증 기준: 금속재료산업기사 등 재료 분야 산업기사 필기 과목 구성(최신 공고 확인)과 {}. 레벨1에 재료 과목이 없어 입문 범위를 넓게 잡았습니다."
L3NOTE = "레벨 3 (심화, 대졸·기사 수준). 목차 검증 기준: 금속재료기사 등 재료 분야 기사 필기 과목 구성(최신 공고 확인)과 {}. 레벨3은 단원당 자가점검 3문항, 학습 조언 1문단의 가벼운 형식입니다."
