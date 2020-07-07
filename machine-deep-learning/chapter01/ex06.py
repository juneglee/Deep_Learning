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
print(text)