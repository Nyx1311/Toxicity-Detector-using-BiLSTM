import streamlit as st
import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow.keras.layers import TextVectorization
from datetime import datetime
import random
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

# === PAGE CONFIG ===
st.set_page_config(page_title="Toxicity Detection + Healing Toolkit", layout="wide")

# === CUSTOM CSS FOR SIDEBAR ===
sidebar_image_path = "C:/Users/neelu/OneDrive/Desktop/download-removebg-preview.png"

st.markdown(f"""
    <style>
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #2b2a4c, #3e326f, #5a4fcf);
        padding-top: 1rem;
        border-right: 3px solid #8e8cf0;
        box-shadow: 4px 0 15px rgba(90, 79, 207, 0.4);
    }}
    .sidebar-button button {{
        background-color: #5a4fcf !important;
        color: white !important;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        margin-top: 10px;
        transition: all 0.3s ease;
    }}
    .sidebar-button button:hover {{
        box-shadow: 0 0 12px #ffffffaa;
        transform: scale(1.03);
    }}
    .sparkle {{
        animation: sparkle 1.2s ease-out forwards;
        font-size: 18px;
        padding-top: 10px;
        color: #ff66cc;
    }}
    @keyframes sparkle {{
        0% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.5; transform: scale(1.2); }}
        100% {{ opacity: 0; transform: scale(0.8); }}
    }}
    </style>
""", unsafe_allow_html=True)

# ---------- Session State ----------
if 'show_vent_box' not in st.session_state:
    st.session_state.show_vent_box = False
if 'vented' not in st.session_state:
    st.session_state.vented = False

# === SIDEBAR ===
import streamlit as st
import base64
import os

# ===== Session State Initialization =====
if 'show_vent_box' not in st.session_state:
    st.session_state.show_vent_box = False
if 'vented' not in st.session_state:
    st.session_state.vented = False
if 'toolkit_open' not in st.session_state:
    st.session_state.toolkit_open = False

# ===== Helper to Convert Image to Base64 =====
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# ===== Load Image =====
img_base64 = get_image_base64("download-removebg-preview.png")

# ===== Sidebar Layout and Styling =====
import streamlit as st
import base64
import os

# ===== Session State Initialization =====
if 'show_vent_box' not in st.session_state:
    st.session_state.show_vent_box = False
if 'vented' not in st.session_state:
    st.session_state.vented = False
if 'toolkit_open' not in st.session_state:
    st.session_state.toolkit_open = False

# ===== Convert Local Image to Base64 =====
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# ✅ Your actual image path
image_path = r"C:\Users\neelu\OneDrive\Desktop\Comment-Toxicity-Classifier-using-BiLSTM-1\download-removebg-preview.png"
img_base64 = get_image_base64(image_path)

