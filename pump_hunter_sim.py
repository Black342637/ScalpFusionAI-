# Pump Hunter Bot code placeholder
import os
from dotenv import load_dotenv
import requests

load_dotenv()
MEXC_API_KEY= "mx0vglZxoV3JnOlZiW"
MEXC_SECRET_KEY= "8b1f01332b4b4019b877b76221522b34"
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def telegram_send(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=payload)
    return response.status_code

# Przykład użycia (test)
if __name__ == "__main__":
    msg = msg = r"✅ Pump Hunter aktywny!\nWitaj Feniksie 🔥\nBot gotowy do łowienia pomp 💸"


    status = telegram_send(msg)
    print(f"Status: {status}")