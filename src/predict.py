import joblib
from preprocess import clean_text

model = joblib.load("models/spam_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")

def predict_message(text):
    text = clean_text(text)
    vector = tfidf.transform([text])
    result = model.predict(vector)

    return "SPAM 🚨" if result[0] == 1 else "HAM ✅"

# quick test
if __name__ == "__main__":
    print(predict_message("Win a free iPhone now"))