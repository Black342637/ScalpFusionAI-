# 🚀 ScalpFusion AI

ScalpFusion AI to open-source bot do scalpowania na giełdzie MEXC, łączący:
- Dane real-time z WebSocket
- Wskaźniki techniczne (RSI, MACD, MA)
- Moduł sentymentu (Grok mock + FinBERT placeholder)
- Decyzyjny silnik AI (prosty scoring)
- Dashboard w Streamlit

## 🔧 Wymagania

- Python 3.8+
- Klucze API do MEXC (opcjonalnie na start)
- `pip install -r requirements.txt`

## 🚀 Jak uruchomić

```bash
python main.py  # test danych i wskaźników
streamlit run dashboard/app.py  # dashboard frontend
