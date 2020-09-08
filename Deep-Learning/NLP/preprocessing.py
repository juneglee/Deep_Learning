from nltk.tokenize import sent_tokenize
text = "Hello, world. These are NLP tutorials."
print(sent_tokenize(text))

import nltk
from nltk import WordPunctTokenizer
# nltk.download('punkt')
text = "Hello, world. These are NLP tutorials."
print(WordPunctTokenizer().tokenize(text))

from nltk import WordPunctTokenizer
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
text = "Hello, world. These are NLP tutorials."
words = WordPunctTokenizer().tokenize(text)
print(words)
porter_stemmer = PorterStemmer()
print([porter_stemmer.stem(w) for w in words])
lancaster_stemmer = LancasterStemmer()
print([lancaster_stemmer.stem(w) for w in words])

import nltk
from nltk import WordPunctTokenizer
from nltk.stem import WordNetLemmatizer
# nltk.download('wordnet')
text = "Hello, world. These are NLP tutorials."
words = WordPunctTokenizer().tokenize(text)
lemmatizer = WordNetLemmatizer()
print(words)
print([lemmatizer.lemmatize(w) for w in words])

