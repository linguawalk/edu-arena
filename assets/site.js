/* edu-arena 공통 스크립트: 사이트 설정, 방문자 기록(GA4), 광고(AdSense), 하단 링크, 로그인 상태 표시
   ─────────────────────────────────────────────────────────────
   아래 SITE 값만 채우면 기능이 켜집니다. 비어 있으면 해당 기능은 조용히 꺼져 있습니다.
   (모두 브라우저에 공개되어도 되는 값입니다. 비밀 키는 넣지 마세요.) */
window.EA_SITE = window.EA_SITE || {
  GA_ID: "",               // 구글 애널리틱스 4 측정 ID, 예: "G-XXXXXXXXXX"
  ADSENSE_CLIENT: "",      // 애드센스 게시자 ID, 예: "ca-pub-1234567890123456"
  SUPABASE_URL: "",        // 예: "https://abcdefgh.supabase.co"
  SUPABASE_ANON_KEY: "",   // Supabase 프로젝트의 anon(public) 키
  WEB3FORMS_KEY: ""        // Web3Forms 액세스 키(문의 양식 전달용)
};

(function () {
  var S = window.EA_SITE;
  var path = location.pathname;
  var immersive = /(player|practice-player|placement|play|lesson|task|checkpoint)\.html$/.test(path) && !/\/learn\//.test(path);

  /* ---------- 방문자 기록: Google Analytics 4 ---------- */
  if (S.GA_ID && !window.gtag) {
    var g = document.createElement("script");
    g.async = true;
    g.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(S.GA_ID);
    document.head.appendChild(g);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", S.GA_ID);
  }

  /* ---------- 광고: Google AdSense 자동 광고 ---------- */
  if (S.ADSENSE_CLIENT && !document.querySelector('script[src*="adsbygoogle.js"]')) {
    var a = document.createElement("script");
    a.async = true;
    a.crossOrigin = "anonymous";
    a.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + encodeURIComponent(S.ADSENSE_CLIENT);
    document.head.appendChild(a);
  }

  /* ---------- 로그인 여부(라이브러리를 불러오지 않고 저장된 세션만 확인) ---------- */
  function signedIn() {
    if (!S.SUPABASE_URL) return false;
    try {
      var ref = S.SUPABASE_URL.replace(/^https?:\/\//, "").split(".")[0];
      var raw = localStorage.getItem("sb-" + ref + "-auth-token");
      if (!raw) return false;
      var t = JSON.parse(raw);
      return !!(t && (t.access_token || (t.currentSession && t.currentSession.access_token)));
    } catch (e) { return false; }
  }
  window.EA_SIGNED_IN = signedIn;

  function authLink() {
    var a = document.createElement("a");
    a.className = "ea-auth";
    if (signedIn()) { a.href = "/account.html"; a.textContent = "내 계정"; }
    else { a.href = "/login.html"; a.textContent = "로그인"; }
    return a;
  }

  /* ---------- 공통 하단 ---------- */
  var FOOT_CSS =
    ".ea-foot{border-top:1px solid #DCE4F0;margin-top:48px;background:#FAFBFD;color:#4A5670;font:400 14px/1.6 'IBM Plex Sans KR','Apple SD Gothic Neo','Malgun Gothic',sans-serif}" +
    ".ea-foot .ea-fin{max-width:1040px;margin:0 auto;padding:24px 20px 32px;display:flex;flex-wrap:wrap;gap:8px 20px;align-items:center}" +
    ".ea-foot a{color:#172033;text-decoration:none}.ea-foot a:hover{text-decoration:underline}" +
    ".ea-foot .ea-copy{margin-left:auto;color:#4A5670}" +
    ".ea-auth{margin-left:12px}";

  function addFooter() {
    if (document.querySelector(".ea-foot")) return;
    var st = document.createElement("style"); st.textContent = FOOT_CSS; document.head.appendChild(st);
    var f = document.createElement("footer");
    f.className = "ea-foot";
    f.innerHTML = '<div class="ea-fin">' +
      '<a href="/about.html">소개</a><a href="/lessons.html">전체 레슨 목록</a><a href="/contact.html">문의</a>' +
      '<a href="/terms.html">이용약관</a><a href="/privacy.html"><strong>개인정보처리방침</strong></a>' +
      '<span class="ea-copy">© ' + new Date().getFullYear() + ' edu-arena</span></div>';
    document.body.appendChild(f);
  }

  function addAuthToBars() {
    // 과목 화면의 공통 상단 바(family-bar.js)
    var bar = document.querySelector(".ea-bar .ea-in");
    if (bar && !bar.querySelector(".ea-auth")) {
      var l = authLink(); l.style.color = "#fff"; l.style.fontWeight = "500"; bar.appendChild(l);
    }
    // 과목 화면의 머리글(.ea-head), 메인·안내 화면의 머리글 nav
    var nav = document.querySelector(".ea-head .ea-links") || document.querySelector("header nav[data-auth]");
    if (nav && !nav.querySelector(".ea-auth")) nav.appendChild(authLink());
  }

  function ready() {
    if (!immersive) addFooter();
    if (S.SUPABASE_URL) addAuthToBars();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", function () { setTimeout(ready, 0); });
  else setTimeout(ready, 0);
})();
