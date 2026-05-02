# AAPL Stock Analysis Tool

A Python tool that fetches and analyzes Apple (AAPL) stock data using real market data from Yahoo Finance.

## Features
- Fetch real AAPL price data from 2020-01-01 to 2025-12-31
- Filter by time period: 1W, 1M, 3M, 6M, 1Y, ALL
- Calculate 50-day and 200-day moving averages
- Calculate daily returns and annualized volatility
- Display summary statistics (total return, best/worst day)
- Visualize price trends and returns distribution

## Tech Stack
- Python, Pandas, NumPy
- yfinance (Yahoo Finance API)
- Seaborn, Matplotlib

## How to Run
```bash
pip install yfinance pandas seaborn matplotlib
python main.py
```

## Project Structure
- `fetcher.py` — downloads AAPL data from Yahoo Finance
- `analyzer.py` — filters by period, calculates MAs, returns, volatility
- `visualizer.py` — generates price trend and returns charts
- `main.py` — runs the full pipeline

## Roadmap
- Add ML-based price prediction using scikit-learn
- Analyze impact of CEO transition (Tim Cook → ?, September 2025)
