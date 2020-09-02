# 정제(Cleaning) & 정규화(Normalization)

# 정제 : 갖ㅂ고 있는 코퍼스로부터 노이즈 데이터를 제거한다 
# 정규화 : 표현 방법이 다른 단어들을 통합시켜서 같은 단어로 만들어 준다 

# 정제 작업은 토큰화 작어베 방해가 되는 부분들을 배제시키고 토크놔 작업을 수행하기 위해서 
# 토큰화 작업보다 앞서 이루어지기도 하지만 토큰화 작업 이후에도 여전히 남아 있는 노이즈들을 제거하기 위해 
# 지속적으로 이루어지기도 합니다. 

# 규칙에 기반한 표기가 다른 단어들의 통합
# 필요에 따라 직접 코딩을 통해 정의할 수 있는 정규화 규칙의 예로서 같은 의미를 갖고있음에도, 
# 표기가 다른 단어들을 하나의 단어로 정규화하는 방법을 사용할 수 있습니다.
# ex) USA와 US는 같은 의미를 가지므로, 하나의 단어로 정규화해볼 수 있습니다.

# 대, 소문자 통합 
# 대문자와 소문자를 무작정 통합해서는 안된다 

# 불필요한 단어의 제거(Removing Unnecessary Words)
# 정제 작업에서 제거해야하는 노이즈 데이터(noise data)는 자연어가 아니면서 아무 의미도 갖지 않는 글자들(특수 문자 등)을 의미하기도 하지만, 
# 분석하고자 하는 목적에 맞지 않는 불필요 단어들을 노이즈 데이터라고 하기도 합니다.
# (1) 등장 빈도가 적은 단어(Removing Rare words)
# (2) 길이가 짧은 단어(Removing words with very a short length)
#     - 일반적으로 영단어 6-7 정도, 한국어 단어 평균 길이는 2-3 정도로 추정
import re
text = "I was wondering if anyone out there could enlighten me on this car."
shortword = re.compile(r'\W*\b\w{1,2}\b')
print(shortword.sub('', text))
#  was wondering anyone out there could enlighten this car.
# 길이가 1~ 2인 단어들을 정규 표현식을 이용하여 삭제 



