/* edu-arena 공통 상단 바: 각 과목 섹션에서 edu-arena 메인으로 돌아가는 링크 */
(function () {
  var SECTIONS = {
    socio: "사회와 역사", biz: "경제와 경영", lit: "언어와 문학",
    math: "수학", sci: "과학", tech: "공학", code: "코딩", 
  };
  // 레슨·진단 화면은 몰입형이라 상단 바를 넣지 않음
  if (/(player|practice-player|placement)\.html$/.test(location.pathname)) return;
  var parts = location.pathname.split("/").filter(Boolean);
  var key = "";
  for (var i = 0; i < parts.length; i++) { if (SECTIONS[parts[i]]) { key = parts[i]; break; } }
  var home = key ? location.pathname.slice(0, location.pathname.indexOf("/" + key + "/") + 1) : "/";

  var css = document.createElement("style");
  css.textContent =
    ".ea-bar{background:#172033;color:#E7ECFA;font:500 14px/1 'IBM Plex Sans KR','Apple SD Gothic Neo','Malgun Gothic',sans-serif}" +
    ".ea-bar .ea-in{max-width:1040px;margin:0 auto;padding:0 20px;height:36px;display:flex;align-items:center;gap:8px;overflow:hidden;white-space:nowrap}" +
    ".ea-bar a{color:#fff;text-decoration:none;font-weight:700}" +
    ".ea-bar a:hover{text-decoration:underline}" +
    ".ea-bar .ea-sep{opacity:.5}" +
    ".ea-bar .ea-all{margin-left:auto;font-weight:500;color:#E7ECFA}";
  document.head.appendChild(css);

  var bar = document.createElement("div");
  bar.className = "ea-bar";
  bar.innerHTML =
    '<div class="ea-in"><a href="' + home + '">edu-arena</a>' +
    (key ? '<span class="ea-sep">›</span><a href="' + home + key + '/browse.html">' + SECTIONS[key] + "</a>" : "") +
    (/\/olympiad\//.test(location.pathname) ? '<span class="ea-sep">›</span><span>심화</span>' : "") +
    '<a class="ea-all" href="' + home + '#subjects">전체 과목</a></div>';
  document.body.insertBefore(bar, document.body.firstChild);
})();
