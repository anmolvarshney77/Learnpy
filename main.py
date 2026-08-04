import requests


def get_stock_data():
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
    response = requests.get(url, timeout=1)

    if response.status_code == 200:
        data = response.json()

        if "Error Message" in data:
            return None

        meta_data = data.get("Meta Data", {})
        last_refreshed = meta_data.get("3. Last Refreshed") or meta_data.get("Last Refreshed")

        if not last_refreshed:
            return None

        time_series_key = next((key for key in data if key.startswith("Time Series")), None)
        if not time_series_key:
            return None

        time_series = data.get(time_series_key, {})
        if last_refreshed not in time_series:
            return None

        price = time_series[last_refreshed].get("1. open")
        return price

    return None


price = get_stock_data()
symbol = "IBM"
if price is not None:
    print(f"{symbol}: {price}")
else:
    print("failed to retrieve data.")