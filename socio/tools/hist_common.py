"""한국사·세계사 트랙 가이드 공용 자료."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gk import *  # noqa: F401,F403

ENCY = {"kind": "web", "provider": "한국학중앙연구원", "title": "한국민족문화대백과사전", "url": "https://encykorea.aks.ac.kr/", "lang": "한국어"}
HERITAGE = {"kind": "web", "provider": "국가유산청", "title": "국가유산포털 (유물·유적 검색)", "url": "https://www.heritage.go.kr/", "lang": "한국어"}
EMUSEUM = {"kind": "web", "provider": "국립중앙박물관 등", "title": "e뮤지엄 (전국 박물관 소장품 검색)", "url": "https://www.emuseum.go.kr/", "lang": "한국어"}
HANKOOK = {"kind": "web", "provider": "국사편찬위원회", "title": "한국사능력검정시험 (시험 안내·기출문제)", "url": "https://www.historyexam.go.kr/", "lang": "한국어"}
GILJABI = book("지식산업사", "한국사연구회 편, 『새로운 한국사 길잡이』 상·하 (시대별 장)")
TEUKGANG = book("서울대학교출판문화원", "서울대학교 국사학과 편, 『한국사 특강』 (시대별 장)")
HANKOOK_BOOK = book("여러 출판사", "한국사능력검정시험 심화 기본서 (최신판, 시대별 장)")
WH1 = OPENSTAX("World History Volume 1: to 1500", "world-history-volume-1")
WH2 = OPENSTAX("World History Volume 2: from 1400", "world-history-volume-2")
FAIRBANK = book("까치", "Fairbank · Goldman, China: A New History (번역본 『신중국사』, 시대별 장)")
GORDON = book("이산", "Gordon, A Modern History of Japan (번역본 『현대 일본의 역사』)")
COFFIN = book("소나무", "Coffin 외, Western Civilizations (번역본 『새로운 서양 문명의 역사』, 시대별 장)")
WORLDHIST = {"kind": "web", "provider": "World History Encyclopedia", "title": "World History Encyclopedia (인물·사건 해설)", "url": "https://www.worldhistory.org/", "lang": "영어"}
