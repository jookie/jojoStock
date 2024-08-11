import requests

url = "https://data.alpaca.markets/v2/stocks/auctions?symbols=AAPL%2CTSLA&start=2022-01-03T00%3A00%3A00Z&end=2022-01-04T00%3A00%3A00Z&limit=1000&feed=sip&sort=asc"

headers = {
    "accept": "application/json",
    "APCA-API-KEY-ID": "PKVD6WOSPEMKS0UI6A3K",
    "APCA-API-SECRET-KEY": "RJICB6GmO6FPff1e8pGq5IArPYabYi2ZaAqpHEar"
}

response = requests.get(url, headers=headers)

print(response.text)