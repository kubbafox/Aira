import nltk
import json
from nltk.sentiment import vader

tempArray = [];

with open('../Miner/flyer1.json') as json_data:
    data = json.load(json_data)
    # print (data)

for text in data:
    tempArray.insert(0, text['text'])

encodeList = [x.encode('utf-8') for x in tempArray];

sia = vader.SentimentIntensityAnalyzer()

for sentence in encodeList:
    vs = sia.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs)))