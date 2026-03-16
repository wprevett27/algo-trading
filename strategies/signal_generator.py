# strategies/signal_generator.py

import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strategies.indicators import calculate_moving_average, calculate_rsi

def generate_signals(data):
    """
    Looks at each day of price data and decides: Buy, Sell, or Hold.
    Returns the original dataframe with a new 'Signal' column added.
    """
    data["SMA_20"] = calculate_moving_average(data, 20)
    data["SMA_50"] = calculate_moving_average(data, 50)
    data["RSI"]    = calculate_rsi(data)

    data["Signal"] = 0

    buy_condition = (
        (data["SMA_20"] > data["SMA_50"]) &
        (data["SMA_20"].shift(1) <= data["SMA_50"]) &
        (data["RSI"] < 70)
    )

    sell_condition = (
        (data["SMA_20"] < data["SMA_50"]) &
        (data["SMA_20"].shift(1) >= data["SMA_50"]) &
        (data["RSI"] > 30)
    )

    data.loc[buy_condition, "Signal"]  = 1
    data.loc[sell_condition, "Signal"] = -1
    
    return data
      
if __name__ == "__main__":
    import yfinance as yf
    from datetime import date

    data = yf.download("AAPL", start="2022-01-01", end=date.today())
    data = generate_signals(data)
    
    print(data[data["Signal"] != 0][["Close", "SMA_20", "SMA_50", "RSI", "Signal"]])