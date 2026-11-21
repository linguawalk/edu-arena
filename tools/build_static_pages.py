"""edu-arena 안내 페이지 생성: 소개, 개인정보처리방침, 이용약관, 문의, 로그인, 내 계정.

    python3 tools/build_static_pages.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_parts import FOOT_CSS, FOOT_HTML, SITE_JS, SITE, ICON_HEAD, MARK, social

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EFFECTIVE = "2026년 11월 21일"
OFFICER = "김양석"
OPERATOR = "여행일기"
BIZNO = "720-97-01549"
EMAIL = "contact@edu-arena.org"

CSS = """
:root{--paper:#FAFBFD;--ink:#172033;--ink-soft:#4A5670;--grid:#DCE4F0;--blue:#1D3FA8;--blue-soft:#E7ECFA;--warn:#8A1C1C;
  --font:"IBM Plex Sans KR","Apple SD Gothic Neo","Malgun Gothic",sans-serif}
*{box-sizing:border-box}
html,body{margin:0;word-break:keep-all;overflow-wrap:anywhere;background:var(--paper);color:var(--ink);font-family:var(--font)}
:focus-visible{outline:3px solid var(--blue);outline-offset:3px}
.wrap{max-width:820px;margin:0 auto;padding:0 20px}
header{border-bottom:1px solid var(--grid);background:#fff}
header .hin{max-width:1040px;margin:0 auto;padding:0 20px;display:flex;align-items:center;justify-content:space-between;height:60px}
.logo{font-weight:700;font-size:20px;color:var(--ink);text-decoration:none}.logo{display:inline-flex;align-items:center;gap:9px}.logo .ea-mark{flex:none;display:block}
header nav a{color:var(--ink-soft);text-decoration:none;margin-left:16px;font-size:15px}
header nav a:hover{color:var(--ink);text-decoration:underline}
main{padding:36px 0 8px;line-height:1.75;font-size:16px}
h1{font-size:30px;line-height:1.3;margin:0 0 8px}
h2{font-size:20px;margin:36px 0 8px;padding-top:4px}
h3{font-size:17px;margin:20px 0 6px}
.lede{color:var(--ink-soft);margin:0 0 20px}
table{border-collapse:collapse;width:100%;font-size:15px;margin:8px 0}
th,td{border:1px solid var(--grid);padding:8px 10px;text-align:left;vertical-align:top}
th{background:var(--blue-soft)}
.card{background:#fff;border:1px solid var(--grid);border-radius:10px;padding:20px;margin:16px 0}
label{display:block;font-weight:500;margin:14px 0 6px}
input[type=text],input[type=email],input[type=password],select,textarea{width:100%;font:inherit;padding:10px 12px;border:1px solid #B9C7DD;border-radius:8px;background:#fff;color:var(--ink)}
textarea{min-height:160px;resize:vertical}
.check{display:flex;gap:8px;align-items:flex-start;font-weight:400;margin:10px 0}
.check input{margin-top:6px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;font:inherit;font-weight:700;padding:12px 18px;border-radius:8px;border:1px solid var(--blue);background:var(--blue);color:#fff;cursor:pointer;text-decoration:none;min-height:44px}
.btn.ghost{background:#fff;color:var(--blue)}
.btn.kakao{background:#FEE500;border-color:#FEE500;color:#191919}
.btn.danger{background:#fff;color:var(--warn);border-color:var(--warn)}
.btn[disabled]{opacity:.45;cursor:not-allowed}
.stack{display:grid;gap:10px;margin:16px 0}
.note{font-size:14px;color:var(--ink-soft)}
.msg{padding:12px 14px;border-radius:8px;background:var(--blue-soft);margin:14px 0}
.msg.err{background:#FBEAEA;color:var(--warn)}
.hp{position:absolute;left:-9999px}
[hidden]{display:none!important}
"""


def page(slug, title, desc, body, extra_head="", noindex=False):
    robots = '<meta name="robots" content="noindex, follow">\n' if noindex else ""
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
{ICON_HEAD}
{robots}<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · edu-arena</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{slug}">
{social(title + " · edu-arena", desc, SITE + "/" + slug)}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<style>{CSS}{FOOT_CSS}</style>
{extra_head}</head>
<body>
<header><div class="hin"><a class="logo" href="/">{MARK}<span>edu-arena</span></a><nav data-auth><a href="/lessons.html">레슨 목록</a></nav></div></header>
<main class="wrap">
{body}
</main>
{FOOT_HTML}
{'' if 'site.js' in extra_head else SITE_JS}
</body>
</html>
"""
    with open(os.path.join(ROOT, slug), "w", encoding="utf-8") as f:
        f.write(html)
    print("작성:", slug)


ABOUT = """
<h1>edu-arena 소개</h1>
<p class="lede">읽기 전에 먼저 풀어 보는 15분 레슨으로 고교 교과부터 대학 수준, 올림피아드 심화까지 공부하는 무료 학습 사이트입니다.</p>

<h2>무엇을 배울 수 있나요</h2>
<p>인문사회(사회와 역사, 경제와 경영, 언어와 문학, 외국어), 수학·과학(수학, 과학, 공학, 코딩), 예체능의 9개 과목, 66개 코스를 한곳에 모았습니다. 모든 레슨은 edu-arena가 직접 쓴 설명과 문제로 이루어져 있습니다.</p>

<h2>어떻게 배우나요</h2>
<p>레슨은 짧은 설명 하나, 곧바로 문제 하나가 번갈아 나오는 방식입니다. 답을 입력하면 바로 채점되고, 틀리면 힌트와 해설을 볼 수 있습니다. 레슨마다 연습 문제와, 생각을 글로 정리해 보는 에세이(논술) 과제가 함께 있습니다.</p>
<ul>
<li><strong>레벨1 · 고교 수준</strong>: 설명과 문제가 번갈아 나오는 레슨으로 배웁니다. 기초가 불안하면 진입 진단으로 시작 위치를 찾을 수 있습니다.</li>
<li><strong>레벨2 · 전문대 수준, 레벨3 · 대학 수준</strong>: 주제별 독학 가이드로 스스로 공부합니다.</li>
<li><strong>심화</strong>: 과목별 올림피아드·경시를 준비하는 과정입니다.</li>
</ul>

<h2>이용 요금</h2>
<p>모든 학습 콘텐츠는 로그인 없이 무료로 이용할 수 있습니다. 사이트 운영비는 광고 수익으로 충당합니다. 회원으로 가입하면 학습 기록을 계정에 보관하는 등의 기능을 이용할 수 있습니다.</p>

<h2>만든 사람</h2>
<p>edu-arena는 출판사 여행일기(대표 김양석, 사업자등록번호 720-97-01549)가 기획하고 제작합니다. 콘텐츠의 오류를 발견하셨거나 제안이 있으시면 <a href="/contact.html">문의 페이지</a>나 <a href="mailto:contact@edu-arena.org">contact@edu-arena.org</a>로 알려 주세요. 확인 후 고치겠습니다.</p>
"""

PRIVACY = f"""
<h1>개인정보처리방침</h1>
<p class="lede">edu-arena(이하 "사이트")는 {OPERATOR}(사업자등록번호 {BIZNO})가 운영하며, 「개인정보 보호법」에 따라 이용자의 개인정보를 보호하고 관련 고충을 원활하게 처리하기 위해 다음과 같이 개인정보처리방침을 둡니다. 시행일: {EFFECTIVE}</p>

<h2>1. 처리하는 개인정보와 목적</h2>
<table>
<tr><th>구분</th><th>항목</th><th>목적</th></tr>
<tr><td>회원가입·로그인(이메일)</td><td>이메일 주소, 비밀번호(단방향 암호화하여 저장되며 운영자도 알 수 없음)</td><td>회원 식별, 로그인, 가입 확인·비밀번호 재설정 메일 발송, 계정 관리</td></tr>
<tr><td>회원가입·로그인(구글·카카오)</td><td>이메일 주소, 서비스별 회원 식별자, 닉네임(제공되는 경우)</td><td>회원 식별, 계정 관리</td></tr>
<tr><td>학습 진도(회원)</td><td>완료한 레슨·에세이의 식별자, 점수, 완료 일시</td><td>다른 기기에서 이어 학습, 내 학습 진도 화면 제공, 서비스 운영 통계</td></tr>
<tr><td>회원 동의 기록</td><td>만 14세 이상 확인 여부, 약관·방침 동의 일시</td><td>가입 요건 확인과 동의 증빙</td></tr>
<tr><td>문의</td><td>이름(또는 별칭), 회신받을 이메일 주소, 문의 내용</td><td>문의 확인과 답변</td></tr>
<tr><td>자동 수집</td><td>접속 기록, 방문 페이지, 기기·브라우저 정보, 쿠키, 대략적인 위치(국가·도시 수준)</td><td>방문 통계 분석, 서비스 개선, 광고 게재</td></tr>
</table>
<p>로그인하지 않고 레슨을 풀 때 생기는 학습 진도와 점수는 이용자의 브라우저(로컬 저장소)에만 저장되며 사이트가 수집하지 않습니다. 회원으로 로그인한 경우에는 위 표의 학습 진도가 계정에 저장됩니다. 운영자는 회원 관리와 서비스 운영 통계를 위해 관리자 화면에서 회원의 이메일, 가입 방식, 가입일, 학습 진도를 확인할 수 있으며, 이 권한은 지정된 관리자에게만 있습니다.</p>

<h2>2. 보유 및 이용 기간</h2>
<ul>
<li>회원 정보: 회원 탈퇴 시까지 보유하며, 탈퇴하면 지체 없이 삭제합니다.</li>
<li>문의 내용: 답변을 마친 날부터 1년간 보관한 뒤 삭제합니다.</li>
<li>방문 통계: 구글 애널리틱스의 데이터 보존 기간 설정(14개월)에 따라 보관 후 자동 삭제됩니다.</li>
<li>다른 법령에 따라 보존할 의무가 있는 경우에는 그 기간 동안 보관합니다.</li>
</ul>

<h2>3. 제3자 제공</h2>
<p>사이트는 이용자의 개인정보를 제3자에게 제공하지 않습니다. 다만 이용자가 동의하거나 법령에 특별한 규정이 있는 경우는 예외로 합니다.</p>

<h2>4. 처리 위탁과 국외 이전</h2>
<p>사이트는 서비스 운영을 위해 다음과 같이 개인정보 처리를 위탁하며, 이 과정에서 개인정보가 국외로 이전될 수 있습니다. 이전은 이용자가 서비스를 이용할 때 정보통신망을 통해 이루어집니다.</p>
<table>
<tr><th>수탁자(국가)</th><th>위탁 업무</th><th>이전 항목</th><th>보유 기간</th></tr>
<tr><td>Supabase, Inc.(미국, 데이터 저장 위치: 대한민국 서울 리전)</td><td>회원 인증, 계정 정보 보관</td><td>이메일 주소, 회원 식별자, 동의 기록</td><td>회원 탈퇴 시까지</td></tr>
<tr><td>Web3Creative(인도, 서비스명 Web3Forms)</td><td>문의 내용을 운영자 메일로 전달</td><td>이름, 회신 이메일, 문의 내용</td><td>전달 후 수탁자 정책에 따름</td></tr>
<tr><td>Google LLC(미국)</td><td>방문 통계 분석(구글 애널리틱스), 광고 게재(구글 애드센스)</td><td>접속 기록, 쿠키, 기기·브라우저 정보</td><td>각 서비스 정책과 설정에 따름</td></tr>
</table>
<p>국외 이전을 원하지 않는 이용자는 회원으로 가입하지 않거나 문의 양식을 이용하지 않을 수 있으며, 아래 6항의 방법으로 쿠키 저장을 거부할 수 있습니다. 이 경우에도 학습 콘텐츠는 그대로 이용할 수 있습니다.</p>

<h2>5. 만 14세 미만 아동</h2>
<p>사이트는 만 14세 미만 아동의 회원가입을 받지 않습니다. 가입할 때 만 14세 이상임을 확인하며, 만 14세 미만 아동의 개인정보가 수집된 사실을 알게 되면 즉시 삭제합니다. 학습 콘텐츠는 회원가입 없이 누구나 이용할 수 있습니다.</p>

<h2>6. 쿠키와 광고</h2>
<p>사이트는 방문 통계 분석과 광고 게재를 위해 쿠키를 사용합니다.</p>
<ul>
<li><strong>구글 애널리틱스</strong>: 방문자가 어떤 페이지를 얼마나 보는지 통계를 내기 위해 쿠키를 사용합니다. 개인을 식별하지 않는 통계 형태로만 활용합니다.</li>
<li><strong>구글 애드센스</strong>: Google을 포함한 제3자 광고 사업자는 쿠키를 사용해 이용자가 이 사이트나 다른 웹사이트를 방문한 기록을 바탕으로 광고를 게재합니다. Google은 광고 쿠키를 사용해 이용자의 방문 기록에 맞춘 광고를 보여 줄 수 있습니다.</li>
</ul>
<p>쿠키 저장을 원하지 않으면 다음 방법으로 거부할 수 있습니다.</p>
<ul>
<li>맞춤 광고 해제: <a href="https://adssettings.google.com" rel="nofollow">Google 광고 설정</a>에서 맞춤 광고를 끌 수 있습니다.</li>
<li>방문 통계 제외: <a href="https://tools.google.com/dlpage/gaoptout" rel="nofollow">구글 애널리틱스 차단 브라우저 부가 기능</a>을 설치할 수 있습니다.</li>
<li>브라우저 설정: 웹 브라우저의 설정 메뉴에서 쿠키 저장을 거부하거나 삭제할 수 있습니다. 쿠키를 거부해도 학습 콘텐츠는 이용할 수 있습니다.</li>
</ul>
<p>광고 사업자의 개인정보 처리에 관한 자세한 내용은 <a href="https://policies.google.com/technologies/ads?hl=ko" rel="nofollow">Google 광고 정책</a>을 참고하세요. 유럽경제지역·영국·스위스에서 접속하는 이용자에게는 광고 쿠키 사용 전에 동의를 묻습니다.</p>

<h2>7. 이용자의 권리와 행사 방법</h2>
<p>이용자는 언제든지 자신의 개인정보를 열람·정정·삭제하거나 처리 정지를 요구할 수 있습니다. 회원은 <a href="/account.html">내 계정</a> 화면에서 가입 정보를 확인하고 직접 탈퇴할 수 있으며, 그 밖의 요청은 <a href="/contact.html">문의 페이지</a>로 보내 주시면 지체 없이 처리합니다.</p>

<h2>8. 파기 절차와 방법</h2>
<p>보유 기간이 끝나거나 처리 목적을 이룬 개인정보는 지체 없이 파기합니다. 전자 파일 형태의 정보는 복구할 수 없는 방법으로 삭제합니다.</p>

<h2>9. 안전성 확보 조치</h2>
<ul>
<li>모든 통신을 HTTPS로 암호화합니다.</li>
<li>비밀번호를 받지 않고 이메일 로그인 링크와 구글·카카오 로그인을 사용해 비밀번호 유출 위험을 없앴습니다.</li>
<li>회원 정보는 본인만 조회할 수 있도록 데이터베이스 접근 권한을 제한합니다.</li>
<li>개인정보에 접근할 수 있는 사람을 운영자로 한정합니다.</li>
</ul>

<h2>10. 개인정보 보호책임자</h2>
<p>개인정보 처리에 관한 문의, 불만, 피해 구제는 아래로 연락해 주세요.</p>
<ul><li>개인정보 보호책임자: {OFFICER}({OPERATOR} 대표)</li><li>이메일: <a href="mailto:{EMAIL}">{EMAIL}</a></li><li>또는 <a href="/contact.html">문의 페이지</a>(문의 유형 "개인정보 관련" 선택)</li></ul>
<p>개인정보 침해에 대한 신고나 상담은 개인정보침해신고센터(국번 없이 118, privacy.kisa.or.kr), 개인정보분쟁조정위원회(1833-6972, www.kopico.go.kr)에도 할 수 있습니다.</p>

<h2>11. 방침의 변경</h2>
<p>이 개인정보처리방침은 {EFFECTIVE}부터 시행합니다. 내용이 바뀌면 시행 7일 전에 이 페이지에 알립니다.</p>
"""

TERMS = f"""
<h1>이용약관</h1>
<p class="lede">시행일: {EFFECTIVE}</p>

<h2>제1조 (목적)</h2>
<p>이 약관은 edu-arena(이하 "사이트")가 제공하는 학습 서비스의 이용 조건과 절차, 이용자와 사이트의 권리·의무를 정합니다.</p>

<h2>제2조 (서비스의 내용)</h2>
<p>사이트는 레슨, 문제, 연습, 에세이 과제, 독학 가이드 등 학습 콘텐츠를 무료로 제공합니다. 학습 콘텐츠는 회원가입 없이 이용할 수 있으며, 회원에게는 학습 기록 보관 등 추가 기능을 제공할 수 있습니다.</p>

<h2>제3조 (회원가입)</h2>
<ol>
<li>회원가입은 만 14세 이상인 사람만 할 수 있습니다.</li>
<li>이용자는 이 약관과 <a href="/privacy.html">개인정보처리방침</a>에 동의하고 이메일 또는 구글·카카오 계정으로 가입합니다.</li>
<li>회원은 언제든지 <a href="/account.html">내 계정</a> 화면에서 탈퇴할 수 있습니다.</li>
</ol>

<h2>제4조 (이용자의 의무)</h2>
<p>이용자는 다음 행위를 해서는 안 됩니다.</p>
<ul>
<li>사이트의 콘텐츠를 사이트의 허락 없이 복제해 판매하거나 다른 곳에 게시하는 행위(개인 학습과 수업 중 인용은 출처를 밝히면 허용합니다)</li>
<li>자동화된 수단으로 콘텐츠를 대량으로 수집하거나 서비스 운영을 방해하는 행위</li>
<li>다른 사람의 정보를 도용해 가입하거나 문의하는 행위</li>
<li>광고를 부정하게 클릭하거나 클릭을 유도하는 행위</li>
</ul>

<h2>제5조 (콘텐츠의 권리)</h2>
<p>사이트가 제작한 설명, 문제, 해설, 그림 등 콘텐츠의 저작권은 사이트에 있습니다.</p>

<h2>제6조 (광고)</h2>
<p>사이트는 운영을 위해 화면에 광고를 게재할 수 있습니다. 광고를 통해 이루어지는 거래는 이용자와 광고주 사이의 일이며, 사이트는 이에 책임을 지지 않습니다.</p>

<h2>제7조 (서비스의 변경과 중단)</h2>
<p>사이트는 콘텐츠를 고치거나 추가·삭제할 수 있으며, 시스템 점검이나 불가피한 사정이 있으면 서비스를 일시적으로 중단할 수 있습니다.</p>

<h2>제8조 (책임의 제한)</h2>
<p>사이트는 콘텐츠의 정확성을 위해 노력하지만, 학습 콘텐츠는 참고용이며 시험 결과나 진학 등을 보장하지 않습니다. 오류를 발견하면 <a href="/contact.html">문의 페이지</a>로 알려 주세요.</p>

<h2>제9조 (약관의 변경)</h2>
<p>약관을 바꿀 때는 시행 7일 전에 이 페이지에 알립니다.</p>

<h2>제10조 (준거법과 관할)</h2>
<p>이 약관은 대한민국 법에 따르며, 분쟁이 생기면 민사소송법에 따른 관할 법원에서 해결합니다.</p>
"""

CONTACT = """
<h1>문의</h1>
<p class="lede">콘텐츠 오류 신고, 학습 관련 질문, 제안, 개인정보 관련 요청을 보내 주세요. 확인 후 적어 주신 이메일로 답변드립니다. 메일로 직접 보내셔도 됩니다: <a href="mailto:contact@edu-arena.org">contact@edu-arena.org</a></p>
<div class="card">
<form id="cf" novalidate>
  <label for="name">이름 또는 별칭</label>
  <input type="text" id="name" name="name" maxlength="40" required autocomplete="name">
  <label for="email">답변받을 이메일</label>
  <input type="email" id="email" name="email" maxlength="120" required autocomplete="email">
  <label for="kind">문의 유형</label>
  <select id="kind" name="kind">
    <option>콘텐츠 오류 신고</option><option>학습 관련 질문</option><option>제안</option><option>회원·로그인</option><option>개인정보 관련</option><option>기타</option>
  </select>
  <label for="where">관련 페이지(선택)</label>
  <input type="text" id="where" name="page" maxlength="300" placeholder="예: 수학 › 미적분 › 극한의 뜻">
  <label for="message">내용</label>
  <textarea id="message" name="message" maxlength="5000" required></textarea>
  <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off">
  <div class="msg note">
    <strong>개인정보 수집·이용 안내</strong><br>
    수집 항목: 이름(별칭), 이메일, 문의 내용 · 목적: 문의 확인과 답변 · 보유 기간: 답변 후 1년<br>
    문의 내용은 전달 서비스(Web3Forms)를 거쳐 운영자 메일로 전달됩니다. 동의하지 않으면 문의를 보낼 수 없습니다.
  </div>
  <label class="check"><input type="checkbox" id="agree" required> <span>위 개인정보 수집·이용에 동의합니다.</span></label>
  <div class="stack"><button class="btn" id="send" type="submit">보내기</button></div>
  <div id="out" class="msg" role="status" hidden></div>
</form>
</div>
<p class="note">자주 묻는 내용: 학습 콘텐츠는 로그인 없이 무료로 이용할 수 있습니다. 로그인하지 않으면 진도는 이 브라우저에만 저장됩니다.</p>
<script>
(function(){
  var f=document.getElementById("cf"), out=document.getElementById("out"), btn=document.getElementById("send");
  function show(t,err){out.hidden=false;out.textContent=t;out.className="msg"+(err?" err":"");}
  f.addEventListener("submit",function(ev){
    ev.preventDefault();
    var key=(window.EA_SITE||{}).WEB3FORMS_KEY;
    if(!key){show("문의 양식이 아직 연결되지 않았습니다. 잠시 후 다시 시도해 주세요.",true);return;}
    var name=f.name.value.trim(), email=f.email.value.trim(), msg=f.message.value.trim();
    if(!name||!email||!msg){show("이름, 이메일, 내용을 모두 적어 주세요.",true);return;}
    if(!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(email)){show("이메일 주소를 확인해 주세요.",true);return;}
    if(!document.getElementById("agree").checked){show("개인정보 수집·이용에 동의해야 보낼 수 있습니다.",true);return;}
    var data={access_key:key,subject:"[edu-arena 문의] "+f.kind.value,from_name:"edu-arena 문의 양식",
      name:name,email:email,"문의 유형":f.kind.value,"관련 페이지":f.page.value.trim(),message:msg,botcheck:f.botcheck.checked};
    btn.disabled=true;show("보내는 중입니다…");
    fetch("https://api.web3forms.com/submit",{method:"POST",headers:{"Content-Type":"application/json",Accept:"application/json"},body:JSON.stringify(data)})
      .then(function(r){return r.json();})
      .then(function(j){ if(j.success){f.reset();show("문의가 접수되었습니다. 확인 후 이메일로 답변드리겠습니다.");} else show("보내지 못했습니다. 잠시 후 다시 시도해 주세요.",true); })
      .catch(function(){show("네트워크 문제로 보내지 못했습니다. 잠시 후 다시 시도해 주세요.",true);})
      .then(function(){btn.disabled=false;});
  });
})();
</script>
"""

SUPA_JS = '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>\n<script src="/assets/site.js"></script>\n'

_SIGNUP_BASE = """
<h1>로그인 · 회원가입</h1>
<p class="lede">처음이면 자동으로 가입됩니다. 학습 콘텐츠는 로그인하지 않아도 모두 이용할 수 있습니다.</p>
<div class="card" id="box">
  <label class="check"><input type="checkbox" id="age"> <span>[필수] 만 14세 이상입니다.</span></label>
  <label class="check"><input type="checkbox" id="terms"> <span>[필수] <a href="/terms.html" target="_blank">이용약관</a>과 <a href="/privacy.html" target="_blank">개인정보처리방침</a>(수집 항목: 이메일, 회원 식별자 · 보유: 탈퇴 시까지)에 동의합니다.</span></label>
  <div class="stack">
    <button class="btn ghost" id="google" disabled>구글 계정으로 계속하기</button>
    <button class="btn kakao" id="kakao" disabled>카카오 계정으로 계속하기</button>
  </div>
  <label for="em">또는 이메일로 로그인 링크 받기</label>
  <input type="email" id="em" autocomplete="email" placeholder="you@example.com">
  <div class="stack"><button class="btn" id="mail" disabled>로그인 링크 보내기</button></div>
  <p class="note">비밀번호는 쓰지 않습니다. 메일로 받은 링크를 누르면 로그인됩니다.</p>
  <div id="out" class="msg" role="status" hidden></div>
</div>
<script>
(function(){
  var S=window.EA_SITE||{}, out=document.getElementById("out");
  function show(t,err){out.hidden=false;out.textContent=t;out.className="msg"+(err?" err":"");}
  if(!S.SUPABASE_URL||!S.SUPABASE_ANON_KEY||!window.supabase){show("로그인 기능이 아직 연결되지 않았습니다.",true);return;}
  var sb=window.supabase.createClient(S.SUPABASE_URL,S.SUPABASE_ANON_KEY);
  var age=document.getElementById("age"), terms=document.getElementById("terms");
  var btns=["google","kakao","mail"].map(function(id){return document.getElementById(id);});
  var P=S.AUTH_PROVIDERS||["email"];
  if(P.indexOf("google")<0) btns[0].hidden=true;
  if(P.indexOf("kakao")<0) btns[1].hidden=true;
  function sync(){var ok=age.checked&&terms.checked;btns.forEach(function(b){b.disabled=!ok;});}
  age.addEventListener("change",sync);terms.addEventListener("change",sync);
  function remember(){try{localStorage.setItem("ea-consent",JSON.stringify({age14:true,at:new Date().toISOString()}));}catch(e){}}
  var back=location.origin+"/account.html";
  sb.auth.getSession().then(function(r){ if(r.data&&r.data.session) location.replace("/account.html"); });
  function oauth(p){ remember(); sb.auth.signInWithOAuth({provider:p,options:{redirectTo:back}}).then(function(r){ if(r.error) show("로그인을 시작하지 못했습니다: "+r.error.message,true); }); }
  btns[0].addEventListener("click",function(){oauth("google");});
  btns[1].addEventListener("click",function(){oauth("kakao");});
  btns[2].addEventListener("click",function(){
    var em=document.getElementById("em").value.trim();
    if(!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(em)){show("이메일 주소를 확인해 주세요.",true);return;}
    remember(); btns[2].disabled=true;
    sb.auth.signInWithOtp({email:em,options:{emailRedirectTo:back}}).then(function(r){
      if(r.error){show("메일을 보내지 못했습니다: "+r.error.message,true);btns[2].disabled=false;}
      else show(em+"로 로그인 링크를 보냈습니다. 메일함을 확인해 주세요. 메일이 보이지 않으면 스팸함도 확인해 주세요.");
    });
  });
})();
</script>
"""

ACCOUNT = """
<h1>내 계정</h1>
<div id="out" class="msg" role="status">계정 정보를 불러오는 중입니다…</div>
<div class="card" id="consent" hidden>
  <p>처음 가입하셨습니다. 이용을 계속하려면 아래 항목에 동의해 주세요.</p>
  <label class="check"><input type="checkbox" id="age"> <span>[필수] 만 14세 이상입니다.</span></label>
  <label class="check"><input type="checkbox" id="terms"> <span>[필수] <a href="/terms.html" target="_blank">이용약관</a>과 <a href="/privacy.html" target="_blank">개인정보처리방침</a>에 동의합니다.</span></label>
  <div class="stack"><button class="btn" id="agree">동의하고 계속하기</button><button class="btn ghost" id="refuse">동의하지 않음(가입 취소)</button></div>
</div>
<div class="card" id="info" hidden>
  <table>
    <tr><th>이메일</th><td id="email"></td></tr>
    <tr><th>로그인 방식</th><td id="prov"></td></tr>
    <tr><th>가입일</th><td id="since"></td></tr>
  </table>
  <div class="stack"><a class="btn" href="/progress.html">내 학습 진도</a><a class="btn ghost" href="/#subjects">공부하러 가기</a><a class="btn ghost" id="adminlink" href="/admin.html" hidden>관리자 페이지</a><button class="btn ghost" id="logout">로그아웃</button></div>
  <h2>비밀번호</h2>
  <p class="note">비밀번호를 정해 두면 메일 인증 없이 이메일과 비밀번호로 바로 로그인할 수 있습니다.</p>
  <input type="password" id="newpw" autocomplete="new-password" placeholder="새 비밀번호(8자 이상)">
  <div class="stack"><button class="btn ghost" id="setpw">비밀번호 설정·변경</button></div>
  <h2>회원 탈퇴</h2>
  <p class="note">탈퇴하면 계정 정보와 동의 기록이 즉시 삭제되며 되돌릴 수 없습니다. 계정에 저장된 학습 진도도 함께 삭제되며, 이 브라우저에 저장된 진도는 그대로 남습니다.</p>
  <div class="stack"><button class="btn danger" id="del1">회원 탈퇴</button><button class="btn danger" id="del2" hidden>정말 탈퇴합니다</button></div>
</div>
<script>
(function(){
  var S=window.EA_SITE||{}, out=document.getElementById("out");
  function show(t,err){out.hidden=false;out.textContent=t;out.className="msg"+(err?" err":"");}
  if(!S.SUPABASE_URL||!S.SUPABASE_ANON_KEY||!window.supabase){show("로그인 기능이 아직 연결되지 않았습니다.",true);return;}
  var sb=window.supabase.createClient(S.SUPABASE_URL,S.SUPABASE_ANON_KEY);
  var PROV={email:"이메일 링크",google:"구글",kakao:"카카오"};
  var user=null;
  function pending(){try{return JSON.parse(localStorage.getItem("ea-consent"));}catch(e){return null;}}
  function saveConsent(at){
    return sb.from("profiles").upsert({id:user.id,age14_confirmed:true,agreed_at:at||new Date().toISOString()}).then(function(r){
      if(r.error) throw r.error; try{localStorage.removeItem("ea-consent");}catch(e){} });
  }
  function render(){
    out.hidden=true; document.getElementById("consent").hidden=true; document.getElementById("info").hidden=false;
    document.getElementById("email").textContent=user.email||"(제공되지 않음)";
    var p=(user.app_metadata&&user.app_metadata.provider)||"email";
    document.getElementById("prov").textContent=PROV[p]||p;
    document.getElementById("since").textContent=new Date(user.created_at).toLocaleDateString("ko-KR");
    sb.rpc("is_admin").then(function(a){ if(a.data===true) document.getElementById("adminlink").hidden=false; });
    if(window.EA_SYNC) window.EA_SYNC();
  }
  function start(session){
    if(!session){location.replace("/login.html");return;}
    user=session.user;
    sb.from("profiles").select("age14_confirmed").eq("id",user.id).maybeSingle().then(function(r){
      if(r.error){show("계정 정보를 불러오지 못했습니다: "+r.error.message,true);return;}
      if(r.data&&r.data.age14_confirmed){render();return;}
      var c=pending();
      if(c&&c.age14){saveConsent(c.at).then(render).catch(function(e){show("동의 기록을 저장하지 못했습니다: "+e.message,true);});return;}
      out.hidden=true; document.getElementById("consent").hidden=false;
    });
  }
  sb.auth.getSession().then(function(r){start(r.data&&r.data.session);});
  document.getElementById("agree").addEventListener("click",function(){
    if(!document.getElementById("age").checked||!document.getElementById("terms").checked){show("두 항목에 모두 동의해야 가입할 수 있습니다.",true);return;}
    saveConsent().then(render).catch(function(e){show("동의 기록을 저장하지 못했습니다: "+e.message,true);});
  });
  function removeAccount(){
    return sb.rpc("delete_my_account").then(function(r){ if(r.error) throw r.error; return sb.auth.signOut(); });
  }
  document.getElementById("refuse").addEventListener("click",function(){
    removeAccount().then(function(){location.replace("/");}).catch(function(e){show("가입 취소에 실패했습니다: "+e.message,true);});
  });
  document.getElementById("setpw").addEventListener("click",function(){
    var v=document.getElementById("newpw").value;
    if(v.length<8){show("비밀번호는 8자 이상이어야 합니다.",true);return;}
    sb.auth.updateUser({password:v}).then(function(r){ if(r.error) show("변경하지 못했습니다: "+r.error.message,true); else {show("비밀번호를 저장했습니다.");document.getElementById("newpw").value="";} });
  });
  document.getElementById("logout").addEventListener("click",function(){ sb.auth.signOut().then(function(){location.replace("/");}); });
  document.getElementById("del1").addEventListener("click",function(){ this.hidden=true; document.getElementById("del2").hidden=false; });
  document.getElementById("del2").addEventListener("click",function(){
    removeAccount().then(function(){ try{localStorage.removeItem("ea-consent");}catch(e){} show("탈퇴가 완료되었습니다. 이용해 주셔서 감사합니다."); document.getElementById("info").hidden=true; })
      .catch(function(e){show("탈퇴하지 못했습니다: "+e.message+" 문의 페이지로 알려 주시면 처리해 드립니다.",true);});
  });
})();
</script>
"""

SIGNUP = """
<h1>회원가입</h1>
<p class="lede">가입하면 수업 진도가 계정에 저장되어 다른 기기에서도 이어서 볼 수 있습니다. 학습 콘텐츠는 가입하지 않아도 모두 이용할 수 있습니다. 이미 회원이면 <a href="/login.html">로그인</a>하세요.</p>
<div class="card" id="box">
  <label class="check"><input type="checkbox" id="age"> <span>[필수] 만 14세 이상입니다.</span></label>
  <label class="check"><input type="checkbox" id="terms"> <span>[필수] <a href="/terms.html" target="_blank">이용약관</a>과 <a href="/privacy.html" target="_blank">개인정보처리방침</a>(수집 항목: 이메일, 비밀번호(암호화 저장), 회원 식별자, 학습 진도 · 보유: 탈퇴 시까지)에 동의합니다.</span></label>
  <label for="em">이메일</label>
  <input type="email" id="em" autocomplete="email" placeholder="you@example.com">
  <label for="pw">비밀번호 (8자 이상)</label>
  <input type="password" id="pw" autocomplete="new-password">
  <label for="pw2">비밀번호 확인</label>
  <input type="password" id="pw2" autocomplete="new-password">
  <div class="stack"><button class="btn" id="join" disabled>가입하기</button></div>
  <div class="stack">
    <button class="btn ghost" id="google" disabled>구글 계정으로 가입하기</button>
    <button class="btn kakao" id="kakao" disabled>카카오 계정으로 가입하기</button>
  </div>
  <div id="out" class="msg" role="status" hidden></div>
  <p class="note">이미 회원이신가요? <a href="/login.html">로그인</a></p>
</div>
<script>
(function(){
  var S=window.EA_SITE||{}, out=document.getElementById("out");
  function show(t,err){out.hidden=false;out.textContent=t;out.className="msg"+(err?" err":"");}
  if(!S.SUPABASE_URL||!S.SUPABASE_ANON_KEY||!window.supabase){show("로그인 기능이 아직 연결되지 않았습니다.",true);return;}
  var sb=window.supabase.createClient(S.SUPABASE_URL,S.SUPABASE_ANON_KEY);
  var age=document.getElementById("age"), terms=document.getElementById("terms");
  var join=document.getElementById("join"), g=document.getElementById("google"), k=document.getElementById("kakao");
  var P=S.AUTH_PROVIDERS||["email"];
  if(P.indexOf("google")<0) g.hidden=true;
  if(P.indexOf("kakao")<0) k.hidden=true;
  function sync(){var ok=age.checked&&terms.checked;join.disabled=!ok;g.disabled=!ok;k.disabled=!ok;}
  age.addEventListener("change",sync);terms.addEventListener("change",sync);
  function remember(){try{localStorage.setItem("ea-consent",JSON.stringify({age14:true,at:new Date().toISOString()}));}catch(e){}}
  var back=location.origin+"/account.html";
  sb.auth.getSession().then(function(r){ if(r.data&&r.data.session) location.replace("/account.html"); });
  function oauth(p){ remember(); sb.auth.signInWithOAuth({provider:p,options:{redirectTo:back}}).then(function(r){ if(r.error) show("가입을 시작하지 못했습니다: "+r.error.message,true); }); }
  g.addEventListener("click",function(){oauth("google");});
  k.addEventListener("click",function(){oauth("kakao");});
  join.addEventListener("click",function(){
    var em=document.getElementById("em").value.trim(), pw=document.getElementById("pw").value, pw2=document.getElementById("pw2").value;
    if(!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(em)){show("이메일 주소를 확인해 주세요.",true);return;}
    if(pw.length<8){show("비밀번호는 8자 이상이어야 합니다.",true);return;}
    if(pw!==pw2){show("비밀번호 확인이 일치하지 않습니다.",true);return;}
    remember(); join.disabled=true;
    sb.auth.signUp({email:em,password:pw,options:{emailRedirectTo:back}}).then(function(r){
      if(r.error){show(/registered|already/i.test(r.error.message)?"이미 가입된 이메일입니다. 로그인해 주세요.":"가입하지 못했습니다: "+r.error.message,true);join.disabled=false;return;}
      if(r.data&&r.data.user&&r.data.user.identities&&r.data.user.identities.length===0){show("이미 가입된 이메일입니다. 로그인해 주세요.",true);join.disabled=false;return;}
      if(r.data&&r.data.session){location.replace("/account.html");return;}
      show(em+"로 확인 메일을 보냈습니다. 메일의 링크를 한 번 눌러 가입을 마쳐 주세요. 이후에는 인증 없이 이메일과 비밀번호로 바로 로그인합니다.");
    });
  });
})();
</script>
"""

LOGIN = """
<h1>로그인</h1>
<p class="lede">학습 콘텐츠는 로그인하지 않아도 모두 이용할 수 있습니다. 로그인하면 수업 진도가 계정에 저장됩니다.</p>
<div class="card" id="box">
  <label for="em">이메일</label>
  <input type="email" id="em" autocomplete="email" placeholder="you@example.com">
  <label for="pw">비밀번호</label>
  <input type="password" id="pw" autocomplete="current-password">
  <div class="stack">
    <button class="btn" id="login">로그인</button>
    <a class="btn ghost" href="/signup.html">회원가입</a>
  </div>
  <div class="stack">
    <button class="btn ghost" id="google">구글 계정으로 로그인</button>
    <button class="btn kakao" id="kakao">카카오 계정으로 로그인</button>
  </div>
  <div id="out" class="msg" role="status" hidden></div>
  <p class="note"><a href="#" id="forgot">비밀번호를 잊으셨나요?</a> · <a href="#" id="link">비밀번호 없이 메일 링크로 로그인</a></p>
</div>
<script>
(function(){
  var S=window.EA_SITE||{}, out=document.getElementById("out");
  function show(t,err){out.hidden=false;out.textContent=t;out.className="msg"+(err?" err":"");}
  if(!S.SUPABASE_URL||!S.SUPABASE_ANON_KEY||!window.supabase){show("로그인 기능이 아직 연결되지 않았습니다.",true);return;}
  var sb=window.supabase.createClient(S.SUPABASE_URL,S.SUPABASE_ANON_KEY);
  var P=S.AUTH_PROVIDERS||["email"];
  var g=document.getElementById("google"), k=document.getElementById("kakao"), b=document.getElementById("login");
  if(P.indexOf("google")<0) g.hidden=true;
  if(P.indexOf("kakao")<0) k.hidden=true;
  var back=location.origin+"/progress.html";
  function email(){var em=document.getElementById("em").value.trim();if(!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(em)){show("이메일 주소를 확인해 주세요.",true);return null;}return em;}
  sb.auth.getSession().then(function(r){ if(r.data&&r.data.session) location.replace("/progress.html"); });
  function oauth(p){ sb.auth.signInWithOAuth({provider:p,options:{redirectTo:back}}).then(function(r){ if(r.error) show("로그인을 시작하지 못했습니다: "+r.error.message,true); }); }
  g.addEventListener("click",function(){oauth("google");});
  k.addEventListener("click",function(){oauth("kakao");});
  function go(){
    var em=email(); if(!em) return;
    var pw=document.getElementById("pw").value; if(!pw){show("비밀번호를 입력해 주세요.",true);return;}
    b.disabled=true;
    sb.auth.signInWithPassword({email:em,password:pw}).then(function(r){
      b.disabled=false;
      if(r.error){show(/not confirmed/i.test(r.error.message)?"가입 확인 메일의 링크를 아직 누르지 않았습니다. 메일함을 확인해 주세요.":"이메일 또는 비밀번호가 맞지 않습니다. 처음이면 회원가입을, 비밀번호를 모르면 '비밀번호를 잊으셨나요?'를 눌러 주세요.",true);return;}
      location.replace("/progress.html");
    });
  }
  b.addEventListener("click",go);
  document.getElementById("pw").addEventListener("keydown",function(e){if(e.key==="Enter")go();});
  document.getElementById("forgot").addEventListener("click",function(e){
    e.preventDefault(); var em=email(); if(!em) return;
    sb.auth.resetPasswordForEmail(em,{redirectTo:location.origin+"/account.html"}).then(function(r){
      show(r.error?"메일을 보내지 못했습니다: "+r.error.message:em+"로 안내 메일을 보냈습니다. 메일의 링크를 누르면 내 계정 화면에서 새 비밀번호를 정할 수 있습니다.",!!r.error);
    });
  });
  document.getElementById("link").addEventListener("click",function(e){
    e.preventDefault(); var em=email(); if(!em) return;
    sb.auth.signInWithOtp({email:em,options:{emailRedirectTo:back,shouldCreateUser:false}}).then(function(r){
      if(r.error){show(/signup|not allowed|not found/i.test(r.error.message||"")?"가입되지 않은 이메일입니다. 먼저 회원가입을 해 주세요.":"메일을 보내지 못했습니다: "+r.error.message,true);}
      else show(em+"로 로그인 링크를 보냈습니다. 메일함을 확인해 주세요.");
    });
  });
})();
</script>
"""

PROGRESS = """
<h1>내 학습</h1>
<p class="lede">로그인한 기기와 상관없이 완료한 레슨과 에세이를 모아 보여 줍니다.</p>
<div id="out" class="msg" role="status">진도를 불러오는 중입니다…</div>
<div id="body" hidden>
  <div class="card"><div id="total"></div></div>
  <h2>과목별 진도</h2>
  <table id="subj"><tr><th>과목</th><th>완료 레슨</th><th>완료 에세이</th><th>첫 시도 정답률</th><th>마지막 학습</th></tr></table>
  <h2>최근 학습</h2>
  <table id="recent"><tr><th>날짜</th><th>과목</th><th>내용</th><th>결과</th></tr></table>
  <div class="stack"><a class="btn" href="/lessons.html">이어서 공부하기</a><a class="btn ghost" href="/account.html">내 계정</a><a class="btn ghost" id="adminlink" href="/admin.html" hidden>관리자</a></div>
</div>
<script>
(function(){
  var S=window.EA_SITE||{}, out=document.getElementById("out");
  function show(t,err){out.hidden=false;out.textContent=t;out.className="msg"+(err?" err":"");}
  if(!S.SUPABASE_URL||!S.SUPABASE_ANON_KEY||!window.supabase){show("로그인 기능이 아직 연결되지 않았습니다.",true);return;}
  var sb=window.supabase.createClient(S.SUPABASE_URL,S.SUPABASE_ANON_KEY);
  var MAP={"socio-arena":["사회·역사","socio"],"biz-arena":["경제·경영","biz"],"lit-arena":["언어·문학·외국어","lit"],"math-arena":["수학","math"],
    "sci-arena":["과학","sci"],"tech-arena":["공학","tech"],"arts":["예체능","arts"],"code-arena":["코딩","code"],"test-arena":["시험 대비",""]};
  function esc(t){var d=document.createElement("div");d.textContent=String(t==null?"":t);return d.innerHTML;}
  function dt(ms){return ms?new Date(ms).toLocaleDateString("ko-KR"):"-";}
  function stores(){var o={};for(var i=0;i<localStorage.length;i++){var k=localStorage.key(i);if(/:progress$/.test(k)){try{o[k.replace(/:progress$/,"")]=JSON.parse(localStorage.getItem(k))||{};}catch(e){}}}return o;}
  function render(){
    var all=stores(), rows="", recent=[], nl=0, ne=0;
    Object.keys(MAP).forEach(function(key){
      var st=all[key]; if(!st) return;
      var L=0,E=0,f=0,t=0,last=0;
      Object.keys(st).forEach(function(id){
        var r=st[id]; if(!r||typeof r!=="object") return;
        var ess=/-essay$/.test(id);
        if(ess) E++; else {L++; f+=r.first||0; t+=r.total||0;}
        last=Math.max(last,r.at||0);
        recent.push({key:key,id:id,r:r,ess:ess});
      });
      nl+=L; ne+=E;
      var lk=MAP[key][1]?'<a href="/'+MAP[key][1]+'/browse.html">'+esc(MAP[key][0])+'</a>':esc(MAP[key][0]);
      rows+="<tr><td>"+lk+"</td><td>"+L+"</td><td>"+E+"</td><td>"+(t?Math.round(f/t*100)+"%":"-")+"</td><td>"+dt(last)+"</td></tr>";
    });
    document.getElementById("total").innerHTML="완료한 레슨 <strong>"+nl+"</strong>개 · 완료한 에세이 <strong>"+ne+"</strong>편";
    var tb=document.getElementById("subj");
    tb.insertAdjacentHTML("beforeend",rows||'<tr><td colspan="5">아직 완료한 레슨이 없습니다. 레슨 하나를 끝내면 여기에 나타납니다.</td></tr>');
    recent.sort(function(a,b){return (b.r.at||0)-(a.r.at||0);});
    recent=recent.slice(0,15);
    var rt=document.getElementById("recent");
    recent.forEach(function(x){
      var tr=document.createElement("tr"), dir=MAP[x.key][1], base=x.id.replace(/-essay$/,"");
      tr.innerHTML="<td>"+dt(x.r.at)+"</td><td>"+esc(MAP[x.key][0])+"</td><td data-id=\\""+esc(base)+"\\">"+(x.ess?"에세이 · ":"")+esc(x.id)+"</td><td>"+(x.ess?(x.r.first||0)+"/"+(x.r.total||0)+"편":(x.r.first||0)+" / "+(x.r.total||0))+"</td>";
      rt.appendChild(tr);
      if(dir&&!/review/.test(x.id)) fetch("/"+dir+"/learn/"+base+".html").then(function(r){return r.ok?r.text():null;}).then(function(h){
        var m=h&&h.match(/<title>([^<]*)<\\/title>/); if(!m) return;
        var name=m[1].split(" | ")[0].trim();
        var td=tr.children[2]; td.innerHTML=(x.ess?"에세이 · ":"")+'<a href="/'+dir+'/learn/'+esc(base)+'.html">'+esc(name)+"</a>";
      }).catch(function(){});
    });
    out.hidden=true; document.getElementById("body").hidden=false;
  }
  sb.auth.getSession().then(function(r){
    if(!(r.data&&r.data.session)){location.replace("/login.html");return;}
    var user=r.data.session.user;
    sb.from("profiles").select("age14_confirmed").eq("id",user.id).maybeSingle().then(function(p){
      if(!(p.data&&p.data.age14_confirmed)){location.replace("/account.html");return;}
      Promise.resolve(window.EA_SYNC&&window.EA_SYNC()).then(render,render);
      sb.rpc("is_admin").then(function(a){ if(a.data===true) document.getElementById("adminlink").hidden=false; });
    });
  });
})();
</script>
"""

ADMIN = """
<h1>관리자</h1>
<div id="out" class="msg" role="status">확인하는 중입니다…</div>
<div id="body" hidden>
  <div class="card" id="cards"></div>
  <h2>최근 14일 가입</h2>
  <div id="daily" class="note"></div>
  <h2>가입 방식 · 과목별 학습 기록</h2>
  <table id="split"><tr><th>구분</th><th>항목</th><th>수</th></tr></table>
  <h2>회원 목록</h2>
  <p class="note">최근 가입순 200명까지 표시합니다. 이메일 등 개인정보는 회원 관리 목적으로만 확인하세요.</p>
  <table id="mem"><tr><th>이메일</th><th>방식</th><th>가입일</th><th>최근 로그인</th><th>동의</th><th>완료</th><th>진도</th></tr></table>
  <div id="detail" class="msg" hidden></div>
</div>
<script>
(function(){
  var S=window.EA_SITE||{}, out=document.getElementById("out");
  function show(t,err){out.hidden=false;out.textContent=t;out.className="msg"+(err?" err":"");}
  if(!S.SUPABASE_URL||!S.SUPABASE_ANON_KEY||!window.supabase){show("로그인 기능이 아직 연결되지 않았습니다.",true);return;}
  var sb=window.supabase.createClient(S.SUPABASE_URL,S.SUPABASE_ANON_KEY);
  function esc(t){var d=document.createElement("div");d.textContent=String(t==null?"":t);return d.innerHTML;}
  function d(x){return x?new Date(x).toLocaleDateString("ko-KR"):"-";}
  var PROV={email:"이메일",google:"구글",kakao:"카카오"};
  sb.auth.getSession().then(function(r){
    if(!(r.data&&r.data.session)){location.replace("/login.html");return;}
    sb.rpc("is_admin").then(function(a){
      if(a.data!==true){show("관리자만 볼 수 있는 페이지입니다.",true);return;}
      Promise.all([sb.rpc("admin_overview"),sb.rpc("admin_members",{p_limit:200,p_offset:0})]).then(function(x){
        if(x[0].error||x[1].error){show("불러오지 못했습니다: "+(x[0].error||x[1].error).message,true);return;}
        var o=x[0].data, m=x[1].data||[];
        function c(n,l){return '<div style="display:inline-block;min-width:120px;margin:6px 16px 6px 0"><div style="font-size:26px;font-weight:700">'+n+'</div><div class="note">'+l+'</div></div>';}
        document.getElementById("cards").innerHTML=c(o.members,"전체 회원")+c(o.new_7d,"최근 7일 가입")+c(o.new_30d,"최근 30일 가입")+c(o.learners,"학습 기록이 있는 회원")+c(o.active_7d,"최근 7일 학습 회원")+c(o.records,"저장된 학습 기록");
        var max=Math.max.apply(null,o.daily.map(function(z){return z.n;}).concat([1]));
        document.getElementById("daily").innerHTML=o.daily.map(function(z){return '<div style="display:flex;align-items:center;gap:8px"><span style="width:84px">'+esc(z.d.slice(5))+'</span><span style="display:inline-block;height:10px;background:#1D3FA8;width:'+Math.round(z.n/max*240)+'px"></span><span>'+z.n+'</span></div>';}).join("");
        var sp=document.getElementById("split"), h="";
        Object.keys(o.providers).forEach(function(k){h+="<tr><td>가입 방식</td><td>"+esc(PROV[k]||k)+"</td><td>"+o.providers[k]+"</td></tr>";});
        Object.keys(o.stores).forEach(function(k){h+="<tr><td>학습 기록</td><td>"+esc(k.replace(/:progress$/,""))+"</td><td>"+o.stores[k]+"</td></tr>";});
        sp.insertAdjacentHTML("beforeend",h);
        var mt=document.getElementById("mem");
        m.forEach(function(u){
          var tr=document.createElement("tr");
          tr.innerHTML="<td>"+esc(u.email||"(없음)")+"</td><td>"+esc(PROV[u.provider]||u.provider)+"</td><td>"+d(u.created_at)+"</td><td>"+d(u.last_sign_in_at)+"</td><td>"+(u.age14?"완료":"미동의")+"</td><td>"+u.done_count+"</td><td><button class=\\"btn ghost\\" style=\\"min-height:32px;padding:4px 10px\\">보기</button></td>";
          tr.querySelector("button").addEventListener("click",function(){
            sb.rpc("admin_member_progress",{p_user:u.id}).then(function(q){
              var de=document.getElementById("detail"); de.hidden=false;
              de.textContent=(u.email||"")+" — "+((q.data||[]).map(function(z){return z.store.replace(/:progress$/,"")+" "+z.done+"건(마지막 "+d(z.last_at)+")";}).join(", ")||"학습 기록 없음");
            });
          });
          mt.appendChild(tr);
        });
        out.hidden=true; document.getElementById("body").hidden=false;
      });
    });
  });
})();
</script>
"""

if __name__ == "__main__":
    page("about.html", "소개", "edu-arena는 읽기 전에 먼저 풀어 보는 15분 레슨으로 고교 교과부터 대학 수준, 올림피아드 심화까지 공부하는 무료 학습 사이트입니다.", ABOUT)
    page("privacy.html", "개인정보처리방침", "edu-arena의 개인정보 수집 항목, 이용 목적, 보유 기간, 쿠키와 광고, 이용자의 권리를 안내합니다.", PRIVACY)
    page("terms.html", "이용약관", "edu-arena 학습 서비스의 이용 조건과 회원가입, 이용자의 의무를 안내합니다.", TERMS)
    page("contact.html", "문의", "edu-arena에 콘텐츠 오류 신고, 학습 질문, 제안, 개인정보 관련 요청을 보내는 문의 양식입니다.", CONTACT)
    page("login.html", "로그인", "edu-arena 로그인.", LOGIN, extra_head=SUPA_JS, noindex=True)
    page("signup.html", "회원가입", "edu-arena 회원가입.", SIGNUP, extra_head=SUPA_JS, noindex=True)
    page("progress.html", "내 학습", "edu-arena 내 학습 진도.", PROGRESS, extra_head=SUPA_JS, noindex=True)
    page("admin.html", "관리자", "edu-arena 관리자.", ADMIN, extra_head=SUPA_JS, noindex=True)
    page("account.html", "내 계정", "edu-arena 내 계정.", ACCOUNT, extra_head=SUPA_JS, noindex=True)
