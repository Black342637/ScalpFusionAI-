from data.fetcher import fetch_mexc_klines
from indicators.technical import calculate_indicators
from ai.scoring import calculate_ai_score
import pandas as pd

def main():
    df = fetch_mexc_klines(limit=100)
    if df.empty:
        print("Brak danych – przerwano.")
        return

    df = calculate_indicators(df)

    latest = df.iloc[-1]
    confidence, score = calculate_ai_score(
        latest['RSI_14'],
        latest['MACD_12_26_9'],
        latest['MA_fast'],
        latest['MA_slow']
    )

    print(f"\nAI Score: {score} | Confidence: {confidence:.2f}%")

    if confidence > 70:
        decision = "BUY"
    elif confidence < 30:
        decision = "SELL"
    else:
        decision = "HOLD"

    print(f"Decyzja bota: {decision}")
