"""화공 트랙 가이드 공용 자료와 링크."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gk import *

T = "chemical"
MIT1037 = OCW("10.37", "Chemical and Biological Reaction Engineering (2007년 봄)", "10-37-chemical-and-biological-reaction-engineering-spring-2007")
LEARNCHEME = {"kind": "video", "provider": "LearnChemE (콜로라도 대학교, 무료)", "title": "화학공학 짧은 강의 영상과 시뮬레이션", "url": "https://learncheme.com/", "lang": "영어"}
FELDER = book("Wiley", "Felder · Rousseau, Elementary Principles of Chemical Processes (번역본 『화공양론』, 장 제목으로 표기)")
HIMMELBLAU = book("Pearson", "Himmelblau · Riggs, Basic Principles and Calculations in Chemical Engineering (장 제목으로 표기)")
SMITH = book("McGraw-Hill", "Smith · Van Ness · Abbott, Introduction to Chemical Engineering Thermodynamics (번역본 『화공열역학』, 장 제목으로 표기)")
MCCABE = book("McGraw-Hill", "McCabe · Smith · Harriott, Unit Operations of Chemical Engineering (번역본 『단위조작』, 장 제목으로 표기)")
FOGLER = book("Pearson", "Fogler, Elements of Chemical Reaction Engineering (번역본 『반응공학』, 장 제목으로 표기)")
LEVENSPIEL = book("Wiley", "Levenspiel, Chemical Reaction Engineering (장 제목으로 표기)")
BSL = book("Wiley", "Bird · Stewart · Lightfoot, Transport Phenomena (장 제목으로 표기)")
WELTY = book("Wiley", "Welty 외, Fundamentals of Momentum, Heat, and Mass Transfer (장 제목으로 표기)")
SEADER = book("Wiley", "Seader · Henley · Roper, Separation Process Principles (장 제목으로 표기)")
SEBORG = book("Wiley", "Seborg · Edgar · Mellichamp · Doyle, Process Dynamics and Control (번역본 『공정제어』, 장 제목으로 표기)")
NISTWEB = {"kind": "web", "provider": "NIST Chemistry WebBook", "title": "물질의 열역학 성질·상평형 데이터", "url": "https://webbook.nist.gov/chemistry/", "lang": "영어"}
KOSHA = {"kind": "web", "provider": "안전보건공단", "title": "공정안전관리(PSM)·화학물질 안전 안내", "url": "https://www.kosha.or.kr/", "lang": "한국어"}

G2 = lambda s, u, t: {"title": f"레벨2 {t}", "href": f"guide.html?lv=2&t=chemical&s={s}&u={u}"}
G2R = lambda s, u, t: {"kind": "web", "provider": "tech-arena 레벨2", "title": t, "url": f"guide.html?lv=2&t=chemical&s={s}&u={u}"}
GM = lambda lv, s, u, t: {"kind": "web", "provider": f"tech-arena 레벨{lv} (기계 트랙)", "title": t, "url": f"guide.html?lv={lv}&t=mechanical&s={s}&u={u}"}
C3 = lambda n, t: {"kind": "web", "provider": "tech-arena 레벨1", "title": f"화학공학 챕터 {n} {t}", "url": f"browse.html?c=c3#ch{n:02d}", "part": "레벨1 복습"}

L2NOTE = "레벨 2 (응용, 전문대졸·산업기사 수준). 목차 검증 기준: 화공기사 필기 과목 구성의 기초 부분과 {}. 최신 출제 기준은 큐넷(Q-Net) 공고로 확인하세요."
L3NOTE = "레벨 3 (심화, 대졸·기사 수준). 목차 검증 기준: 화공기사 필기 과목 구성(공정시스템, 단위공정관리, 반응운전, 화공계측제어 — 최신 공고 확인)과 {}. 레벨3은 단원당 자가점검 3문항, 학습 조언 1문단의 가벼운 형식입니다."
