import yfinance as yf
import pandas as pd
import boto3
import os
from io import StringIO
from datetime import datetime
import time  # ✅ Add this to fix the error

# AWS S3 Configuration
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
BUCKET_NAME = "real-time-stock-data-username"

# Initialize S3 Client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
)

def fetch_stock_data(symbols=["AAPL", "TMUS", "NVDA"]):
    """Fetch real-time stock data for multiple tickers"""
    all_data = {}

    for symbol in symbols:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d", interval="1m")  # 1-minute interval
        data.reset_index(inplace=True)
        all_data[symbol] = data  # Store in dictionary

    return all_data

def upload_csv_to_s3(df, file_name):
    """Upload DataFrame as CSV directly to AWS S3"""
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    try:
        s3_client.put_object(Bucket=BUCKET_NAME, Key=f"stock_data/{file_name}", Body=csv_buffer.getvalue())
        print(f"✅ Uploaded {file_name} to S3")
    except Exception as e:
        print(f"❌ Error uploading {file_name}: {e}")

if __name__ == "__main__":
    tickers = ["AAPL", "TMUS", "NVDA"]

    while True:  # Keep running
        stock_data = fetch_stock_data(tickers)

        for ticker, df in stock_data.items():
            file_name = f"{ticker}_stock_data.csv"
            upload_csv_to_s3(df, file_name)  # Upload directly to S3 (NO LOCAL SAVE)

        print("⏳ Waiting for the next update...\n")
        time.sleep(60)  # Wait 60 seconds before fetching again
