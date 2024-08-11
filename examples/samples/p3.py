import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
from datetime import datetime, timedelta

# Set the stock symbol and date range
SYMBOL = 'AAPL'
START_DATE = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
END_DATE = datetime.now().strftime('%Y-%m-%d')

# Function to fetch historical data from Yahoo Finance
def fetch_data():
    data = yf.download(SYMBOL, start=START_DATE, end=END_DATE, interval='1m')
    # Filter data for 1:23 PM for each of the last 7 days
    data = data.between_time('13:23', '13:23')
    return data

def stock_grabber():
    data = fetch_data()
    # Extract the closing price for 1:23 PM each day
    return data['Close']

# Initialize variables for plotting
x = []
y = []

# Function to update the animation
def animate(i):
    global x, y
    y = stock_grabber()
    x = [date.strftime('%Y-%m-%d') for date in y.index]

    plt.cla()  # Clear the previous plot
    plt.plot(x, y, marker='o', label='1:23 PM Close Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f"Apple (AAPL) Price at 1:23 PM for the Last 7 Days")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()
