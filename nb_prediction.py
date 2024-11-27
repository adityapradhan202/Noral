from joblib import load
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load saved model and vectorizer
saved_nb_model = load(filename='models/nb_model.joblib')
saved_vectorizer = load(filename='models/vectorizer.joblib')

def nb_predict(text: str, model: MultinomialNB = saved_nb_model, vectorizer: TfidfVectorizer = saved_vectorizer):
    """
    Takes in an entire text, separates it into segments of text, 
    and identifies the symptoms of oral disease.

    Parameters:
    - text (str): The input text to analyze.
    - model (MultinomialNB): The trained Naive Bayes model.
    - vectorizer (TfidfVectorizer): The fitted TfidfVectorizer for text transformation.

    Returns:
    - set: A set of predicted disease categories.
    """

    text_list = text.split(". ")
    output_list = []

    for txt in text_list:
        transformed_text = vectorizer.transform([txt])
        pred_class = model.predict(transformed_text)[0]
        output_list.append(pred_class)

    return output_list

if __name__ == "__main__":
    description = input("Describe your problem:\n")
    print(nb_predict(text=description))