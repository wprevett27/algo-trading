import pandas as pd
import numpy as np
from ta.momentum import RSIIndicator
import yfinance as yf


def calculate_moving_average(data, window):
    """
    Calculates the Simple Moving Average (SMA) for a given window size.
    data: a pandas Series of closing prices
    window: how many days to average over (e.g. 20 or 50)
    """
    return data["Close"].rolling(window=window).mean()


def calculate_rsi(data, window=14):
    """
    Calculates the Relative Strength Index (RSI).
    data: a pandas DataFrame of price data
    window: lookback period in days (14 is the universal standard)
    """
    close_prices = data["Close"].squeeze()
    rsi = RSIIndicator(close=close_prices, window=window)
    return rsi.rsi()