# ===== Sidebar Layout and Styling =====
with st.sidebar:
    st.markdown(
        f"""
        <style>
        .sidebar-button button {{
            font-weight: bold;
            font-size: 16px;
            padding: 14px 28px;
            border-radius: 12px;
            margin: 10px 0;
            width: 100%;
            border: none;
        }}

        .vent-btn button {{
            background-color: #6C5CE7 !important;  /* Violet */
            color: white !important;
        }}

        .toolkit-btn button {{
            background-color: #55efc4 !important;  /* Soft teal */
            color: black !important;
        }}

        /* Fix image inside the sidebar */
        .sidebar-image {{
            margin-top: auto;
            padding-top: 30px;
            width: 100%;
            display: flex;
            justify-content: center;
        }}
        .sidebar-image img {{
            max-width: 100%;
            border-radius: 15px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sidebar Title
    st.markdown('<h3 style="margin-bottom:5px;"><em>💜 Safe Space Control</em></h3>', unsafe_allow_html=True)

    # Vent Box Button
    st.markdown('<div class="sidebar-button vent-btn">', unsafe_allow_html=True)
    if st.button("💜 Vent Box", key="toggle_button_sidebar"):
        st.session_state.show_vent_box = not st.session_state.show_vent_box
        st.session_state.vented = False
    st.markdown('</div>', unsafe_allow_html=True)

    # Healing Toolkit Button
    # Healing Toolkit Button (moved inside sidebar)
    st.markdown('<div class="sidebar-button toolkit-btn">', unsafe_allow_html=True)
    if st.button("💖 Healing Toolkit", key="toggle_toolkit"):
        st.session_state.toolkit_open = not st.session_state.toolkit_open
    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.toolkit_open:
        st.markdown("## 💖 Healing Toolkit for Women")

        # Updated Articles
        st.markdown("### 📚 Articles")
        article_links = [
            ("Times of India – 5 Classic Signs of a Narcissist & What to Do", "https://timesofindia.indiatimes.com/life-style/relationships/work/5-classic-signs-of-a-narcissist-how-to-spot-them-and-what-to-do/photostory/121831207.cms"),
            ("Worldcrunch – 'My Mother Is a Narcissist' — How Adult Daughters Can Heal", "https://worldcrunch.com/in-the-news/narcissistic-mother-daughter-recovery/"),
            ("Time – How to Deal With a Narcissist (Feb 2025)", "https://time.com/7213814/how-to-deal-with-narcissists/"),
            ("VeryWellMind – Yes, You Can Safely Leave a Narcissist", "https://www.verywellmind.com/how-to-leave-a-narcissist-8706872"),
        ]
        for title, url in article_links:
            st.markdown(f"- [{title}]({url})")

        # Updated YouTube Talks
        st.markdown("### 🎥 Empowering YouTube Talks")
        video_links = [
            ("10 Signs Of A Female Narcissist: Hidden Traits", "https://www.youtube.com/watch?v=_su7HD_WZDs"),
            ("How to Deal with Narcissists", "https://www.youtube.com/watch?v=oiG32O71wF4"),
            ("10 Tactics Female Covert Narcissist Use to Keep You HOOKED", "https://www.youtube.com/watch?v=Vi7n4--cUO8"),
        ]
        for title, url in video_links:
            st.markdown(f"- [{title}]({url})")

    # ✅ Sidebar image should always show
    if img_base64:
        st.markdown(f"""
            <div class="sidebar-image">
                <img src="data:image/png;base64,{img_base64}">
            </div>
        """, unsafe_allow_html=True)



# === MAIN TITLE ===
st.markdown("""
    <h1 style='text-align: center; font-size: 2.5em; color: white;'>🧭 Toxicity Detection</h1>
""", unsafe_allow_html=True)
st.markdown("""
    <h5 style='text-align: center; color: #e74c3c; font-family: Georgia, serif;'>
     <i>🎀 Detecting Cute Little Red Flags 🎀</i>
    </h5>
""", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; font-size:17px; font-weight:600; margin-bottom: 20px;'>
        This tool flags toxic comments and shows a popup if more than 1 toxic trait is detected.
    </div>
""", unsafe_allow_html=True)

# === LOAD MODEL AND VECTORIZER ===
@st.cache_resource
def load_model_and_vectorizer():
    model = tf.keras.models.load_model('model_epoch_30.h5')
    df = pd.read_csv('data_final.csv')
    text_data = df['comment']
    vectorizer = TextVectorization(max_tokens=200000, output_sequence_length=1800, output_mode='int')
    vectorizer.adapt(text_data.values)
    label_names = ['toxic', 'severe_toxic', 'threat', 'insult', 'identity_hate', 'gaslight', 'manipulation']
    return model, vectorizer, label_names

model, vectorizer, label_names = load_model_and_vectorizer()
thresholds = np.array([0.45, 0.60, 0.55, 0.50, 0.60, 0.50, 0.45])

# === ANALYSIS ===
if 'history' not in st.session_state:
    st.session_state.history = []
comment = st.text_area("💬 Enter a comment to analyze:", height=100)

