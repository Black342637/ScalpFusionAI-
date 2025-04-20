from data.fetcher import fetch_mexc_klines
from indicators.technical import calculate_indicators
from trading.engine import decision_logic
import pandas as pd

# Parametry strategii
TP = 0.01   # 1%
SL = 0.005  # 0.5%

def backtest():
    df = fetch_mexc_klines(limit=500)
    df = calculate_indicators(df)
    df["decision"] = df.apply(decision_logic, axis=1)

    trades = []
    position = None

    for i in range(1, len(df)):
        row = df.iloc[i]
        prev_row = df.iloc[i - 1]

        # Otwarcie pozycji
        if not position and row["decision"] == "BUY":
            position = {
                "entry_price": row["close"],
                "entry_index": i,
                "status": "open"
            }

        # Sprawdź TP/SL
        if position:
            entry = position["entry_price"]
            current_price = row["close"]
            if current_price >= entry * (1 + TP):
                position["exit_price"] = current_price
                position["result"] = "TP"
                trades.append(position)
                position = None
            elif current_price <= entry * (1 - SL):
                position["exit_price"] = current_price
                position["result"] = "SL"
                trades.append(position)
                position = None

    # Podsumowanie
    print("🧪 Wyniki backtestu:")
    print(f"Ilość transakcji: {len(trades)}")
    tp_count = sum(1 for t in trades if t["result"] == "TP")
    sl_count = sum(1 for t in trades if t["result"] == "SL")
    print(f"TP: {tp_count} | SL: {sl_count}")
    if trades:
        winrate = round(tp_count / len(trades) * 100, 2)
        print(f"Skuteczność: {winrate}%")

if __name__ == "__main__":
    backtest()
