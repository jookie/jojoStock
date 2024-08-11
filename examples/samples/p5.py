import yfinance as yf
import pandas as pd
import numpy as np

# Define a function to fetch and process data using Yahoo Finance
def fetch_and_process_data(ticker_list, start_date, end_date, technical_indicator_list, if_vix):
    # Initialize an empty list to hold dataframes
    data_frames = []

    # Fetch data for each ticker
    for ticker in ticker_list:
        # Download historical data
        data = yf.download(ticker, start=start_date, end=end_date)
        
        # Add ticker column
        data['Ticker'] = ticker

        # Append the dataframe to the list
        data_frames.append(data)
    
    # Combine all dataframes into a single dataframe
    combined_data = pd.concat(data_frames)

    # Clean data
    combined_data = combined_data.dropna()

    # Add technical indicators (dummy example)
    for indicator in technical_indicator_list:
        if indicator == 'SMA':
            combined_data['SMA_30'] = combined_data['Close'].rolling(window=30).mean()
        elif indicator == 'EMA':
            combined_data['EMA_30'] = combined_data['Close'].ewm(span=30, adjust=False).mean()

    # Add VIX or turbulence (dummy example)
    if if_vix:
        combined_data['VIX'] = np.random.rand(len(combined_data))  # Replace with actual VIX data if available
    else:
        combined_data['Turbulence'] = np.random.rand(len(combined_data))  # Replace with actual turbulence data if available

    # Convert dataframe to numpy arrays
    price_array = combined_data[['Close']].values
    tech_array = combined_data[[col for col in combined_data.columns if col.startswith('SMA') or col.startswith('EMA')]].values
    turbulence_array = combined_data[['VIX', 'Turbulence']].values if if_vix else combined_data[['Turbulence']].values

    return price_array, tech_array, turbulence_array

# Example usage
ticker_list = ['AAPL', 'MSFT']  # List of tickers
start_date = '2023-01-01'
end_date = '2023-08-01'
technical_indicator_list = ['SMA', 'EMA']
if_vix = False

price_array, tech_array, turbulence_array = fetch_and_process_data(ticker_list, start_date, end_date, technical_indicator_list, if_vix)

print("Price Array:", price_array)
print("Technical Indicators Array:", tech_array)
print("Turbulence Array:", turbulence_array)
