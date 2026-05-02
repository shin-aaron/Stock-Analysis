from fetcher import StockFetcher
from analyzer import StockAnalyzer
from visualizer import StockVisualizer

period = input("Which period are you interested in? (1W, 1M, 3M, 6M, 1Y, ALL)")
fetcher_obj = StockFetcher()
data = fetcher_obj.fetch()
data

analyzer_obj = StockAnalyzer(data)
analyzer_obj.filter_period(period)
analyzer_obj.calculate_moving_averages()
analyzer_obj.calculate_daily_returns()
summary = analyzer_obj.get_summary()
summary

visual_obj = StockVisualizer(analyzer_obj.filtered, summary)
print(f"""
═══════════════════════════════════════
        AAPL Stock Analysis — {period}
═══════════════════════════════════════
Start Price:  ${summary['start price']:.2f}
End Price:    ${summary['end price']:.2f}
Total Return: {summary['total return']:.2f}%
Volatility:   {summary['volatility']:.2f}%
Best Day:     +{summary['best day']:.2f}%  ({summary['best date']})
Worst Day:    {summary['worst day']:.2f}%  ({summary['worst date']})
═══════════════════════════════════════
""")
visual_obj.plot()