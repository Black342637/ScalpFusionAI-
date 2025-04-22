import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ai.scoring import calculate_ai_score

from data.fetcher import fetch_mexc_klines
from indicators.technical import calculate_indicators

st.set_page_config(page_title="ScalpFusion AI Dashboard", layout="wide")
st.title("ScalpFusion AI - Live Trading Dashboard")

df = fetch_mexc_klines(limit=100)
if df.empty:
    st.warning("Brak danych z MEXC")
else:
    df = calculate_indicators(df)
    df[["confidence", "score"]] = df.apply(
        lambda row: pd.Series(calculate_ai_score(
            row["RSI_14"], row["MACD_12_26_9"], row["MA_fast"], row["MA_slow"]
        )), axis=1)

    st.dataframe(df.tail(20)[["timestamp", "close", "RSI_14", "MACD_12_26_9", "MA_fast", "MA_slow", "confidence"]])
    st.line_chart(df.set_index("timestamp")["close"], height=300)
    st.line_chart(df.set_index("timestamp")["confidence"], height=200)
