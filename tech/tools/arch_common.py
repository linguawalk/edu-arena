"""건축 트랙 가이드 공용 자료와 링크. 정역학은 기계 트랙, 구조해석·RC·기초는 토목 트랙 과목과 연결한다."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gk import *

T = "architecture"
CHING_F = book("Wiley", "Ching, Architecture: Form, Space, and Order (번역본 『건축: 형태, 공간, 그리고 질서』)")
NEUFERT = book("Wiley", "Neufert, Architects' Data (번역본 『건축 설계 자료집』)")
ALLEN = book("Wiley", "Allen · Iano, Fundamentals of Building Construction: Materials and Methods (장 제목으로 표기)")
CHING_S = book("Wiley", "Ching · Onouye · Zuberbuhler, Building Structures Illustrated (장 제목으로 표기)")
GRONDZIK = book("Wiley", "Grondzik · Kwok, Mechanical and Electrical Equipment for Buildings (장 제목으로 표기)")
TARANATH = book("CRC Press", "Taranath, Structural Analysis and Design of Tall Buildings (장 제목으로 표기)")
LYNCH = book("MIT Press", "Lynch, The Image of the City (번역본 『도시의 이미지』)")
GEHL = book("Island Press", "Gehl, Cities for People (번역본 『인간을 위한 도시 만들기』)")
KR_ARCH = book("국내 교재", "건축계획·건축시공·건축설비 국내 교재(최신 법령 반영판)")
LAW = {"kind": "web", "provider": "국가법령정보센터", "title": "건축법, 국토의 계획 및 이용에 관한 법률, 녹색건축물 조성 지원법 등", "url": "https://www.law.go.kr/", "lang": "한국어", "part": "법령 검색에서 이름으로 찾기"}
KCSC = {"kind": "web", "provider": "국가건설기준센터", "title": "국가건설기준(KDS 41 건축구조기준 등) 검색", "url": "https://www.kcsc.re.kr/", "lang": "한국어"}
PHI = {"kind": "web", "provider": "Passive House Institute", "title": "패시브하우스 기준과 자료", "url": "https://passivehouse.com/", "lang": "영어"}
USGBC = {"kind": "web", "provider": "U.S. Green Building Council", "title": "LEED 녹색 건축 인증", "url": "https://www.usgbc.org/leed", "lang": "영어"}

G2 = lambda s, u, t: {"title": f"레벨2 {t}", "href": f"guide.html?lv=2&t=architecture&s={s}&u={u}"}
G2R = lambda s, u, t: {"kind": "web", "provider": "tech-arena 레벨2", "title": t, "url": f"guide.html?lv=2&t=architecture&s={s}&u={u}"}
GC = lambda lv, s, u, t: {"kind": "web", "provider": f"tech-arena 레벨{lv} (토목 트랙)", "title": t, "url": f"guide.html?lv={lv}&t=civil&s={s}&u={u}"}
GCL = lambda lv, s, u, t: {"title": f"레벨{lv} {t} (토목 트랙)", "href": f"guide.html?lv={lv}&t=civil&s={s}&u={u}"}
GML = lambda lv, s, u, t: {"title": f"레벨{lv} {t} (기계 트랙 공유)", "href": f"guide.html?lv={lv}&t=mechanical&s={s}&u={u}"}
GMR = lambda lv, s, u, t: {"kind": "web", "provider": f"tech-arena 레벨{lv} (기계 트랙)", "title": t, "url": f"guide.html?lv={lv}&t=mechanical&s={s}&u={u}"}

L2NOTE = "레벨 2 (응용, 전문대졸·산업기사 수준). 목차 검증 기준: 건축산업기사 필기 과목 구성(건축계획, 건축시공, 건축구조, 건축설비, 건축법규 — 최신 공고 확인)과 {}."
L3NOTE = "레벨 3 (심화, 대졸·기사 수준). 목차 검증 기준: 건축기사 필기 과목 구성(건축계획, 건축시공, 건축구조, 건축설비, 건축관계법규 — 최신 공고 확인)과 {}. 레벨3은 단원당 자가점검 3문항, 학습 조언 1문단의 가벼운 형식입니다."
ARCH_LAW = "건축법·같은 법 시행령·건축물의 피난·방화구조 등의 기준에 관한 규칙"
