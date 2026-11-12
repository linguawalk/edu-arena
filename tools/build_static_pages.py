"""edu-arena 안내 페이지 생성: 소개, 개인정보처리방침, 이용약관, 문의, 로그인, 내 계정.

    python3 tools/build_static_pages.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_parts import FOOT_CSS, FOOT_HTML, SITE_JS, SITE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EFFECTIVE = "2026년 11월 13일"
OFFICER = "edu-arena 운영자"   # 개인정보 보호책임자 표기(성명으로 바꿔 쓰는 것을 권장)

CSS = """
:root{--paper:#FAFBFD;--ink:#172033;--ink-soft:#4A5670;--grid:#DCE4F0;--blue:#1D3FA8;--blue-soft:#E7ECFA;--warn:#8A1C1C;
  --font:"IBM Plex Sans KR","Apple SD Gothic Neo","Malgun Gothic",sans-serif}
*{box-sizing:border-box}
html,body{margin:0;word-break:keep-all;overflow-wrap:anywhere;background:var(--paper);color:var(--ink);font-family:var(--font)}
:focus-visible{outline:3px solid var(--blue);outline-offset:3px}
.wrap{max-width:820px;margin:0 auto;padding:0 20px}
header{border-bottom:1px solid var(--grid);background:#fff}
header .hin{max-width:1040px;margin:0 auto;padding:0 20px;display:flex;align-items:center;justify-content:space-between;height:60px}
.logo{font-weight:700;font-size:20px;color:var(--ink);text-decoration:none}
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
input[type=text],input[type=email],select,textarea{width:100%;font:inherit;padding:10px 12px;border:1px solid #B9C7DD;border-radius:8px;background:#fff;color:var(--ink)}
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
{robots}<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · edu-arena</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{slug}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<style>{CSS}{FOOT_CSS}</style>
{extra_head}</head>
<body>
<header><div class="hin"><a class="logo" href="/">edu-arena</a><nav data-auth><a href="/#subjects">과목</a><a href="/lessons.html">레슨 목록</a></nav></div></header>
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
<p>인문사회(사회와 역사, 경제와 경영, 언어와 문학, 외국어), 수학·과학(수학, 과학, 공학, 코딩), 예체능의 9개 과목, 68개 코스를 한곳에 모았습니다. 모든 레슨은 edu-arena가 직접 쓴 설명과 문제로 이루어져 있습니다.</p>

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
<p>edu-arena는 개인 운영자가 기획하고 제작하는 사이트입니다. 콘텐츠의 오류를 발견하셨거나 제안이 있으시면 <a href="/contact.html">문의 페이지</a>로 알려 주세요. 확인 후 고치겠습니다.</p>

<h2>관련 사이트</h2>
<p><a href="https://mind-arena.org/">mind-arena</a>: 퍼즐과 보드게임으로 생각하는 힘을 기르는 자매 사이트입니다.</p>
"""

PRIVACY = f"""
<h1>개인정보처리방침</h1>
<p class="lede">edu-arena(이하 "사이트")는 「개인정보 보호법」에 따라 이용자의 개인정보를 보호하고 관련 고충을 원활하게 처리하기 위해 다음과 같이 개인정보처리방침을 둡니다. 시행일: {EFFECTIVE}</p>

<h2>1. 처리하는 개인정보와 목적</h2>
<table>
<tr><th>구분</th><th>항목</th><th>목적</th></tr>
<tr><td>회원가입·로그인(이메일)</td><td>이메일 주소</td><td>회원 식별, 로그인 링크 발송, 계정 관리</td></tr>
<tr><td>회원가입·로그인(구글·카카오)</td><td>이메일 주소, 서비스별 회원 식별자, 닉네임(제공되는 경우)</td><td>회원 식별, 계정 관리</td></tr>
<tr><td>회원 동의 기록</td><td>만 14세 이상 확인 여부, 약관·방침 동의 일시</td><td>가입 요건 확인과 동의 증빙</td></tr>
<tr><td>문의</td><td>이름(또는 별칭), 회신받을 이메일 주소, 문의 내용</td><td>문의 확인과 답변</td></tr>
<tr><td>자동 수집</td><td>접속 기록, 방문 페이지, 기기·브라우저 정보, 쿠키, 대략적인 위치(국가·도시 수준)</td><td>방문 통계 분석, 서비스 개선, 광고 게재</td></tr>
</table>
<p>로그인하지 않고 레슨을 풀 때 생기는 학습 진도와 점수는 이용자의 브라우저(로컬 저장소)에만 저장되며 사이트가 수집하지 않습니다.</p>

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
<ul><li>개인정보 보호책임자: {OFFICER}</li><li>연락 방법: <a href="/contact.html">문의 페이지</a>(문의 유형 "개인정보 관련" 선택)</li></ul>
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
<p class="lede">콘텐츠 오류 신고, 학습 관련 질문, 제안, 개인정보 관련 요청을 보내 주세요. 확인 후 적어 주신 이메일로 답변드립니다.</p>
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

LOGIN = """
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
  <div class="stack"><a class="btn" href="/#subjects">공부하러 가기</a><button class="btn ghost" id="logout">로그아웃</button></div>
  <h2>회원 탈퇴</h2>
  <p class="note">탈퇴하면 계정 정보와 동의 기록이 즉시 삭제되며 되돌릴 수 없습니다. 이 브라우저에 저장된 학습 진도는 그대로 남습니다.</p>
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
  document.getElementById("logout").addEventListener("click",function(){ sb.auth.signOut().then(function(){location.replace("/");}); });
  document.getElementById("del1").addEventListener("click",function(){ this.hidden=true; document.getElementById("del2").hidden=false; });
  document.getElementById("del2").addEventListener("click",function(){
    removeAccount().then(function(){ try{localStorage.removeItem("ea-consent");}catch(e){} show("탈퇴가 완료되었습니다. 이용해 주셔서 감사합니다."); document.getElementById("info").hidden=true; })
      .catch(function(e){show("탈퇴하지 못했습니다: "+e.message+" 문의 페이지로 알려 주시면 처리해 드립니다.",true);});
  });
})();
</script>
"""

if __name__ == "__main__":
    page("about.html", "소개", "edu-arena는 읽기 전에 먼저 풀어 보는 15분 레슨으로 고교 교과부터 대학 수준, 올림피아드 심화까지 공부하는 무료 학습 사이트입니다.", ABOUT)
    page("privacy.html", "개인정보처리방침", "edu-arena의 개인정보 수집 항목, 이용 목적, 보유 기간, 쿠키와 광고, 이용자의 권리를 안내합니다.", PRIVACY)
    page("terms.html", "이용약관", "edu-arena 학습 서비스의 이용 조건과 회원가입, 이용자의 의무를 안내합니다.", TERMS)
    page("contact.html", "문의", "edu-arena에 콘텐츠 오류 신고, 학습 질문, 제안, 개인정보 관련 요청을 보내는 문의 양식입니다.", CONTACT)
    page("login.html", "로그인", "edu-arena 로그인과 회원가입.", LOGIN, extra_head=SUPA_JS, noindex=True)
    page("account.html", "내 계정", "edu-arena 내 계정.", ACCOUNT, extra_head=SUPA_JS, noindex=True)
