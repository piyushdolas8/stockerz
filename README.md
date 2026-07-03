# 📈 Stockerz - AI Stock Predictor

Stockerz is a Machine Learning project that predicts the next day's stock closing price using historical stock market data.

## 🚀 Features

- Download stock data from Yahoo Finance
- Interactive stock charts
- 50-Day Moving Average
- 200-Day Moving Average
- Next-day stock price prediction
- Streamlit dashboard
- Supports multiple stock tickers

## 🛠 Tech Stack

- Python
- Pandas
- Scikit-learn
- yfinance
- Plotly
- Streamlit
- Joblib

## Installation

```bash
pip install -r requirements.txt
```

Run the app

```bash
streamlit run app.py
```

## Project Structure

```
stockerz/
│
├── app.py
├── data.py
├── train.py
├── predict.py
├── visualize.py
├── requirements.txt
├── README.md
│
├── data/
├── models/
└── venv/
```

## Future Improvements

- LSTM-based prediction
- Multiple ML model comparison
- Technical indicators (RSI, MACD)
- Real-time market data
- News sentiment analysis