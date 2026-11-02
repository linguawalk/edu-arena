"""컴퓨터 트랙 가이드 공용 자료와 링크.

code-arena와의 경계: tech-arena는 시스템 원리와 설계를, code-arena는 코드 작성과 구현 실습을 맡는다.
가이드는 실습 자료로 code-arena 모듈·언어 트랙을 링크한다.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gk import *

T = "computer"
MIT6004 = OCW("6.004", "Computation Structures (2017년 봄)", "6-004-computation-structures-spring-2017")
PH = book("Morgan Kaufmann", "Patterson · Hennessy, Computer Organization and Design RISC-V Edition (번역본 『컴퓨터 구조 및 설계』, 장 제목으로 표기)")
N2T = {"kind": "web", "provider": "Nand2Tetris (무료 공개 과정)", "title": "From Nand to Tetris — 게이트부터 컴퓨터·컴파일러까지", "url": "https://www.nand2tetris.org/", "lang": "영어"}
OSTEP = {"kind": "book", "provider": "Arpaci-Dusseau (무료 공개 교재)", "title": "Operating Systems: Three Easy Pieces", "url": "https://pages.cs.wisc.edu/~remzi/OSTEP/", "lang": "영어"}
SILBER_OS = book("Wiley", "Silberschatz · Galvin · Gagne, Operating System Concepts (번역본 『운영체제』, 장 제목으로 표기)")
KUROSE = book("Pearson", "Kurose · Ross, Computer Networking: A Top-Down Approach (번역본 『컴퓨터 네트워킹 하향식 접근』, 장 제목으로 표기)")
WIRESHARK = {"kind": "web", "provider": "Wireshark", "title": "Wireshark 패킷 분석기와 사용자 안내서", "url": "https://www.wireshark.org/", "lang": "영어"}
DBBOOK = {"kind": "book", "provider": "Silberschatz · Korth · Sudarshan", "title": "Database System Concepts (교재 사이트, 장 제목으로 표기)", "url": "https://www.db-book.com/", "lang": "영어"}
CMU445 = {"kind": "lecture", "provider": "CMU 15-445 (공개 강의)", "title": "Intro to Database Systems — 강의 노트·영상", "url": "https://15445.courses.cs.cmu.edu/", "lang": "영어"}
SOMMERVILLE = book("Pearson", "Sommerville, Software Engineering (장 제목으로 표기)")
PRESSMAN = book("McGraw-Hill", "Pressman · Maxim, Software Engineering: A Practitioner's Approach (장 제목으로 표기)")
GOF = book("Addison-Wesley", "Gamma 외, Design Patterns (번역본 『GoF의 디자인 패턴』)")
PROGIT = {"kind": "book", "provider": "git-scm.com (무료 공개 교재, 한국어판 있음)", "title": "Pro Git", "url": "https://git-scm.com/book/ko/v2", "lang": "한국어"}
CSAPP = book("Pearson", "Bryant · O'Hallaron, Computer Systems: A Programmer's Perspective (번역본 『컴퓨터 시스템』, 장 제목으로 표기)")
CMU213 = {"kind": "lecture", "provider": "CMU 15-213 (공개 강의 자료)", "title": "Introduction to Computer Systems", "url": "https://www.cs.cmu.edu/~213/", "lang": "영어"}
DDIA = book("O'Reilly", "Kleppmann, Designing Data-Intensive Applications (번역본 『데이터 중심 애플리케이션 설계』)")
MIT6824 = {"kind": "lecture", "provider": "MIT 6.5840 (구 6.824, 공개 강의 자료)", "title": "Distributed Systems", "url": "https://pdos.csail.mit.edu/6.824/", "lang": "영어"}
RAFT = {"kind": "web", "provider": "Raft 공식 사이트", "title": "The Raft Consensus Algorithm (논문·시각화)", "url": "https://raft.github.io/", "lang": "영어"}
K8S = {"kind": "web", "provider": "Kubernetes 공식 문서 (한국어판 있음)", "title": "쿠버네티스 문서", "url": "https://kubernetes.io/ko/docs/", "lang": "한국어"}
STALLINGS = book("Pearson", "Stallings · Brown, Computer Security: Principles and Practice (장 제목으로 표기)")
OWASP = {"kind": "web", "provider": "OWASP", "title": "OWASP Top 10 웹 애플리케이션 보안 위험", "url": "https://owasp.org/www-project-top-ten/", "lang": "영어"}
KISA = {"kind": "web", "provider": "한국인터넷진흥원(KISA)", "title": "보안 가이드·ISMS-P 인증 안내", "url": "https://www.kisa.or.kr/", "lang": "한국어"}
PIPC = {"kind": "web", "provider": "개인정보보호위원회", "title": "개인정보 보호법령과 안내서", "url": "https://www.pipc.go.kr/", "lang": "한국어"}
DRAGON = book("Pearson", "Aho · Lam · Sethi · Ullman, Compilers: Principles, Techniques, and Tools (일명 드래곤 북, 장 제목으로 표기)")
CRAFTING = {"kind": "book", "provider": "Nystrom (무료 공개 교재)", "title": "Crafting Interpreters", "url": "https://craftinginterpreters.com/", "lang": "영어"}

CA = lambda title, q, part=None: dict({"kind": "web", "provider": "code-arena (실습)", "title": title, "url": "https://code-arena.org/browse.html?" + q, "lang": "한국어"}, **({"part": part} if part else {}))
CA_DSA = CA("자료구조 & 알고리즘 모듈", "type=module&key=dsa")
CA_LINUX = CA("Linux 모듈 (권한·명령어·프로세스·셸)", "type=module&key=linux")
CA_DB = CA("DB 이론 모듈", "type=module&key=db_theory")
CA_C = CA("C 언어 트랙", "type=language&track=track_a&lang=c")
CA_SQL = {"kind": "web", "provider": "code-arena (실습)", "title": "SQL 코드 작성 실습", "url": "https://code-arena.org/", "lang": "한국어", "part": "실습(코드 작성) → SQL"}
CAL = lambda title, q: {"title": f"code-arena · {title}", "href": "https://code-arena.org/browse.html?" + q}

G2 = lambda s, u, t: {"title": f"레벨2 {t}", "href": f"guide.html?lv=2&t=computer&s={s}&u={u}"}
G2R = lambda s, u, t: {"kind": "web", "provider": "tech-arena 레벨2", "title": t, "url": f"guide.html?lv=2&t=computer&s={s}&u={u}"}
C4 = lambda n, t: {"kind": "web", "provider": "tech-arena 레벨1", "title": f"컴퓨터 챕터 {n} {t}", "url": f"browse.html?c=c4#ch{n:02d}", "part": "레벨1 복습"}
L1C4 = lambda n, t: {"title": f"레벨1 · 컴퓨터 챕터 {n} {t}", "href": f"browse.html?c=c4#ch{n:02d}"}

L2NOTE = "레벨 2 (응용, 전문대졸·산업기사 수준). 목차 검증 기준: 정보처리산업기사·정보처리기사 필기 과목 구성과 {}. 최신 출제 기준은 큐넷(Q-Net) 공고로 확인하세요. 코드 작성 실습은 code-arena를 링크합니다."
L3NOTE = "레벨 3 (심화, 대졸·기사 수준). 목차 검증 기준: 정보처리기사·정보보안기사 필기 과목 구성과 {}. 레벨3은 단원당 자가점검 3문항, 학습 조언 1문단의 가벼운 형식입니다."
