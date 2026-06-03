import pandas as pd

class FeatureEngineer:
    def build_features(self, df):
        # Moving averages
        df["MA7"] = df['Close'].rolling(window=7).mean()
        df["MA30"] = df['Close'].rolling(window=30).mean()

        # Daily return
        df["Daily_Return"] = df['Close'].pct_change()*100

        # Rolling volatility (14 day rolling std of Daily_Return)
        df["Volatility"] = df["Daily_Return"].rolling(window=14).std()

        # RSI (trickiest one — I'll show you this one)
        df["RSI"] = self._calculate_rsi(df["Close"])

        df.dropna(inplace=True)
        return df

    def _calculate_rsi(self, series, period=14):
        delta = series.diff()
        gain = delta.where(delta > 0, 0).rolling(window=period).mean()
        loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))