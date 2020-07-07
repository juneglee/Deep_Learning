import urllib.request 
# URL과 저장 경로 지정하기
url = "http://www.google.co.kr"
savename = "test.png"

mem = urllib.request.urlopen(url).read()
# print(mem)
print(mem.decode("euc-kr"))

# b' ~ 바이너리를 의미한것이며 , 바이너리를 다운한 것이다 