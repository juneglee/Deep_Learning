# ## 불용어 확인
# import nltk
# from nltk.corpus import stopwords
# # nltk.download('stopwords')
# english_stopwords = stopwords.words('english')
# print(len(english_stopwords))
# print(english_stopwords[:10])

## 불용어 제거
# 다운받은 불용어는 모두 소문자로 되어있기 때문에 소문자로 변환하여야 불용어로 제거가 가능하다
# from nltk.corpus import stopwords
# from nltk import WordPunctTokenizer
# text = "Hello, world. These are NLP tutorials."
# stop_words = set(stopwords.words('english'))
# words = WordPunctTokenizer().tokenize(text)
# result = []
# for word in words:
#     if word not in stop_words:
#         result.append(word)
# print(words)
# print(result)

## POS tagging
import nltk
from nltk import WordPunctTokenizer

text = "Hello, world. These are NLP tutorials."

words = WordPunctTokenizer().tokenize(text)
tagged = nltk.pos_tag(words)
# 객체명 인식
entities = nltk.chunk.ne_chunk(tagged)

print(words)
print(tagged)
print(entities)