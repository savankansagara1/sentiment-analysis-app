# Sentiment Analyzer 💬

A machine learning-powered web application that predicts the emotional tone of text input. Built with Streamlit and scikit-learn.

---

## 🌟 Features

- Real-time sentiment prediction (joy, sadness, anger, love, fear, surprise)
- Interactive and intuitive interface
- Emoji-enhanced results and color-coded feedback
- Responsive design for all devices
- Secure and private (no data storage)

---

## 🛠️ Technologies Used

- **Frontend:** Streamlit
- **Backend:** Python
- **Machine Learning:**  
  - scikit-learn  
  - SVM Classifier  
  - Text Vectorization (e.g., TF-IDF)
- **Data Processing:** Pandas, NLTK
- **Model Serialization:** Joblib

---

## 📝 Input

- Any English sentence or phrase

---

## 🚀 Live Demo

Try the live application: **[Sentiment Analyzer App](https://sentimentchecker.streamlit.app/)**

---

## 💻 Local Development

**Clone the repository**
```sh
git clone https://github.com/savankansagara1/sentiment-analysis-app.git
cd sentiment-analysis-app
```

**Install dependencies**
```sh
pip install -r requirements.txt
```

**Run the application**
```sh
streamlit run app.py
```

---

## 📁 Project Structure

```
sentiment-analysis-app/
├── app.py                # Main Streamlit application
├── requirements.txt      # Project dependencies
├── svm_model.pkl         # Trained SVM model
├── vectorizer.pkl        # Text vectorizer
└── README.md             # Project documentation
```

---

## 🔑 Model Details

- **Algorithm:** Support Vector Machine (SVM)
- **Accuracy:** ~88% on test data
- **Classes:** Joy, Sadness, Anger, Love, Fear, Surprise
- **Output:** Predicted emotion label

---

## 👨‍💻 Developer

**Savan Kansagara**  
📧 important.savan@gmail.com  
💼 [LinkedIn Profile](https://www.linkedin.com/in/savan-kansagara/)

---

## ⚠️ Disclaimer

This tool is for educational purposes only and should not be used as a substitute for professional psychological advice, diagnosis, or treatment.

---

Made with ❤️ by Savan Kansagara
