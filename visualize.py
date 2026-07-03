import pandas as pd
import plotly.graph_objects as go

# Load stock data
df = pd.read_csv("data/apple_stock.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Calculate Moving Averages
df["MA50"] = df["Close"].rolling(window=50).mean()
df["MA200"] = df["Close"].rolling(window=200).mean()

# Create interactive chart
fig = go.Figure()

# Closing Price
fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["Close"],
        mode="lines",
        name="Close Price"
    )
)

# 50-Day MA
fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["MA50"],
        mode="lines",
        name="50-Day MA"
    )
)

# 200-Day MA
fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["MA200"],
        mode="lines",
        name="200-Day MA"
    )
)

fig.update_layout(
    title="Apple Stock Analysis",
    xaxis_title="Date",
    yaxis_title="Price (USD)",
    template="plotly_white"
)

fig.show()