import streamlit as st
import pandas as pd
from data.fetcher import fetch_mexc_klines
from indicators.technical import calculate_indicators
from trading.engine import decision_logic

st.set_page_config(page_title="ScalpFusion AI", layout="wide")

st.title("📊 ScalpFusion AI – Dashboard")

# Parametry użytkownika
symbol = st.text_input("Symbol", value="BTC/USDT")
timeframe = st.selectbox("Interwał", options=["1m", "5m", "15m"], index=0)
limit = st.slider("Liczba świec", 50, 200, 100)

# Pobieranie danych
df = fetch_mexc_klines(symbol=symbol, timeframe=timeframe, limit=limit)
df = calculate_indicators(df)

# Logika decyzji
df["decision"] = df.apply(decision_logic, axis=1)

# Wyświetlanie
st.subheader("📈 Wskaźniki i sygnały")
st.dataframe(df.tail(10))

buy_signals = df[df["decision"] == "BUY"]
sell_signals = df[df["decision"] == "SELL"]

st.success(f"💹 BUY sygnałów: {len(buy_signals)}")
st.error(f"📉 SELL sygnałów: {len(sell_signals)}")
