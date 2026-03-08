# 💊 Prescripto

**Prescripto** is the complete AI assistant that reads, translates, and schedules treatments instantly.

Built @ Innovation Labs AI Hackathon 2026 by a team of 2nd-year Computer Science students from Cluj-Napoca.

---

## 🚀 What it does

1. Upload a photo of your medical prescription
2. AI reads and translates the medical jargon into plain language
3. Extracts drug names, dosages, and instructions
4. Generates a daily medication schedule
5. Syncs reminders directly to Google Calendar (WhatsApp automated alerts for caregivers are currently in development 🚧)

---

## 🛠️ Tech Stack

- **Frontend/UI:** Streamlit
- **AI:** Google Gemini API (gemini-flash-latest) for fast, multimodal reasoning.
- **OCR:** Gemini Vision (Handwriting decryption)
- **Data Validation:** Local lookups against Romanian medication nomenclature (CSV) and official ICD disease codes (PDF).
- **Disease Codes:** ICD PDF lookup
- **Integrations:** Google Calendar API.
- **Planned Integrations:** WhatsApp Business API (WIP).

---

## ⚙️ Setup

1. Clone the repo
```bash
git clone https://github.com/CalinNebunu/Prescripto.git
cd Prescripto
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root folder
```
GEMINI_API_KEY=your_gemini_api_key_here
WHATSAPP_API_TOKEN=your_whatsapp_token_here
# Note: Google Calendar API requires a credentials.json file downloaded from Google Cloud Console.
```

4. Run the app
```bash
streamlit run main.py
```

---

## 📁 Project Structure

```
## 📁 Project Structure

```text
Prescripto/
├── data/
│   ├── coduri_boala.pdf         # ICD Disease code nomenclature
│   ├── medicamente.csv          # Romanian drug database nomenclature
│   ├── IMG_20260307_102240.jpg  # Test prescription image
│   └── IMG_20260307_102254.jpg  # Test prescription image
├── services/
│   ├── ai_service.py            # Gemini AI integration & prompt engineering
│   ├── calendar_service.py      # Google Calendar API integration
│   └── data_service.py          # Local DB & PDF data extraction
├── utils/
│   ├── __init__.py
│   └── config.py                # Configuration and env variables loader
├── .env                         # API keys (Not tracked by Git)
├── .gitignore                   # Specifies intentionally untracked files
├── credentials.json             # Google Calendar API credentials
├── token.json                   # Google Calendar saved auth token
├── main.py                      # Main Streamlit UI application
├── README.md                    # Project documentation
├── requirements.txt             # Python project dependencies
├── test_api.py                  # Local API testing script
├── leanv3.png                   # Lean Canvas image
└── Prescripto.pdf               # Pitch deck presentation
```

---

## ⚠️ Disclaimer

**Prescripto is a productivity and accessibility tool only.** It translates and organizes prescription instructions to improve medication adherence. It does **not** provide medical advice, diagnoses, or treatment recommendations. Always consult your doctor or pharmacist regarding your health and medication.

---

## 👥 Contributors (Team Mentolații)

Built with ❤️ at Innovation Labs Cluj 2026 by:

* **Bedea Călin** - [GitHub Profile](https://github.com/CalinNebunu)
* **Trofin Alissia** - [GitHub Profile](https://github.com/trofinalissia98)
* **Tîrcob Alina** - [GitHub Profile](https://github.com/alinatircob)
* **Bota Luca** - [GitHub Profile](https://github.com/Lapt1c)
