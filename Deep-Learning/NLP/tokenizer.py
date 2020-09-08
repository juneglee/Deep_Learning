import nltk
from nltk.tokenize import sent_tokenize
from nltk import WordPunctTokenizer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer

# sentence tokenizing
# word tokenizing
# 타입에 따라서 토큰으로 분리
type = ['stem', 'lemma', 'pos']

def tokenize(document, type):
    words = []

    sentences = sent_tokenize(document) # sentence tokenizing

    for sentence in sentences:
        words.extend(WordPunctTokenizer.tokenize(sentence))

    if type == 'stem':
        lancaster_stemmer = LancasterStemmer()
        tokenized = [lancaster_stemmer.stem(w) for w in words]
    elif type == "lemma":
        lemmatizer = WordNetLemmatizer()
        tokenized = [lemmatizer.lemmatize(w) for w in words]
    elif type == "pos":
        tokenized = nltk.pos_tag(words)
    else:
        raise TypeError

    return tokenized

if __name__ == '__main__':
    document = "Hello, world. These are NLP tutorials."
    print(tokenize(document, 'pos'))

#
# import nltk
# from nltk.tokenize import sent_tokenize
# from nltk import WordPunctTokenizer
# from nltk.stem import LancasterStemmer
# from nltk.stem import WordNetLemmatizer
#
#
# types = ['stem', 'lemma', 'pos']
#
# def tokenize(document, type):
#     words = []
#
#     sentences = sent_tokenize(document) # sentence tokenizing
#     for sentence in sentences:
#         words.extend(WordPunctTokenizer().tokenize(sentence)) # word tokenizing
#     if type == 'stem':
#         lancaster_stemmer = LancasterStemmer()
#         tokenized = [lancaster_stemmer.stem(w) for w in words] # stemming
#     elif type == 'lemma':
#         lemmatizer = WordNetLemmatizer()
#         tokenized = [lemmatizer.lemmatize(w) for w in words] # lemmatizing
#     elif type == 'pos':
#         # tokenized = nltk.pos_tag(words) # pos tagging
#         tokenized = [token[0]+'/'+token[1] for token in nltk.pos_tag(words)]
#     else:
#         raise TypeError
#     return tokenized
#
#
# if __name__ == '__main__':
#     document = 'Hello, Python\nThese are NLP tutorials\nWelcome to Saltlux'
#     print(tokenize(document, 'pos'))




