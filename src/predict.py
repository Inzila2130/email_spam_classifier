import joblib
from preprocess import clean_text


# Load trained model and vectorizer
model = joblib.load("models/spam_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


def predict_message(message):
    """
    Predict whether a message is Spam or Ham.

    Returns:
        prediction (str)
        confidence (float)
    """

    cleaned_message = clean_text(message)

    vector = vectorizer.transform([cleaned_message])

    prediction = model.predict(vector)[0]

    probability = model.predict_proba(vector)[0]

    confidence = max(probability) * 100

    label = "Spam" if prediction == 1 else "Ham"

    return label, round(confidence, 2)


if __name__ == "__main__":
    sample = "Congratulations! You have won a free iPhone."

    prediction, confidence = predict_message(sample)

    print(prediction)
    print(confidence)