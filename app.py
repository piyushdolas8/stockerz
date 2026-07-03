import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import joblib

st.set_page_config(
    page_title="Stockerz - AI Stock Predictor",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Stockerz - AI Stock Predictor")

ticker = st.text_input("Enter Stock Ticker", "AAPL")

if st.button("Analyze Stock"):

    with st.spinner("Downloading stock data..."):

        df = yf.download(
            ticker,
            start="2020-01-01",
            progress=False,
            auto_adjust=True
        )

    if df.empty:
        st.error("Invalid ticker symbol.")
        st.stop()

    # Flatten MultiIndex columns if present
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.droplevel(1)

    # Moving averages
    df["MA50"] = df["Close"].rolling(50).mean()
    df["MA200"] = df["Close"].rolling(200).mean()

    # Current price
    current_price = df["Close"].iloc[-1]

    # Load trained model
    model = joblib.load("models/stock_model.pkl")

    # Predict next day's closing price
    prediction = model.predict(pd.DataFrame({"Close": [current_price]}))[0]

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Current Price", f"${current_price:.2f}")

    with col2:
        st.metric("Predicted Next Close", f"${prediction:.2f}")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Close"],
            name="Close Price"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["MA50"],
            name="50-Day MA"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["MA200"],
            name="200-Day MA"
        )
    )

    fig.update_layout(
        title=f"{ticker} Stock Price",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        template="plotly_white",
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)