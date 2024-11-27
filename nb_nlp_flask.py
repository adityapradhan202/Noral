from flask import Flask, jsonify

from joblib import load
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

saved_nb_model = load(filename='models/nb_model.joblib')
saved_vectorizer = load(filename='models/vectorizer.joblib')

app = Flask(__name__)

@app.route("/text-classify/<string:sentences>")
def nb_predict(sentences:str,
               model:MultinomialNB=saved_nb_model,
               vectorizer:TfidfVectorizer=saved_vectorizer):
    text_list = sentences.split(". ")
    output_list = []

    for text in text_list:
        transformed_text = vectorizer.transform([text])
        pred_class = model.predict(transformed_text)[0]
        output_list.append(pred_class)

    result = {
        "Extracted symptoms" : output_list
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
