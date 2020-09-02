# 어간 추출(Stemming) & 표제어 추출(Lemmatization)
# 정규화 기법 중 코퍼스에 있는 단어의 개수를 줄일 수 있느 ㄴ기법 
# 눈으로 봤을 때는 서로 다른 단어들이지만, 하나의 단어로 일반화 시킬 수 있다
# 단어의 빈도수를 기반으로 문제를 풀고자 하는 BoW(Bag of Words) 표현을 사용하는 자연어 처리 문제에서 주로 사용

# 표제어 추출 (Lemmatization)
# : 단어들로부터 표제어를 찾아 가는 과정
# ex)  am, are, is는 서로 다른 스펠링이지만 그 뿌리 단어는 be라고 볼 수 있습니다. 
#      이 때, 이 단어들의 표제어는 be라고 합니다

# 표제어 추출을 하는 가장 섬세한 방법은 단어의 형태학적 파싱을 먼저 진행하는 것
# 행태소란 의미를 가진 가장 작은 단위
# 형태학(morphology)이란, 형태소로부터 단어들을 만들어가는 학문을 뜻

# 형태소의 두가지 종류 
# 어간(Stem) : 단어의 의미를 담고 있는 단어의 핵십 부분
# 접사(affix) : 단어에 추가적인 의미를 주는 부분

# NLTK에서는 표제어 추출을 위한 도구인 WordNetLemmatizer를 지원
from nltk.stem import WordNetLemmatizer
n=WordNetLemmatizer()
words=['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']
print([n.lemmatize(w) for w in words])
# ['policy', 'doing', 'organization', 'have', 'going', 'love', 'life', 'fly', 'dy', 'watched', 'ha', 'starting']
# 위의 결과에서는 dy나 ha와 같이 의미를 알 수 없는 적절하지 못한 단어를 출력
# 표제어 추출기(lemmatizer)가 본래 단어의 품사 정보를 알아야만 정확한 결과를 얻을 수 있기 때문

# n.lemmatize('dies', 'v') # 'die'
# n.lemmatize('watched', 'v') # 'watch'
# n.lemmatize('has', 'v') # 'have'
# dies와 watched, has가 문장에서 동사로 쓰였다는 것을 알려준다면 표제어 추출기는 품사의 정보를 보존하면서 정확한 Lemma를 출력

# 어간 추출(Stemming)
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
s = PorterStemmer()
text="This was not the map we found in Billy Bones's chest, but an accurate copy, complete in all things--names and heights and soundings--with the single exception of the red crosses and the written notes."
words=word_tokenize(text)
print(words)
print([s.stem(w) for w in words])
# ['thi', 'wa', 'not', 'the', 'map', 'we', 'found', 'in', 'billi', 'bone', "'s", 
# 'chest', ',', 'but', 'an', 'accur', 'copi', ',', 
# 'complet', 'in', 'all', 'thing', '--', 'name', 'and', 'height', 'and', 'sound', 
# '--', 'with', 'the', 'singl', 'except', 'of', 'the', 'red', 'cross', 'and', 'the', 'written', 'note', '.']

# 표제어 추출과 어간 추출을 비교 
# 어간 추출(Stemming)
# am → am
# the going → the go
# having → hav

# 표제어 추출(Lemmatization)
# am → be
# the going → the going
# having → have