import yfinance as yf
import pandas as pd
import os
from datetime import date 
import matplotlib.pyplot as plt 
# --- Settings ---
TICKER = "AAPL"
START_DATE = "2022-01-01"
END_DATE   = date.today()
# --- Download stock data ---
print(f"Downloading {TICKER} data...")
data = yf.download(TICKER, start=START_DATE, end=END_DATE)

# --- Preview the data ---
print(data.head())
# --- Save data to CSV ---
csv_path = "data/AAPL_data.csv"
data.to_csv(csv_path)
print(f"Data saved to {csv_path}")
data["Close"].plot(title=f"{TICKER} Closing Price", ylabel="Price (USD)", xlabel="Date")
plt.tight_layout()
plt.show()