if st.button("Analyze"):
    if not comment.strip():
        st.warning("🧭 Please enter a valid comment.")
    else:
        # === Vectorize + Predict ===
        input_vector = vectorizer([comment])
        preds = model.predict(input_vector)[0]
        triggered = [label_names[i] for i, val in enumerate(preds) if val > thresholds[i]]
        
        # Save to history
        st.session_state.history.append((comment, triggered))
        if len(st.session_state.history) > 5:
            st.session_state.history = st.session_state.history[-5:]


    label_display_map = {
            "toxic": "🌋 General Toxicity", "severe_toxic": "💣 Severe Toxicity",
            "threat": "🚨 Threatening Behavior", "insult": "🔯 Insulting Language",
            "identity_hate": "🧠 Identity-Based Hate", "gaslight": "🔮 Gaslighting Tactics",
            "manipulation": "🎭 Manipulative Behavior"
        }

        
       # === Display only if preds exists and is valid ===
if 'preds' in locals() and preds is not None and len(preds) > 0:
    st.markdown("### 🧪 Prediction Result")

    values = []
    count_1_to_5 = sum(1 for p in preds if 0.01 < p < 0.05)

    # Case 1: Only one label in 1%–5% range
    if count_1_to_5 == 1:
        for i, label in enumerate(label_names):
            display_label = label_display_map.get(label, label)
            if 0.01 < preds[i] < 0.05:
                result = "✅ True"
            else:
                result = "❌ False"
            st.markdown(
                f"<div style='font-size:16px; margin-left:10px; color:white'>{display_label} → <b>{result}</b></div>",
                unsafe_allow_html=True
            )
            values.append(preds[i])

    else:
        # Default threshold logic
        triggered = []
        for i, label in enumerate(label_names):
            display_label = label_display_map.get(label, label)
            result = "✅ True" if preds[i] >= thresholds[i] else "❌ False"
            if preds[i] >= thresholds[i]:
                triggered.append(display_label)
            st.markdown(
                f"<div style='font-size:16px; margin-left:10px; color:white'>{display_label} → <b>{result}</b></div>",
                unsafe_allow_html=True
            )
            values.append(preds[i])

        if not any(preds >= thresholds):
            st.info("No toxicity detected.")
        if len(triggered) > 1:
            components.html("""<script>alert("🚨 Girl YOU DESERVE BETTER!");</script>""", height=0, width=0)

    # === Visualization ===
    st.markdown("### 📈 Toxicity Scores Visualization")
    fig, ax = plt.subplots(figsize=(8, 4), facecolor='#000000')
    ax.barh(label_names, values, color='red')
    ax.set_xlim([0, 1])
    ax.set_facecolor('#000000')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.set_yticklabels(label_names, color='white')
    for i, v in enumerate(values):
        ax.text(v + 0.01, i, f"{v * 100:.1f}%", color='white', fontweight='bold', va='center')
    for spine in ax.spines.values():
        spine.set_visible(False)
    st.pyplot(fig)

    # === Low-confidence override visualization ===
    low_prob_indices = [i for i, p in enumerate(preds) if 0.01 < p < 0.05]
    if len(low_prob_indices) == 1:
        i = low_prob_indices[0]
        display_label = label_display_map.get(label_names[i], label_names[i])
        st.markdown(f"<div style='font-size:16px; margin-left:10px; color:yellow'>⚠️ {display_label} → <b>✅ True (Low confidence override)</b></div>", unsafe_allow_html=True)

if st.session_state.history:
    st.markdown("---")
    st.subheader("🕘 Last 5 Analyzed Comments")
    for i, (prev_comment, prev_labels) in enumerate(reversed(st.session_state.history), 1):
        label_text = ", ".join(prev_labels) if prev_labels else "No toxicity"
        st.markdown(f"<div style='padding-left:10px; color:white'><b>{i}.</b> <i>{prev_comment}</i> → <b>Labels:</b> {label_text}</div>", unsafe_allow_html=True)

