import seaborn as sns
import matplotlib.pyplot as plt

class StockVisualizer:
    def __init__(self, filtered_data, summary):
        self.filtered_data = filtered_data
        self.summary = summary

    def plot(self):
        dt = self.filtered_data
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        sns.lineplot(data=dt, x=dt.index, y="Close", ax=ax1, label = "Close")
        sns.lineplot(data=dt, x=dt.index, y="MA50", ax=ax1, label = "MA50")
        sns.lineplot(data=dt, x=dt.index, y="MA200", ax=ax1, label = "MA200")
        ax1.set_title("Close, MA50, MA200 in Chosen Period")
        sns.histplot(data=dt, ax=ax2, x="Daily Return")
        ax2.set_title("Daily Return in Chosen Period")
        plt.tight_layout()
        plt.show()