"""정치학·행정학·법학 트랙 가이드 공용 자료."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gk import *  # noqa: F401,F403

POLSCI = OPENSTAX("Introduction to Political Science", "introduction-political-science")
HEYWOOD = book("여러 출판사", "Heywood, Politics (번역본 『정치학』, 장 제목으로 표기)")
BAYLIS = book("을유문화사", "Baylis · Smith · Owens, The Globalization of World Politics (번역본 『세계 정치론』, 장 제목으로 표기)")
KPOL_BOOK = book("여러 출판사", "대학 한국 정치론 교재 (한국 정치의 제도와 과정, 장 제목으로 표기)")
ADMIN_BOOK = book("여러 출판사", "대학 행정학원론 교재 (공무원 시험 행정학 범위, 장 제목으로 표기)")
LAWINTRO_BOOK = book("여러 출판사", "대학 법학개론 교재 (장 제목으로 표기)")
CONST_BOOK = book("여러 출판사", "대학 헌법 교과서 (헌법총론·기본권론·통치구조론, 장 제목으로 표기)")
CIVIL_BOOK = book("여러 출판사", "대학 민법총칙 교과서 (장 제목으로 표기)")
ASSEMBLY = {"kind": "web", "provider": "대한민국 국회", "title": "국회 누리집 (의안 정보, 국회 구성)", "url": "https://www.assembly.go.kr/", "lang": "한국어"}
NEC = {"kind": "web", "provider": "중앙선거관리위원회", "title": "선거 통계·선거 제도 안내", "url": "https://www.nec.go.kr/", "lang": "한국어"}
CCOURT = {"kind": "web", "provider": "헌법재판소", "title": "헌법재판소 결정 검색", "url": "https://www.ccourt.go.kr/", "lang": "한국어"}
SCOURT = {"kind": "web", "provider": "대법원", "title": "대법원 종합법률정보 (판례 검색)", "url": "https://glaw.scourt.go.kr/", "lang": "한국어"}
EASYLAW = {"kind": "web", "provider": "법제처", "title": "찾기 쉬운 생활 법령 정보", "url": "https://www.easylaw.go.kr/", "lang": "한국어"}
MOIS = {"kind": "web", "provider": "행정안전부", "title": "정부 조직 관리 정보", "url": "https://www.mois.go.kr/", "lang": "한국어"}
GOSI = {"kind": "web", "provider": "인사혁신처", "title": "사이버국가고시센터 (공무원 시험 과목 안내)", "url": "https://www.gosi.kr/", "lang": "한국어"}
