"""토목 트랙 가이드 공용 자료와 링크. 정역학·재료역학은 기계 트랙 과목을 공유한다."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gk import *

T = "civil"
GHILANI = book("Pearson", "Ghilani · Wolf, Elementary Surveying (장 제목으로 표기)")
DAS_G = book("Cengage", "Das · Sobhan, Principles of Geotechnical Engineering (번역본 『토질역학』, 장 제목으로 표기)")
DAS_F = book("Cengage", "Das, Principles of Foundation Engineering (번역본 『기초공학』, 장 제목으로 표기)")
CHIN = book("Pearson", "Chin, Water-Resources Engineering (장 제목으로 표기)")
CHOW_OC = book("McGraw-Hill", "Chow, Open-Channel Hydraulics (장 제목으로 표기)")
CHOW_H = book("McGraw-Hill", "Chow · Maidment · Mays, Applied Hydrology (장 제목으로 표기)")
HIB_SA = book("Pearson", "Hibbeler, Structural Analysis (번역본 『구조해석』, 장 제목으로 표기)")
WIGHT = book("Pearson", "Wight · MacGregor, Reinforced Concrete: Mechanics and Design (장 제목으로 표기)")
SALMON = book("Pearson", "Salmon · Johnson · Malhas, Steel Structures: Design and Behavior (장 제목으로 표기)")
KR_RC = book("국내 교재", "철근콘크리트 구조설계(KDS 기준 반영 국내 교재, 최신판)")
KCSC = {"kind": "web", "provider": "국가건설기준센터", "title": "국가건설기준(KDS 설계기준, KCS 시공기준) 검색", "url": "https://www.kcsc.re.kr/", "lang": "한국어"}
NGII = {"kind": "web", "provider": "국토지리정보원", "title": "측량 기준과 국가기준점·지도 정보", "url": "https://www.ngii.go.kr/", "lang": "한국어"}
KMA = {"kind": "web", "provider": "기상청 기상자료개방포털", "title": "강수 등 기상 관측 자료", "url": "https://data.kma.go.kr/", "lang": "한국어"}
USGS = {"kind": "web", "provider": "USGS Water Science School", "title": "물 순환과 수문학 기초 자료", "url": "https://www.usgs.gov/special-topics/water-science-school", "lang": "영어"}

G2 = lambda s, u, t: {"title": f"레벨2 {t}", "href": f"guide.html?lv=2&t=civil&s={s}&u={u}"}
G2R = lambda s, u, t: {"kind": "web", "provider": "tech-arena 레벨2", "title": t, "url": f"guide.html?lv=2&t=civil&s={s}&u={u}"}
GM = lambda lv, s, u, t: {"kind": "web", "provider": f"tech-arena 레벨{lv} (기계 트랙)", "title": t, "url": f"guide.html?lv={lv}&t=mechanical&s={s}&u={u}"}
GML = lambda lv, s, u, t: {"title": f"레벨{lv} {t} (기계 트랙 공유)", "href": f"guide.html?lv={lv}&t=mechanical&s={s}&u={u}"}
C2 = lambda n, t: {"kind": "web", "provider": "tech-arena 레벨1", "title": f"기계 챕터 {n} {t}", "url": f"browse.html?c=c2#ch{n:02d}", "part": "레벨1 복습"}

L2NOTE = "레벨 2 (응용, 전문대졸·산업기사 수준). 목차 검증 기준: 토목기사 필기 과목 구성의 기초 부분과 {}. 최신 출제 기준은 큐넷(Q-Net) 공고로 확인하세요."
L3NOTE = "레벨 3 (심화, 대졸·기사 수준). 목차 검증 기준: 토목기사 필기 과목 구성(응용역학, 측량학, 수리학 및 수문학, 철근콘크리트 및 강구조, 토질 및 기초, 상하수도공학)과 {}. 레벨3은 단원당 자가점검 3문항, 학습 조언 1문단의 가벼운 형식입니다."
KDS_RC = "국가건설기준 KDS 14 20(콘크리트구조 설계기준)·KDS 14 31(강구조 설계기준)"
