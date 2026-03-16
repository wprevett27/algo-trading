# backtesting/backtest.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strategies.signal_generator import generate_signals

def run_backtest(data, initial_capital=10000):
    """
    Simulates trading based on signals and tracks portfolio value over time.
    
    Parameters:
    - data: DataFrame with signals already generated
    - initial_capital: how much money you start with (default $10,000)
    """
    data = generate_signals(data)
    
    cash = initial_capital
    shares = 0
    portfolio_values = []

    for i, row in data.iterrows():
        if row["Signal"].item() == 1 and shares == 0:
            shares = float(cash / row["Close"].item())
            cash = 0

        elif row["Signal"].item() == -1 and shares > 0:
            cash = float(shares * row["Close"].item())
            shares = 0

        total_value = cash + (shares * row["Close"].item())
        portfolio_values.append(total_value)

    portfolio_series = pd.Series(portfolio_values, index=data.index)
    
    total_return = ((portfolio_series.iloc[-1] - initial_capital) / initial_capital) * 100
    
    peak = portfolio_series.cummax()
    drawdown = (portfolio_series - peak) / peak * 100
    max_drawdown = drawdown.min()

    return {
        "portfolio": portfolio_series,
        "total_return": round(total_return, 2),
        "max_drawdown": round(max_drawdown, 2),
        "final_value": round(portfolio_series.iloc[-1], 2)
    }
if __name__ == "__main__":
    import yfinance as yf
    from datetime import date
    starting_capital = 10000

    data = yf.download("AAPL", start="2022-01-01", end=date.today())
    results = run_backtest(data)

    print(f"Final Portfolio Value: ${results['final_value']}")
    print(f"Total Return: {results['total_return']}%")
    print(f"Max Drawdown: {results['max_drawdown']}%")

    plt.figure(figsize=(14, 6))
    plt.plot(results["portfolio"], color="blue", linewidth=1.5, label="Portfolio Value")
    plt.axhline(y=starting_capital, color="red", linestyle="--", linewidth=1, label="Starting Capital")
    plt.title("AAPL Backtest — Portfolio Value Over Time")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value (USD)")
    plt.legend(loc="upper left")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()