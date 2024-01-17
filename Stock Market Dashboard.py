import yfinance as yf
import matplotlib.pyplot as plt

# Function to fetch historical stock data
def get_stock_data(ticker, period='1y'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data

# Function to plot stock data
def plot_stock_data(data, ticker):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label=f'{ticker} Closing Price', color='blue')
    plt.title(f'{ticker} Closing Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
ticker = 'AAPL' ##change company name here!!!!
stock_data = get_stock_data(ticker)
plot_stock_data(stock_data, ticker)
