import yfinance as yf

# Download stock data
stock = yf.download(
    "AAPL",
    start="2020-01-01",
    end="2025-01-01",
    auto_adjust=True
)

# Flatten MultiIndex columns if they exist
if hasattr(stock.columns, "droplevel"):
    stock.columns = stock.columns.droplevel(1)

# Save CSV
stock.to_csv("apple_stock.csv")

print("Data downloaded successfully!")
print(stock.head())
print(stock.shape)