from fetcher import StockFetcher
from features import FeatureEngineer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

class StockTrainer:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.features = ["MA7", "MA30", "Daily_Return", "Volatility", "RSI"]

    def prepare_data(self):
        # Step 1: fetch and build features
        fetcher = StockFetcher()
        df = fetcher.fetch()
        engineer = FeatureEngineer()
        df = engineer.build_features(df)

        # Step 2: create target column
        df["Target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)
        df.dropna(inplace=True)
        return df

    def split_data(self, df):
        train = df.loc["2020-01-01" : "2023-12-31"]
        test = df.loc["2024-01-01" : "2025-12-31"]

        X_train = train[self.features]
        y_train = train["Target"]
        X_test = test[self.features]
        y_test = test["Target"]
        return X_train, y_train, X_test, y_test

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def evaluate(self, X_test, y_test):
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print(f"Test Accuracy: {accuracy:.2%}")
        print(classification_report(y_test, predictions))

    def save_model(self):
        with open("models/random_forest.pkl", "wb") as f:
            pickle.dump(self.model, f)
        print("Model saved!")

if __name__ == "__main__":
    trainer = StockTrainer()
    df = trainer.prepare_data()
    X_train, y_train, X_test, y_test = trainer.split_data(df)
    trainer.train(X_train, y_train)
    trainer.evaluate(X_test, y_test)
    trainer.save_model()


# #get data, 
# fetcher = StockFetcher()
# data = fetcher.fetch()

# #create features and label
# data['MA50'] = data['Close'].rolling(window=50).mean()
# data['MA200'] = data['Close'].rolling(window=200).mean()
# data['Daily Return'] = data['Close'].pct_change()*100
# data['Target'] = data['Close'].shift(-1)
# data = data.dropna()

# # define features and labels
# features = ['Close', 'MA50', 'MA200', 'Daily Return']
# X = data[features]
# y = data['Target']

# #split into train/test 
# from sklearn.model_selection import train_test_split
# # shuffle=False because this is time-series data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
# from sklearn.linear_model import LinearRegression
# model = LinearRegression()
# model.fit(X_train, y_train)
# predictions = model.predict(X_test)
# for i in range(5):
#     print(f"Predicted: ${predictions[i]:.2f}  |  Actual: ${y_test.iloc[i]:.2f}")

# from sklearn.metrics import mean_absolute_error, r2_score
# mae = mean_absolute_error(y_test, predictions)
# r2 = r2_score(y_test, predictions)

# print(f"\nModel Accuracy:")
# print(f"MAE:  ${mae:.2f} average error per prediction")
# print(f"R²:   {r2:.4f}")

# from sklearn.tree import DecisionTreeRegressor

# tree_model = DecisionTreeRegressor(max_depth=10)
# tree_model.fit(X_train, y_train)
# tree_predictions = tree_model.predict(X_test)

# tree_mae = mean_absolute_error(y_test, tree_predictions)
# tree_r2 = r2_score(y_test, tree_predictions)

# print(f"\nDecision Tree Accuracy:")
# print(f"MAE:  ${tree_mae:.2f} average error per prediction")
# print(f"R²:   {tree_r2:.4f}")

# from sklearn.ensemble import RandomForestRegressor

# forest_model = RandomForestRegressor(n_estimators=100)
# forest_model.fit(X_train, y_train)
# forest_predictions = forest_model.predict(X_test)

# forest_mae = mean_absolute_error(y_test, forest_predictions)
# forest_r2 = r2_score(y_test, forest_predictions)

# print(f"\nRandom Forest Accuracy:")
# print(f"MAE:  ${forest_mae:.2f} average error per prediction")
# print(f"R²:   {forest_r2:.4f}")