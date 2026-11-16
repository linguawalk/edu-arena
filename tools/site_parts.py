"""edu-arena 정적 페이지에 공통으로 넣는 조각(하단 링크, 공통 스크립트)."""

SITE = "https://edu-arena.org"

FOOT_CSS = (
    ".ea-foot{border-top:1px solid #DCE4F0;margin-top:48px;background:#FAFBFD;color:#4A5670;"
    "font:400 14px/1.6 'IBM Plex Sans KR','Apple SD Gothic Neo','Malgun Gothic',sans-serif}"
    ".ea-foot .ea-fin{max-width:1040px;margin:0 auto;padding:24px 20px 32px;display:flex;flex-wrap:wrap;gap:8px 20px;align-items:center}"
    ".ea-foot a{color:#172033;text-decoration:none}.ea-foot a:hover{text-decoration:underline}"
    ".ea-foot .ea-copy{margin-left:auto;color:#4A5670}.ea-auth{margin-left:12px}"
)

FOOT_HTML = (
    '<footer class="ea-foot"><div class="ea-fin">'
    '<a href="/about.html">소개</a><a href="/lessons.html">전체 레슨 목록</a><a href="/contact.html">문의</a>'
    '<a href="/terms.html">이용약관</a><a href="/privacy.html"><strong>개인정보처리방침</strong></a>'
    '<span class="ea-copy">© 2026 edu-arena · 운영 여행일기 · 사업자등록번호 720-97-01549 · contact@edu-arena.org</span></div></footer>'
)

SITE_JS = '<script src="/assets/site.js" defer></script>'

ICON_HEAD = ('<link rel="icon" href="/favicon.svg" type="image/svg+xml">'
             '<link rel="icon" href="/favicon.ico" sizes="48x48">'
             '<link rel="apple-touch-icon" href="/apple-touch-icon.png">'
             '<link rel="manifest" href="/site.webmanifest"><meta name="theme-color" content="#172033">')
MARK = ('<svg class="ea-mark" viewBox="0 0 64 64" width="28" height="28" aria-hidden="true">'
        '<rect width="64" height="64" rx="15" fill="#172033"/>'
        '<path d="M22 16h-7v32h7M42 16h7v32h-7" fill="none" stroke="#fff" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M24 33l6 6 11-14" fill="none" stroke="#FFD84D" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/></svg>')
