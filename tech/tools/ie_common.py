"""산업 트랙 가이드 공용 자료와 링크. 레벨1 산업 과목이 없으므로 레벨2 입문을 넓게(12단원) 잡는다."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gk import *

T = "industrial"
MIT15053 = OCW("15.053", "Optimization Methods in Management Science (2013년 봄)", "15-053-optimization-methods-in-management-science-spring-2013")
NISTHB = {"kind": "web", "provider": "NIST/SEMATECH (무료)", "title": "e-Handbook of Statistical Methods", "url": "https://www.itl.nist.gov/div898/handbook/", "lang": "영어"}
HILLIER = book("McGraw-Hill", "Hillier · Lieberman, Introduction to Operations Research (번역본 『경영과학』, 장 제목으로 표기)")
MONTGOMERY = book("Wiley", "Montgomery, Introduction to Statistical Quality Control (번역본 『통계적 품질관리』, 장 제목으로 표기)")
MONT_DOE = book("Wiley", "Montgomery, Design and Analysis of Experiments (장 제목으로 표기)")
SANDERS = book("McGraw-Hill", "Sanders · McCormick, Human Factors in Engineering and Design (장 제목으로 표기)")
WICKENS = book("Routledge", "Wickens 외, Engineering Psychology and Human Performance (장 제목으로 표기)")
NIEBEL = book("McGraw-Hill", "Freivalds · Niebel, Niebel's Methods, Standards, and Work Design (장 제목으로 표기)")
HEIZER = book("Pearson", "Heizer · Render · Munson, Operations Management (번역본 『생산운영관리』, 장 제목으로 표기)")
EBELING = book("Waveland", "Ebeling, An Introduction to Reliability and Maintainability Engineering (장 제목으로 표기)")
KOSHA = {"kind": "web", "provider": "안전보건공단", "title": "근골격계 질환 예방·작업 환경 자료", "url": "https://www.kosha.or.kr/", "lang": "한국어"}
NIOSH = {"kind": "web", "provider": "미국 NIOSH", "title": "들기 작업 지침(NIOSH Lifting Equation) 등 인간공학 자료", "url": "https://www.cdc.gov/niosh/ergonomics/", "lang": "영어"}

G2 = lambda u, t: {"title": f"레벨2 산업공학 입문 · {u}단원 {t}", "href": f"guide.html?lv=2&t=industrial&s=ie-intro&u={u}"}
G2R = lambda u, t: {"kind": "web", "provider": "tech-arena 레벨2", "title": f"산업공학 입문 {u}단원 {t}", "url": f"guide.html?lv=2&t=industrial&s=ie-intro&u={u}"}
GX = lambda lv, tr, s, u, t: {"kind": "web", "provider": f"tech-arena 레벨{lv}", "title": t, "url": f"guide.html?lv={lv}&t={tr}&s={s}&u={u}"}
GXL = lambda lv, tr, s, u, t: {"title": f"레벨{lv} {t}", "href": f"guide.html?lv={lv}&t={tr}&s={s}&u={u}"}

L2NOTE = "레벨 2 (응용, 전문대졸·산업기사 수준). 목차 검증 기준: 품질경영산업기사 등 산업공학 분야 산업기사 필기 과목 구성(최신 공고 확인)과 {}. 레벨1에 산업 과목이 없어 입문 범위를 넓게 잡았습니다."
L3NOTE = "레벨 3 (심화, 대졸·기사 수준). 목차 검증 기준: 산업공학기사·품질경영기사·인간공학기사 필기 과목 구성(최신 공고 확인)과 {}. 레벨3은 단원당 자가점검 3문항, 학습 조언 1문단의 가벼운 형식입니다."
