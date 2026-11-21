/* edu-arena 공통 스크립트: 사이트 설정, 방문자 기록(GA4), 광고(AdSense), 하단 링크, 로그인 상태 표시
   ─────────────────────────────────────────────────────────────
   아래 SITE 값만 채우면 기능이 켜집니다. 비어 있으면 해당 기능은 조용히 꺼져 있습니다.
   (모두 브라우저에 공개되어도 되는 값입니다. 비밀 키는 넣지 마세요.) */
window.EA_SITE = window.EA_SITE || {
  GA_ID: "",               // 구글 애널리틱스 4 측정 ID, 예: "G-XXXXXXXXXX"
  ADSENSE_CLIENT: "",      // 애드센스 게시자 ID, 예: "ca-pub-1234567890123456"
  SUPABASE_URL: "https://snknxkqardjrtqfprkad.supabase.co",        // 예: "https://abcdefgh.supabase.co"
  SUPABASE_ANON_KEY: "sb_publishable_K_Olqr8l9hWeZl1QAIEhlA_Z-ZhMftP",   // Supabase 프로젝트의 anon(public) 키
  WEB3FORMS_KEY: "",       // Web3Forms 액세스 키(문의 양식 전달용)
  AUTH_PROVIDERS: ["email"] // Supabase에서 켠 로그인 방식만: "email", "google", "kakao"
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

  /* ---------- 로고 표시와 브라우저 탭 아이콘(정적으로 만든 페이지에는 이미 들어 있음) ---------- */
  if (!document.querySelector('link[rel="icon"]')) {
    [["icon", "/favicon.svg", "image/svg+xml"], ["icon", "/favicon.ico"], ["apple-touch-icon", "/apple-touch-icon.png"]].forEach(function (l) {
      var k = document.createElement("link"); k.rel = l[0]; k.href = l[1]; if (l[2]) k.type = l[2]; document.head.appendChild(k);
    });
  }
  var MARK = '<svg class="ea-mark" viewBox="0 0 64 64" width="28" height="28" aria-hidden="true"><rect width="64" height="64" rx="15" fill="#172033"/>' +
    '<path d="M22 16h-7v32h7M42 16h7v32h-7" fill="none" stroke="#fff" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>' +
    '<path d="M24 33l6 6 11-14" fill="none" stroke="#FFD84D" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  function addMarks() {
    var logos = document.querySelectorAll("a.ea-logo, header a.logo");
    if (!logos.length) return;
    if (!document.getElementById("ea-mark-css")) {
      var st = document.createElement("style"); st.id = "ea-mark-css";
      st.textContent = "a.ea-logo,header a.logo{display:inline-flex!important;align-items:center;gap:9px}" +
        "a.ea-logo span,header a.logo span{background:none!important}.ea-mark{flex:none;display:block}";
      document.head.appendChild(st);
    }
    for (var i = 0; i < logos.length; i++) {
      if (!logos[i].querySelector(".ea-mark")) logos[i].insertAdjacentHTML("afterbegin", MARK);
    }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", addMarks); else addMarks();

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
    var w = document.createElement("span");
    w.className = "ea-auth";
    function mk(h, t) { var a = document.createElement("a"); a.href = h; a.textContent = t; a.style.color = "inherit"; a.style.marginLeft = "12px"; return a; }
    if (signedIn()) { w.appendChild(mk("/progress.html", "내 학습")); w.appendChild(mk("/account.html", "내 계정")); }
    else { w.appendChild(mk("/login.html", "로그인")); w.appendChild(mk("/signup.html", "회원가입")); }
    return w;
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
      '<span class="ea-copy">© ' + new Date().getFullYear() + ' edu-arena · 운영 여행일기 · 사업자등록번호 720-97-01549 · contact@edu-arena.org</span></div>';
    document.body.appendChild(f);
  }


  /* ---------- 학습 진도 동기화: 로그인한 회원의 *:progress 기록을 계정과 맞춘다 ---------- */
  var syncing = null;
  function loadLib() {
    return new Promise(function (res, rej) {
      if (window.supabase) return res();
      var s = document.createElement("script");
      s.src = "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2";
      s.onload = function () { res(); }; s.onerror = function () { rej(new Error("lib")); };
      document.head.appendChild(s);
    });
  }
  function localStores() {
    var out = {};
    try {
      for (var i = 0; i < localStorage.length; i++) {
        var k = localStorage.key(i);
        if (/:progress$/.test(k)) { try { out[k] = JSON.parse(localStorage.getItem(k)) || {}; } catch (e) { out[k] = {}; } }
      }
    } catch (e) {}
    return out;
  }
  function syncProgress() {
    if (syncing) return syncing;
    if (!signedIn()) return Promise.resolve(null);
    syncing = loadLib().then(function () {
      var sb = window.supabase.createClient(S.SUPABASE_URL, S.SUPABASE_ANON_KEY);
      window.EA_SB = window.EA_SB || sb;
      return sb.auth.getSession().then(function (r) {
        var ses = r.data && r.data.session; if (!ses) return null;
        var uid = ses.user.id;
        // 가입 동의를 마친 회원만 저장한다
        return sb.from("profiles").select("age14_confirmed").eq("id", uid).maybeSingle().then(function (pr) {
          if (!pr.data || !pr.data.age14_confirmed) return null;
          var rows = [], from = 0;
          function page() {
            return sb.from("user_progress").select("store,lesson_id,rec,updated_at").range(from, from + 999).then(function (q) {
              if (q.error) throw q.error;
              rows = rows.concat(q.data || []);
              if ((q.data || []).length === 1000) { from += 1000; return page(); }
            });
          }
          return page().then(function () {
            var loc = localStores(), remote = {}, up = [], changed = {};
            rows.forEach(function (x) { (remote[x.store] = remote[x.store] || {})[x.lesson_id] = x.rec; });
            Object.keys(remote).forEach(function (st) { if (!loc[st]) loc[st] = {}; });
            Object.keys(loc).forEach(function (st) {
              var L = loc[st], R = remote[st] || {};
              Object.keys(L).forEach(function (id) {
                var a = L[id], b = R[id];
                if (!a || typeof a !== "object") return;
                if (!b || (a.at || 0) > (b.at || 0)) up.push({ user_id: uid, store: st, lesson_id: id, rec: a, updated_at: new Date().toISOString() });
              });
              Object.keys(R).forEach(function (id) {
                var a = L[id], b = R[id];
                if (!a || (b.at || 0) > (a.at || 0)) { L[id] = b; changed[st] = true; }
              });
            });
            Object.keys(changed).forEach(function (st) { try { localStorage.setItem(st, JSON.stringify(loc[st])); } catch (e) {} });
            var jobs = [];
            for (var i = 0; i < up.length; i += 500) jobs.push(sb.from("user_progress").upsert(up.slice(i, i + 500)));
            return Promise.all(jobs).then(function () { return { up: up.length, down: Object.keys(changed).length }; });
          });
        });
      });
    }).catch(function () { return null; });
    return syncing;
  }
  window.EA_SYNC = syncProgress;
  // 레슨을 푸는 중에는 방해하지 않도록 조금 뒤에 한 번만 맞춘다
  setTimeout(function () { try { syncProgress(); } catch (e) {} }, 1500);
  if (immersive) setInterval(function () { if (!document.hidden) { syncing = null; syncProgress(); } }, 90000);

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
