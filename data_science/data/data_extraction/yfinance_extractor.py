import yfinance as yf
import time
import os
import pandas as pd


def fetch_yahoo_data(ticker, start="2020-01-01", end="2025-01-01"):
    for _ in range(5):
        try:
            data = yf.download(ticker, start=start, end=end, progress=False)
            if not data.empty:
                return data
            else:
                print(f"No data received for {ticker}")
                return None
        except Exception as e:
            print(f"Error: {e}. Retrying in 10 seconds...")
            time.sleep(10)
    return None


if __name__ == "__main__":
    tickers = ["^GSPC"]
    save_path = os.path.join(os.path.dirname(__file__), "../raw_data/")
    os.makedirs(save_path, exist_ok=True)

    for ticker in tickers:
        data = fetch_yahoo_data(ticker)

        if data is not None:
            data.reset_index(inplace=True)
            data.rename(columns={"Date": "date", "Open": "open", "High": "high",
                                 "Low": "low", "Close": "close", "Volume": "volume"}, inplace=True)

            filename = f"{ticker.replace('^', '').lower()}.csv"
            data.to_csv(os.path.join(save_path, filename), index=False)
            print(f"Data for {ticker} saved.")
        else:
            print(f"Skipping {ticker}, no data retrieved.")
