# flask 모듈
#
# flask 모듈 사용하기 
from flask import Flask
app = Flask(__name__)

@app.route("/") #  데코레이터 
def hello():
    return "<h1>Hello World!</h1>"

# 실생방법 (윈도우) 
# set Flask_APP = flask_basic.py
# flask run
# 실생방법 (맥과 리눅스 ) 
# export Flask_APP = flask_basic.py
# flask run
# 이때 나오는 url 확인 

# BeautifulSoup 스크레이핑 실행하기 (http://127.0.0.1:5000)
from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route("/")

def hello():
    # urlopen() 함수로 기상청의 전국 날씨를 읽습니다.
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

    # BeautifulSoup를 사용해 웹 페이지를 분석합니다.
    soup = BeautifulSoup(target, "html.parser")

    # location 태그를 찾습니다.
    output = ""
    for location in soup.select("location"):
        # 내부의 city, wf, tmn, tmx 태그를 찾아 출력합니다.
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨: {}<br/>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}"\
            .format(\
                location.select_one("tmn").string,\
                location.select_one("tmx").string\
            )
        output += "<hr/>"
    return output
