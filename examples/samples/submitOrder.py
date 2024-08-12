# import alpaca_trade_api as tradeapi
import alpaca_trade_api as tradeapi

API_KEY = "PKEJH4W0URAU56SHKQW3"
API_SECRET = "9g6xpk2x2RiBeV5Cy48WdpxCU51chZx91Lj8x6Ow"
API_BASE_URL = 'https://paper-api.alpaca.markets'

# Initialize the Alpaca client
api = tradeapi.REST(API_KEY, API_SECRET, API_BASE_URL, api_version='v2')

try:
    # Get account information
    account = api.get_account()
    print(f"Account status: {account.status}")

    # Define order parameters
    symbol = 'AAPL'
    qty = 1  # Quantity to buy

    # Place a buy order
    buy_order = api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='day'
    )

    print(f"Buy order submitted: {buy_order}")

except Exception as e:
    print(f"An error occurred: {e}")
