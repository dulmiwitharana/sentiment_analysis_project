from flask import Flask, render_template, request, redirect
from helper import preprocessing, vectorizer, get_prediction
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

data = dict()
reviews = []
positive = 0
negative = 0

@app.route("/")
def index():
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative
    return render_template('index.html', data=data)

@app.route("/", methods=['POST'])
def my_post():
    text = request.form['text']
    preprocessed_txt = preprocessing(text)
    vectorized_txt = vectorizer(preprocessed_txt)
    prediction = get_prediction(vectorized_txt)

    global positive, negative

    if prediction == 'negative':
        negative += 1
    else:
        positive += 1

    reviews.insert(0, text)
    return redirect(request.url)

if __name__ == "__main__":
    app.run()