# === VENT BOX ===
if st.session_state.show_vent_box:
    st.title("💬 Safe Venting Space")
    st.markdown("Write whatever you're feeling. This space is just for you. Nothing will be saved or judged.")

    if not st.session_state.vented:
        # Text area for venting
        vent_input = st.text_area("Start venting here...", height=300, max_chars=15000, key="vent_input")

        # Button to submit
        if st.button("Vent & Let Go", key="vent_button"):
            st.session_state.vented = True

    else:
        # Show message only — no input box or button
        st.markdown('<div class="sparkle">✨ Vent text cleared...</div>', unsafe_allow_html=True)
        st.success("❤️ You have vented successfully. Take a deep breath — you're doing amazing!")

# === AFFIRMATIONS ===
affirmations = [
    "🎀 You are worthy of love, exactly as you are.",
    "🌷 Your presence in this world matters, even on days you feel invisible.",
    "🔥 The fact that you’re still standing, still trying, is a strength unmatched.",
    "💖 Healing is not linear, and it’s okay to take your time.",
    "😭 You are not a burden for having emotions, you are beautifully human.",
    "💅 Kindness, especially toward yourself, is never wasted.",
    "🕊 You deserve peace, even if your mind tells you otherwise.",
    "✨ You are not your mistakes — you are your resilience.",
    "🌼 You are allowed to start over, again and again.",
    "📖 Your story has power, even if it’s messy or unfinished.",
    "🧳 Being soft is not weak; it’s a form of brave.",
    "❤ Every part of you, even the broken parts, are deserving of love.",
    "👑 Your self-worth is not tied to productivity or perfection.",
    "💫 There is no one like you, and that is your superpower.",
    "🌙 You are doing the best you can with what you have — and that’s enough.",
    "🌺 Self-love doesn’t mean you’re always happy. It means you’re always worthy.",
    "🎠 You don’t need to earn rest, joy, or forgiveness.",
    "🔮 Even in silence, your soul is speaking — be gentle and listen.",
    "📈 Progress is progress, no matter how small.",
    "🌈 You’ve made it through every dark day so far — that’s a 100% survival rate."
]
colors = [
    "#FFC0CB", "#E6E6FA", "#F0E68C", "#D8BFD8", "#FFDAB9", "#B0E0E6",
    "#FFFACD", "#FFE4E1", "#F5DEB3", "#E0FFFF", "#FFD700", "#C0C0C0",
    "#FFB6C1", "#F8C8DC", "#E0BBE4", "#FFEBCD", "#FADADD", "#E1F5FE"
]
js_sentences = str(affirmations).replace("'", '"')
js_colors = str(colors).replace("'", '"')
components.html(f"""
<div id=\"rotating-container\" style=\"text-align:center; margin-top: 60px;\">
    <h4 style=\"color:#ffaaff;\">🌈 Sass & Soul Affirmation 🌈</h4>
    <div id=\"affirmation\" onclick=\"copyAffirmation()\" style=\"cursor:pointer; font-size:18px; font-style:italic; font-family: 'Georgia', cursive, serif;
            font-weight:400; color:#fff; padding:14px 22px; border-radius:14px; background-color:#2a2a2a; 
            display:inline-block; max-width:80%; transition: all 0.3s ease;\">
        Click to receive a sweet whisper of strength 💝
    </div>
    <div id=\"copied-msg\" style=\"font-size:12px; margin-top:6px; color:lightgreen; display:none;\">✨ Copied to clipboard!</div>
</div>
<script>
    const sentences = {js_sentences};
    const colors = {js_colors};
    let currentIndex = 0;
    function rotateSentence() {{
        const box = document.getElementById("affirmation");
        const msg = document.getElementById("copied-msg");
        currentIndex = (currentIndex + 1) % sentences.length;
        box.innerText = sentences[currentIndex];
        box.style.color = colors[Math.floor(Math.random() * colors.length)];
        msg.style.display = "none";
    }}
    function copyAffirmation() {{
        navigator.clipboard.writeText(sentences[currentIndex]);
        document.getElementById("copied-msg").style.display = "block";
    }}
    rotateSentence();
    setInterval(rotateSentence, 5000);
</script>
""", height=260)  