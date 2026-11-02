"""정보통신 트랙 가이드 공용 자료와 링크."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gk import *

MIT602 = OCW("6.02", "Introduction to EECS II: Digital Communication Systems (2012년 가을)", "6-02-introduction-to-eecs-ii-digital-communication-systems-fall-2012")
MIT6450 = OCW("6.450", "Principles of Digital Communications I (2006년 가을)", "6-450-principles-of-digital-communications-i-fall-2006")
HAYKIN = book("Wiley", "Haykin, Communication Systems (번역본 『통신 시스템』, 장 제목으로 표기)")
LATHI = book("Oxford University Press", "Lathi · Ding, Modern Digital and Analog Communication Systems (장 제목으로 표기)")
PROAKIS = book("McGraw-Hill", "Proakis · Salehi, Digital Communications (장 제목으로 표기)")
RAPPAPORT = book("Pearson", "Rappaport, Wireless Communications: Principles and Practice (장 제목으로 표기)")
GOLDSMITH = book("Cambridge University Press", "Goldsmith, Wireless Communications (장 제목으로 표기)")
KEISER = book("McGraw-Hill", "Keiser, Optical Fiber Communications (장 제목으로 표기)")
AGRAWAL = book("Wiley", "Agrawal, Fiber-Optic Communication Systems (장 제목으로 표기)")
POZAR = book("Wiley", "Pozar, Microwave Engineering (장 제목으로 표기)")
BALANIS = book("Wiley", "Balanis, Antenna Theory: Analysis and Design (장 제목으로 표기)")
PRATT = book("Wiley", "Pratt · Allnutt, Satellite Communications (장 제목으로 표기)")
TANENBAUM = book("Pearson", "Tanenbaum · Wetherall, Computer Networks (번역본 『컴퓨터 네트워크』, 장 제목으로 표기)")
KUROSE = book("Pearson", "Kurose · Ross, Computer Networking: A Top-Down Approach (장 제목으로 표기)")
DAHLMAN = book("Academic Press", "Dahlman · Parkvall · Sköld, 5G NR: The Next Generation Wireless Access Technology (장 제목으로 표기)")
OPPENHEIMER = book("Cisco Press", "Oppenheimer, Top-Down Network Design (장 제목으로 표기)")
GPP = {"kind": "web", "provider": "3GPP", "title": "3GPP 규격과 릴리스 정보", "url": "https://www.3gpp.org/", "lang": "영어"}
ITU = {"kind": "web", "provider": "ITU", "title": "ITU 무선통신부문(ITU-R) 전파규칙과 권고", "url": "https://www.itu.int/en/ITU-R/", "lang": "영어"}
RRA = {"kind": "web", "provider": "국립전파연구원", "title": "전파 관련 기술기준·고시 안내", "url": "https://www.rra.go.kr/", "lang": "한국어"}

T = "ict"
G2 = lambda s, u, t: {"title": f"레벨2 {t}", "href": f"guide.html?lv=2&t=ict&s={s}&u={u}"}
G2R = lambda s, u, t: {"kind": "web", "provider": "tech-arena 레벨2", "title": t, "url": f"guide.html?lv=2&t=ict&s={s}&u={u}"}
C1 = lambda n, t: {"kind": "web", "provider": "tech-arena 레벨1", "title": f"전기전자 챕터 {n} {t}", "url": f"browse.html?c=c1#ch{n:02d}", "part": "레벨1 복습"}
C4 = lambda n, t: {"kind": "web", "provider": "tech-arena 레벨1", "title": f"컴퓨터 챕터 {n} {t}", "url": f"browse.html?c=c4#ch{n:02d}", "part": "레벨1 복습"}
L1C4 = lambda n, t: {"title": f"레벨1 · 컴퓨터 챕터 {n} {t}", "href": f"browse.html?c=c4#ch{n:02d}"}

L2NOTE = "레벨 2 (응용, 전문대졸·산업기사 수준). 목차 검증 기준: 정보통신산업기사 필기 과목 구성과 {}. 최신 출제 기준은 큐넷(Q-Net) 공고로 확인하세요."
L3NOTE = "레벨 3 (심화, 대졸·기사 수준). 목차 검증 기준: 정보통신기사 필기 과목 구성과 {}. 레벨3은 단원당 자가점검 3문항, 학습 조언 1문단의 가벼운 형식입니다."

RADIO_LAW = "전파법과 대한민국 주파수 분배표(과학기술정보통신부 고시)"
FACILITY_STD = "방송통신설비의 기술기준에 관한 규정과 관련 고시(접지설비·구내통신설비 등)"
