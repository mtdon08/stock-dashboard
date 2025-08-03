# 📊 Real-Time Stock Dashboard Project

## 🧭 Project Goal

Build a real-time stock trading dashboard with:

* Price & volume charting
* Sentiment analysis
* Automated data pipelines using Airflow
* Data storage in AWS S3 and Snowflake
* Transformations with dbt
* Visualization with Streamlit

---

## 💻 Tech Stack

| Layer          | Tools Used                                           |
| -------------- | ---------------------------------------------------- |
| Frontend       | Streamlit                                            |
| Ingestion      | Airflow, Python, yfinance                            |
| API Layer      | FastAPI, **Pydantic**, **REST API Design**           |
| Storage        | AWS S3                                               |
| Data Warehouse | Snowflake                                            |
| Transformation | dbt (dbt-core), Pandas                               |
| Database       | PostgreSQL, **SQLAlchemy**                           |
| Sentiment      | Finnhub API, VADER (optional)                        |
| Orchestration  | Airflow                                              |
| Security       | `.env`, `streamlit.secrets`, IAM                     |
| DevOps         | GitHub Actions, Docker (if applicable), Git          |

---

## 📅 Weekly Development Timeline (Weekend-Based)

### 🗓️ WEEK 1
#### ✅ Saturday (Progress Log)

- [ ] Review existing app code and add comments  
  **Notes:** Currently, only `AAPL` is supported. Need to extend script to handle multiple tickers (e.g., `NVDA`, `TMUS`).  
  Yahoo Finance API (free tier) does not support live intraday feeds — solution is to pull latest 5 days of data and update via cron job.

- [ ] Document current status in README (I'm doing this right now)

- [x] Confirm S3 bucket and verify file structure (e.g., `stock_data/{ticker}_stock_data.csv`)

- [ ] Improve error handling in Streamlit (e.g., when `df_filtered` is empty, show `st.warning`)

#### ✅ Sunday

* [ ] Integrate Finnhub sentiment API
* [ ] Display % bullish/bearish in dashboard

### 🗓️ WEEK 2

#### ✅ Saturday

* [ ] Set up Airflow locally via Docker
* [ ] Create DAG to fetch stock data and save CSV locally

#### ✅ Sunday

* [ ] Push daily CSVs to S3
* [ ] Organize folder structure in S3 by ticker/date

### 🗓️ WEEK 3

#### ✅ Saturday

* [ ] Create raw table in Snowflake
* [ ] Set up Snowflake external stage to S3 bucket

#### ✅ Sunday

* [ ] Write COPY INTO command to load CSVs into Snowflake

### 🗓️ WEEK 4

#### ✅ Saturday

* [ ] Initialize dbt project (`dbt init`)
* [ ] Create cleaned model for stock data

#### ✅ Sunday

* [ ] Add indicators: moving avg, RSI in dbt model
* [ ] Run dbt + validate in Snowflake

---

## 🧱 Features Being Built

* [x] Streamlit UI for stock price/volume
* [x] Date selection + timezone conversion
* [ ] Market sentiment insight
* [ ] Airflow ingestion pipeline
* [ ] S3 → Snowflake raw load
* [ ] dbt models for transformed data
* [ ] Dashboard upgrade: add indicators
* [ ] Secure secret management via `.env`
* [ ] 💡 Bonus (Optional, After Launch)
Set up logging instead of print() for future debugging.

Add a dropdown to select tickers dynamically (from a list of tickers in S3).

Build out more analytics or chart types (e.g., moving average, RSI, etc.)

---

## 🔒 Security Tips 

* NEVER commit credentials (AWS, Snowflake, API keys) to GitHub
* Use `.env` + `python-dotenv` or `streamlit.secrets` instead

---

## ✅ Next Steps

* Generate Airflow DAG + test locally
* Create S3 loader function
* Set up Snowflake stage + COPY commands
* Build dbt models and test with `dbt run`
* Expand dashboard visuals with Plotly or technical overlays

---

## 📘 Skills Inuse 

* Streamlit dashboards
* Workflow automation (Airflow)
* Cloud data storage (S3)
* Data warehousing (Snowflake)
* SQL transformation (dbt)
* API integration & NLP
* Project structure + security best practices

---
