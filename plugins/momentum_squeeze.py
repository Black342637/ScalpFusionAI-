# plugins/momentum_squeeze.py

def generate_signal(df):
    """
    Strategia Momentum Squeeze:
    Kupuj, gdy świeca przebija w górę 2 poprzednie, przy wzroście wolumenu.
    """
    if len(df) < 5:
        return "Za mało danych"

    c = df["close"]
    v = df["volume"]
    
    if c.iloc[-1] > c.iloc[-2] and c.iloc[-2] > c.iloc[-3] and v.iloc[-1] > v.iloc[-2]:
        return "BUY – Impuls wzrostowy 🚀"
    elif c.iloc[-1] < c.iloc[-2] and c.iloc[-2] < c.iloc[-3] and v.iloc[-1] > v.iloc[-2]:
        return "SELL – Impuls spadkowy 🔻"
    else:
        return "HOLD – Brak wyraźnego ruchu"
