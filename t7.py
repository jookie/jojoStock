import alpaca_trade_api as tradeapi
from examples.ExampleOFinrl.config import ALPACA_API_BASE_URL

# Replace with your API key, secret, and base URL
API_KEY = "PKVD6WOSPEMKS0UI6A3K"
API_SECRET = "RJICB6GmO6FPff1e8pGq5IArPYabYi2ZaAqpHEar"
API_BASE_URL = 'https://paper-api.alpaca.markets'

APACA_EMAIL =  "dpeles20@gmail.com"
APACA_PWD1 = "102774Dov9012"
APACA_PWD2 = "f1ecd682-009e-49fc-893e-bc595cc4e015"
ALPACA_DATA = "https://data.alpaca.markets/v2/stocks/auctions?symbols=AAPL%2CTSLA&start=2022-01-03T00%3A00%3A00Z&end=2022-01-04T00%3A00%3A00Z&limit=1000&feed=sip&sort=asc"

# Initialize the Alpaca API
api = tradeapi.REST(API_KEY, API_SECRET, API_BASE_URL, api_version='v2')
# Specify the stock symbol and quantity you want to buy
symbol = "AAPL"
quantity = 10  # Number of shares to buy

# limit, stop, stop_limit orders. 
# Place a market order to buy the specified quantity of AAPL
try:
    order = api.submit_order(
        symbol=symbol,
        qty=quantity,
        side='buy', # buy or sell order for a security 
        type='market',  # Market order to be executed immediately at the current market price    
        time_in_force='gtc'  # Good 'til canceled
    )
    print(f"Market order placed to buy {quantity} shares of {symbol}")
except tradeapi.rest.APIError as e:
    print(f"An API error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
 
