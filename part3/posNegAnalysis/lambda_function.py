from nltk import download
download('punkt')
download('stopwords')

import json
import pickle
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation

stopwords_eng = stopword.words('english')

model_file = open('sa_classifier.pickle', 'rb')
model = pickle.load(model_file)
model_file.close()

def extract_features(words):
    return [w for w in words if w not in stopwords_eng and w not in punctuation]

def bag_of_words(words):
    bag = {}
    for w in words:
        bag[w] = bag.get(w, 0)+1
    return bag

def get_sentiment(review):
    words = word_tokenize(review)
    words = extract_features(words)
    words = bag_of_words(words)
    return model.classify(words)


def lambda_handler(event, context):
    review_result = get_sentiment(event.review)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(review_result)
    }

