<p align="center">
  <img src="Stockerz.png" alt="Stockerz Banner" width="100%">
</p>

<h1 align="center">📈 Stockerz</h1>

<h3 align="center">
AI-Powered Stock Analysis & Prediction Dashboard
</h3>

<p align="center">
Analyze historical stock prices, visualize market trends, and predict the next day's closing price using Machine Learning.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge\&logo=scikitlearn\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?style=for-the-badge\&logo=plotly\&logoColor=white)

</p>

---

# 🚀 Overview

**Stockerz** is an end-to-end Machine Learning project that enables users to:

* 📈 Download real-time historical stock data
* 📊 Visualize stock price trends
* 📉 Analyze 50-Day & 200-Day Moving Averages
* 🤖 Predict the next day's closing stock price
* 🌐 Interact through a modern Streamlit dashboard

The application combines data collection, preprocessing, machine learning, and interactive visualization into a single user-friendly dashboard.

---

# ✨ Features

* 📥 Download stock data using Yahoo Finance
* 📊 Interactive Plotly charts
* 📈 50-Day Moving Average
* 📉 200-Day Moving Average
* 🤖 Machine Learning prediction
* 💾 Saved ML model using Joblib
* 🌐 Streamlit Web Dashboard
* 🔍 Support for multiple stock tickers

---

# 🛠 Tech Stack

### Programming Language

<p>
<img src="https://skillicons.dev/icons?i=python"/>
</p>

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Data Source

* Yahoo Finance API (yfinance)

### Data Visualization

* Plotly
* Matplotlib

### Web Framework

* Streamlit

### Tools

<p>
<img src="https://skillicons.dev/icons?i=git,github,vscode"/>
</p>

---

# 📂 Project Structure

```text
stockerz/
│
├── app.py                 # Streamlit Dashboard
├── data.py                # Download Stock Data
├── train.py               # Train Machine Learning Model
├── predict.py             # Predict Next-Day Price
├── visualize.py           # Stock Charts
├── requirements.txt
├── README.md
│
├── data/
│   └── apple_stock.csv
│
├── models/
│   └── stock_model.pkl
│
└── venv/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/piyushdolas8/stockerz.git
```

Move into the project

```bash
cd stockerz
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📊 How It Works

1. Download historical stock market data.
2. Clean and preprocess the dataset.
3. Calculate technical indicators.
4. Train a Linear Regression model.
5. Predict the next day's closing price.
6. Display predictions and charts through Streamlit.

---

# 📸 Application Preview

<p align="center">

### 🖥️ Dashboard

<img src="Dashboard.png" width="95%">

<br><br>

### 📈 Prediction & Interactive Chart

<img src="Prediction.png" width="95%">

</p>

---

# 🔮 Future Improvements

* Random Forest Regressor
* LSTM Deep Learning Model
* GRU & Transformer Models
* Technical Indicators (RSI, MACD, Bollinger Bands)
* Real-Time Stock Prices
* News Sentiment Analysis
* Portfolio Tracker
* Multi-Stock Comparison

---

# 📖 What I Learned

Through this project I gained hands-on experience with:

* Machine Learning workflow
* Data preprocessing
* Feature engineering
* Financial data analysis
* Interactive data visualization
* Model serialization
* Streamlit application development
* Git & GitHub project management

---

# 🤝 Connect With Me

<p align="left">
  <a href="https://www.linkedin.com/in/piyush-dolas-0567a6303" target="_blank">
    <img src="https://skillicons.dev/icons?i=linkedin" height="45" alt="LinkedIn"/>
  </a>
  &nbsp;
  <a href="mailto:piyushdolas8@gmail.com">
    <img src="https://skillicons.dev/icons?i=gmail" height="45" alt="Email"/>
  </a>
  &nbsp;
  <a href="https://www.youtube.com/@piyushbuilds2026" target="_blank">
    <img src="https://cdn.simpleicons.org/youtube/FF0000" height="45" alt="YouTube"/>
  </a>
</p>

<p align="center">

⭐ If you found this project interesting, consider giving it a star!

</p>

🚀 **Live Demo:** https://stockerz-ai.streamlit.app
