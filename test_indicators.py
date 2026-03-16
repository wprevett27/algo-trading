import yfinance as yf
from datetime import date 
import sys
from strategies.indicators import calculate_moving_average, calculate_rsi
sys.path.append(".")
# --- Load data ---
print("Downloading data...")
data = yf.download("AAPL", start="2022-01-01", end=date.today())

# --- Calculate indicators ---
data["SMA_20"] = calculate_moving_average(data, 20)
data["SMA_50"] = calculate_moving_average(data, 50)
data["RSI"]    = calculate_rsi(data)

# --- Preview results ---
print(data[["Close", "SMA_20", "SMA_50", "RSI"]].tail(10))