"""기계 트랙 가이드 공용 자료와 링크. 정역학·재료역학은 토목·건축 트랙과 공유한다."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gk import *

T = "mechanical"
MIT2001 = OCW("2.001", "Mechanics & Materials I (2006년 가을)", "2-001-mechanics-materials-i-fall-2006")
MIT2003 = OCW("2.003SC", "Engineering Dynamics (2011년 가을)", "2-003sc-engineering-dynamics-fall-2011")
MIT206 = OCW("2.06", "Fluid Dynamics (2013년 봄)", "2-06-fluid-dynamics-spring-2013")
UP1 = OPENSTAX("University Physics Volume 1 (역학)", "university-physics-volume-1")
UP2 = OPENSTAX("University Physics Volume 2 (열역학)", "university-physics-volume-2")
ESTATICS = {"kind": "book", "provider": "Baker · Haynes (무료 공개 교재)", "title": "Engineering Statics: Open and Interactive", "url": "https://engineeringstatics.org/", "lang": "영어"}
AHTT = {"kind": "book", "provider": "Lienhard (무료 공개 교재)", "title": "A Heat Transfer Textbook", "url": "https://ahtt.mit.edu/", "lang": "영어"}
BEER_S = book("McGraw-Hill", "Beer · Johnston, Vector Mechanics for Engineers: Statics (번역본 『정역학』, 장 제목으로 표기)")
BEER_M = book("McGraw-Hill", "Beer · Johnston, Mechanics of Materials (번역본 『재료역학』, 장 제목으로 표기)")
HIBBELER = book("Pearson", "Hibbeler, Mechanics of Materials / Engineering Mechanics (장 제목으로 표기)")
CENGEL_T = book("McGraw-Hill", "Çengel · Boles, Thermodynamics: An Engineering Approach (번역본 『열역학』, 장 제목으로 표기)")
SHIGLEY = book("McGraw-Hill", "Budynas · Nisbett, Shigley's Mechanical Engineering Design (번역본 『기계설계』, 장 제목으로 표기)")
NORTON = book("Pearson", "Norton, Machine Design (장 제목으로 표기)")
WHITE_F = book("McGraw-Hill", "White, Fluid Mechanics (번역본 『유체역학』, 장 제목으로 표기)")
INCROPERA = book("Wiley", "Bergman 외, Fundamentals of Heat and Mass Transfer (번역본 『열전달』, 장 제목으로 표기)")
RAO = book("Pearson", "Rao, Mechanical Vibrations (번역본 『기계진동학』, 장 제목으로 표기)")
MERIAM = book("Wiley", "Meriam · Kraige, Engineering Mechanics: Dynamics (장 제목으로 표기)")
KSDRAW = book("한국표준협회 등", "KS 기계제도 교재(KS B 0001 기계제도 등, 최신판 기준)")
KSSITE = {"kind": "web", "provider": "e나라표준인증", "title": "KS 표준 검색", "url": "https://www.standard.go.kr/", "lang": "한국어"}

G2 = lambda s, u, t: {"title": f"레벨2 {t}", "href": f"guide.html?lv=2&t=mechanical&s={s}&u={u}"}
G2R = lambda s, u, t: {"kind": "web", "provider": "tech-arena 레벨2", "title": t, "url": f"guide.html?lv=2&t=mechanical&s={s}&u={u}"}
C2 = lambda n, t: {"kind": "web", "provider": "tech-arena 레벨1", "title": f"기계 챕터 {n} {t}", "url": f"browse.html?c=c2#ch{n:02d}", "part": "레벨1 복습"}

L2NOTE = "레벨 2 (응용, 전문대졸·산업기사 수준). 목차 검증 기준: 기계 분야 산업기사(기계설계산업기사 등) 필기 과목 구성과 {}. 최신 출제 기준은 큐넷(Q-Net) 공고로 확인하세요."
L3NOTE = "레벨 3 (심화, 대졸·기사 수준). 목차 검증 기준: 일반기계기사 필기 과목 구성(재료역학, 기계열역학, 기계유체역학, 기계재료 및 유압기기, 기계제작법 및 기계동력학)과 {}. 레벨3은 단원당 자가점검 3문항, 학습 조언 1문단의 가벼운 형식입니다."
