import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strategies.indicators import calculate_moving_average, calculate_rsi

# --- Load and prepare data ---
data = yf.download("AAPL", start="2022-01-01", end=date.today())

data["SMA_20"] = calculate_moving_average(data, 20)
data["SMA_50"] = calculate_moving_average(data, 50)
data["RSI"]    = calculate_rsi(data)

# --- Set up a figure with 2 stacked panels ---
fig, (ax1, ax2) = plt.subplots(
    nrows=2,        # 2 rows of charts stacked vertically
    ncols=1,        # 1 column
    figsize=(14, 8),# width=14 inches, height=8 inches
    sharex=True     # both charts share the same x-axis (date)
)

# --- Top chart: Closing price + both SMAs ---
ax1.plot(data.index, data["Close"],  
         label="Close Price", color="black",  linewidth=1)
ax1.plot(data.index, data["SMA_20"], 
         label="SMA 20",      color="blue",   linewidth=1.5)
ax1.plot(data.index, data["SMA_50"], 
         label="SMA 50",      color="orange", linewidth=1.5)

ax1.set_title("AAPL — Price and Moving Averages")
ax1.set_ylabel("Price (USD)")
ax1.legend(loc="upper left")
ax1.grid(True, alpha=0.3)

# --- Bottom chart: RSI ---
ax2.plot(data.index, data["RSI"], 
         label="RSI (14)", color="purple", linewidth=1)

ax2.axhline(y=70, color="red",   linestyle="--", linewidth=1, label="Overbought (70)")
ax2.axhline(y=30, color="green", linestyle="--", linewidth=1, label="Oversold (30)")

ax2.set_title("RSI Indicator")
ax2.set_ylabel("RSI Value")
ax2.set_xlabel("Date")
ax2.set_ylim(0, 100)
ax2.legend(loc="upper left")
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()