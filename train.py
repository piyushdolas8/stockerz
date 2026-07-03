import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load data
df = pd.read_csv("data/apple_stock.csv")

# Keep only Close price
df = df[["Close"]]

# Create target (Tomorrow's Close)
df["Prediction"] = df["Close"].shift(-1)

# Remove last row
df.dropna(inplace=True)

# Features & Target
X = df[["Close"]]
y = df["Prediction"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"MAE: {mae:.2f}")
print(f"R² Score: {r2:.4f}")

# Save trained model
joblib.dump(model, "models/stock_model.pkl")

print("\n✅ Model saved to models/stock_model.pkl")