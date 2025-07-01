# MoodiJournal Mood Journal Streamlit Project first Streamlit project 
# MoodiJournal

**MoodiJournal** is a Streamlit-based web application that helps users reflect on their emotional well-being through journaling. The app analyzes sentiment in journal entries, categorizes the mood, displays historical mood trends, and provides motivational messages based on the detected mood.

---

## Features

- **Google Sign-In Authentication**  
  Secure login using your Google account.

- **Sentiment Analysis**  
  Automatically analyzes text using `TextBlob` to determine emotional tone.

- **Mood Categorization**  
  Entries are classified as Great, Good, Neutral, Bad, or Terrible based on sentiment polarity scores.

- **Personalized Quotes**  
  Receive a tailored supportive or uplifting quote depending on your mood.

- **Mood Trend Visualization**  
  Graph your mood over time to track patterns and reflect on emotional health.

- **Journal Persistence**  
  Entries are saved in a CSV file named uniquely for each user.

- **Data Management**  
  Option to delete all journal entries with a single click.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/moodijournal.git
   cd moodijournal
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   streamlit run app.py
   ```

---

## Dependencies

- streamlit  
- textblob  
- pandas  
- matplotlib  
- Pillow  

Install them using:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
moodijournal/
├── app.py
├── requirements.txt
├── images/
│   └── logo.png
├── journal_<user_email>.csv
```

---

## Usage

1. Launch the app with `streamlit run app.py`.
2. Sign in with your Google account.
3. Write your journal entry in the text area.
4. Click **"Analyze My Mood"** to analyze and log your entry.
5. View your mood classification and receive a related quote.
6. Check your mood trends over time using the visual chart.
7. Use the delete button to clear all journal data if needed.

---

## Notes

- Polarity values range from -1 (most negative) to +1 (most positive).
- Journals are saved as `journal_<user_email>.csv` in the root directory.
- The mood detection is based on simple threshold logic applied to polarity scores.

---

## License

This project is licensed under the MIT License.
