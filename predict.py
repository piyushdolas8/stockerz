import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/stock_model.pkl")

# Load stock data
df = pd.read_csv("data/apple_stock.csv")

# Keep only Close price
df = df[["Close"]]

# Get latest closing price
latest_close = df.iloc[-1]["Close"]

# Predict next day's closing price
prediction = model.predict([[latest_close]])

print("=" * 40)
print("AI STOCK PREDICTION")
print("=" * 40)
print(f"Latest Closing Price : ${latest_close:.2f}")
print(f"Predicted Next Close : ${prediction[0]:.2f}")
print("=" * 40)