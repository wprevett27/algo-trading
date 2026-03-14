\# Project Roadmap — Algorithmic Trading Bot



A rule-based algorithmic trading system built in Python. This project pulls historical stock data,

applies technical indicators to generate buy/sell signals, backtests the strategy against historical

data, and executes simulated trades via the Alpaca paper trading API.



Built as a college application project to demonstrate applied programming, data analysis, and

systems design skills.



\---



\## Phase 0 — Environment Setup ✅

\*\*Status: Complete\*\*



\- \[x] Python virtual environment configured

\- \[x] All libraries installed (yfinance, pandas, numpy, matplotlib, ta, alpaca-trade-api)

\- \[x] Project folder structure created

\- \[x] Alpaca paper trading account set up

\- \[x] GitHub repository initialized with .gitignore and requirements.txt



\---



\## Phase 1 — Data Collection

\*\*Status: Up next\*\*



Goal: Pull real historical stock price data and understand its structure.



\- \[ ] Write `data/fetch\_data.py` to download OHLCV data using yfinance

\- \[ ] Understand Open, High, Low, Close, Volume (OHLCV) format

\- \[ ] Save data locally as CSV files in `data/`

\- \[ ] Plot a basic price chart using matplotlib



\*\*Key concept:\*\* OHLCV — the standard format for stock price data. Each row represents

one time period (e.g. one day) and records the opening price, highest price, lowest price,

closing price, and number of shares traded.



\---



\## Phase 2 — Technical Indicators

\*\*Status: Not started\*\*



Goal: Calculate mathematical indicators from price data that help identify trends.



\- \[ ] Implement Simple Moving Average (SMA) — smooths price data over N days

\- \[ ] Implement Exponential Moving Average (EMA) — like SMA but weights recent prices more

\- \[ ] Implement RSI (Relative Strength Index) — measures momentum, identifies overbought/oversold conditions

\- \[ ] Visualize indicators overlaid on price charts



\*\*Key concept:\*\* A moving average is the average closing price over the last N days,

recalculated each day. When a short-term average crosses above a long-term average,

it can signal upward momentum — this is called a "golden cross."



\---



\## Phase 3 — Signal Generation

\*\*Status: Not started\*\*



Goal: Write rules that convert indicator values into actionable trade signals.



\- \[ ] Write `strategies/moving\_average\_crossover.py`

\- \[ ] Write `strategies/rsi\_strategy.py`

\- \[ ] Generate BUY / SELL / HOLD signals based on indicator conditions

\- \[ ] Visualize signals on price charts (mark buy/sell points)



\*\*Key concept:\*\* A trading signal is a rule-based trigger. Example: "If the 10-day

moving average crosses above the 50-day moving average, generate a BUY signal."



\---



\## Phase 4 — Backtesting

\*\*Status: Not started\*\*



Goal: Test strategies against historical data to measure how they would have performed.



\- \[ ] Write `backtesting/backtester.py` — simulates trades on historical data

\- \[ ] Track portfolio value over time

\- \[ ] Calculate key performance metrics:

&#x20; - Total return (%)

&#x20; - Win rate (% of trades that were profitable)

&#x20; - Maximum drawdown (largest peak-to-trough loss)

&#x20; - Sharpe ratio (return relative to risk)

\- \[ ] Plot equity curve (portfolio value over time)



\*\*Key concept:\*\* Backtesting is the process of running a strategy on past data to see

how it would have performed — without risking real money. It's how traders validate

ideas before going live.



\---



\## Phase 5 — Paper Trading (Live Simulation)

\*\*Status: Not started\*\*



Goal: Connect to Alpaca's API and execute trades automatically with simulated money.



\- \[ ] Set up `.env` file for secure API key storage

\- \[ ] Write `live\_trading/alpaca\_client.py` — connect to Alpaca API

\- \[ ] Write `live\_trading/trader.py` — submit buy/sell orders based on signals

\- \[ ] Test end-to-end: data → signal → order submission

\- \[ ] Verify trades appear in Alpaca paper trading dashboard



\*\*Key concept:\*\* Paper trading means executing a real trading strategy with fake money

in a simulated market environment. All the mechanics are real — only the money isn't.



\---



\## Phase 6 — Logging and Monitoring

\*\*Status: Not started\*\*



Goal: Record every trade and track performance over time.



\- \[ ] Write `logs/logger.py` — log trades with timestamps, prices, and reasoning

\- \[ ] Track daily portfolio value in a CSV log

\- \[ ] Build a simple performance dashboard using matplotlib

\- \[ ] Add error handling so the bot doesn't crash silently



\*\*Key concept:\*\* In production systems, logging is how you debug problems after the

fact. A trade log answers: "What did the bot do, when, and why?"



\---



\## Phase 7 — Documentation and Polish

\*\*Status: Not started\*\*



Goal: Make the project presentable for college applications and public viewers.



\- \[ ] Write comprehensive README.md with setup instructions

\- \[ ] Add docstrings to every function explaining what it does

\- \[ ] Add inline comments to complex logic

\- \[ ] Clean up all code (consistent naming, remove debug prints)

\- \[ ] Add example output charts to README

\- \[ ] Write project reflection (what worked, what didn't, what I'd improve)



\---



\## Tech Stack



| Tool | Purpose |

|------|---------|

| Python 3.10+ | Core language |

| yfinance | Historical stock data |

| pandas | Data manipulation |

| numpy | Numerical calculations |

| matplotlib | Charting and visualization |

| ta | Technical indicator library |

| alpaca-trade-api | Paper trading API |

| Git + GitHub | Version control |



\---



\## Project Structure



```

algo-trading/

│

├── data/               # Raw and processed price data

├── strategies/         # Trading strategy logic

├── backtesting/        # Backtesting engine

├── live\_trading/       # Alpaca API connection

├── logs/               # Trade and performance logs

├── notebooks/          # Jupyter notebooks for exploration

│

├── main.py             # Entry point

├── config.py           # Settings and parameters

├── requirements.txt    # Python dependencies

└── ROADMAP.md          # This file

```



\---



\*This project uses Alpaca paper trading only — no real money is involved.\*

