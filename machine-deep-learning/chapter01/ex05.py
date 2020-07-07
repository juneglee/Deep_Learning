import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
# 매개변수를 URL 인코딩합니다. --- (※1)
values = {
    'stnId': '108'
}
params = urllib.parse.urlencode(values)

url = API + "?" + params
print("url=", url)

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(data) 
# data로 출력하면 decode를 하기 전이므로 바이너리 방식으로 출력한다 
# 그렇기 때문에 utf-8 로 decode를 실행하여 문자열로 출력할 수 있도록 한다 
# ex 06 참조 