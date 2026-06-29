from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

from src.preprocess import clean_text

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "models" / "spam_model.pkl")
vectorizer = joblib.load(BASE_DIR / "models" / "tfidf_vectorizer.pkl")

data = pd.read_csv(BASE_DIR / "data" / "spam.csv")

X = data["message"].apply(clean_text)
y = data["label"]

X = vectorizer.transform(X)

predictions = model.predict(X)

print("Accuracy:", accuracy_score(y, predictions))
print("\nClassification Report:\n")
print(classification_report(y, predictions))
print("\nConfusion Matrix:\n")
print(confusion_matrix(y, predictions))