# 💊 Prescripto

**Prescripto** is an AI-powered assistant that transforms confusing medical prescriptions into a clear, actionable daily medication plan.

Built at Innovation Labs AI Hackathon 2026 by a team of 2nd-year Computer Science students from Cluj-Napoca.

---

## 🚀 What it does

1. Upload a photo of your medical prescription
2. AI reads and translates the medical jargon into plain language
3. Extracts drug names, dosages, and instructions
4. Generates a daily medication schedule
5. Syncs reminders to Google Calendar and WhatsApp

---

## 🛠️ Tech Stack

- **Frontend/UI:** Streamlit
- **AI:** Google Gemini API (gemini-1.5-flash)
- **OCR:** Gemini Vision
- **Drug Database:** Romanian medication nomenclature (CSV)
- **Disease Codes:** ICD PDF lookup
- **Notifications:** WhatsApp Business API, Google Calendar API

---

## ⚙️ Setup

1. Clone the repo
```bash
git clone https://github.com/username/prescripto.git
cd prescripto
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root folder
```
GEMINI_API_KEY=your_api_key_here
```

4. Run the app
```bash
streamlit run main.py
```

---

## 📁 Project Structure

```
prescripto/
├── main.py              # Streamlit UI
├── services/
│   ├── ai_service.py    # Gemini AI integration
│   └── data_service.py  # Drug DB & PDF lookup
├── utils/
│   └── config.py        # API key config
├── data/
│   ├── medicamente.csv  # Romanian drug database
│   └── coduri_boala.pdf # Disease code nomenclature
└── .env                 # API keys (not committed)
```

---

## ⚠️ Disclaimer

Prescripto is a productivity tool only. It translates and organizes prescription instructions — it does **not** provide medical advice, diagnoses, or recommendations. Always consult your doctor or pharmacist.

---

## 👥 Team

Built with ❤️ by **Mentolatii** @ Innovation Labs Cluj 2026
