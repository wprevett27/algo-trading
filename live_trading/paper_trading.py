# live_trading/paper_trader.py

import pandas as pd
import yfinance as yf
from datetime import date, datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strategies.signal_generator import generate_signals

TICKER = "AAPL"
STARTING_CAPITAL = 10000
LOG_FILE = "logs/paper_trades.csv"

def load_portfolio():
    """
    Loads the current portfolio state from the log file.
    If no log file exists yet, returns a fresh starting portfolio.
    """
    if os.path.exists(LOG_FILE):
        trades = pd.read_csv(LOG_FILE)
        last_row = trades.iloc[-1]
        return {
            "cash": float(last_row["cash"]),
            "shares": float(last_row["shares"]),
            "portfolio_value": float(last_row["portfolio_value"])
        }
    else:
        return {
            "cash": STARTING_CAPITAL,
            "shares": 0,
            "portfolio_value": STARTING_CAPITAL
        }
    
def execute_trade(signal, price, portfolio):
    """
    Simulates placing a buy or sell order.
    
    Parameters:
    - signal: 1 (buy), -1 (sell), or 0 (hold)
    - price: today's closing price
    - portfolio: current portfolio state dictionary
    """
    if signal == 1 and portfolio["shares"] == 0:
        shares_bought = portfolio["cash"] / price
        portfolio["shares"] = shares_bought
        portfolio["cash"] = 0
        action = "BUY"

    elif signal == -1 and portfolio["shares"] > 0:
        portfolio["cash"] = portfolio["shares"] * price
        portfolio["shares"] = 0
        action = "SELL"

    else:
        action = "HOLD"

    portfolio["portfolio_value"] = portfolio["cash"] + (portfolio["shares"] * price)
    
    return portfolio, action

def log_trade(action, price, portfolio):
    """
    Saves today's trade to the CSV log file.
    """
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ticker": TICKER,
        "action": action,
        "price": round(price, 2),
        "shares": round(portfolio["shares"], 4),
        "cash": round(portfolio["cash"], 2),
        "portfolio_value": round(portfolio["portfolio_value"], 2)
    }

    log_df = pd.DataFrame([log_entry])

    if os.path.exists(LOG_FILE):
        log_df.to_csv(LOG_FILE, mode="a", header=False, index=False)
    else:
        log_df.to_csv(LOG_FILE, mode="w", header=True, index=False)

def run_paper_trader():
    """
    Main function that runs the paper trader for today.
    """
    print(f"Running paper trader for {TICKER} — {date.today()}")

    data = yf.download(TICKER, start="2022-01-01", end=date.today())
    data = generate_signals(data)

    today_signal = int(data["Signal"].iloc[-1].item())
    today_price = float(data["Close"].iloc[-1].item())

    portfolio = load_portfolio()
    portfolio, action = execute_trade(today_signal, today_price, portfolio)

    log_trade(action, today_price, portfolio)

    print(f"Action: {action}")
    print(f"Price: ${today_price}")
    print(f"Shares held: {round(portfolio['shares'], 4)}")
    print(f"Cash: ${round(portfolio['cash'], 2)}")
    print(f"Portfolio Value: ${round(portfolio['portfolio_value'], 2)}")


if __name__ == "__main__":
    run_paper_trader()