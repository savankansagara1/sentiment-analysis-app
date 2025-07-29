import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("svm_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Emotion and color mapping (with emojis!)
label_mapping = {
    0: ("sadness", "😢", "#5D8AA8"),      # blue-gray
    1: ("anger", "😠", "#D7263D"),        # strong red
    2: ("love", "❤️", "#FF6F91"),         # soft pink
    3: ("surprise", "😲", "#FFD166"),     # bright yellow
    4: ("fear", "😨", "#3D348B"),         # deep indigo
    5: ("joy", "😊", "#43AA8B"),          # vibrant green
}

def get_emotion_label(index):
    return label_mapping.get(index, ("Unknown", "❓", "#007bff"))

# --- Custom Styles (minimal but modern) ---
st.markdown("""
    <style>
    .main-title {
        font-size:2.2rem;
        font-weight:bold;
        text-align:center;
        color:#4a4e69;
        margin-top: 1.5rem;
    }
    .subtitle {
        color:#7678ed;
        text-align:center;
        margin-bottom:1.5rem;
        font-size:1.1rem;
    }
    .result-box {
        padding:1.2rem 0.5rem;
        margin:1.5rem 0;
        font-size:1.5rem;
        text-align:center;
        border-radius:18px;
        font-weight:600;
        color:#fff;
        box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);
        transition: background 0.3s;
        word-break: break-word;
    }
    .contact {
        margin-top:2.5rem;
        text-align:center;
        color:#444444;
        font-size:1rem;
        word-break: break-word;
    }
    .stTextArea textarea {
        font-size:1.1rem;
        min-height: 100px;
        border-radius: 10px;
        padding: 0.7rem;
    }
    .emotion-guide {
        margin:1rem 0;
        text-align:center;
        font-size:1.05rem;
        color: #495057;
        background: #f8f9fa;
        border-radius: 10px;
        padding: 0.5rem 0.2rem;
        box-shadow: 0 2px 8px 0 rgba(0,0,0,0.03);
        word-break: break-word;
    }
    @media (max-width: 600px) {
        .main-title { font-size: 1.4rem; }
        .subtitle { font-size: 0.95rem; }
        .result-box { font-size: 1.1rem; padding: 0.8rem 0.2rem; }
        .emotion-guide { font-size: 0.95rem; padding: 0.4rem 0.1rem; }
        .contact { font-size: 0.95rem; }
    }
    </style>
""", unsafe_allow_html=True)

# --- UI Layout ---
st.markdown('<div class="main-title">🧠 Sentiment Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Type your sentence below to analyze its emotional tone.</div>', unsafe_allow_html=True)

user_input = st.text_area("Your Text", placeholder="Type a sentence (e.g., 'I feel awesome today!')")
if st.button("🔍 Analyze"):
    if not user_input.strip():
        st.warning("Please enter text to analyze.")
    else:
        input_vec = vectorizer.transform([user_input])
        pred = model.predict(input_vec)
        emotion, emoji, color = get_emotion_label(int(pred[0]))

        st.markdown(
            f'<div class="result-box" style="background:{color};">'
            f'{emoji}  <b>{emotion.capitalize()}</b>'
            f'</div>', unsafe_allow_html=True
        )

        st.markdown(
            f'<div style="text-align:center;"><i>Input:</i> "{user_input}"</div>',
            unsafe_allow_html=True
        )

# --- Simple Emotion Guide ---
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown(
    '<div class="emotion-guide">'
    '<b>Emotion Guide:</b><br>'
    '😊 <b>Joy</b> &nbsp; | &nbsp; 😢 <b>Sadness</b> &nbsp; | &nbsp; 😠 <b>Anger</b> &nbsp; | &nbsp; ❤️ <b>Love</b> &nbsp; | &nbsp; 😨 <b>Fear</b> &nbsp; | &nbsp; 😲 <b>Surprise</b>'
    '</div>', unsafe_allow_html=True
)

# --- Contact Info ---
st.markdown(
    '<div class="contact">'
        '<b>Contact:</b> '
        '<a href="mailto:important.savan@gmail.com">important.savan@gmail.com</a> &nbsp;|&nbsp; '
    '<a href="https://www.linkedin.com/in/savan-kansagara" target="_blank">LinkedIn</a>'
    '<br><span style="font-size:0.95em; color:#888;">© 2025 Savan</span>'
    '</div>', unsafe_allow_html=True
)
