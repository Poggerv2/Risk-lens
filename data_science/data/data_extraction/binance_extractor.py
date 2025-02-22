from binance.client import Client
import pandas as pd
import os
from dotenv import load_dotenv

os.makedirs("data/raw_data", exist_ok=True)


load_dotenv()
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

def fetch_binance_data(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1DAY, limits=1000):
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limits)
    df = pd.DataFrame(klines, columns=["date", "open", "high", "low", "close", "volume", "close_time",
                                       "quote_asset_volume", "trades", "taker_buy_base", "taker_buy_quote", "ignore"])
    df["date"] = pd.to_datetime(df["date"], unit="ms")
    df = df[["date", "open", "high", "low", "close", "volume"]]
    return df

if __name__ == "__main__":
    btc_data = fetch_binance_data()
    btc_data.to_csv("data/raw_data/btc.csv", index=False)