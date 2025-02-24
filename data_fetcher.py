import boto3
import pandas as pd
import pytz
from io import StringIO
import config  # ✅ Import AWS settings from config.py

# ✅ Initialize AWS S3 Client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=config.AWS_ACCESS_KEY,
    aws_secret_access_key=config.AWS_SECRET_KEY,
    region_name=config.AWS_REGION
)

def get_stock_data(ticker, timezone="US/Eastern"):
    """Fetch the latest stock data from AWS S3 and convert timezone"""
    
    file_name = f"stock_data/{ticker}_stock_data.csv"

    try:
        obj = s3_client.get_object(Bucket=config.BUCKET_NAME, Key=file_name)
        df = pd.read_csv(StringIO(obj["Body"].read().decode("utf-8")))
    except Exception as e:
        print(f"❌ Error fetching data from S3: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error

    # ✅ Convert 'Datetime' column to timezone-aware format
    df["Datetime"] = pd.to_datetime(df["Datetime"], errors='coerce')

    if df["Datetime"].dt.tz is None:
        df["Datetime"] = df["Datetime"].dt.tz_localize("UTC")  # Default to UTC

    user_timezone = pytz.timezone(timezone)
    df["Datetime"] = df["Datetime"].dt.tz_convert(user_timezone)

    return df.sort_values("Datetime", ascending=False)  # Show latest first
