# Script 1: Basic Average Stock Trend Calculator

# Ask for stock ticker
ticker = input("Enter stock ticker symbol: ")

# Ask for daily trend values (price % changes)
trend_input = input("Enter daily trend values separated by spaces (e.g., 1.2 -0.5 0.8): ")

# Convert input to list of floats
trends = [float(x) for x in trend_input.split()]

# Calculate average
average_trend = sum(trends) / len(trends)

# Output result
print(f"The average trend for {ticker} is {average_trend:.2f}%")
# Script 2: Calculates average daily percentage change from prices

ticker = input("Enter stock ticker symbol: ")
price_input = input("Enter daily closing prices separated by spaces (e.g., 150 152 151 153): ")

# Convert to list of floats
prices = [float(x) for x in price_input.split()]

# Calculate daily percentage changes
trends = []
for i in range(1, len(prices)):
    change = ((prices[i] - prices[i-1]) / prices[i-1]) * 100
    trends.append(change)

# Calculate average trend
average_trend = sum(trends) / len(trends)

print(f"The average daily trend for {ticker} is {average_trend:.2f}%")
# Script 3: Fetches real stock data using yfinance
import yfinance as yf

# Ask for stock ticker
ticker = input("Enter stock ticker symbol (e.g., AAPL): ")

# Download recent 5 days of data
data = yf.download(ticker, period="5d")

# Get closing prices
prices = data["Close"].tolist()

# Calculate daily percentage changes
trends = []
for i in range(1, len(prices)):
    change = ((prices[i] - prices[i-1]) / prices[i-1]) * 100
    trends.append(change)

# Calculate average trend
average_trend = sum(trends) / len(trends)

# Output
print(f"The 5-day average daily trend for {ticker} is {average_trend:.2f}%")

