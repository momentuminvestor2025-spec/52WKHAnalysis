# NSE Streamlit Deployment Guide

## 1. Prerequisites
- GitHub account
- Streamlit Community Cloud account
- Python 3.11 or 3.12 installed locally
- PostgreSQL database, or Supabase PostgreSQL if you want managed hosting

## 2. Local project setup
1. Unzip the project.
2. Open terminal in the project root.
3. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
4. Activate it:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Create local secrets file:
   - Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml`
   - Fill in real values for `DATABASE_URL`

## 3. Run locally
```bash
streamlit run app.py
```
Open the local URL shown in the terminal, usually `http://localhost:8501`.

## 4. Create the database
1. Create a PostgreSQL database.
2. Open the `sql/schema.sql` file.
3. Run the script in PostgreSQL using psql, DBeaver, pgAdmin, or Supabase SQL Editor.
4. Confirm that all five tables are created.

## 5. Push to GitHub
1. Create a new GitHub repository.
2. Initialize git in the project folder:
   ```bash
   git init
   git add .
   git commit -m "Initial NSE Streamlit dashboard"
   ```
3. Add the GitHub remote:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git branch -M main
   git push -u origin main
   ```

## 6. Deploy to Streamlit Community Cloud
1. Go to https://share.streamlit.io/
2. Click **Create app**.
3. Choose your GitHub repository.
4. Branch: `main`
5. Main file path: `app.py`
6. Click **Advanced settings** and add secrets:
   ```toml
   DATABASE_URL="postgresql://user:password@host:5432/dbname"
   NSE_USER_AGENT="Mozilla/5.0"
   APP_ENV="production"
   ```
7. Click **Deploy**.

## 7. Auto deployment flow
- Every push to the selected branch triggers a fresh deployment.
- Use pull requests for controlled releases.
- Merge to `main` only after validation.

## 8. Recommended production hardening
- Replace sample data with database-backed queries.
- Add SQLAlchemy engine and repository layer.
- Add scraper scheduling outside Streamlit using GitHub Actions, cron jobs, or Render jobs.
- Add holiday calendar logic for NSE holidays.
- Store logs centrally.
- Add Playwright fallback only if NSE blocks requests-based scraping.

## 9. Suggested GitHub Actions scraper job
Use a separate scheduled workflow to scrape NSE once daily and write into PostgreSQL. Example trigger:
```yaml
on:
  schedule:
    - cron: '10 4 * * 1-5'
```
This runs at 09:40 IST during weekdays after UTC conversion.

## 10. Validation checklist before production
- App loads on desktop and mobile.
- Secrets are configured in Streamlit Cloud.
- Database schema is applied.
- Live market badge changes correctly in IST.
- TradingView links open in new tab.
- No duplicate rows for same symbol and trade date.
- Logs capture scraper failures and retries.
