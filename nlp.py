import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json

stop_words = set(stopwords.words('english'))
file = open('checks.txt','r')
text = json.loads(file.read())
text_to_check = text['checks']

for line in text_to_check:
    word_tokens = word_tokenize(line['text'])
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    print(filtered_sentence)
