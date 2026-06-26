from flask import Flask, render_template, request
import joblib
from src.preprocess import clean_text

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static")
)

print("Base directory:", BASE_DIR)
print("Templates folder:", BASE_DIR / "templates")

model = joblib.load("models/spam_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    message = clean_text(message)

    vector = tfidf.transform([message])
    result = model.predict(vector)

    output = "SPAM 🚨" if result[0] == 1 else "HAM ✅"

    return render_template("index.html", prediction=output)

if __name__ == "__main__":
    app.run(debug=True)