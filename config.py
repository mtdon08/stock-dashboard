import os
import streamlit as st

# ✅ AWS Credentials (Use Secrets in Streamlit Cloud)
AWS_ACCESS_KEY = st.secrets["AWS_ACCESS_KEY"]
AWS_SECRET_KEY = st.secrets["AWS_SECRET_KEY"]
BUCKET_NAME = "real-time-stock-data-username"

# ✅ AWS Region
AWS_REGION = "us-east-1"
