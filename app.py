import streamlit as st
import pandas as pd
import datetime
from data_fetcher import get_stock_data  # ✅ Import function from data_fetcher.py

# ✅ Streamlit UI Setup
st.title("📈 Real-Time Stock Market Dashboard")

# ✅ User selects a timezone BEFORE fetching data
timezone = st.radio("Select Timezone:", ["US/Eastern", "US/Central"], key="timezone_selector")

# ✅ User selects a stock
ticker = st.selectbox("Select a stock", ["AAPL", "TMUS", "NVDA"], key="stock_selector")

# ✅ Fetch data (calls get_stock_data from data_fetcher.py)
df = get_stock_data(ticker, timezone)

# ✅ Ensure it defaults to today’s date or latest available stock data
default_start_date = df["Datetime"].max().date() if not df.empty else datetime.date.today()
default_end_date = df["Datetime"].max().date() if not df.empty else datetime.date.today()

start_date = st.date_input("Start Date", default_start_date)
end_date = st.date_input("End Date", default_end_date)

# ✅ Filter dataframe based on selected dates
df_filtered = df[(df["Datetime"].dt.date >= start_date) & (df["Datetime"].dt.date <= end_date)]

# ✅ Display Timezone & Stock Selection
st.write(f"Timezone: {timezone}")
st.write(f"Showing latest data for {ticker} from {start_date} to {end_date}")

# ✅ Stock Price Line Chart
st.line_chart(df_filtered.set_index("Datetime")["Close"])

# ✅ Stock Volume Bar Chart
st.subheader("📊 Stock Volume Over Time")
st.bar_chart(df_filtered.set_index("Datetime")["Volume"])

# ✅ Refresh Button to Clear Cache
if st.button("🔄 Refresh Data"):
    st.cache_data.clear()
