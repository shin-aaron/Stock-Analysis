import yfinance as yf
class StockFetcher:
    def __init__(self):
        self.ticker = "AAPL"
        self.start = "2020-01-01"
        self.end = "2025-12-31"
        self.data = None

    def fetch(self):
        df = yf.download(self.ticker, start=self.start, end=self.end)
        df = df[["Close"]]
        df.columns = ["Close"]
        self.data = df
        return self.data