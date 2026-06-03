import pickle
import pandas as pd
from fetcher import StockFetcher
from features import FeatureEngineer

class StockPredictor:
    def __init__(self):
        self.features = ["MA7", "MA30", "Daily_Return", "Volatility", "RSI"]
        self.model = self.load_model()

    def load_model(self):
        with open("models/random_forest.pkl", "rb") as f:
            model = pickle.load(f)
        return model

    def predict(self):
        # Step 1: fetch and build features
        fetcher = StockFetcher()
        df = fetcher.fetch()
        engineer = FeatureEngineer()
        df = engineer.build_features(df)

        # Step 2: take the last row (most recent day)
        latest = df[self.features].iloc[-1]

        # Step 3: predict (model expects a 2D array so we reshape)
        prediction = self.model.predict(latest.values.reshape(1, -1))

        # Step 4: print result
        if prediction[0] == 1:
            print("Prediction for tomorrow: UP ↑")
        else:
            print("Prediction for tomorrow: DOWN ↓")

if __name__ == "__main__":
    predictor = StockPredictor()
    predictor.predict()