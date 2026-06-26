import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from preprocess import clean_text

# load dataset (IMPORTANT FIXED PATH)
df = pd.read_csv(
    "data/spam_data.txt",
    sep="\t",
    header=None,
    names=["label", "message"]
)

# convert labels
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# clean text
df['message'] = df['message'].apply(clean_text)

# features
tfidf = TfidfVectorizer(max_features=5000)
X = tfidf.fit_transform(df['message'])
y = df['label']

# train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# model
model = MultinomialNB()
model.fit(X_train, y_train)

# save model
joblib.dump(model, "models/spam_model.pkl")
joblib.dump(tfidf, "models/tfidf_vectorizer.pkl")

print("Model trained successfully 👍")