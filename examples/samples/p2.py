import alpaca_trade_api as tradeapi

# API_KEY = 'your_api_key_here'
# API_SECRET = 'your_api_secret_here'
# API_BASE_URL = 'https://paper-api.alpaca.markets'


API_KEY = "PKA2OY3YK7Y4M6Q7LCLR"
API_SECRET = "BxT64PIQtDBb*tnW"
API_BASE_URL = 'https://paper-api.alpaca.markets/v2'
data_url = 'wss://data.alpaca.markets/v2'
import alpaca_trade_api as tradeapi
# Step 2. Get ticker list, Set start date and end date, specify the data frequency
# https://data.sandbox.alpaca.markets/v2
from finrl.config_tickers import DOW_30_TICKER
from finrl.config import INDICATORS
from finrl.meta.env_stock_trading.env_stocktrading_np import StockTradingEnv
from finrl.meta.env_stock_trading.env_stock_papertrading import AlpacaPaperTrading
from finrl.meta.data_processor import DataProcessor
from finrl.plot import backtest_stats, backtest_plot, get_daily_return, get_baseline

api = tradeapi.REST(API_KEY, API_SECRET, API_BASE_URL, api_version='v2')
