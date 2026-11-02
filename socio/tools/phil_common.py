"""철학·윤리학 트랙 가이드 공용 자료."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gk import *  # noqa: F401,F403

T = "philosophy"
PHIL = OPENSTAX("Introduction to Philosophy", "introduction-philosophy")
IEP = {"kind": "web", "provider": "Internet Encyclopedia of Philosophy", "title": "인터넷 철학 백과사전 (주제별 해설)", "url": "https://iep.utm.edu/", "lang": "영어"}
FORALLX = {"kind": "book", "provider": "Open Logic Project (무료 공개 교재)", "title": "forall x: Calgary — An Introduction to Formal Logic", "url": "https://forallx.openlogicproject.org/", "lang": "영어"}
RUSSELL_POP = {"kind": "book", "provider": "Project Gutenberg (무료 공개)", "title": "Russell, The Problems of Philosophy (번역본 『철학의 문제들』)", "url": "https://www.gutenberg.org/ebooks/5827", "lang": "영어"}
COPI = book("여러 출판사", "Copi · Cohen, Introduction to Logic (번역본 『논리학 입문』, 장 제목으로 표기)")
RUSSELL_HIST = book("을유문화사", "Russell, A History of Western Philosophy (번역본 『서양철학사』, 시대별 장)")
FUNG = book("까치", "펑유란(馮友蘭), 『중국철학사』 (시대별 장)")
PHIL_KR = book("여러 출판사", "대학 철학개론 교재 (분야별 장)")
