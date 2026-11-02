"""지리학 트랙 가이드 공용 자료."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gk import *  # noqa: F401,F403

T = "geography"
GEOSYS = book("시그마프레스", "Christopherson 외, Geosystems (번역본 『지오시스템』, 장 제목으로 표기)")
KNOX = book("시그마프레스", "Knox · Marston, Human Geography: Places and Regions in Global Context (번역본 『인문지리학』, 장 제목으로 표기)")
SLOCUM = book("Pearson/CRC", "Slocum 외, Thematic Cartography and Geovisualization (장 제목으로 표기)")
PIDWIRNY = {"kind": "book", "provider": "Pidwirny (무료 공개 교재)", "title": "Fundamentals of Physical Geography (PhysicalGeography.net)", "url": "http://www.physicalgeography.net/fundamentals/contents.html", "lang": "영어"}
PSU_CARTO = {"kind": "lecture", "provider": "Penn State (공개 강의)", "title": "GEOG 486 Cartography and Visualization", "url": "https://courses.ems.psu.edu/geog486/", "lang": "영어"}
NGII = {"kind": "web", "provider": "국토지리정보원", "title": "국토정보플랫폼 (지형도·항공 사진·지도 자료)", "url": "https://map.ngii.go.kr/", "lang": "한국어"}
KMA = {"kind": "web", "provider": "기상청", "title": "기상자료개방포털 (기후 통계)", "url": "https://data.kma.go.kr/", "lang": "한국어"}
SGIS = {"kind": "web", "provider": "국가데이터처", "title": "SGIS 통계지리정보서비스 (통계 지도)", "url": "https://sgis.kostat.go.kr/", "lang": "한국어"}
QGIS = {"kind": "web", "provider": "QGIS 프로젝트", "title": "QGIS 무료 GIS 소프트웨어와 교육 자료", "url": "https://qgis.org/", "lang": "영어(한국어 일부)"}
