import json
import pickle
import sys

from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from nltk import download
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation

download('punkt')
download('stopwords')

stopwords_eng = stopwords.words('english')

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

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/predict', methods = ['GET', 'POST'])
@cross_origin()
def predict():
    if request.method == 'GET':
        input = request.args.get('input')
    else:
        input = request.get_json(force=True)['input']
    if not input:
        return 'No input value found'
    return get_sentiment(input)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False, host='0.0.0.0')
