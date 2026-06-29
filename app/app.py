import os
from pathlib import Path
import time

import joblib
from flask import Flask, render_template, request

from src.preprocess import clean_text

BASE_DIR = Path(__file__).resolve().parent.parent

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static")
)

@app.after_request
def add_security_headers(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response

app.secret_key = "mailshield_secret_key_2026"

model = joblib.load(BASE_DIR / "models" / "spam_model.pkl")
vectorizer = joblib.load(BASE_DIR / "models" / "tfidf_vectorizer.pkl")

app.config["history"] = []


@app.route("/")
def home():
    return render_template(
        "index.html",
        history=app.config["history"]
    )


@app.route("/predict", methods=["POST"])
def predict():

    message = request.form.get("message", "").strip()

    if len(message) > 10000:
     return render_template(
        "index.html",
        error="Message is too long. Maximum 10,000 characters allowed."
    )

    if not message:
        return render_template(
            "index.html",
            error="Please enter a message to analyze.",
            history=app.config["history"]
        )

    start = time.perf_counter()

    cleaned_message = clean_text(message)

    vector = vectorizer.transform([cleaned_message])

    prediction = model.predict(vector)[0]

    probabilities = model.predict_proba(vector)[0]

    confidence = round(max(probabilities) * 100, 2)

    prediction_time = round((time.perf_counter() - start) * 1000, 2)

    result = {
        "label": "Spam" if prediction == 1 else "Ham",
        "confidence": confidence,
        "message": message,
        "words": len(message.split()),
        "characters": len(message),
        "prediction_time": prediction_time
    }

    history = app.config["history"]

    history.insert(0, result)

    if len(history) > 5:
        history.pop()

    return render_template(
        "index.html",
        result=result,
        history=history
    )


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)