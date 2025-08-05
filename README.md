# 📊 Real-Time Stock Dashboard Project

## 🧭 Project Goal

Build a real-time stock trading dashboard with:

- Price & volume charting  
- Sentiment analysis  
- Automated data pipelines using Airflow  
- Data storage in AWS S3 and Snowflake  
- Transformations with dbt  
- Visualization with Streamlit  

---

## 🧠 Architecture Overview
## 🧠 Architecture Overview

- **Frontend**: Streamlit user interface
- **API Layer**: FastAPI application with Pydantic for validation
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Cloud Storage**: AWS S3 for raw stock data
- **Data Warehouse**: Snowflake for centralized analytics
- **Transformation**: dbt for data modeling and enrichment
- **Orchestration**: Airflow for scheduled ingestion + pipeline automation

---

## 💻 Tech Stack

| Layer          | Tools Used                                           |
| -------------- | ---------------------------------------------------- |
| Frontend       | Streamlit                                            |
| Ingestion      | Airflow, Python, yfinance                            |
| API Layer      | FastAPI, Pydantic, REST API Design                   |
| Storage        | AWS S3                                               |
| Data Warehouse | Snowflake                                            |
| Transformation | dbt (dbt-core), Pandas                               |
| Database       | PostgreSQL, SQLAlchemy                               |
| Sentiment      | Finnhub API, VADER (optional)                        |
| Orchestration  | Airflow                                              |
| Security       | `.env`, `streamlit.secrets`, IAM                     |
| DevOps         | GitHub Actions, Docker, Git                          |

---

## 🧱 Features Being Built

- [x] Streamlit UI for stock price/volume  
- [x] Date selection + timezone conversion  
- [ ] Market sentiment insight  
- [ ] Airflow ingestion pipeline  
- [ ] S3 → Snowflake raw load  
- [ ] dbt models for transformed data  
- [ ] Dashboard upgrade: add indicators  
- [ ] Secure secret management via `.env`  
- 💡 Bonus (Post-Launch):
  - Logging for debugging  
  - Ticker dropdown from S3  
  - Moving average, RSI analytics  

---

## 🔍 Notable Implementations

- **SQLAlchemy**: Used to model PostgreSQL tables and abstract DB logic in OOP format.  
- **Pydantic**: Validates request and response schemas for FastAPI endpoints.  
- **REST API Design**: Created endpoints for price retrieval, sentiment scoring, and ticker filtering.  
- **OOP Structure**: Modular Python classes for fetchers, cleaners, uploaders, and orchestrators.  
- **Airflow DAGs**: Automates fetching, storing to S3, and loading into Snowflake.  
- **dbt Models**: Used for cleaning and transforming raw stock data before analytics.  

---

## 📡 FastAPI Endpoints (Planned)

| Method | Endpoint              | Description                          |
|--------|-----------------------|--------------------------------------|
| GET    | `/api/price/{ticker}` | Returns recent stock price data      |
| POST   | `/api/analyze/`       | Accepts ticker/date, returns sentiment |
| GET    | `/api/indicators/`    | Returns MA/RSI analytics             |

---

## 📘 Skills in Use

- Streamlit dashboards  
- Workflow automation (Airflow)  
- Cloud data storage (S3)  
- Data warehousing (Snowflake)  
- SQL transformation (dbt)  
- API integration & NLP  
- Project structure + security best practices  
- Object-Oriented Python development  
- SQLAlchemy ORM and Pydantic schema validation  

---

## 📚 What I Learned

- Best practices for modular OOP in data pipelines  
- How to integrate Airflow for scheduled ingestion and orchestration  
- Secure handling of API keys and cloud credentials  
- Tradeoffs between local processing vs. cloud-native Snowflake loading  
- Designing maintainable, testable FastAPI services  

---

## 🔒 Security Tips

- Never commit credentials (AWS, Snowflake, API keys)  
- Use `.env` + `python-dotenv` or `streamlit.secrets` for secret management  

---

## ✅ Next Steps

- Finalize Airflow DAG + test  
- Create S3 uploader module  
- Configure Snowflake stage + COPY commands  
- Develop and run dbt models  
- Enhance dashboard visuals with indicators (MA, RSI, etc.)
