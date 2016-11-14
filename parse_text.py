import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


with open('example.txt','r') as f:
    text = json.load(f)
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text['text'])
    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    print(word_tokens)
    print(filtered_sentence)
    print(' '.join(filtered_sentence))