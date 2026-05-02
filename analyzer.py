import pandas as pd
class StockAnalyzer:
    def __init__(self, data):
        self.filtered = None
        self.data = data
    
    def filter_period(self, period):
        start = ""
        end = self.data.index.max()
        if period == "1W":
            start = end - pd.DateOffset(weeks=1)
        elif period == "1M":
            start = end - pd.DateOffset(months=1)
        elif period == "3M":
            start = end - pd.DateOffset(months=3)
        elif period == "6M":
            start = end - pd.DateOffset(months=6)
        elif period == "1Y":
            start = end - pd.DateOffset(years=1)
        elif period == "ALL":
            start = self.data.index.min()
        else:
            print("Invalid period. Choose: 1W, 1M, 3M, 6M, 1Y, ALL")
            return None
        self.filtered=self.data.loc[start:end].copy()
        return self.filtered
    
    def calculate_moving_averages(self):
        self.filtered['MA50'] = self.data['Close'].rolling(window=50).mean().reindex(self.filtered.index)
        self.filtered['MA200'] = self.data['Close'].rolling(window=200).mean().reindex(self.filtered.index)

    def calculate_daily_returns(self):
        self.filtered['Daily Return'] = self.filtered['Close'].pct_change()*100

    def get_summary(self):
        start_price=self.filtered["Close"].iloc[0]
        end_price=self.filtered['Close'].iloc[-1]
        total_return = ((end_price-start_price)/start_price)*100
        volatility = self.filtered["Daily Return"].std() * (252 ** 0.5)
        best_day = self.filtered['Daily Return'].max()
        best_date = self.filtered['Daily Return'].idxmax().strftime("%Y-%m-%d")
        worst_day = self.filtered['Daily Return'].min()
        worst_date = self.filtered['Daily Return'].idxmin().strftime("%Y-%m-%d")
        
        return {"start price": start_price, 
                "end price": end_price,
                "total return": total_return,
                "volatility": volatility,
                "best day": best_day,
                "best date": best_date,
                "worst day": worst_day,
                "worst date": worst_date}