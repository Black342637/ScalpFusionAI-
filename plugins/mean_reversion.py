# plugins/mean_reversion.py

def generate_signal(df):
    """
    Strategia Mean Reversion:
    Kupuj, gdy cena jest znacznie poniżej średniej (z 20 świec), sprzedawaj gdy powyżej.
    """
    if len(df) < 20:
        return "Za mało danych"

    current_price = df["close"].iloc[-1]
    moving_average = df["close"].iloc[-20:].mean()

    if current_price < 0.97 * moving_average:
        return "BUY – Odbicie od dna 🔄"
    elif current_price > 1.03 * moving_average:
        return "SELL – Nadmierne wykupienie 🔻"
    else:
        return "HOLD – Blisko średniej"
