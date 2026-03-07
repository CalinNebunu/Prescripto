import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Permisiunea de a citi și scrie evenimente în calendar
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

# Aici e ID-ul calendarului tău partajat "Prescripto"
CALENDAR_ID = '15cfc6384cc7449a766e7b65b36d62edc7f928b0e61becf707f4d2d8ea66ab79@group.calendar.google.com'


def get_calendar_service():
    """Autentifică utilizatorul și returnează serviciul Google Calendar."""
    creds = None

    # Verifică dacă ne-am mai logat înainte (salvează un token.json)
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # Dacă nu avem token sau e expirat, deschidem browserul pentru login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            # Deschide o fereastră de browser ca să te loghezi cu Gmail-ul tău
            creds = flow.run_local_server(port=0)

        # Salvăm token-ul generat ca să nu ne mai ceară logarea și a doua oară
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)


def add_meds_to_calendar(medicamente_confirmate):
    """Primește lista de medicamente din Streamlit și le adaugă în calendar pentru MÂINE."""
    service = get_calendar_service()

    # Setăm data pentru MÂINE (perfect pentru testare/demo la hackathon)
    maine = datetime.date.today() + datetime.timedelta(days=1)

    evenimente_create = 0

    for med in medicamente_confirmate:
        nume = med.get("nume", "Medicament necunoscut")
        doza = med.get("doza", "")
        instructiuni = med.get("instructiuni", "")
        ore = med.get("ore", [])

        for ora in ore:  # De exemplu: "08:00"
            # Construim formatul de dată cerut de Google (ISO 8601)
            start_time = f"{maine}T{ora}:00"

            # Calculăm sfârșitul evenimentului (presupunem că durează 15 minute)
            timp_start = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
            timp_end = timp_start + datetime.timedelta(minutes=15)
            end_time = timp_end.strftime("%Y-%m-%dT%H:%M:%S")

            event = {
                'summary': f'💊 Prescripto: Ia {nume} ({doza})',
                'description': f'Instrucțiuni: {instructiuni}',
                'start': {
                    'dateTime': start_time,
                    'timeZone': 'Europe/Bucharest',
                },
                'end': {
                    'dateTime': end_time,
                    'timeZone': 'Europe/Bucharest',
                },
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                        {'method': 'popup', 'minutes': 10},  # Dă notificare pe telefon cu 10 min înainte
                    ],
                },
            }

            # Trimitem evenimentul în calendarul tău specific
            service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
            evenimente_create += 1

    return evenimente_create