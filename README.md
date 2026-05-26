# NSE Stock Analytics Terminal

Production-ready Streamlit starter for NSE India scanner analytics, historical tracking, overlap detection, and live market monitoring.

## Features
- NSE 52-week high scanner tab
- Historical symbol analytics tab
- Most active equities with overlap analytics
- Live market status badge using IST logic
- Dark institutional trading-dashboard UI
- Streamlit Cloud-ready structure
- PostgreSQL-first schema with SQLite fallback path

## Project structure
```text
app.py
components/
services/
db/
sql/
.streamlit/
requirements.txt
packages.txt
README.md
```

## Local run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Environment
Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` for local testing.

## Streamlit Cloud deployment
1. Push this project to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Create a new app and select the repository.
4. Set main file path to `app.py`.
5. Add secrets from `.streamlit/secrets.toml.example` in the Streamlit Cloud Secrets UI.
6. Deploy.
