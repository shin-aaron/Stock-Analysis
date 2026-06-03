# AAPL Stock Analysis & ML Predictor
A Python tool that fetches, analyzes, and predicts Apple (AAPL) stock data using real market data from Yahoo Finance.

## Features
- Fetch real AAPL price data from 2020-01-01 to 2025-12-31
- Filter by time period: 1W, 1M, 3M, 6M, 1Y, ALL
- Calculate 50-day and 200-day moving averages
- Calculate daily returns and annualized volatility
- Display summary statistics (total return, best/worst day)
- Visualize price trends and returns distribution
- ML pipeline to predict next day's price direction (UP/DOWN)

## Tech Stack
- Python, Pandas
- yfinance (Yahoo Finance API)
- Seaborn, Matplotlib
- scikit-learn (Random Forest Classifier)

## How to Run
```bash
pip install yfinance pandas seaborn matplotlib scikit-learn
```
# Analysis tool
```bash
python main.py
```
# ML pipeline
```bash
python train.py     # train and evaluate model
python predict.py   # predict tomorrow's direction
```

## Project Structure
- `fetcher.py` — downloads AAPL OHLCV data from Yahoo Finance
- `analyzer.py` — filters by period, calculates MAs, returns, volatility
- `visualizer.py` — generates price trend and returns charts
- `main.py` — runs the analysis pipeline interactively
- `features.py` — engineers ML features (MA7, MA30, RSI, Volatility, Daily Return)
- `train.py` — trains Random Forest classifier with time-based train/test split
- `predict.py` — loads saved model and predicts next day's direction

## ML Approach
- **Model:** Random Forest Classifier
- **Features:** MA7, MA30, Daily Return, 14-day Volatility, RSI
- **Train set:** 2020–2023 | **Test set:** 2024–2025
- **Test Accuracy:** 44.91%

> Stock price prediction is inherently difficult due to market efficiency. This project is an educational exercise in building an end-to-end ML pipeline, not a financial tool. Planned upgrade: XGBoost with additional features.

## Roadmap
- ~~Add ML-based price prediction using scikit-learn~~ ✅
- Upgrade to XGBoost with improved feature engineering
- Analyze impact of CEO transition (Tim Cook → ?, September 2025)
