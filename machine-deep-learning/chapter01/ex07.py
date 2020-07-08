from bs4 import BeautifulSoup

# beautifulSoup : HTML, XML 을 분석(파싱) 해주는 라이브러리 

# CSS 선택자 사용하기 

# 태그 선택자
# "h1"
# "html#<아이디 이름>"
# 아이디 선택자 
# "#<아이디 이름>"
# 클래스 선택자 
# ".<클래스 이름>"
# 후손 선택자 : 아래 모든 것
#  "#meigen li "
# 자손 선택자 : 바로 아래 있는 것
#  "#ul.items > li "
html = """
<html>
<body>
<div id="meigen">
  <h1>위키북스 도서</h1>
  <ul class="items">
    <li>유니티 게임 이펙트 입문</li>
    <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
    <li>모던 웹사이트 디자인의 정석</li>
  </ul>
</div>
</body>
</html>
"""
# HTML 분석하기 --- (※2)
soup = BeautifulSoup(html, 'html.parser')
# 필요한 부분을 CSS 쿼리로 추출하기
# 타이틀 부분 추출하기 --- (※3)
h1 = soup.select_one("div#meigen > h1").string
# soup.select_one() : 하나를 선택하는 것
# soup.select() : 여러개를 선택하는 것

print("h1 =", h1)
# 목록 부분 추출하기 --- (※4)
li_list = soup.select("div#meigen > ul.items > li")
for li in li_list:
  print("li =", li.string)