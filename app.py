import streamlit as st
from textblob import TextBlob
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import random
from pandas.errors import EmptyDataError
from PIL import Image
import os
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

user_email = "guest@example.com"

QUOTES = {
    "great😆": [
        "Keep up the great energy!",
        "Your vibe attracts your tribe!",
        "Good vibes only, and you’re full of them!",
        "Your energy lights up the room!",
        "Smiles look great on you—keep wearing them!",
    ],
    "good🙂": [
        "Today feels steady, and that’s something to celebrate.",
        "Even on the calm days, your energy matters.",
        "You're doing well—keep leaning into the light.",
        "Good days build strong foundations—enjoy this one.",
        "You don’t have to be glowing to be growing.",
    ],
    "neutral😐": [
        "Every day won't be exciting, and that's okay.",
        "Steady is strong.",
        "Keep going, you're doing fine.",
        "Neutral isn’t empty—it’s space to reset and rise.",
        "You don’t need to feel amazing to keep moving forward.",
    ],
    "bad😕": [
        "It’s okay to have hard days—just don’t unpack and stay there.",
        "This moment doesn’t define you—better ones are still coming.",
        "Even tough days pass—your strength won’t.",
        "You’ve made it through 100% of your worst days—keep going.",
        "Some days surviving is enough—and that’s a win, too.",
    ],
    "terrible🙁": [
        "It's okay to feel off — tomorrow is a fresh start.",
        "Be kind to yourself today.",
        "Storms make trees take deeper roots.",
        "Breathe. This day will end, and you will still be here.",
        "Even when everything hurts, you are not alone.",
    ],
}


def analyze_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.3:
        mood = "great😆"
    elif polarity < -0.3:
        mood = "terrible🙁"
    elif 0.1 < polarity <= 0.3:
        mood = "good🙂"
    elif -0.3 <= polarity < -0.1:
        mood = "bad😕"
    else:
        mood = "neutral😐"
    return mood, polarity


def log_entry(entry: str, mood: str, polarity: float) -> None:
    filename = f"journal_{user_email}.csv"
    columns = ["timestamp", "entry", "mood", "polarity"]

    try:
        df = pd.read_csv(filename)
    except (FileNotFoundError, EmptyDataError):
        df = pd.DataFrame(columns=columns)

    new_row = pd.DataFrame([{
        "timestamp": datetime.datetime.now(),
        "entry": entry,
        "mood": mood,
        "polarity": polarity
    }])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(filename, index=False)


def load_log():
    filename = f"journal_{user_email}.csv"
    try:
        df = pd.read_csv(filename)
        return df
    except:
        return pd.DataFrame(columns=["timestamp", "entry", "mood", "polarity"])


def clear_user_data():
    filename = f"journal_{user_email}.csv"
    if os.path.exists(filename):
        os.remove(filename)



image_path = os.path.join("images", "logo.png")
if os.path.exists(image_path):
    st.image(image_path, width=200)

st.title("MoodiJournal📓")
st.write("Welcome to MoodiJournal, a safe space to write about your day or your feelings throughout the day and assess your mood from a neutral perspective. "
         "Log your mood and content from your journal for you to reflect on and receive a special message based off of your mood to either support or enhance your day.")
st.write("Happy Journalling!!!🌸")
st.subheader("Write about your day and get insights on your mood.✍🏻")

def clear_entry():
    st.session_state["entry"] = ""

entry = st.text_area("How are you feeling today?🙂", height=200, key="entry")

col1, col2 = st.columns(2)
with col1:
    if st.button("Analyze My Mood"):
        if entry.strip():
            mood, polarity = analyze_mood(entry)
            log_entry(entry, mood, polarity)
            st.success(f"Detected mood: **{mood.capitalize()}** (Score: {polarity:.2f})")
            st.info(random.choice(QUOTES[mood]))
        else:
            st.warning("Please write something first.")
with col2:
    st.button("Clear text", on_click=clear_entry)

df = load_log()
if not df.empty and 'timestamp' in df.columns:
    st.subheader("Let's have a look at your mood over time📈")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    plt.figure(facecolor="slategray")
    ax = plt.gca()
    ax.set_facecolor("slategray")
    plt.plot(df['timestamp'], df['polarity'], marker='o', color='black')
    plt.axhline(0, color='gray', linestyle='--')
    plt.title("Mood Polarity Trend")
    plt.xticks(rotation=45)
    plt.ylabel("Polarity")
    plt.tight_layout()
    st.pyplot(plt)
else:
    st.info("No mood entries yet. Start journaling!")

if st.button("🛑 Delete all journal entries", key="clear_data"):
    clear_user_data()
    st.rerun()
    st.success("Your journal data has been cleared for today!")
    if st.button("🛑 Delete all journal entries", key="clear_data"):
        clear_user_data()
        st.rerun()
        st.success("Your journal data has been cleared for today!")
