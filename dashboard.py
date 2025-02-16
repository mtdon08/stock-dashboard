import pytz
import streamlit as st
import pandas as pd
import boto3
import os

from io import StringIO

# AWS S3 Configuration
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
BUCKET_NAME ="real-time-stock-data-username"

# Initialize S3 Client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name = "us-east-1"
)

def get_stock_data(ticker):
    """Fetch stock data from AWS S3"""
    file_name = f"stock_data/{ticker}_stock_data.csv"
    
    obj = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_name)
    df = pd.read_csv(StringIO(obj["Body"].read().decode("utf-8")))

 # ✅ Convert 'Datetime' column to datetime format
    df["Datetime"] = pd.to_datetime(df["Datetime"], errors='coerce')


    # Select the user’s chosen timezone
    user_timezone = pytz.timezone(timezone)

  # ✅ Fix: Check if 'Datetime' is already timezone-aware
    if df["Datetime"].dt.tz is None:
        df["Datetime"] = df["Datetime"].dt.tz_localize("UTC")

 # Convert from UTC to Eastern Time (ET)
    eastern = pytz.timezone("US/Eastern")
    df["Datetime"] = df["Datetime"].dt.tz_convert(eastern)

    return df

# ✅ Fix: Move Streamlit UI setup **before using df**
st.title("📈 Real-Time Stock Market Dashboard")

# ✅ Fix: Let Users Choose a Timezone BEFORE fetching data
timezone = st.radio("Select Timezone:", ["US/Eastern", "US/Central"], key="timezone_selector")


# User selects a stock
ticker = st.selectbox("Select a stock", ["AAPL", "TMUS", "NVDA"],key="stock_selector")

# ✅ Fix: Fetch data **before** using df in date filters
df = get_stock_data(ticker)

# ✅ Fix: Convert 'Datetime' before using it for filtering
df["Datetime"] = pd.to_datetime(df["Datetime"], errors='coerce')

# ✅ Fix: Show the selected timezone in the dashboard
st.write(f"Timezone: {timezone}")


# ✅ Fetch AWS credentials from Streamlit secrets
AWS_ACCESS_KEY = st.secrets["AWS_ACCESS_KEY"]
AWS_SECRET_KEY = st.secrets["AWS_SECRET_KEY"]
BUCKET_NAME = "real-time-stock-data-username"

# ✅ Use Streamlit secrets for AWS authentication
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name="us-east-1"
)

# Feature 1: Date Range Selector
start_date = st.date_input("Start Date", df["Datetime"].min().date())
end_date = st.date_input("End Date", df["Datetime"].max().date())

# Filter the dataframe based on selected dates
df_filtered = df[(df["Datetime"].dt.date >= start_date) & (df["Datetime"].dt.date <= end_date)]

# Streamlit UI
st.title("📈 Real-Time Stock Market Dashboard")

# User selects a stock
ticker = st.selectbox("Select a stock", ["AAPL", "TMUS", "NVDA"])

# Fetch data and display it
df = get_stock_data(ticker)
st.write(f"Showing latest data for {ticker} from {start_date} to {end_date}")
st.line_chart(df.set_index("Datetime")["Close"])

# ✅ Additional Feature: Show Stock Trading Volume
st.subheader("📊 Stock Volume Over Time")
st.bar_chart(df_filtered.set_index("Datetime")["Volume"])
