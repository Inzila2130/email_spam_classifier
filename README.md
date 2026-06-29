![MailShield Banner](static/assets/mailshield-banner.png)

# MailShield - AI Email & SMS Spam Classifier
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> An AI-powered web application that classifies Email and SMS messages as **Spam** or **Ham (Safe)** using Natural Language Processing (NLP) and Machine Learning.

---

## 🌐 Live Demo

🚀 **Try MailShield:**  
**https://YOUR-RENDER-URL.onrender.com**

> Replace the URL above with your actual Render deployment URL.

---

## 📌 Features

- ✉️ Email & SMS Spam Detection
- 🤖 Machine Learning Classification
- 🧹 NLP Text Preprocessing
- 🌙 Dark & ☀️ Light Theme
- 📊 Confidence Score Visualization
- 📈 Prediction Statistics
- 📋 Copy Prediction Result
- 💬 Safe & Spam Sample Messages
- 📜 Prediction History
- 📱 Fully Responsive UI
- ⚡ Fast Flask Backend

---

## 🖼️ Screenshots

### Dark Theme
![Dark Theme](static/assets/darktheme-web.png)

### Light Theme
![Light Theme](static/assets/lighttheme-web.png)

### Spam Detection
![Spam Example](static/assets/spam-web.png)

### Ham Detection
![Ham Example](static/assets/ham-web.png)

### Mobile View (Light - Home Page)
![Mobile Light](static/assets/mobileview_ligh.png)

### Mobile View (Dark - Spam)
![Mobile Dark 1](static/assets/mobileview-dark2.png)

### Mobile View (Dark - Spam View 2)
![Mobile Dark 2](static/assets/mobileview-3.png)

## 🧠 Machine Learning Pipeline

```text
Input Message
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Multinomial Naive Bayes
      │
      ▼
Spam / Ham Prediction
```

---

## 🛠️ Tech Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Flask
- Python

### Machine Learning

- Scikit-Learn
- Pandas
- NumPy
- NLTK
- Joblib

---

## 📂 Project Structure

```text
Email Spam Classifier/
│
├── app/
│   └── app.py
│
├── data/
│
├── models/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   └── evaluate.py
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── icons/
│
├── templates/
│   ├── index.html
│   └── 404.html
│
├── requirements.txt
├── README.md
├── Procfile
├── runtime.txt
├── render.yaml
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/email_spam_classifier.git
```

Go to the project folder:

```bash
cd email_spam_classifier
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app/app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 📊 Model Information

| Property | Value |
|----------|-------|
| Algorithm | Multinomial Naive Bayes |
| Feature Extraction | TF-IDF Vectorizer |
| NLP | Tokenization, Stopword Removal, Stemming |
| Language | Python |

---

## 🚀 Future Improvements

- User Authentication
- Email Inbox Integration
- REST API
- Deep Learning Models
- Multi-language Spam Detection
- Cloud Database Support
- Dashboard Analytics

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Inzila Danish Khan**

GitHub: https://github.com/Inzila2130

---

Thank you for visiting this project. Feedback and suggestions are always appreciated.