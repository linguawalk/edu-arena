"""lit-arena 레벨2·3 가이드 공용 자료."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gk import *  # noqa: F401,F403

# 문학
WELLEK = book("문예출판사 등", "Wellek · Warren, Theory of Literature (번역본 『문학의 이론』, 장 제목으로 표기)")
EAGLETON = book("창비 등", "Eagleton, Literary Theory: An Introduction (번역본 『문학이론입문』)")
ABRAMS = book("교보문고 등", "Abrams, The Mirror and the Lamp (번역본 『거울과 등불』)")
CULLER = book("교유서가 등", "Culler, Literary Theory: A Very Short Introduction (번역본 『문학이론』)")
CHO_DI = book("지식산업사", "조동일, 『한국문학통사』 1~6 (시대별 권으로 표기)")
KIM_HK = book("민음사", "김흥규, 『한국문학의 이해』")
KIM_KIM = book("민음사", "김윤식 · 김현, 『한국문학사』")
KWON_YM = book("민음사", "권영민, 『한국현대문학사』 1~2")
AUERBACH = book("민음사 등", "Auerbach, Mimesis (번역본 『미메시스』, 장 제목으로 표기)")
NORTON = book("W. W. Norton", "The Norton Anthology of World Literature (시대별 권으로 표기)")
KIM_HJ = book("신아사", "김학주, 『중국문학사』")
KEENE = book("여러 출판사", "Keene, 일본문학사(Seeds in the Heart 등 시대별 권, 번역본 제목으로 표기)")
KLTI = WEB("한국문학번역원", "한국문학번역원 (해외 출판·번역 현황)", "https://www.ltikorea.or.kr/")
KDB = WEB("한국학중앙연구원", "한국민족문화대백과사전 (작가·작품 항목)", "https://encykorea.aks.ac.kr/")
CTEXT = WEB("Chinese Text Project", "중국 고전 원문 데이터베이스", "https://ctext.org/", "중국어·영어")
NOBEL = WEB("Nobel Prize Outreach", "노벨 문학상 수상자와 선정 이유", "https://www.nobelprize.org/prizes/literature/", "영어")

# 국어학
LEE_IS = book("학연사", "이익섭, 『국어학개설』")
NAM_KO = book("한국문화사 등", "남기심 · 고영근 외, 『표준 국어문법론』")
KO_KU = book("집문당", "고영근 · 구본관, 『우리말 문법론』")
LEE_CHAE = book("학연사", "이익섭 · 채완, 『국어문법론강의』")
URIMAL = WEB("국립국어원", "우리말샘 (개방형 사전)", "https://opendict.korean.go.kr/")
KORQA = WEB("국립국어원", "온라인 가나다 (어문 규범 질의응답)", "https://korean.go.kr/")

# 한자·한문
HANJA_TEST = WEB("한국어문회", "한자능력검정시험 (급수별 배정 한자·출제 기준)", "https://www.hanja.re.kr/")
SHUOWEN = WEB("Chinese Text Project", "『설문해자』 원문", "https://ctext.org/shuo-wen-jie-zi", "중국어·영어")
HANMUN_BOOK = book("여러 출판사", "대학 한문 문법·한문 강독 교재 (장 제목으로 표기)")

# 영어학
FROMKIN = book("Cengage", "Fromkin · Rodman · Hyams, An Introduction to Language (장 제목으로 표기)")
YULE = book("Cambridge University Press", "Yule, The Study of Language (장 제목으로 표기)")
SWALES = book("University of Michigan Press", "Swales · Feak, Academic Writing for Graduate Students")
OWL = WEB("Purdue University", "Purdue OWL (학술 글쓰기·인용 형식)", "https://owl.purdue.edu/", "영어")
AWL = WEB("Victoria University of Wellington", "Academic Word List (학술 어휘 목록)", "https://www.wgtn.ac.nz/lals/resources/academicwordlist", "영어")
