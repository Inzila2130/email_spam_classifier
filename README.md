# 🛡️ MailShield – AI-Powered Email & SMS Spam Detector

MailShield is a Machine Learning-powered web application that classifies Email and SMS messages as **Spam** or **Ham (Legitimate)** using **Natural Language Processing (NLP)** and the **Multinomial Naive Bayes** algorithm.

Built with **Flask**, MailShield provides a modern and responsive user interface featuring real-time spam prediction, confidence scores, prediction history, dark/light theme support, and an intuitive user experience.

---

## ✨ Features

- 📧 Email & SMS Spam Detection
- 🤖 Machine Learning using Multinomial Naive Bayes
- 📝 TF-IDF Text Vectorization
- 🧹 Natural Language Processing (NLP)
- 📊 Prediction Confidence Score
- ⚡ Prediction Time Display
- 📈 Word & Character Counter
- 📋 Copy Prediction Result
- 💬 Sample Spam & Safe Messages
- 🕒 Recent Prediction History
- 🌙 Dark & ☀️ Light Theme
- 💾 Theme Preference Memory
- 📱 Fully Responsive User Interface
- 🚫 Custom 404 Error Page
- 🔒 Input Validation & Security Enhancements

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Multinomial Naive Bayes
- TF-IDF Vectorizer

### Natural Language Processing
- NLTK
- Regular Expressions

### Data Processing
- Pandas
- NumPy

---

## 📂 Project Structure

```text
MailShield/
│
├── app/
│   └── app.py
│
├── dataset/
│
├── models/
│   ├── spam_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── src/
│   ├── train.py
│   ├── preprocess.py
│   ├── predict.py
│   └── evaluate.py
│
├── static/
│   ├── images/
│   ├── style.css
│   └── script.js
│
├── templates/
│   ├── index.html
│   └── 404.html
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/mailshield-ai-spam-detector.git
```

### 2. Navigate to the project directory

```bash
cd mailshield-ai-spam-detector
```

### 3. Create a virtual environment (Optional but Recommended)

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Flask application

```bash
python app/app.py
```

### 7. Open your browser

```text
http://127.0.0.1:5000
```

---

## 🧠 Machine Learning Workflow

1. Collect Dataset
2. Clean and Preprocess Text
3. Convert Text into TF-IDF Features
4. Train the Multinomial Naive Bayes Model
5. Save the Trained Model
6. Predict Spam or Ham
7. Display Confidence Score and Statistics

---

## 🔒 Security Features

- Input Validation
- Maximum Character Limit
- Secure Form Handling
- Security Headers
- Production-ready Configuration
- Theme Preference Stored Locally

---

## 📸 Screenshots

Screenshots will be added after deployment.

- 🏠 Home Page (Dark Theme)
- ☀️ Home Page (Light Theme)
- 🚨 Spam Detection Result
- ✅ Legitimate Message Result

---

## 🚀 Future Enhancements

- Deep Learning Models (LSTM/BERT)
- User Authentication
- Email Attachment Analysis
- Database Integration
- REST API
- Cloud Deployment
- Multi-language Spam Detection

---

## 👨‍💻 Author

**Inzila Danish Khan**

B.Tech Computer Science Engineering

Machine Learning & AI Enthusiast

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is developed for educational and learning purposes.