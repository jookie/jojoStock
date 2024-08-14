# main.py

from alpaca_trade_api.rest import REST, TimeFrame
from stable_baselines3 import PPO

API_KEY = "PKEJH4W0URAU56SHKQW3"
API_SECRET = "9g6xpk2x2RiBeV5Cy48WdpxCU51chZx91Lj8x6Ow"
API_BASE_URL = 'https://paper-api.alpaca.markets'
api = REST(API_KEY, API_SECRET, API_BASE_URL, api_version='v2')
# Initialize Alpaca API

def get_market_data():
    # Fetch recent market data for a specific stock
    barset = api.get_bars("AAPL", TimeFrame.Day, "2023-01-01", "2024-01-01").df
    return barset

def place_order():
    # Place an order for a specific stock
    api.submit_order(
        symbol="AAPL",
        qty=1,
        side="buy",
        type="market",
        time_in_force="gtc"
    )

def train_and_trade():
    # Load market data and train a DRL model
    data = get_market_data()
    # Assuming you have a pre-trained model or a specific logic here
    # Example: model = PPO('MlpPolicy', env, verbose=1)
    # model.learn(total_timesteps=10000)

    # Decision-making logic (simplified for illustration)
    action = "buy"  # This would come from the model prediction

    if action == "buy":
        place_order()
        return "Order placed successfully"

    return "No action taken"

if __name__ == "__main__":
    result = train_and_trade()
    print(result)
