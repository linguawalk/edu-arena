// curriculum-data.js
// Code Arena 전체 커리큘럼 구조. index.html, browse.html, player.html이 공유해서 사용합니다.
// 새 언어/레벨/유닛을 추가할 때는 이 파일만 수정하면 됩니다.

const CURRICULUM = {

  foundation: {
    title: "Foundation",
    subtitle: "프로그래밍 언어 이전에, 컴퓨터처럼 생각하기",
    accent: "var(--c-found)",
    stages: [
      {
        key: "stage0_computer_thinking",
        path: "foundation/stage0_computer_thinking",
        title: "Stage 0 · 컴퓨터적 사고",
        units: 6
      },
      {
        key: "stage1_c_onboarding",
        path: "foundation/stage1_c_onboarding",
        title: "Stage 1 · C 온보딩",
        units: 8
      }
    ]
  },

  tracks: [
    {
      key: "track_a",
      title: "트랙 A · 시스템 / 저수준",
      subtitle: "메모리를 직접 다루는 언어들",
      accent: "var(--c-system)",
      category: "system_low_level",
      languages: [
        { key: "c",    name: "C",     path: "content/system_low_level/c",    levels: 6 },
        { key: "cpp",  name: "C++",   path: "content/system_low_level/cpp",  levels: 4 },
        { key: "rust", name: "Rust",  path: "content/system_low_level/rust", levels: 4 }
      ]
    },
    {
      key: "track_b",
      title: "트랙 B · 객체지향 / 엔터프라이즈",
      subtitle: "기업용 애플리케이션 언어들",
      accent: "var(--c-oop)",
      category: "oop_enterprise",
      languages: [
        { key: "visual_basic", name: "Visual Basic", path: "content/oop_enterprise/visual_basic", levels: 6 },
        { key: "csharp",       name: "C#",            path: "content/oop_enterprise/csharp",       levels: 6 },
        { key: "java",         name: "Java",           path: "content/oop_enterprise/java",         levels: 6 }
      ]
    },
    {
      key: "track_c",
      title: "트랙 C · 스크립트 / 실무",
      subtitle: "웹과 자동화의 언어들",
      accent: "var(--c-script)",
      category: "scripting",
      languages: [
        { key: "python",     name: "Python",     path: "content/scripting/python",     levels: 6 },
        { key: "javascript", name: "JavaScript", path: "content/scripting/javascript", levels: 6 },
        { key: "php",        name: "PHP",        path: "content/scripting/php",        levels: 4 }
      ]
    },
    {
      key: "track_d",
      title: "트랙 D · 레거시 / 역사",
      subtitle: "지금의 언어들이 태어난 뿌리",
      accent: "var(--c-legacy)",
      category: "legacy_historical",
      languages: [
        { key: "basic_early", name: "BASIC",   path: "content/legacy_historical/basic_early", levels: 3 },
        { key: "pascal",      name: "Pascal",  path: "content/legacy_historical/pascal",       levels: 3 },
        { key: "fortran",     name: "FORTRAN", path: "content/legacy_historical/fortran",       levels: 3 },
        { key: "cobol",       name: "COBOL",   path: "content/legacy_historical/cobol",         levels: 3 }
      ]
    }
  ],

  modules: [
    {
      key: "dsa",
      title: "자료구조 & 알고리즘",
      subtitle: "언어에 상관없이 알아야 할 것 (Python으로 구현)",
      accent: "var(--c-module)",
      path: "modules/data_structures_algorithms",
      levels: 4
    },
    {
      key: "statistics",
      title: "통계",
      subtitle: "평균·분산부터 가설검정, 베이즈 정리, 심슨의 역설까지",
      accent: "var(--c-module)",
      path: "modules/statistics",
      levels: 4
    },
    {
      key: "db_theory",
      title: "DB 이론",
      subtitle: "정규화, 기본키·외래키, 트랜잭션(ACID), 인덱스",
      accent: "var(--c-module)",
      path: "modules/db_theory",
      levels: 2
    },
    {
      key: "linux",
      title: "Linux",
      subtitle: "파일 권한, 명령어, 프로세스, 셸 스크립트",
      accent: "var(--c-module)",
      path: "modules/linux",
      levels: 4
    },
    {
      key: "excel_access",
      title: "Excel / Access",
      subtitle: "함수·참조 원리부터 피벗테이블, 관계형 DB 개념까지",
      accent: "var(--c-module)",
      path: "modules/excel_access",
      levels: 2
    }
  ],

  // 실습형(코드 작성) 콘텐츠 — 축 B. 개념이해형(축 A)과 달리 stdin/stdout 실행 채점이 필요하며,
  // practice-player.html로 재생합니다(browse.html?type=practice&lang=... 에서 연결).
  practice: [
    { key: "python",     name: "Python",     path: "practice/python",     levels: 6 },
    { key: "c",           name: "C",          path: "practice/c",          levels: 6 },
    { key: "cpp",         name: "C++",        path: "practice/cpp",        levels: 4 },
    { key: "java",        name: "Java",       path: "practice/java",       levels: 6 },
    { key: "csharp",      name: "C#",         path: "practice/csharp",     levels: 6 },
    { key: "javascript",  name: "JavaScript", path: "practice/javascript", levels: 6 },
    { key: "rust",        name: "Rust",       path: "practice/rust",       levels: 4 },
    { key: "php",         name: "PHP",        path: "practice/php",        levels: 4 },
    { key: "ruby",        name: "Ruby",       path: "practice/ruby",       levels: 6 },
    { key: "r",           name: "R",          path: "practice/r",          levels: 4 },
    { key: "sql",         name: "SQL",        path: "practice/sql",        levels: 4 },
    { key: "vb",          name: "Visual Basic", path: "practice/vb",       levels: 6 },
    { key: "basic",       name: "BASIC",      path: "practice/basic",      levels: 3 },
    { key: "pascal",      name: "Pascal",     path: "practice/pascal",     levels: 3 },
    { key: "fortran",     name: "FORTRAN",    path: "practice/fortran",    levels: 3 },
    { key: "cobol",       name: "COBOL",      path: "practice/cobol",      levels: 3 }
  ],

  // Tier 2: 글로벌 벤더 자격증 (객관식 전용) — 코딩 실습 없이 player.html/browse.html을 그대로 재사용
  certifications: [
    {
      key: "cert_aws",
      title: "Amazon (AWS)",
      subtitle: "클라우드 서비스 자격증",
      accent: "var(--c-oop)",
      exams: [
        {
          key: "clf-c02",
          name: "AWS Certified Cloud Practitioner (CLF-C02)",
          path: "certifications/aws/clf-c02",
          levels: 4,
          levelNames: ["클라우드 개념", "보안·컴플라이언스", "핵심 서비스", "요금·청구"]
        },
        {
          key: "saa-c03",
          name: "AWS Certified Solutions Architect – Associate (SAA-C03)",
          path: "certifications/aws/saa-c03",
          levels: 4,
          levelNames: ["보안 아키텍처 설계", "복원력 아키텍처 설계", "고성능 아키텍처 설계", "비용 최적화 아키텍처 설계"]
        }
      ]
    },
    {
      key: "cert_oracle",
      title: "Oracle",
      subtitle: "Java·데이터베이스 자격증",
      accent: "var(--c-legacy)",
      exams: [
        {
          key: "java-ocp",
          name: "Oracle Certified Professional: Java SE 17 Developer (1Z0-829)",
          path: "certifications/oracle/java-ocp",
          levels: 7,
          levelNames: ["기본 타입·형변환", "OOP 심화(상속·인터페이스·sealed)", "컬렉션과 제네릭", "함수형 프로그래밍(람다·스트림)", "예외 처리", "동시성", "I/O·모듈·JDBC"]
        },
        {
          key: "sql-associate",
          name: "Oracle Database SQL Certified Associate (1Z0-071)",
          path: "certifications/oracle/sql-associate",
          levels: 3,
          levelNames: ["SELECT 기초·함수", "집계함수·JOIN·서브쿼리·집합연산자", "DML·트랜잭션·뷰·시퀀스·권한"]
        },
        {
          key: "plsql-associate",
          name: "Oracle Database Program with PL/SQL Certified Associate (1Z0-149)",
          path: "certifications/oracle/plsql-associate",
          levels: 7,
          levelNames: ["PL/SQL 블록 기초", "커서 심화", "예외 처리", "프로시저와 함수", "패키지", "트리거", "동적 SQL·설계 고려사항"]
        }
      ]
    },
    {
      key: "cert_microsoft",
      title: "Microsoft (Azure)",
      subtitle: "클라우드 서비스 자격증",
      accent: "var(--c-script)",
      exams: [
        {
          key: "az-900",
          name: "Microsoft Certified: Azure Fundamentals (AZ-900)",
          path: "certifications/microsoft/az-900",
          levels: 3,
          levelNames: ["클라우드 개념", "Azure 아키텍처와 핵심 서비스", "Azure 관리·거버넌스"]
        }
      ]
    },
    {
      key: "cert_google",
      title: "Google Cloud",
      subtitle: "클라우드 서비스 자격증",
      accent: "var(--c-system)",
      exams: [
        {
          key: "cloud-digital-leader",
          name: "Google Cloud Digital Leader",
          path: "certifications/google/cloud-digital-leader",
          levels: 6,
          levelNames: ["디지털 전환", "데이터 전환", "Google Cloud AI", "인프라 현대화", "신뢰·보안", "운영"]
        }
      ]
    },
    {
      key: "cert_cisco",
      title: "Cisco",
      subtitle: "네트워크 자격증",
      accent: "var(--c-module)",
      exams: [
        {
          key: "ccna",
          name: "Cisco Certified Network Associate (CCNA 200-301)",
          path: "certifications/cisco/ccna",
          levels: 6,
          levelNames: ["네트워크 기초", "네트워크 액세스", "IP 연결성", "IP 서비스", "보안 기초", "자동화·프로그래밍"]
        }
      ]
    },
    {
      key: "cert_lpi",
      title: "LPI",
      subtitle: "리눅스 자격증",
      accent: "var(--c-found)",
      exams: [
        {
          key: "lpic-1",
          name: "LPIC-1: Linux Administrator (101-500 / 102-500)",
          path: "certifications/lpi/lpic-1",
          levels: 4,
          levelNames: ["시스템 아키텍처·패키지 관리", "GNU/Unix 명령어(텍스트 처리)", "셸 스크립팅·사용자 관리·cron", "네트워킹 기초"]
        },
        {
          key: "lpic-2",
          name: "LPIC-2: Linux Engineer (201-450 / 202-450)",
          path: "certifications/lpi/lpic-2",
          levels: 4,
          levelNames: ["커널·RAID/LVM·부팅(GRUB2)", "시스템 유지보수·네트워크 진단", "DNS·웹서버·파일공유·방화벽", "이메일·LDAP·DHCP·SSH 강화"]
        }
      ]
    }
  ],

  // 유닛 파일 이름 규칙: 항상 4유닛/레벨, level{N}_unit{NN}.json
  UNITS_PER_LEVEL: 4,

  // 파일 경로 헬퍼
  unitFile(basePath, level, unit) {
    const uu = String(unit).padStart(2, "0");
    return `${basePath}/level${level}_unit${uu}.json`;
  },
  stageFile(basePath, unit) {
    const uu = String(unit).padStart(2, "0");
    return `${basePath}/unit${uu}.json`;
  }
};

if (typeof module !== "undefined") { module.exports = CURRICULUM; }
