import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load dataset
df = pd.read_csv("apple_stock.csv")

# Keep only Close price
df = df[["Close"]]

# Create tomorrow's closing price
df["Prediction"] = df["Close"].shift(-1)

# Remove last row
df.dropna(inplace=True)

# Features (Today's Close)
X = df[["Close"]]

# Target (Tomorrow's Close)
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

# Predict
predictions = model.predict(X_test)

# Compare Actual vs Predicted
results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions
})

print(results.head(10))

# Evaluate model
mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5

print(f"\nMean Absolute Error: {mae:.2f}")
print(f"Root Mean Squared Error: {rmse:.2f}")