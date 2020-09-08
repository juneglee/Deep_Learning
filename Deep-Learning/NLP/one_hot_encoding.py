import nltk
from nltk.tokenize import sent_tokenize
from nltk import WordPunctTokenizer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer


types = ['stem', 'lemma', 'pos']

def tokenize(document, type):
    words = []

    sentences = sent_tokenize(document) # sentence tokenizing
    for sentence in sentences:
        words.extend(WordPunctTokenizer().tokenize(sentence)) # word tokenizing
    if type == 'stem':
        lancaster_stemmer = LancasterStemmer()
        tokenized = [lancaster_stemmer.stem(w) for w in words] # stemming
    elif type == 'lemma':
        lemmatizer = WordNetLemmatizer()
        tokenized = [lemmatizer.lemmatize(w) for w in words] # lemmatizing
    elif type == 'pos':
        # tokenized = nltk.pos_tag(words) # pos tagging
        tokenized = [token[0]+'/'+token[1] for token in nltk.pos_tag(words)]
    else:
        raise TypeError
    return tokenized

def make_vocab(tokens):
    word2index={}
    for voca in tokens:
        if voca not in word2index.keys():
            word2index[voca]=len(word2index)
    return word2index

def one_hot_encoding(word, word2index):
    one_hot_vector = [0]*(len(word2index))
    index=word2index[word]
    one_hot_vector[index]=1
    return one_hot_vector

if __name__ == '__main__':
    document = 'Hello, Python\nThese are NLP tutorials\nWelcome to Saltlux'
    tokens = tokenize(document, 'lemma')
    word2index = make_vocab(tokens)
    print('dictionary: ' , word2index)
    print(one_hot_encoding("NLP", word2index))
